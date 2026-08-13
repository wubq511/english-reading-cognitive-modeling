# Cognitive Target and Observability Matrix

> Status: `SOURCE-RECOVERED DESIGN`
> Human validation: not started

本矩阵先问“观测中有没有信息”，再问“哪种模型最好”。可观测性不足时，增加模型复杂度不能创造缺失信息。

## Output classes

- `DIRECT`: 由事件定义直接支持的行为事实。
- `BEHAVIORAL`: 从事件与 state timeline 可靠派生的行为。
- `PROBABILISTIC`: 有信息但存在多个解释，输出分布/置信与 alternatives。
- `VALIDATION-REQUIRED`: 只有经独立 response-process evidence 才能使用认知名称。
- `UNIDENTIFIABLE`: 当前 observation model 下没有足够信息区分。
- `UNKNOWN`: 当前样本证据不足；不代表目标理论上永远不可识别。

## Matrix

| Target | Direct observations | Main alternatives / failure mode | Initial class | Required validation |
| --- | --- | --- | --- | --- |
| option elimination used | elimination toggle | accidental toggle | `DIRECT` | event QA |
| answer change | answer history | accidental click | `DIRECT` | replay QA |
| passage/question shown | UI state | shown does not mean processed | `DIRECT` | instrumentation QA |
| passage revisit | reconstructed viewport/scroll | layout/scroll artifacts | `BEHAVIORAL` | boundary annotation |
| evidence-region revisit | revisit + item EvidenceMap | EvidenceMap may not match student's evidence | `BEHAVIORAL` | item audit |
| reading focus region | viewport, pointer, selection, action history | eyes may move without event; inactive pointer | `PROBABILISTIC` | coarse recall and optional independent sensor study |
| evidence search | navigation/revisit before answer + relevance | verification, memory refresh, normal rereading | `VALIDATION-REQUIRED` | blinded recall/coding, item-stratified test |
| answer verification | relevant revisit after candidate answer | search, difficulty, monitoring | `VALIDATION-REQUIRED` | same as above |
| monitoring/uncertainty | changes, comparisons, revisits | strategic checking or accidental action | `VALIDATION-REQUIRED` | explicit reports + external relations |
| difficulty/confusion | long/irregular processing, revisits, errors | engagement, verification, distraction, text length | often `UNKNOWN` | independent reports and outcome evidence |
| reason for eliminating option C | elimination sequence + nearby evidence | semantic reasoning absent from log | usually `UNIDENTIFIABLE` | targeted report may recover some cases |
| interpretation of sentence | visited/highlighted text | internal semantic representation absent | `UNIDENTIFIABLE` from trace alone | interview/assessment task |
| inference skill mastery | multiple responses + validated evidence | item difficulty, language knowledge, strategy heterogeneity | indirect, `VALIDATION-REQUIRED` | multiple items + independent assessment + model checks |
| misconception | systematic wrong actions | guessing, local misunderstanding, interface errors | `VALIDATION-REQUIRED`, often unknown | designed diagnostic items + independent evidence |

## Identifiability test

对每个 target 先尝试构造两个不同 latent states 产生同一 observable trace 的反例。如果合理反例在当前 UI 下无法区分，则该 target 不能强制分类；需要增加独立证据、限制用途或标 `UNIDENTIFIABLE`。

## Granularity policy

Focus 先评估 coarse region/paragraph，再根据数据决定是否进入 sentence。Webcam、cursor 或统计模型的点级输出不自动授权更细语义粒度。目标粒度的晋级依据是 held-out calibration、selective risk、cross-device stability 和 construct evidence，而不是视觉上“轨迹看起来对”。

## Required uncertainty outputs

每个非直接输出至少包含：

```yaml
label_distribution: {}
unknown_probability: 0.0
evidence_quality: low | medium | high
alternatives: []
applicability_scope: []
mapping_version: string
```
