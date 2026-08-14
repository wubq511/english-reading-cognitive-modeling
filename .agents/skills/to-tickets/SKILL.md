---
name: to-tickets
description: Break an approved implementation, experiment, or hybrid spec into independently verifiable GitHub evidence-slice tickets with native parent and blocking relationships. Invoke explicitly with the spec Issue or EXP file.
disable-model-invocation: true
---

# To Tickets

Tickets are **evidence slices**, not merely coding slices. A complete slice may deliver a sourced decision, a rights-cleared asset, an experiment design/run, data, software, or governance evidence. It must fit one fresh Agent context and be independently verifiable.

## Required context and gate

Run project preflight; read `docs/agents/research-workflow.md`, `docs/agents/issue-tracker.md`, the full spec and comments, relevant canonical owners, and applicable protocols.

Refuse decomposition when:

- the source is a Wayfinder map with unresolved decisions;
- an implementation spec is not approved for decomposition;
- an experiment spec is absent, not versioned as `EXP-*`, or not explicitly frozen/reviewed;
- the claimed work depends on unresolved rights, source, human-research, sensitive-data, or AI gates that are not represented as blockers.

## Slice types

Apply exactly one primary `work:<type>` label:

- `research` — a sourced research asset or decision evidence;
- `source` — acquisition, identity, rights, catalog, or item/data closure;
- `experiment` — frozen design, fixture, run, analysis, or validity result;
- `code` — executable runtime, instrument, pipeline, or test behavior;
- `data` — versioned project-generated dataset or transformation;
- `governance` — protocol, ADR, audit, or collaboration control.

UI work is not automatically `code`: UI measurement design can be research or experiment work, while implementation of the frozen instrument is code.

## Evidence-slice rules

Each ticket must:

- deliver one complete, reviewable outcome rather than one technical layer;
- name its canonical inputs and outputs without copying their contents;
- define commands or evidence that prove completion;
- state the strongest claim the result may support and claims it cannot support;
- name applicable source, rights, AI, human, data, and publication gates;
- list native blocking edges and external unblock conditions;
- preserve negative/null outcomes as valid completion where scientifically appropriate;
- fit one fresh Agent context.

Wide mechanical refactors may use expand–migrate–contract tickets when no green vertical slice exists. Do not use this exception for vague research phases.

## Ticket template

```markdown
## Parent contract
<linked spec title and canonical artifact, if any>

## Outcome
<one independently reviewable result>

## Why this slice exists
<downstream question or capability it unlocks>

## Canonical inputs
<stable IDs and owner links>

## Work and deliverables
<research, code, data, experiment, or governance scope>

## Acceptance and verification
- [ ] <observable criterion plus command/evidence>

## Evidence and claim boundary
<allowed claim, forbidden overclaim, null/negative handling>

## Gates
<source/rights/AI/human/data/publication state and unblock condition>

## Blocked by
<linked ticket titles or None>

## Out of scope
<explicit boundary>
```

## Process

1. Draft dependency-ordered slices and check that every spec acceptance condition is owned exactly once.
2. Present a numbered breakdown with title, type, blockers, outcome, verification, and gate. Ask whether granularity and edges are correct; revise until approved.
3. Create one GitHub Issue per approved slice in blocker-first order.
4. Attach each to the spec tracking Issue as a native sub-issue and add native dependency edges in a second pass.
5. Apply `workflow:ticket`, one `work:<type>`, and `ready-for-agent` only when the contract is sufficiently specified. An open native dependency or external gate still keeps it off the executable frontier.
6. Read relationships and labels back. Report the frontier as open, unblocked, unassigned, sufficiently specified tickets.
7. Do not modify/close the parent spec, claim a ticket, or begin work.
