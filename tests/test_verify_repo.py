from pathlib import Path
import importlib.util
import unittest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("verify_repo", ROOT / "scripts" / "verify_repo.py")
VERIFY = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(VERIFY)


class VerifyRepoTests(unittest.TestCase):
    def test_local_markdown_links_resolve(self):
        self.assertEqual([], VERIFY.check_links())

    def test_no_stale_current_paths(self):
        self.assertEqual([], VERIFY.check_stale_current_paths())

    def test_raw_manifest_matches(self):
        self.assertEqual([], VERIFY.check_manifest("reports/provenance/RAW_SOURCE_MANIFEST.sha256"))

    def test_public_manifest_formats_are_valid(self):
        self.assertEqual(
            [],
            VERIFY.check_manifest_format("reports/provenance/RAW_SOURCE_MANIFEST.sha256"),
        )
        self.assertEqual([], VERIFY.check_manifest_format("papers/checksums.sha256"))

    def test_paper_manifest_matches(self):
        self.assertEqual([], VERIFY.check_manifest("papers/checksums.sha256"))

    def test_manifest_counts_are_derived_from_current_files(self):
        self.assertEqual(
            25,
            VERIFY.manifest_entry_count("reports/provenance/RAW_SOURCE_MANIFEST.sha256"),
        )
        self.assertGreaterEqual(
            VERIFY.manifest_entry_count("papers/checksums.sha256"),
            74,
        )


if __name__ == "__main__":
    unittest.main()
