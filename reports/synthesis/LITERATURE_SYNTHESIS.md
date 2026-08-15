# 文献综合：现有语料能支持什么

> 语料：44 份 A–E PDF + 18 份 UI 交互 PDF
> 完整论文映射：`sources/catalog.yaml`
> 详细证据：现有深读报告及其 Evidence Indexes

本文件不重写 8,000+ 行深读报告，只固定各文献组在系统中的证据角色及不能外推的边界。

## A — 过程序列到潜在测量

A 组支持：经过任务语义抽象的 action/state sequence 可以进入 state-response、continuous-time、mixture、HMM/network 等测量或行为异质性模型。

它没有解决：原始 UI logging、阅读特定 action segmentation、cursor/focus、action→reading skill 的独立效度。Latent state 的数学可辨识或 model fit 不等于被命名 cognition 已验证。

## A+ — 有效性、计时与更新的过程模型

A+ 展示从 expert-defined effectiveness 到 graph/probability/reward 等多种 action value 表达，并联合 action/time 或 growth。

主要风险：effectiveness 由 outcome 或设计规则定义时，容易把成功路径假设循环写进能力；新 passage/task 泛化仍是核心未决。A+5 是 preprint，证据权重低于正式同行评审研究。

## B — 阅读特定过程证据

B 组最稳健的贡献是把 navigation、pause、reread、search 等放回 reading task demand、item type、student skill 与时间上下文。

它支持 behavior→contextualized process evidence，而不支持把 revisit、pause 或 navigation 单独等价为 skill/difficulty/strategy。阅读任务中的 underline 与 option elimination 仍缺足够直接认知语义证据。

## C — 指针作为情境辅助证据

C 组支持 cursor/pointer 在部分任务中包含 visual-attention 或 interaction-intent 信息，但关系强烈依赖任务、active/inactive use 和个人习惯。

它不支持 cursor=gaze、点级 focus 真值或全局固定权重。自然双栏、滚动英语阅读是现有文献的外推边界，必须做本项目 ablation。

## D — 抽象与分段

D 组区分 denoising、boundary detection、segmentation 和 activity recognition；rare event 不等于 noise，statistical change point 不等于 semantic boundary。

确定性 semantic action 无需 ML segmentation；连续流可比较 rules、grammar、CPD、HMM、HSMM 与 hybrid。现有语料没有本项目 reading UI 上的共同 head-to-head winner。

## E — 认知诊断与构念效度

E 组支持 process data 在特定设计下增加 diagnostic information，也展示 key action/Q-matrix、RT/fixation、joint modeling 与 trace/verbal triangulation。

同时它明确暴露：key action→attribute 多由研究者预设；Q-matrix 是输入假设；diagnostic utility、model fit、simulation 和 correlation 都不能单独证明 psychological interpretation。Trace、think-aloud 和 recall 各有误差且不互换。

## UIB — 日志、任务抽象与模式发现

UIB 语料提供 object-centric logging、interaction abstraction、grammar/task-level events、trace clustering、process mining 与动态 focus 的跨领域方法词汇。

它们主要支持系统设计和候选方法，不直接验证英语阅读 cognition。旧“论文 1–18”与 UIB ID 的映射见 `SOURCE_REPORT_CROSSWALK.md`。

## 综合证据链

```text
UIB + D: raw event -> semantic behavior
B + C: behavior -> contextual focus/process evidence
E: mapping validity gate
A + A+: validated evidence -> latent/student model candidates
```

每个箭头都可能是 `DIRECT`、`PROBABILISTIC`、`VALIDATION-REQUIRED` 或 `UNKNOWN`。跨组综合是项目推论，不是某篇论文直接给出的完整架构。

## 仍缺失的证据

- 本项目双栏 UI 的 raw/replay 与 segmentation benchmark；
- pointer 的真实边际价值和个体校准；
- Search/Verification 等构念的 blinded human reference；
- validated process evidence 对 response-only student model 的泛化增量；
- 题目/数据资产及其权利、难度与 observability gradient；
- Phase 0 和方法学新增来源的本地全文与许可审计。
