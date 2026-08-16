# METHOD-035 提取笔记：Furenes, Kucirkova & Bus (2021) 儿童纸屏阅读元分析

## 头部

- **source ID**: `METHOD-035`
- **本地路径**: `sources/library/papers/methods/2021_Furenes_PaperVsScreen.pdf`（SHA-256 见 catalog，已核验）
- **完整书目**: Furenes, M. I., Kucirkova, N., & Bus, A. G. (2021). A Comparison of Children's Reading on Paper Versus Screen: A Meta-Analysis. *Review of Educational Research*, 91(4), 483–517. DOI: 10.3102/0034654321998074
- **书目核对**: PDF 首页与 catalog 一致（标题、venue、卷期页码、DOI）；唯一不符：catalog `authors` 写作 "Monica I. Furenes"，PDF 首页及作者行均为 **"May Irene Furenes"**（PDF p.1）。按任务纪律仅在此标注，不改 catalog。
- **页码约定**: 下文页码均为 PDF 物理页（PDF p.1 = printed p.483；PDF 页 = printed 页 − 482）。
- **审计角色**: Class 4 儿童段证据（1–8 岁）。焦点：效应量、moderators（年龄/成人陪伴/材料）、与成人元分析的差异。

## 研究概览

- **研究问题**（PDF p.6）：① 若纸书与数字书唯一差异是媒介，故事理解与词汇是否相同？② 数字书设计（enhancements）能否解释其收益？③ 内嵌词典如何与其它 enhancements 交互？④ 成人陪伴如何影响结论？
- **样本/设计**: 元分析（random-effects，Hedges' g，正号 = 数字书有利）。**39 项研究、30 篇文章/报告、n = 1,812 名 1–8 岁儿童**（PDF p.11）。纳入标准：纸/数字叙事对照的实验或准实验；结局为故事理解（story comprehension, SC）或词汇（vocabulary, VOC）；语言限定英/荷/德/挪（PDF pp.7–8）。多数为 RCT（n = 21，个体层面随机）或 counterbalanced within-subject（n = 14）（PDF p.12）。排除仅测阅读行为的研究、字母/音位等基础技能、>8 岁、人工耳蜗/自闭症样本（PDF p.8）。
- **任务与材料**: 同一故事书纸版 vs 数字版（图画书 app / e-book / CD-ROM 等，任何数字设备；18 项在触屏设备，较早研究用鼠标，PDF p.12）。数字书多数带附加功能：34 项有 voiceover、13 项内嵌词典、18 项含 story-related enhancements；仅 5 项研究是"除屏幕外别无差异"（如 Krcmar & Cingel 2014; Strouse & Ganea 2017，PDF p.12）。题材以 fiction 为主。
- **结局变量**: SC（故事内容答问、复述质量、排序任务）与 VOC（接受/表达命名、定义任务）（PDF p.9）。
- **过程/缺失指标**: 本文为产品结局元分析，**不提供过程指标**；仅以编码方式记录 design 特征、成人陪伴、attrition（risk-of-bias 域之一，多数研究低风险，PDF p.12）。
- **质量与发表偏倚处理**: Cohen's κ 0.63–1.00（19 变量，PDF p.9）；outlier 按 CI 不重叠剔除；funnel plot + trim-and-fill；fail-safe N；prediction interval（PDF p.10）。

## 核心发现（按四类主张分组）

### Class 4 — 学习/构念与 estimand（本论文的主贡献）

1. **媒介（纸 vs 屏）本身移动儿童故事理解分数，但整体净效应接近零，纸优势仅出现在"纯数字化"对照中。**
   - SC 总效应（26 项研究，剔除 3 outliers 后）：g = −0.07，95% CI [−0.17, 0.04]（含 0，无方向；I² = 35.17，Q p = .04，预测区间 [−0.47, 0.34]）（PDF p.16；Table 2 写 CI [−0.18, 0.04]，PDF p.19，下限与正文差 0.01，属报告内部小不一致）。
   - 纸/数字仅差在最小附加（voiceover 和/或高亮字）：纸优于屏，k = 10, g = −0.22, 95% CI [−0.36, −0.08]，预测区间 [−0.38, −0.06] 不含 0（PDF p.17）。Table 2 的 "No enhancements" 子组 k = 11, g = −0.20 [−0.33, −0.08]（PDF p.19）——正文子组（k = 10）与表（k = 11）口径略异，需标注。
   - 摘要句："The comparison of digital versus paper books that only differed by digitization showed lower comprehension scores for digital books."（PDF p.1）
2. **数字书设计特征是方向翻转器：story-related enhancements 把 SC 翻到数字书有利，词典对 SC 无效甚至有害。**
   - 有 enhancements 时纸优势消失：k = 16, g = −0.03 [−0.18, 0.11]，Q(1) = 3.48, p = .062（PDF p.17）。
   - 仅 story-related：k = 8, g = 0.17 [0.01, 0.32]（PDF p.18）；story-related + 词典：k = 3, g = −0.20 [−0.40, 0.01]；词典仅（k = 5）无方向。子组比较 Q(2) = 7.79, p = .020（PDF p.18）。
   - "the enhancements interfered with comprehension of the digital book if they were combined with a dictionary"（PDF p.18）。
3. **词典对词汇有利、对故事理解无益——同一 UI 特征对不同估量方向相反。**
   - VOC 词典仅：k = 4, g = 0.49 [0.23, 0.74]；词典 + story-related：k = 6, g = 0.09 [−0.11, 0.28]；Q(1) = 5.83, p = .016（PDF p.21）。SC 侧词典"no or negative effect"（摘要 PDF p.1；实践建议处 "promotes vocabulary learning but harms meaning-making"，PDF p.27）。
4. **词汇结局整体偏向数字书，但稳健性弱。**
   - VOC 总效应：k = 18, g = 0.20 [0.08, 0.32]（PDF p.20；Table 3 写 g = 0.22 [0.09, 0.35]，PDF p.23，文本与表不一致）；trim-and-fill 补 6 项后降为 g = 0.09 [−0.04, 0.23]，不再显著；fail-safe N = 55（PDF p.20）。
   - 正文报告 "these studies included 881 children (n_digital = 557, n_print = 488)"（PDF p.20）——557 + 488 = 1,045 ≠ 881，**报告内部数字不一致，引用时须标注**。
5. **Moderators：设置与 SES 调制 SC 的纸优势；年龄（1–8 岁）不显著；体裁仅调制 VOC。**
   - 学校设置纸优于屏：k = 9, g = −0.28 [−0.42, −0.15]，预测区间 [−0.49, −0.07] 不含 0；家庭 k = 5, g = 0.08、实验室 k = 12, g = 0.06；Q(2) = 15.56, p < .001（PDF p.16）。
   - 低 SES 样本纸优于屏：低/混合 SES k = 17, g = −0.19 [−0.32, −0.05] vs 中高 SES k = 9, g = 0.05；Q(2) = 6.71, p = .010（PDF p.17）。
   - 年龄：以各研究中位年龄元回归 SC 不显著（PDF p.17）；VOC 的 SES/年龄/地点均不相关（PDF p.20）。
   - 体裁：SC 无显著 medium × genre（PDF p.16）；VOC 显著——含 nonfiction 时更偏数字书：k = 6, g = 0.42 [0.23, 0.61] vs 纯 fiction k = 12, g = 0.09；Q(1) = 7.87, p = .005（PDF p.20）。
6. **成人陪伴是第三个"仪器变量"：同样的陪伴水平下，enhancements 的效果方向翻转。**
   - 仅纸书有成人支持（数字书独立读）：纸优于数字书，k = 7, g = −0.22 [−0.38, −0.06]，预测区间 [−0.43, −0.01]（PDF p.18）。
   - 两条件陪伴相同：未增强数字书 < 纸（k = 10, g = −0.22 [−0.36, −0.08]）；story-related 增强数字书 > 纸（k = 5, g = 0.20 [0.03, 0.36]）；词典居中（k = 4, g = 0.04）；Q(2) = 14.68, p < .001（PDF pp.18–19）。
   - 摘要："Adults' mediation during print books' reading was more effective than the enhancements in digital books read by children independently."（PDF p.1）
7. **与成人元分析的差异（本文自述，PDF p.22）**: 成人/学生段的 "paper advantage" / "screen inferiority"（Clinton 2019; Delgado 2018; Kong 2018，PDF p.2）在本儿童段并不整体复现：SC 聚合为 null；无体裁交互；VOC 方向相反（数字书有利，且 nonfiction 更有利——与 Delgado 2018 "nonfiction 屏劣势" 相反，PDF pp.22–23）。作者归因于早期儿童 nonfiction 常嵌于叙事线、且词汇书的多媒体目标是生词（PDF pp.22–23）。
8. **年份趋势**: VOC 的 medium 效应随发表年变新而增大（z = 2.84, p = .005，作者解释为数字书质量改善，PDF p.15）；发表状态（未发表 vs 期刊）对 SC 无显著影响（p = .221，PDF p.15）；样本量与设计（RCT vs within-subject）无影响（PDF p.15）。

### Class 2 — 行为改变（本论文为间接/二手证据）

- 元分析**按设计排除了仅测阅读行为的研究**（"apart from studies just focusing on behavior during book reading (e.g., Moody et al., 2010; Rees et al., 2017) we did not include studies targeting basic reading skills…"，PDF p.8），故不提供自身过程指标。
- 但其引用的原始研究给出方向性行为证据：增强型电子书比纸书/无增强电子书诱发更多**非内容相关互动**（device-focused talk、推开手等），k 级引用 Chiong et al. (2012)（PDF p.5）；Richter & Courage (2017) 中 3–4 岁儿童在纸书条件下更不专注、更多 off-task 时间（PDF p.2）；Bus & Anstadt (2020) 平台 analytics 显示儿童单次会话读更多书、重复更多次（PDF p.3）。
- 作者的理论解释（cognitive load / Mayer 多媒体学习模型）：设备操作（point, click, swipe）与叙事加工竞争有限认知资源，"the device seems to attract young children's attention at the expense of attention paid to the storyline"（PDF p.25）；并假设儿童因习惯游戏化互动而主动寻找交互（PDF p.2）。
- **判定**: `PARTIAL`——设计/媒介确实改变儿童交互行为且改变可能是 construct-irrelevant（device talk），但均为元分析内引用的二手叙述，无效应量、无本元分析的直接过程指标；行为证据链路到我们的作答 UI 是 `PROJECT-INFERENCE`。

### Class 3 — 仪器信度与缺失（贡献极弱）

- 缺失相关仅存在于 risk-of-bias 编码："bias due to missing outcome data (attrition rate)"，多数研究 attrition 低风险（PDF pp.9, 12）；无 item-level 缺失率、无可比性分析、无按条件的数据完整性报告。
- 值得警示的元层面问题：报告存在内部数值不一致（正文 881 vs 557+488；文本/表 g 与 CI 差异；SC 子组 k = 10 vs 11），任何复用其数字的综合必须回到原文核验。
- **判定**: 本论文对 Class 3 无直接贡献（`UNRESOLVED` 于缺失/信度主张）；仅提供"结局层面缺失未系统报告"的反证边界。

### Class 1 — 可用性/偏好（无直接证据）

- 未测 usability/satisfaction/preference；阅读行为研究被排除（PDF p.8）。
- 唯一相近的是投入/注意类观察，且**方向与产品分数相反**：数字书条件下儿童注意/投入更好（PDF p.2、p.3），而纯数字化对照下 SC 偏纸（g = −0.22）。即"投入度/参与感指标朝数字有利"与"理解分数朝纸有利"并存——**参与/偏好类指标不可当作产品分数代理**（本项目的推论，`PROJECT-INFERENCE`）。

## 边界与局限（作者自述 + 提取者判定）

- **作者自述局限**（PDF p.26）: ① 对 enhancements 只能做粗分类（story-related vs dictionary），无法区分与故事线的连贯度（fine-grained coherence）；② 现有数字书 enhancement 质量偏低，可能低估数字书潜力；③ 因 enhancement 组合受限，成人支持 vs 独立数字阅读的比较不充分；④ 结局多为 SC/VOC，缺阅读动机；⑤ 样本集中在 4–5 岁，难推广到婴幼儿与向常规阅读过渡的大龄儿童。
- **提取者补充边界**: ① 人群 1–8 岁 emergent readers，多为听读/共读图画书（常含旁白、插图），**不是独立识字者的文本默读**——到本项目 baseline（独立阅读英文说明文/题文 MC 作答）的迁移是 `PROJECT-INFERENCE`；② 材料为叙事图画书，体裁以 fiction 为主，本项目为说明文/测试文本；③ "媒介"对比是纸 vs 数字设备整体，未分离屏幕尺寸/翻页方式/设备类型（触屏 vs 鼠标，PDF p.12 仅编码设备类型）；④ 词典类增强近似"文本内词义注释"，与 UI 层 glossary/翻译工具最接近，可类比但非同一层。
- **不确定/阴性结果保留**: SC 聚合 null 且预测区间很宽（[−0.47, 0.34]）；VOC 正效应在 trim-and-fill 后消失（0.20→0.09）；词典+story-related 合并反而负向；纯 fiction VOC 无差异。以上均须随结论传播。

## 对审计的用途

- **审计主文件现状**: `METHOD-035` 在 `reports/research/ui-instrument-effects-evidence-audit.md` 中无 UIE 条目引用，仅作为队列 E2 的已定位未读项出现；`reports/research/human-tasks/wayfinder-5-ui-instrument-effects.md` 条目 21 已标记入库。本文是审计 Class 4 "mode-effect 元分析须全文获取后才能做方向性断言"（审计 Limitations 与 Remaining audit debt 两处）中的一篇，现已读完，**可局部关闭该队列缺口（儿童段）**。
- **可支持**: 审计决策含义第 1 条"投递仪器/设计特征会移动估量"在儿童段获得直接元分析证据；方向性结论是**有条件的**（纯数字化对照、学校、低 SES 才见纸优势；词汇与故事理解方向相反；enhancements 可翻转向量）——比成人段（METHOD-012 的 d = .16–.22 单向优势）更强调条件性，需防止把"纸优于屏"当全局事实。
- **可反驳/限定**: 审计队列 E2 引述为"children's paper-vs-screen meta-analysis"——不可据此断言儿童段存在统一 screen-inferiority；对 Class 4 "no locally held source demonstrates … variant change moves the estimand" 的缺口，本文在**媒介级与设计特征级**提供证据，但仍是儿童图画书叙事段，不关闭"MC 作答 UI 变体"的缺口。
- **不与既有 UIE 条目直接冲突**；与 UIE-29（METHOD-014，5–8 年级纸/数字过程行为）构成年龄互补：METHOD-014 是学龄段过程行为，METHOD-035 是幼儿段产品分数。

## 建议的新 UIE 条目草稿

1. **UIE-31（Class 4, 草稿）**: 投递媒介本身（纸 vs 屏）移动幼儿故事理解估量：纯数字化/最小增强对照纸优于屏（k = 10, g = −0.22, 95% CI [−0.36, −0.08]，预测区间 [−0.38, −0.06] 不含 0），但 26 项研究聚合为 null（g = −0.07, CI [−0.17, 0.04]）——媒介效应存在且条件化，方向由设计/设置/SES 调制。
   - 页码: PDF pp.1, 16–17, 19；暂定 verdict: `SUPPORTED`（儿童段、元分析层面）；scope: 1–8 岁叙事图画书 SC，独立识字者/测试文本迁移为 `PROJECT-INFERENCE`。
2. **UIE-32（Class 4, 草稿）**: 同一数字书设计特征对不同估量方向相反——内嵌词典促进词汇（词典仅 k = 4, g = 0.49 [0.23, 0.74]）但对故事理解无益甚至有害（story-related + 词典 k = 3, g = −0.20 [−0.40, 0.01]；Q(2) = 7.79, p = .020）；story-related enhancements 把 SC 翻向数字书（k = 8, g = 0.17 [0.01, 0.32]）。
   - 页码: PDF pp.1, 18, 21, 27；暂定 verdict: `SUPPORTED`；scope: 同上（词典 ≈ 文本内词义辅助，类比受限）。
3. **UIE-33（Class 4, 草稿）**: 设置与 SES 调制媒介效应——学校 k = 9, g = −0.28 [−0.42, −0.15]、低 SES k = 17, g = −0.19 [−0.32, −0.05]，均显著异于家庭/实验室与中高 SES（Q(2) = 15.56, p < .001；Q(2) = 6.71, p = .010）；年龄 1–8 不显著。
   - 页码: PDF pp.16–17；暂定 verdict: `SUPPORTED`；scope: 同人群；含义：投递媒介 × 亚组交互 → 组间估量可比性风险。
4. **UIE-34（Class 2, 草稿）**: 数字媒介与增强特征改变儿童交互行为且可能是 construct-irrelevant——增强电子书诱发更多非内容相关互动（device talk 等，Chiong 2012）；纸书条件下 off-task 更多（Richter & Courage 2017）；作者以认知负荷解释 point/click/swipe 与叙事加工竞争。
   - 页码: PDF pp.2, 5, 25；暂定 verdict: `PARTIAL`（元分析内部引用的二手行为证据，无效应量；行为研究被纳入标准排除）；scope: 幼儿共读/听读，行为→我们作答 UI 为 `PROJECT-INFERENCE`。
5. **UIE-35（Class 4, 草稿，儿童 vs 成人段差异）**: 儿童段媒介效应方向与成人段不一致——成人元分析（Clinton 2019; Delgado 2018）整体 paper advantage 且 nonfiction 屏劣势；儿童段 SC 聚合 null、VOC 偏数字书且 nonfiction 更偏数字（k = 6, g = 0.42 [0.23, 0.61]，Q(1) = 7.87, p = .005），与 Delgado 2018 方向相反。
   - 页码: PDF pp.2, 20, 22–23；暂定 verdict: `SUPPORTED`（作者自报的比较）；scope: 跨段不可合并——任何把儿童段效应外推到成人段（或反之）的断言属 `OVERSTATED`。

## 数据质量注记（引用本元分析数字前必读）

- VOC 正文 n 报告不一致：881 vs 557+488=1,045（PDF p.20）。
- 正文与表的小口径差：SC 总体 CI 下限 −0.17（正文 PDF p.16）vs −0.18（Table 2 PDF p.19）；VOC 总体 g = 0.20 [0.08, 0.32]（正文 PDF p.20）vs 0.22 [0.09, 0.35]（Table 3 PDF p.23）；SC "minimal additions" 子组 k = 10（正文 PDF p.17）vs "No enhancements" k = 11（Table 2 PDF p.19）。
- 复用数字须回到原文/原始研究核验；对审计而言采用保守口径（正文句 + 对应表值并存标注）。
