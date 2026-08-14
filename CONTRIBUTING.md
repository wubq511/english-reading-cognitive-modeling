# Contributing

## Before research or changes

```bash
scripts/bootstrap
scripts/verify
```

Windows 使用 `.\scripts\bootstrap.cmd` 与 `.\scripts\verify.cmd`。若工作来自团队规划，先用 `ercm-workflow` 判断阶段；只领取用户明确指定的 GitHub evidence-slice ticket。完整状态机和 tracker 规则见 `docs/agents/`。

Read `AGENTS.md`, `CONTEXT.md`, `reports/project_state/CURRENT_STATE.md` and the protocol relevant to the work. Do not use `webchat_raw_materials/` as the normal continuation point.

## Evidence discipline

- Use stable source IDs from `sources/catalog.yaml` and cite page/section/table/figure for consequential claims.
- Label project synthesis as `PROJECT-INFERENCE`; do not present it as a paper's original conclusion.
- Preserve negative, ambiguous and unknown results. Do not tune away `UNKNOWN` for a cleaner narrative.
- A method choice that depends on local data remains an `EXPERIMENT-GATE` until compared under frozen data, splits, metrics and budget.
- AI-assisted work follows `reports/protocols/AI_RESEARCH_TOOLING_POLICY.md`; human-participant work follows `reports/protocols/HUMAN_RESEARCH_GATES.md`.

## Adding an external source

1. Human-acquired papers go only to `tmp/pdfs/`; do not rename or place them in the canonical library manually.
2. The Agent determines exact work/version/type and records DOI/title/authors/year/venue, acquisition, rights, SHA and parser QA.
3. Update `sources/catalog.yaml` and `sources/checksums.sha256`, then run `scripts/sources inbox`.
4. Update crosswalks or reports that use the source; run `scripts/sources doctor` and `scripts/verify`.

Public Git does not include source originals by default. Any file requires version-specific redistribution evidence and separate release approval; local access or “free to read” is not enough.

## Adding a claim or experiment

Each major claim should identify:

- what was directly observed;
- what was derived or inferred;
- the evidence and applicability scope;
- competing explanations and failure conditions;
- what would falsify it;
- the artifact or command that reproduces it.

Experiment design and run outputs follow `experiments/README.md`; do not invent a parallel manifest format.

## Data safety

Never commit secrets, identity maps, consent forms, human raw logs, recordings, Webcam/eye-tracking data or pseudonymized participant records. If uncertain, stop and classify the data before copying it into the workspace.
