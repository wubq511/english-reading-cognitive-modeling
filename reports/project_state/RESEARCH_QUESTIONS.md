# Research Questions

## Primary question

在不使用 LLM、生成式 AI 或 Agent 作为 runtime 推断组件，且不显著改变学生自然英语阅读作答方式的条件下，UI 过程证据能够以什么精度、校准度和效度支持：

1. 可观察行为恢复；
2. 处理区域与过程假设估计；
3. 经独立验证的认知解释；
4. 跨题阅读技能或 latent trait 判断？

“能够预测”与“具有所声称的认知含义”是两个不同问题，必须分别回答。

## RQ0 — UI instrument effects

- 答题 UI 的布局、导航、滚动、划线、排除、反馈与设备适配如何改变自然阅读行为、事件缺失、时序和可观测性？
- 哪些差异只是 usability preference，哪些会改变测量可靠性、estimand 或构念解释？
- 在固定任务、题目、日志 schema 和分析规则下，不同 UI variant 对 replay fidelity、完成率、missingness、行为分布和下游指标有什么影响？

Success evidence: 先通过开发者工程验证和 `BENCH-E0` 仪器可靠性；涉及团队外参与者的 variant 比较必须进入 H2。探索性 pilot 可选择候选 UI，但同一数据不得同时充当确认性效果证据。

## RQ1 — Measurement fidelity

- 原始事件是否完整、有序、可跨浏览器/设备解释？
- Raw event 能否无损重建 UI state 和 replay？
- resize、zoom、后台 tab、重复、缺失和乱序事件如何影响恢复？

Success evidence: deterministic invariants、replay diff、已知工程 oracle。这里不涉及 cognition。

## RQ2 — Behavioral abstraction

- 哪些 semantic actions 可确定性恢复？
- scroll/pointer 等连续流如何切 episode？
- boundary detection 与 activity labeling 分别达到什么水平？

Candidate methods remain an `EXPERIMENT-GATE`: rules/FSM/grammar、change-point、HMM、HSMM 与 hybrid。

## RQ3 — Focus observability

- 只用 viewport、scroll、selection、pointer、题目状态和历史，能恢复到 page、region、paragraph 还是 sentence 粒度？
- pointer 的边际信息量是否因学生、设备和状态变化？
- selective prediction 下的 risk–coverage 边界是什么？

输出必须是 belief/uncertainty，可 abstain；不得把 cursor 或 viewport 当 gaze。

## RQ4 — Process hypotheses

- 哪些轨迹能够区分 Evidence Search、Verification、Monitoring、Memory Refresh 和 Difficulty？
- 在哪些 item types、学生和 evidence structures 上，它们 observationally indistinguishable？
- discovery patterns 是否能在新样本复现并获得独立语义验证？

Success evidence: blinded human reference、replay/recall triangulation、跨 item/student split、calibration 和 alternative explanations。

## RQ5 — Construct validity

- 行为到认知 mapping 的内容、response-process、内部结构、外部关系和后果证据是否支持预期解释与用途？
- participant report、coder interpretation、trace 和 optional sensor 在哪里一致或冲突？
- 何时必须输出 `UNVALIDATED`、`AMBIGUOUS` 或 `UNIDENTIFIABLE`？

Predictive utility、model fit、Q-matrix 和 simulation recovery 都不能单独回答本问题。

## RQ6 — Student modeling

- 经验证的 process evidence 是否相对 response-only baseline 提供稳定、可泛化的增量？
- 这种增量能否跨学生、题目、文章、题型和 cohort 保持？
- 更复杂模型是否改善决策，而不只是拟合训练数据？

## RQ7 — AI extension after baseline

Baseline 跑通并暴露瓶颈以后，分两条独立研究线：

- **Vertical enhancement**：AI 是否能在已存在的环节提高指标、校准或效率？
- **Horizontal extension**：AI 是否能支持 baseline 无法完成且有独立效度证据的新任务？

两条线都必须与无 AI baseline 同数据、同 split、同 metric 比较，AI 不能自造真值。
