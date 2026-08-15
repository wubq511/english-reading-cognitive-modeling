# 研究问题

## 主问题

在不使用 LLM、生成式 AI 或 Agent 作为 runtime 推断组件，且不显著改变学生自然英语阅读作答方式的条件下，UI 过程证据能够以什么精度、校准度和效度支持：

1. 可观察行为恢复；
2. 处理区域与过程假设估计；
3. 经独立验证的认知解释；
4. 跨题阅读技能或潜在特质（latent trait）判断？

“能够预测”与“具有所声称的认知含义”是两个不同问题，必须分别回答。

## RQ0 — UI 仪器效应

- 答题 UI 的布局、导航、滚动、划线、排除、反馈与设备适配如何改变自然阅读行为、事件缺失、时序和可观测性？
- 哪些差异只是可用性偏好（usability preference），哪些会改变测量可靠性、estimand 或构念解释？
- 在固定任务、题目、日志 schema 和分析规则下，不同 UI variant 对回放保真度（replay fidelity）、完成率、缺失（missingness）、行为分布和下游指标有什么影响？

成功证据：先通过开发者工程验证和 `BENCH-E0` 仪器可靠性；涉及团队外参与者的 variant 比较必须进入 H2。探索性 pilot 可选择候选 UI，但同一数据不得同时充当确认性效果证据。

## RQ1 — 测量保真度

- 原始事件是否完整、有序、可跨浏览器/设备解释？
- 原始事件（raw event）能否无损重建 UI 状态（UI state）和回放（replay）？
- resize、zoom、后台 tab、重复、缺失和乱序事件如何影响恢复？

成功证据：确定性不变量（deterministic invariants）、回放差异（replay diff）、已知工程 oracle。这里不涉及认知（cognition）。

## RQ2 — 行为抽象

- 哪些语义动作（semantic actions）可确定性恢复？
- scroll/pointer 等连续流如何切片段（episode）？
- 边界检测（boundary detection）与活动标注（activity labeling）分别达到什么水平？

候选方法仍处于 `EXPERIMENT-GATE`：规则/FSM/语法、变点（change-point）、HMM、HSMM 与混合（hybrid）。

## RQ3 — 焦点可观测性

- 只用视口（viewport）、滚动、选择（selection）、指针（pointer）、题目状态和历史，能恢复到页面、区域、段落还是句子粒度？
- 指针的边际信息量是否因学生、设备和状态变化？
- 选择性预测（selective prediction）下的风险-覆盖（risk–coverage）边界是什么？

输出必须是信念/不确定性（belief/uncertainty），可弃权（abstain）；不得把光标（cursor）或视口当注视（gaze）。

## RQ4 — 过程假设

- 哪些轨迹能够区分证据搜索（Evidence Search）、验证（Verification）、监控（Monitoring）、记忆刷新（Memory Refresh）和难度（Difficulty）？
- 在哪些题型（item types）、学生和证据结构（evidence structures）上，它们观测上不可区分？
- 发现模式（discovery patterns）是否能在新样本复现并获得独立语义验证？

成功证据：盲法人类参照（blinded human reference）、回放/回忆三角互证（replay/recall triangulation）、跨题目/学生划分（split）、校准（calibration）和替代解释（alternative explanations）。

## RQ5 — 构念效度

- 行为到认知映射（mapping）的内容、作答过程（response-process）、内部结构、外部关系和后果证据是否支持预期解释与用途？
- 参与者报告（participant report）、编码者解读（coder interpretation）、trace 和可选传感器（optional sensor）在哪里一致或冲突？
- 何时必须输出 `UNVALIDATED`、`AMBIGUOUS` 或 `UNIDENTIFIABLE`？

预测效用（predictive utility）、模型拟合（model fit）、Q 矩阵（Q-matrix）和模拟恢复（simulation recovery）都不能单独回答本问题。

## RQ6 — 学生建模

- 经验证的过程证据（process evidence）是否相对仅响应 baseline（response-only baseline）提供稳定、可泛化的增量？
- 这种增量能否跨学生、题目、文章、题型和队列（cohort）保持？
- 更复杂模型是否改善决策，而不只是拟合训练数据？

## RQ7 — baseline 之后的 AI 扩展

Baseline 跑通并暴露瓶颈以后，分两条独立研究线：

- **纵向增强（Vertical enhancement）**：AI 是否能在已存在的环节提高指标、校准或效率？
- **横向扩展（Horizontal extension）**：AI 是否能支持 baseline 无法完成且有独立效度证据的新任务？

两条线都必须与无 AI baseline 同数据、同 split、同 metric 比较，AI 不能自造真值。
