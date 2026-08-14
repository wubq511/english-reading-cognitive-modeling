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
        self.assertEqual([], VERIFY.check_manifest_format("sources/checksums.sha256"))

    def test_source_manifest_matches(self):
        self.assertEqual([], VERIFY.check_manifest("sources/checksums.sha256"))

    def test_every_cataloged_source_is_in_crosswalk(self):
        self.assertEqual([], VERIFY.check_source_crosswalk())

    def test_agent_rule_symlink_is_single_source(self):
        self.assertEqual([], VERIFY.check_agent_rule_link())

    def test_source_hooks_and_bootstrap_are_present(self):
        self.assertEqual([], VERIFY.check_hook_files())

    def test_bootstrap_is_configured_for_this_clone(self):
        self.assertEqual([], VERIFY.check_bootstrap_configuration())

    def test_research_workspace_skeleton_is_complete(self):
        self.assertEqual([], VERIFY.check_workspace_skeleton())

    def test_source_inbox_has_no_unresolved_files(self):
        self.assertEqual([], VERIFY.check_inbox_empty())

    def test_dynamic_state_has_one_owner(self):
        self.assertEqual([], VERIFY.check_knowledge_ownership())

    def test_manifest_counts_are_derived_from_current_files(self):
        self.assertEqual(
            25,
            VERIFY.manifest_entry_count("reports/provenance/RAW_SOURCE_MANIFEST.sha256"),
        )
        self.assertGreaterEqual(
            VERIFY.manifest_entry_count("sources/checksums.sha256"),
            79,
        )


if __name__ == "__main__":
    unittest.main()
