---
name: ercm-implement
description: Execute one explicitly named, ready ERCM GitHub evidence-slice ticket under this research repository's source, experiment, ethics, logging, review, and publication gates. Never selects a ticket automatically.
disable-model-invocation: true
---

# Implement One Ticket

`ercm-implement` means complete the ticket's verifiable outcome. It may involve research, source work, data, an experiment, code, UI instrumentation, or governance. It does **not** mean “write code regardless of the ticket.”

## Invocation contract

The user must supply exactly one GitHub ticket number or URL before execution. If it is absent, ambiguous, a map/spec parent, or a phase name, enter **selection assistance**: query the execution frontier read-only, show up to three titled ticket URLs with work type, readiness/gates, downstream value, and fit with the user's stated goal; recommend one and explain why another may be preferable. Then stop and ask the user to invoke `ercm-implement` again with one exact ticket. Do not assign, relabel, branch, modify files, or begin work in selection assistance.

The explicit invocation authorizes validating and claiming that ticket plus local execution. It does not authorize public push, PR creation, Release, third-party-file publication, or human-participant activity.

## 1. Preflight and eligibility

1. Run project bootstrap and read `docs/agents/research-workflow.md`, `docs/agents/issue-tracker.md`, the ticket with comments/relationships, its parent contract, and applicable canonical owners/protocols.
2. Prove the issue has `workflow:ticket`, exactly one `work:<type>`, and `ready-for-agent`.
3. Refuse if any native blocker is open, an external gate is unmet, acceptance is not testable, the parent spec is not approved/frozen, or the ticket is assigned to another member.
4. Inspect the worktree. Preserve unrelated changes; stop if overlap makes isolation unsafe.
5. If on a protected/default branch, create the neutral work branch defined by `docs/agents/issue-tracker.md`; otherwise stay on the current branch.
6. Only after all checks pass, assign the ticket to the current GitHub user, remove `ready-for-agent`, and apply `workflow:in-progress`.

## 2. Execute by outcome type

- **Research** — use high-trust primary sources and stable source IDs/page locators; write to the canonical report location; distinguish observed/derived/inferred/validated/simulation-only; preserve alternatives and uncertainty. Adapt the `ercm-research` skill inline when sub-agents are unavailable.
- **Source** — verify identity, version, rights, acquisition, hash, parser QA, catalog/checksum/crosswalk, and inbox cleanup. Never infer redistribution rights.
- **Experiment** — require the frozen `EXP-*` spec; lock data/sources/splits/metrics/seeds/environment; write a run manifest; preserve invalid, negative, and null runs; enforce AI and human gates. Synthetic recovery cannot validate human cognition.
- **Code** — use `ercm-tdd` at the agreed highest seam, then targeted tests/typecheck/lint and the full relevant suite. Do not change a metric or gate merely to pass.
- **Data** — keep raw inputs append-only; version transformations and hashes; prevent leakage; classify public/private/sensitive data before writing.
- **Governance** — update the single owner first, search stale copies, record supersession/ADR where needed, and verify links/invariants.

For UI tickets, separate instrument reliability from treatment effects. A visually preferred UI is not automatically a measurement-valid UI, and exploratory pilot optimization cannot be reported as confirmatory evidence on the same sample.

## 3. Verify, review, log, and commit

1. Run every ticket acceptance check plus the repository checks required by `AGENTS.md`.
2. Use `ercm-code-review` against the fixed point for both Standards and Spec. If parallel sub-agents are unavailable, run the two axes sequentially with independent notes.
3. Fix actionable findings and rerun affected checks.
4. Create the required append-only member activity log with exact verification status.
5. Review `git diff` and staged scope; commit the ticket and log together on the current work branch. Mention the Issue in the commit.

## 4. Stop at the publication boundary

Do not push or open a PR without the user's explicit approval for that public action. Report:

- ticket title/URL and branch/commit;
- delivered canonical assets;
- verification and review results;
- remaining gates or follow-ups;
- the exact proposed push/PR action awaiting approval.

Do not close the Issue at local completion. After an authorized PR is merged and required CI passes, remove `workflow:in-progress`, record the merged evidence, and close the ticket (or let an explicit closing keyword do so).
