---
name: ercm-to-spec
description: Turn a resolved ERCM Wayfinder map or already-decided conversation into a reviewable implementation, experiment, or hybrid contract, with a GitHub Issue as the collaboration surface. Invoke explicitly only after important decisions are settled.
disable-model-invocation: true
---

# To Spec

Synthesize decisions; do not reopen the interview. If a consequential choice is still unresolved, stop and route it to Wayfinder rather than hiding an assumption in the spec.

## Required context

Run project preflight and read:

- `docs/agents/research-workflow.md`
- `docs/agents/issue-tracker.md`
- the source map/conversation and all decision resolutions it links
- `CONTEXT.md`, relevant ADRs, policies, and canonical research owners
- `experiments/README.md` and `experiments/templates/EXPERIMENT_SPEC.md` for scientific experiments

## Classify the contract

Classify by what must be frozen, not by whether code or literature appears:

1. **Implementation/instrument spec** — software, UI instrument, schema, pipeline, or operational behavior. The GitHub spec Issue body is canonical.
2. **Experiment spec** — hypothesis, estimand, comparison, data, split, metric, or validity test. A versioned `experiments/specs/EXP-*` file is canonical; its GitHub Issue is the publication, ownership, status, and discussion surface.
3. **Hybrid spec** — both contracts are needed. Create one parent spec Issue and two linked child contract surfaces: an implementation spec Issue and an experiment tracking Issue pointing to the canonical `EXP-*` file.

Every form must have a GitHub Issue. Never maintain duplicate scientific spec prose in the Issue and the file.

## Preconditions

Before writing, prove:

- the source map has no open decision frontier or in-scope fog, or the current conversation already resolved equivalent decisions;
- the intended external behavior or scientific estimand is testable at a named seam;
- rights, AI, human, sensitive-data, and source gates are classified;
- the contract has a named owner and an explicit out-of-scope boundary.

If any precondition fails, report the exact missing decision/gate and the next `/ercm-wayfinder` or `$ercm-wayfinder` command.

## Implementation spec body

```markdown
## Problem and outcome
## Actors and externally observable stories
## Frozen behavior and interfaces
## Data, evidence, and provenance contract
## Acceptance and failure criteria
## Verification seams and prior art
## Governance gates
## Out of scope
## Decision sources
```

Use extensive numbered stories only where they add observable coverage. Do not include volatile file paths or implementation snippets unless a prototype encodes a decision more precisely than prose.

## Experiment spec

1. Allocate the next unused stable `EXP-*` ID; never recycle an ID.
2. Copy the repository template and complete every field with a value or explicit `UNKNOWN`/`N/A`.
3. Keep status `PROPOSED` until independent review confirms inputs, claim boundary, split, metrics, gates, and decision rule. `ercm-to-spec` does not invent approval.
4. Create the GitHub tracking Issue with the experiment ID, question, allowed claim, owner, status, target path, gates, and review requirement. Link it back from the file.
5. The issue must say when the artifact is still local/branch-only. Do not imply public availability before merge.

## Publish and verify

1. Draft all bodies/files before external writes. Every spec Issue body opens with the plain-language `速览` block owned by the Readability contract in `docs/agents/issue-tracker.md`.
2. Publish Issues using the labels and relationships in `docs/agents/issue-tracker.md`.
3. Read every Issue back, verify labels/links/parentage, and report the titled URLs plus canonical artifact paths.
4. Do not apply `ready-for-agent`; a spec must pass review and then be decomposed by `ercm-to-tickets`.
5. Do not push a branch or open a PR unless the user separately authorized that public action.
