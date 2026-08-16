# 证据提取笔记 — METHOD-018

> 供「UI 仪器效应证据审计」（Wayfinder #5）综合使用。本文档只记录本 source 的全文证据，不修改审计主文件、catalog、checksums 或任何其他文件。

## 头部信息

- **source ID**: `METHOD-018`
- **本地路径**: `sources/library/papers/methods/2018_Delgado_DigitalVsPaper.pdf`
- **完整书目（以 PDF 首页为准）**:
  - 作者: Pablo Delgado, Cristina Vargas, Rakefet Ackerman, Ladislao Salmerón（University of Valencia / Technion-Israel Institute of Technology）
  - 标题: *Don't throw away your printed books: A meta-analysis on the effects of reading media on reading comprehension*
  - 年份: 2018
  - Venue: *Educational Research Review*, Vol. 25, pp. 23–38
  - DOI: 10.1016/j.edurev.2018.09.003
  - 许可: CC BY-NC-ND 4.0（© 2018 The Authors; Elsevier）——PDF 首页与 catalog 一致
- **书目核对**: catalog.yaml 中 METHOD-018 条目的作者/年份/标题/venue/DOI 与 PDF 首页完全一致，无差异标注项。
- **页码约定**: 本笔记页码一律为 PDF 物理页（文件共 16 页）；物理页 = 打印页 − 22（如物理页 9 = 打印页 31）。全文（摘要→参考文献）均已通读，无 `ABSTRACT-ONLY` 标注项；Appendix 表 A1/A2（participant 分布细节）为在线 supplementary，未本地获取，本笔记不引用其单元格内容。

## 研究概览

- **研究问题**（p.4, Objectives）:
  1. 阅读媒介（paper vs digital screen）是否影响阅读理解成绩；
  2. 哪些因素调节媒介效应（时间框架、文本类型、设备、滚动、开放作答、理解类型、教育水平、年份等）。
- **设计**: 元分析（random-effects；between 与 within 两个独立数据集分别分析，不合并——p.7 "it is not recommended to combine studies with between-participants and within-participants designs in one meta-analysis"）。
- **样本**: 54 项研究（2000–2017，英文报告）、76 个媒体比较、171,055 名参与者（p.1 摘要、p.5）。Between: 38 研究 / 58 ES → outlier 移除 2 项后 56 ES / 169,524 参与者，其中 4 项大规模研究占 165,778（Pommerich 2004; Puhan et al. 2005; Lenhard et al. 2017; Eyre et al. 2017，p.8）；Within: 16 研究 / 18 ES / 1,531 参与者（p.8）。检索：PsycInfo/ERIC/Proquest/WoS/Scopus/Google Scholar/学位论文 + 前向引用 + 专家征集，1,840 条记录筛至 54 项，截至 2017 年 5 月（p.5）。
- **纳入标准**（p.4–5）: 纸 vs 屏（电脑/平板/手机/e-reader）对比；个体默读；**跨媒介文本可比（内容/结构/图片一致），数字条件不含超链接或网页导航**（p.5 "specific features of digital environments, such as hyperlinks or web navigation, are not present in the digital-based condition"）；日常语言；规范人群（无阅读困难/认知障碍）；2000–2017；可计算效应量。
- **任务与材料**: 阅读后作答理解题，测验形式混合（标准化测验 22 ES vs 研究者自制任务 34 ES，无调节，p.12 Table 2）；约 63.79% 为研究者自制任务、72.41% 为文本+推断混合题型（p.8）；44.83% 的比较限时（p.8）。
- **变量**:
  - 产品分数（outcome）: 理解测验成绩 → Hedges' g（between）与 dc（within，standardized mean change）。方向约定：负值 = 纸优（p.7 "A positive Hedges' g indicates better comprehension results for the digital-based condition, whereas a negative Hedges' g indicates better outcomes for the paper-based condition"）。Within 用 digital 作 control 组以保持方向一致（p.7）；r 未报告的按 Rosenthal 保守插补 r=.7（p.7），敏感性范围 .10–.90（p.10）。
  - 过程指标: 无（元分析不采集行为/过程数据；滚动与否仅编码为文本呈现特征）。
  - 缺失指标: 无（缺失率/完成率/作答率不在分析变量中；排除标准为统计信息缺失或非正态，p.15）。
  - Moderators（p.5–6 编码定义）: 教育水平、文本长度（<1000 词 vs 长）、允许阅读时间框架（free vs limited）、数字设备（电脑 vs 手持）、文本类型（信息/叙事/混合）、滚动需要、开放作答（作答时能否回看文本）、理解类型（文本/推断/混合）、显式策略要求（k=5 太小未测，p.12）、发布状态、发表年份、样本量、抽样方法（无变异未测）、组分配、测验类型、测试媒介（同媒介作答 / 总是纸 / 总是数字）。
- **质量处理**: 双编码者、随机 28% 样本、Cohen's κ=.89（p.6）；outlier 用 Beath robust model 确认移除 2 项（Duran 2013; Nishizaki 2015，p.9）；敏感性：one-study-removal、剔除 4 项大规模研究、剔除灰色文献、r 值插补范围（p.9–10）；发表偏倚：Rosenthal fail-safe N、Egger 回归、published vs unpublished ANOVA（p.7, 10–11）。

## 核心发现（按四类主张）

### Class 4 — 学习/构念与 estimand（本论文主要贡献）

1. **投递模式（screen vs paper）移动阅读分数分布，纸优，between 与 within 两数据集独立同向**。Between: Hedges' g = −0.21（95% CI [−0.28, −0.14]，k=56，p.9）；Within: dc = −0.21（95% CI [−0.37, −0.06]，k=18，p.10）。摘要 p.1: "Both designs yielded the same advantage of paper over digital reading (Hedge's g = −0.21; dc = −0.21)." 方向与审计已持有的 `METHOD-012`（UIE-27，ACT 在线 > paper，d=.16–.22）**相反**，跨证据必须并列处理（见「对审计的用途」）。

2. **效应有方向但不均质：high heterogeneity，prediction interval 跨零**。Between: I²=72.24, Q=208.96, p<.001；预测区间 −0.56 到 0.14（p.9）。Within: I²=89.88, Q=167.94, p<.001；预测区间 −0.90 到 0.47（p.10）。p.9: "the effects are large in some populations, but moderated and trivial in other populations." → 单一方向断言（"屏幕阅读普遍更差"）超出现有证据；方向依赖人群/任务条件。

3. **允许阅读时间框架是显著 moderator：限时放大纸优，自定步调下纸优不显著**。Limited: g = −0.26（[−0.35, −0.16]）；Self-paced: g = −0.09（[−0.22, 0.05]，CI 跨 0）；QB = 4.12, p = .04, R² = .05（Table 1 p.11；正文 p.11 "comparisons in studies with time constraints yielded a significantly larger (QB = 4.12, p = .04) print advantage (Hedges' g = −0.26) than comparisons in studies in which participants were allowed to self-pace their reading (Hedges' g = −0.09)"）。→ 作答 UI 是否计时直接调节交付模式效应的大小；自定步调时模式效应接近消失。这是对本项目「baseline 是否限时」的仪器决策级证据。

4. **文本类型是显著 moderator：信息类/混合类纸优稳定，纯叙事无模式效应**。Informational: g = −0.27（[−0.36, −0.18]）；Mixed: g = −0.30（[−0.40, −0.21]）；Narrative: g = 0.01（[−0.20, 0.20]，ns）；QB = 7.00(2), p<.05, R² = .31（Table 1 p.11）。p.11: "Comparisons conducted with informational texts or a combination of informational and narrative texts showed significant mean effect sizes favouring paper-based reading…whereas comparisons conducted only with narrative texts showed no effect of media (Hedge's g = 0.01)." 作者警告 narrative 分支仅 k=7，须谨慎（p.15 4.3）。

5. **发表年份是显著 moderator：纸优自 2000 年起逐年增加，而非消失**。Meta-regression: b = −0.01/年, QR = 4.95, p = .03, R² = .64（Table 3, p.12–13；正文 p.12 "The beta coefficient of −0.01 (QR = 4.95, p = .03) indicates that the effect size favouring paper-based reading increased by 0.01 points a year, explaining 64% of the mean effect size variance"）。作者明言"我们没有等来技术经验自动消除屏劣势"（p.13 4.1: "our results indicate that the screen inferiority effect has increased in the past 18 years"）；同时承认用发表日期代理世代是简化（p.15 局限）。

6. **设备类型与滚动需要未达显著，但方向趋势一致**（p.12）: Computer: g = −0.23（p<.001）vs Hand-held: g = −0.12（p = .11），QB = 1.55 ns；Scrolling yes: g = −0.25（p<.001）vs no: g = −0.13（p = .06），QB = 1.99 ns。p.12: "Two variables are worth mentioning, even though their moderating effects did not reach significance." 元分析层面不支持「手持设备/免滚动可消除模式效应」，但方向性提示存在。

7. **开放作答（作答时可回看文本）不显著改变模式效应**（Table 1, p.11）: Open testing yes: g = −0.18（[−0.29, −0.07]）vs no: g = −0.26（[−0.37, −0.16]），QB = 1.21 ns。→ 在元分析证据内，「允许回看文本」不能作为抵消模式效应的设计手段（方向仍纸优）。与项目「左侧 passage 独立滚动、可自由回看/跳题」的 UI 决策直接相关。

8. **方法学 moderators 全部不显著**（Table 2/3, p.12–13）: 组分配（random −0.20 vs non-random −0.28）、测验类型（standardized −0.21 vs researcher-created −0.21）、测试媒介（same-medium −0.26 vs always-paper −0.17，QB=1.11 ns）、样本量（b=−0.00, QR=3.11 ns）、发布状态（published −0.22 vs unpublished −0.19）。→ 元分析范围内模式效应不因这些设计特征系统变化。

9. **教育水平无显著调节**（Table 1, p.11）: G1–6: −0.19、G7–12: −0.15、大学: −0.28，QB = 2.33 ns（k=3 的研究生/职业人群未纳入分析）。p.13 4.1: "there were no differences in media effects between age groups."（注意：年级跨度宽、但各层样本小且未做年份×年龄交互——作者承认该交互无法可靠分析，p.15）。

10. **效应量的教育意义解释（作者计算，供 estimand 定性用）**（p.13）: 0.21 ≈ 小学年阅读增长（0.32）的 2/3、补救干预平均效应（0.45）的 1/2。p.13: "the effects of media are relevant in the educational context because they represent approximately 2/3 of the yearly growth in comprehension in elementary school, and 1/2 of the effect of remedial interventions."

11. **发表偏倚处理：三法一致指示无偏倚**（p.10–11）: Between: fail-safe N = 1,727（Rosenthal 标准 5k+10 = 290）；Egger p = .39；published vs unpublished ANOVA QB(1,54) = 0.14, p = .71（p.10–11）。Within: fail-safe N = 475（标准 100）；Egger p = .20；ANOVA QB(1,16) = 0.02, p = .90（p.11）。灰色文献剔除敏感性：between −0.19（k=38）/ −0.20（k=51），within −0.22/−0.23，均不影响结论（p.10）。

### Class 3 — 仪器信度与缺失

12. **元分析本身无缺失率/完成率证据；缺失只以「排除标准」形式存在**（p.15, p.5）: 10 项符合纳入标准的研究因缺必要统计信息（n=8）或非正态分布（n=2）被排除（p.15 "ten studies that met the inclusion criteria could not be included due to lack of necessary statistical data (n = 8) or non-normal distributions (n = 2)"）。纳入标准第 9–10 条要求"报告包含效应量或足够统计信息（或经作者提供）"与"允许参数分析"（p.5）。→ 对审计的 Class 3：缺失率/作答率随模式变化的证据在本元分析中不存在；不能从本来源推断投递模式对缺失率的影响。

13. **作者声明未测因素含「测试工具信度」，且原始文献普遍不报告**（p.15）: "factors related to research methods (e.g., the reliability of the testing tools) or to sample characteristics (e.g., SES or degree of use of digital texts for learning purposes) could be considered. These factors were missing from most of the reports we included." → 工具信度在模式效应研究中的缺失本身构成测量可比性盲区（间接证据）。

14. **方法学变量（组分配、测验类型、测试媒介、样本量、发布状态）对效应量无系统影响**（p.12–13 Table 2/3，见发现 8）→ 元分析证据内，ES 层面的模式效应不依赖这些设计特征；但这是 ES 层面而非事件缺失层面的结论，不能外推到日志完整性。

### Class 2 — 行为改变

15. **本元分析无行为/过程指标，无直接 Class 2 贡献**。过程层面只有引述背景（非本分析发现，二级来源，供上下文）: Ackerman & Goldsmith (2011) 数字阅读下时间分配决策更不稳定（p.2）；Ackerman & Lauterman (2012) 限时条件下电脑阅读者更过度自信、成绩更低，且仅纸面阅读在限时下提高效率（p.2）。这些是引言引述的原始研究，不是本元分析的编码数据，不得当作 Delgado et al. 的实测发现。

16. **滚动作为「数字文本特征」与成绩的关系（ns 趋势，见发现 6）是分数层面证据**，且作者承认机制不清（p.15 4.4）: "One of the questions about the scrolling findings is whether the effect of scrolling is related to longer texts or some other artefact of mouse use while reading, although text length was not found to be a moderating factor." → 滚动→理解的因果机制未建立；对本项目 scrollable passage 设计无直接行为证据。

### Class 1 — 可用性/偏好

17. **无偏好/满意度测量；仅引述他人偏好研究（二级背景）**（p.2）: "several recent studies found that the preference for paper over digital-based reading persists despite technological advances (Baron, Calixte, & Havewala, 2017; Mizrachi, 2015; Kurata, Ishita, Miyata, & Minami, 2017)"; 以及 Lauterman & Ackerman (2014) "methods to overcome screen inferiority are effective only for people who prefer digital reading, but not for those who prefer paper reading"（p.2）。这些是本元分析引用的背景，非其编码发现。→ 对 Class 1 无直接贡献，Class 1 维持 `UNRESOLVED`。

## 边界与局限

- **人群边界**: 以大学生为主（between 63.79%）；教育水平无调节但研究生/职业人群 k=3 被排除（p.8, p.11）；规范人群（无阅读困难/认知障碍，p.4）；2000–2017 英文报告研究（p.5）。
- **任务边界**: 线性文本、个体默读、跨媒介内容可比、数字条件无超链接/网页导航（p.4–5）→ 与 B-tier PISA 超文本导航证据（B2/B3/B5/B6）**不重叠**：本元分析明确排除导航型数字阅读；网页导航数字阅读的媒介效应是作者声明的开放问题（p.15 "we excluded digital affordances (except for scrolling) such as hypertext reading or navigation through webpages. Their effect on reading comprehension is still an open question"）。
- **工具边界**: 4 项大规模研究占 between 样本 165,778/169,524（p.8）——但敏感性分析剔除后效应不变（g=−0.22, p<.001, p.9–10），不影响稳健性。
- **作者声明局限**（p.15）: (1) 10 项研究因统计信息缺失/非正态未纳入；(2) 异质性高，moderators 只解释部分方差，未测因素（工具信度、SES、数字文本使用程度）可能影响均值效应；(3) 世代解释基于发表日期，是简化；(4) 为隔离媒介效应而排除超文本/导航等数字功能。
- **测量边界**: within 数据集因 ES 数量少（k=18）未做 moderator 分析（p.10）；r 值插补 r=.7 为 Rosenthal 推荐但属假设（敏感性显示最大差异 <3%，p.10）；narrative 分支 k=7 结论脆弱（p.15）。
- **不可外推处**: 测验媒介对比是 mode-level（paper vs screen），非 within-mode UI variant；不含缺失率、过程数据、满意度；不含导航型/超文本数字阅读；不含自适应测试（纳入标准排除非可比功能）。

## 对审计的用途

审计主文件（`reports/research/ui-instrument-effects-evidence-audit.md`）中对 METHOD-018 的既有引用（grep 确认）:
- 行 46（C4 检索命中，gated 记录）与行 68（W1 cluster 确认）；
- 行 175（Class-4 段落）: "the mode-effect meta-analyses (Delgado 2018; Clinton 2019; Schwabe 2022; Salmerón 2024; Li & Yan 2024) bound whether screen-vs-paper delivery itself shifts comprehension scores, but were screened at metadata level only and their conclusions must not be asserted here in either direction"；
- 行 177: "adult reading-medium metas (Delgado/Clinton vs the contrary-direction Schwabe record) are all still full-text-gated — the queue must resolve them before any directional mode claim is used"；
- 行 186（Limitations）: "must not be asserted in either direction until acquired"。

本笔记（全文已读）的作用：
1. **闭合行 175/177/186 对 Delgado 的「metadata-only / 不得断言」状态**：现在可在审计中正面引用 Delgado 2018 的元分析结论（方向：纸优；方向限定：限时/信息类/年份趋势）——审计 owner 更新上述三行的引用状态（本笔记不改审计主文件）。
2. **与 UIE-27（`METHOD-012`，ACT online > paper d=.16–.22）方向相反**，强化审计已记录的跨层方向张力（行 177）: 两证据必须并列，不能统一为单一方向。差异可解释维度（不强行调和，如实记录）: Delgado 是 2000–2017 阅读媒介研究元分析（纸优、限时更强）；ACT 是 operational 大考（在线优、集中于后期题目，作者归因 differential speededness）。Delgado 的 time-frame moderator（限时放大纸优）与 ACT 的速度性解释涉及不同机制（元认知/浅层加工 vs 时间分配），两者不直接矛盾也不直接融合。
3. **支持 UIE-26（`METHOD-011` TME 来源枚举）的 timing 维度**：time-frame moderator（发现 3）为「计时策略是模式效应来源」提供元分析级证据；同时其「review/change policy」（开放测试）在 Delgado 中 ns（发现 7）——对审计行 177 的 TME 来源映射是部分支持、部分限定。
4. **对项目 UI 决策**: 发现 3（限时 vs 自定步调）直接进入 baseline 计时策略决策；发现 7（开放作答/可回看 ns）进入「可自由回看」设计——元分析证据不支持回看消除模式效应，也不支持回看改变模式效应方向。
5. **Class 3 确认 gap**: 本来源无缺失率证据（发现 12），缺失率随投递模式变化的直接证据仍主要靠 `METHOD-012`（UIE-27 omit 率）与 B-tier 导航缺失（UIE-11）。
6. **Schwabe 2022（contrary-direction）仍 gated**，行 177 的方向张力只闭合一半。

### 建议的新 UIE 条目草稿

> 编号说明：先例笔记 `METHOD-017.md` 已建议 UIE-31..37 草稿，本笔记草案同样从 UIE-31 起编号，**与 METHOD-017 草案编号冲突**；以下编号均为占位，最终编号与合并由审计 owner 在综合时仲裁。

| #（占位） | Claim（中文主张） | Pages | 暂定 verdict | Scope boundary |
| --- | --- | --- | --- | --- |
| UIE-31 | 投递模式（screen vs paper）移动阅读分数分布，纸优：between g=−0.21 [−0.28,−0.14] k=56 与 within dc=−0.21 [−0.37,−0.06] k=18 两设计独立同向；但 I²=72.24/89.88、预测区间跨零（−0.56~0.14 / −0.90~0.47），方向断言须限定人群/任务 | p.1, p.9, p.10 | `SUPPORTED`（方向限定；与 UIE-27 的 ACT 在线优方向相反，须并列） | 2000–2017 线性文本阅读/测验任务，纸 vs 电脑/平板/手机/e-reader；排除超文本导航；mode-level 非 within-mode variant |
| UIE-32 | 时间压力放大投递模式效应：限时 g=−0.26 vs 自定步调 g=−0.09（CI 跨 0），QB=4.12, p=.04 → 作答 UI 计时策略直接调节模式效应大小 | p.11 | `SUPPORTED` | 元分析 moderator 层面；R²=.05 |
| UIE-33 | 文本类型调节模式效应：信息类 −0.27 / 混合类 −0.30 纸优显著，纯叙事 0.01 无效应（k=7，作者警告谨慎）；R²=.31 | p.11, p.15 | `SUPPORTED`（narrative 分支 `PARTIAL`） | 信息类/说明文阅读任务最稳定；叙事文本分支样本小 |
| UIE-34 | 纸优自 2000 年起逐年增加（b=−0.01/yr, QR=4.95, p=.03, R²=.64）→ 「数字原住民经验自动消除屏劣势」不成立；日期代理世代是作者承认的局限 | p.12, p.13, p.15 | `SUPPORTED`（meta-regression；世代解释简化） | 2000–2017 时间窗；世代推断不可外推为个体经验因果 |
| UIE-35 | 作答时可回看文本（open testing）不显著改变模式效应：open −0.18 vs closed −0.26，QB=1.21 ns → 「回看/开放作答」不能作为抵消模式效应的设计手段 | p.11 | `SUPPORTED`（ns 边界证据） | 元分析 moderator 层面；方向仍纸优；与项目「可自由回看」UI 直接相关 |
| UIE-36 | 发表偏倚三法一致指示无偏倚（between: fail-safe N=1,727 vs 290、Egger p=.39、pub-vs-unpub p=.71；within: 475 vs 100、p=.20、p=.90）→ 纸优方向非发表偏倚产物 | p.10, p.11 | `SUPPORTED` | 元分析层面；灰色文献剔除不改变结论 |

共建议新增 6 条（UIE-31..36，占位编号）：Class 4 全部六条（31–36）。Class 3/2/1 无新条目：Class 3 无缺失率证据（发现 12，保持 gap）、Class 2 无过程指标（发现 15，仅背景）、Class 1 无偏好测量（发现 17，维持 `UNRESOLVED`）。

## 提取验证记录

- 全文通读：`pdftotext -layout` 逐页（物理页 1–16）复核关键段落、Table 1/2/3 与 Fig. 1–4；摘要与正文结果数字一致。
- SHA-256 与 catalog 一致性：未复算（catalog 已核验）；书目与 PDF 首页一致，无差异标注。
- 本笔记之外未修改任何文件（审计主文件、catalog、checksums 未触碰）。
