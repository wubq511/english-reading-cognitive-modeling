---
schema_version: 1
member_id: robert
timestamp: 2026-08-14T08:50:11Z
category: source
summary: Downgrade a drifted source endpoint before publication
supersedes: NONE
---

## Work completed

- Completed the first-bootstrap audit in a source-empty clone and measured automatic versus manual recovery.
- Downgraded `METHOD-003` from `DIRECT_PUBLIC` to `MANUAL_ONLY` after the official endpoint returned bytes that did not match the catalog lock.
- Recorded both hashes and preserved the DOI, local expected bytes and redistribution-rights judgment without silently changing the checksum.

## Research or decision impact

- No paper conclusion or project scientific conclusion changed.
- Collaborator Agents will no longer repeatedly download and reject a known-drifted endpoint; they will request the exact expected version for manual reconciliation.
- Source-dependent research remains fail closed: a fresh clone restored 11 exact originals automatically and reported 69 exact manual requirements.

## Verification

- Source-empty clone bootstrap installed `.githooks`, exposed the missing member identity, restored 11 exact originals and reported 69 manual requirements; no missing source was treated as present.
- The former `METHOD-003` download returned SHA-256 `2ebb67846ae525c35cf3f79b3e568bb68331e975a6c74494f8717bef920d888a` versus catalog `36a0d04cacac5bdb2f24e7022bcbc6fd01493dfcbc6104c588123eb0c7f3b744`; import failed closed.
- `scripts/sources catalog-check`, `doctor` and `sync`: PASS locally for all 80 catalog records after the acquisition downgrade.
- `python3 -m unittest discover -s tests -v`: PASS, 39 tests; `scripts/verify` and `scripts/verify --public`: PASS with 72 Markdown files.
- NOT_RUN: one final source-empty clone will confirm that the known-drifted endpoint is no longer attempted after this commit.

## Follow-ups

- Compare the current Cambridge endpoint PDF against catalog `METHOD-003`; only then choose whether to add a distinct version record or update the canonical version through the normal source-review process.
