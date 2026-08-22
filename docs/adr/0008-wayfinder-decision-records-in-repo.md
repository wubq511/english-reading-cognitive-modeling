# ADR 0008: Store Wayfinder decision answers as in-repo decision records

Status: Accepted
Date: 2026-08-22

## Context

ADR 0007 made GitHub Issues the collaboration surface for maps, decisions, specs and evidence slices, and the wayfinder skill correspondingly placed the canonical decision answer in the child ticket's resolution comment. Two tensions surfaced while resolving the first decision tickets:

- Decision answers are load-bearing project knowledge (candidate sets, invariant contracts, rejected alternatives, downstream implications), yet issue comments live outside git, are mutable without review, and pass neither PR review nor `scripts/verify`. This is inconsistent with the project's provenance discipline: every other load-bearing class of knowledge has a versioned in-repo canonical owner.
- The project already applies the inverse pattern to dynamic phase status: `reports/project_state/CURRENT_STATE.md` is the canonical owner and Issues carry only links and summaries (`reports/provenance/SOURCE_POLICY.md`). Decision answers were the remaining class whose canonical copy lived only on the tracker.
- Decision aids that are throwaway by nature (prototype code, screenshots) still must not enter `main`; they are decision provenance, not assets.

## Decision

`reports/decisions/` is the canonical owner of Wayfinder decision answers, one Markdown record per resolved decision ticket, named `wayfinder-<issue>-<slug>.md`, following the resolution contract (answer; evidence/assets; rejected alternatives; uncertainty/gates; downstream implications) with a Chinese 结论速览 section.

The decision child Issue remains the collaboration surface: discussion, assignment, labels, dependencies and status. At closure, after the human reviewer of record signs off, the resolution comment carries a summary plus a link to the record; the parent map keeps only a one-line titled-link gist. Records are append-only once merged to `main`; supersession follows the wayfinder rule (create or reopen a decision ticket, record supersession in a new record).

Disposable decision aids (prototype code, screenshots, working materials) stay out of `main`; they are captured on a throwaway branch linked from the record as provenance.

The first resolved ticket under the pre-ADR convention, issue #5, is backfilled: its signed-off resolution comment is copied verbatim into `reports/decisions/wayfinder-5-ui-instrument-effects.md` with provenance noted.

## Consequences

- `docs/agents/research-workflow.md`, `.agents/skills/ercm-wayfinder/SKILL.md` and the canonical-ownership map in `reports/provenance/SOURCE_POLICY.md` are updated to name `reports/decisions/` as the answer owner.
- Closing a decision ticket now includes a repository change landing on `main` through the normal protected-branch path (PR + verify), in addition to the GitHub resolution summary and map gist update.
- Issue comments no longer carry the only copy of a decision answer; they summarize and link.
- Throwaway branches carrying decision aids must remain undeleted while their records reference them.

## Supersedes

This decision supersedes the portion of the wayfinder invariant "a decision answer lives once, in its child ticket resolution" (`.agents/skills/ercm-wayfinder/SKILL.md`, pre-0008) and the corresponding ownership-table row in `docs/agents/research-workflow.md`. Issue-based discussion, assignment and dependency topology are unchanged.
