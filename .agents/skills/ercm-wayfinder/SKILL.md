---
name: ercm-wayfinder
description: Plan an ERCM project-sized research or engineering effort as one GitHub parent map and decision child tickets, or resolve one decision ticket, until the route to a spec is clear. Invoke explicitly with a destination, map, or decision ticket.
disable-model-invocation: true
---

# Wayfinder

Wayfinder resolves **decisions**, not delivery work. A decision may require literature, code, data inspection, a prototype, or a human discussion; that does not turn it into an implementation ticket.

## Required context

Run project preflight, then read these files completely:

- `docs/agents/research-workflow.md`
- `docs/agents/issue-tracker.md`
- `CONTEXT.md`
- the canonical project owner documents relevant to the destination

Use project terms and evidence states. Historical chats are not a normal planning source.

## Invariants

- The map is one GitHub Issue labelled `wayfinder:map`.
- Every known decision is a GitHub sub-issue with exactly one `wayfinder:<type>` label: `research`, `prototype`, `grilling`, or `task`.
- The map is an index. A decision answer lives once, in its decision record under `reports/decisions/` (ADR 0008); the child ticket carries the discussion plus a resolution summary linking the record, and the map contains only a one-line titled link.
- Native GitHub sub-issues and dependencies are canonical. Follow `docs/agents/issue-tracker.md`; do not invent another tracker.
- Refer to issues as linked titles in prose, not bare numbers.
- Do not execute the destination, create implementation tickets, freeze an experiment, or claim scientific validity.
- Work at most one non-research decision ticket in a session.

## Map shape

```markdown
## Destination

<the reviewable contract or decision this map must make possible>

## Notes

<canonical owners, required policies, standing constraints>

## Decisions so far

<!-- one linked title and one-line gist per resolved child; no duplicated answer -->

## Not yet specified

<in-scope fog that cannot yet be phrased as a precise question>

## Out of scope

<conscious boundaries for this map>
```

## Decision ticket shape

```markdown
## Question

<one decision or investigation that fits one fresh Agent context>

## Why this blocks the destination

<the downstream contract that cannot be frozen without the answer>

## Required evidence and gates

<canonical files, source IDs, data/ethics/rights conditions, or human authority>

## Resolution contract

<what a sufficient answer must record, including alternatives and uncertainty>
```

## Ticket types

- `wayfinder:research` — primary-source or local-evidence investigation that answers a decision. Use `ercm-research`. An LLM summary is not evidence.
- `wayfinder:prototype` — a disposable artifact that makes behavior or UI concrete enough for a human decision. Use `ercm-prototype`; never treat prototype data as study evidence.
- `wayfinder:grilling` — a decision owned by a human. Use `ercm-grilling` and the project vocabulary from `ercm-domain-modeling`; never answer the human side yourself.
- `wayfinder:task` — access, acquisition, inspection, or other work needed before a decision can be answered. It must unblock a decision, not deliver the final system.

## Invocation A — chart a map

The user supplies a loose destination.

1. Use `ercm-grilling` to settle the destination and scope. Use `ercm-domain-modeling` when terminology is unstable. Do not edit or publish until the user confirms shared understanding.
2. Breadth-first, identify all currently precise decisions and the remaining fog. Do not pre-slice unknown territory.
3. If the whole path already fits one session and contains no meaningful fog, stop and route to `ercm-to-spec`; do not manufacture a map.
4. Draft the parent map and currently visible child tickets. Classify each decision and draft dependency edges.
5. Show the draft to the user. Publishing GitHub issues is external state; use the confirmation already given in the current invocation or obtain it before the first write.
6. Create the parent, create all children, then attach native sub-issue and dependency relationships in a second pass. Verify every relationship by reading it back.
7. Stop. Do not auto-run the research tickets; they are now available for team allocation.

## Invocation B — advance a map

The user supplies a map and exactly one child decision ticket.

1. Load the map at low resolution and query its open children and dependencies.
2. If only the map is supplied, inspect its decision frontier read-only and report up to three titled options. Recommend one based on the user's stated destination, downstream decisions unlocked, evidence/gate readiness, and fit with the requested work; explain why the alternatives may be chosen instead. Then stop and ask the user to name one child. Recommendation is selection assistance, not assignment or permission to work.
3. Assign the named decision ticket to the current GitHub user before work. Never take a ticket assigned to someone else.
4. Resolve the question using the ticket type and required evidence. Preserve rejected alternatives, uncertainty, null findings, and project claim states.
5. Present a review briefing in chat and wait for the user's review before any GitHub write: headline findings, how they were produced, which file and section holds which result, and the open residuals. The human research member is the reviewer of record — a resolution they have not seen is not a resolution. For research children the briefing content follows `ercm-research` step 9.
6. After the user's sign-off, write the decision record at `reports/decisions/wayfinder-<issue>-<slug>.md` (answer; evidence/assets; rejected alternatives; uncertainty/gates; downstream implications), land it on the default branch through the repository's review path, then post one resolution summary comment linking the record.
7. Close the child, append only its linked-title gist to `Decisions so far`, and verify the map.
8. Create newly visible decision tickets and dependency edges; move clarified fog into tickets and remove it from `Not yet specified`.
9. When the frontier and fog are empty, mark the map ready for `ercm-to-spec`. Do not write the spec in the same invocation.

If new evidence contradicts an earlier decision, create or reopen a decision ticket and record supersession. Never silently rewrite the old resolution.
