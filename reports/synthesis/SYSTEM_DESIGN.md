# Baseline System Design

> Status: `SOURCE-RECOVERED + PROJECT-INFERENCE`
> Implementation: not started
> Scientific validation: not started

## 1. Scope

Baseline 要解决的不是“从点击直接读出学生思想”，而是构建一条可审计的测量链：忠实记录交互、恢复 UI 状态、抽象行为、生成有上下文的候选过程证据，最后只让通过独立效度门的证据进入学生模型。

Baseline runtime 不调用 LLM、生成式 AI 或 Agent。研究与实验外环可以使用 AI，但其产物是待验证工件，详见 `AI_RESEARCH_TOOLING_POLICY.md`。

## 2. Low-interference task UI

```text
┌────────────────────────────┬─────────────────────────┐
│ Passage                    │ ‹ Prev  1 2 3 4  Next › │
│                            │                         │
│ Paragraph 1                │ Q1 stem                 │
│ Paragraph 2                │ ○ A ... [eliminate]     │
│ Paragraph 3                │ ○ B ... [eliminate]     │
│ ...                        │ ○ C ... [eliminate]     │
│ select / underline text    │ ○ D ... [eliminate]     │
└────────────────────────────┴─────────────────────────┘
```

Locked properties:

- Passage 独立滚动；右侧一次只显示一道题。
- Prev/Next 与题号跳转并存，允许自由跳题。
- 支持选文、划线/高亮、删除划线、排除/恢复选项、选择和修改答案。
- 不强制固定阅读顺序、逐题提交、解释或 confidence。
- 不采用 Mouselab 式隐藏正文来换取更整洁的观测，因为它会改变自然搜索过程。

`displayed_question_id` 是 UI context，不代表学生此刻只在思考该题；passage action 也不能自动归属给当时显示的题目。

## 3. Collection tiers

| Namespace | Role | Examples | Runtime role |
| --- | --- | --- | --- |
| `COL-L0` | passive interaction | viewport、scroll、navigation、answer history、visibility、timing、pointer | production |
| `COL-L1` | paper-native explicit action | underline/highlight、text selection、option eliminate/restore | production |
| `COL-L2` | explicit cognitive report | stimulated recall、explanation、confidence、interview | research only |

`COL-L2` 不进入常规答题流程，也不是绝对 cognition truth。

## 4. Object-centric raw measurement

Raw event 只记录浏览器可观察事实，不写 `student_confused`、`reading_P2` 或 `found_evidence`。事件可以同时关联 session、passage、paragraph、sentence、question、option 和 annotation；当前显示题目只是 context。

Canonical V1 event vocabulary:

```text
session_started                 session_submitted
question_navigated              answer_option_clicked
option_elimination_toggled      text_selection_committed
underline_created               underline_removed
passage_scroll_sampled          passage_scroll_ended
viewport_changed                visibility_changed
layout_changed                  pointer_sampled
```

每条事件至少保留：

- UTC `wall_time`；
- 单调 `mono_ms`；
- session-local `sequence`；
- event type 与 schema version；
- semantic object IDs；
- 当时 UI/layout context；
- producer/version provenance。

Raw store append-only。纠错或新算法产生新派生版本，不能覆盖原始事件。

## 5. System measurement layers

| Layer | Responsibility | Current decision state |
| --- | --- | --- |
| `SYS-L0` Measurement/Logging | 忠实记录事件、时钟和对象 | structure `LOCKED` |
| `SYS-L1` State Reconstruction | 确定性恢复 UI state 与 replay | structure `LOCKED` |
| `SYS-L2` Behavioral Abstraction | semantic events、composites、continuous episodes | mixed; continuous segmentation is gate |
| `SYS-L3` Focus Estimation | region-level belief + abstention | `EXPERIMENT-GATE` |
| `SYS-L4` Contextual Evidence | behavior + task semantics + temporal context | structure `LOCKED`, mappings open |
| `SYS-L5` Process/Strategy Modeling | hypotheses, patterns, discovery/confirmation | `EXPERIMENT-GATE` |
| `SYS-L6` Cognitive Validity Gate | 决定 mapping 能否支持认知用途 | must exist, `LOCKED` |
| `SYS-L7` Student Model | 跨题整合技能/latent traits | `EXPERIMENT-GATE` |

## 6. Deterministic before probabilistic

无需 ML 的原子行为直接恢复：题目导航、答案选择、选项排除/恢复、划线创建/删除、文本选择。

确定性 composite 由 state diff/FSM/grammar 恢复，例如：

```text
answer B -> answer C = ANSWER_CHANGE(B,C)
eliminate A -> restore A = OPTION_RESTORE(A)
scroll samples -> scroll end = SCROLL_BURST(candidate)
```

只有 scroll/pointer 等连续流需要真正的 segmentation 候选比较。规则、change-point、HMM、HSMM 和 hybrid 均未在本项目同数据 head-to-head；不得提前指定 winner。

## 7. Focus as belief, not gaze

初始状态空间保持粗粒度：`PASSAGE_P1..Pn`、`QUESTION_STEM`、`OPTION_A..D`、`UNKNOWN`。输出为概率分布与证据质量，不是硬真值。

Pointer 只是上下文相关的辅助信号：active pointer、wheel target、selection/underline 通常比停放 cursor 更强；个体使用习惯可能显著改变可靠度。是否使用 global、personal 或 hierarchical calibration 必须由 `BENCH-E1` 裁决。

Webcam/eye tracking 不属于 baseline。它们可以在未来成为独立、经伦理批准的研究子项目，不能作为普通系统依赖。

## 8. Task semantic context

题目包需要显式 metadata：

```yaml
question_id: Q03
candidate_item_type: detail
evidence_spans: [P2-S4]
supporting_paragraphs: [P2]
distractor_metadata: []
candidate_required_processes: []
candidate_skill_tags: []
```

这些是 task prior/design metadata，不是学生实际过程或技能真值。官方 item type、作者意图、Q-matrix 或正确 evidence span 不能自动证明学生采用了对应认知过程。

## 9. Contextual Evidence Packet

裸 feature 不直接进入 cognition model。最小 packet 应绑定：

```yaml
behavior: PASSAGE_REVISIT
interval: {start_ms: 0, end_ms: 0}
focus_distribution: {}
current_item: Q03
target_region: P2
task_relevance: candidate
previous_actions: []
subsequent_actions: []
timing_features: {}
student_baseline: unknown
candidate_interpretations:
  - EVIDENCE_SEARCH
  - VERIFICATION
  - MEMORY_REFRESH
  - DIFFICULTY
  - NORMAL_REREADING
  - UNKNOWN
evidence_quality: unknown
```

同一 revisit/pause/navigation 的解释依赖题目、前后行为、学生与时机，必须保留 competing hypotheses。

## 10. Discovery and confirmatory lanes

Discovery lane 可使用 sequence mining、process mining、DTW、clustering、network、mixture 或 latent-state models。其输出只能先命名为 `Pattern 1`、`Cluster 2`、`Latent State 3`。

Confirmatory lane 只有在理论、任务设计、独立 response-process evidence、reliability 和泛化共同支持后，才将 pattern 命名为 Search、Verification 等 construct 并允许进入 runtime。

## 11. Validation Registry

每个 behavior→cognition mapping 至少记录：

```yaml
mapping_id: MAP-001
behavior: RELEVANT_REVISIT_BEFORE_ANSWER
candidate_construct: EVIDENCE_CHECKING
task_types: []
population: []
evidence_sources: []
human_reference_protocol: null
agreement_and_uncertainty: null
alternative_explanations: []
status: UNVALIDATED
version: 1
```

状态至少包括 `VALIDATED`、`CONDITIONAL`、`UNVALIDATED`、`INVALIDATED`。任何 cognitive conclusion 必须能下钻到 packet、episode、action、state timeline 和 raw events。

## 12. Student model gate

Response-only baseline 永久保留。候选模型包括 response+RT/count、response+validated process indicators、key-action/phantom-item DCM、SRM/MSRM、TEM-like 和 joint process models；目前没有 winner。

只有通过 `SYS-L6/BENCH-E4` 的 process evidence 才可进入 student model。模型拟合更好、分类更准或 simulation recovery 更高，都不能反向证明输入 mapping 的心理含义正确。

## 13. Research plane

研究验证链使用 natural trace + replay + stimulated recall + independent human coding；眼动/Webcam 只是未来可选验证模态。Participant report、coder label、system prediction 和 sensor evidence 分库存储并保留分歧。详情见 `MEASUREMENT_VALIDATION_FRAMEWORK.md` 和 `HUMAN_RESEARCH_GATES.md`。

## 14. Traceability to recovery sources

本设计的主要恢复锚点记录在 `reports/provenance/CLAIM_LEDGER.md`。架构是跨论文和跨领域的项目综合，不应伪装成某篇论文原样提出。
