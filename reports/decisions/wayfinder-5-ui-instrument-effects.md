# Wayfinder #5 决策记录：UI 仪器效应证据审计

> Status: `CURRENT`
> 决策票：[Review evidence for UI effects on reading and measurement](https://github.com/wubq511/english-reading-cognitive-modeling/issues/5)（父地图 [#2](https://github.com/wubq511/english-reading-cognitive-modeling/issues/2)）
> 票型：`wayfinder:research`
> 决议日期：2026-08-16
> 回填说明：本记录为 2026-08-22 按 [ADR 0008](../../docs/adr/0008-wayfinder-decision-records-in-repo.md) 从该票已 sign-off 的 resolution 评论逐字回填；正文即当时审查通过的文本，未做内容改动。

## 结论速览

- **核心结论**：作答 UI 的选择是测量仪器设计，不是 UX 偏好——UI 变化可移动 estimand（五个独立证据收敛），baseline variant 必须在 `BENCH-E0` 前冻结为 instrument contract；模式效应方向裁决为三档条件结构，任何单方向断言不受支持；WCAG 2.2 四条 SC（2.5.7 / 1.4.10 / 2.2.1 / 2.5.8）直接进入仪器合同。
- **怎么得出的**：本地 80 源盘点 + 2026-08-15 开放网络检索（Crossref / Semantic Scholar / WebSearch / ERIC）+ 2026-08-16 对 24 篇队列文献的全文逐页钉页提取；全部负载结论钉到本地 PDF 物理页码，四类主张（可用性偏好 / 行为改变 / 信度与缺失 / 学习与构念）全程分离。
- **未决项**：Class-1 可用性/偏好实证为领域共识级缺口（`UNRESOLVED`）；within-mode 阅读 MC 作答 UI 变体是否移动构念/estimand 无直接证据，须由 H2-gated 变体研究回答；#12 Lovett & Lewandowski 2015 不可获取（影响已评估）。

## Resolution（2026-08-16，经两轮研究 + 一轮用户审查后关闭；研究成员已审查中文简报并 sign-off）

### 答案（核心结论）

1. **UI variant 选择是仪器设计，不是 UX 偏好**：UI 变化会移动 estimand（五个独立证据收敛：B7 OR=1.40；`METHOD-016/032/038/039`；`METHOD-012` ACT 数据 d=.16–.22）。baseline variant 必须在 BENCH-E0 前冻结为 instrument contract。
2. **模式效应「方向张力」裁决为三档条件结构**：说明文/限时语境纸优（g≈−.21~−.32）；叙事/非速度语境统计等价零（TOST）；高速度操作性考试屏优（d=.16–.22）；儿童标准化语境屏劣且与能力/性别交互。任何单方向断言均不受支持；存在性前提比方向断言更稳。
3. **无障碍规范直接进入合同**：WCAG 2.2 SC 2.5.7 / 1.4.10 / 2.2.1 / 2.5.8 约束作答 UI（拖拽替代路径、重排、计时例外、目标尺寸）。计时政策中的「essential」例外使用 = 构念主张，须照此记录。
4. **住宿（accommodation）效应须分层表述**：item 参数 / scale 分布 / 方差结构三层各自独立（UIE-60/62/63）；「可用 ≠ 被用」，使用率须实测报告。
5. **Class-1（个别 UI 元素对阅读过程指标的效应）实证缺口确认为领域共识级**（UIE-61），不是本审计的检索失败。

### 证据与资产

- 主资产：`reports/research/ui-instrument-effects-evidence-audit.md`（中文，UIE-01..64 钉页证据，observed/derived/inferred/validated 与 simulation-only 分离，Class 1–4 主张分级）
- 逐篇提取笔记：`reports/research/ui-instrument-effects-evidence-audit/METHOD-016..039.md`（24 份，页码钉物理页）
- 新入库来源：`METHOD-016..039`（24 篇，逐篇首页核验标题/作者/年份/DOI/许可）；`STANDARD-003`（WCAG 2.2，W3C Recommendation 12 December 2024，单文件 HTML，`text/html` 登记，4 条引用 SC 逐字核验一致）；catalog / checksums / crosswalk 已同步（sources=111）
- 人工事项与决策留痕：`reports/research/human-tasks/wayfinder-5-ui-instrument-effects.md`（含 CNKI/万方检索评估、#12 决策与 OA 核查、WCAG 归档 supersession 记录）
- 中文库检索原始结果：`reports/research/human-tasks/search_results.md`

### 被否替代

- 「纸优」或「屏优」的单方向概括 → 三档条件结构（见上）。
- 「UI variant 可凭 UX 偏好选定」→ 仪器设计，须冻结为合同。
- 「个别 UI 元素效应已有现成实证可引」→ Class-1 缺口为领域共识级。
- 第一轮曾决策「WCAG 2.2 不入 catalog」→ 前提证伪（media_type 校验为通用 MIME 正则，`text/html` 可直接登记），第二轮 supersede 为 `STANDARD-003` 归档，留痕于 human-tasks「已决策事项」。

### 不确定性与门禁

- **#12 Lovett & Lewandowski 2015 不可获取**：无 PsycNet 机构权限；OA 核查（2026-08-16）未发现作者预印本，PsycNet 公开 PDF 经核验仅为该书附录 A + 参考文献。影响评估：其实证落点已由 `METHOD-017/026/031/036/037` 覆盖，审计住宿条款不依赖该章；日后获权限按 supersession 增补。
- CNKI/万方人工检索轮近阴性，但 Q3–Q5 受检索通道限制（反爬/未登录），不能解读为「中文无相关文献」；补强通道 = `METHOD-011` 引文追溯。
- PISA 2015「65/103 题」量化出处（Technical Report）未获取，`METHOD-025` 行已限定表述（模式效应量化不在本卷）。
- 门禁：`scripts/sources doctor` OK checked=111；`scripts/verify` OK（sources=111）。

### 下游含义（对地图目的地）

- baseline UI variant 冻结清单获得依据：四条 WCAG SC + 格式移动 estimand 证据 → 直接输入 [#6 Freeze baseline UI variants and invariant instrument behavior](https://github.com/wubq511/english-reading-cognitive-modeling/issues/6)（决议见 [`wayfinder-6-baseline-ui-variants.md`](wayfinder-6-baseline-ui-variants.md)）。
- 计时政策 = 构念决策 → 输入 #8（BENCH-E0 logging contract：计时器状态属被测量构念的一部分）。
- 住宿分层测量义务与「可用≠被用」→ 输入 #13（UI-variant estimands）与 H2 设计票。
- Class-1 缺口 → 支持「baseline 先冻结、AI 扩展后评估」的地图路线，不解锁任何新实现工作。
