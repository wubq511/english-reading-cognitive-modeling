from pathlib import Path
import importlib.util
import tempfile
import unittest
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("skills_cli", ROOT / "scripts" / "skills.py")
SKILLS = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(SKILLS)


class SkillsCliTests(unittest.TestCase):
    def test_expected_repository_skills_are_present(self):
        names = SKILLS.expected_skills()
        self.assertEqual(13, len(names))
        self.assertTrue(SKILLS.USER_INVOKED.issubset(set(names)))

    def test_skill_sources_and_invocation_policies_are_valid(self):
        self.assertEqual([], SKILLS.validate_skill_sources())

    def test_claude_mapping_git_boundary_is_valid(self):
        self.assertEqual([], SKILLS.validate_claude_mapping_boundary())

    def test_claude_mappings_resolve_to_physical_skills(self):
        self.assertEqual([], SKILLS.doctor())

    def test_label_manifest_is_valid(self):
        self.assertEqual([], SKILLS.validate_label_manifest())

    def test_relative_mapping_target_is_platform_neutral(self):
        self.assertEqual(
            "../../.agents/skills/wayfinder",
            SKILLS.relative_target("wayfinder"),
        )

    def test_git_symlink_placeholder_is_replaceable(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "wayfinder"
            expected = SKILLS.relative_target("wayfinder")
            path.write_text(expected, encoding="utf-8")
            self.assertTrue(SKILLS.is_placeholder(path, expected))
            SKILLS.remove_replaceable_mapping(path, expected)
            self.assertFalse(path.exists())

    def test_unknown_directory_is_never_replaced(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "wayfinder"
            path.mkdir()
            with self.assertRaises(RuntimeError):
                SKILLS.remove_replaceable_mapping(path, SKILLS.relative_target("wayfinder"))

    def test_windows_mapping_uses_non_admin_directory_junction(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            link = root / "claude" / "wayfinder"
            target = root / "agents" / "wayfinder"
            with mock.patch.object(SKILLS.subprocess, "run") as run:
                run.return_value.returncode = 0
                run.return_value.stdout = "Junction created"
                SKILLS.create_mapping(
                    link,
                    target,
                    SKILLS.relative_target("wayfinder"),
                    platform="nt",
                )
            command = run.call_args.args[0]
            environment = run.call_args.kwargs["env"]
            self.assertEqual("powershell.exe", command[0])
            self.assertIn("New-Item -ItemType Junction", command[-1])
            self.assertNotIn(str(link), command[-1])
            self.assertNotIn(str(target), command[-1])
            self.assertEqual(str(link), environment["PROJECT_SKILL_LINK"])
            self.assertEqual(str(target), environment["PROJECT_SKILL_TARGET"])


if __name__ == "__main__":
    unittest.main()
