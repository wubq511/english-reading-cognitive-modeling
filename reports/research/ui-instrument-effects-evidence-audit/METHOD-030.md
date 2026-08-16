# METHOD-030 全文证据提取笔记

## 结论速览（中文）

- 挪威 2015 年 10 岁儿童（5 年级）纸面 vs 屏幕阅读理解被试内大样本实验（n=1139，IRT 2PL+PCM 建模）：**数字模式（CBA）平均成绩显著低于纸面（PBA），p<0.05**；30.5% 学生 PBA 高约 1 分 vs 13.6% CBA 高约 1 分。
- **投递模式效应随 latent 能力增大而增大**（方向性假设 H2 被数据拒绝）：Q1 d=0.31、Q2&3 d=0.41、Q4 d=0.44，三个能力层均显著。
- **性别×模式交互**：H3（男孩对 CBA 更免疫）被拒绝；最高能力组（Q4）女孩效应最大 **d=0.53**（Q4 男孩 d=0.33），Q4 内 CBA 男女差异 t=2.16。
- **产品级缺失也模式依赖**：CBA 测试末尾缺失明显更多；作者把「末尾连续 5 个响应的缺失」按 null-response（未接触）而非错误计分——缺失的 IRT 处理决策直接改变 estimand。
- 与审计既有 `METHOD-012`（ACT）方向相反（ACT online>paper，本文 paper>CBA）：投递模式效应方向不可先验假定。
- 本文**明确未做可用性测试**（"We did not conduct a usability test"，PDF p.5），Class 1 无直接实证贡献。

---

## 头部信息

- **source ID**: `METHOD-030`
- **本地路径**: `sources/library/papers/methods/2020_Stole_PaperVsScreen.pdf`（SHA-256 与 `sources/catalog.yaml` 一致，预检 `scripts/bootstrap` sources doctor OK）
- **完整书目**: Støle, H. (Hildegunn), Mangen, A., & Schwippert, K. (2020). *Assessing children's reading comprehension on paper and screen: A mode-effect study*. Computers & Education 151, 103861. DOI: 10.1016/j.compedu.2020.103861. CC BY 4.0（© 2020 The Author(s); Elsevier）.
- **catalog 核对不符处（不改 catalog，仅标注）**: `sources/catalog.yaml` 条目作者写作 `["Heidi Støle", ...]`，但 PDF 首页与 Author contribution statement 均为 **"Hildegunn Støle"**（PDF p.1, p.11）。其余字段（标题、年份、venue、DOI、license、路径）与 PDF 一致。

---

## 研究概览

### 研究问题与假设
- 目的（双重）：为 2016 年挪威首次数字化的全国阅读测验（NRT）验证数字模式的效度与信度（不改变纸面测验已用了十年的阅读构念），同时实证检验模式效应是否存在于 10 岁儿童（PDF p.4, §1.5）。
- 三个假设（PDF p.4, §1.5）：
  - **H1**: PBA 条件平均成绩优于 CBA（模式效应存在）。
  - **H2**: 模式效应与阅读能力相关——低成就者比高成就者受模式影响更大（预期方向：弱势读者吃亏更多）。
  - **H3**: 模式效应与性别相关——男孩的模式效应比女孩小。

### 样本
- n=1139 匹配样本（同一学生两种模式各测一次）；性别分析 n=1133（6 人性别不明）。原始响应：纸面 1461、数字 1538，清理匹配后为 1139（PDF p.5–6）。
- 挪威 5 年级（约 10 岁），2015 年秋；由教育部按学校规模、城乡、地区分层抽样，全国 5 年级约 61,000 人（PDF p.4–5, §2.1）。
- 功效：匹配对样本，检测 d=0.2 效应时 power=1−β=0.999，α=0.05 双侧（PDF p.6, §2.2）。

### 设计
- **被试内（within-subjects）对照实验**，两组 A/B 卷 × 纸/屏媒介，版本与媒介次序 counterbalanced；班级内由教师随机分配条件（cluster-randomized assignment），连续两周各测一卷（PDF p.5, §2.1）。
- 属实验（experimental）而非准实验：随机分配在班级内进行；但注意分配单位是班级成员（cluster-randomized），不是完全个体随机。

### 任务与材料
- 每卷 5 篇文本（共 10 篇），A 卷 36 题、B 卷 35 题；文本长度 204–683 词；体裁从线性叙事到含表格/插图的多模态信息文本；题型 MC（单选四选一）+ CR（构答反应，人工按评分指南计分，拼写不算错）（PDF p.3–5, §1.4/§2.1）。
- 限时：每卷 90 分钟，CBA 最多再加 5 分钟（教师讲解更长）（PDF p.5, §2.1）。
- 设备：标准电脑屏幕（约 20 英寸）、鼠标点选 MC、键盘输入 CR；无平板（PDF p.5, §2.1）。

### 关键 UI/仪器差异（纸 vs 屏，均在实验内存在）
- 纸卷 A4 小册子、双页布局；CBA 多模态文本需滚动（滚动量与表格/插图数量相关，而非词数）（PDF p.5）。
- 题目呈现位置：PBA 常需翻页看题；CBA 题目在左侧，学生滚动/读完文本后出现；题多时也需滚动（PDF p.5）。
- 两种模式都允许在文本与题目间前后移动、允许修改答案；**CBA 额外在提交前提示未答题**（PBA 无此反馈）（PDF p.5）。

### 变量
- **产品分数（estimand）**：IRT（2PL + partial credit model）分别拟合两卷，logit 分数线性化为 M=50、SD=10 量表（Xcalibre 4.2），同一学生获得 PBA 与 CBA 两个可比分数（PDF p.5–6, §2.2）。
- **过程指标**：本研究未报告行为 logging 分析；唯一报告的过程层面指标是**缺失响应**（CBA 末尾缺失更多，PDF p.9）。
- **缺失/信度指标**：双人评分纸卷 + 随机 10% 复查 inter-scorer reliability（PDF p.5）；题目层 bias（DIF）筛查（PDF p.6）；item fit 筛查（PDF p.6）。

---

## 核心发现（按四类主张分组）

### Class 4 — 学习/构念与 estimand（本研究的主战场）

**F4-1. 投递模式移动产品分数分布：CBA 平均显著更低（H1 支持）。**
- 摘要与正文："Results showed that the students in average achieved lower scores on the digital test than on the paper version"（PDF p.1）；"The digital reading test was significantly (p < 0.05) more difficult than the paper-and-pencil test"（PDF p.6, §3.1）。
- 个体分布：53% 学生两模式成绩相同/接近（|差|≤0.5 SD，n=599）；30.5%（n=373）PBA 高约 1 分；13.6%（n=167）CBA 高约 1 分；38 名学生差异 >2 SD（PDF p.6, §3.1；Fig. 1 见 PDF p.7）。
- 判定：`SUPPORTED`（在其研究范围内）。这是 mode-level（纸 vs 屏整体投递）的直接主要证据，非 within-mode UI variant 对照。

**F4-2. 模式效应与 latent 能力交互，且方向与作者的 H2 预期相反：高能力者受数字模式损害最大。**
- "the effect size is most pronounced for students in the Q4 group, i.e. the highest reading achievement group, at Cohen's d = 0.44. The effect size reaches d = 0.41 for the middle range students, while it is smallest for students who only reach Q1"（PDF p.6, §3.2）；Table 1 给出 Q1 d=0.31、Q2&3 d=0.41、Q4 d=0.44（PDF p.8, Table 1）。
- 三个能力层 PBA 优势均显著："significant at the p < 0.05 level for all three skills levels (Q1; Q2 & Q3; Q4)"（PDF p.6, §3.2）。
- 对 H2 的否定表述："In sum, we did not find support for the second hypothesis in our data. It emerged that students at all skills levels performed significantly better on PBA than on CBA ... with an increasing mode effect ... for higher achieving students"（PDF p.7, §3.2）。
- 判定：`SUPPORTED`。**审计含义：投递/UI 层变体对分数的影响不是常数——它随 latent 能力变化，即改变的是分数-能力关系的形状（interaction），不是单纯平移**；对 DIF/等值有直接含义。

**F4-3. 性别×模式交互：H3 被拒绝（男孩并未对 CBA 免疫），最高能力组女孩受损最大。**
- "we find no support for hypothesis 3 that boys perform better on CBA"（PDF p.7, §3.3）。
- "Top-performing girls especially, experience a significant mode effect, with an effect size of d = 0.53"（PDF p.7, §3.3）；Table 3（男孩）：Q1 d=0.26、Q2&3 d=0.41、Q4 d=0.33；Table 4（女孩）：Q1 d=0.40、Q2&3 d=0.43、Q4 d=0.53（PDF p.8–9, Tables 3–4）。
- Q4 组内 CBA 男女差异显著：男孩 62.29 vs 女孩 60.75，t=2.16（PDF p.7, §3.3 / Table 2, PDF p.8）。
- 作者对性别结果的限定：挪威 5 年级测试本身被设计为减少性别差异（选男孩感兴趣的文本、更多 MC 题），故性别相关结果可能不普适（PDF p.11, §6 Limitations）。
- 判定：`SUPPORTED`（本研究范围内）；跨测试外推受限（见边界与局限）。

**F4-4. 作者归因（推测性，非实测）：滚动与数字浅读习惯是主要机制，高阶阅读受损更重。**
- "Scrolling and/or misplaced digital reading habits may be salient factors behind this difference"（PDF p.1, 摘要）。
- "reading from paper may be more efficient than reading from screens when reading is not self-paced"（PDF p.9, §4，引 Ackerman & Lauterman 2012）。
- "our study supports this suggestion [Kerr & Symons 2006：推断理解等高阶过程受电脑阅读影响更大]，since we found that top-performing students ... are the ones who were most disadvantaged in the CBA mode"（PDF p.9, §4）。
- 判定：机制归因为 `PROJECT-INFERENCE`（作者自己用 "may"/"could" 措辞，未实测滚动量或阅读策略）；效应本身（F4-1/2/3）为 `SUPPORTED`。

### Class 3 — 仪器信度与缺失

**F3-1. 产品级缺失模式依赖：CBA 末尾缺失明显更多。**
- "There were noticeably more missing responses towards the end of the CBA compared to the PBA test"（PDF p.9, §4）。
- 判定：`SUPPORTED`。与 `METHOD-012`/UIE-27（ACT：paper 11.1% vs online 8.3% 有 ≥1 题缺失）同层但方向相反（本文 CBA 末尾缺失更多）——缺失方向同样不可先验假定，且本文语境是**限时速度化测试**。

**F3-2. 缺失的 IRT 处理决策改变 estimand。**
- "missing were treated as null-responses when occurring as a string of the five last responses and not as faulty responses. This means that only given responses (and random missing responses) were scored for calculations of student achievement"（PDF p.9, §4）。
- 判定：`SUPPORTED`（作为研究操作事实）。**审计含义：末尾连续缺失（限时导致未接触）与随机缺失的区分方式直接改变分数估计；这是仪器契约必须记录的打分规则。**

**F3-3. 技术性缺失与保守清理策略。**
- 题目层 bias（DIF）预分析发现部分题目对数字模式显著不利（p<0.05）；教师/学生反馈 CBA 存在 .jpg 插图未成功下载的技术问题，作者排除所有相关插图题以确保无偏（"to be on the safe (unbiased) side, we excluded from the mode effect analyses all items related to illustrations"）（PDF p.6, §2.2）。
- 重复考试数据全部剔除（同一学生考了两次同一卷）；只保留两种模式都参加的学生（1461+1538 → n=1139）（PDF p.6, §2.2）。
- item fit 筛查：判别度 rbis < 0.300 的题剔除（PDF p.6, §2.2）。
- 纸卷双人评分，随机 10% 复查 inter-scorer reliability（PDF p.5, §2.1）。
- 判定：`SUPPORTED`（作为研究操作记录）。`METHOD-030` 展示了大型测试对缺失/题目偏倚/重复数据的三重清理门禁，且这些门禁本身改变样本与题目池——与 UIE-12（`B7` 的清理操作）同型。

### Class 2 — 行为改变

**F2-1. 布局差异改变任务的行为空间（设计层面的事实）。**
- PBA 双页布局 vs CBA 滚动；题目出现位置（PBA 翻页 vs CBA 左侧）；CBA 提交前未答题提示（PBA 无）（PDF p.5, §2.1）。滚动量由多模态特征数量决定而非词数（PDF p.5）。
- 判定：`SUPPORTED`（作为实验条件的事实描述）。本研究**未报告行为 logging 数据**（除缺失外），因此这些差异对行为的实际影响是设计推论，非实测。

**F2-2. 定性用户测试：儿童把纸面触觉阅读策略（用手指描行）带到屏幕上。**
- 前期定性用户测试（Mangen & Støle, n.p.）观察到儿童用手指在电脑屏幕上描行（"we observed a number of children tracing text lines with a finger on their pc screens"），作者认为该策略转移到屏幕可能减慢阅读（PDF p.9, §4）。
- 引证：Margolin et al. (2013)：43% 大学生在电脑上用手指描行、53% 在纸上（PDF p.9, §4）。
- 判定：`SUPPORTED` 作为引用事实；`PROJECT-INFERENCE` 作为机制（"it likely slows down reading" 为推测）。

**F2-3. 滚动损害空间定位/增加认知负荷——作者推测性归因。**
- "It has been suggested that scrolling disrupts the reader's ... sense of text structure and spatial location of information ... Scrolling is likely to draw on the limited working memory capacity"（PDF p.9, §4，引 Sanchez & Wiley 2009、Chen & Lin 2016 等）。
- 判定：`PROJECT-INFERENCE`——作者用 "may have introduced an additional challenge" 等措辞，未直接测量滚动行为。

### Class 1 — 可用性/偏好

**F1-1. 本研究明确未做可用性测试。**
- "We did not conduct a usability test, because the digital platform had already been employed for assessments of mathematics and English"（PDF p.5, §2.1）。
- 采用「低门槛数字方案」（"we aimed at a low-threshold digital solution that all students would likely handle without difficulty"）（PDF p.5, §2.1）。
- 判定：无 Class 1 实证。`METHOD-030` 不改变审计 Class 1 的 `UNRESOLVED` 状态。

**F1-2. 二手引用：偏好-表现分离存在于儿童（非本研究直接数据）。**
- 讨论中引用 Golan et al. (2018) 与 Halamish & Elbaz (2019)：儿童偏好屏幕但纸面表现更好，且大多无元认知意识（PDF p.9, §4）。属文献综述引用，未在本文本地复验。
- 判定：不采用为本地证据；仅作背景。

---

## 边界与局限

- **作者自声明局限（§6, PDF p.11）**：
  1. "results may in part depend on the selected digital solution. Digital technologies and test delivery platforms change"——建议在平板/手机上复刻；但同时认为低门槛方案下显著的模式差异难以用平台特性解释，更可能源于滚动与浅读策略（PDF p.11）。
  2. 挪威 5 年级测试为减少性别差异而选文本与题目（男孩兴趣文本、更多 MC），类似儿童模式效应研究可能得到不同的性别结果（PDF p.11）。
- **人群/任务边界**：10 岁儿童、挪威、2015 年；文本较短（204–683 词）且多模态；限时 90 分钟（速度化，非自定步调）；仅电脑（约 20 英寸）、鼠标+键盘，无平板。
- **工具边界**：无行为 logging 数据（除缺失外）；滚动量/阅读策略均为推测归因；无可用性测量；IRT 清理策略（DIF 排除、item fit 门禁、只保留双模式参与者）本身影响可推广性。
- **不可外推处（对项目）**：本研究是纸 vs 屏的**投递模式对照（mode-level）**，不是作答 UI 内 variant 对照；其滚动设计（整篇滚动、题目左侧）与本项目冻结的「左 passage 独立滚动 + 右侧逐题」布局不同；儿童被试 vs 项目可能的成人/学生受众不同；d 值（0.31–0.53）不应直接作为项目 UI 变体效应量的先验——但「投递层变体移动分数分布且方向不可先验」这一结构性结论可迁移。
- **负面/反向证据**：13.6% 学生在 CBA 反而更高（PDF p.6）；作者对 H2/H3 的方向性预期双双被数据拒绝（PDF p.7）——提示模式效应方向与交互模式不可凭常识假定。

---

## 对审计的用途

### 与审计主文件的衔接
- 审计主文件 Limitations 明确把本篇列为 metadata-level screened（"the Norway children's mode-effect experiment 2020 ... were screened at title/abstract/metadata level only ... their conclusions ... must not be asserted in either direction until acquired"）。本笔记将其升级为**全文钉页证据**。
- 审计主文件正文未直接引用 `METHOD-030`（grep 确认：仅在 `SOURCE_REPORT_CROSSWALK.md`、`catalog.yaml`、`human-tasks/wayfinder-5-ui-instrument-effects.md` 出现）。因此以下为新条目建议，编号待审计主文件 owner 分配。

### 对既有条目的支持/限定
- **强化 `UIE-27`（`METHOD-012`，ACT）**：`METHOD-030` 是投递模式移动阅读分数分布的第二份本地主要证据，且为儿童被试内 IRT 设计。**方向相反**（ACT online>paper，d=.16–.22；本文 paper>CBA，d=0.31–0.53 按子组）——两条合并后得出更稳的结构结论：投递模式效应大小与方向都不可先验，必须在本仪器上实测。
- **支撑 `UIE-26`（`METHOD-011` TME 综述）**：为综述的 TME 威胁提供一篇原始主要证据（含题目层 DIF 排除、缺失模式、速度化）。
- **支撑 `UIE-18`（`STANDARD-001` 公平性框架）**：实证示例——同一仪器（CBA）对 Q4 女孩（d=0.53）与 Q1 男孩（d=0.26）的分数影响系统性不同，是构念无关方差异质性伤害的实例。
- **与 `UIE-11`/`UIE-27` 并列补充 Class 3**：产品级缺失（非仅过程通道缺失）模式依赖，加上缺失的 IRT 处理决策（null-response vs faulty）直接改变 estimand。
- **不改变**：审计 Class 4 的缺口声明（"no locally held source demonstrates that a *specific variant change in a reading MC answer UI* changes the measured construct or the estimand"）——`METHOD-030` 是 mode-level，不填补 within-mode variant 缺口，但强化了「仪器变化 ⇒ estimand 变化」前提（决策含义 1）。

### 建议的新 UIE 条目草稿

1. **UIE-31（建议）**：投递模式（纸 vs 屏）在被试内设计中移动儿童阅读产品分数分布：CBA 平均显著更低（p<0.05）；30.5% 学生 PBA 高约 1 分 vs 13.6% CBA 高约 1 分、53% 相当；个体差异呈厚尾（38 人差 >2 SD）。
   - Pages: PDF pp.1, 6–7（Fig. 1）
   - 暂定 verdict: `SUPPORTED`（研究范围内）；mode-level，非 within-mode variant
   - Scope boundary: 挪威 10 岁儿童、2015、限时 90 分钟、20 英寸电脑、多模态文本、A/B 卷 counterbalanced

2. **UIE-32（建议）**：模式效应与 latent 能力交互且方向反直觉——高能力组（Q4）效应最大（d=0.44），低能力组最小（d=0.31），三能力层均显著；作者的 H2 方向性假设被数据拒绝。投递/UI 层变体改变分数-能力关系形状（interaction）而非单纯平移。
   - Pages: PDF pp.6–7, 8（Table 1）
   - 暂定 verdict: `SUPPORTED`
   - Scope boundary: 同 UIE-31；对 DIF/等值有含义（该模式效应无法用单一平移参数描述）

3. **UIE-33（建议）**：性别×模式交互——最高能力组女孩受损最大（Q4 d=0.53 vs 男孩 0.33），Q4 内 CBA 男女差 t=2.16 显著；H3（男孩对 CBA 免疫）被拒绝。
   - Pages: PDF pp.7–9（Tables 2–4）
   - 暂定 verdict: `SUPPORTED`（本研究）；作者声明挪威测验设计旨在减少性别差异，跨测试外推受限
   - Scope boundary: 同 UIE-31 + 测验设计（男孩兴趣文本、MC 偏多）

4. **UIE-34（建议）**：产品级缺失模式依赖 + 缺失处理决策改变 estimand——CBA 末尾缺失明显更多；末尾连续 5 个响应的缺失按 null-response（未接触）而非错误计分。
   - Pages: PDF p.9
   - 暂定 verdict: `SUPPORTED`
   - Scope boundary: 限时速度化测试语境；与 `METHOD-012` 缺失方向相反（不可先验）；仪器契约必须记录该打分规则

5. **UIE-35（建议）**：投递布局差异改变任务行为空间（双页 vs 滚动、题目位置、未答题提示仅 CBA），滚动被推测损害空间定位/增加认知负荷——行为空间改变为事实，机制为推测。
   - Pages: PDF pp.5, 9
   - 暂定 verdict: `PARTIAL`（设计事实支持，机制为推测 → 机制部分 `PROJECT-INFERENCE`）
   - Scope boundary: 无行为 logging 实测；儿童触觉描行策略转移来自定性用户测试 + 二手引用（Margolin 2013）

### 对审计决策含义的增量
- 决策含义 1（仪器变化 ⇒ estimand 变化，冻结前必须测量）：`METHOD-030` 提供儿童大规模阅读测试中被试内实测——投递层变体移动分数分布（30.5% vs 13.6%），且与能力/性别交互（F4-2/3），效应量级超过 ACT 证据（d 至 0.53）。
- 决策含义 5（缺失政策）：补充产品级缺失的模式依赖证据 + null-response 规则先例，支持「缺失是设计依赖的默认状态」。
- 预 H2 声明预算：不改变——仍不允许跨模式/跨 variant 的构念等价声明。

---

## 提取纪律说明

- 全部负载发现经 `pdftotext -layout` 全文核对并钉物理页；无 `ABSTRACT-ONLY` 条目。
- 页码均为 PDF 物理页（本地文件共 13 页；封面无页脚，页脚 N 即物理页 N 末行，映射经 awk 页脚定位核对）。
- catalog 作者名不符（"Heidi Støle" vs PDF "Hildegunn Støle"）已标注，未修改 catalog。
- 未修改 `sources/catalog.yaml`、`checksums.sha256`、审计主文件或任何其他文件。
