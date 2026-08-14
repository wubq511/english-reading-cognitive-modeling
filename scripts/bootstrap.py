#!/usr/bin/env python3
"""Cross-platform repository bootstrap shared by shell and Windows wrappers."""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
HOOKS_PATH = ".githooks"
REQUIRED_HOOKS = ("post-checkout", "post-merge", "pre-commit", "pre-push")


def run(command: list[str], *, quiet: bool = False) -> int:
    result = subprocess.run(
        command,
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE if quiet else None,
        stderr=subprocess.STDOUT if quiet else None,
        check=False,
    )
    return result.returncode


def git_output(args: list[str]) -> tuple[int, str]:
    result = subprocess.run(
        ["git", *args],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    return result.returncode, result.stdout.strip()


def check_hook_contract() -> list[str]:
    errors: list[str] = []
    code, configured = git_output(["config", "--local", "--get", "core.hooksPath"])
    if code or configured != HOOKS_PATH:
        errors.append(f"core.hooksPath={configured or 'UNSET'} expected={HOOKS_PATH}")
    for hook in REQUIRED_HOOKS:
        path = ROOT / HOOKS_PATH / hook
        if not path.is_file() or (os.name != "nt" and not os.access(path, os.X_OK)):
            errors.append(f"hook={HOOKS_PATH}/{hook} reason=missing_or_not_executable")
    return errors


def python_tool(name: str, *args: str) -> list[str]:
    return [sys.executable, str(SCRIPTS / f"{name}.py"), *args]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode_group = parser.add_mutually_exclusive_group()
    mode_group.add_argument("--check", action="store_true")
    mode_group.add_argument("--hook", action="store_true")
    args = parser.parse_args(argv)
    mode = "--check" if args.check else "--hook" if args.hook else "install"

    code, inside = git_output(["rev-parse", "--is-inside-work-tree"])
    if code or inside != "true":
        print("bootstrap: FAIL reason=not_a_git_worktree", file=sys.stderr)
        return 1

    if mode == "install":
        if run(["git", "config", "--local", "core.hooksPath", HOOKS_PATH]):
            print("bootstrap: FAIL reason=git_hook_configuration", file=sys.stderr)
            return 1
        print(f"bootstrap: CONFIGURED core.hooksPath={HOOKS_PATH}")

    if mode == "--check":
        errors = check_hook_contract()
        if run(python_tool("skills", "doctor")):
            errors.append("skills=invalid action=run_scripts/skills_install")
        if errors:
            for error in errors:
                print(f"bootstrap: FAIL {error}", file=sys.stderr)
            return 1
        print(f"bootstrap: OK core.hooksPath={HOOKS_PATH} skills=ready")
        return 0

    status = 0
    if run(python_tool("skills", "install")):
        status = 1
    for command in ("inbox", "sync", "doctor"):
        if run(python_tool("sources", command)):
            status = 1
    if run(python_tool("logs", "status")):
        print("bootstrap: NOTICE activity_log_identity_required_before_first_commit", file=sys.stderr)

    if status:
        print(
            "bootstrap: INCOMPLETE action=resolve_reported_skill_or_source_requirements_then_rerun",
            file=sys.stderr,
        )
        return 1
    if mode == "install":
        errors = check_hook_contract()
        if errors:
            for error in errors:
                print(f"bootstrap: FAIL {error}", file=sys.stderr)
            return 1
    print(f"bootstrap: OK sources=ready skills=ready hooks={HOOKS_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
