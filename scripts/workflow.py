#!/usr/bin/env python3
"""Validate or install the GitHub label vocabulary for project workflow skills."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / ".agents" / "skills" / "research-workflow" / "references" / "github-labels.json"


def run_gh(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["gh", *args],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )


def load_labels() -> list[dict[str, str]]:
    payload = json.loads(MANIFEST.read_text(encoding="utf-8"))
    return payload["labels"]


def resolve_repo() -> tuple[str | None, str | None]:
    result = run_gh(["repo", "view", "--json", "nameWithOwner,url"])
    if result.returncode:
        return None, result.stdout.strip()
    payload = json.loads(result.stdout)
    return payload["nameWithOwner"], None


def remote_labels() -> tuple[dict[str, dict[str, str]] | None, str | None]:
    result = run_gh(["label", "list", "--limit", "1000", "--json", "name,color,description"])
    if result.returncode:
        return None, result.stdout.strip()
    labels = json.loads(result.stdout)
    return {label["name"]: label for label in labels}, None


def check() -> list[str]:
    repo, error = resolve_repo()
    if error:
        return [f"github-repository-unavailable {error}"]
    actual, error = remote_labels()
    if error or actual is None:
        return [f"github-labels-unavailable {error}"]
    errors: list[str] = []
    for expected in load_labels():
        current = actual.get(expected["name"])
        if current is None:
            errors.append(f"missing-label {expected['name']}")
            continue
        if current["color"].lower() != expected["color"].lower():
            errors.append(f"wrong-label-color {expected['name']}")
        if (current.get("description") or "") != expected["description"]:
            errors.append(f"wrong-label-description {expected['name']}")
    if not errors:
        print(f"workflow labels: repository={repo}")
    return errors


def install() -> list[str]:
    repo, error = resolve_repo()
    if error:
        return [f"github-repository-unavailable {error}"]
    errors: list[str] = []
    for label in load_labels():
        result = run_gh(
            [
                "label",
                "create",
                label["name"],
                "--color",
                label["color"],
                "--description",
                label["description"],
                "--force",
            ]
        )
        if result.returncode:
            errors.append(f"label-install-failed {label['name']}: {result.stdout.strip()}")
    if not errors:
        print(f"workflow labels: INSTALLED repository={repo} count={len(load_labels())}")
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("labels-check", "labels-install"))
    args = parser.parse_args(argv)
    errors = install() if args.command == "labels-install" else check()
    if errors:
        print(f"workflow {args.command}: FAILED", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(f"workflow {args.command}: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
