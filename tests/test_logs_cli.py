from __future__ import annotations

import importlib.util
import argparse
from io import StringIO
import json
from pathlib import Path
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("logs_cli", ROOT / "scripts" / "logs.py")
assert SPEC is not None and SPEC.loader is not None
logs_cli = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(logs_cli)


CATEGORIES = [
    "research",
    "experiment",
    "source",
    "code",
    "data",
    "documentation",
    "governance",
    "maintenance",
]


def run_git(root: Path, *args: str) -> str:
    return subprocess.run(
        ["git", *args],
        cwd=root,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
    ).stdout.strip()


def write_policy(root: Path, boundary: str) -> None:
    path = root / "logs" / "policy.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(
            {
                "schema_version": 1,
                "entry_schema_version": 1,
                "enforcement_after": boundary,
                "entry_root": "logs/members",
                "categories": CATEGORIES,
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )


def valid_entry(member: str = "robert", summary: str = "Record a concrete change") -> tuple[str, str]:
    path = f"logs/members/{member}/2026-08/20260814T082030Z-record-change.md"
    text = f"""---
schema_version: 1
member_id: {member}
timestamp: 2026-08-14T08:20:30Z
category: governance
summary: {summary}
supersedes: NONE
---

## Work completed

- Added a deterministic activity-log gate.

## Research or decision impact

- No scientific conclusion changed; repository accountability changed.

## Verification

- Unit test passed.

## Follow-ups

- None.
"""
    return path, text


def init_repo(root: Path) -> str:
    run_git(root, "init")
    run_git(root, "config", "user.name", "Test User")
    run_git(root, "config", "user.email", "test@example.invalid")
    write_policy(root, "0" * 40)
    (root / "README.md").write_text("base\n", encoding="utf-8")
    (root / "logs" / "members").mkdir(parents=True)
    run_git(root, "add", ".")
    run_git(root, "commit", "-m", "base")
    return run_git(root, "rev-parse", "HEAD")


class EntryValidationTests(unittest.TestCase):
    def test_valid_entry_matches_real_policy(self) -> None:
        policy = logs_cli.load_policy(ROOT)
        path, text = valid_entry()
        self.assertEqual([], logs_cli.validate_entry(path, text, policy))

    def test_member_directory_must_match_front_matter(self) -> None:
        policy = logs_cli.load_policy(ROOT)
        path, text = valid_entry(member="alice")
        text = text.replace("member_id: alice", "member_id: bob")
        errors = logs_cli.validate_entry(path, text, policy)
        self.assertIn("member_id does not match the member directory", errors)

    def test_placeholder_is_rejected(self) -> None:
        policy = logs_cli.load_policy(ROOT)
        path, text = valid_entry()
        text = text.replace("- Unit test passed.", "- TODO")
        errors = logs_cli.validate_entry(path, text, policy)
        self.assertTrue(any("placeholder" in error for error in errors))


class StagedGateTests(unittest.TestCase):
    def test_substantive_change_without_log_fails(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            init_repo(root)
            run_git(root, "config", "--local", "research.memberId", "robert")
            (root / "README.md").write_text("changed\n", encoding="utf-8")
            run_git(root, "add", "README.md")
            out, err = StringIO(), StringIO()
            result = logs_cli.run_check_staged(root, out, err)
            self.assertEqual(1, result)
            self.assertIn("missing member log", err.getvalue())

    def test_substantive_change_with_matching_log_passes(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            init_repo(root)
            run_git(root, "config", "--local", "research.memberId", "robert")
            (root / "README.md").write_text("changed\n", encoding="utf-8")
            path, text = valid_entry()
            entry = root / path
            entry.parent.mkdir(parents=True, exist_ok=True)
            entry.write_text(text, encoding="utf-8")
            run_git(root, "add", "README.md", path)
            out, err = StringIO(), StringIO()
            result = logs_cli.run_check_staged(root, out, err)
            self.assertEqual(0, result, err.getvalue())

    def test_staged_log_must_match_local_member(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            init_repo(root)
            run_git(root, "config", "--local", "research.memberId", "alice")
            (root / "README.md").write_text("changed\n", encoding="utf-8")
            path, text = valid_entry(member="robert")
            entry = root / path
            entry.parent.mkdir(parents=True, exist_ok=True)
            entry.write_text(text, encoding="utf-8")
            run_git(root, "add", "README.md", path)
            out, err = StringIO(), StringIO()
            result = logs_cli.run_check_staged(root, out, err)
            self.assertEqual(1, result)
            self.assertIn("does not match local member=alice", err.getvalue())

    def test_existing_log_is_append_only(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            init_repo(root)
            run_git(root, "config", "--local", "research.memberId", "robert")
            path, text = valid_entry()
            entry = root / path
            entry.parent.mkdir(parents=True, exist_ok=True)
            entry.write_text(text, encoding="utf-8")
            run_git(root, "add", path)
            run_git(root, "commit", "-m", "add historical log")
            entry.write_text(text.replace("Unit test passed", "Unit tests passed"), encoding="utf-8")
            run_git(root, "add", path)
            out, err = StringIO(), StringIO()
            result = logs_cli.run_check_staged(root, out, err)
            self.assertEqual(1, result)
            self.assertIn("append-only violation", err.getvalue())


class HistoryGateTests(unittest.TestCase):
    def test_history_gate_reads_utf8_entries(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            boundary = init_repo(root)
            write_policy(root, boundary)
            path, text = valid_entry(summary="记录可审计的研究变更")
            entry = root / path
            entry.parent.mkdir(parents=True, exist_ok=True)
            entry.write_text(text, encoding="utf-8")
            run_git(root, "add", "logs/policy.json", path)
            run_git(root, "commit", "-m", "add UTF-8 activity log")

            out, err = StringIO(), StringIO()
            result = logs_cli.run_check_history(root, out, err)

            self.assertEqual(0, result, err.getvalue())

    def test_history_gate_finds_commit_without_log_after_boundary(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            boundary = init_repo(root)
            write_policy(root, boundary)
            path, text = valid_entry()
            entry = root / path
            entry.parent.mkdir(parents=True, exist_ok=True)
            entry.write_text(text, encoding="utf-8")
            run_git(root, "add", "logs/policy.json", path)
            run_git(root, "commit", "-m", "enable activity logs")
            (root / "README.md").write_text("unlogged\n", encoding="utf-8")
            run_git(root, "add", "README.md")
            run_git(root, "commit", "-m", "unlogged change")

            out, err = StringIO(), StringIO()
            result = logs_cli.run_check_history(root, out, err)

            self.assertEqual(1, result)
            self.assertIn("missing member log", err.getvalue())


class NewEntryTests(unittest.TestCase):
    def test_new_command_creates_a_complete_valid_entry(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            init_repo(root)
            run_git(root, "config", "--local", "research.memberId", "robert")
            args = argparse.Namespace(
                category="governance",
                summary="Create a complete activity log",
                slug="complete-activity-log",
                work=["Created the entry."],
                impact=["No scientific conclusion changed."],
                verification=["Unit test exercised the command."],
                follow_up=["None."],
                supersedes=None,
            )
            out, err = StringIO(), StringIO()

            result = logs_cli.run_new(root, args, out, err)

            self.assertEqual(0, result, err.getvalue())
            entries = list((root / "logs" / "members" / "robert").rglob("*.md"))
            self.assertEqual(1, len(entries))
            policy = logs_cli.load_policy(root)
            relative = entries[0].relative_to(root).as_posix()
            self.assertEqual(
                [],
                logs_cli.validate_entry(relative, entries[0].read_text(encoding="utf-8"), policy),
            )
            (root / ".gitignore").write_text(".DS_Store\n", encoding="utf-8")
            (root / "logs" / "members" / ".DS_Store").write_bytes(b"\xffignored")
            validate_out, validate_err = StringIO(), StringIO()
            self.assertEqual(
                0,
                logs_cli.run_validate(root, validate_out, validate_err),
                validate_err.getvalue(),
            )


if __name__ == "__main__":
    unittest.main()
