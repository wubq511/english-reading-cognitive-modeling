---
schema_version: 1
member_id: robert
timestamp: 2026-08-14T08:33:52Z
category: maintenance
summary: Restrict member-log validation to repository-relevant files
supersedes: NONE
---

## Work completed

- Corrected member-log validation to inspect tracked and non-ignored untracked files instead of every filesystem entry.
- Added regression coverage for a binary `.DS_Store` below `logs/members/` when the file is excluded by `.gitignore`.
- Reconciled publication inventory counts for the additional append-only maintenance entry.

## Research or decision impact

- No scientific conclusion or logging policy changed.
- The validator now matches the actual repository boundary: ignored workspace residue cannot enter Git and does not represent a member log, while any non-ignored unexpected file still fails validation.

## Verification

- `python3 -m unittest discover -s tests -v`: PASS, 39 tests including the ignored binary `.DS_Store` regression.
- `scripts/logs validate`: PASS, two member entries and ignored residue excluded; `scripts/logs check-history`: PASS for the existing post-boundary commit.
- `scripts/verify` and `scripts/verify --public`: PASS, 70 Markdown files, 80 sources and 25 frozen raw-source manifest entries.
- `scripts/logs check-staged`, `.githooks/pre-commit` and `.githooks/pre-push`: PASS for the five-path corrective change.

## Follow-ups

- None.
