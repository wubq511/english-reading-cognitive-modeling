# ADR 0009: Allow explicit owner waivers for task-scoped source gates

Status: Accepted
Date: 2026-09-05

## Context

The repository correctly defaults to fail-closed source handling: local verification requires every catalogued required source and an empty acquisition inbox, while Wayfinder decisions normally require their named document and source/provenance/rights deliverables. Two different concerns had become coupled:

- a collaborator could not push an otherwise valid tracked public snapshot when their clone intentionally did not contain all local-only source originals; and
- a task could not close when the project owner intentionally removed document acquisition or source/rights-record closure from that task's deliverable.

Treating either absence as successful verification would destroy provenance. Treating both as permanently non-waivable would make the workflow unable to represent a legitimate, narrower owner decision.

## Decision

Keep the complete local path as the default. Add two explicit, scoped alternatives:

1. A one-shot push may set `ERCM_VERIFY_MODE=public` after the user explicitly states that local raw/PDF files are not required for that push. The pre-push hook then runs `scripts/verify --public`, which validates the tracked public snapshot, catalog/checksum structure, skills, logs and links without requiring local originals or an empty local inbox.
2. A named Wayfinder/spec/ticket gate for document completeness or source/provenance/rights-record closure may be resolved as `WAIVED_BY_OWNER` only after the current user explicitly names the task and omitted gate. The owning artifact records the exact scope, date, authority, narrowed deliverable/claim boundary and downstream reopen condition.

A waiver is not a successful source or rights check. Missing documents stay missing; unknown metadata stays unknown; and downstream work cannot cite the waiver as evidence. Public distribution continues to require separate approval for the exact material. Human-research approval, consent, privacy and sensitive-data controls, security, technical acceptance, CI and human review are not eligible for this waiver.

## Consequences

- Clones without the local research library can submit a verified public-only change without weakening the default local workflow.
- Project-owner scope decisions can close a task honestly as a narrowed deliverable instead of being mislabeled as blocked or verified.
- `ERCM_VERIFY_MODE=public` is intentionally per-process rather than a persistent repository setting.
- The decision record or ticket must expose `WAIVED_BY_OWNER`; silence and urgency never activate the alternative.
- A later task that needs an omitted source, provenance fact or rights claim must re-open the corresponding gate.

## Supersedes

This refines, but does not replace, ADR 0003's fail-closed source-manifest design. ADR 0003 remains authoritative for source identity, file validation and redistribution status whenever those artifacts are in scope.
