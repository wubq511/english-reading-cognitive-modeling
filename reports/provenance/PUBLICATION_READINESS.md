# Public Repository Readiness

Status: `READY FOR EXPLICIT PUBLICATION APPROVAL`
Audit date: 2026-08-14
Target: `https://github.com/wubq511/english-reading-cognitive-modeling`

## Decision

The local research recovery is ready to become the first public repository snapshot, subject to the project lead's explicit approval. No remote repository has been created and no content has been pushed.

The approved first snapshot must remain metadata-first: it contains canonical research documents, provenance, paper metadata/checksums and recovery tooling, but no raw chat export, third-party PDF bytes or human-participant data.

## Audited public boundary

| Check | Result |
| --- | --- |
| Tracked raw recovery material | `0`; `webchat_raw_materials/` is ignored |
| Tracked PDF files | `0`; `papers/library/**/*.pdf` is ignored |
| Tracked human/private data directories | `0` |
| Common credential/token/private-key signatures | no matches in the staged snapshot |
| Credentialized URLs | no matches |
| Personal email addresses | no matches |
| Machine-local absolute paths | no matches |
| Largest tracked blob | 277,824 bytes; no GitHub large-file boundary is approached |
| Citation metadata | `CITATION.cff` parses successfully |
| Workflow supply-chain pins | checkout `v7.0.1` and setup-python `v7.0.0` commit hashes verified against upstream tags |
| Diff hygiene | `git diff --cached --check` passes |

The credential scan is a bounded signature scan, not a proof that arbitrary prose can never encode sensitive information. The stronger structural protection is that the raw, PDF, AI-payload and human-data trees are excluded by path and verified before publication.

## Paper and rights state

- 74 required PDF/attachment files are present locally and pass exact SHA-256/PDF checks.
- 11 catalog records have a verified `DIRECT_PUBLIC` acquisition route; one is `MANUAL_ONLY`; 62 remain `UNKNOWN`.
- Six specific versions are conservatively marked `REDISTRIBUTION_ALLOWED`, six `RESTRICTED`, and 62 `UNKNOWN`.
- Despite the six permissions, **zero PDFs enter the first Git history**. Any later release of a rights-cleared version is a separate file-level audit and public-approval event.
- Collaborators restore local originals with `scripts/papers doctor`, `scripts/papers sync` and `scripts/papers import`; missing required full text fails closed.

The legal and engineering rationale is recorded in [`../research/public-repository-paper-distribution-audit.md`](../research/public-repository-paper-distribution-audit.md).

## Research-claim boundary

- The public reports recover and organize prior work; they are not peer review or empirical confirmation.
- The existing-literature audit samples major claims and marks unsupported upgrades, but does not certify every sentence of every legacy report.
- Consequential future claims still require stable paper IDs plus page/section evidence and, where relevant, independent empirical validation.
- Phase 2A is design-closed only. Phase 0 remains open, Phase 3 is a draft specification, Phase 4 is not completed, and no system, benchmark result or human study exists yet.
- AI/Agent use is allowed in the research and experiment plane under policy; the baseline runtime itself remains free of LLMs, generative AI and Agents.

## Verification evidence

The final local audit passed:

```text
python3 -m unittest discover -s tests -p 'test_*.py' -v  -> 17/17 PASS
scripts/verify                                           -> PASS (local, 74 papers, 25 raw sources)
scripts/verify --public                                  -> PASS (public snapshot)
scripts/papers doctor                                    -> PASS (74/74)
scripts/papers sync                                      -> PASS (0 missing downloads)
git diff --cached --check                                -> PASS
```

## Residual actions after publication

1. Confirm the first GitHub Actions run passes on the public remote.
2. Enable a simple main-branch protection rule requiring the verification workflow.
3. Continue the manual acquisition, laboratory and ethics queue in [`../project_state/MANUAL_ACTIONS.md`](../project_state/MANUAL_ACTIONS.md).
4. Never infer that deleting a later-public artifact retracts copies already cloned; prevent unsafe publication before push.

These follow-up actions do not expand the first publication scope.
