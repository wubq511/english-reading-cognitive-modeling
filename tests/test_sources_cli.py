from __future__ import annotations

import hashlib
import importlib.util
from io import StringIO
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("sources_cli", ROOT / "scripts" / "sources.py")
assert SPEC is not None and SPEC.loader is not None
sources_cli = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(sources_cli)


def source_record(source_id: str, relative_path: str, payload: bytes) -> dict:
    return {
        "id": source_id,
        "asset_type": "PAPER",
        "media_type": "application/pdf",
        "title": f"Source {source_id}",
        "doi": None,
        "required": True,
        "acquisition_status": "UNKNOWN",
        "source_url": None,
        "download_url": None,
        "redistribution_status": "UNKNOWN",
        "local_path": relative_path,
        "sha256": hashlib.sha256(payload).hexdigest(),
    }


def catalog(*records: dict) -> dict:
    return {
        "schema_version": 2,
        "source_count": len(records),
        "sources": list(records),
    }


class CatalogTests(unittest.TestCase):
    def test_real_catalog_loads_with_stdlib_subset_and_doctor_passes(self) -> None:
        data = sources_cli.load_catalog(ROOT / "sources" / "catalog.yaml")
        stdout, stderr = StringIO(), StringIO()
        result = sources_cli.run_doctor(data, ROOT, stdout, stderr)
        self.assertEqual(result, 0, stderr.getvalue())
        self.assertIn(f"checked={data['source_count']}", stdout.getvalue())

    def test_real_catalog_matches_public_checksum_manifest(self) -> None:
        data = sources_cli.load_catalog(ROOT / "sources" / "catalog.yaml")
        stdout, stderr = StringIO(), StringIO()
        result = sources_cli.run_catalog_check(
            data,
            ROOT,
            ROOT / "sources" / "checksums.sha256",
            stdout,
            stderr,
        )
        self.assertEqual(result, 0, stderr.getvalue())
        self.assertIn(f"checked={data['source_count']}", stdout.getvalue())

    def test_catalog_check_rejects_checksum_drift(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            payload = b"%PDF-1.4\nfixture"
            data = catalog(source_record("P1", "sources/library/p1.pdf", payload))
            manifest = root / "checksums.sha256"
            manifest.write_text(
                f"{'0' * 64}  sources/library/p1.pdf\n", encoding="utf-8"
            )
            stdout, stderr = StringIO(), StringIO()
            result = sources_cli.run_catalog_check(
                data, root, manifest, stdout, stderr
            )
            self.assertEqual(result, 1)
            self.assertIn("checksum differs", stderr.getvalue())

    def test_duplicate_id_is_schema_error(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            payload = b"%PDF-1.4\nfixture"
            record = source_record("P1", "sources/library/p1.pdf", payload)
            errors = sources_cli.validate_schema(catalog(record, dict(record)), root)
            self.assertTrue(any("duplicate id" in error for error in errors))

    def test_unsupported_yaml_without_pyyaml_has_clear_dependency_error(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "catalog.yaml"
            path.write_text("schema_version: 2\nsource_count: 0\ncustom: true\n")
            real_import = __import__

            def import_without_yaml(name, *args, **kwargs):
                if name == "yaml":
                    raise ModuleNotFoundError("blocked for test")
                return real_import(name, *args, **kwargs)

            with patch("builtins.__import__", side_effect=import_without_yaml):
                with self.assertRaisesRegex(
                    sources_cli.CatalogLoadError, "PyYAML is not installed"
                ):
                    sources_cli.load_catalog(path)

    def test_missing_required_source_fails_with_manual_action(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            payload = b"%PDF-1.4\nfixture"
            data = catalog(source_record("P1", "sources/library/p1.pdf", payload))
            stdout, stderr = StringIO(), StringIO()
            result = sources_cli.run_doctor(data, root, stdout, stderr)
            self.assertEqual(result, 1)
            detail = stderr.getvalue()
            self.assertIn("[MISSING]", detail)
            self.assertIn("id=P1", detail)
            self.assertIn("doi=NONE", detail)
            self.assertIn("source_url=NONE", detail)
            self.assertIn("tmp/pdfs/", detail)
            self.assertIn("scripts/sources inbox", detail)

    def test_invalid_existing_source_action_preserves_provenance(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            payload = b"%PDF-1.4\nexpected"
            target = root / "sources" / "library" / "p1.pdf"
            target.parent.mkdir(parents=True)
            target.write_bytes(b"not a PDF")
            data = catalog(source_record("P1", "sources/library/p1.pdf", payload))
            stdout, stderr = StringIO(), StringIO()
            result = sources_cli.run_doctor(data, root, stdout, stderr)
            self.assertEqual(result, 1)
            self.assertIn("move the unexpected target aside", stderr.getvalue())


class ImportTests(unittest.TestCase):
    def test_import_verifies_and_atomically_places_pdf(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            payload = b"%PDF-1.4\nverified fixture"
            source = root / "incoming.pdf"
            source.write_bytes(payload)
            data = catalog(source_record("P1", "sources/library/p1.pdf", payload))
            stdout, stderr = StringIO(), StringIO()
            result = sources_cli.run_import(data, root, "P1", source, stdout, stderr)
            self.assertEqual(result, 0, stderr.getvalue())
            self.assertEqual(
                (root / "sources" / "library" / "p1.pdf").read_bytes(), payload
            )
            self.assertIn("INSTALLED", stdout.getvalue())

    def test_import_rejects_unexpected_hash(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            expected = b"%PDF-1.4\nexpected"
            source = root / "incoming.pdf"
            source.write_bytes(b"%PDF-1.4\nwrong")
            data = catalog(source_record("P1", "sources/library/p1.pdf", expected))
            stdout, stderr = StringIO(), StringIO()
            result = sources_cli.run_import(data, root, "P1", source, stdout, stderr)
            self.assertEqual(result, 1)
            self.assertFalse((root / "sources" / "library" / "p1.pdf").exists())
            self.assertIn("temporary file validation failed", stderr.getvalue())

    def test_import_never_overwrites_existing_different_content(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            target = root / "sources" / "library" / "p1.pdf"
            target.parent.mkdir(parents=True)
            target.write_bytes(b"%PDF-1.4\nexisting wrong file")
            expected = b"%PDF-1.4\nexpected"
            source = root / "incoming.pdf"
            source.write_bytes(expected)
            data = catalog(source_record("P1", "sources/library/p1.pdf", expected))
            stdout, stderr = StringIO(), StringIO()
            result = sources_cli.run_import(data, root, "P1", source, stdout, stderr)
            self.assertEqual(result, 1)
            self.assertEqual(target.read_bytes(), b"%PDF-1.4\nexisting wrong file")
            self.assertIn("IMPORT_REFUSED", stderr.getvalue())


class InboxTests(unittest.TestCase):
    def test_missing_inbox_is_created_as_the_standard_drop_location(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            inbox = root / "tmp" / "pdfs"
            payload = b"%PDF-1.4\nexpected"
            data = catalog(
                source_record("P1", "sources/library/papers/p1.pdf", payload)
            )
            stdout, stderr = StringIO(), StringIO()

            result = sources_cli.run_inbox(data, root, inbox, stdout, stderr)

            self.assertEqual(result, 0, stderr.getvalue())
            self.assertTrue(inbox.is_dir())
            self.assertIn("created=", stdout.getvalue())

    def test_inbox_imports_hash_match_then_deletes_verified_input(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            inbox = root / "tmp" / "pdfs"
            inbox.mkdir(parents=True)
            payload = b"%PDF-1.4\nverified inbox fixture"
            source_file = inbox / "human-filename.pdf"
            source_file.write_bytes(payload)
            data = catalog(
                source_record("P1", "sources/library/papers/p1.pdf", payload)
            )
            stdout, stderr = StringIO(), StringIO()

            result = sources_cli.run_inbox(data, root, inbox, stdout, stderr)

            self.assertEqual(result, 0, stderr.getvalue())
            self.assertFalse(source_file.exists())
            self.assertEqual(
                (root / "sources" / "library" / "papers" / "p1.pdf").read_bytes(),
                payload,
            )
            self.assertIn("imported=1", stdout.getvalue())
            self.assertIn("cleaned=1", stdout.getvalue())

    def test_inbox_unknown_hash_is_preserved_for_agent_review(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            inbox = root / "tmp" / "pdfs"
            inbox.mkdir(parents=True)
            source_file = inbox / "new-source.pdf"
            source_file.write_bytes(b"%PDF-1.4\nunknown")
            expected = b"%PDF-1.4\nexpected"
            data = catalog(
                source_record("P1", "sources/library/papers/p1.pdf", expected)
            )
            stdout, stderr = StringIO(), StringIO()

            result = sources_cli.run_inbox(data, root, inbox, stdout, stderr)

            self.assertEqual(result, 1)
            self.assertTrue(source_file.exists())
            self.assertIn("INBOX_REVIEW_REQUIRED", stderr.getvalue())
            self.assertIn("update_catalog", stderr.getvalue())

    def test_inbox_removes_exact_duplicate_after_target_verification(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            inbox = root / "tmp" / "pdfs"
            inbox.mkdir(parents=True)
            payload = b"%PDF-1.4\nalready installed"
            source_file = inbox / "duplicate.pdf"
            source_file.write_bytes(payload)
            target = root / "sources" / "library" / "papers" / "p1.pdf"
            target.parent.mkdir(parents=True)
            target.write_bytes(payload)
            data = catalog(
                source_record("P1", "sources/library/papers/p1.pdf", payload)
            )
            stdout, stderr = StringIO(), StringIO()

            result = sources_cli.run_inbox(data, root, inbox, stdout, stderr)

            self.assertEqual(result, 0, stderr.getvalue())
            self.assertFalse(source_file.exists())
            self.assertEqual(target.read_bytes(), payload)
            self.assertIn("cleaned=1", stdout.getvalue())


class SyncTests(unittest.TestCase):
    def test_unknown_rights_produces_manual_list_and_nonzero_exit(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            payload = b"%PDF-1.4\nfixture"
            data = catalog(source_record("P1", "sources/library/p1.pdf", payload))
            stdout, stderr = StringIO(), StringIO()
            result = sources_cli.run_sync(data, root, stdout, stderr)
            self.assertEqual(result, 1)
            detail = stderr.getvalue()
            self.assertIn("MANUAL_REQUIRED", detail)
            self.assertIn("redistribution_status=UNKNOWN", detail)
            self.assertIn("acquisition_status=UNKNOWN", detail)
            self.assertIn("manual=1", detail)


if __name__ == "__main__":
    unittest.main()
