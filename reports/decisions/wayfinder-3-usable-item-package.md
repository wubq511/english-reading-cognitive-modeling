# Wayfinder #3 决策记录：五篇 35 题候选评审包与可豁免门禁

> Status: `CURRENT`
> 决策票：[Establish the usable item-package and redistribution route](https://github.com/wubq511/english-reading-cognitive-modeling/issues/3)（父地图 [#2](https://github.com/wubq511/english-reading-cognitive-modeling/issues/2)）
> 票型：`wayfinder:task`
> 决议日期：2026-09-05
> 关闭复核：2026-09-20，负责人确认关闭 #3，并对下述两项门禁行使 `WAIVED_BY_OWNER`

## 结论速览

- **核心结论**：#3 的候选评审范围冻结为 `issue-3-five-passages-v0`：5 篇文章、35 道原题。它取代此前“先准备 6 篇、每篇 4–6 题”的范围假设，但只冻结进入专家 UI 证据评审的候选包，不预先决定最终 pilot 使用多少篇或多少题；最终准入与施测子集仍由 #4 决定。
- **怎么得出的**：项目负责人提供并指定了五个来源文档中的确切篇章，确认五篇材料可公开再分发；随后发布不含答案、解析和预设 evidence span 的盲评包及公开 local-first 专家评审站。公开包的 SHA-256 为 `c265a4944f961d4ab0b4223a69df9e72436bd9699bbec2965422b4d516d0438a`。
- **关闭边界**：负责人于 2026-09-20 明确确认关闭 #3，并将本任务的文档齐备门禁与 source/provenance/rights-record closure 门禁记为 `WAIVED_BY_OWNER`。因此 #3 只关闭“候选题包范围与当前公开评审路线”这一决定；缺失材料和记录不视为已验证。专家评审综合、内部答案/解析/evidence spans、Candidate Bank V1 准入与 pilot subset 继续由 #4 闭合。

## 决议一：候选评审包范围

| ID | 文章 | 题数 |
| --- | --- | ---: |
| P1 | The Star Quality of New Zealand’s Great Barrier Island | 10 |
| P2 | Passage Two - Cooperation, selfishness, genes and environment | 5 |
| P3 | Meet the “digital nomads” who travel the world in search of fast Wi-Fi | 10 |
| P4 | Passage Two - Corporate profit-shifting to tax havens | 5 |
| P5 | Reading Passage 1 - Children’s ideas about rainforests | 5 |

总计 5 篇、35 题。公开盲评站：<https://ercm-reading-review-lab-35.neat-angel-1849.chatgpt.site>。

该范围是 **candidate review scope**，不是最终施测合同。#4 仍需根据 UI 证据强度、可定位性、可观察行为、替代解释风险、施测时长和题型覆盖决定 Candidate Bank V1 与 pilot subset。

## 决议二：文档齐备门禁有两个路径

- `DOCUMENTS_REQUIRED`（默认）：取得并核验任务决议所依赖的全部指定文档，依赖全文的结论通过 `scripts/sources doctor`。
- `WAIVED_BY_OWNER`（显式备选）：负责人明确点名某任务不需要哪些文档后，可把这些文档移出该任务的 required corpus。记录必须写明日期、文件/范围、原因、缩窄后的交付与主张边界，以及下游何时必须重开门禁。

豁免后的任务不能依据未读文档作结论，也不能把“无需取得”写成“已核验”。提交仅缺少本地 raw/PDF 时，可在同一次明确授权下用 `ERCM_VERIFY_MODE=public` 触发公开快照验证；该选项不改变 catalog 状态。

### #3 采用的路径：`WAIVED_BY_OWNER`

- 日期与权限：2026-09-20，项目负责人在关闭复核中明确确认。
- 任务：GitHub #3「Establish the usable item-package and redistribution route」。
- 被豁免的文档交付：不要求 #3 在关闭前把下列五组来源材料的 PDF/DOCX 表示迁入并核验为 canonical required corpus：`第一、二篇 原文原题 来源`、`第一、二篇 解析 来源`、`第三、四篇 原文原题 来源`、`第三、四篇 解析 来源`、`第五篇 原文原题解析 来源`；本地目录 `tmp/pdfs/issue-3-five-passages/` 仍保持待分类，不得写成已导入或已核验。
- 缩窄后的交付与主张：只确认负责人指定的五篇 35 题构成候选评审范围、当前公开盲评包及站点是该范围的一个发布表示；不依据被豁免文档新增或验证答案、解析、evidence span、版本同一性、题目质量或认知主张。
- 重开条件：#4 若使用这些原题或解析建立答案键、人工 evidence spans、Candidate Bank V1 或 pilot subset，必须重新取得并核验其所依赖的确切文档；任何 runtime 计分、正式 pilot 或基于原解析的结论也必须先重开该门禁。

## 决议三：source/provenance/rights-record closure 有两个路径

- `SOURCE_RIGHTS_CLOSURE_REQUIRED`（默认）：将任务需要的来源身份、版本、hash、来源链和权利状态闭合到 canonical owners。
- `WAIVED_BY_OWNER`（显式备选）：负责人明确点名该任务不需要闭合 source/provenance/rights record 后，可从该任务出口移除这项交付，并记录未闭合字段与下游重开条件。

该豁免只改变任务范围。它不会生成许可、不会把 `UNKNOWN` 变成 `REDISTRIBUTION_ALLOWED`，也不替代某次公开分发所需的 exact-material approval。

### #3 采用的路径：`WAIVED_BY_OWNER`

- 日期与权限：2026-09-20，项目负责人在关闭复核中明确确认。
- 被豁免的记录交付：#3 不要求在关闭前把五篇 35 题的逐文件 source identity、版本、hash、来源链、许可名称或其他 rights evidence 闭合到 catalog、checksum 与权利记录 owner。
- 保留事实：负责人于 2026-09-04 对当前五篇所选文本和题目的公开再分发作出 exact-material approval；该负责人声明仍只记录为 `observed`，不得扩写成未提供的许可名称、权利链或法律结论。
- 缩窄后的交付与主张：#3 仅记录当前候选包和部署路线，不声称 source/provenance/rights records 已闭合，不把 `UNKNOWN` 或 `NOT_RECORDED` 改写成 `validated`。
- 重开条件：材料版本、公开载荷或发布渠道发生变化，或 #4/后续实现、pilot、论文、数据共享需要依赖来源身份、版本谱系或再分发依据时，必须对实际使用的 exact materials 重新闭合记录并取得适用批准。

## 被否替代

- **6 篇、每篇 4–6 题作为 #3 固定范围**：被当前 5 篇、35 题候选评审包取代。其“约半小时施测”的动机仍有效，转由 #4 在最终 subset 中处理。
- **任何缺文档或缺记录都永久阻止任务关闭**：被显式、可审计、缩窄主张范围的 `WAIVED_BY_OWNER` 备选取代；默认路径仍为 fail-closed。
- **把豁免写成验证通过**：否决。豁免与验证是不同状态。

## 证据、边界与下游含义

- `observed`：公开包包含 5 篇、35 题；包 hash 如上；公开站于 2026-09-04 部署，2026-09-05 仍可访问。
- `observed`：负责人在 2026-09-04 明确确认这五篇所选文本和题目具备公开再分发权；本记录不推断未声明的许可名称。
- `WAIVED_BY_OWNER`：#3 的文档齐备门禁已按上述范围豁免；本地材料仍是未导入、未核验状态。
- `WAIVED_BY_OWNER`：#3 的 source/provenance/rights-record closure 已按上述范围豁免；未记录字段保持 `UNKNOWN` 或 `NOT_RECORDED`。
- `OPEN`（转交 #4）：尚未收到并综合独立专家导出的 UI 证据评审结果。
- `OPEN`（转交 #4）：答案键、解析、人工 evidence spans、Candidate Bank V1 版本合同与 pilot subset 仍未闭合。
- → #4（[Freeze Candidate Bank V1 and EvidenceMap admission rules](https://github.com/wubq511/english-reading-cognitive-modeling/issues/4)）：以 5 篇、35 题为候选输入，决定最终准入与 pilot subset；不能继续把“必须 6 篇”当作 #3 当前事实。
- → 后续实现：公开盲评包不含答案、解析或预设 evidence spans，不能直接充当 runtime 的完整计分题库。
