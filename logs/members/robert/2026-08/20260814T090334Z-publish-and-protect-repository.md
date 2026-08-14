---
schema_version: 1
member_id: robert
timestamp: 2026-08-14T09:03:34Z
category: governance
summary: Publish and protect the collaborative research repository
supersedes: NONE
---

## Work completed

- Published the audited metadata-first project snapshot to the public `wubq511/english-reading-cognitive-modeling` repository after explicit owner approval.
- Observed the first GitHub Actions verification to successful completion.
- Protected `main` with mandatory pull requests and the strict `verify` check, enforced the rule for the administrator, and disabled force-pushes and branch deletion.
- Reconciled the canonical project-state, manual-action, publication-readiness and recovery-goal documents with the live remote state.

## Research or decision impact

- No scientific claim, phase status or runtime design changed.
- Researchers and their Agents now have a public, reproducible collaboration entry point whose remote merge gate rechecks source boundaries, member activity logs and repository integrity.
- Source originals, raw recovery materials and human data remain outside public Git; full-text-dependent work still fails closed until exact local dependencies are restored.

## Verification

- `scripts/bootstrap`: PASS with 80/80 local sources and `.githooks` configured.
- `scripts/verify` and `scripts/verify --public`: PASS before publication.
- `python3 -m unittest discover -s tests -p 'test_*.py'`: PASS, 39 tests.
- GitHub Actions run `31786325757`: PASS for published commit `f3a826c7d4e53e4fdb9bad784a16ffe90646f079`.
- GitHub branch-protection API: PASS; strict `verify`, pull request required, admin enforcement enabled, force-push and deletion disabled.

## Follow-ups

- Continue Phase 0 item/data-rights work and institutional ethics coordination under `reports/project_state/MANUAL_ACTIONS.md`.
- Treat every future public push, Release or third-party-file distribution as a separately approved publication event.
