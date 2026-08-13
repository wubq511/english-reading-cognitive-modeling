# Contributing

## Before research or changes

```bash
scripts/papers doctor
scripts/verify
```

Read `AGENTS.md`, `CONTEXT.md`, `reports/project_state/CURRENT_STATE.md` and the protocol relevant to the work. Do not use `webchat_raw_materials/` as the normal continuation point.

## Evidence discipline

- Use stable paper IDs from `papers/catalog.yaml` and cite PDF page/section/table/figure for consequential claims.
- Label project synthesis as `PROJECT-INFERENCE`; do not present it as a paper's original conclusion.
- Preserve negative, ambiguous and unknown results. Do not tune away `UNKNOWN` for a cleaner narrative.
- A method choice that depends on local data remains an `EXPERIMENT-GATE` until compared under frozen data, splits, metrics and budget.
- AI-assisted work follows `reports/protocols/AI_RESEARCH_TOOLING_POLICY.md`; human-participant work follows `reports/protocols/HUMAN_RESEARCH_GATES.md`.

## Adding a paper

1. Determine the exact work and version; record DOI/title/authors/year/venue.
2. Record `source_url`, `download_url`, `redistribution_status`, SHA-256, parser QA and reports that use it.
3. Use `scripts/papers import ID FILE`; do not manually overwrite an existing PDF.
4. Update crosswalks if an old report basename or numbering system refers to the work.
5. Run `scripts/papers doctor` and `scripts/verify`.

Public Git does not automatically include paper PDFs. A PDF requires version-specific redistribution evidence and separate release approval; local access or “free to read” is not enough.

## Adding a claim or experiment

Each major claim should identify:

- what was directly observed;
- what was derived or inferred;
- the evidence and applicability scope;
- competing explanations and failure conditions;
- what would falsify it;
- the artifact or command that reproduces it.

Experiment outputs should preserve code commit, environment, data/catalog hash, split manifest, config, seeds, metric version and result hashes.

## Data safety

Never commit secrets, identity maps, consent forms, human raw logs, recordings, Webcam/eye-tracking data or pseudonymized participant records. If uncertain, stop and classify the data before copying it into the workspace.
