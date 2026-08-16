---
schema_version: 1
member_id: smiling-wei
timestamp: 2026-08-16T09:53:01Z
category: research
summary: Completed issue 7 replay-fidelity research and simulation assets
supersedes: NONE
---

## Work completed

- Registered and locally verified eleven primary replay/oracle sources with stable IDs, rights notes, checksums, and crosswalk entries.
- Produced the replay-fidelity-oracles/v1 report and meeting outline, separating sourced findings from PROJECT-INFERENCE recommendations.
- Specified, implemented, and ran EXP-001 with three deterministic DATA-D1 simulation-only scenarios and AI provenance.
- Made the repository verification and pre-commit subprocess calls Windows-portable and added a UTF-8 history regression test.

## Research or decision impact

- Recommended layered structural, ordered-replay, prefix-state, final-state, timing, and cross-environment oracles instead of a single final-state check.
- Assigned sequence, mono_ms, and wall_time distinct replay, duration, and calendar roles; real-environment tolerances remain an experiment gate for issue 8.
- The simulations support only the frozen engineering DGM and do not support cognitive, ecological, or real-session prevalence claims.

## Verification

- PASS: sources catalog-check and inbox; all eleven REPLAY source IDs independently returned OK with expected SHA-256.
- PASS: EXP-001 completed 10/10 predeclared checks; five replay simulation unit tests passed.
- PASS: scripts/verify.cmd --public reported 91 sources, 131 Markdown files, and 25 raw-source records.
- PARTIAL: full unittest discovery ran 61 tests; 56 passed, 3 were expected skips for absent local assets, and 2 existing symlink tests errored because Windows user privilege WinError 1314 is unavailable.
- EXPECTED_FAIL: local scripts/verify.cmd reports 25 absent frozen migration files and 70 absent historical source originals; no REPLAY-001..011 source is missing.

## Follow-ups

- Obtain teammate review, then post the report link and resolution summary to GitHub issue 7 only after user approval.
- Restore the clone-wide historical raw/source assets or use an approved complete clone before treating the local verify gate as green; Windows symlink tests require Developer Mode or elevated privilege.
