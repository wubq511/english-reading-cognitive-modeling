# 测量与验证框架（Phase 2A）

> Design status: `CLOSED FOR ITEM-INDEPENDENT V1`
> Implementation status: `NOT STARTED`
> Item-specific Phase 2B: `WAITING FOR ITEMS + H2 PILOT`

“Closed”只表示题目无关的 V1 结构已经充分收敛；schema、阈值、样本量、实际可靠性和效度仍需实现和实验。

## 1. 产品定义

Phase 2A 的产品不是一个扁平的“认知标签数据集”，而是可重放的 `Response-Process Evidence Dataset`：

```text
immutable raw events
  + deterministic UI state
  + replay
  + behavior episodes
  + participant account
  + independent coder interpretations
  + item/task context
  + disagreement and uncertainty
  + provenance
```

这样 taxonomy 变化时可以从原证据重新编码，而不必重新做真人实验。

## 2. 原始测量契约

- Object-centric append-only events；raw 内禁止 cognition。
- `wall_time + mono_ms + sequence`，保存 time origin 与 schema version。
- Page visibility、layout change 与 semantic viewport visibility 必采。
- `pointerrawupdate` 不是系统依赖；pointer sampling policy 是实验门。
- 内部 store 可以 OCEL-inspired，但不是宣称完全遵守 OCEL 标准。
- Caliper 等语义导出是可选 interoperability 层，不能替代内部忠实记录。

## 3. Replay 保真度

Replay 必须从日志和版本化任务资产确定性重建，不以屏幕视频作为唯一真相。对关键事件保存足够 layout/object snapshot，验证原始状态与 replay state 的差异。

`BENCH-E0` 至少覆盖：navigation、answer history、eliminate/restore、underline create/delete、scroll burst、visibility、resize/zoom、duplicate/missing/out-of-order events。

## 4. 刺激回忆

1. 学生正常完成任务；不显示模型预测。
2. 任务后尽快 replay；不设未经证据支持的固定 5–10 分钟硬阈值。
3. 自动 bookmark 只定位候选窗口，不预填认知解释。
4. 先开放问题，再针对事件的 focused probe。
5. 参与者可以回答“不记得/不知道”，可以暂停、跳题或要求删除片段。
6. Participant report 与 researcher/coder interpretation 分开存储。

Recall 是回顾性证据，受记忆、重构和提示影响，不是 cognition 神谕。

## 5. 标注记录

```yaml
episode_id: string
session_id: string
start_ms: number
end_ms: number
observable_behavior: []
participant_reports: []
coder_labels: []
competing_labels: []
evidence_sources: []
confidence: null
disagreement_status: string
item_id: string
evidence_region_ids: []
provenance: {}
```

必须允许 `AMBIGUOUS_SEARCH_VERIFICATION`、`UNKNOWN_RECALL`、`INSUFFICIENT_OBSERVATION`、`CODER_DISAGREEMENT` 等状态。Adjudication 新增裁决，不覆盖独立原 label。

## 6. 盲法与信度

- 至少两名人类 coder 独立标注；关键认知构念由第三人 adjudicate。
- Coders 不看 system/LLM predictions；adjudicator 不看系统输出。
- Segmentation agreement 与 label agreement 分开评价。
- Categorical coding 默认报告 Krippendorff alpha/kappa、原始 agreement 和不确定性；temporal unitizing 需选适合重叠片段的 metric，当前仍是 method gate。
- Main study 前冻结 manual；实质修改产生新版本并重编码受影响数据。

AI 作为候选第三臂时还必须遵守 `AI_RESEARCH_TOOLING_POLICY.md`，不能替代 reference standard。

## 7. 溯源链

任何派生结论保留：source event range、task asset version、reconstruction version、segmentation version、codebook、coder、adjudication、mapping registry version、model version 和生成时间。Derived result 不覆盖旧版本。

## 8. 生产 vs 研究

| 证据 | 生产 | 研究验证 |
| --- | --- | --- |
| 自然的 `COL-L0/L1` | 是 | 是 |
| replay | 否 | 是 |
| 刺激回忆/访谈 | 否 | 仅 H2/H3 |
| 人工标注 | 否 | 是 |
| 屏幕/音频录制 | 否 | 仅经批准的 M1 |
| Webcam/眼动追踪 | 否 | 仅可选 M1 子研究 |

## 9. Phase 2B 仍未封闭

只有具体题目和 pilot 到位后才能冻结：

- 逐题 EvidenceMap；
- 题目特定 recall probes；
- episode taxonomy 调整；
- thresholds、class prevalence 与 sample size；
- 最终标注预算与 adjudication 规则。

提前写死这些项目会把研究假设反向编码进题目和标签。
