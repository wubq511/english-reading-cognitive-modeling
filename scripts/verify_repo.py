#!/usr/bin/env python3
"""Fail-closed repository integrity checks for research handoff assets."""

from __future__ import annotations

import argparse
import hashlib
import os
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
    "papers/library/",
    "papers/catalog.yaml",
    "papers/checksums.sha256",
    "scripts/papers",
)
HISTORY_ALLOWLIST = {
    "reports/provenance/ASSET_MAP.md",
    "reports/provenance/CONFLICT_REGISTER.md",
    "scripts/verify_repo.py",
}
REQUIRED_HOOKS = ("post-checkout", "post-merge", "pre-push")
REQUIRED_SKELETON = (
    "src/README.md",
    "experiments/README.md",
    "experiments/specs/README.md",
    "experiments/templates/EXPERIMENT_SPEC.md",
    "experiments/templates/RUN_MANIFEST.yaml",
    "data/README.md",
    "data/synthetic/README.md",
    "data/derived/README.md",
    "artifacts/README.md",
    "scripts/README.md",
)


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


def check_agent_rule_link() -> list[str]:
    agents = ROOT / "AGENTS.md"
    claude = ROOT / "CLAUDE.md"
    errors: list[str] = []
    if not agents.is_file():
        errors.append("missing-agent-rules AGENTS.md")
    if not claude.is_symlink():
        errors.append("claude-rules-must-be-symlink CLAUDE.md -> AGENTS.md")
        return errors
    if os.readlink(claude) != "AGENTS.md":
        errors.append(f"claude-rules-wrong-target CLAUDE.md -> {os.readlink(claude)}")
    if claude.resolve(strict=False) != agents.resolve(strict=False):
        errors.append("claude-rules-resolve-mismatch CLAUDE.md != AGENTS.md")
    return errors


def check_hook_files() -> list[str]:
    errors: list[str] = []
    bootstrap = ROOT / "scripts" / "bootstrap"
    if not bootstrap.is_file() or not os.access(bootstrap, os.X_OK):
        errors.append("missing-or-nonexecutable scripts/bootstrap")
    for name in REQUIRED_HOOKS:
        hook = ROOT / ".githooks" / name
        if not hook.is_file() or not os.access(hook, os.X_OK):
            errors.append(f"missing-or-nonexecutable .githooks/{name}")
    return errors


def check_bootstrap_configuration() -> list[str]:
    result = subprocess.run(
        ["git", "config", "--local", "--get", "core.hooksPath"],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    configured = result.stdout.strip()
    if result.returncode or configured != ".githooks":
        return [
            f"bootstrap-not-configured core.hooksPath={configured or 'UNSET'} "
            "action=run_scripts/bootstrap"
        ]
    return []


def check_workspace_skeleton() -> list[str]:
    return [
        f"missing-workspace-skeleton {relative}"
        for relative in REQUIRED_SKELETON
        if not (ROOT / relative).is_file()
    ]


def check_inbox_empty() -> list[str]:
    inbox = ROOT / "tmp" / "pdfs"
    if not inbox.exists():
        return []
    return [
        f"unresolved-source-inbox {path.relative_to(ROOT)} "
        "action=run_scripts/sources_inbox_or_agent_review"
        for path in sorted(inbox.iterdir())
    ]


def check_knowledge_ownership() -> list[str]:
    errors: list[str] = []
    roadmap = (ROOT / "reports/project_state/ROADMAP.md").read_text(encoding="utf-8")
    if re.search(r"^Current:", roadmap, re.MULTILINE):
        errors.append("duplicated-current-state ROADMAP.md must defer to CURRENT_STATE.md")
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


def check_source_crosswalk() -> list[str]:
    crosswalk = ROOT / "reports/provenance/SOURCE_REPORT_CROSSWALK.md"
    text = crosswalk.read_text(encoding="utf-8")
    errors: list[str] = []
    for line in (ROOT / "sources/checksums.sha256").read_text(encoding="utf-8").splitlines():
        match = re.fullmatch(r"[0-9a-f]{64}  (.+)", line)
        if match and match.group(1) not in text:
            errors.append(f"source-missing-from-crosswalk {match.group(1)}")
    return errors


def run_source_doctor() -> list[str]:
    result = subprocess.run(
        [str(ROOT / "scripts" / "sources"), "doctor"],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    if result.returncode:
        return ["sources-doctor-failed\n" + result.stdout.rstrip()]
    return []


def run_source_catalog_check() -> list[str]:
    result = subprocess.run(
        [str(ROOT / "scripts" / "sources"), "catalog-check"],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    if result.returncode:
        return ["sources-catalog-check-failed\n" + result.stdout.rstrip()]
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
    errors.extend(check_agent_rule_link())
    errors.extend(check_hook_files())
    errors.extend(check_workspace_skeleton())
    errors.extend(check_knowledge_ownership())
    errors.extend(check_source_crosswalk())
    if args.public:
        errors.extend(check_manifest_format("reports/provenance/RAW_SOURCE_MANIFEST.sha256"))
        errors.extend(check_manifest_format("sources/checksums.sha256"))
        errors.extend(run_source_catalog_check())
    else:
        errors.extend(check_bootstrap_configuration())
        errors.extend(check_inbox_empty())
        errors.extend(check_manifest("reports/provenance/RAW_SOURCE_MANIFEST.sha256"))
        errors.extend(check_manifest("sources/checksums.sha256"))
        errors.extend(run_source_doctor())
    if errors:
        print("repository verification: FAILED", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(
        f"repository verification: OK mode={'public' if args.public else 'local'} "
        f"markdown_files={len(markdown_files())} "
        f"sources={manifest_entry_count('sources/checksums.sha256')} "
        f"raw_sources={manifest_entry_count('reports/provenance/RAW_SOURCE_MANIFEST.sha256')}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
