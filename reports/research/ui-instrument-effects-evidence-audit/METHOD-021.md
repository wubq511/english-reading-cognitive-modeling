# 提取笔记：METHOD-021 — Salmerón et al. 2024 手持设备 vs 纸媒阅读理解元分析

**结论速览（中文）**：这是审计队列中第一份专测「手持设备 vs 纸」的设备尺寸维度证据。两个多水平随机效应元分析一致显示手持设备阅读存在小而显著的纸媒优势（between-participant `g = −0.113`，within-participant `dc = −0.103`），约为此前以电脑为主的 screen inferiority 元分析效应量（`g ≈ −0.21 ~ −0.25`）的一半。moderators 中仅学业阶段（大学生 `g = −0.227` vs 中小学生 `g = +0.057`）与施测情境（单人 `g = −0.230` vs 团体 `g = +0.004`）显著；文本体裁、文本长度、翻页/滚动导航、设备亚型（平板 vs 电纸书）、时间压力、题目类型、发表年份、测试标准化程度与信度均为 null。between 效应含离群值时降至不显著（`g = −0.069`），且 94% 初级研究为便利样本——效应真实但脆弱，方向性结论须带这些限制。书目与 catalog 有两处作者姓名不一致（见下）。

---

## 头部

- **source ID**：`METHOD-021`
- **本地路径**：`sources/library/papers/methods/2024_Salmeron_HandheldVsPaper.pdf`（20 页，PDF 物理页码）
- **书目（catalog 为准，已与 PDF 首页核对）**：
  - Salmerón, L., Altamura, L., Delgado, P., Karagiorgi, A., & Vargas, C. (2024). Reading comprehension on handheld devices versus on paper: A narrative review and meta-analysis of the medium effect and its moderators. *Journal of Educational Psychology, 116*(2), 153–172. https://doi.org/10.1037/edu0000830（在线首发 2023-10-16，正式卷期 2024）
  - **与 PDF 首页不符处（不改 catalog，仅标记）**：catalog 写作者 `Laura Altamura` / `Andria Karagiorgi`；PDF 首页实际为 `Lidia Altamura` / `Anastasia Karagiorgi`（PDF p.1）。其余（标题、卷期页码、DOI、五位作者含 Vargas）一致。

## 研究概览

- **研究问题**：手持设备（平板/电纸书）vs 纸媒阅读理解是否也存在「screen inferiority effect」，效应量多大，哪些因素（reader/text/activity/sociocultural context 四类，按 Snow 2002 reading for understanding 框架）起调节作用；并对照此前以电脑为主的元分析效应量。
- **设计**：系统综述（narrative review）+ 两个独立的三水平随机效应元分析，按研究设计（between / within）分列，未预注册，数据公开（OSF）。检索 2010–2022，来源 WoS/Scopus/PsycInfo/ProQuest + 11 份既往综述回溯 + 前向检索 + 灰色文献作者联系。
- **样本**：初筛 1,845 条记录 → 49 研究（30 between / 19 within），63 效应量；去离群值后 between 数据 38 效应量（29 研究，原含 161,469 名参与者）、within 数据 21 效应量（18 研究，1,379 名参与者）。注意 between 数据参与者数由两三项大规模研究主导（含 NAEP 2017 转型研究，Jewsbury et al. 2020，p.10, p.14）。
- **任务与材料**：纸 vs 平板/电纸书阅读后测阅读理解；多数为闭卷式选择题/判断题测试（between k=31；within k=15），少数开放题；文本以说明文为主，平均 1,549 词（between）/ 868 词（within）。
- **变量**：产品分数为主（Hedges' g / 标准化均数变化 dc）；无过程指标、无缺失率指标。moderators：学业阶段、体裁、字数、导航方式（翻页 vs 滚动）、设备类型（平板 vs 电纸书）、时间限制、题目类型、施测情境（单人/团体）、可否手持设备、发表年份；方法学变量：样本量、抽样方式、标准化与否、信度、发表状态。

## 核心发现（按四类主张分组）

### Class 4 — 学习/构念与 estimand（本论文主角色：设备尺寸维度）

- **C4-1 手持设备存在小而显著、约为电脑一半的纸媒优势**：between `g = −0.113`，95% CI [−0.215, −0.012]，p = .030；within `dc = −0.103`，95% CI [−0.145, −0.062]，p < .001（负值 favor 纸媒）。作者将手持效应量与既往以电脑为主的元分析对照：「approximately half the size of that found in previous synthesis that mostly analyzed paper–computer comparisons (g = −0.25, Clinton, 2019; g = −0.21, dc = −0.21, Delgado et al., 2018; RVE = −0.21, Kong et al., 2018)」。(PDF pp.1, 11, 12, 14)
  - 原文：`Results from the two multilevel random-effect meta-analyses ... consistently showed a significant small size effect favoring print text comprehension` (PDF p.1)
- **C4-2 between 效应异质性极大、预测区间跨零**：`Q(37) = 256.27, p < .001`，`I² = 94.39`（其中 study-level 73.54%、within-study 20.85%），95% PI [−0.486, 0.259]——真实效应在不同人群可正可负。(PDF p.11)
- **C4-3 between 效应不稳健于离群值**：含离群值后 `g = −0.069`，95% CI [−0.177, 0.038]，p = .191，不再显著；within 含离群值 `dc = −0.093`，p = .006 仍显著（原文此处疑排版错误：「95% CI [−0.153, −0.34]」上界应为 −0.034，且 k/n 疑似互换，原 within 全量 23 效应量/19 研究）。(PDF p.12)
- **C4-4 within 设计异质性极低、无可调**：`Q(20) = 7.309, p = .995`，I² = 0，95% PI [−0.145, −0.062]；因此未做 moderator 分析，且「none of the primary studies resulted in significant differences」。(PDF p.12)
- **C4-5 moderator：学业阶段显著**——大学生 vs 中小学：`F(1, 12.67) = 6.321, p = .026`；小学+初中 `g = +0.057`（CI [−0.136, 0.250]），大学生 `g = −0.227`（CI [−0.405, −0.049]），即纸媒优势集中于大学生。(PDF p.12, Table 1 p.15)
- **C4-6 moderator：施测情境显著**——单人 vs 团体：`F(1, 17.74) = 5.127, p = .036`；单人 `g = −0.230`（CI [−0.413, −0.048]），团体 `g = +0.004`（CI [−0.142, 0.149]）。作者解释为单人/实验室情境更利于专注，且与学业阶段混淆（大学生研究多在实验室单人施测）。(PDF pp.12–13, Table 1 p.15, discussion p.17)
- **C4-7 moderator 均 null**：体裁（narrative `g = −0.206` vs expository `g = −0.083`，p = .203）、文本长度（word count，p = .503/.983）、导航方式（paging `g = −0.109` vs scroll `g = −0.149`，p = .867）、设备类型（tablet `g = −0.103` vs e-reader `g = −0.155`，p = .615）、时间压力（free `g = −0.108` vs time pressure `g = −0.126`，p = .853）、题目类型（p = .909）、发表年份（p = .872）、样本量（p = .902）、标准化测试（p = .332）、测试信度（p = .412）、发表状态（p = .678）。(Table 1 p.15, Table 2 p.16)
- **C4-8 唯一的两个大规模代表性样本研究（NAEP 2017 转型研究，Jewsbury et al. 2020）均得显著纸媒优势**（4 年级与 8 年级）；「in the cases in which differences between reading media among the effect sizes in primary studies were significant, they consistently favored text comprehension outcomes」→ 作者自认无法排除中小学阶段受负向影响。(PDF pp.14, 17)
- **C4-9 时间压力 moderator 未在手持设备上复现**（与电脑上的 Delgado 2018 相反，作者原预测时间限制效应更大）；作者推测手持设备更接近纸的深度阅读体验。(PDF p.16)
- **C4-10 前代元分析设备维度调节检验均 null 但样本不足**：Delgado 2018（手持 12 研究/14 效应量）与 Öztop & Nayci 2021（仅 2 项手持研究）设备类型调节均不显著；本元分析是首个专测手持设备的中介级证据。(PDF p.2)
- **C4-11 教育与决策建议（作者主张，非效应量）**：「we recommend caution when using such devices in educational scenarios where the goal is to promote or to assess reading comprehension」并建议学校暂以纸为主、探索手持设备优于电脑的用法。(PDF p.18)

### Class 2 — 行为改变

- **C2-1 本元分析不测量行为/过程指标**：纳入研究只报告产品分数，无事件、时间、缺失率等过程数据。其贡献是**行为相关 UI 变量的产品级 null**：翻页 vs 滚动的 comprehension 无差异（`g = −0.109` vs `−0.149`，p = .867），但滚动组仅 5 个效应量，作者明言「the specific differences between swiping full pages ... or scrolling ... on reading comprehension have not been examined for handheld devices」，功率不足以作结论。(PDF pp.4, 10, 16)
- **C2-2 手持/具身交互变量无法分析**：可否手持设备仅 2 项研究有变异（between 数据），within 数据 8/16 允许手持，作者承认无法在元分析层面检验具身交互假设（Mangen 线）。持设备这一物理 affordance 对 comprehension 的调节仍是开放问题。(PDF pp.10, 17)
- **C2-3 narrative review 层的行为相关背景（非本元分析证据）**：滚动丢失纸页的空间定位于线索（引 Haverkamp et al. 2023）；低注意/ADHD 学生的行距调节证据方向矛盾（Stern & Shalev 2013 屏优、Ben-Yehudah & Brann 2019 纸优）。(PDF pp.4, 16)

### Class 3 — 仪器信度与缺失

- **C3-1 测试信度不调节中媒效应**：测试信度（questionable `g = −0.152` vs acceptable `g = −0.070`，p = .412）与标准化/自制测试（p = .332）均 null；作者表述为「The effect was robust and arised regardless of the reliability of the reading comprehension test used」——即仪器信度层面没有证据表明纸/屏差异是低信度仪器的产物。(PDF p.17, Table 1 p.15)
- **C3-2 元分析层面的数据缺失/报告缺失**：多个 moderator 因初级研究报告不足而无法编码（设备类型 4 个效应量无法区分、within 时间限制 7 项未报等），作者呼吁「increasing effort in detailing research methods exhaustively」——仪器与报告细节缺失直接损害 moderator 估计。(PDF pp.7, 10, 17)
- **C3-3 抽样质量问题**：between 数据 38/40 效应量为便利样本，仅 2 项概率抽样（Jewsbury 2020）；作者以统计功效与可推广性警示解读（Stanley et al. 2018）。(PDF pp.10, 14)
- **C3-4 发表偏倚检查**：funnel plot 目测不对称但 Egger MLMA 截距不显著（between `b = −0.364`, p = .501；within `b = 0.081`, p = .181）；发表/未发表效应量无显著差异（p = .678 / .336）。(PDF p.12)

### Class 1 — 可用性/偏好

- **C1-1 本元分析不提供可用性/偏好一级数据**：偏好证据仅以二手引述出现——「Empirical research on reading medium preferences indicates that readers value handheld devices for their tactile nature and the ability to hold them, in contrast to reading on computers (Mangen & Pirhonen, 2022)」（PDF p.6）；e-reader 被知觉为「clear, easy to read, more natural, less tiring」（引 Bon & Burke 2022，PDF p.5）。均属 review-mediated，不可当一级证据。
- **C1-2 一个「偏好 vs 客观测量分离」的既有锚点**：参考文献收录 Kretzschmar et al. 2013（《Subjective impressions do not mirror online reading effort》），正文用以说明设备间 comprehension 无差异（PDF p.5）——方向支持「主观偏好≠客观效果」，但仅二手引用。

## 边界与局限（作者声明 + 提取者判定）

- **情境边界（作者明示）**：效应刻画的是「taking multiple-choice text comprehension questionnaires」情境下的表现，作者自警不能推广到自然阅读/非测试情境（引 Rupp et al. 2006：MC 情境可能被当作 problem-solving 而非 purposeful comprehension reading）。(PDF pp.16–17)
- **样本边界**：几乎全部便利样本；仅 2 项大规模代表性研究（NAEP 转型）；中小学段结论依赖少量研究，作者「cannot rule out」中小学负向效应。(PDF pp.14, 17)
- **confound 声明**：大学生 moderator 与文本长度/体裁、单人施测与实验室情境可能混淆（「we cannot discard a confounding effect between reader and text characteristics, namely academic level and text length or genre」）。(PDF p.14)
- **功率边界**：滚动仅 5 效应量、e-reader 仅 8 效应量、可否手持仅 2 项有变异——这些 null 不能当「已证无差异」。(PDF pp.10, 16, 17)
- **发表窗口**：检索止于 2022-06；2010 前无手持研究（平板 2010 年出现），无法检验代际/Web 2.0 时间趋势（发表年份 null 的解释受限）。(PDF pp.7, 17)
- **提取者备注**：catalog 与 PDF 首页作者名两处不符（Altamura 名、Karagiorgi 名）；两处疑似排版错误——between 主效应 CI 打印为 `[0.215, −0.012]`（应为 [−0.215, −0.012]，负号/顺序错），within 离群值敏感性段 `95% CI [−0.153, −0.34]` 上界应为 −0.034 且 k/n 互换——引用时勿传播错值。全文 20 页均通读，无 `ABSTRACT-ONLY` 条目。

## 对审计的用途

- **直接解决审计 INTERIM 状态**：审计主文件此前仅按 metadata 记录 Salmerón 2024（S3 行、Limitations 行、Class 4 段「screened at metadata level only ... must not be asserted in either direction」），并把它与 Delgado/Clinton/Schwabe 一起列为待全文裁决的方向性 tension。本文可部分裁决**设备尺寸维度**：手持设备纸媒优势 ≈ 电脑的一半，方向与 Delgado/Clinton 一致、与 Schwabe 的叙事文本 null 部分相容（体裁在本文也 null）。但注意与 **UIE-27（METHOD-012，ACT）方向张力**：ACT 在线 > 纸（d = .16–.22，且集中于后段题、疑似速度差异），而本文（含 NAEP 2017 转型研究）为纸 > 手持——两者方向相反但人群、情境（高中应试 speededness vs K-12/大学 comprehension）不同，合成时必须分别陈述，不能并成单一方向性结论。
- **支持/限定既有条目**：
  - **UIE-27**：提供设备尺寸对照（电脑 > 手持的效应量梯度）与「同一方向证据在不同人群反转」的张力；限定：UIE-27 是 mode-level 操作性证据，本文是实验/类实验综合，二者测量情境不同。
  - **UIE-26（METHOD-011，TME 综述）**：其「屏幕尺寸/清晰度」类 TME 来源在此获得部分反证——手持类内屏幕尺寸差异（平板 vs 电纸书）在 comprehension 上 null；但本文无时间限制/反馈/修订政策等 UI 常量，不构成对 UIE-26 的全面反驳。
  - **UIE-29（METHOD-014）与 C 层布局证据**：本文证明设备尺寸调节产品效应量，支持「medium/设备层改变 estimand」的总前提（audit Class 4 结论 1/4）。
  - **Class 1 的 UNRESOLVED 状态**：本文不提供可用性/偏好一级证据，Class 1 实证缺口不变。
- **建议的新 UIE 条目草稿**（编号延续 UIE-30 之后，最终编号由审计主文件决定）：
  1. **UIE-31（Class 4）**：claim：设备尺寸维度调制投递模式效应——手持设备阅读的纸媒优势（between `g = −0.113`，within `dc = −0.103`）约为以电脑为主的既往元分析（`g ≈ −0.21 ~ −0.25`）的一半，且都在 Cohen small 区间。pages：PDF pp.1, 11–12, 14。暂定 verdict：`SUPPORTED`（元分析层面；注意 between 效应含离群值即不显著、PI 跨零）。scope boundary：阅读 comprehension 产品分数，平板/电纸书 vs 纸；非作答 UI 变体；对「UI 变体改变 estimand」为支持性、非决定性证据。
  2. **UIE-32（Class 4）**：claim：手持类内部设备亚型（平板 vs 电纸书）与导航方式（翻页 vs 滚动）均不调节 comprehension 中媒效应；时间压力 moderator 在手持设备上不成立（与电脑证据相反）。pages：PDF pp.16（Table 1 p.15）。暂定 verdict：`SUPPORTED` as nulls within corpus，但滚动/电纸书组功率不足，**不得据此宣称「布局/导航变体在中介效应上等效」**——翻页 vs 滚动在手持设备上的产品级差异仍为开放问题（作者明言未检验）。scope boundary：comprehension 分数、手持设备；不覆盖作答界面内布局/导航。
  3. **UIE-33（Class 4）**：claim：施测情境（单人 vs 团体）调节中媒效应（单人 `g = −0.230` vs 团体 `g = +0.004`，p = .036），纸媒优势只在可专注的单人/实验室情境出现；与学业阶段混淆。pages：PDF pp.12–13, 17。暂定 verdict：`PARTIAL`（显著但 confounded，作者自述）。scope boundary：投递/施测情境维度，非 UI 变体；提示 baseline 作答环境的受控性本身是估测量的一部分。
  4. **UIE-34（Class 4）**：claim：学业阶段调节（大学生 `g = −0.227` vs 中小学 `g = +0.057`，p = .026），但仅有的两项大规模标准化测试研究（NAEP 2017 转型，4/8 年级）均呈显著纸媒优势——中小学结论不能排除负向效应。pages：PDF pp.12, 14, 17。暂定 verdict：`PARTIAL`（moderator 与大规模证据方向分歧）。scope boundary：年龄/样本维度；支持「同 UI 对不同人群 estimand 效应可异」前提。
  5. **UIE-35（Class 4 + Class 3 边界）**：claim：中媒效应在测试信度与标准化程度上稳健（均 null moderator，「robust ... regardless of the reliability」），表明纸/屏差异不是低信度测量伪影；同时初级研究报告缺失严重损害 moderator 估计（元层缺失）。pages：PDF p.17, Table 1 p.15。暂定 verdict：`SUPPORTED` as reported nulls；元层报告缺失为 `SUPPORTED` as study-operation evidence。scope boundary：产品分数信度层面，不覆盖过程通道信度（对应审计 Class 3 的 BENCH-E0 责任不变）。
