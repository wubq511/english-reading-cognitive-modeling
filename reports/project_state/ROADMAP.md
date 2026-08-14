# Research Roadmap

本路线保留历史 Phase 名称以便追溯，但使用稳定子命名空间：采集 `COL-*`、系统层 `SYS-*`、数据角色 `DATA-*`、实验族 `BENCH-*`。历史聊天中的同名 `L0/L1/L2`、`D3` 和 E0–E10 不再作为 canonical 标识。

本文件只维护依赖顺序与 exit gate；当前完成度统一见 [`CURRENT_STATE.md`](CURRENT_STATE.md)。

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

## Phase 1 — Cognitive target and observability

Exit gate:

- 每个 target 有可观测证据、不可识别反例、输出类型和所需 validation；
- 强制 `UNKNOWN/AMBIGUOUS/UNVALIDATED/UNIDENTIFIABLE`；
- 题目类型与可观测性梯度明确。

## Phase 2A — Measurement and validation infrastructure

Exit gate:

- object-centric append-only raw schema；
- wall clock + monotonic time + sequence；
- deterministic state timeline 与 log-derived replay；
- open-to-focused stimulated recall；
- participant/coder/system evidence 分离；
- 原始 disagreement、blinding 和 provenance 保留。

## Phase 3 — Development data and benchmark specification

Data roles:

- `DATA-D0`: external reference data；
- `DATA-D1`: engineering synthetic；
- `DATA-D2`: empirically calibrated semi-synthetic；
- `DATA-D3`: H2 human pilot；
- `DATA-D4`: human main study；
- `DATA-D5`: generalization samples。

## Phase 4 — Implementation and low-level benchmarks

Top-level families:

- `BENCH-E0`: logging/replay validity；
- `BENCH-E1`: focus estimation；
- `BENCH-E2`: action segmentation；
- `BENCH-E3`: process/strategy recovery；
- `BENCH-E4`: behavior→cognition construct validity；
- `BENCH-E5`: student cognitive/skill model；
- `BENCH-E6`: end-to-end ablation。

## Cross-cutting lane — UI as a measurement instrument

UI 不是 Phase 4 的普通前端子任务，而是贯穿 Phase 1/2A/4/5/6 的实验仪器：

1. Phase 1 明确 natural-reading constraints、可观测性、accessibility、设备/浏览器范围和可能改变 estimand 的 UI 因素；
2. Phase 2A 冻结 interaction/state/event contract，使 variant 之间的 logging、replay 和 provenance 可比；
3. Phase 4 通过 `BENCH-E0` 验证各支持环境的日志完整性、确定性重建和 replay fidelity；
4. H1 smoke 只排工程缺陷，数据不得用于选择“更优”UI；
5. Phase 5 在 H2 批准后，以预先声明的 variant、分配、outcome 和分析比较 usability、missingness、行为改变与测量可靠性；
6. 探索性 pilot 选出的 UI 必须在 held-out 样本或后续预注册研究中确认，之后才能冻结为 main-study baseline instrument；
7. UI 引起的测量变化与真正的认知/学习效果分开估计，视觉偏好、完成时间或预测准确率不能单独决定 instrument 优劣。

本 lane 的研究问题由 [`RESEARCH_QUESTIONS.md`](RESEARCH_QUESTIONS.md) 的 RQ0 所有；工作流与 artifact gate 见 [`docs/agents/research-workflow.md`](../../docs/agents/research-workflow.md)。

## Phase 5 / Phase 2B — Pilot then item-specific freeze

Phase 5 cannot start until H2 approval, item assets and data-management arrangements exist. The pilot estimates feasibility, distributions, item difficulty, recall/annotation usability and measurement failures. After pilot, Phase 2B freezes item EvidenceMaps, probes, taxonomy, thresholds, sample size and main-study analysis.

## Phase 6–8 — Validity, student model and generalization

- Phase 6 tests behavior→cognition interpretations on human reference evidence.
- Phase 7 admits only validated process indicators into student models and compares against response-only baselines.
- Phase 8 tests new students, passages, items, item types and cohorts.

## AI extension gate

AI extension work begins only after the corresponding baseline component has a frozen interface, metric, split and result. Each AI arm must state whether it deepens an existing capability or adds a new one, and must follow `AI_RESEARCH_TOOLING_POLICY.md`.
