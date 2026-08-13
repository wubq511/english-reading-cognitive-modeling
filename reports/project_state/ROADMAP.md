# Research Roadmap

本路线保留历史 Phase 名称以便追溯，但使用稳定子命名空间：采集 `COL-*`、系统层 `SYS-*`、数据角色 `DATA-*`、实验族 `BENCH-*`。历史聊天中的同名 `L0/L1/L2`、`D3` 和 E0–E10 不再作为 canonical 标识。

## Dependency chain

```text
Phase 0 Item/Data closure
  -> Phase 1 observability specification
  -> Phase 2A measurement infrastructure
  -> Phase 3 development data + benchmark
  -> Phase 4 implementation + BENCH-E0/E1/E2
  -> Phase 5 H2-approved human pilot
  -> Phase 2B item-specific protocol freeze
  -> Phase 6 main human validity study
  -> Phase 7 student-model benchmark
  -> Phase 8 external generalization
  -> AI vertical/horizontal extensions
```

Phase 1 和 Phase 2A 已有设计资产，但依赖链中的“完成”仍要求本地实现或实验，不因网页讨论而自动满足。

## Phase 0 — Item and data assets

Exit gate:

- 至少一组可实际使用、权利清楚的 passage/item packages；
- passage、question、options、answer、evidence spans、候选 item/skill tags 完整；
- 自动文本难度只用于预筛，item 难度由真人 pilot 估计；
- external datasets 的字段、许可、下载、可迁移统计量和限制清楚；
- Candidate Bank 与 pilot 选题规则版本化。

Current: `OPEN`。Primary-source/access audit 已完成，J. Intell. 正文/S2 与 Jin & Liu 作者稿已落地；但尚无权利清晰、答案与 evidence spans 完整的可用 item package。

## Phase 1 — Cognitive target and observability

Exit gate:

- 每个 target 有可观测证据、不可识别反例、输出类型和所需 validation；
- 强制 `UNKNOWN/AMBIGUOUS/UNVALIDATED/UNIDENTIFIABLE`；
- 题目类型与可观测性梯度明确。

Current: `SOURCE-RECOVERED DESIGN`，待实施与真人验证。

## Phase 2A — Measurement and validation infrastructure

Exit gate:

- object-centric append-only raw schema；
- wall clock + monotonic time + sequence；
- deterministic state timeline 与 log-derived replay；
- open-to-focused stimulated recall；
- participant/coder/system evidence 分离；
- 原始 disagreement、blinding 和 provenance 保留。

Current: `DESIGN CLOSED / IMPLEMENTATION OPEN`。

## Phase 3 — Development data and benchmark specification

Data roles:

- `DATA-D0`: external reference data；
- `DATA-D1`: engineering synthetic；
- `DATA-D2`: empirically calibrated semi-synthetic；
- `DATA-D3`: H2 human pilot；
- `DATA-D4`: human main study；
- `DATA-D5`: generalization samples。

Current: `DRAFT`。生成器模型、参数分布和晋级阈值尚未由实验裁决。

## Phase 4 — Implementation and low-level benchmarks

Top-level families:

- `BENCH-E0`: logging/replay validity；
- `BENCH-E1`: focus estimation；
- `BENCH-E2`: action segmentation；
- `BENCH-E3`: process/strategy recovery；
- `BENCH-E4`: behavior→cognition construct validity；
- `BENCH-E5`: student cognitive/skill model；
- `BENCH-E6`: end-to-end ablation。

Current: `NOT STARTED`。

## Phase 5 / Phase 2B — Pilot then item-specific freeze

Phase 5 cannot start until H2 approval, item assets and data-management arrangements exist. The pilot estimates feasibility, distributions, item difficulty, recall/annotation usability and measurement failures. After pilot, Phase 2B freezes item EvidenceMaps, probes, taxonomy, thresholds, sample size and main-study analysis.

Current: `NOT STARTED`。

## Phase 6–8 — Validity, student model and generalization

- Phase 6 tests behavior→cognition interpretations on human reference evidence.
- Phase 7 admits only validated process indicators into student models and compares against response-only baselines.
- Phase 8 tests new students, passages, items, item types and cohorts.

Current: `NOT STARTED`。

## AI extension gate

AI extension work begins only after the corresponding baseline component has a frozen interface, metric, split and result. Each AI arm must state whether it deepens an existing capability or adds a new one, and must follow `AI_RESEARCH_TOOLING_POLICY.md`.
