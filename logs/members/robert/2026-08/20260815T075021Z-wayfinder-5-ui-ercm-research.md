---
schema_version: 1
member_id: robert
timestamp: 2026-08-15T07:50:21Z
category: research
summary: Wayfinder #5（UI 仪器效应证据审计）两轮研究：检索、24 篇入库与全文综合
supersedes: NONE
---

## Work completed

- 第一轮（2026-08-15）：完成 #5 研究决策的第一轮：产出 reports/research/ui-instrument-effects-evidence-audit.md（30 条钉页证据 UIE-01..30，四类主张分离）；本地 80 源盘点 + Crossref/S2/WebSearch/ERIC dated 检索 + 五种子引用链；新获 6 源（METHOD-010..015）；25 项获取队列 + CNKI 检索块 + API key 常设任务。ercm-research 流程就地补强三条：联网 AI 深搜轮、人工队列聊天清单直给、定位文献未读完时研究票默认保持 open。GitHub：#5 一度关闭后经用户指出已重开；#16 以 not planned 关闭并从 #2 摘除。
- 第二轮（2026-08-16）：24 篇队列文献经用户人工下载、Agent 逐篇首页核验后入正式库（METHOD-016..039，catalog/checksums/crosswalk 同步）；24 个并行提取代理完成全文逐页证据提取，每篇一份钉页笔记（reports/research/ui-instrument-effects-evidence-audit/METHOD-016..039.md）；用户完成 CNKI/万方人工检索轮，Agent 评估为近阴性并留档（human-tasks/search_results.md + 评估段）；提取中发现的 8 处 catalog 作者名拼写不符已按 PDF 首页修正；审计主文件综合改写为中文，证据表扩至 UIE-01..64。OPENALEX_API_KEY 已配置并验证（用户 ~/.zshrc 中 key 带脏字符已修复）。
- 第三轮（2026-08-16，用户审查简报通过、指示按第一性原理重审两个待决项）：（1）WCAG 2.2 归档决策推翻重来——首轮"管线强制 PDF"前提证伪（media_type 为通用 MIME 校验，magic 检查仅覆盖 pdf/zip/json），TR 端点重试成功，规范全文（W3C Recommendation 12 December 2024 单文件 HTML）登记为 STANDARD-003 入 catalog（sources=111），4 条引用 SC 逐字核验一致，artifacts/wcag22/ 临时片段删除；human-tasks 已决策事项按 supersession 留痕。（2）#12 补做开放获取核查：网页检索无作者预印本；PsycNet 公开 PDF 核验仅为该书附录 A+参考文献，不含第 10 章；维持不可获取结论，核查轨迹已记录。

## Research or decision impact

- 第一轮确立：UI variant 选择是仪器设计而非 UX 偏好（B7 OR=1.40；METHOD-012 d=.16–.22）；baseline variant 须在 BENCH-E0 前冻结为 instrument contract；WCAG SC 2.5.7/1.4.10/2.2.1/2.5.8 进入合同；可用性/构念等价主张留待 H2。
- 第二轮新增：（1）第一轮的模式效应「方向张力」裁决为三档条件结构——说明文/限时语境纸优（g≈−.21~−.32）、叙事/非速度语境统计等价零、高速度操作性考试屏优（d=.16–.22），儿童标准化语境屏劣且与能力/性别交互；任何单方向断言不受支持，存在性前提更稳。（2）格式移动 estimand 获五个独立证据收敛（B7、METHOD-016/032/038/039）。（3）住宿效应确立层级表述义务：item 参数 / scale 分布 / 方差结构三层各自独立（UIE-60/62/63），「可用≠被用」须实测报告。（4）Class-1 可用性实证缺口确认为领域共识级（UIE-61）。（5）新增决策含义第 7 条（住宿可比性分层测量）与第 8 条（计时政策=构念决策）。无既有 verdict 被推翻；UIE-10 由 PARTIAL 升 SUPPORTED（Arslan 2020 一手验证）；W4 的 Lee 2021「低使用率」概括与 W6 的 PISA 2015 Vol. V 归属两处第一轮表述已修正。

## Verification

- 第一轮：scripts/bootstrap OK；scripts/sources doctor OK checked=86；scripts/verify OK sources=86；三处负载引用 pdftotext 全文抽查通过；GitHub 回读 #5 OPEN、#16 closed 且摘除、地图 #2 一致。
- 第二轮：scripts/sources doctor OK checked=110；scripts/verify OK（markdown_files=142, sources=110）；24 篇首页核验（标题/作者/年份/DOI/许可）全部 MATCH；每篇提取笔记含提取验证记录（页码钉物理页、无 ABSTRACT-ONLY 为主）；审计主文件 UIE 条目计数核验=64。
- 第三轮：WCAG TR 单文件 HTML 经 tag-strip 后 4 条 SC 引文逐字匹配（SC 2.5.7 / 1.4.10 / 2.5.8 / 2.2.1）；W3C Document License 2023 原文核验（copy/distribute 授予，须归属）；PsycNet 2014-16766-000-BKM.pdf 经 pdftotext 核验为附录 A+参考文献（不含第 10 章）；scripts/sources doctor OK checked=111；scripts/verify OK（markdown_files=142, sources=111）。

## Follow-ups

- 用户已于第三轮审查通过（sign-off 收到）。后续动作：ghr 发 resolution comment、关 #5、更新地图 #2 的 Decisions so far、本批次（审计资产、24 份提取笔记、sources 元数据、human-tasks、crosswalk、README、STANDARD-003 登记）commit 并 push（用户已批准推送）。
- 可选后续：PISA 2015 Technical Report（「65/103 题」量化出处）获取；OpenAlex 同题复检轮（key 已配置）；S2 API key 审批中（约 60 天不活跃会被回收）。
