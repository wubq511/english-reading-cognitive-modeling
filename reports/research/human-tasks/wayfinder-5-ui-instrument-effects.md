# Wayfinder #5 — UI 仪器效应证据审计：人工事项

本文件是 [Wayfinder #5](https://github.com/wubq511/english-reading-cognitive-modeling/issues/5)（UI 仪器效应证据审计）的人工事项清单。登记与完成规则见 [README.md](README.md)；完整研究上下文见 `../ui-instrument-effects-evidence-audit.md`。

背景：以下 25 项来自 2026-08-15 开放网络检索，书目记录当日已逐条对照 Crossref per-DOI 元数据核验。本机对出版商/仓储站点的所有自动抓取都在传输层被 bot-wall 拒绝——这是访问失败，不是版权判定。**操作方式**：在普通浏览器打开链接（需要时用机构网络/VPN），把 PDF 下载到 `tmp/pdfs/`，然后告诉 Agent——它负责核验身份/版本/权利/SHA、登记 catalog 并运行 `scripts/sources inbox`。条目编号是稳定 ID（审计资产其他部分引用了它们），不要重排。

**状态（2026-08-15）**：25 项中 24 项已由用户下载、Agent 逐篇首页核验（标题/作者/年份/DOI/许可）后入正式库，登记为 `METHOD-016`..`METHOD-039`（映射见各行，`scripts/sources doctor` 通过）。唯一未获取：**#12**（用户无 PsycNet 权限）。

## A 组 — 免费直下（仅 bot-wall 挡 curl，浏览器免费合法下载，无需订阅）

- [x] **7. Li, Y., & Yan, L. (2024).** → 已入库 `METHOD-022`（`2024_Li_DigitalVsPaper.pdf`，CC BY-NC 4.0）。
- [x] **8. OECD (2024).** Item characteristics and test-taker disengagement in PISA（OECD 工作论文 No. 312，实际署名作者 Avvisati, Buchholz, Piacentini & Vargas-Madriz）→ 已入库 `METHOD-023`（`2024_OECD_ItemDisengagement.pdf`）。
- [x] **9. OECD (2011).** PISA 2009 Results: Students On Line 整卷（第 3 章 Navigation 确认存在）→ 已入库 `METHOD-024`（`2011_OECD_StudentsOnLine.pdf`）。
- [x] **10. OECD (2017).** PISA 2015 Results (Volume V) → 已入库 `METHOD-025`（`2017_OECD_CollaborativeProblemSolving.pdf`，CC BY-NC-SA 3.0 IGO）。
- [x] **16. Støle, H., Mangen, A., & Schwippert, K. (2020).** → 已入库 `METHOD-030`（`2020_Stole_PaperVsScreen.pdf`，CC BY 4.0）。
- [x] **20. Ulitzsch, E., et al. (2024).** → 已入库 `METHOD-034`（`2024_Ulitzsch_ScaleFormatCIER.pdf`，CC BY 4.0）。

## B 组 — 付费墙（大概率需要机构权限或购买）

- [x] **1. Arslan, B., et al. (2020).** Drag-and-Drop 题目特征效应 → 已入库 `METHOD-016`（`2020_Arslan_DragDrop.pdf`；实际 6 位作者，含 Katz 与 Yan）。
- [x] **2. Ogut, B., et al. (2025).** Universal by Design → 已入库 `METHOD-017`（`2025_Ogut_UniversalByDesign.pdf`；实际 5 位作者，含 Circi）。
- [x] **3. Delgado, P., et al. (2018).** → 已入库 `METHOD-018`（`2018_Delgado_DigitalVsPaper.pdf`，CC BY-NC-ND 4.0）。
- [x] **4. Clinton, V. (2019).** → 已入库 `METHOD-019`（`2019_Clinton_DigitalVsPaper.pdf`）。
- [x] **5. Schwabe, A., et al. (2022).** → 已入库 `METHOD-020`（`2022_Schwabe_ScreenVsPrintComprehension.pdf`，CC BY 4.0）。
- [x] **6. Salmerón, L., et al. (2024).** → 已入库 `METHOD-021`（`2024_Salmeron_HandheldVsPaper.pdf`；实际 5 位作者，含 Vargas）。
- [x] **11. Taylor, L., & Banerjee, J. (2023).** → 已入库 `METHOD-026`（`2023_Taylor_LanguageAssessmentAccommodations.pdf`）。
- [x] **12. Lovett, B. J., & Lewandowski, L. J. (2015).** Universal design for assessment. In *Testing accommodations for students with disabilities: Research-based practice* (pp. 207–223). DOI 10.1037/14468-010. — **已决策（2026-08-16，用户授权 Agent 拍板）：标记为不可获取**。用户无 PsycNet 机构权限；馆际互借/购买成本相对其边际价值不成比例。影响评估：该章是 universal design for assessment 的框架性综述，其实证落点已由本轮入库并读毕的 Ogut 2025（`METHOD-017`）、Dembitzer & Kettler 2023（`METHOD-036`）、Lee 2021（`METHOD-037`）、Witmer & Marinho 2024（`METHOD-031`）与 Taylor & Banerjee 2023（`METHOD-026`）覆盖，审计住宿条款不依赖该章。若日后获得机构权限可补读，按 supersession 规则增补。**开放获取核查（2026-08-16，用户指示重审后执行）**：网页检索未发现作者预印本或机构库合法副本；PsycNet 公开 PDF（`2014-16766-000-BKM`，81 页）经下载核验仅为该书附录 A（Documentation Review in Postsecondary Settings）与全书参考文献，**不含第 10 章正文**，不入库。结论维持：不可获取。
- [x] **13. Mangen, A., Walgermo, B. R., & Brønnick, K. (2013).** → 已入库 `METHOD-027`（`2013_Mangen_PaperVsScreen.pdf`）。
- [x] **14. Wang, S., et al. (2008).** → 已入库 `METHOD-028`（`2008_Wang_TestModeEffects.pdf`；文件名 2007 为在线优先年，正式卷期 2008）。
- [x] **15. Kong, Y., Seo, Y. S., & Zhai, L. (2018).** → 已入库 `METHOD-029`（`2018_Kong_ScreenVsPaper.pdf`）。
- [x] **17. Witmer, S., & Marinho, N. (2024).** → 已入库 `METHOD-031`（`2024_Witmer_ExtendedTimeScoreComparability.pdf`，CC BY）。
- [x] **18. Ponce, H., Mayer, R., & Loyola, M. (2021).** → 已入库 `METHOD-032`（`2021_Ponce_DragDropResponseEffects.pdf`；正式卷期年 2021，© 2020）。
- [x] **19. Moon, J., et al. (2022).** → 已入库 `METHOD-033`（`2022_Moon_SplitAttention.pdf`）。
- [x] **21. Furenes, M. I., Kucirkova, N., & Bus, A. G. (2021).** → 已入库 `METHOD-035`（`2021_Furenes_PaperVsScreen.pdf`）。
- [x] **22. Dembitzer, L., & Kettler, R. J. (2023).** → 已入库 `METHOD-036`（`2023_Dembitzer_UniversalAccommodations.pdf`）。
- [x] **23. Lee, D., et al. (2021).** Embedded Accommodation and Accessibility Support Usage → 已入库 `METHOD-037`（`2021_Lee_EmbeddedAccommodationUsage.pdf`；期刊实为 *Practical Assessment, Research, and Evaluation* 26, Article 25；实际 5 位作者，含 Laitusis；无 DOI）。
- [x] **24. Kobayashi, M. (2002).** → 已入库 `METHOD-038`（`2002_Kobayashi_MethodEffectsTextFormat.pdf`）。
- [x] **25. Woodcock, S., Howard, S. J., & Ehrich, J. (2020).** → 已入库 `METHOD-039`（`2020_Woodcock_ItemFormatEffects.pdf`；标题原文含 "assessment results" 后缀）。

## CNKI/万方检索块

**状态（2026-08-16）：已完成**，原始结果存 [search_results.md](search_results.md)，Agent 评估如下。

无合规自动化路径——请在 https://www.cnki.net 和 https://www.wanfangdata.com.cn 跑下列检索式，把结果告诉 Agent，由 Agent 核验书目记录后再入 catalog：

- 「测验模式效应」（test mode effect——`METHOD-011` 自己的参考文献列表、尤其是其国内引文，是最佳入口）
- 「计算机化测验 纸笔测验 等值」 和 「机考 纸笔 可比性」
- 「阅读测验 屏幕 纸 呈现方式 影响」
- 「PISA 机考 纸笔 难度 等值」
- 「大规模测评 无障碍 特殊需要 机考 accommodation」

**Agent 评估（2026-08-16）**：检索未产生新的必读中文来源。Q1 唯一直接命中即库存 `METHOD-011`（陈平等 2023），确认该综述是中文「测验模式效应」文献的锚点。万方 Q2 候选中 3 条（武圣君 2009、唐小娟 2013、涂冬波 2009）为 CAT/认知诊断编制研究，等值仅为手段，**排除**。两条边际候选非必需，仅记录不下载：谢小庆（1998，HSK 等值试验研究，世界汉语教学 1998年3期——中文语言测验模式等值早期一手实证）；陈芳等（2026，机考环境下地理学业水平测评，上海教育科研——实践向、证据强度弱）。Q3/Q4/Q5 因 CNKI 反爬验证默认填充与万方未登录 0 条而失效——这是检索通道限制，不能解读为「中文无相关文献」；如需补证据强度，改走 `METHOD-011` 参考文献列表做引文追溯。

## 已决策事项

- **WCAG 2.2 本地归档形式（2026-08-16 第二轮决策，用户指示按第一性原理重审后 Agent 拍板）：归档为 `STANDARD-003` 入 catalog。** 本条 supersede 下方 2026-08-16 首轮决策——首轮前提（"sources 管线强制 PDF"）经复查证伪：`media_type` 校验是通用 MIME 正则（`scripts/sources.py`），magic 检查仅覆盖 `application/pdf` / `application/zip` / `application/json`，`text/html` 可直接登记，**无需任何工具链改动**；首轮"HTML 无法登记"系登记时误用 `application/pdf` media type 所致（INVALID_PDF_MAGIC）。实际做法：2026-08-16 重试 TR 端点成功（首轮被 Cloudflare 挑战属间歇性），WCAG 2.2 规范全文（W3C Recommendation 12 December 2024，单文件 HTML）存档 `sources/library/standards/2024_W3C_WCAG22_Recommendation.html`，catalog/checksums/crosswalk 已同步；归档件身份与完整性由 sha256 固定，bytes 可经 canonical TR URL 重取；审计引用的 4 条 SC（2.5.7 / 1.4.10 / 2.2.1 / 2.5.8）逐字文本已对归档件核验一致。`artifacts/wcag22/` 首轮临时片段已删除（冗余，可由归档件重建）。许可：W3C Document License 2023 授予 copy/distribute（须保留归属链接与版权声明），登记为 `REDISTRIBUTION_ALLOWED`。
- ~~**WCAG 2.2 本地归档形式（2026-08-16 首轮决策）：不入 catalog。**~~ **SUPERSEDED**（被上条取代；保留备查）：原理由为"现有 sources 管线强制 PDF（`local_path` 必填、`scripts/sources doctor` 校验 PDF magic），HTML 快照无法登记；把规范文本制造成 PDF 会产生派生工件而非原始来源；为 4 条 SC 修改校验工具链成本不成比例"——前提证伪，见上条。
- **#12 Lovett & Lewandowski 2015：标记为不可获取**（见 B 组第 12 行的影响评估）。
