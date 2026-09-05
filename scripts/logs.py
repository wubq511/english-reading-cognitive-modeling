#!/usr/bin/env python3
"""Create and enforce append-only member activity logs."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import re
import subprocess
import sys
from typing import TextIO


ROOT = Path(__file__).resolve().parents[1]
POLICY_PATH = Path("logs/policy.json")
MEMBER_ID_RE = re.compile(r"^[a-z0-9](?:[a-z0-9-]{0,38}[a-z0-9])?$")
ENTRY_PATH_RE = re.compile(
    r"^logs/members/(?P<member>[a-z0-9](?:[a-z0-9-]{0,38}[a-z0-9])?)/"
    r"(?P<month>\d{4}-\d{2})/"
    r"(?P<stamp>\d{8}T\d{6}Z)-"
    r"(?P<slug>[a-z0-9](?:[a-z0-9-]{0,62}[a-z0-9])?)\.md$"
)
TIMESTAMP_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")
REQUIRED_FIELDS = (
    "schema_version",
    "member_id",
    "timestamp",
    "category",
    "summary",
    "supersedes",
)
REQUIRED_SECTIONS = (
    "## Work completed",
    "## Research or decision impact",
    "## Verification",
    "## Follow-ups",
)
PLACEHOLDER_MARKERS = ("<!--", "<describe", "<replace", "TODO", "TBD")


class LogPolicyError(RuntimeError):
    """Raised when the tracked activity-log policy is invalid."""


def git(root: Path, *args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(
        ["git", *args],
        cwd=root,
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if check and result.returncode:
        detail = result.stderr.strip() or result.stdout.strip() or "unknown git error"
        raise LogPolicyError(f"git {' '.join(args)} failed: {detail}")
    return result


def load_policy(root: Path) -> dict:
    path = root / POLICY_PATH
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise LogPolicyError(f"cannot load {POLICY_PATH}: {exc}") from exc

    errors: list[str] = []
    if data.get("schema_version") != 1:
        errors.append("schema_version must be 1")
    if data.get("entry_schema_version") != 1:
        errors.append("entry_schema_version must be 1")
    boundary = data.get("enforcement_after")
    if not isinstance(boundary, str) or not re.fullmatch(r"[0-9a-f]{40}", boundary):
        errors.append("enforcement_after must be a full lowercase commit SHA")
    categories = data.get("categories")
    if (
        not isinstance(categories, list)
        or not categories
        or any(not isinstance(item, str) or not re.fullmatch(r"[a-z][a-z-]*", item) for item in categories)
        or len(set(categories)) != len(categories)
    ):
        errors.append("categories must be a non-empty unique lowercase string list")
    if data.get("entry_root") != "logs/members":
        errors.append("entry_root must be logs/members")
    if errors:
        raise LogPolicyError("; ".join(errors))
    return data


def parse_front_matter(text: str) -> tuple[dict[str, str], int, list[str]]:
    lines = text.splitlines()
    errors: list[str] = []
    if not lines or lines[0] != "---":
        return {}, 0, ["missing opening front-matter delimiter"]
    try:
        closing = lines.index("---", 1)
    except ValueError:
        return {}, 0, ["missing closing front-matter delimiter"]

    fields: dict[str, str] = {}
    order: list[str] = []
    for number, line in enumerate(lines[1:closing], start=2):
        if ":" not in line:
            errors.append(f"front matter line {number} must be key: value")
            continue
        key, value = line.split(":", 1)
        key, value = key.strip(), value.strip()
        if key in fields:
            errors.append(f"duplicate front-matter field {key}")
            continue
        fields[key] = value
        order.append(key)
    if tuple(order) != REQUIRED_FIELDS:
        errors.append(f"front-matter fields must appear exactly as: {', '.join(REQUIRED_FIELDS)}")
    return fields, closing, errors


def validate_entry(relative_path: str, text: str, policy: dict) -> list[str]:
    errors: list[str] = []
    match = ENTRY_PATH_RE.fullmatch(relative_path)
    if not match:
        return ["path does not match logs/members/<member-id>/YYYY-MM/<UTC>-<slug>.md"]

    fields, front_matter_end, front_matter_errors = parse_front_matter(text)
    errors.extend(front_matter_errors)
    if front_matter_errors:
        return errors

    member_id = fields["member_id"]
    timestamp = fields["timestamp"]
    if fields["schema_version"] != str(policy["entry_schema_version"]):
        errors.append("schema_version does not match logs/policy.json")
    if member_id != match.group("member"):
        errors.append("member_id does not match the member directory")
    if not MEMBER_ID_RE.fullmatch(member_id):
        errors.append("member_id is not a valid lowercase slug")

    parsed_timestamp: datetime | None = None
    if not TIMESTAMP_RE.fullmatch(timestamp):
        errors.append("timestamp must use UTC YYYY-MM-DDTHH:MM:SSZ")
    else:
        try:
            parsed_timestamp = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%SZ").replace(
                tzinfo=timezone.utc
            )
        except ValueError:
            errors.append("timestamp is not a real UTC date/time")
    if parsed_timestamp is not None:
        if parsed_timestamp.strftime("%Y-%m") != match.group("month"):
            errors.append("timestamp month does not match the month directory")
        if parsed_timestamp.strftime("%Y%m%dT%H%M%SZ") != match.group("stamp"):
            errors.append("timestamp does not match the filename")

    if fields["category"] not in policy["categories"]:
        errors.append(
            "category must be one of: " + ", ".join(policy["categories"])
        )
    summary = fields["summary"]
    if len(summary) < 8 or summary in {"-", "NONE", "None"}:
        errors.append("summary must be a concrete description of at least 8 characters")

    supersedes = fields["supersedes"]
    if supersedes != "NONE" and not ENTRY_PATH_RE.fullmatch(supersedes):
        errors.append("supersedes must be NONE or a canonical member-log path")

    body_lines = text.splitlines()[front_matter_end + 1 :]
    section_positions: list[int] = []
    for section in REQUIRED_SECTIONS:
        positions = [index for index, line in enumerate(body_lines) if line == section]
        if len(positions) != 1:
            errors.append(f"section must appear exactly once: {section}")
        else:
            section_positions.append(positions[0])
    if len(section_positions) == len(REQUIRED_SECTIONS):
        if section_positions != sorted(section_positions):
            errors.append("required sections are out of order")
        for index, (section, start) in enumerate(zip(REQUIRED_SECTIONS, section_positions)):
            end = section_positions[index + 1] if index + 1 < len(section_positions) else len(body_lines)
            content = [line.strip() for line in body_lines[start + 1 : end] if line.strip()]
            if not content or not any(line.startswith("- ") and len(line) > 2 for line in content):
                errors.append(f"section requires at least one concrete bullet: {section}")

    for marker in PLACEHOLDER_MARKERS:
        if marker.lower() in text.lower():
            errors.append(f"unresolved placeholder marker: {marker}")
    return errors


def configured_member(root: Path) -> str | None:
    result = git(root, "config", "--local", "--get", "research.memberId", check=False)
    member_id = result.stdout.strip() if result.returncode == 0 else ""
    return member_id or None


def staged_changes(root: Path) -> list[tuple[str, str]]:
    result = git(root, "diff", "--cached", "--name-status", "--no-renames")
    changes: list[tuple[str, str]] = []
    for line in result.stdout.splitlines():
        if not line:
            continue
        try:
            status, path = line.split("\t", 1)
        except ValueError as exc:
            raise LogPolicyError(f"cannot parse staged change: {line!r}") from exc
        changes.append((status, path))
    return changes


def commit_changes(root: Path, commit: str) -> list[tuple[str, str]]:
    result = git(
        root,
        "diff-tree",
        "--no-commit-id",
        "--name-status",
        "--no-renames",
        "-r",
        commit,
    )
    changes: list[tuple[str, str]] = []
    for line in result.stdout.splitlines():
        if not line:
            continue
        status, path = line.split("\t", 1)
        changes.append((status, path))
    return changes


def entry_paths(changes: list[tuple[str, str]]) -> list[tuple[str, str]]:
    return [(status, path) for status, path in changes if path.startswith("logs/members/")]


def validate_change_set(
    changes: list[tuple[str, str]],
    read_entry,
    policy: dict,
    expected_member: str | None,
    enforce_local_member: bool = False,
) -> list[str]:
    if not changes:
        return []
    errors: list[str] = []
    entries = entry_paths(changes)
    added_entries = [path for status, path in entries if status == "A"]
    non_entry_changes = [path for _, path in changes if not path.startswith("logs/members/")]

    for status, path in entries:
        if status != "A":
            errors.append(
                f"append-only violation status={status} path={path}; add a superseding entry instead"
            )
    if non_entry_changes and not added_entries:
        errors.append(
            "missing member log for substantive changes; run scripts/logs new and stage the entry"
        )
    if added_entries and enforce_local_member and expected_member is None:
        errors.append("member identity is unset; run scripts/logs init <member-id>")

    observed_members: set[str] = set()
    for path in added_entries:
        match = ENTRY_PATH_RE.fullmatch(path)
        if match:
            observed_members.add(match.group("member"))
        try:
            text = read_entry(path)
        except LogPolicyError as exc:
            errors.append(f"{path}: {exc}")
            continue
        for error in validate_entry(path, text, policy):
            errors.append(f"{path}: {error}")
    if enforce_local_member and len(observed_members) > 1:
        errors.append("one commit must have one accountable member directory")
    if (
        enforce_local_member
        and expected_member is not None
        and observed_members
        and observed_members != {expected_member}
    ):
        errors.append(
            f"staged log member={','.join(sorted(observed_members))} "
            f"does not match local member={expected_member}"
        )
    return errors


def print_errors(label: str, errors: list[str], err: TextIO) -> int:
    if not errors:
        return 0
    print(f"activity logs: FAIL check={label} errors={len(errors)}", file=err)
    for error in errors:
        print(f"- {error}", file=err)
    return 1


def run_init(root: Path, member_id: str, out: TextIO, err: TextIO) -> int:
    if not MEMBER_ID_RE.fullmatch(member_id):
        print(
            "activity logs: FAIL member-id must be a lowercase slug using a-z, 0-9 and internal hyphens",
            file=err,
        )
        return 1
    try:
        git(root, "config", "--local", "research.memberId", member_id)
    except LogPolicyError as exc:
        print(f"activity logs: FAIL {exc}", file=err)
        return 1
    print(f"activity logs: CONFIGURED member_id={member_id} scope=local-clone", file=out)
    return 0


def run_status(root: Path, out: TextIO, err: TextIO) -> int:
    member_id = configured_member(root)
    if member_id is None:
        print(
            'activity logs: SETUP_REQUIRED action="scripts/logs init <member-id>" '
            "before_first_commit",
            file=err,
        )
        return 1
    if not MEMBER_ID_RE.fullmatch(member_id):
        print(
            f"activity logs: FAIL invalid_local_member_id={member_id} "
            'action="scripts/logs init <member-id>"',
            file=err,
        )
        return 1
    print(f"activity logs: OK member_id={member_id}", file=out)
    return 0


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return (slug[:64].rstrip("-") or "change")


def bullets(values: list[str]) -> str:
    return "\n".join(f"- {value.strip()}" for value in values)


def run_new(root: Path, args: argparse.Namespace, out: TextIO, err: TextIO) -> int:
    try:
        policy = load_policy(root)
    except LogPolicyError as exc:
        print(f"activity logs: FAIL {exc}", file=err)
        return 1
    member_id = configured_member(root)
    if member_id is None or not MEMBER_ID_RE.fullmatch(member_id):
        print('activity logs: FAIL action="scripts/logs init <member-id>"', file=err)
        return 1
    if args.category not in policy["categories"]:
        print("activity logs: FAIL invalid category", file=err)
        return 1
    timestamp = datetime.now(timezone.utc).replace(microsecond=0)
    timestamp_text = timestamp.strftime("%Y-%m-%dT%H:%M:%SZ")
    stamp = timestamp.strftime("%Y%m%dT%H%M%SZ")
    slug = slugify(args.slug or args.summary)
    relative = Path("logs/members") / member_id / timestamp.strftime("%Y-%m") / f"{stamp}-{slug}.md"
    path = root / relative
    if path.exists():
        print(f"activity logs: FAIL collision={relative}", file=err)
        return 1
    supersedes = args.supersedes or "NONE"
    content = f"""---
schema_version: 1
member_id: {member_id}
timestamp: {timestamp_text}
category: {args.category}
summary: {args.summary.strip()}
supersedes: {supersedes}
---

## Work completed

{bullets(args.work)}

## Research or decision impact

{bullets(args.impact)}

## Verification

{bullets(args.verification)}

## Follow-ups

{bullets(args.follow_up or ["None."])}
"""
    validation_errors = validate_entry(relative.as_posix(), content, policy)
    if validation_errors:
        return print_errors("new", validation_errors, err)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print(
        f"activity logs: CREATED path={relative} action=review_then_git_add",
        file=out,
    )
    return 0


def run_validate(root: Path, out: TextIO, err: TextIO) -> int:
    try:
        policy = load_policy(root)
    except LogPolicyError as exc:
        return print_errors("validate", [str(exc)], err)
    entries_root = root / policy["entry_root"]
    errors: list[str] = []
    checked = 0
    if not entries_root.is_dir():
        errors.append(f"missing entry root: {policy['entry_root']}")
    else:
        candidates = git(
            root,
            "ls-files",
            "--cached",
            "--others",
            "--exclude-standard",
            "--",
            policy["entry_root"],
        ).stdout.splitlines()
        for relative in sorted(candidates):
            path = root / relative
            checked += 1
            try:
                text = path.read_text(encoding="utf-8")
            except (OSError, UnicodeDecodeError) as exc:
                errors.append(f"{relative}: cannot read UTF-8 Markdown: {exc}")
                continue
            for error in validate_entry(relative, text, policy):
                errors.append(f"{relative}: {error}")
    if print_errors("validate", errors, err):
        return 1
    print(f"activity logs: OK check=validate entries={checked}", file=out)
    return 0


def run_check_staged(root: Path, out: TextIO, err: TextIO) -> int:
    try:
        policy = load_policy(root)
        changes = staged_changes(root)
        member_id = configured_member(root)

        def read_entry(path: str) -> str:
            result = git(root, "show", f":{path}")
            return result.stdout

        errors = validate_change_set(
            changes,
            read_entry,
            policy,
            member_id,
            enforce_local_member=True,
        )
    except LogPolicyError as exc:
        errors = [str(exc)]
        changes = []
    if print_errors("staged", errors, err):
        return 1
    print(f"activity logs: OK check=staged changes={len(changes)}", file=out)
    return 0


def run_check_history(root: Path, out: TextIO, err: TextIO) -> int:
    try:
        policy = load_policy(root)
        boundary = policy["enforcement_after"]
        exists = git(root, "cat-file", "-e", f"{boundary}^{{commit}}", check=False)
        if exists.returncode:
            raise LogPolicyError(
                f"enforcement boundary {boundary} is unavailable; fetch full history"
            )
        ancestor = git(root, "merge-base", "--is-ancestor", boundary, "HEAD", check=False)
        if ancestor.returncode:
            raise LogPolicyError("HEAD does not descend from the activity-log enforcement boundary")
        commits = git(root, "rev-list", "--reverse", f"{boundary}..HEAD").stdout.splitlines()
        errors: list[str] = []
        checked = 0
        for commit in commits:
            parents = git(root, "show", "-s", "--format=%P", commit).stdout.split()
            if len(parents) > 1:
                continue
            checked += 1
            changes = commit_changes(root, commit)

            def read_entry(path: str, current_commit: str = commit) -> str:
                return git(root, "show", f"{current_commit}:{path}").stdout

            commit_errors = validate_change_set(
                changes, read_entry, policy, expected_member=None
            )
            for error in commit_errors:
                errors.append(f"commit={commit[:12]} {error}")
    except LogPolicyError as exc:
        errors = [str(exc)]
        checked = 0
    if print_errors("history", errors, err):
        return 1
    print(f"activity logs: OK check=history commits={checked}", file=out)
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    init_parser = subparsers.add_parser("init", help="bind this clone to a member ID")
    init_parser.add_argument("member_id")
    subparsers.add_parser("status", help="show this clone's member identity")
    new_parser = subparsers.add_parser("new", help="create one complete activity-log entry")
    new_parser.add_argument("--category", required=True)
    new_parser.add_argument("--summary", required=True)
    new_parser.add_argument("--slug")
    new_parser.add_argument("--work", action="append", required=True)
    new_parser.add_argument("--impact", action="append", required=True)
    new_parser.add_argument("--verification", action="append", required=True)
    new_parser.add_argument("--follow-up", action="append")
    new_parser.add_argument("--supersedes")
    subparsers.add_parser("validate", help="validate all working-tree member logs")
    subparsers.add_parser("check-staged", help="enforce the staged commit contract")
    subparsers.add_parser("check-history", help="enforce every commit after the boundary")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "init":
        return run_init(ROOT, args.member_id, sys.stdout, sys.stderr)
    if args.command == "status":
        return run_status(ROOT, sys.stdout, sys.stderr)
    if args.command == "new":
        return run_new(ROOT, args, sys.stdout, sys.stderr)
    if args.command == "validate":
        return run_validate(ROOT, sys.stdout, sys.stderr)
    if args.command == "check-staged":
        return run_check_staged(ROOT, sys.stdout, sys.stderr)
    if args.command == "check-history":
        return run_check_history(ROOT, sys.stdout, sys.stderr)
    raise AssertionError(f"unhandled command: {args.command}")


if __name__ == "__main__":
    raise SystemExit(main())
