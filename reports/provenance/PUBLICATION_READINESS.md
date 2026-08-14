# Public Repository Readiness

Status: `READY; PUBLICATION RESUMED; GITHUB AUTH REQUIRED`
Audit date: 2026-08-14
Target: `https://github.com/wubq511/english-reading-cognitive-modeling`

## Decision

The local research recovery, source-boundary migration and automation migration have passed the updated final audit. The project owner explicitly resumed and authorized public publication on 2026-08-14. No remote repository has been created and no content has been pushed because the active `gh` account currently requires reauthentication; this is an execution prerequisite, not a content-readiness failure.

The approved first snapshot must remain metadata-first: it contains canonical research documents, provenance, source metadata/checksums and recovery tooling, but no raw chat export, third-party source bytes or human-participant data.

## Audited public boundary

| Check | Result |
| --- | --- |
| Tracked raw recovery material | `0`; `webchat_raw_materials/` is ignored |
| Prospective tracked files | `98` |
| Tracked third-party source files | `0`; only `sources/library/README.md` is tracked below the ignored local library |
| Tracked human/private data directories | `0` |
| Common credential/token/private-key signatures | no matches in the staged snapshot |
| Credentialized URLs | no matches |
| Personal email addresses | no matches |
| Machine-local absolute paths | no matches |
| Largest tracked blob | 277,815 bytes; no GitHub large-file boundary is approached |
| Citation metadata | `CITATION.cff` parses successfully |
| Workflow supply-chain pins | checkout `v7.0.1` and setup-python `v7.0.0` commit hashes verified against upstream tags |
| Member activity logs | append-only schema, staged gate and post-boundary history gate covered by repository tests; CI fetches full history |
| Diff hygiene | `git diff --cached --check` passes |

The credential scan is a bounded signature scan, not a proof that arbitrary prose can never encode sensitive information. The stronger structural protection is that the raw, PDF, AI-payload and human-data trees are excluded by path and verified before publication.

## Source and rights state

- 80 required PDF/attachment files are present locally and pass exact SHA-256 and media-signature checks.
- 11 catalog records have a currently hash-reproducible `DIRECT_PUBLIC` acquisition route; 7 are `MANUAL_ONLY`; 62 remain `UNKNOWN`. `METHOD-003` was downgraded after its official endpoint returned bytes that differed from the catalog lock during a fresh-clone audit.
- Eight specific versions are conservatively marked `REDISTRIBUTION_ALLOWED`, ten `RESTRICTED`, and 62 `UNKNOWN`.
- Despite the permissions, **zero source originals may enter the first Git history**. Any later release is a separate file-level audit and public-approval event.
- Collaborators run `scripts/bootstrap` once. Human downloads go to `tmp/pdfs/`; Agents update metadata and use `scripts/sources inbox`, which removes only verified migrated copies.

The legal and engineering rationale is recorded in [`../../docs/project-management/SOURCE_DISTRIBUTION.md`](../../docs/project-management/SOURCE_DISTRIBUTION.md).

## Research-claim boundary

- The public reports recover and organize prior work; they are not peer review or empirical confirmation.
- The existing-literature audit samples major claims and marks unsupported upgrades, but does not certify every sentence of every legacy report.
- Consequential future claims still require stable source IDs plus page/section evidence and, where relevant, independent empirical validation.
- Phase 2A is design-closed only. Phase 0 remains open, Phase 3 is a draft specification, Phase 4 is not completed, and no system, benchmark result or human study exists yet.
- AI/Agent use is allowed in the research and experiment plane under policy; the baseline runtime itself remains free of LLMs, generative AI and Agents.

## Verification evidence

```text
39 unit tests (local complete corpus)              PASS
39 unit tests (public clone)                       PASS: local-byte checks skip when originals are absent
scripts/verify (local)                            PASS: 72 Markdown, 80 sources, 25 raw sources
scripts/verify --public                           PASS: 72 Markdown, 80 sources, 25 raw sources
scripts/bootstrap --check                         PASS: core.hooksPath=.githooks
scripts/logs validate                             PASS: 2 member entries; ignored workspace residue excluded
scripts/sources inbox                             PASS: inbox empty
scripts/sources sync                              PASS: no missing direct-public dependency
scripts/sources doctor                            PASS: 80/80 exact local dependencies
CITATION.cff parse                                PASS
prospective Git index                             PASS: 98 files, 0 PDFs, 0 raw files, 0 tmp files
secret/path/credential URL/email signature scan   PASS: no matches
CLAUDE.md                                         PASS: mode 120000 -> AGENTS.md
git diff --cached --check                         PASS
```

The Git client does not clone or automatically enable repository-controlled hooks. Each clone therefore needs one explicit `scripts/bootstrap` invocation; the root `AGENTS.md` requires both Codex and Claude (through the `CLAUDE.md` symlink) to announce and run it before work, so the human does not need to remember the command. After that, configured checkout, merge, commit and push hooks enforce source, activity-log and repository gates automatically. Duplicate tool-specific SessionStart Hooks are intentionally deferred unless real omission evidence appears. The existing GitHub Actions Workflow is retained for remote push/PR verification; it cannot bootstrap a local clone. See [`../../docs/project-management/AGENT_BOOTSTRAP.md`](../../docs/project-management/AGENT_BOOTSTRAP.md) and [`../../logs/README.md`](../../logs/README.md).

## Residual actions after publication

1. Confirm the first GitHub Actions run passes on the public remote.
2. Enable a simple main-branch protection rule requiring the verification workflow.
3. Continue the manual acquisition, laboratory and ethics queue in [`../project_state/MANUAL_ACTIONS.md`](../project_state/MANUAL_ACTIONS.md).
4. Never infer that deleting a later-public artifact retracts copies already cloned; prevent unsafe publication before push.

These follow-up actions do not expand the first publication scope.
