from __future__ import annotations

import hashlib
import importlib.util
from io import StringIO
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("papers_cli", ROOT / "scripts" / "papers.py")
assert SPEC is not None and SPEC.loader is not None
papers_cli = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(papers_cli)


def paper_record(paper_id: str, relative_path: str, payload: bytes) -> dict:
    return {
        "id": paper_id,
        "title": f"Paper {paper_id}",
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
        "schema_version": 1,
        "paper_count": len(records),
        "papers": list(records),
    }


class CatalogTests(unittest.TestCase):
    def test_real_catalog_loads_with_stdlib_subset_and_doctor_passes(self) -> None:
        data = papers_cli.load_catalog(ROOT / "papers" / "catalog.yaml")
        stdout, stderr = StringIO(), StringIO()
        result = papers_cli.run_doctor(data, ROOT, stdout, stderr)
        self.assertEqual(result, 0, stderr.getvalue())
        self.assertIn(f"checked={data['paper_count']}", stdout.getvalue())

    def test_real_catalog_matches_public_checksum_manifest(self) -> None:
        data = papers_cli.load_catalog(ROOT / "papers" / "catalog.yaml")
        stdout, stderr = StringIO(), StringIO()
        result = papers_cli.run_catalog_check(
            data,
            ROOT,
            ROOT / "papers" / "checksums.sha256",
            stdout,
            stderr,
        )
        self.assertEqual(result, 0, stderr.getvalue())
        self.assertIn(f"checked={data['paper_count']}", stdout.getvalue())

    def test_catalog_check_rejects_checksum_drift(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            payload = b"%PDF-1.4\nfixture"
            data = catalog(paper_record("P1", "papers/p1.pdf", payload))
            manifest = root / "checksums.sha256"
            manifest.write_text(f"{'0' * 64}  papers/p1.pdf\n", encoding="utf-8")
            stdout, stderr = StringIO(), StringIO()
            result = papers_cli.run_catalog_check(
                data, root, manifest, stdout, stderr
            )
            self.assertEqual(result, 1)
            self.assertIn("checksum differs", stderr.getvalue())

    def test_duplicate_id_is_schema_error(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            payload = b"%PDF-1.4\nfixture"
            record = paper_record("P1", "papers/p1.pdf", payload)
            errors = papers_cli.validate_schema(catalog(record, dict(record)), root)
            self.assertTrue(any("duplicate id" in error for error in errors))

    def test_unsupported_yaml_without_pyyaml_has_clear_dependency_error(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "catalog.yaml"
            path.write_text("schema_version: 1\npaper_count: 0\ncustom: true\n")
            real_import = __import__

            def import_without_yaml(name, *args, **kwargs):
                if name == "yaml":
                    raise ModuleNotFoundError("blocked for test")
                return real_import(name, *args, **kwargs)

            with patch("builtins.__import__", side_effect=import_without_yaml):
                with self.assertRaisesRegex(
                    papers_cli.CatalogLoadError, "PyYAML is not installed"
                ):
                    papers_cli.load_catalog(path)

    def test_missing_required_paper_fails_with_manual_action(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            payload = b"%PDF-1.4\nfixture"
            data = catalog(paper_record("P1", "papers/p1.pdf", payload))
            stdout, stderr = StringIO(), StringIO()
            result = papers_cli.run_doctor(data, root, stdout, stderr)
            self.assertEqual(result, 1)
            detail = stderr.getvalue()
            self.assertIn("[MISSING]", detail)
            self.assertIn("id=P1", detail)
            self.assertIn("doi=NONE", detail)
            self.assertIn("source_url=NONE", detail)
            self.assertIn("scripts/papers import P1 FILE", detail)

    def test_invalid_existing_paper_action_preserves_provenance(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            payload = b"%PDF-1.4\nexpected"
            target = root / "papers" / "p1.pdf"
            target.parent.mkdir(parents=True)
            target.write_bytes(b"not a PDF")
            data = catalog(paper_record("P1", "papers/p1.pdf", payload))
            stdout, stderr = StringIO(), StringIO()
            result = papers_cli.run_doctor(data, root, stdout, stderr)
            self.assertEqual(result, 1)
            self.assertIn("move the unexpected target aside", stderr.getvalue())


class ImportTests(unittest.TestCase):
    def test_import_verifies_and_atomically_places_pdf(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            payload = b"%PDF-1.4\nverified fixture"
            source = root / "incoming.pdf"
            source.write_bytes(payload)
            data = catalog(paper_record("P1", "papers/p1.pdf", payload))
            stdout, stderr = StringIO(), StringIO()
            result = papers_cli.run_import(data, root, "P1", source, stdout, stderr)
            self.assertEqual(result, 0, stderr.getvalue())
            self.assertEqual((root / "papers" / "p1.pdf").read_bytes(), payload)
            self.assertIn("INSTALLED", stdout.getvalue())

    def test_import_rejects_unexpected_hash(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            expected = b"%PDF-1.4\nexpected"
            source = root / "incoming.pdf"
            source.write_bytes(b"%PDF-1.4\nwrong")
            data = catalog(paper_record("P1", "papers/p1.pdf", expected))
            stdout, stderr = StringIO(), StringIO()
            result = papers_cli.run_import(data, root, "P1", source, stdout, stderr)
            self.assertEqual(result, 1)
            self.assertFalse((root / "papers" / "p1.pdf").exists())
            self.assertIn("temporary file validation failed", stderr.getvalue())

    def test_import_never_overwrites_existing_different_content(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            target = root / "papers" / "p1.pdf"
            target.parent.mkdir(parents=True)
            target.write_bytes(b"%PDF-1.4\nexisting wrong file")
            expected = b"%PDF-1.4\nexpected"
            source = root / "incoming.pdf"
            source.write_bytes(expected)
            data = catalog(paper_record("P1", "papers/p1.pdf", expected))
            stdout, stderr = StringIO(), StringIO()
            result = papers_cli.run_import(data, root, "P1", source, stdout, stderr)
            self.assertEqual(result, 1)
            self.assertEqual(target.read_bytes(), b"%PDF-1.4\nexisting wrong file")
            self.assertIn("IMPORT_REFUSED", stderr.getvalue())


class SyncTests(unittest.TestCase):
    def test_unknown_rights_produces_manual_list_and_nonzero_exit(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            payload = b"%PDF-1.4\nfixture"
            data = catalog(paper_record("P1", "papers/p1.pdf", payload))
            stdout, stderr = StringIO(), StringIO()
            result = papers_cli.run_sync(data, root, stdout, stderr)
            self.assertEqual(result, 1)
            detail = stderr.getvalue()
            self.assertIn("MANUAL_REQUIRED", detail)
            self.assertIn("redistribution_status=UNKNOWN", detail)
            self.assertIn("acquisition_status=UNKNOWN", detail)
            self.assertIn("manual=1", detail)


if __name__ == "__main__":
    unittest.main()
