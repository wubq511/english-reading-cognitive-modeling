---
schema_version: 1
member_id: robert
timestamp: 2026-08-14T08:45:28Z
category: governance
summary: Make public-clone verification portable and resume publication
supersedes: NONE
---

## Work completed

- Ran a true Git clone with no local raw materials or source originals and checked the public snapshot, rule symlink and hook state.
- Removed local-machine assumptions from CI tests while retaining local byte-level verification whenever the complete corpus is present.
- Recorded the owner's renewed publication authorization and the current GitHub authentication prerequisite.

## Research or decision impact

- No scientific conclusion changed.
- A collaborator can verify the public metadata snapshot without possessing restricted originals; source-dependent research still fails closed until the exact cataloged bytes are restored.
- The recovery goal remains incomplete only until the public repository, first CI run and required branch check are live.

## Verification

- First fresh clone: public snapshot verification passed with 96 tracked files, zero PDFs, zero raw files and `CLAUDE.md -> AGENTS.md`; the full test suite exposed four local-only assumptions and correctly blocked publication.
- `python3 -m unittest discover -s tests -v`: PASS locally, 39 tests with the complete corpus.
- `scripts/verify` and `scripts/verify --public`: PASS locally, 71 Markdown files, 80 sources and 25 frozen raw-source manifest entries.
- `scripts/logs validate`: PASS for three member entries; `git diff --check`: PASS.
- NOT_RUN: the second clean-clone test requires this compatibility fix to exist in a commit and is the immediate post-commit release gate.

## Follow-ups

- The owner must run `gh auth refresh -h github.com`; the Agent can then create the public repository, push, observe CI and enable the required check.
