# Item and Data Source Status (Phase 0)

> Status: `OPEN`
> Purpose: distinguish acquired source files from a deployable, rights-cleared item bank
> Detailed primary-source audit: `../research/phase-0-item-data-source-audit.md`

## Exit criteria

Phase 0 只有在以下四类交付都可本地验收时才能关闭：

1. 至少一组 passage/item-level 资产，含题干、选项、答案、evidence spans 和权利；
2. PELDiaG 等候选的公开资产追踪与必要作者申请记录；
3. Candidate Passage/Item Bank V1；
4. 冻结的 pilot 选题与难度估计规则。

原始 chat3 Turn 4 明确承诺完成这四项，但后续原文没有证明全部交付。

## Current candidate families

| Candidate | Intended role | Current verified local status |
| --- | --- | --- |
| PELDiaG | 大学英语阅读诊断题/属性映射候选 | `DOMAIN-003` 全文已核实 5 passages、43 原题/41 分析题、N=740、专家/学生 Q-matrix 与 verbal-report 流程；完整题本、答案键、响应矩阵和复用权利仍未取得 |
| 2022 CSE reading inference study | CSE 阅读推理构念与题目谱系 | 官方摘要已核实 N=1083、6 推理+2 字面理解属性；CNKI 全文、题本、Q-matrix 与数据未取得 |
| 2026 J. Intell. Q-matrix study | 新一代题目/Q-matrix 候选 | `ITEM-001/002` 已落地；S2 含 20 题，但无独立官方 answer key 和逐题权利/来源清单，故不能直接进 Candidate Bank |
| TSC 2026 | J. Intell. 明确承接的属性/Q-matrix 来源 | `DOMAIN-002` 全文已核实 28→20 题、pilot 382/360、主测 975/886 与 6 推理+2 字面属性；完整题本/响应数据/复用权利仍未取得。2022→TSC/J. Intell. 的题本与数据映射为 `NOT FOUND` |
| Zhang et al. 2024 CSE-based CDM | CSE 阅读能力属性与 G-DINA 设计参考 | `DOMAIN-001` 出版商 VOR 已落地；是独立研究，不是缺失的 Ma & Du 2022，也不提供本项目可直接部署题库 |
| Jin & Liu difficulty pilot | 文本预筛 + 真人 item pilot 方法参考 | `ITEM-003` 作者稿已落地；n=47、CSE 分层与 33 篇 TOEFL 已核实；TOEFL 材料不随论文许可再分发 |
| PISA 2012 digital reading logs | 外部行为分布/字段参考 | OECD 官方可下载；只用于 ETL、序列特征和分布校准，不作本项目认知真值 |
| ePIRLS 2016 | 外部任务/统计参考 | 公开数据可得，但未确认公开原始 clickstream；item 复制/部署受 IEA/第三方权利限制 |
| PIAAC 1st Cycle | 外部过程日志/特征工程参考 | 17 国 raw XML 公共使用文件可得；人群/任务不同，不能验证本项目构念 |
| NAEP | 受限过程数据治理参考 | respondent-level 需 NCES restricted-use license；未确认公开 reading process microdata，当前不作为可用数据源 |

## Rejected shortcuts

- 自动 readability/CSE 等级不能替代 item difficulty 或目标人群 pilot。
- 官方 item type/Q-matrix 不能替代学生实际过程的效度证据。
- 外部平台日志不能直接当本项目 UI 的分布或 cognition truth。
- “同一研究谱系”在没有版本、样本、题目和补充材料比对时不能写成已确认继承。

## Required asset record

每个 candidate item/source 最少记录：

```yaml
asset_id: string
passage_id: string-or-null
item_id: string-or-null
source_citation: string
source_url: string
rights_status: UNKNOWN
local_files: []
answer_key_status: unknown
evidence_span_status: unknown
q_matrix_status: unknown
target_population: null
difficulty_evidence: []
observability_class: null
intended_use: screening | pilot | benchmark | external_reference
verified_at: null
```

## Next acquisition actions

1. 实验室通过 CNKI 或作者渠道合法获取 `10.19360/j.cnki.11-3303/g4.2022.12.001`；人工下载统一放 `tmp/pdfs/` 交由 Agent 入库。
2. 向 Wenbo Du/Xiaomei Ma 请求 PELDiaG/2022/TSC/J. Intell. 的 instrument/data lineage、题本/answer key、响应数据、data dictionary 与允许用途；请求数据前先完成实验室数据治理审批。
3. 对 S2 做逐题 provenance/rights audit，由至少两名内容专家独立作答并裁决 answer key/evidence spans；豆包 S3 不得作 gold key。
4. 只在权利、答案和 evidence metadata 足够时进入 Candidate Bank。Candidate Bank 必须覆盖 local/detail 到 cross-paragraph/global 的 observability gradient，不能只选容易从轨迹识别的题。
