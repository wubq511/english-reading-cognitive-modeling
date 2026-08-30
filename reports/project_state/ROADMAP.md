# 研究路线图

本路线保留历史 Phase 名称以便追溯，但使用稳定子命名空间：采集 `COL-*`、系统层 `SYS-*`、数据角色 `DATA-*`、实验族 `BENCH-*`。历史聊天中的同名 `L0/L1/L2`、`D3` 和 E0–E10 不再作为 canonical 标识。

本文件只维护依赖顺序与退出门禁；当前完成度统一见 [`CURRENT_STATE.md`](CURRENT_STATE.md)。

## 依赖链

```text
Phase 0 Item/Data closure
  -> Phase 1 observability specification
  -> Phase 2A measurement infrastructure
  -> Phase 3 development data + benchmark
  -> Phase 4 implementation + BENCH-E0 + 内部信号冒烟（2026-08-30 #10 收窄；E1/E2 正式 benchmark 移到 pilot 后）
  -> Phase 5 H2-approved human pilot
  -> Phase 2B item-specific protocol freeze
  -> Phase 6 main human validity study
  -> Phase 7 student-model benchmark
  -> Phase 8 external generalization
  -> AI vertical/horizontal extensions
```

Phase 1 和 Phase 2A 已有设计资产，但依赖链中的“完成”仍要求本地实现或实验，不因网页讨论而自动满足。

## Phase 0 — 题目与数据资产

退出门禁：

- 至少一组可实际使用、权利清楚的 passage/item packages；
- passage、question、options、answer、evidence spans、候选 item/skill tags 完整；
- 自动文本难度只用于预筛，item 难度由真人 pilot 估计；
- external datasets 的字段、许可、下载、可迁移统计量和限制清楚；
- Candidate Bank 与 pilot 选题规则版本化。

## Phase 1 — 认知目标与可观测性

退出门禁：

- 每个 target 有可观测证据、不可识别反例、输出类型和所需 validation；
- 强制 `UNKNOWN/AMBIGUOUS/UNVALIDATED/UNIDENTIFIABLE`；
- 题目类型与可观测性梯度明确。

## Phase 2A — 测量与验证基础设施

退出门禁：

- object-centric append-only raw schema；
- wall clock + monotonic time + sequence；
- deterministic state timeline 与 log-derived replay；
- open-to-focused stimulated recall；
- participant/coder/system evidence 分离；
- 原始 disagreement、blinding 和 provenance 保留。

## Phase 3 — 开发数据与 benchmark 规范

数据角色：

- `DATA-D0`：外部参照数据；
- `DATA-D1`：工程合成数据；
- `DATA-D2`：经验校准的半合成数据；
- `DATA-D3`：H2 真人 pilot；
- `DATA-D4`：真人主要研究；
- `DATA-D5`：泛化样本。

## Phase 4 — 实现与低层 benchmark

顶层族：

- `BENCH-E0`：日志/回放效度；
- `BENCH-E1`：焦点估计；
- `BENCH-E2`：动作分割；
- `BENCH-E3`：过程/策略恢复；
- `BENCH-E4`：行为→认知构念效度；
- `BENCH-E5`：学生认知/技能模型；
- `BENCH-E6`：端到端消融。

## 横切主线 — UI 作为测量仪器

UI 不是 Phase 4 的普通前端子任务，而是贯穿 Phase 1/2A/4/5/6 的实验仪器：

1. Phase 1 明确 natural-reading constraints、可观测性、accessibility、设备/浏览器范围和可能改变 estimand 的 UI 因素；
2. Phase 2A 冻结 interaction/state/event contract，使 variant 之间的 logging、replay 和 provenance 可比；
3. Phase 4 通过 `BENCH-E0` 验证各支持环境的日志完整性、确定性重建和 replay fidelity；
4. H1 smoke 只排工程缺陷，数据不得用于选择“更优”UI；
5. Phase 5 在 H2 批准后，以预先声明的 variant、分配、outcome 和分析比较 usability、missingness、行为改变与测量可靠性；
6. 探索性 pilot 选出的 UI 必须在 held-out 样本或后续预注册研究中确认，之后才能冻结为 main-study baseline instrument；
7. UI 引起的测量变化与真正的认知/学习效果分开估计，视觉偏好、完成时间或预测准确率不能单独决定 instrument 优劣。

本主线（lane）的研究问题由 [`RESEARCH_QUESTIONS.md`](RESEARCH_QUESTIONS.md) 的 RQ0 所有；工作流与 artifact gate 见 [`docs/agents/research-workflow.md`](../../docs/agents/research-workflow.md)。

## Phase 5 / Phase 2B — 先 pilot，再题目专属冻结

Phase 5 只有具备 H2 批准、题目资产和数据管理安排后才能开始。pilot 前最低实现范围为 `BENCH-E0`（日志/重建/回放）加一次内部 H0 数据上的切分/焦点信号存在性冒烟（go/no-go，不冻结模块）；`BENCH-E1/E2` 正式 benchmark 移到 pilot 后用 D3 数据完成（2026-08-30 #10 决定，依据：采集不可逆、派生可重算，切分候选方法需真实数据定胜负）。pilot 估计可行性、分布、题目难度、回忆/标注可用性与测量失败。pilot 之后，Phase 2B 冻结题目 EvidenceMaps、探针（probes）、分类体系（taxonomy）、阈值、样本量与主要研究分析。

## Phase 6–8 — 效度、学生模型与泛化

- Phase 6 在人类参照证据上检验行为→认知解释。
- Phase 7 只允许经验证的过程指标进入学生模型，并与仅响应 baseline（response-only baseline）比较。
- Phase 8 检验新的学生、文章（passages）、题目、题型与队列（cohorts）。

## AI 扩展门禁

AI 扩展工作只能在对应 baseline 组件冻结接口、指标、划分（split）和结果之后开始。每条 AI 分支必须说明它是深化现有能力还是新增能力，并且必须遵循 `AI_RESEARCH_TOOLING_POLICY.md`。
