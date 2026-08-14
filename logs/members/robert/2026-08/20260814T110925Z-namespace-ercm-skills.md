---
schema_version: 1
member_id: robert
timestamp: 2026-08-14T11:09:25Z
category: governance
summary: Namespace ERCM workflow skills and add read-only ticket recommendations
supersedes: NONE
---

## Work completed

- Renamed all 13 repository-adapted skills to the ercm- namespace, migrated generated Claude mappings safely, and updated Wayfinder, Workflow, and Implement so missing ticket selection yields bounded recommendations without assignment or execution.

## Research or decision impact

- Codex and Claude Code can distinguish project adaptations from global upstream skills; team members receive actionable ticket guidance while retaining explicit human selection and claim control.

## Verification

- PASS: 55 unit tests; scripts/skills install; scripts/skill-evals doctor; local/public scripts/verify; workflow labels-check; Codex ercm-wayfinder and Claude ercm-implement no-claim dry runs.

## Follow-ups

- Publish the approved branch, open a draft PR, require verify plus macOS/Windows skill-portability CI, then update completion evidence.
