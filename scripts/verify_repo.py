#!/usr/bin/env python3
"""Fail-closed repository integrity checks for research handoff assets."""

from __future__ import annotations

import argparse
import hashlib
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
SKIP_PARTS = {".git", ".venv", "__pycache__", "webchat_raw_materials"}
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]*\]\((?:<([^>]+)>|([^\s)]+))(?:\s+['\"][^'\"]*['\"])?\)")
OLD_CURRENT_PATHS = (
    "reports/A-E_analyses",
    "reports/ui_interation_behavior_literature_research",
    "papers/chatgpt_A-E",
    "papers/ui_interation_behavior",
)
HISTORY_ALLOWLIST = {
    "reports/provenance/ASSET_MAP.md",
    "scripts/verify_repo.py",
}


def markdown_files() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("*.md")
        if not any(part in SKIP_PARTS for part in path.relative_to(ROOT).parts)
    )


def check_links() -> list[str]:
    errors: list[str] = []
    for path in markdown_files():
        text = path.read_text(encoding="utf-8")
        for match in MARKDOWN_LINK.finditer(text):
            raw = match.group(1) or match.group(2)
            if not raw or raw.startswith(("http://", "https://", "mailto:", "app://", "plugin://")):
                continue
            target_text = unquote(raw.split("#", 1)[0])
            if not target_text:
                continue
            target = Path(target_text)
            resolved = target if target.is_absolute() else path.parent / target
            if not resolved.exists():
                line = text.count("\n", 0, match.start()) + 1
                errors.append(f"broken-link {path.relative_to(ROOT)}:{line} -> {raw}")
    return errors


def check_stale_current_paths() -> list[str]:
    errors: list[str] = []
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path.suffix.lower() in {".pdf"}:
            continue
        rel = path.relative_to(ROOT)
        if any(part in SKIP_PARTS for part in rel.parts) or rel.as_posix() in HISTORY_ALLOWLIST:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for old in OLD_CURRENT_PATHS:
            if old in text:
                line = text[: text.index(old)].count("\n") + 1
                errors.append(f"stale-current-path {rel}:{line} -> {old}")
    return errors


def check_manifest(relative_manifest: str) -> list[str]:
    manifest = ROOT / relative_manifest
    errors: list[str] = []
    for number, line in enumerate(manifest.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            errors.append(f"blank-manifest-line {relative_manifest}:{number}")
            continue
        match = re.fullmatch(r"([0-9a-f]{64})  (.+)", line)
        if not match:
            errors.append(f"invalid-manifest-line {relative_manifest}:{number}")
            continue
        expected, relative_path = match.groups()
        target = ROOT / relative_path
        if not target.is_file():
            errors.append(f"missing-manifest-target {relative_manifest}:{number} -> {relative_path}")
            continue
        actual = hashlib.sha256(target.read_bytes()).hexdigest()
        if actual != expected:
            errors.append(f"manifest-mismatch {relative_path}: expected={expected} actual={actual}")
    return errors


def check_manifest_format(relative_manifest: str) -> list[str]:
    manifest = ROOT / relative_manifest
    errors: list[str] = []
    seen_paths: set[str] = set()
    for number, line in enumerate(manifest.read_text(encoding="utf-8").splitlines(), start=1):
        match = re.fullmatch(r"([0-9a-f]{64})  (.+)", line)
        if not match:
            errors.append(f"invalid-manifest-line {relative_manifest}:{number}")
            continue
        relative_path = match.group(2)
        if relative_path in seen_paths:
            errors.append(f"duplicate-manifest-target {relative_manifest}:{number} -> {relative_path}")
        seen_paths.add(relative_path)
    return errors


def run_paper_doctor() -> list[str]:
    result = subprocess.run(
        [str(ROOT / "scripts" / "papers"), "doctor"],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    if result.returncode:
        return ["papers-doctor-failed\n" + result.stdout.rstrip()]
    return []


def run_paper_catalog_check() -> list[str]:
    result = subprocess.run(
        [str(ROOT / "scripts" / "papers"), "catalog-check"],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    if result.returncode:
        return ["papers-catalog-check-failed\n" + result.stdout.rstrip()]
    return []


def manifest_entry_count(relative_manifest: str) -> int:
    manifest = ROOT / relative_manifest
    return sum(1 for line in manifest.read_text(encoding="utf-8").splitlines() if line.strip())


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--public",
        action="store_true",
        help="validate the tracked public snapshot without local raw/PDF files",
    )
    args = parser.parse_args(argv)
    errors = []
    errors.extend(check_links())
    errors.extend(check_stale_current_paths())
    if args.public:
        errors.extend(check_manifest_format("reports/provenance/RAW_SOURCE_MANIFEST.sha256"))
        errors.extend(check_manifest_format("papers/checksums.sha256"))
        errors.extend(run_paper_catalog_check())
    else:
        errors.extend(check_manifest("reports/provenance/RAW_SOURCE_MANIFEST.sha256"))
        errors.extend(check_manifest("papers/checksums.sha256"))
        errors.extend(run_paper_doctor())
    if errors:
        print("repository verification: FAILED", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(
        f"repository verification: OK mode={'public' if args.public else 'local'} "
        f"markdown_files={len(markdown_files())} "
        f"papers={manifest_entry_count('papers/checksums.sha256')} "
        f"raw_sources={manifest_entry_count('reports/provenance/RAW_SOURCE_MANIFEST.sha256')}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
