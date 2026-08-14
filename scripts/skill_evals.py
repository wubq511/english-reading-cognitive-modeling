#!/usr/bin/env python3
"""Validate committed skill-creator eval suites for explicit workflow skills."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ENTRY_SKILLS = (
    "ercm-workflow",
    "ercm-wayfinder",
    "ercm-to-spec",
    "ercm-to-tickets",
    "ercm-implement",
)
MIN_EVALS = {
    "ercm-workflow": 4,
    "ercm-wayfinder": 4,
    "ercm-to-spec": 2,
    "ercm-to-tickets": 2,
    "ercm-implement": 4,
}


def eval_path(skill_name: str, root: Path = ROOT) -> Path:
    return root / ".agents" / "skills" / skill_name / "evals" / "evals.json"


def validate_eval_suite(skill_name: str, root: Path = ROOT) -> list[str]:
    path = eval_path(skill_name, root)
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"invalid-evals-json {skill_name}: {exc}"]
    errors: list[str] = []
    if not isinstance(payload, dict) or payload.get("skill_name") != skill_name:
        errors.append(f"eval-skill-name-mismatch {skill_name}")
    evals = payload.get("evals") if isinstance(payload, dict) else None
    if not isinstance(evals, list):
        return errors + [f"evals-must-be-list {skill_name}"]
    if len(evals) < MIN_EVALS[skill_name]:
        errors.append(
            f"insufficient-eval-coverage {skill_name}: "
            f"actual={len(evals)} minimum={MIN_EVALS[skill_name]}"
        )
    ids: set[int] = set()
    for index, item in enumerate(evals):
        prefix = f"{skill_name}[{index}]"
        if not isinstance(item, dict):
            errors.append(f"invalid-eval-entry {prefix}")
            continue
        eval_id = item.get("id")
        if not isinstance(eval_id, int) or eval_id < 1:
            errors.append(f"invalid-eval-id {prefix}")
        elif eval_id in ids:
            errors.append(f"duplicate-eval-id {skill_name}:{eval_id}")
        else:
            ids.add(eval_id)
        prompt = item.get("prompt")
        if not isinstance(prompt, str) or not prompt.strip():
            errors.append(f"missing-eval-prompt {prefix}")
        elif f"${skill_name}" not in prompt and f"/{skill_name}" not in prompt:
            errors.append(f"eval-must-explicitly-invoke-skill {prefix}")
        expected = item.get("expected_output")
        if not isinstance(expected, str) or not expected.strip():
            errors.append(f"missing-expected-output {prefix}")
        expectations = item.get("expectations")
        if not isinstance(expectations, list) or len(expectations) < 2 or not all(
            isinstance(value, str) and value.strip() for value in expectations
        ):
            errors.append(f"invalid-expectations {prefix}")
        files = item.get("files")
        if files is not None and (
            not isinstance(files, list)
            or not all(isinstance(value, str) and value.strip() for value in files)
        ):
            errors.append(f"invalid-eval-files {prefix}")
    return errors


def validate_all(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    for skill_name in ENTRY_SKILLS:
        errors.extend(validate_eval_suite(skill_name, root))
    return errors


def total_evals(root: Path = ROOT) -> int:
    total = 0
    for skill_name in ENTRY_SKILLS:
        payload = json.loads(eval_path(skill_name, root).read_text(encoding="utf-8"))
        total += len(payload["evals"])
    return total


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("doctor",))
    parser.parse_args(argv)
    errors = validate_all()
    if errors:
        print("skill evals doctor: FAILED", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(f"skill evals doctor: OK skills={len(ENTRY_SKILLS)} evals={total_evals()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
