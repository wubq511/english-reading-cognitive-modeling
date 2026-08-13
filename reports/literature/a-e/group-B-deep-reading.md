# Group B — English / Digital Reading Process Data

> 本文档为 B 组 11 篇论文（[B1]–[B11]）的深度阅读报告，回答核心问题：**英语/数字阅读中，可观测的页面交互行为究竟能够在多大程度上支持对 reading behavior、reading process、strategy、cognitive state 和 reading skill 的推断？**
>
> 报告遵循 A/A+ 组已建立的推断边界（Raw Event → Behavior → Process → Cognitive → Skill），B 组只提供阅读领域的证据，不重复比较测量算法（IRT/HMM/RL 等）。
>
> 生成日期：2026-08-12。全部页码引用均基于本地 PDF 文件逐页核对。

---

## 0. PDF Mapping

| 编号 | 论文 | 本地 PDF 文件 | 期刊/场合 | 证据等级 |
|---|---|---|---|---|
| B1 | Gamified Self-Regulated Learning Improves EFL Reading Comprehension, Motivation, Self-Regulation Skills and Process Patterns: Quasi-Experiment with Process Mining (Maimaiti & Hew, 2025) | `B_2025_Maimaiti_GamifiedSRL.pdf` | The Internet and Higher Education 67, 101042 | peer-reviewed journal |
| B2 | Clustering Sequential Navigation Patterns in Multiple-Source Reading Tasks with Dynamic Time Warping Method (He, Borgonovi & Suárez-Álvarez, 2023) | `B_2022_He_DTW_Navigation.pdf` | Journal of Computer Assisted Learning, 39(3), 719–736 | peer-reviewed journal |
| B3 | A Model of Online Reading Engagement: Linking Engagement, Navigation, and Performance in Digital Reading (Naumann, 2015) | `B_2015_Naumann_OnlineReadingEngagement.pdf` | Computers in Human Behavior 53, 263–277 | peer-reviewed journal |
| B4 | Using Sequence Mining to Explore Students' Behaviors in Digital Reading Assessments (Soyoye, 2023) | `B_2023_Soyoye_SequenceMining.pdf` | AERA 2023 年会论文（AERA Online Paper Repository, DOI 10.3102/2016968） | conference paper（按 §19 降权） |
| B5 | Indirect Effects of Strategy Knowledge and Comprehension Skills on Navigation and Performance in Digital Reading (Naumann, Pucite, Salmerón & Eichmann, 2020) | `B_2022_Naumann_StrategyKnowledge.pdf` | AERA 2020 年会圆桌报告（AERA Online Paper Repository, DOI 10.3102/1582511） | conference paper（按 §19 降权） |
| B6 | For Skilled Comprehenders Digital Reading Is a Routine Task, for Unskilled Comprehenders It Is a Problem (Naumann et al., 2025) | `B_2025_Naumann_SkilledComprehenders.pdf` | Learning and Individual Differences 122, 102745 | peer-reviewed journal |
| B7 | Leveraging Process Data to Investigate the Interplay Between Response Formats and Cognitive Processes in Digital Assessment and Learning Environments (Arslan et al., 2026) | `B_2026_Arslan_ResponseFormatsCognitiveProcesses.pdf` | Contemporary Educational Psychology 85, 102461 | peer-reviewed journal |
| B8 | Combining Cognitive Theory and Data Driven Approaches to Examine Students' Search Behaviors in Simulated Digital Environments (Tenison & Sparks, 2023) | `B_2023_Tenison_SearchBehaviorsSimulatedEnvironments.pdf` | Large-scale Assessments in Education 11:28 | peer-reviewed journal |
| B9 | Going Beyond Observable Actions: A Cognition-Centered Approach to Interpreting Pauses Represented in Process Data (Arslan, Tenison & Finn, 2023) | `B_2023_Arslan_InterpretingPausesProcessData.pdf` | European Journal of Psychological Assessment, 39(4), 263–270 | peer-reviewed journal（special issue） |
| B10 | Purpose Instructions and Task Models in Multiple-Text Reading (Lyu, Yao & McCrudden, 2026) | `B_2026_Lyu_PurposeInstructionsTaskModels.pdf` | Learning and Instruction 104, 102347 | peer-reviewed journal |
| B11 | Quantifying the Benefits of the Reread-Before-Answer Strategy in Japanese High-School EFL (Wijerathne, Flanagan & Ogata, 2025) | `B_2025_Wijerathne_RereadBeforeAnswer.pdf` | ICCE 2025 论文集（Asia-Pacific Society for Computers in Education） | conference proceedings（按 §19 降权） |

**编号说明**：
- 文件名中的年份不代表论文出版年份（如 `B_2022_He_DTW_Navigation.pdf` 实为 JCAL 2023 出版；`B_2022_Naumann_StrategyKnowledge.pdf` 为 AERA 2020 报告），编号完全依据论文标题匹配任务给定编号，11 篇全部在位，无 `B7 — PDF NOT FOUND`。
- 按任务 §19：[B4]、[B5]、[B11] 属于 conference / proceedings，证据等级低于 peer-reviewed journal；当与高等级期刊冲突时，以后者为主，但不因会议论文证据较弱而不分析。

---

## 1. Executive Findings

以下为 B 组跨 11 篇论文的最高层结论（详细证据见各章）。

1. **阅读领域存在足够的 Process/Strategy 理论基础，但「行为→认知」的证据强度严重分层。** 理论框架（MD-TRACE / RESOLV / IPS-I，见 [B6]/[B8]/[B10]；Guthrie 投入模型，见 [B3]）为解释行为序列提供了稳定概念框架（task model、goal formation、navigation、evaluation、monitoring），但把具体行为映射到这些概念的实证证据，多数只是 CORRELATIONAL 或 POST-HOC，只有 [B7]（反应格式实验）和 [B9]（ACT-R 认知建模）达到了「理论驱动的受控实验/论证」级别。

2. **「导航/访问/回读的量」没有独立认知意义，其含义由任务需求（access demands）决定。** [B3] 提供了最强证据：访问任务相关页面的次数对表现的预测强度，在高访问需求任务（β=0.51）远强于低访问需求任务（β=0.19）；[B2] 显示同一「多页导航」模式在不同学生身上对应不同表现与性别/SES 差异。**禁止「行为计数 → 认知标签」的粗暴映射。**

3. **revisit（回读/重访）在 B 组证据中是「正向预测正确率」的行为，但含义多重。** [B11] 直接证明「答题前回读循环（RBA）」在控制时间、序列长度、先前能力后仍显著预测更高正确率（OR≈1.28），且高能力组获益更大；但同一篇论文承认回读也可能代表困惑/分心。[B4] 对 look-back 给出互斥解释（struggle vs. confident）。[B3]/[B6] 证明回读「相关」页面对复杂任务有利、对简单任务只是多余动作。**单靠 revisit 序列无法区分「策略性回读 vs. 困难驱动的重复阅读 vs. 验证」——只能给概率证据。**

4. **pause 本身（纯停留时长）几乎没有认知意义；只有「带事件上下文的 pause」才有解释力。** [B9] 是该论断的直接理论来源：pause 的认知内容取决于前导/后继事件与任务 affordance；[B7] 用受控实验证明「信息检索 pause」（两次答题动作之间）与「终答检查 pause」（最后一次答题到提交之间）在反应格式间系统差异；[B8] 给出可用阈值（<250ms 动作准备、2.5–10/10–30/>30s）。**结论：Pause + Before-event + After-event + Task state + Location → Cognitive evidence，但其中多数为项目迁移推论而非论文结论。**

5. **理解技能（comprehension skill）是行为意义的关键调节变量。** [B5] 证明策略知识对数字阅读的作用被 navigation 完全中介，而理解技能对 navigation 的作用独立存在；[B6] 证明理解技能与问题解决技能对 navigation 呈「补偿性」交互——对低理解者，问题解决技能更能预测导航精确度；对高理解者，数字阅读是「常规任务」。**同一行为在不同能力学生身上含义不同（adaptive vs. inefficient），[B6] 的补偿性交互是可辩护证据。**

6. **task model（任务模型）是「题目预览/目标形成」的合法理论锚点，但需要直接测量。** [B10]（think-aloud）证明：同样的目的指令在不同学生身上产生不同 task model，而 task model 成分（写作目标、重读计划）而非指令本身预测阅读过程与学习结果；这为「question preview → goal formation」提供了理论支持，也警告「同一指令 ≠ 同一任务模型」。

7. **underline/highlight 与 option elimination 在 B 组论文中基本无证据。** 没有 B 组论文直接研究划线/高亮或划掉选项的认知含义（[B11] 的 BookRoll 记录了高亮事件但未分析；[B8] 的 annotation 计划只出现在 self-report 中且与 elaboration 负相关）。按任务 §6.9/§6.10 要求，明确标注 **UNSUPPORTED BY GROUP B**，系统不得把这两类行为直接当证据检索/相关判断使用。

8. **B 组自身无法把行为直接解释成阅读技能；A/A+ 提供「过程证据 → latent trait」的统计机制，两者之间的构念效度桥梁缺失。** B 组没有任何论文建立从过程行为到长期阅读技能的直接因果/强预测链路（全部是相关、群组差异、或过程作为中介变量的路径模型）；A/A+ 已证明 process sequence + effectiveness/skill mapping 可以在统计测量层估计 latent trait / 多维能力。**综合：B 组交付「行为 → 阅读过程证据」；A/A+ 交付「过程证据 → latent trait」的数学机制；但「过程证据 → 具体技能构念（information locating / inference 等）」的 construct-validity 桥梁仍未验证——这是 E 组的核心任务。** A+ 的 effectiveness（距离/概率/reward）在阅读中最可辩护的定义是 **B 路线（P(correct | 到达某状态)）+ 任务相关性的先验定义**，但必须直面 construct circularity。

9. **题型依赖性被证实。** [B7] 的核心发现是同一反应格式在不同任务类型（排序 vs. 分类）产生相反的过程指标差异；[B3] 的 access demands 交互；[B6] 讨论的任务透明度（搜索起点 vs. 明确书目）。**同一种 navigation/revisit 行为在不同题型下应有不同解释——这是 B 组的明确结论，不是推断。**

10. **B 组最重要的方法论交付**：[B9] 的三步法（理论认知建模 → 日志预处理 → 统计建模）+ [B8] 的事件粒度选择（低层事件折叠、pause 语境化）+ [B7] 的「为过程数据而设计」原则，为我们的系统提供了一条「Raw Event → Semantic Event」的可辩护路径。

---

## 2. B1 — Gamified Self-Regulated Learning Improves EFL Reading Comprehension, Motivation, Self-Regulation Skills and Process Patterns（Maimaiti & Hew, 2025）

**类型**：peer-reviewed journal（The Internet and Higher Education 67, 101042）。**编号映射**：`B_2025_Maimaiti_GamifiedSRL.pdf`。

### 5.1 Research Question
RQ1–RQ4：游戏化 SRL 方法对（1）英语阅读表现、（2）动机、（3）自陈 SRL 技能、（4）SRL 策略频率与**序列**的影响。它研究的是 SRL 行为模式（process mining）与学习结果的关系，**不是阅读过程本身**——reading 只作为被测的学业结果，不作为被记录的交互行为对象。

### 5.2 Reading Task
EFL 翻转课堂（flipped classroom）学习环境。阅读任务 = 课前材料（视频+quiz）、课上练习、4 个**可选**阅读任务（每任务含基于一篇 passage 的阅读理解题与策略训练题）+ CET-4 阅读子测试作为前后测（两篇各 ~350 词，各 5 道选择题）。
- **single/multiple-text**：single-text（每任务一篇 passage + MCQ）；EFL；learning（非 assessment）；closed environment（学习平台）。
- **与「左 Passage + 右题目」相似度：LOW**。原因是被记录的交互全部是平台级 SRL 动作（目标设定、监控、求助、自评），阅读 passage 内的滚动/划线/答题过程本身没有被细粒度记录；reading 只是完成任务的载体。

### 5.3 Participants
177 名一年级本科生（软件工程专业），18–20 岁，中国某公立大学，College English 课程；整班分配为实验组（n=91，游戏化）与对照组（n=86）。准实验设计。

### 5.4 Raw Process Data
- **Raw log**：学习平台 trace data —— 点击、页面访问、任务耗时、材料访问、作业提交（p.3）；具体编码为 16 个 trace 指标（Table 2, p.8：目标设定 3 项、监控 3 项、认知策略 3 项、求助 3 项、自评 4 项）：提交目标/计划、查看目标、查看课程要求、查看学习任务、查看完成进度、标记任务完成、提交作业、学习课程材料、重新提交、访问 Q&A 论坛、查看 FAQ、给老师发私信、提交自评、查看已交任务、查看 SRL 仪表盘、查看推荐材料等。
- **Derived feature**：各 SRL 策略聚合频率；FOMM 转移概率；可选任务完成率。
- **注意**：无阅读 passage 内的低层事件（无 scroll/选择/停留于正文的日志）。Time 数据存在但未作为分析变量。

### 5.5 Event Granularity
单一平台动作（点击/页面访问/提交），属**粗粒度语义事件**；不是鼠标/滚动级。论文未讨论粒度改变认知解释的问题。

### 5.6 Preprocessing
- 策略操作化：基于 Barnard et al. (2009) 编码方案，每策略 3–4 个 trace 指标（Table 2, p.8）。
- 排除游戏化专属 trace 指标以保证组间可比。
- FOMM 转移概率 <0.01 的边被剔除（p.10）。

### 5.7 Behavioral Indicators
- 各 trace 指标频率（计数）、SRL 策略聚合频率、FOMM 转移概率（TP）、可选任务完成率。
- 无 dwell/pause 分析；无阈值说明（论文未给，不补）。

### 5.8 Behavioral Pattern / Strategy
First-Order Markov Model（FOMM，pMineR 包）→ 转移概率热力图（Fig. 6/7）。**策略类别是理论先定的**（Barnard 编码把行为映射到 goal-setting/monitoring/cognitive/help-seeking/self-evaluation），转移结构是数据挖出的；对「哪个行为是中心、哪些转移强」的解释是**研究者事后解释**。

### 5.9 Cognitive Interpretation
将行为解释为 SRL 策略：查看仪表盘→评估/反思性过程；查看推荐材料→主动补救；给老师发私信→主动求助。证据类型：**THEORY-BASED**（行为按 SRL 理论编码）+ **POST-HOC**（FOMM 模式解释）。无 think-aloud。

### 5.10 Reading Skill
阅读成绩（CET-4 子测试）作为结果变量：实验组校正均值 87.37 vs 对照组 68.60，F=72.52，p<.001，η²=0.29（Table 3, p.9）。**但没有建立具体行为 → 阅读成绩的关系**——行为与阅读成绩的关联是推断性的（更多 SRL → 更多学习 → 更好成绩），无中介/回归证据。

### 5.11 Individual Differences
未考察（仅组间比较）。

### 5.12 Task Dependence
未考察。

### 5.13 Temporal Evidence
只有「任务耗时」被记录（p.3），未分析。FOMM 编码顺序但不编码时间。无 pause/dwell 证据。

### 5.14 Ground Truth / Validation
- 自陈 OSLQ（5 维度，α=0.95 整体）与 trace 频率分析**汇合验证**（p.8–10）：自陈与行为一致 → 行为频率有一定 behavioral validity。
- Predictive validity：游戏化组更好阅读成绩。
- 无 cognitive construct validity（无 think-aloud / 实验操控）。

### 5.15 Main Findings
- 阅读成绩：η²=0.29（Table 3）。
- 动机（内在价值）：F=22.87，η²=0.12；可选任务完成率 EG 全部显著更高（96.7 vs 75.6、92.1 vs 61.6、89.0 vs 61.6、72.5 vs 53.5，Holm-Bonferroni 校正后显著）。
- SRL 自陈全部 5 维显著（η² 0.06–0.11）。
- SRL 行为频率全部 5 策略显著（r=0.18–0.65；self-evaluation r=0.65）。
- FOMM：对照组以「查看学习任务」为中心（监控导向、任务提交驱动）；实验组以「查看 SRL 仪表盘」为中心，强转移到「查看推荐材料」（TP=0.695），评估性策略更活跃。

### 5.16 Limitations
- **Paper-stated**：准实验/整班分组限制因果与推广；规则式推荐不够自适应；特定中国 EFL 翻转课堂情境。
- **Transfer limitations**：process data 是平台 SRL 行为而非阅读过程；对我们的「passage+题目交互」推断几乎没有直接贡献。价值在于：证明 **trace 频率 vs 自陈汇合验证**是行为指标的一个可辩护验证方式，以及 FOMM 作为行为序列可视化/建模的可用工具。

---

## 3. B2 — Clustering Sequential Navigation Patterns in Multiple-Source Reading Tasks with Dynamic Time Warping Method（He, Borgonovi & Suárez-Álvarez, 2023）

**类型**：peer-reviewed journal（JCAL 39(3), 719–736）。**编号映射**：`B_2022_He_DTW_Navigation.pdf`（文件名年份 2022，论文出版 2023）。

### 5.1 Research Question
三个 RQ：（1）数据驱动识别学生在多源阅读任务中的代表性导航模式（页面转移 + 每页停留时间序列）；（2）导航模式与阅读能力的关系；（3）导航模式与性别、SES 的系统差异。它研究 **navigation 行为模式 → performance / 背景变量** 的关系，把 navigation 视为「mapping students' navigation strategies through the traces」（p.720），但不直接声称测量认知状态。

### 5.2 Reading Task
PISA 2018 单一题项 CR551Q11（"Rapa Nui" 单元最后一题）。多源文本环境：博客页、书评页、科学新闻页三个来源；需检测并处理冲突信息，整合三源作答（开放题，人工评分，Level 4 中高难度）。assessment、closed environment、multiple-source hypertext。
- **与「左 Passage + 右题目」相似度：MEDIUM**。页面转移（tab 切换）与每页停留时间的概念可直接映射到我们的「段落/区域重访」与「停留」；但我们的 passage 是单一滚动文档而非多页 tab，导航 affordance 不同。

### 5.3 Participants
16,957 名 15 岁学生，69 国，PISA 2018（对 Rapa Nui 单元至少做了一次导航的学生子样本）。平均阅读分 579（比全样本高 62 分——**样本偏向高能力**）；56.1% 女生；ESCS 平均 0.245。66.3% 被分配该单元的学生无任何导航行为被排除。

### 5.4 Raw Process Data
- **Raw log**：页面访问/转移事件 + 时间戳（谁在什么时间访问了哪个页面）。
- **Derived feature**：页面序列 P_i=(p1..pn)（按访问顺序的页面编码序列，页面编码为数字）；时间序列 T_i=(t1..tn)（每页停留时长）；DTW 距离矩阵；k-medoid 聚类成员；联合簇成员（4×4=16）。

### 5.5 Event Granularity
事件 = **一次页面转移（tab 点击）**；序列单元 = 一次访问的页面。论文讨论序列长度必须足够长才能识别模式（因此只分析最后一题，平均 2.88 页转移）；**未讨论粒度改变认知解释**。但明确承认：时间序列聚类无法把「阅读、重读、暂停、略读」区分开（见 5.13）。

### 5.6 Preprocessing
- 排除无导航学生（导航长度为 0，无法计算相似度）。
- 页面编码为有序数字（Blog/Book Review/Science News 各自编号，p.3-4 §2.5）。
- DTW 两两距离矩阵（页面序列 + 时间序列分别）。
- k-medoid 聚类，k=2..10，Silhouette 选 k=4（页面序列 S=0.6219；时间序列 S=0.4235）。
- 联合簇 4×4=16。

### 5.7 Behavioral Indicators
导航序列（页面顺序）、每页停留时长、序列长度、revisit（嵌在序列中）、簇质心序列。无 dwell 阈值（停留时长连续）。

### 5.8 Behavioral Pattern / Strategy
**DTW 距离 + k-medoid 聚类——纯数据驱动发现模式**；模式命名（P1 单页书评导航、P2 多页+revisit、T1 skimming、T2 rush reading、T3 深读转移页、T4 短时）是**研究者事后解释**。论文明确用「might reflect」「possible indicator」等措辞（p.729）。

### 5.9 Cognitive Interpretation
- 访问全部页 + 更多停留时间 → 「focused reading / 无 rush transition」；只访问 1 页 + 极短时间 → 「less focused navigation / inefficient」。
- 时间簇 T2（主页 80s、转移页 20s）→ 「possible indicator of rush reading or quick skimming」。
- 证据类型：**CORRELATIONAL**（导航簇 ↔ 阅读分）+ **POST-HOC/THEORY-BASED**（认知标签为研究者推断）。

### 5.10 Reading Skill
- 页面模式：ANOVA F(3,16953)=63.267, p<.001（显著）；时间模式：F(3,16953)=147.706, p<.001（显著）。
- **η² 数值可靠性注记**：论文报告页面 η²=0.11、时间 η²=0.25（"解释 11%/25% 方差"），但按论文自身的 F 与 df 反算（η²=F·df₁/(F·df₁+df₂)）分别约仅 0.011 / 0.025（即约 1.1% / 2.5%）。该 η² 数值疑为原论文排版/计算错误（ESCS 部分亦存在类似不一致）。**本报告不再采信 0.11/0.25 或"11%/25% 方差"**，只保留：ANOVA 显著、cluster 平均成绩差异、PT43 与 PT14 约 55 分差、导航模式与表现存在关联。
- P2（多页导航）最高 599 vs P1（单页）最低 574；T3（转移页长时阅读）最高 598 vs T4（短时）最低 564；联合 PT43（长序列+长转移页时间）最高 612 vs PT14（单页+短时）最低 557，差距 55 分。
- 全部为**相关**（ANOVA 群组差异），无因果。

### 5.11 Individual Differences
- **性别**：女生更可能在 T3（更长阅读时间），男生更可能在 T4（更短时间）；同一导航模式 PT24/PT41/PT42/PT44 中女生得分高 20+ 分；PT22/PT43 中男生更高。→ **同一行为模式在不同性别学生身上对应不同成绩**。
- **SES**：弱势学生更多使用有限导航 + 短阅读时间（PT14/PT44 ESCS 最低）；PT43 的 ESCS 最高。
- 论文解释：同一模式可能是「efficient reading」（女生）或「aimless quick switching」（男生，p.731）。

### 5.12 Task Dependence
部分涉及：任务要求整合三源信息 → 导航多源是必要的；同时指出 UI 布局影响页面选择（book review tab 距 homepage 更近 → P1 学生「conveniently choosing an adjacent page」，p.728–729）。→ **导航选择受界面 affordance 与任务需求共同影响**。

### 5.13 Temporal Evidence
时间序列是核心：T1（主页 ~25s、第 2 页 2s 略读、第 3 页 ~80s）、T2（主页 ~80s、转移页 ~20s，疑似 rush/skim）、T3（主页 ~20s、转移页 ~160s，总时间最长）、T4（主页 ~10s、转移页 ~50s，总时间最短）。时间聚类与阅读分 ANOVA 显著（η² 数值不可靠，见 5.10 注记）。**局限中明确承认**：单靠时间序列无法区分阅读/重读/暂停/略读（p.733 limitation 3）。

### 5.14 Ground Truth / Validation
- Predictive validity：导航模式预测阅读分（ANOVA）。
- Behavioral validity：聚类稳定（Silhouette）。
- 无 cognitive construct validity（无 think-aloud）。作者在讨论中把「把策略映射到认知理论」列为未来工作（p.733）。

### 5.15 Main Findings
如 5.10 所示：页面与时间聚类 ANOVA 均显著（η² 数值不可靠，见 5.10 注记）；PT43 vs PT14 差 55 分；性别与 SES 差异显著。

### 5.16 Limitations
- **Paper-stated**：单一题项；只有 3 页不够丰富；页面序列与时间序列分开聚类，无法把时间归属到具体转移；未做跨国建模；样本偏向高能力（排除了 66.3% 无导航学生）；item 非响应率 31%。
- **Transfer limitations**：我们的界面是单一 passage，页面转移要映射到段落/区域转移；tab 邻近性混淆映射为 UI 布局效应；「只访问相邻页」在我们的滚动界面中可能没有对应物。

---

## 4. B3 — A Model of Online Reading Engagement: Linking Engagement, Navigation, and Performance in Digital Reading（Naumann, 2015）

**类型**：peer-reviewed journal（Computers in Human Behavior 53, 263–277）。**编号映射**：`B_2015_Naumann_OnlineReadingEngagement.pdf`。

### 5.1 Research Question
检验「在线阅读投入模型」的两个关键路径：（1）长期在线阅读习惯（信息型 vs 社交型投入）→ task-adaptive navigation；（2）task-adaptive navigation → 数字阅读表现（在印刷阅读技能之上）。它研究 **engagement（特质）→ navigation（过程）→ performance** 的关系，并特别关注**任务需求对导航行为意义的调节**。

### 5.2 Reading Task
PISA 2009 数字阅读测评（Digital Reading Assessment）。29 题、9 个单元，每题在模拟浏览器超文本环境中作答（博客、网站、邮件、论坛、搜索引擎结果页等）。任务间「access demands」（任务相关页面数量）不同（1–14 页）。assessment、closed environment、multi-page hypertext。
- **与「左 Passage + 右题目」相似度：MEDIUM-LOW**。界面差异大（多页超文本 vs 单 passage 滚动），但「访问任务相关页面的次数」若把「页面」替换为「相关段落/区域」，该指标与我们的系统高度同构；「access demands × 行为」的交互逻辑完全可迁移。

### 5.3 Participants
29,395 名 15 岁学生，17 国/经济体，PISA 2009。印刷阅读技能（PISA print reading WLE）同时测得。L1 为主。

### 5.4 Raw Process Data
- **Raw log**：学生在测试中的动作序列（clicks）被记录（p.268 §2.3）。
- **Derived feature**：access behavior = 访问任务相关页面的次数（含重访）；access demands = 每任务相关页面数（任务设计/专家编码，1–14）；information engagement（4 项问卷，WLE）；social engagement（5 项问卷，WLE）；print reading skill；ICT 可用性；SES。

### 5.5 Event Granularity
事件 = 页面访问（点击链接/tab）；分析单元 = **个体任务响应**（task-level），与模型的 task layer 对齐。论文说明这是大样本研究首次在任务级做行为→表现预测（p.265）。

### 5.6 Preprocessing
日志分析 → 页面访问计数；相关页面由专家按三类标准编码（必需信息/有帮助信息/导航必需，p.266 §2.2.1）；engagement 用 partial credit model 缩放（WLE，reliability .73/.56）。

### 5.7 Behavioral Indicators
access behavior（相关页访问次数含重访，无阈值）、access demands（相关页数）、info/social engagement（WLE）。**阈值：无**（论文未给，不补）。

### 5.8 Behavioral Pattern / Strategy
无序列挖掘——线性混合模型 + 交互项。「Task-adaptive navigation」= 访问行为与任务需求（access demands）的匹配度，通过交互效应统计推断。策略是**研究者定义**（task-adaptive vs not），非数据挖掘。

### 5.9 Cognitive Interpretation
- navigation = task engagement 的体现（Lawless & Schrader 的 navigation 隐喻，p.264）；访问/重访相关页 = 「information access behavior」，即选择/丢弃材料的判断过程；高需求任务中重访相关页 = 有效策略（多页信息难以同时记住，p.265）。
- feature explorers（被无关内容分心）理解更差（文献引用，p.264）。
- 证据类型：**CORRELATIONAL**（PISA 横断）+ **THEORY-BASED**（Guthrie 投入模型）；论文明确「prediction here does not imply causation」（p.265）。

### 5.10 Reading Skill
- H4/H5：印刷阅读技能 b=0.71（大效应），access behavior 在印刷技能之上预测数字阅读 b=0.35（Table 4）。
- H6：access behavior × access demands 交互 b=0.16；高需求任务中 access behavior→表现 b=0.51（9 国预测概率差 >.20，大效应）；低需求任务中 b=0.19（仍正，H6c 假设的负相关被否定）。
- **关键**：访问行为的含义随任务需求变化（moderation），且低需求任务中「多访问」仍与更好表现相关（p.275）。

### 5.11 Individual Differences
engagement 作为个体差异调节：高信息型投入者更 task-adaptive（与 access demands 正交互 b=0.17；高需求任务中 info engagement→access 正相关 b=0.25，低需求任务中**负相关** b=-0.09）——高信息投入者在简单任务中更节制；高社交型投入者在低需求任务中做得过多（b=0.04 正），但高需求任务中无负效应（H3b 被否定）。**即：个体习惯调节「行为→表现」的意义。**

### 5.12 Task Dependence
**核心发现**：access behavior 的意义高度依赖 access demands。高需求任务中多访问 = 全面覆盖（好）；低需求任务中多访问 = 不够 task-appropriate（虽仍正相关）。这是「同一行为、不同任务、不同含义」的最直接证据。

### 5.13 Temporal Evidence
无 dwell 分析（只有访问计数）。时间仅以总任务时长形式存在，未使用。

### 5.14 Ground Truth / Validation
- Predictive validity：access behavior → 任务级表现（GLMM，17 国一致）。
- Behavioral validity：效应跨 17 国 meta-analytic 一致（I² 各异）。
- 无 cognitive construct validity（无 think-aloud）；相关性明确。

### 5.15 Main Findings
- H1：access demands → access behavior b=3.16（大效应）：学生普遍把访问量调整到任务需求。
- H2a：info engagement × access demands 交互 b=0.17。
- H3a：social engagement × access demands 交互 b=-0.03（小，9/17 国显著）。
- H5：access behavior → 数字阅读 b=0.35（印刷技能之上）。
- H6a：access behavior × access demands → 表现 b=0.16。

### 5.16 Limitations
- **Paper-stated**：横断/相关，无因果；仅 15 岁；国家间差异未深究；engagement 测量有限（无用途信息）。
- **Transfer limitations**：「task-relevant pages」需要专家编码相关页面——我们的系统若用该指标，需定义「每题的 relevant paragraph/sentence」；access behavior 是页面级计数，非段落/区域级；我们的界面是单 passage 滚动而非多页。

---

## 5. B4 — Using Sequence Mining to Explore Students' Behaviors in Digital Reading Assessments（Soyoye, 2023）

**类型**：conference paper（AERA 2023，AERA Online Paper Repository, DOI 10.3102/2016968）。**编号映射**：`B_2023_Soyoye_SequenceMining.pdf`。按任务 §19 证据等级降权；conference 证据与期刊冲突时以后者为主。

### 5.1 Research Question
RQ1：学生在 NAEP 数字阅读测评中展示哪些导航序列？RQ2：阅读行为/导航模式是否与阅读成就相关？论文目的是理解数字阅读测评中的认知过程与策略（abstract）。

### 5.2 Reading Task
NAEP 2019 12 年级数字阅读块（11 道题）。平板作答，2 个 30 分钟块，分析其中一块。文章（Article1–3）+ 题项（item01–11）+ start/review 页，学生可在文章页与题目页间来回切换。
- **single-text**（每篇文章 + 题目）+ assessment。
- **与「左 Passage + 右题目」相似度：MEDIUM-HIGH**（文章与题目分屏/分页、可回看——look-back 模式与我们的 question→passage→question 切换高度同构）。注意：NAEP 数字阅读是文章/题目分页，不是同屏。

### 5.3 Participants
1,673 名美国 12 年级学生（原 1,833，剔除加时便利者），NAEP 2019，L1 英语。

### 5.4 Raw Process Data
- **Raw log**：每次点击/页面访问（16 个唯一动作：Start、3 篇文章、11 题、review）。
- **Derived feature**：导航序列（编码的动作序列）、导航序列长度、测试时长、NAEP 阅读 scale score。示例序列：Start, Article1, item01, Article1, item01, Article2, ..., review。

### 5.5 Event Granularity
页面点击（文章/题目页之间导航）；序列 = 页面访问列表。未讨论粒度改变认知解释。

### 5.6 Preprocessing
页面编码为 1–16；序列从原始日志提取；DTW 距离 + k-medoid 聚类（k=2..17，Silhouette/DB/Dunn 选 k=6）；聚类代表性序列提取。

### 5.7 Behavioral Indicators
导航序列长度（往返页面/题目的次数）、测试时长（秒）、scale score。look-back 模式 = 前进前反复回到之前题目/页面。无阈值说明。

### 5.8 Behavioral Pattern / Strategy
DTW + k-medoid → 6 簇，代表性序列。**模式是数据挖掘的，解释是事后贴标签**。cluster 1 代表性序列显示密集的 Article↔item 往返（look-back）。

### 5.9 Cognitive Interpretation
- look-back = 「不确定答案 → 回看收集信息或确认」；反复回看某题 → 「struggling with content，需要支持」；快速不回看 → 「confident」**或** 「overconfident / casual attitude」。
- **论文明确给出同一行为的多重互斥解释**（p.「Implications」节），无 think-aloud 区分。
- 证据类型：**POST-HOC / THEORY-BASED**。

### 5.10 Reading Skill
导航序列长度与 NAEP 阅读 scale score 正相关 r=0.423。Cluster 6（导航动作最多、时长最长）平均 308.8 vs Cluster 4（最少）236.3（Table 1）。**CORRELATIONAL**。

### 5.11 Individual Differences
未考察（论文承认，p.5.2 Limitations）。

### 5.12 Task Dependence
未考察。

### 5.13 Temporal Evidence
只有测试总时长；被解释为「struggling OR thorough」的歧义（p.3.3）。无逐页 dwell。

### 5.14 Ground Truth / Validation
- Predictive validity：导航活动 ↔ 成绩（r=0.423）。
- 无 cognitive construct validity。conference 论文，方法细节（聚类中心、统计检验）不完整。

### 5.15 Main Findings
r=0.423（导航活动↔阅读成绩）；Cluster 6 最高分/最长序列/最长时长；Cluster 4 最低。look-back 模式在各簇中形态不同。

### 5.16 Limitations
- **Paper-stated**：单一 grade（12）、单一任务块；只考虑 3 个变量；未分析人口学；未来应包含「每题的 revisit 次数、答案编辑次数、每页停留时间」。
- **Transfer limitations**：conference 论文，方法学细节与统计显著性不足，证据等级低；look-back 的歧义解释直接支持我们的「revisit ≠ confusion」边界——但该论文本身无法分辨。

---

## 6. B5 — Indirect Effects of Strategy Knowledge and Comprehension Skills on Navigation and Performance in Digital Reading（Naumann, Pucite, Salmerón & Eichmann, 2020）

**类型**：conference paper（AERA 2020 圆桌报告，AERA Online Paper Repository, DOI 10.3102/1582511）。**编号映射**：`B_2022_Naumann_StrategyKnowledge.pdf`。按任务 §19 证据等级降权。

### 5.1 Research Question
厘清理解技能与阅读策略知识在预测导航行为、进而预测数字阅读表现中的关系。检验三个竞争路径模型：（M1）两者平行预测导航；（M2）策略知识 → 理解技能；（M3）理解技能 → 策略知识 → 导航 → 表现。它研究 **skill/strategy → navigation → performance** 的中介结构。

### 5.2 Reading Task
PISA 2009 数字阅读测评（29 题、9 单元，每题 1–14 个任务相关页面，模拟浏览器超文本）。与 [B3] 同题库。相似度：**MEDIUM-LOW**（同 [B3]）。

### 5.3 Participants
34,400 名 15 岁学生，19 国，PISA 2009。

### 5.4 Raw Process Data
- **Raw log**：页面访问日志。
- **Derived feature**：**Precision 指数**（Rouet, 2003）= 访问的相关页数 ÷（可用相关页数 + 访问的无关页数）——同时捕获全面性与分心；**Adaptive processing 指数** = 个人内「任务难度 × 相关页平均时间」的相关——难度高时在相关页上花更多时间是 adaptive。策略知识（两个场景化问卷题，专家排序比对计分，WLE）；理解技能（PISA 印刷阅读 WLE）；数字阅读成绩。

### 5.5 Event Granularity
页面访问；adaptive processing 在个人内跨任务聚合（相关）。

### 5.6 Preprocessing
Precision 需要专家相关页编码；adaptive processing 需要项目难度（OECD delta）；潜变量建模（lavaan）。

### 5.7 Behavioral Indicators
Precision（比值，无阈值）、Adaptive processing（相关系数，[-1,1]）、策略知识 WLE、理解技能 WLE。

### 5.8 Behavioral Pattern / Strategy
无数据挖掘——理论驱动的路径模型（SEM）。navigation 为潜变量「task focused navigation」，两个指标（Precision + Adaptive processing）。

### 5.9 Cognitive Interpretation
Precision = 高效/选择性导航（相关选择）；Adaptive processing = 把时间分配到相关页并按任务难度调节——「task-appropriate processing」。策略知识 → 导航。证据类型：**CORRELATIONAL**（PISA 横断路径模型）。

### 5.10 Reading Skill
Model 3 拟合最佳（理解技能 → 策略知识 → 导航 → 数字阅读）：
- navigation → 数字阅读 b=0.70（直接，各回显著）；理解技能直接效应 b=0.17；策略知识直接效应 b=0.03（边际，几乎全被中介）。
- 间接效应：策略知识经 navigation b=0.15；理解技能总间接 b=0.47（= 直接效应的约 3 倍），分解为「理解 → 导航 → 阅读」b=0.37 + 「理解 → 策略知识 → 导航 → 阅读」b=0.07。
- **结论**：策略知识对数字阅读的作用被导航**完全中介**；理解技能存在独立的、不经策略知识的导航效应。相关性，非因果。

### 5.11 Individual Differences
理解技能是行为意义的关键个体差异：好理解者 → 更多策略知识 → 更精导航；且理解技能直接提升导航（不经策略知识）。文献引用：好理解者选择性地访问有用超链接、少访问无关链接（Naumann et al., 2008; Salmerón & García, 2011）。

### 5.12 Task Dependence
任务难度内嵌于 adaptive processing：学生在困难任务上应花更多时间在相关页。→ 时间分配行为的含义依赖任务难度。

### 5.13 Temporal Evidence
相关页停留时间——聚合为个人内难度相关。时间本身无独立含义；其含义来自「与任务难度匹配」这一 adaptive 标准。

### 5.14 Ground Truth / Validation
数字阅读成绩 + 印刷阅读技能（外部测试）+ 专家排序的策略知识。Predictive/correlational；无 think-aloud。

### 5.15 Main Findings
如上（b=0.70/0.47/0.15/0.07；Model 3 拟合最佳）。

### 5.16 Limitations
- **Paper-stated**：conference 报告，未系统陈述限制；样本为 PISA 2009。
- **Transfer limitations**：Precision 需相关页编码（我们需定义相关区域）；Adaptive processing 的「时间×难度」逻辑可直接迁移到我们每题一个 passage 的设定（题目难度 × 在相关区域的时间）。

---

## 7. B6 — For Skilled Comprehenders Digital Reading Is a Routine Task, for Unskilled Comprehenders It Is a Problem（Naumann et al., 2025）

**类型**：peer-reviewed journal（Learning and Individual Differences 122, 102745）。**编号映射**：`B_2025_Naumann_SkilledComprehenders.pdf`。

### 5.1 Research Question
检验「数字阅读对低理解者是问题、对高理解者是常规任务」的假说：问题解决技能在理解技能之上预测导航与数字阅读；理解技能与问题解决技能对导航/表现存在**序数交互（补偿性）**——问题解决的作用在低理解者中更强、在高理解者中更弱；这些效应经导航中介。它研究 **skill（理解+问题解决）→ navigation → performance**，是 B 组「individual-difference moderators」的核心论文。

### 5.2 Reading Task
PISA 2012。数字阅读 = 6 单元、19 题（PISA 2009 数字阅读题目，博客/论坛/网站/邮件等多页超文本）。19 题中 13 题需要至少一步导航（平均 2.9 步）；示例「Sports Club」需 10 步导航、整合 4 页信息找出最便宜俱乐部。assessment、closed environment、multiple-page hypertext。
- **与「左 Passage + 右题目」相似度：MEDIUM-LOW**。但 Precision 与 Adaptive processing 两个指标若把「页」替换为「段落/区域」，概念完全可迁移。

### 5.3 Participants
13,080 名学生，32 国，PISA 2012，15 岁。三个测量：复杂问题解决（27 个 interactive 题项，EAP rel. .76）、印刷阅读理解（44 题，WLE, EAP rel. .75）、数字阅读（WLE, EAP rel. .77）。**这是唯一同时含三种测量的数据集。**

### 5.4 Raw Process Data
- **Raw log**：PISA 2012 日志（页面访问、停留）。
- **Derived feature**：**Precision**（同 [B5] 公式）= 访问相关页数 ÷（可用相关页 + 访问无关页）；**Adaptive processing** = 个人内「题目难度 × 相关页平均时间」相关；WLE 分数（理解/问题解决/数字阅读）。

### 5.5 Event Granularity
页面访问（计数）；相关页时间按题聚合。粒度与认知解释的关系未直接讨论。

### 5.6 Preprocessing
相关页专家编码（必需/有用/不能排除有用）；Precision 与 Adaptive processing 计算；WLE；逐国路径模型 + 随机效应 meta-analysis。

### 5.7 Behavioral Indicators
Precision（比值）、Adaptive processing（相关，[-1,1]）、三项 WLE。无 dwell 阈值。

### 5.8 Behavioral Pattern / Strategy
理论驱动的路径模型（Fig. 2, p.3）。导航 = 两个指标，被理解技能、问题解决技能及其交互预测，再预测数字阅读。

### 5.9 Cognitive Interpretation
- Precision = 「efficiently building a representation of the problem space」（高效选择相关材料）；Adaptive processing = 「indicator of the quality of monitoring and self-regulation processes」（把时间调到任务难度 = 元认知调节的原型实例，p.4/12）。
- navigation 被概念化为「bridging the gap between an informational given and goal state」的问题解决过程（p.4）。
- 证据类型：**CORRELATIONAL**（PISA 路径模型）+ **THEORY-BASED**（RESOLV、问题解决框架、MD-TRACE）。

### 5.10 Reading Skill
- 总效应：理解技能 → 数字阅读 b=0.40；问题解决 → 数字阅读 b=0.31（理解之上）；交互（补偿）b=-0.05（meta-analytic 显著，11/32 国显著）。
- Precision → 数字阅读 b≈0.39（各国显著）；Adaptive processing → 数字阅读 b≈0.15（26/32 国）。
- 中介：Precision 中介理解 b=0.12、问题解决 b=0.10、交互 b=-0.03；Adaptive 中介理解 b=0.027、问题解决 b=0.015、交互不显著。

### 5.11 Individual Differences
**核心**：
- 理解 × 问题解决对 Precision 的补偿性交互 b=-0.08：对低理解者，问题解决技能更预测导航精确度；高理解者问题解决作用较小。
- 对 Adaptive processing 无交互（b=-0.02 n.s.）：时间分配被两种技能**加性**预测——「adequately realizing when textual information needs to be processed with a high degree of scrutiny is hampered by failing comprehension and problem solving alike」（p.12）。
- 国家层面：交互效应与国家级问题解决均值相关 r=-0.74 → 阈值模型（p.14）。

### 5.12 Task Dependence
Discussion 区分任务类型：搜索引擎起点的任务（信息空间不透明、需要高导航精度 → 交互模型成立）vs. 明确指定待读文本的电子课本任务（透明 → 加性模型成立）。→ **任务透明度决定导航是否反映问题解决**。

### 5.13 Temporal Evidence
Adaptive processing 即时间指标：相关页时间应与题目难度正相关（adaptive）。好理解者更擅长时间-难度适配（文献）。时间含义 = 监控/自我调节质量，且**任务难度依赖**。

### 5.14 Ground Truth / Validation
三项技能的外部计分（WLE）+ 数字阅读成绩。Predictive validity（路径模型）；无 think-aloud；作者明确呼吁用 eye-tracking/think-aloud 打开黑箱（p.14）。

### 5.15 Main Findings
H1a 支持（PS→Precision b=0.27）；H1b 支持（PS→Adaptive b=0.15）；H2a 支持（CS×PS→Precision b=-0.08）；H2b 不支持（CS×PS→Adaptive n.s.）；H3 支持（PS 总效应 b=0.31）；H4 部分支持（CS×PS→数字阅读 b=-0.05）；H5 支持（Precision 中介）；H6 部分支持（Adaptive 中介 CS/PS，不中介交互）。

### 5.16 Limitations
- **Paper-stated**：相关设计、无因果；PISA 2012 数据较老；缺元认知策略知识变量；仅「cold」认知——导航也反映动机/投入（Guthrie）；交互效应只在约半数国家显著；国家阈值效应。
- **Transfer limitations**：相关区域编码前提；Adaptive processing（时间×难度）可迁移；「同一行为在高/低理解者含义不同」直接支撑我们的个体差异调节器设计。

---

## 8. B7 — Leveraging Process Data to Investigate the Interplay Between Response Formats and Cognitive Processes in Digital Assessment and Learning Environments（Arslan et al., 2026）

**类型**：peer-reviewed journal（Contemporary Educational Psychology 85, 102461）。**编号映射**：`B_2026_Arslan_ResponseFormatsCognitiveProcesses.pdf`。

### 5.1 Research Question
反应格式（拖放 D&D、下拉、点网格）是否显著影响排序任务与分类任务中的认知过程？它研究 **response format × task type → cognitive processes**（用 macro + micro process indicators 追踪），是 B 组「pause 何时才有认知解释」的核心实验证据。

### 5.2 Reading Task
ELA 阅读测评（8 年级）。三篇故事（Alice 528 词、A Voyage to the Moon 383 词、Mary's Pigeons 450 词），每篇故事在「Story」页签、题目在「Questions」页签，学生**可自由往返**（p.5）。每篇含：排序任务（5 个事件 + 2 个干扰项）、分类任务（7 个短语）、一个推论 MC 题。排序 = Locate/Recall，分类 = Integrate/Interpret（NAEP 框架）。assessment、closed environment。
- **与「左 Passage + 右题目」相似度：HIGH**。Story/Questions 双页签自由切换 = 我们「左 passage + 右题目」的语义等价物；排序/分类任务的反应过程与 MC 题不同，但 pause 定义与「信息检索/终答检查」指标直接可迁移。

### 5.3 Participants
443 名 8 年级学生（原 536，剔除 76 名泄漏题目学校学生、1 名系统崩溃、16 名英语非熟练者），美国 6 州 6 校。49.4% 女生。外部州 ELA 成绩。

### 5.4 Raw Process Data
- **Raw log**：毫秒级时间戳的交互与系统事件：拖放事件（drag-drop-to-target / move-to-target / replace-target / move-reorder）、下拉选择（inline-change）、点网格（ssmc-click）、提交点击、题目 onset/exit（p.6–7）。
- **Derived feature**：**superfluous response-related events**（实际事件数 − 设计最小必需数）、**item completion time**（onset→exit，排除读故事时间）、**information-retrieval pause**（两次连续答题事件之间）、**final-response-review pause**（最后答题事件→提交之间）、ELA 任务得分。

### 5.5 Event Granularity
单一交互事件（毫秒级）。论文明确区分 **macro-level**（事件计数/总时间，不够推断策略）与 **micro-level**（事件间 pause，可推断认知过程）——「macro-level measures alone are not sufficient to make inferences about learner strategies and cognitive processes」（p.3）。

### 5.6 Preprocessing
IQR 去离群（各指标 4.5%–9.4%）；极端值仅从对应结果变量的模型中剔除；最小必需事件数由设计固定（排序 D&D=5、下拉/网格=7；分类=7）。

### 5.7 Behavioral Indicators
superfluous events（计数）、item completion time（秒）、information-retrieval pause（秒）、final-response-review pause（秒）。**阈值由设计固定（最小必需事件数），无任意 dwell 阈值。**

### 5.8 Behavioral Pattern / Strategy
无聚类——**受控实验**（within-subject，36 个 counterbalanced form）+ 混合效应模型。指标由认知理论先定（offloading cognition onto perception, Hegarty 2011）。

### 5.9 Cognitive Interpretation
- information-retrieval pause = 作答时的信息检索/比较等内部加工；final-response-review pause = 提交前的决定 + 监控/检查（p.4）。
- 排序任务中静态格式（下拉/网格）pause 更长 → 需要更多内部加工（工作记忆负担、检索）；D&D 把认知外化到知觉 → pause 更短。
- **process-product 分离**：下拉格式得分反而更高（OR=1.40）——作者给出的解释是「greater observable interaction costs... may reflect more controlled and reflective engagement」（p.9）。**该解释是 plausible explanation，作者明确说需 future studies 验证**。它可靠推翻「更长 pause/更多交互 = 困惑」的固定方向，但**不能反向确立「更长 pause = 审慎」**。
- 证据类型：**EXPERIMENTAL**（受控随机）+ **THEORY-BASED**。论文自认过程指标只是「indirect proxies」（p.9）。

### 5.10 Reading Skill
外部州 ELA 成绩预测任务得分（排序 OR=1.44、分类 OR=1.51，p<.001）——任务效标效度；但 ELA 作为协变量，不探讨交互。反应格式差异与阅读技能本身无关。

### 5.11 Individual Differences
ELA 为协变量非调节；工作记忆任务收集但未用（missing not at random, 24% 未完成）。

### 5.12 Task Dependence
**核心发现**：
- 排序任务：D&D 相比下拉/网格 → 更少 superfluous events（IRR 1.26/1.88）、更短 completion time（仅 vs 下拉 +14.38s）、更短 information-retrieval pause（1.73×/1.31×）、更短 final-response-review pause（1.16×/1.34×）。
- 分类任务：D&D **无优势**；点网格更短时间（-4.48s）与更少事件（IRR 0.51）；D&D 在分类中反而更多 superfluous events。
- → **同一反应格式在不同任务类型产生相反的过程指标差异**，反应格式选择必须匹配任务认知过程。

### 5.13 Temporal Evidence
两个 context-defined pause 是论文核心。pause 定义严格绑定事件对（两次答题事件之间 vs 最后答题到提交），非泛化停留时间。raw dwell 未被使用。

### 5.14 Ground Truth / Validation
**受控实验**（反应格式操控、内容等价题、36 表单完全 counterbalance）+ 外部州 ELA 效标。这是 B 组中最强的 pause 解释实验证据；但仍是间接指标，作者呼吁 think-aloud/eye-tracking 进一步验证（p.9）。

### 5.15 Main Findings
排序任务：D&D 减少 construct-irrelevant 加工（更少事件/时间/pause）但下拉得分更高（process-product 分离）；分类任务：D&D 无益、点网格更优。D&D 均值表（Table 1）：排序 D&D completion 74.23s vs 下拉 90.60s；information-retrieval pause D&D 2.80s vs 下拉 4.67s。

### 5.16 Limitations
- **Paper-stated**：单一课堂时段限制题量；多故事少题可能降低投入；过程指标为间接代理，需 think-aloud/eye-tracking；D&D 的物理拖拽可及性问题。
- **Transfer limitations**：我们的 MC 题 + 划掉选项 ≈ 点网格/下拉类静态格式 → 学生可能需要更多内部检索加工（pause 会反映在作答动作之间）；「时长的认知意义无固定方向（更长 pause 既可能伴随更高得分、也可能伴随困惑）」直接冲击「dwell=困难」的朴素假设。

---

## 9. B8 — Combining Cognitive Theory and Data Driven Approaches to Examine Students' Search Behaviors in Simulated Digital Environments（Tenison & Sparks, 2023）

**类型**：peer-reviewed journal（Large-scale Assessments in Education 11:28）。**编号映射**：`B_2023_Tenison_SearchBehaviorsSimulatedEnvironments.pdf`。

### 5.1 Research Question
RQ1：学生在模拟搜索引擎工具中的主要搜索策略？RQ2：搜索行为与 ELA 任务表现的关系？RQ3：搜索行为在任务过程中的变化？它研究 **search behavior patterns → performance + goal update**，方法论上示范「认知理论 + 数据驱动」的融合（事件选择与 pause 分类由 MD-TRACE 理论指导，聚类由数据驱动）。

### 5.2 Reading Task
ELA Virtual World——场景式多源探究任务（NAEP SAIL）。学生评估 10 条关于历史事件的主张，写来源论证。模拟网页搜索工具（Google-like，~25 个来源，相关性与可靠性各异）+ 证据管理器（评价来源）。三阶段：Setup / Free Roam / Conclusion。multiple-source inquiry，非 comprehension-question-per-passage。
- **与「左 Passage + 右题目」相似度：LOW-MEDIUM**。无单 passage+MCQ；但「搜索会话序列 + pause 语境化 + 信息需求敏感性」的方法可迁移。

### 5.3 Participants
130 名 8 年级学生（67 女），2 校（91 城市、39 乡村），90 分钟 tryout。127 人访问过搜索工具；109 人进入 Conclusion；104 人完成主张评估；98 人完成论证任务。美国。

### 5.4 Raw Process Data
- **Raw log**：带时间戳的学生动作与系统事件（搜索、点击、滚动、按键、帮助、提示）。
- **Derived feature**：24 个动作标签（Plan Search / Locate Information / Evaluate Sources / Interface actions / Pauses 三大类，Table 2）；来源质量编码（high/medium/low = 任务设计意图）；pause 分类（short/medium/long）。

### 5.5 Event Granularity
**明确讨论**：动作 = 改变任务状态的学生事件（运行搜索、导航、求助）；低层事件（滚动位置、按键）被标记并在**首次出现时作为该活动起点**（collapse 为单个行为），依据 Kroehne & Goldhammer (2018) 与 Goldhammer et al. (2021)。→ 粒度选择由认知理论指导。

### 5.6 Preprocessing
- pause <250ms 剔除（动作准备时间，Anderson 2009）；pause <2.5s 剔除（导航动作）；2.5–10s short、10–30s medium、>30s long（p.14–15，Fig. 3 显示不同前置动作的 pause 分布不同：plan M=14.4s、locate M=7.4s、evaluate M=103.6s）。
- 剔除 46 个「访问但未搜索」会话 + 3 个 >125 动作会话（疑似日志 bug）。
- 归一化 OM 编辑距离 → Ward 层次聚类 → 选 4 簇（Calinski-Harabasz 11.7@3clusters、Silhouette 0.83@4clusters）→ 每簇 HMM（4–10 态，BIC 选 9/5 态）→ 用这些作为先验重拟合 mHMM。

### 5.7 Behavioral Indicators
24 个动作类型频率（Table 2）；pause 类别（short/medium/long）；来源质量。**显式阈值：250ms / 2.5s / 10s / 30s。**

### 5.8 Behavioral Pattern / Strategy
数据驱动：归一化 OM + Ward + mHMM。策略标签（thoughtful / scaffolded / secondary-topic / low-quality search）是**研究者事后贴的**，但事件选择与 pause 分类由 MD-TRACE 理论先导。论文坦承：「it is unlikely that each of the clusters represents a singular strategy」；「decoding how these behaviors reflect strategies... involves a degree of subjectivity」（p.31）。

### 5.9 Cognitive Interpretation
- pause = 认知活动（处理信息、决定下一步、执行策略动作），不同上下文的 pause 状态代表不同加工。
- 搜索行为反映「how students generate and update their task goals」（abstract）。
- Thoughtful Search（簇1）= goal-driven：快速构造高相关查询、存取关键来源；Scaffolded（簇2）= 依赖系统提示；Secondary Topic（簇3）= flimsy navigation 或 satisficing（两种互斥解释，p.30）；Low Quality（簇4）= 各方面挣扎。
- 证据类型：**CORRELATIONAL** + **THEORY-BASED**（MD-TRACE）。无 think-aloud，作者明确承认标签主观性并呼吁 think-aloud。

### 5.10 Reading Skill
- 簇1 比例与总任务分正相关 r=0.310（且与 searching r=0.407、evaluating r=0.260、synthesis r=0.203）；簇2 负相关 r=-0.325。
- 簇1 会话得分概率显著高于簇3（OR 0.35, p<.05）；簇1 对剩余信息需求更敏感（points-left × cluster 交互最强）。
- 簇1 首次会话 75% 找到关键信息且不再回访；簇1 更可能到达 finished state（53%）。
- **CORRELATIONAL**。

### 5.11 Individual Differences
未直接建模（无阅读能力测量）；讨论中承认学生目标意识差异大（Rouet et al., 2021），信息需求敏感性是策略差异来源。

### 5.12 Task Dependence
RQ3 证明搜索行为随任务上下文（已积累信息量）改变；系统提示（hints）本身是区分簇2/簇3 的构成性事件——**任务内 scaffold 改变行为意义**。

### 5.13 Temporal Evidence
pause 分类是本论文的可用交付（阈值 + 前置动作依赖分布）；「the sequence mining approach uses both the pause label and the context of the pause within student's action sequences to estimate the cognitive state that generated the pause」（p.15）。

### 5.14 Ground Truth / Validation
任务计分（evidence model，Table 1）+ 分阶段/分构念得分。Predictive validity（簇↔得分相关）；Behavioral validity（聚类稳定）；Cognitive construct validity 有限（无 think-aloud，作者呼吁 eye-tracking/think-aloud 打开黑箱，p.31/35）。

### 5.15 Main Findings
4 簇（99/162/48/10 会话）；簇1 ↔ 更高总任务分/搜索/评价/综合子分；簇2 ↔ 更低；簇3 ↔ 计划子分正、搜索子分负；簇1 对信息需求最敏感。约 52% 学生提交 ≤5 次搜索；工具平均得分仅 7/23（32%）——**学生普遍难以选择相关来源**（仅 2% 访问全部 3 个关键网站）。

### 5.16 Limitations
- **Paper-stated**：N 小；24% 未完成 Conclusion；标签主观性；无法分离单策略与策略链；LCS 对序列长度过敏感（改用归一化 OM）；需要 think-aloud。
- **Transfer limitations**：pause 阈值（250ms/2.5s/10s/30s）与「前置动作依赖分布」可移植到我们界面；「事件选择由理论先导」是 Raw→Semantic Event 的模板；任务为探究式而非 MC 阅读，搜索行为结构不同。

---

## 10. B9 — Going Beyond Observable Actions: A Cognition-Centered Approach to Interpreting Pauses Represented in Process Data（Arslan, Tenison & Finn, 2023）

**类型**：peer-reviewed journal（European Journal of Psychological Assessment, 39(4), 263–270，special issue: Process Data in Computer-Based Assessment）。**编号映射**：`B_2023_Arslan_InterpretingPausesProcessData.pdf`。

### 5.1 Research Question
如何从 process data 中的 pause 做出有效的认知推断？主张必须采用**任务特定、理论驱动的认知建模方法**（ACT-R 理性分析）。它是 B 组「What Does a Pause Mean?」的框架/方法论文。

### 5.2 Reading Task
案例研究为数学题（D&D 按面积把图形拖入箱子），非阅读。但方法声明领域无关（math/science/reading 均可，p.267）。与我们的相似度：内容 LOW，**方法论 HIGH**（pause 定义与事件对抽取直接适用）。

### 5.3 Participants
实证案例：N=476（受控随机实验，5 条件，10 道 D&D 数学题）；470 人、20,767 条观察。非阅读样本。

### 5.4 Raw Process Data
- **Raw log**：事件 + 时间戳：item-loaded、drag-drop-start-drag、drag-drop-drop-to-target、drag-drop-return-source、drag-drop-move-to-target、move-next（Table 1, p.268）。
- **Derived feature**：pause = 两个连续事件的时间差；分类 pause（first / intermediate / final）。

### 5.5 Event Granularity
**核心方法论**：pause 的认知内容由**事件对**（event pair）决定，不是由 pause 本身。例：`<drag-drop-drop-to-target, drag-drop-start-drag>` = problem-solving pause；`<drag-drop-return-source, drag-drop-start-drag>` 与 `<drag-drop-move-to-target, drag-drop-start-drag>` 也可能含 problem-solving，但也可能指示可用性问题或答案修改 → **从分析中排除**（p.268）。→ 粒度与事件对选择直接改变认知解释。

### 5.6 Preprocessing
1) 检测并处理 disengaged responses（快速作答，按题完成时间）；2) 查看日志 codebook 理解事件语义；3) 把 Step 1 的认知过程链接到事件对；4) 抽取含目标认知过程的事件对；5) 计算 pause 时长；6) **剔除 <250ms pause**（ACT-R 最小动作准备时间，Anderson 2007）与离群长 pause（离群 = off-task）。

### 5.7 Behavioral Indicators
各事件对类别的 pause 时长（秒）。**阈值：250ms 下限（理论），离群长 pause 处理（off-task）。**

### 5.8 Behavioral Pattern / Strategy
非数据挖掘——**理论先行**：理性分析（识别目标/约束、信息加工子目标、期望最优行为）→ 构建理论认知模型 → 链接日志事件 → 统计建模。

### 5.9 Cognitive Interpretation
- **第一 pause**（题目 onset → 首次动作）= 编码题面 + 目标设定（可能混入问题解决/计划）；**中间 pause**（答题动作之间）= 问题解决（针对将要动作的那个图元）；**最后 pause**（最后答题动作 → 提交）= 决定提交 + 监控目标达成 + 复查答案（p.265–267）。
- **核心论断**：不结合上下文（前导/后继事件、任务 affordance 与结构）就无法对 pause 做有效认知推断（p.264）；「认知过程取决于任务的 affordance 与结构，以及 pause 发生的上下文」。
- 混杂源：练习效应（随题学习）、disengagement（快速作答）。
- 证据类型：**THEORY-BASED**（ACT-R）+ 案例 **CORRELATIONAL**；作者明确这是 argument-based validation 而非 empirical validation，需 think-aloud/神经影像（p.269）。

### 5.10 Reading Skill
非阅读研究；但框架为阅读任务的 pause 解释提供模板。

### 5.11 Individual Differences
练习效应（跨题学习导致 pause 缩短）与 off-task 作为混杂需控制；模型含被试/题目随机效应。

### 5.12 Task Dependence
「认知过程取决于任务的 affordance 与结构」（p.264）——同一类型 pause 在不同任务结构下含义不同。

### 5.13 Temporal Evidence
**核心交付**：为什么「停留 10 秒」本身没有认知意义？因为 pause 的认知内容来自事件对（前后事件）+ 任务状态 + 位置，而非时长本身；250ms 以下无认知意义（动作准备）；长 pause 可能是 off-task 也可能是深加工，需按上下文判断。案例实证：problem-solving pause → 正确率 OR=1.40（95% CI [1.06, 1.84], p=.016）。

### 5.14 Ground Truth / Validation
- **Behavioral validity**：事件对提取的 pause 分布稳定。
- **Predictive validity**：problem-solving pause 预测正确率（OR=1.40）。
- **Cognitive construct validity**：argument-based（ACT-R 理论论证）而非 empirical——作者明确呼吁 think-aloud/神经影像补充。

### 5.15 Main Findings
框架方法（三步骤）+ 案例：problem-solving pause 预测成功（OR=1.40）。「任务特定认知建模」是有效 pause 推断的必要前提。

### 5.16 Limitations
- **Paper-stated**：argument-based 验证非实证验证；案例简单（well-defined math）；需要 think-aloud/神经影像。
- **Transfer limitations**：为我们的系统提供 pause 解释的模板——需要为「左 passage + 右题目」建立任务特定认知模型来定义 pause 类（如 passage→question 切换 pause = 信息检索；最后答题→离开 pause = 终答检查），不可直接用 raw dwell。

---

## 11. B10 — Purpose Instructions and Task Models in Multiple-Text Reading（Lyu, Yao & McCrudden, 2026）

**类型**：peer-reviewed journal（Learning and Instruction 104, 102347）。**编号映射**：`B_2026_Lyu_PurposeInstructionsTaskModels.pdf`。

### 5.1 Research Question
目的指令（理解/测验/论文/展示）如何影响任务模型建构（阅读目标 + 计划策略）、阅读过程（think-aloud）与学习结果？它研究 **task instruction → task model → reading process → learning outcome** 的链条，是 B 组「question preview → goal formation」的理论锚点，且提供 think-aloud 地面真值。

### 5.2 Reading Task
多文本阅读：4 篇互补短文（自然选择原理篇 204 词 + 3 篇动物实例篇各 ~104–116 词），每 1–2 句一个 typed think-aloud 框（共 29 个）。random 分配 4 种目的指令。learning、closed environment、linear multiple-text（无导航）。
- **与「左 Passage + 右题目」相似度：LOW**（无逐题交互，think-aloud 逐句打断）。但任务模型概念（阅读目标 + 计划）与「学生如何理解题目要求」直接相关；think-aloud 编码提供了「何种认知过程对应何种目标/计划」的实证映射。

### 5.3 Participants
75 名本科生（平均 20.17 岁），美国公立大学教育心理学导论课；76% 女性；L1 英语。前测后测主题知识（自然选择五原理应用，α=.82/.95）。

### 5.4 Raw Process Data
- **Raw**：typed think-aloud 逐句反应（非点击流）；开放题任务模型反应（2 题：阅读目标 + 计划）。
- **Derived feature**：12 个目标元素（理解内容、阅读、报告想法、学知识、跨文链接、备考、解释、准备展示、概括、分析、写作、形成观点）；9 个计划策略（注意力、标注、出声思维、结构组织、重读、任务定向、自我检查、环境调节、外部资源）；4 类认知过程（paraphrase、elaboration、monitoring、bridging）。

### 5.5 Event Granularity
think-aloud 在句子组（概念单元）粒度；非行为事件。与点击流无关。

### 5.6 Preprocessing
归纳编码 + 双人编码（κ：目标 .81、计划 .65、过程 .79）；backward elimination 回归。

### 5.7 Behavioral Indicators
自陈目标/计划的频率分布；think-aloud 认知过程频率。**无行为日志、无 dwell。**

### 5.8 Behavioral Pattern / Strategy
编码方案 + 回归，非序列挖掘。策略 = 自陈计划 + think-aloud 观测。

### 5.9 Cognitive Interpretation
- 任务模型 = 「mental representation that directs students' reading by specifying what the task entails, why it is important, and how it should be completed」（MD-TRACE Step 1）。
- **关键**：同样的目的指令在不同学生产生不同任务模型；task model 成分（而非指令本身）预测阅读过程。Rereading 作为计划策略预测 bridging 推理（β=.29）与后测（β=.26）。
- 证据类型：**CORRELATIONAL**（回归）+ **THINK-ALOUD**（直接过程测量）。

### 5.10 Reading Skill
后测（迁移/应用测试）：quiz 指令直接预测（β=.28）、前测 β=.34、写作目标 β=.22、重读计划 β=.26、paraphrase β=.22、bridging β=.22（边际）；R²adj=.46。认知过程（paraphrase、bridging）→ 学习，符合文档模型框架。

### 5.11 Individual Differences
**核心**：组内变异性——同一指令下任务模型分化；理解条件中仍有学生形成高阶目标（备考、跨文链接）。「task model formation is influenced by both instructional cues and learner-specific factors」（p.10）。前测知识 β=.34 预测后测。

### 5.12 Task Dependence
指令类型改变任务模型复杂度与方向：quiz → 结果导向目标 + 更广计划（结构化/标注/自我检查）；essay → 最多样目标；presentation → 内容掌握 + 展示准备双重。目的指令不直接预测任一阅读过程——**只有任务模型成分预测过程**。

### 5.13 Temporal Evidence
无时间数据。Rereading 是**自陈计划**，非实测行为——不能据此推断真实重读时长。

### 5.14 Ground Truth / Validation
think-aloud（直接认知过程）+ 开放题任务模型（直接测量解释）+ 迁移测试。这是 B 组少有的「直接过程测量」来源。κ 可靠性报告。

### 5.15 Main Findings
- 各条件：理解内容（37.3%）与阅读（36.0%）是普遍目标；注意力（40.0%）、标注（30.7%）、出声思维（28.0%）是普遍计划。
- 目的指令不预测任一阅读过程；任务模型成分预测：paraphrase（阅读目标/跨文链接/备考/结构化）、bridging（跨文链接/写作/重读/环境）、elaboration（理解/报告/学知识/概括；标注**负**预测）、monitoring（展示目标+出声思维；阅读目标负预测）。
- 后测：quiz 指令、前测、写作目标、重读计划、paraphrase、bridging 显著。

### 5.16 Limitations
- **Paper-stated**：开放题可能未捕捉任务模型全貌；think-aloud 干扰自然阅读；backward regression 过拟合风险；计划编码 κ=.65 偏中；探索性。
- **Transfer limitations**：任务模型（目标+计划）为我们的「question preview → goal formation」提供理论支持，但**警告**：不能从「给了题目」推断「学生形成了何种目标」——目标形成存在个体差异；think-aloud 是地面真值但不能规模化，需过程数据 + 任务模型问卷/编码三角验证。

---

## 12. B11 — Quantifying the Benefits of the Reread-Before-Answer Strategy in Japanese High-School EFL（Wijerathne, Flanagan & Ogata, 2025）

**类型**：conference proceedings（ICCE 2025，Asia-Pacific Society for Computers in Education）。**编号映射**：`B_2025_Wijerathne_RereadBeforeAnswer.pdf`。按任务 §19 证据等级降权。

### 5.1 Research Question
RQ1：Reread-Before-Answer（RBA）循环与 MCQ 成绩是否相关？RQ2：控制停留时间、序列长度、先前英语能力后，RBA 效应是否成立？RQ3：哪些导航行为区分 top-quartile MCQ 会话？它研究 **revisit-before-answer 策略 → 成绩**——是 B 组「revisit 意味着什么」的最直接实证。

### 5.2 Reading Task
BookRoll 电子书平台，日本高中 EFL 课程，56 个 PDF 内容单元，每单元末尾有 open-book MCQ。学生读数字文本 + 回答 MCQ，日志记录页面导航。
- **single-text + MCQ + open-book**。
- **与「左 Passage + 右题目」相似度：HIGH-MEDIUM**。单文本阅读 + 答题 + 答题前回读行为是语义最近似；区别是页面翻页导航而非单页滚动。

### 5.3 Participants
263 名日本高中英语学习者（EFL），1 个月日志；57,532 事件、6,023 个 MCQ 答案、正确率 55.4%。

### 5.4 Raw Process Data
- **Raw log**：xAPI 事件——PDF 访问、页面导航、文本高亮、测验响应 + 时间戳。
- **Derived feature**：页面导航序列（有序页面 ID）、**RBA 循环检测**（k=10 窗口内回跳）、Time-on-Page（事件间时间求和，封顶）、Sequence Length（转移数）、Prior English Ability（分班测试，标准化）、MCQ Accuracy。

### 5.5 Event Granularity
页面事件（翻页）+ 测验响应；序列 = 页面访问有序列表。粒度未讨论对认知解释的影响。

### 5.6 Preprocessing
JST 时区调整、去重排序；**30 分钟不活跃会话化**（稳健性 5/15/45）；RBA 检测 = O(n) 扫描（k=10 窗口；稳健性 k=1..5）；缺失先前能力用多重插补（10 数据集，Rubin 规则）。

### 5.7 Behavioral Indicators
has_RBA（二值）、Time-on-Page（z 标准化，封顶）、Sequence Length（z）、Prior Ability（z）、MCQ Accuracy。**阈值：会话间隙 30 分钟；回跳窗口 k=10（稳健性 k=1..5）。**

### 5.8 Behavioral Pattern / Strategy
RBA = **显式规则定义**（page i → page i−k → page i → answer，k≥1，p.1-2）；motif = **PrefixSpan 频繁子序列挖掘**（长度 3–5 页、≥2% 序列）+ 分位数组比较 + PageRank 网络可视化。策略部分规则先定、部分数据挖掘，解释为「constructive re-processing」/「metacognitive strategy of verifying facts」（p.1-2）。

### 5.9 Cognitive Interpretation
- RBA = 答题前「deliberate backtracking to previously read material」= 验证事实/概念的元认知策略（p.1-2）。
- **论文明确承认**：「Deducing strategies from log data bears the risk of mischaracterizing certain page revisits as constructive, when they may instead signify confusion or distraction」（p.4, Discussion）——回读可能 = 建设性重加工，也可能 = 困惑/分心。
- 证据类型：**CORRELATIONAL**（观察数据，控制混杂）+ **THEORY-BASED**（重读促进理解，Thomas & Healy 2012）。

### 5.10 Reading Skill
- RQ1：RBA 会话准确率 56.4% vs 线性 46.3%（~10pp；Cohen's d≈0.35，z=4.9，p<.001）。
- RQ2：控制后 RBA β=0.244（OR=1.28, 95% CI [1.07, 1.53], p=.008）→ 约 6% 绝对提升（46%→52%）。先前能力最强预测（β=0.569, OR=1.77）；Sequence Length β=0.123（OR=1.13）、Time-on-Page β=0.188（OR=1.21）。
- RQ3：top-quartile 会话中 backward motifs（3→2、2→1、4→3）与 self-loop（3→3）更常见；2/3 的 top-quartile 会话有后向导航，bottom-quartile 不到一半。
- **CORRELATIONAL**，明确非因果。

### 5.11 Individual Differences
中等/高能力组 RBA 获益 8–12pp；低能力组仅 3–5pp（低能力者准确率从 ~40%→45%）。先前能力控制后 RBA 仍显著 → RBA 独立于能力，但获益大小随能力变化。

### 5.12 Task Dependence
open-book 格式下 RBA 有益；论文明确「results could vary... in contexts requiring closed-book assessments」（p.4）。回跳窗口敏感性：k 是 **RBA 检测算法允许的 backward-window（检测参数），不是实验操纵的阅读距离**；k=1 几乎无 RBA；k≈4 的窗口捕获了多数与较高正确率相关的回读模式（约 9.1pp），k>4 不再增加。**这是「该数据集 + 该检测定义」下的相关模式，不能推广为「英语阅读回读 4 页是最佳策略」。**

### 5.13 Temporal Evidence
Time-on-Page（封顶）作为协变量；RBA 的本质是**序列**而非时长。在该数据集中更大的回跳窗口不再增加与正确率的关联——但这只说明「检测窗口」与「学生真实回读长度」不是同一概念，**不能据此建立「短促回读最优」的系统规则**。

### 5.14 Ground Truth / Validation
MCQ 准确率（即时成绩）。Predictive validity（控制混杂后回归）；无 think-aloud/eye-tracking——作者呼吁 screen capture/eye-tracking 澄清意图（p.4）。

### 5.15 Main Findings
RBA 占会话 39.6%；RBA ~10pp 原始、~6pp 控制后获益（OR=1.28）；先前能力 OR=1.77 最强；top-quartile 会话更常出现后向回读 motif。k≈4 的回跳窗口捕获多数相关模式（数据集特定，见 5.12，非实验结论）。

### 5.16 Limitations
- **Paper-stated**：相关设计不能断言因果（动机/元认知等外变量可能影响 RBA 使用）；只测即时成绩，长期保持未知；日本 EFL 高中情境与闭卷环境推广受限；**日志推断风险（回读可能是困惑）**；高亮行为未分析；motif 分析范围有限；30 分钟会话阈值的低估风险。
- **Transfer limitations**：这是「revisit-before-answer」在我们任务（passage+MCQ）上最直接的正向证据，但 conference 等级 + 相关设计 → 只能作为**概率证据**（revisit-before-answer 关联更高正确率），不能作为「revisit = 策略」的确定性判断；低能力组获益小 → 能力调节。

---

## 13. Cross-Paper Comparison Matrix

| 维度 | [B1] (SRL) | [B2] (DTW) | [B3] (Engagement) | [B4] (SeqMining) | [B5] (Strategy) | [B6] (Skilled) | [B7] (ResponseFmt) | [B8] (Search) | [B9] (Pauses) | [B10] (TaskModel) | [B11] (RBA) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 期刊等级 | journal | journal | journal | conference | conference | journal | journal | journal | journal | journal | conference |
| 任务类型 | EFL 翻转学习 | 多源阅读题 | 超文本数字阅读 | 数字阅读（文章+题） | 超文本数字阅读 | 超文本数字阅读 | 排序/分类阅读题 | 多源探究 | 数学题（方法通用） | 多文本阅读学习 | EFL 电子书+MCQ |
| 与我们的界面相似度 | LOW | MEDIUM | MEDIUM-LOW | MEDIUM-HIGH | MEDIUM-LOW | MEDIUM-LOW | **HIGH** | LOW-MEDIUM | 内容 LOW/方法 HIGH | LOW | **HIGH-MEDIUM** |
| 过程数据粒度 | 平台动作 | 页面转移+时间 | 页面访问计数 | 页面/题目导航 | 页面访问 | 页面访问+时间 | **单事件(ms)** | 动作+pause类别 | **事件对+pause** | think-aloud | 页面事件 |
| pause/dwell 分析 | 无 | 时间序列（无区分） | 无 | 总时长 | 时间×难度相关 | 时间×难度相关 | **信息检索/终答检查 pause** | **pause 分档+前置动作** | **事件对 pause** | 无 | Time-on-Page（封顶） |
| 行为→策略方法 | FOMM | DTW聚类 | 混合模型交互 | DTW聚类 | 路径模型 | 路径模型 | 受控实验+混合模型 | OM+mHMM | 理论认知建模 | 编码+回归 | 规则+PrefixSpan |
| 主要证据类型 | 相关+准实验 | 相关 | 相关(17国) | 相关 | 相关(路径) | 相关(32国) | **实验** | 相关 | **理论论证**+相关 | 相关+think-aloud | 相关(控制混杂) |
| 个体差异调节 | 无 | 性别/SES | engagement | 无 | 理解技能 | **理解×问题解决** | 无(协变量) | 无(讨论) | 练习/off-task | **组内任务模型差异** | 先前能力 |
| 任务依赖 | 无 | 部分(UI) | **access demands** | 无 | 难度(内嵌) | **任务透明度** | **任务类型** | **任务上下文** | **affordance/结构** | **指令类型** | open-book |
| 回读/重访证据 | 无 | revisit 序列 | 相关页重访 | look-back 模式 | 相关页访问 | 相关页访问 | 无(排序重排) | 来源回访 | 无 | 重读(自陈计划) | **RBA 循环** |

**阅读顺序**：理解「导航/访问数量无独立含义、由任务需求调节」看 [B3]→[B6]；理解 pause 必须语境化看 [B9]→[B7]→[B8]；理解 revisit 的多重含义看 [B11]→[B4]→[B3]；理解任务模型/目标形成看 [B10]→[B6]；理解方法论（Raw→Semantic Event）看 [B9]→[B8]→[B7]。

---

## 14. Behavior → Process Evidence Matrix

表格列出我们系统全部候选行为的解释、支持论文、证据类型、强度与主要混杂。证据强度按任务 §7 四级标准（STRONG / MODERATE / WEAK / UNSUPPORTED）。

| Observable Behavior | Possible Interpretation | Supporting Papers | Evidence Type | Strength | Main Confound |
|---|---|---|---|---|---|
| **Question Preview**（先浏览题目再读文） | task orientation（假设）；goal formation 不可观测 | [B10]（task model 由目的指令塑造，个体差异大）；[B6]（task model 决定信息需求） | theory-supported hypothesis（[B10] 未研究「预览→目标形成」；think-aloud 显示同一指令下学生目标各异） | **WEAK / theory-supported**（可观测行为；「具体形成了什么 goal/plan」不能从 preview 恢复——[B10] 组内差异） | 预览可能只是习惯；形成何种目标不可观测 |
| **First-Pass Reading**（首次顺序阅读） | 建立全局表征 / passage comprehension | [B9]（首段=编码+目标设定类比）；[B2]（T3 转移页长读→高分） | theory-based | WEAK-MODERATE（理论合理；无直接 think-aloud 针对 first-pass in log） | 无法确定是否真在读（viewport≠attention） |
| **Forward Scrolling** | progressive reading / scanning | [B2]（T1 skimming 2s/页）；[B8]（locate 动作） | post-hoc + correlational | WEAK（只能说明 viewport 前进，不说明阅读） | viewport 移动 ≠ 阅读；可能是跳过 |
| **Backward Scrolling** | rereading / evidence search / difficulty / verification | [B11]（RBA→更高正确率）；[B4]（look-back 歧义）；[B3]（相关页重访高需求任务有利） | correlational（[B11] 控制混杂） | MODERATE（回读与更好成绩相关；但含义多重） | 回读可能是困惑/分心（[B11] 自认；[B4] 互斥解释） |
| **Paragraph Revisit** | strategic rereading / information retrieval / verification / comparison / uncertainty / difficulty | [B11]（答题前回读）；[B3]（相关页重访→高需求任务+表现）；[B6]（precision=相关页访问）；[B2]（revisit 序列→高表现模式） | correlational + theory-based | **MODERATE**（回读正向预测正确率，但单靠 revisit 无法区分六种状态——见 §15） | 无法区分策略 vs 困难 vs 不确定性 |
| **Question ↔ Passage Switching** | evidence search / comparison / verification | [B11]（回读后答题）；[B7]（story↔questions 页签切换是设计特征）；[B9]（事件对定义信息检索 pause） | correlational + experimental ([B7]) + theory ([B9]) | MODERATE（切换本身是证据检索的必要动作；结合前后事件可增强） | 切换次数=低效 vs 必要集成取决于题型（[B3]） |
| **Dwell / Pause（raw）** | reading time / thinking / retrieval / review / off-task / confusion | [B9]（核心：raw pause 无认知意义）；[B7]（context pause 有解释力）；[B8]（阈值+前置动作） | theory-based + experimental ([B7]) | **UNSUPPORTED 单独；MODERATE 语境化后**（见 §16） | 一切（时长无区分力） |
| **Repeated Revisit** | difficulty / careful verification / low confidence / normal strategy | [B4]（多重互斥）；[B11]（RBA 有助但能力调节）；[B2]（PT24/PT44 长序列短时=复杂） | correlational | WEAK（无法区分——见 §8） | 六种以上互斥解释 |
| **Underline / Highlight** | selection / relevance judgment / evidence marking | B 组无研究（[B11] 记录未分析；[B10] 标注计划与 elaboration 负相关） | 无 | **UNSUPPORTED BY GROUP B** | — |
| **Option Elimination** | — | B 组无研究 | 无 | **UNSUPPORTED BY GROUP B** | — |
| **Answer Selection** | choice（可观测）；reason/confidence（不可观测） | [B7]（选择动作=response-related event，pause 前后可语境化） | experimental | choice=STRONG；reason/confidence=UNSUPPORTED | 选择 ≠ 推理 |
| **Answer Change** | monitoring? verification? uncertainty? | [B9]（`move-to-target` 事件对可能=答案修改→排除出 problem-solving pause）；[B7]（superfluous events 部分=修改） | theory-based | WEAK（B 组无直接研究 answer change 的认知含义；只能通过事件对分类） | 修改=审慎 vs 不确定 |
| **Final Review**（选答案后回原文再回来未改） | verification / monitoring | [B7]（final-response-review pause=提交前监控/复查）；[B9]（最后 pause=决定提交+监控） | experimental ([B7]) + theory ([B9]) | MODERATE（终答前 pause/复查有理论+实验证据；但「回原文未改答案」的具体模式无直接证据） | 未改答案 ≠ 已验证；可能只是确认 |
| **Answer→Move On（完成后行为）** | confidence / disengagement | [B9]（快速作答=disengaged→剔除）；[B8]（簇1 完成即离开） | theory-based + correlational | WEAK | 快=信心 vs 快=不投入 |

**结论**：B 组可支撑「STRONG/MODERATE」的行为是（a）语境化 pause（[B7]/[B9]/[B8]）、（b）答题前回读/重访相关区域（[B11]/[B3]）、（c）question↔passage 切换（[B11]/[B7]）、（d）终答前复查（[B7]）。**underline/elimination 明确 UNSUPPORTED**；raw dwell、repeated revisit、answer change 只能给概率/弱证据。

### 14.1 反直觉结果专项（Same-Behavior-Different-Meaning）

任务 §15 要求重点寻找「同一行为 + 不同学生/任务/情境 → 不同含义」的反直觉证据，避免「行为计数 → 认知标签」的粗暴映射。B 组此类证据汇总：

| 同一行为 | 不同情境 | 相反/不同的含义 | 出处 |
|---|---|---|---|
| 更多访问/回读相关页 | 高 access demands vs 低 | 高需求任务中强正预测表现（β=0.51）；低需求任务中几乎不预测（β=0.19）——同一行为的意义完全由任务需求决定 | [B3] |
| 更长 pause / 更多交互动作 | 审慎 vs 困惑 | 下拉格式更慢、更多事件、更长 pause，但**得分更高**——作者提出「更审慎/受控作答」解释，但**仅为 plausible explanation 且需 future studies 验证**；可靠结论是「时长认知意义无固定方向」 | [B7] |
| 答题前回读（RBA） | 高/中/低能力 | 中高能力组获益 8–12pp，低能力组仅 3–5pp——同一策略的收益随能力变化 | [B11] |
| 长序列 + 短阅读时间 | 女生 vs 男生 | 同一导航模式下女生更高分（+20 分，疑似高效）；男生可能为「aimless quick switching」 | [B2] |
| 有限导航（只访问一页） | 任务是否需多源 | P1（只访书评页）最低分——但可能是因为「就近 tab」而非策略差；任务界面 affordance 影响行为 | [B2] |
| 多次回看（look-back） | 高 vs 低表现 | 论文同时给出「struggling 需支持」与「confident/overconfident」两种互斥解释——**无法仅凭行为分辨** | [B4] |
| 短促回读 vs 长时回读 | 回跳窗口 k（RBA 检测参数，非实验操纵的阅读距离） | 约 4 页的窗口捕获多数与高正确率相关的回读模式，更大窗口不再增加——**数据集特定**，既不能推出「回读越多越好」，也不能转为「回读 4 页最佳」规则 | [B11] |
| 访问/回读相关区域 | 高 vs 低理解/问题解决技能 | 低理解者靠问题解决技能补偿导航精确度；高理解者问题解决作用减弱（补偿性交互）——同一行为的预测来源随能力重组 | [B6] |

**含义**：B 组反复证实「more rereading ≠ worse」与「more navigation ≠ worse」的反面也同样不成立——**任何行为数量指标单独都没有稳定方向**。我们的系统必须携带「任务需求 + 能力 + 题型 + 事件上下文」四类调节信息才能解释一个行为。

---

## 15. What Does Rereading Mean?

综合 [B1]–[B11]，按任务 §8 的六种解释逐一给出证据强度。

### A. Evidence Retrieval（证据检索）
```text
Question → Passage → relevant region → Answer
```
- **证据**：[B11] 的 RBA 循环（page i → page i−k → page i → answer）正是该结构的直接实现，且与更高正确率相关（OR=1.28，控制后，p=.008）。[B3] 证明访问/重访**相关页**预测表现（高需求任务 β=0.51）。[B2] 中高表现的 PT43（长序列+revisit）支持「回读相关来源 = 获取关键证据」。
- **强度**：MODERATE。[B11] 的 RBA 定义是唯一直接操作化的证据检索回读；但它只证明「答题前回读页」与正确率相关，未证明「回读的是相关证据」。
- **我们的迁移**：`Q→P（相关段落）→Q→answer` 可视为 evidence retrieval 的**候选行为签名**，但需满足「回访区域与题目相关」。

### B. Verification（验证）
```text
tentative answer → reread → confirm / revise
```
- **证据**：间接。[B7] 的 final-response-review pause（最后答题→提交）被理论解释为「决定提交 + 监控目标达成 + 复查」（[B9] 同）。[B7] 发现静态格式下 final-review pause 更长且得分更高；作者对此给出「更审慎作答」的 **plausible explanation（需 future studies 验证）**——可靠结论是「提交前复查可能与更高得分相关，但时长方向无固定规则」。[B9] 把 `<move-to-target>` 事件对（答案修改）从 problem-solving pause 中排除——暗示答案修改是独立过程。
- **强度**：MODERATE（针对「提交前复查」，[B7]/[B9]）；**WEAK**（针对「选答案后回原文再回来未改」这一具体模式——B 组无直接研究，只能推断为监控/验证）。
- **我们的迁移**：`answer → passage → 回到题目（未改答案）→ 离开` 可以作为 verification 的候选，但需意识到 B 组没有直接证据支持「未改答案 = 已验证」。

### C. Strategic Rereading（策略性回读）
- **证据**：[B11] top-quartile 学生回读 motif 更常见（3→2、2→1、4→3、3→3 自环）。论文对回跳窗口 k≈4 的表述属**数据集特定（检测参数，非实验操纵）**，**不能推广为「短促回读最优」**；只能支持「有目的的回读与较高正确率相关」这一方向。[B8] 的 Thoughtful Search 簇（高表现、目标驱动）隐含目标导向的材料选择。[B6] 高理解者「routine task」——回读是其常规工作流的一部分。
- **强度**：MODERATE（[B11] 相关 + 理论重读研究 Thomas & Healy 2012；但无 think-aloud 确认意图）。
- **我们的迁移**：目标导向的回读（回读后立即答题且答案正确）可作为策略性回读的概率证据；[B11] 的 k 是检测窗口而非学生回读长度，**不能据此设定回读时长阈值**。

### D. Difficulty-Driven Rereading（困难驱动的重复阅读）
- **证据**：B 组**几乎没有直接证据**把回读与理解困难直接挂钩。[B2] 把短停留解释为「rush/skim」（非困难）；[B3] 低需求任务的多访问被解释为「不够 task-appropriate」而非困难。[B4] 提出 repeated look-back → struggling 的解释，但**同时给出互斥解释**。[B11] 承认回读可能 = 困惑/分心。
- **强度**：WEAK（理论合理但 B 组无直接验证）。
- **重要**：任务 §2 的「重复回读 ≠ 学生一定不理解」在 B 组证据中**被支持**——没有任何 B 组论文建立了回读 ↔ 困难的直接联系。

### E. Uncertainty（不确定）
- **证据**：[B4] look-back = 不确定的推断（无实证）；[B7] 更多 superfluous events/pause 在低表现者中？——不，[B7] 中下拉格式更慢更多事件但**得分更高**。B 组无直接证据把回读/复查与不确定性挂钩。
- **强度**：WEAK-UNSUPPORTED。
- **我们的迁移**：不确定性的可观测候选是「反复 Q↔P 切换 + 答案修改 + 终答前长时间复查」的组合，但这是**项目迁移推论**，B 组没有直接论文结论。

### F. Routine Task-Oriented Rereading（常规任务导向回读）
- **证据**：[B11] 中 39.6% 会话含 RBA——**回读是常见默认行为**，不是异常；[B3] 中学生在高需求任务中普遍增加访问（b=3.16）——回读是任务常规。[B6] 高理解者对数字阅读是「routine task」。
- **强度**：MODERATE。回读在 B 组数据中是**常态**而非异常信号，单独出现时信息量低。

### 总结判断：仅依靠 viewport / scroll / revisit sequence，可以区分到什么程度？

> **Reliable**：不能。没有任何 B 组论文支持仅靠 revisit 序列可靠区分六种状态。
>
> **Probabilistic**：可以做到的是——（1）「答题前回读」整体上更可能伴随正确作答（[B11] OR≈1.28，概率证据）；（2）回读**相关**区域 vs 无关区域有区分力（[B3]/[B6] 的 relevance 概念：precision 越高表现越好）；（3）回读的**时长/长度**有信息量（[B11] 短促最优；[B2] 长时间停留=高表现模式）；（4）回读的**位置**（答题前 vs 阅读中）改变含义（[B11] 强调 immediately preceding answer）。
>
> **Not distinguishable**：revisit 本身无法区分「策略性回读 / 困难驱动 / 不确定性 / 验证」，除非加入（a）before event（回读前发生了什么：刚答完题？读过几遍？）、（b）after event（回读后：直接答题？改答案？停留多久？）、（c）question context（该题需要的证据在回读区域内吗？）、（d）answer change（回读后是否改答案）。

**给系统的边界**：revisit 只能作为**概率性过程证据**（结合 [B11] 的方向 + [B3]/[B6] 的相关性编码 + [B9]/[B7] 的事件上下文），绝不能作为「confusion/difficulty」的确定性标签。

---

## 16. What Does a Pause Mean?

### 为什么「停留 10 秒」本身几乎没有认知意义？

[B9] 给出直接理论论证（p.264–266）：
1. pause 的定义只是「两个连续事件之间的时间」，**没有内容**。
2. pause 的认知内容由**事件对**决定：同一时长在「题目 onset→首次动作」（=编码+目标设定）、「两次答题动作之间」（=问题解决/检索）、「最后答题→提交」（=决定提交+监控复查）中含义完全不同（[B9] 图 2；[B7] 表 1）。
3. 250ms 以下是动作准备（ACT-R 最小动作时间），无认知意义（[B9]；[B8] 同）。
4. 长 pause 可能是深加工（[B7] 下拉格式更慢但得分更高——作者仅给 plausible explanation）、也可能是 off-task（[B9] 要求剔除离群长 pause）、也可能因练习效应而缩短（[B9]）。
5. 任务 affordance/结构决定 pause 含义（[B9]：不同任务结构下同一 pause 类型含义不同；[B7]：排序 vs 分类任务中同一反应格式的 pause 差异方向相反）。

**因此「停留 10 秒」没有任何独立认知解释力——它可能同时是检索、困惑、复查、发呆。**

### 加上事件上下文后，pause 才开始有认知解释

[B7] + [B9] + [B8] 给出了可辩护的 pause 类：

| Pause 类 | 定义（事件对） | 认知解释 | 证据 |
|---|---|---|---|
| 首段 pause / encoding | 题目/页面 onset → 首次动作 | 编码 + 目标设定（可能混入规划） | [B9] theory; [B8]（前置动作分布） |
| 信息检索 pause | 两次「作答相关动作」之间（[B7]）；或 `<drop-to-target, start-drag>`（[B9]） | 检索/比较/解决当前单元 | [B7] **experimental**（格式间系统差异）；[B9] OR=1.40→正确率 |
| 终答检查 pause | 最后答题事件 → 提交 | 决定提交 + 监控 + 复查 | [B7] **experimental**（格式间差异 + 更高得分关联）；[B9] theory |
| 导航/接口 pause | <250ms 或 <2.5s 的前置 | 动作准备/界面导航，无认知意义 | [B8]（剔除） |

[B8] 的关键补充：不同前置动作（plan/locate/evaluate）的 pause 分布显著不同（M=14.4s / 7.4s / 103.6s），pause 阈值（250ms/2.5s/10s/30s）与「pause 标签 + 上下文」共同估计生成 pause 的认知状态。

### Pause + Before-event + After-event + Task state + Location → Cognitive evidence？

- **论文结论**：[B9] 明确「不结合上下文无法对 pause 做有效认知推断」；[B7] 用受控实验证明 context-defined pause（信息检索、终答检查）在不同格式间系统差异；[B8] 用前置动作 + pause 类别建模。**这是论文结论**。
- **项目迁移推论**（B 组论文未直接验证的部分）：
  - 「passage→question 切换后、在题目上停留的 pause = 信息检索」——我们界面可类比 [B7] 的 information-retrieval pause，但 [B7] 的 pause 定义在**答题动作之间**，我们的题目是单次选择，需要把「切换回题目 → 选择选项」之间的事件对重新建模。
  - 「最后选择 → 离开题目」= 终答检查 pause（[B7] 直接类比）。
  - 「viewport 停在某段落 + 无交互 + 前面是切换过来」= 正在读该段落——**这是推论，B 组无 gaze 数据支撑**（见 Q7）。

### 结论
- raw dwell/pause：**不能**解释为任何认知状态。
- contextualized pause（信息检索 / 终答检查 / 首段编码 / 导航）：**有 MODERATE-STRONG 证据**（[B7] 实验 + [B9] 理论 + [B8] 方法）。
- 「长 pause = 困难」：**被 [B7] 可靠推翻固定方向**（更长 pause 也可伴随更高得分；作者对「审慎作答」的解释为 plausible explanation，非定论）——我们的系统必须避免「时长 → 认知状态」的固定映射。

---

## 17. Reading Process Theory

综合 [B3]/[B8]/[B10]（以及 [B5]/[B6] 的理论框架），B 组可支撑的阅读过程概念框架如下。**不强行制造固定状态机**——文献支持的是概念集，不是刚性状态图。

### 17.1 文献支持的 reading-process constructs

| Construct | 定义 | 支持来源 | 状态判断 |
|---|---|---|---|
| **task representation / task model** | 读者对任务目标与完成方式的心理表征（目标 + 计划） | [B10]（直接测量）；[B6]（RESOLV/MD-TRACE）；[B8]（MD-TRACE） | **相对稳定的 construct**（跨论文一致） |
| **goal formation** | 由指令/需求形成阅读目标 | [B10]；[B8]（search 反映目标生成与更新） | 稳定 construct；但**个体差异大**（[B10]） |
| **planning** | 选择信息来源与加工方式的计划 | [B10]（计划策略）；[B6]（问题解决中的规划） | 稳定 construct |
| **navigation** | 在信息空间中选择/访问/回避信息 | [B3]/[B5]/[B6]（access/discard）；[B8]（搜索） | 稳定 construct（B 组最常操作化的过程） |
| **information selection** | 判断相关性并选择 | [B3]（access demands）；[B6]（precision） | 稳定 construct（relevance 为核心） |
| **information retrieval** | 从记忆/文本提取所需信息 | [B7]/[B9]（信息检索 pause）；[B11]（回读） | 稳定 construct（[B7]/[B9] 有实验操作化） |
| **processing（文本加工）** | 理解、编码当前信息 | [B9]（编码/问题解决 pause）；[B10]（paraphrase/elaboration） | 稳定 construct |
| **integration** | 跨文本/跨段落整合 | [B10]（bridging）；[B6]（多源整合） | 稳定 construct |
| **evaluation** | 评估信息相关性/可信度 | [B8]（评估来源）；[B6]（评价技能） | 稳定 construct |
| **monitoring** | 监控理解与目标达成 | [B9]（最后 pause=监控）；[B10]（monitoring 过程）；[B5]/[B6]（adaptive processing=监控） | 稳定 construct（多来源支持） |
| **verification** | 确认/验证答案或理解 | [B7]（终答复查）；[B9]（提交前监控） | 稳定 construct（弱于 monitoring 的证据） |

### 17.2 哪些是「稳定 construct」，哪些只是特定研究的 operationalization？

- **稳定（多篇论文、多种操作化一致）**：task model / goal formation、navigation、information selection（relevance）、monitoring、integration、evaluation。这些在 [B3]（engagement→navigation）、[B5]/[B6]（skills→navigation）、[B8]（搜索策略）、[B10]（任务模型）中以不同方式出现且互相印证。
- **特定研究的操作化**：
  - Precision（[B5]/[B6]）与「access behavior」（[B3]）是 relevance/selection 的不同指标，不可混为一谈（前者是比值、后者是计数）。
  - Adaptive processing（[B5]/[B6]）= time-allocation-to-difficulty，是 monitoring 的**一种**操作化，不是 monitoring 本身。
  - 「task-adaptive navigation」（[B3]）= 行为与需求的匹配度，是统计交互而非直接测量。
  - information-retrieval / final-response-review pause（[B7]）= retrieval / monitoring 的事件对操作化，只在特定界面结构下成立。

### 17.3 对系统的含义
- 我们的行为词汇应映射到这些**稳定 construct**（navigation、selection、retrieval、monitoring、verification、integration），而不是发明新的认知层标签。
- 行为 → construct 的映射必须**逐层带证据边界**（§14 矩阵 + §15/§16 结论）。
- task model 不可直接观测：[B10] 证明同一指令产生不同任务模型 → 「question preview → 特定 goal」只能是概率推断，除非有任务模型测量（问卷/think-aloud 校准）。

---

## 18. Task-Type Differences

我们的英语阅读题未来可能包括：information locating、vocabulary in context、local inference、global inference、main idea、evaluation。B 组证据对「同一种 navigation/rereading 行为在不同题型下是否应有不同解释」的回答如下。

### 18.1 B 组可直接支撑的题型差异

1. **信息定位类（locating/retrieval）vs 推理/整合类（inference/integration）**：[B3] 的 access demands 是核心——「需要访问多少相关页」决定「访问/回读多」是必要集成还是多余动作。定位题低需求 → 多访问 = 不够 task-appropriate；整合题高需求 → 多访问 = 全面覆盖（β=0.51 vs 0.19）。**回读/导航量在同一学生、不同题型下含义不同**——这一条是 [B3] 的直接结论，可迁移。
2. **任务透明度（opaque vs transparent）**：[B6] 讨论区分「搜索引擎起点的开放任务（需要导航精度，问题解决技能起补偿作用）」vs「明确书目任务（加性模型）」。→ 信息定位/搜索类题（需要学生自己判断去哪找）与「文中某句直接可答」题（透明）中，navigation 的含义不同。
3. **排序 vs 分类（[B7]）**：同一反应格式在不同任务类型产生相反过程指标。虽然 [B7] 是反应格式研究，但它证明**任务类型改变过程的观测形态**——我们的题型若涉及「排序/匹配」类题，pause/事件指标不能与标准 MC 题共用解释。
4. **答题前回读（[B11]）**：只对 open-book 立即答题情境有证据；闭卷/记忆题无证据（论文自认）。

### 18.2 需进一步区分的题型（B 组不足）

- vocabulary in context、main idea、evaluation 题型的**导航/回读差异**：B 组没有任何论文按题型细分这些。（[B7] 区分的是任务类型排序/分类而非阅读认知目标；[B10] 的四种指令接近但那是学习任务不是阅读题。）
- **结论：对 information locating / integration 类题，「导航/回读量 × 题型需求」有 MODERATE 证据（[B3]）；对 vocabulary/main idea/evaluation，INSUFFICIENT EVIDENCE。**

### 18.3 给系统的边界
- 必须为每题标注「证据需求」（哪些段落/区域含该题所需证据）——这是 [B3]/[B6] 的 relevance coding 前提，否则无法解释访问/回读。
- 同一行为特征（如回读次数）**不得**跨题型共用一套认知标签；至少按「证据需求高低」「任务透明度」「题目类型」分层。

---

## 19. Individual-Difference Moderators

重点综合 [B3] / [B5] / [B6]（外加 [B11] 的能力调节）。**只有论文真正支持时才写。**

### 19.1 有直接证据的调节器

| Behavior | Student characteristic | 调节方向 | 支持论文 | 证据类型 |
|---|---|---|---|---|
| 访问/回读相关页（Precision、access behavior） | **阅读理解技能** | 好理解者：更精确选择相关页、丢弃无关页；理解技能经「策略知识→导航」路径作用（完全中介），另有独立直接路径 | [B5]（策略知识被导航完全中介）；[B6]（CS→Precision b=0.32） | CORRELATIONAL（路径模型，19/32 国） |
| 导航精确度（Precision） | **问题解决技能 × 理解技能（补偿性交互）** | 低理解者：问题解决技能更预测导航精度（斜率更陡）；高理解者：问题解决作用弱。→ 高能力学生频繁导航可能是 adaptive；低能力学生相同行为可能反映 inefficient search 但有问题解决补偿 | [B6]（CS×PS→Precision b=-0.08，序数交互） | CORRELATIONAL（32 国 meta） |
| Adaptive processing（时间×难度匹配） | 理解技能、问题解决技能 | **无交互**：时间分配被两种技能加性预测——时间调节是元认知原型，两种技能独立贡献 | [B6]（交互 n.s.） | CORRELATIONAL |
| 答题前回读（RBA） | **先前英语能力** | 中/高能力组 RBA 获益 8–12pp，低能力组 3–5pp；控制能力后 RBA 仍显著 → 独立于能力但获益大小随能力变化 | [B11] | CORRELATIONAL（控制混杂） |
| 任务访问行为 | **信息型/社交型在线阅读投入（习惯）** | 高信息型投入者更 task-adaptive（高需求任务多访问、低需求任务节制）；高社交型投入者在低需求任务做得过多 | [B3] | CORRELATIONAL（17 国 meta） |
| 任务模型构建 | **个体解释/先验知识** | 同一目的指令 → 不同任务模型 → 不同过程与结果；先验知识（前测 β=.34）预测结果 | [B10] | think-aloud + correlational |
| 导航模式 | **性别 / SES** | 同一模式（长序列短时）女生更高分、男生疑似 aimless switching；SES 低学生更多有限导航 | [B2] | CORRELATIONAL |

### 19.2 证据边界
- 「高能力学生频繁 navigation 是 adaptive，低能力学生是 inefficient search」——**[B6] 支持其机制**（补偿性交互使问题解决在低理解者中更强预测导航），但 B 组没有一篇论文在同一界面同时测行为与理解技能并直接显示「同一行为的含义按能力翻转」。
- 「同行为、不同学生、不同含义」最干净的证据是 **[B2] 的性别效应**（同一模式不同成绩）与 **[B11] 的能力调节**（同一回读不同获益）。
- [B4] 的 look-back 歧义（struggle vs confident）**没有**能力调节证据，只能作为「含义多重」的存在性提示。

### 19.3 给系统的边界
- 我们的模型**必须**包含能力/理解水平的调节项（否则「navigation 多 = 好还是差」无解）。
- 至少三个调节维度有 B 组证据：**理解技能**（[B5]/[B6]）、**问题解决技能**（[B6]）、**先前英语能力**（[B11]）。
- 「行为 → 过程意义」的映射应在**能力分层**内定义（低/中/高），而不是单一全局规则。

---

## 20. Candidate Reading Action Vocabulary

根据 B 组结果提出**有文献依据的候选行为词汇表**（只定义 Behavior/Action，不定义 cognition）。每个 action 给 Definition / Required raw events / Supporting papers / Confidence。认知层标签（EVIDENCE_SEARCH、CONFUSION、UNDERSTANDING）**不进入**本词汇表。

| Action | Definition | Required raw events | Supporting papers | Confidence |
|---|---|---|---|---|
| **QUESTION_PREVIEW** | 首次进入题目区、浏览题目后返回文章（或未读文直接答题） | question_navigated 序列；首次 question 访问时间 | [B10]（task model 理论）；[B3]（任务需求适应） | WEAK（theory-supported 假设：可能反映 task orientation，但形成何种 goal/plan 不可从 preview 恢复——[B10] 组内差异） |
| **PASSAGE_FIRST_PASS** | 文章首次顺序滚动/阅读到末尾 | 首次 passage 访问 + 滚动范围覆盖全文 | [B9]（首段编码类比）；[B2]（T3 模式） | WEAK（无法确认在读） |
| **PASSAGE_FORWARD_NAVIGATION** | 视口前进式移动 | scroll/scroll_end 前进事件 | [B2]（T1 skimming 类比） | WEAK |
| **PASSAGE_BACKTRACK** | 视口后退式移动 | 后退 scroll/scroll_end | [B11]（回读）；[B4]（look-back）；[B3]（重访） | MODERATE（概率方向：回读→更好成绩） |
| **PARAGRAPH_REVISIT** | 重新回到之前已访问过的段落 | 段落级 viewport 重叠记录（再次命中） | [B11]；[B3]；[B6]（precision） | MODERATE（结合相关性/时长/前后事件才增强） |
| **QUESTION_TO_PASSAGE_SWITCH** | 题目区 → 文章区（可能=信息检索） | question→passage 转移事件 | [B11]（RBA）；[B7]（tab 切换设计）；[B9] | MODERATE |
| **PASSAGE_TO_QUESTION_SWITCH** | 文章区 → 题目区 | passage→question 转移事件 | [B11]；[B7] | MODERATE |
| **INFORMATION_RETRIEVAL_PAUSE** | 两次作答相关动作之间的暂停（或切换回题目后、作答前的暂停） | 事件对：`question_navigated→answer_option_clicked` 或两次答题动作；duration | [B7]（experimental）；[B9]；[B8] | MODERATE（[B7]/[B9] 支持定义；我们界面的具体事件对需建模） |
| **RESPONSE_REVIEW_PAUSE** | 最后作答动作 → 离开题目/提交之间的暂停 | 事件对：`answer_option_clicked→question_navigated`；duration | [B7]（experimental）；[B9] | MODERATE |
| **ANSWER_SELECT** | 选择一个选项 | answer_option_clicked | [B7]（选择=response event） | STRONG（选择本身可观测） |
| **ANSWER_REVISE** | 修改已选答案 | answer_option_clicked（对已作答题目再次点击不同选项） | [B9]（`move-to-target` 排除处理）；[B7]（superfluous events） | WEAK-MODERATE（含义多重：审慎 vs 不确定） |
| **UNDERLINE_COMMIT** | 在文章上划线/高亮 | underline_created / text_selection_committed | **无 B 组论文** | UNSUPPORTED BY GROUP B（不进入强证据层） |
| **OPTION_ELIMINATE** | 划掉/恢复选项 | option_elimination_toggled | **无 B 组论文** | UNSUPPORTED BY GROUP B（不进入强证据层） |

### 20.1 使用约束
1. 本词汇表**只含可观测动作**；`EVIDENCE_SEARCH`、`CONFUSION`、`UNDERSTANDING` 属于认知层，禁止放入 Action Vocabulary。
2. **ANSWER_REVISE 与 UNDERLINE/ELIMINATE 的认知含义在 B 组无强证据**——它们可以记录、可以建模，但不能预置「修改=不确定」「划线=证据标记」等标签。
3. 每个 action 需要**对应的 raw event 组合**（见 Definition 列），不能用一个近似事件替代（如用 scroll_end 代替 viewport 段落归属——见 Q7）。
4. Confidence 会随加入「before/after event、question context、answer change」而提高（§15/§16 结论）——词汇表应该输出的是**带上下文的事件对**，而非孤立动作。

---

## 21. What Is an Effective Action in Reading?

回答 A+ 组留下的「effectiveness 从哪来」问题（A+ 结论：距离/概率/reward 都以「任务有可判定的成功」为前提，阅读需要 B 组给出证据）。

### A. Distance-to-goal（A+2 路线）

**阅读有没有稳定的 target state？** B 组证据：
- 阅读任务没有「最优路径状态」的可辩护定义。[B2] 的 PT43（多页+长时）表现最好，但 [B3] 证明「访问相关页」的意义随 access demands 变化；[B6] 证明任务透明度改变导航-表现关系——**同一个「状态」（如访问了某页）在不同任务下对目标的距离不同**。
- 例外：**证据定位题**可能有近似的 target state（找到含答案的段落）。此时「访问了相关区域」≈「到达目标附近」。但 B 组没有论文为阅读任务定义目标态图。
- **结论**：distance-to-goal 在阅读中**不通用**；仅在「证据定位类题型 + 事先编码相关区域」时可能局部适用（这需要我们自己定义，B 组无直接支持）。

### B. Probability of Correct Answer（A+1 TEM 路线）

`P(correct | 到达某状态)` 是否适用？
- **优点**：B 组提供了行为状态 → 正确率的相关证据：[B11]（答题前回读 → 更高正确率 OR=1.28）；[B3]（访问相关页 → 更高任务表现，交互由需求调节）；[B6]（Precision/Adaptive processing → 数字阅读，路径系数）。这些与 A+1 的「到达状态后的答对率」同构——**如果状态 = 「访问了相关区域 / 答题前回读了 / 复查了」**。
- **outcome-derived effectiveness**：[B11]/[B3]/[B6] 的「有效行为」全部由最终成绩定义 → 正是 A+1 的 outcome-derived effectiveness，直接继承 A+ 指出的两层风险。
- **construct circularity**：若用同一批学生估计「回读→答对概率」再反过来衡量这些学生 → 循环。B 组论文**没有**做样本外验证（[B11] 是观察性回归，[B3]/[B6] 是相关/路径）。
- **student ability confounding**：[B11] 明确显示先前能力是最强预测（OR=1.77）——「回读学生的更高正确率」可能部分因为高能力学生更爱回读；[B11] 控制能力后 RBA 仍显著（OR=1.28），是 B 组中处理该混淆的最好例子，可作为模板。
- **task dependence**：[B3] 证明「访问相关页 → 答对率」的系数随 access demands 变化（β 0.51 vs 0.19）；[B7] 证明同一反应格式在不同任务中过程指标方向相反。→ **P(correct|state) 必须分题型标定**。

### C. Theory-Defined Relevance / Evidence（理论定义的相关性）

能不能用阅读理论把「relevant paragraph / critical evidence / necessary source」定义为有效行为？
- **可以，且 B 组已经在这么做**：[B3]/[B6] 的「相关页」专家编码（必需信息/有帮助/导航必需）；[B8] 的来源质量编码（high/medium/low 由任务设计意图定义）；[B6] 的 Precision 就是把「相关页访问」作为有效性指标。
- **需要的 ground truth**：每个题目的「相关段落/区域」标注（专家/任务设计）——这是 [B3]/[B6] 的前提，我们的系统**必须**具备；否则 relevance 类指标无法计算。
- **限制**：[B3] 显示访问「相关」页也有边界（低需求任务多访问仍正相关但意义弱）；B 组没有「把相关区域访问定义为有效性」的测量模型验证。

### D. Reward / Value（A+5 路线）

阅读中 reward 能否合法定义？
- **如果 reward 最终来自「答对」**：与 B 路线无实质区别——只是把 `P(correct|state)` 换成累计 reward；A+5 的「构造循环」风险同样存在。B 组没有任何独立于成绩的 reward 来源。
- **能否有独立于答对的过程 reward？** B 组线索：
  - [B6] 的 Adaptive processing（时间匹配难度）是**过程质量指标**，不直接依赖答对——可视为「监控质量」的 reward 候选。
  - [B8] 的「信息需求敏感性」（剩余点数 vs 是否回访）是**目标导向**指标。
  - [B10] 的任务模型成分（重读计划、写作目标）预测结果——但那是自陈，不是日志 reward。
  - 但这些都是**相关**证据，没有一篇论文验证「过程 reward → 能力」的测量模型。
- **结论**：阅读中目前**没有可辩护的、独立于答对的过程 reward**；若用答对做 reward，与 B 路线实质相同，需直面 circularity。

### 21.1 B 组对 effectiveness 问题的最终回答
1. **最可辩护的定义 = 理论定义的相关性（C）为主 + 答对概率（B）为校准**：先由任务设计标注「相关区域」（C，[B3]/[B6] 已验证可操作），再把「访问/回读相关区域后的答对概率」作为经验有效性（B，[B11]/[B3] 提供方向证据）。
2. 必须**分题型**标定（[B3] access demands；[B6] 任务透明度；[B7] 任务类型）。
3. 必须**控制能力**（[B11] 模板）。
4. 必须**样本外/独立校准**以缓解 construct circularity（B 组未做，留给 Group E）。
5. distance-to-goal（A）与 reward（D）在阅读中**缺乏定义前提**，不宜作为主路线。

---

## 22. Twelve Cross-Paper Research Questions

### Q1. 阅读领域是否存在足够稳定的 Reading Process Framework 来解释行为序列？
**是，且不止一个**：MD-TRACE / RESOLV（[B6]/[B8]/[B10]，任务模型 + 信息检索/评估/监控循环）、Guthrie 投入模型（[B3]，投入→导航→表现）、IPS-I 信息问题解决（[B6]）、文档模型框架（[B10]）。这些框架为「行为序列 → 过程」提供概念锚点。**但**：框架是描述性的，B 组没有把它们转成可操作状态机；「把策略映射到认知理论」被 [B2] 作者列为未来工作。→ **框架稳定，操作化待建。**

### Q2. 哪些行为最可能作为 information retrieval 的可观测证据？
**答题前回读相关区域（[B11] RBA，OR=1.28）+ question→passage 切换 + 信息检索 pause（[B7]，experimental）**。三者组合（切换→停留→回读→作答）是最可辩护的 retrieval 行为签名。单独任何一项都是概率证据。

### Q3. 哪些行为最可能作为 verification / monitoring 的证据？
**终答前复查（[B7] final-response-review pause，experimental；[B9] 最后 pause=监控）+ 选答案后回原文再回来（推断）**。[B7] 的 process-product 分离表明「时长无固定方向」——更长复查也可伴随更高得分（「更审慎」为作者 plausible explanation）。Adaptive processing（时间×难度）是 monitoring 的另一操作化（[B6]）。

### Q4. 有没有行为能可靠表示 comprehension difficulty？
**没有可靠指标；只能概率推断**。B 组没有任何行为被验证为 difficulty 的可靠标志：更长 pause 与困难无固定对应（[B7]：时长无固定方向）；更多回读 ≠ 困难（[B11] 反向相关 + [B4] 歧义）；更多导航 ≠ 困难（[B3] 任务依赖）。**「困难」在 B 组证据中是最难从行为推断的状态之一。**

### Q5. revisit 本身的信息量多少？加入 before/after/question/answer-change 后是否增强？
**单独信息量低**（revisit 六种互斥解释，§15）。**加入上下文后显著增强**：答题前回读 + 回读相关区域 + 回读后不改答案 → 更可能是策略性验证（[B11] 回读与更高正确率相关、[B3] 相关页、[B7] 复查）；回读后长时间停留 + 修改答案 + 无关区域 → 更可能是困难/不确定（项目迁移推论，部分由 [B9] 的事件对排除逻辑支持）。B 组证据支持「上下文增强」这一方向，但增强后的区分度仍是**概率性**。

### Q6. pause/dwell 本身的信息量多少？contextualized pause 是否明显优于 raw duration？
**raw dwell 信息量极低（[B9] 理论：无内容）；contextualized pause 明显更优（[B7] experimental 证明 context-defined pause 在格式间系统差异；[B8] 证明前置动作分布不同）**。结论明确：只可用事件对 pause，不可用 raw duration。

### Q7. 能否仅根据 scroll + viewport 判断学生在读哪个 paragraph？
**不能**。B 组没有论文研究 gaze/focus；所有论文都承认 viewport/页面访问 ≠ 注意（[B2] 时间聚类无法区分阅读/重读/暂停/略读；[B9] 强调任务状态而非视觉）。viewport 只提供「某段落处于可视区域」的证据，不是「在读」。**必须明确说不能。**

### Q8. navigation strategy 与 reading ability 的关系是稳定的吗？还是被 task/ability/strategy knowledge 调节？
**被调节，不稳定**：[B3]（access demands 调节导航-表现）；[B5]（策略知识被导航完全中介、理解技能独立预测）；[B6]（理解 × 问题解决补偿性交互、任务透明度调节）；[B11]（先前能力调节 RBA 获益）。→ 单一「导航策略 ↔ 能力」关系不存在；必须按任务需求与个体差异分层。

### Q9. 哪些行为变量适合跨 passage 泛化？哪些高度 task-specific？
- **可泛化（结构性指标）**：事件对 pause 类（信息检索/终答检查——[B7]/[B9] 在不同任务/格式均成立）；Q↔P 切换结构（[B11]/[B7] 语义相似）；答题前回读（[B11] 跨 56 个单元成立）；终答复查。
- **task-specific（需每题标定）**：访问/回读相关区域的**量**（[B3] access demands 每题不同）；Precision 指数（需每题相关区域编码，[B3]/[B6]）；Adaptive processing 的时间-难度匹配（难度需每题可得）。

### Q10. 是否足够证据建立 Behavior → Reading Skill？还是只能 Behavior → Reading Process Evidence？
**分两个层面回答，不互相覆盖**：
- **B 组层面**：只能到 Reading Process Evidence。B 组所有「行为→成绩」都是相关性（[B2]/[B3]/[B4]/[B11]）或路径模型（[B5]/[B6]），没有任何论文建立「行为 → 长期阅读技能」的强预测/因果链路；[B6] 最接近（理解/问题解决技能 → 导航 → 数字阅读），但技能是输入而非输出。
- **A/A+ 层面**：A/A+ 已在统计测量层证明「process sequence + effectiveness/skill mapping → latent trait / multidimensional ability」的数学机制可以运行。
- **综合结论**：B 组没有证明某种阅读行为能被直接解释成某项 reading skill；A/A+ 提供了「从经过定义的过程证据估计 latent ability」的统计模型。两者之间 **Reading Process Evidence → 具体技能构念（information locating / inference skill 等）的 construct-validity 桥梁仍然缺失——这是 E 组的核心任务**。系统现阶段应把行为映射到「过程证据」，技能解释必须由该桥梁支撑，不能跳过。

### Q11. A+ 的 action effectiveness 在阅读任务中最可辩护的定义是什么？
**理论定义相关性（C）为主 + 答对概率（B）为校准，分题型标定 + 控制能力 + 样本外验证**（详见 §21.1）。distance/reward 路线在阅读中缺乏定义前提。

### Q12. 不用 LLM/Agent，仅从英语阅读 process data 出发，当前最可靠能恢复到哪一层？
| 层 | 可恢复性 | 依据 |
|---|---|---|
| Observable behavior | ✅ 完整恢复 | 日志直接给出（§20 词汇表） |
| Reading strategy | ⚠️ 概率性恢复（规则定义 + 数据挖掘簇 + 事后解释） | [B11] RBA 规则；[B8] mHMM 簇；[B1] FOMM；[B2]/[B4] 聚类 |
| Reading process | ⚠️ 概率性恢复（需事件上下文） | [B7]/[B9] pause 类；[B11] 回读；[B6] precision/adaptive |
| Cognitive state | ❌ 不可靠（困难/不确定/困惑尤其不可靠） | [B7] 反驳 dwell=困难；[B4] 歧义；Q4 |
| Reading skill | ⚠️ 不能从行为直接输出；需经 A/A+ 统计层（effectiveness/skill mapping → latent trait）+ E 组构念效度桥梁 | Q10 |

**最可靠可恢复**：observable behavior（确定）+ contextualized reading-process evidence（概率性、分题型/分能力）。**最不可靠**：difficulty/uncertainty 等认知状态与任何技能结论。

---

## 23. What Group B Establishes

### Strong Evidence（至少满足：受控实验 / 直接过程验证 / think-aloud 对齐 / 多独立研究）

1. **pause 必须带事件上下文才有认知解释**（[B7] 受控实验 + [B9] 理论建模 + [B8] 方法）；raw dwell 不能单独解释任何认知状态。
2. **同一行为在不同任务类型/任务需求下含义不同（moderation）**（[B3] access demands 交互 17 国 + [B7] 任务类型实验 + [B6] 任务透明度讨论）。
3. **时长的认知意义没有固定方向**——[B7] 显示更长 pause、更多交互可伴随更高得分，可靠推翻「长 pause = 困难」的固定映射（作者对「更审慎/更受控作答」的解释为 plausible explanation，明确需 future studies 验证，**不能反向确立「长 pause = 审慎」**）。
4. **理解技能是导航-表现关系的关键个体差异调节器，且与问题解决技能补偿性交互**（[B6] 32 国 meta；[B5] 路径模型）。
5. **策略知识对数字阅读的作用被导航完全中介**（[B5]）。
6. **task model（目标+计划）直接测量可行，且同一指令产生不同任务模型、任务模型成分预测阅读过程**（[B10] think-aloud，κ 可靠）。

### Partial Evidence（一致的相关证据 + 强理论，但缺实验/直接验证）

7. **答题前回读（RBA）与更高正确率相关，且独立于时间/序列长度/先前能力**（[B11] 控制混杂；OR≈1.28）——**MODERATE**：observational + conference proceedings + 无 rereading 的随机操纵 + 无 think-aloud/gaze 验证意图；论文自认 page revisit 也可能 = confusion/distraction。可支持「RBA-like pattern → 与较高正确率相关」，**不能支持「RBA → 一定是 strategic evidence retrieval」**。
8. 相关页访问/重访与表现的关联随需求变化（[B3]/[B6]：Precision、access behavior）——方向一致但全部相关。
9. 导航模式聚类可预测成绩（[B2]/[B4]/[B8]）——模式稳定、解释事后。
10. 事件对 pause（信息检索/终答检查）在不同格式间系统差异且与表现关联（[B7]）——指标本身可靠，认知归因仍间接。
11. 行为-成绩关系被性别/SES/先前能力调节（[B2]/[B11]）。
12. trace 频率与自陈 SRL 汇合验证（[B1]）——行为指标可辩护的一种验证路径。

### Unsupported / Still Open（B 组无证据或证据不足）

13. **underline/highlight 的认知含义**——UNSUPPORTED BY GROUP B（[B11] 记录未分析；[B10] 标注计划与 elaboration 负相关）。
14. **option elimination 的认知含义**——UNSUPPORTED BY GROUP B。
15. **answer change 的认知含义**（monitoring vs uncertainty）——B 组无直接研究，只有 [B9] 的事件对排除逻辑暗示它是独立过程。
16. **difficulty/uncertainty/confusion 的可靠行为标志**——不存在（Q4）。
17. **行为 → 阅读技能的直接解释**——B 组无证据；A/A+ 提供「过程证据 → latent trait」的统计机制，但「过程证据 → 具体技能构念」的 construct-validity 桥梁缺失（Q10，E 组核心任务）。
18. **独立于答对的过程 reward / distance-to-goal**——缺乏定义前提（§21）。
19. **「viewport/scroll → 正在读某段落」**——无 gaze 数据支撑（Q7）。
20. **跨题型的行为标签统一**——被 [B3]/[B6]/[B7] 反驳（必须分题型）。

---

## 24. Inputs Needed From Group C

**Group C 固定定义（研究计划，与 A 组报告 §9 一致）**：Mouse / Cursor → Attention / Intent——验证鼠标/光标轨迹能否作为注意与意图的代理。

B 组在阅读领域**无法直接提供**「cursor → attention」的证据（本报告 Q7 已明确：B 组没有任何论文研究 gaze/focus，viewport/页面访问 ≠ 注意，viewer 停在某段落 ≠ 在读该段落）。因此本节的输入主要是需求与边界：

1. **cursor/pointer 与注意一致性的实证**：B 组需要 C 组验证「在左 passage + 右题目的阅读任务中，cursor-position / hover 与注视/注意的一致程度、什么条件下失效」。这是 B 组 revisit/dwell 指标能否从「视口可见」上升到「注意」层的**决定性前提**。若 C 组证明 pointer 在阅读任务中近似注意，[B11] 的「答题前回读」、[B3]/[B6] 的「相关区域访问」可获得注意锚点；若不能，B 组行为指标停留在视口层。
2. **scroll 行为的认知解释验证**：B 组给出需 C 组用鼠标/光标数据验证的 scroll 假设——[B2] 把短停留解释为 skimming/rush（事后解释）；[B8] 把滚动折叠为低层事件、明确「不携带目标证据」。C 组需验证 scroll 速度/方向/回滚在阅读中携带多少认知语义，能否作为「证据检索」的行为指标。
3. **pointer 事件去噪与采样标准**：B 组 pause 指标（[B9] 250ms 下限、[B8] 2.5s/10s/30s 分档）依赖干净的事件时间戳；C 组需给出抖动、采样频率、噪声的处理标准，供 D 组 Action Segmentation 使用。
4. **hover/悬停语义**：B 组无证据。若 C 组证明悬停在阅读任务中携带相关性判断语义，可为「相关区域关注」提供行为代理，反哺 B 组的 revisit 解释（§15）。

---

## 25. Inputs Needed From Group D

**Group D 固定定义（研究计划，与 A 组报告 §9 一致）**：Raw Event → Action / Activity Segmentation——从 scroll/pointer/viewport 原始事件流中切出「读段落 / 找信息 / 作答 / 消去选项」等语义动作块。

B 组为本层的**语义定义**提供主要输入（§20 候选行为词汇表本身就是 D 组动作词汇的候选），D 组负责**分割方法与验证**：

1. **语义动作块的界定依据（B 组已提供，D 组需算法化）**：[B9] 的事件对（event pair）定义——哪些相邻事件构成「信息检索 pause」「终答检查 pause」等语义块，哪些事件对（如答案修改）应被排除；[B8] 的低层事件折叠规则（scroll 位置、按键在首次出现时折叠为该活动起点）；[B7] 的「为过程数据而设计」原则（story/questions 分屏以区分阅读时间与答题时间）。
2. **分割边界与粒度的验证**：D 组需验证在阅读场景下「raw scroll/pointer/viewport 流 → 读段落/找信息/作答动作块」的边界怎么定、粒度怎么选（A 组 §9 D1）。B 组给出语义候选（revisit、Q↔P 切换、retrieval pause），D 组验证这些语义块在数据中是否稳定可切、粒度改变是否改变语义（[B9] 的粒度讨论是模板）。
3. **micro action → task state 的自动化**：[B5]/[B6] 的 Precision/Adaptive processing 依赖「相关区域访问」状态；D 组需提供「已看关键句 / 已访问相关区域」这类信息状态在阅读场景下的自动构造与稳定性证据（A 组 §9 D2）。
4. **动作词汇的构建与裁剪**：§20 是 B 组交付的动作词汇候选；D 组负责低频处理、同义合并、与 pause 阈值（[B9] 250ms、[B8] 2.5s/10s/30s）配套的词汇粒度裁剪。
5. **语义标注与日志规范（分割的前置输入）**：D 组的 raw event → semantic action 依赖一组语义标注，B 组列出最低要求——每题「相关段落/区域」标注（[B3]/[B6] relevance coding 前提）、题目难度（[B5]/[B6] Adaptive processing 前提）、每题「证据需求」/access demands 类比（[B3] 交互模型输入）、题型分类（locating / inference / main idea / evaluation，§18 分层前提）；日志须能重建「事件对」（答题事件之间、答题→离开、切换→作答）以计算 context-defined pause（[B7]/[B9]），且 viewport 段落归属需段落级坐标、不能只用 scroll 事件（Q7）。

---

## 26. Inputs Needed From Group E

**Group E 固定定义（研究计划，与 A 组报告 §9 一致）**：Process Evidence → Cognitive Diagnosis + Construct Validity——把过程证据映射到认知诊断/阅读技能，并验证其构念有效性。

B 组交付的「行为 → 阅读过程证据」是 E 组的输入边界；E 组负责「过程证据 → 技能/认知诊断」及构念效度：

1. **（核心任务）「过程证据 → 具体技能构念」的 construct-validity 桥梁**：B 组交付「行为 → 阅读过程证据」（§22 Q10/Q12），A/A+ 交付「过程证据 → latent trait」的统计机制；但「这段过程证据真的是 information locating / inference skill 吗」未被验证。E 组需建立该桥梁（criterion 关联、think-aloud/eye-tracking 校准、独立技能测验对照），否则 skill 层结论无构念支撑。
2. **Q-matrix 式「行为 × 阅读技能」映射的效度**：A1 的 I⁺ 是 Q-matrix 的过程版（A 组 §9 E1）。B 组提供「哪些阅读行为值得进入有效性/技能映射」的行为学依据（revisit、retrieval pause、relevance 编码等，§14/§20），E 组负责该映射的建立与验证（专家 vs 数据驱动、识别性检验）。
3. **latent state/class 构念有效性的验证框架**：B 组确认行为只能到「过程证据」层；E 组需用外部测量（阅读测验分数、教师评定、眼动）验证估计的潜在状态/能力确实是「阅读认知」而非「界面操作熟练度」（A 组 §9 E2）。
4. **能力与策略分离**：B 组显示同一行为在不同能力学生身上含义不同（[B6] 补偿性交互、[B2] 性别差异、[B11] 能力调节）；E 组需提供统计方法（scale anchoring、能力-类别联合建模）区分「低技能」与「不同策略」（A 组 §9 E3）。
5. **新任务泛化效度**：如何在少量新 passage 上验证「状态定义规则 + 技能映射」的稳定性（A 组 §9 E4）。B 组的 relevance 编码（[B3]/[B6]）每篇需重新标注，跨 passage 的测量等价性需 E 组验证。
6. **样本外/独立校准**：缓解 outcome-derived effectiveness + construct circularity（A+1 风险；B 组论文全部无样本外验证）。
7. **能力/先前水平测量作为效标**：B 组显示先前英语能力是行为-成绩关系的最强调节/混杂（[B11] OR=1.77、[B6] 理解×问题解决、[B5] 理解技能），E 组构念效度检验需要至少一个独立能力/水平测量作为 criterion（外部阅读测验、分班成绩等），否则无法区分「行为反映技能」与「行为反映界面熟练度」。

---

## 27. Evidence Index

所有影响项目设计的重要结论及其定位。页码基于本地 PDF 逐页核对；期刊论文引用**印刷页码**（如 [B3] 印刷页 269=PDF 页 7、[B2] 印刷页 728=PDF 页 10），无页码的会议论文（[B4]/[B5]/[B11]）用章节名定位。

| Conclusion | Paper | PDF Page | Section / Table / Figure |
|---|---|---|---|
| Pause 必须结合前后事件才有认知解释 | [B9] | p.264–266 | Introduction / Step 1–2 |
| 250ms 是认知有意义 pause 的下限（动作准备） | [B9] | p.266 | Step 2; [B8] p.14–15 |
| 信息检索 pause（两次答题事件之间）与终答检查 pause（最后答题→提交）定义 | [B7] | p.6 | §2.4.2; Fig. 2 |
| 排序任务中 D&D 减少 superfluous 事件/时间/两种 pause；下拉得分反而更高（process-product 分离） | [B7] | p.6–8 | §3.1; Tables A2–A3 |
| 分类任务中 D&D 无优势、点网格更优（任务类型调节） | [B7] | p.7–8 | §3.2 |
| 时长/交互量认知意义无固定方向；更长 pause 可伴随更高得分（「审慎」为作者 plausible explanation，需 future studies 验证） | [B7] | p.9 | §4 Discussion |
| 访问/回读相关页的次数预测表现，由 access demands 调节（高需求 β=0.51 vs 低需求 β=0.19） | [B3] | p.273–274 | Table 4, Table 5; Fig. 3 |
| access demands → access behavior b=3.16（学生普遍适应任务） | [B3] | p.269 | §3.1.2.1 |
| 信息投入者更 task-adaptive；社交投入者低需求任务做过多 | [B3] | p.270–271 | Tables 2–3 |
| 访问相关页在印刷技能之上预测数字阅读 b=0.35 | [B3] | p.273 | §3.2.2.3 |
| 导航（Precision）→ 数字阅读 b≈0.39；Adaptive processing b≈0.15 | [B6] | p.11 | Table 5 |
| 理解×问题解决对 Precision 补偿性交互 b=-0.08；对 Adaptive 无交互 | [B6] | p.9 | §3.2; Table 3 |
| 问题解决在理解之上预测数字阅读 b=0.31；交互 b=-0.05 | [B6] | p.10 | §3.3–3.4; Table 4 |
| Precision 中介理解 b=0.12 / 问题解决 b=0.10 / 交互 b=-0.03 | [B6] | p.11–12 | Table 6 |
| 策略知识对数字阅读被导航完全中介（b=0.15 间接）；理解技能直接 b=0.17 | [B5] | p.「Results」 | Model 3 参数 |
| 页面与时间导航聚类均显著预测阅读分（论文 η²=.11/.25 疑误，按 F、df 反算约 1.1%/2.5%，不采信）；PT43 vs PT14 差 55 分 | [B2] | p.728–729 | Table 1; Fig. 6 |
| 性别/SES 调节导航模式-成绩关系 | [B2] | p.730–731 | Fig. 7; §3.3 |
| 时间序列无法区分阅读/重读/暂停/略读 | [B2] | p.733 | §Discussion limitation 3 |
| RBA 循环 ~10pp 原始 / ~6pp 控制后获益（OR=1.28, p=.008） | [B11] | p.「Results」 | §3.1–3.2; Fig. 3 |
| 先前能力最强预测（OR=1.77）；RBA 获益随能力变化（低能力 3–5pp） | [B11] | p.「Results」 | §3.2; Fig. 5 |
| 回跳窗口 k≈4 捕获多数相关模式（数据集特定，非实验结论） | [B11] | p.「Results」 | §3.3 |
| 日志推断风险：回读可能是困惑/分心 | [B11] | p.4 | §Discussion Limitations |
| 导航活动与 NAEP 成绩 r=0.423；look-back 多重互斥解释 | [B4] | p.「Results」/「Implications」 | RQ2; §5.1 |
| pause 阈值 250ms/2.5s/10s/30s；前置动作依赖分布（plan 14.4s/locate 7.4s/evaluate 103.6s） | [B8] | p.14–15 | Fig. 3; §Process Data Representation |
| 4 簇搜索行为；簇1 与总任务分 r=0.310、簇2 r=-0.325；簇1 对信息需求更敏感 | [B8] | p.26–28 | Tables 4–5, 7 |
| 事件选择由认知理论指导（Raw→Semantic Event 模板） | [B8] | p.13–16 | §Process Data Representation |
| 目的指令不预测阅读过程；任务模型成分预测（重读计划→bridging β=.29、后测 β=.26） | [B10] | p.8–9 | Tables 6–7 |
| 同一指令 → 不同任务模型（组内变异）；先验知识 β=.34 | [B10] | p.9–10 | §5.1, §5.3 |
| SRL trace 频率与自陈汇合验证 | [B1] | p.8–10 | §3.2.4, §4.4 |
| 游戏化组 FOMM 中心转移到 SRL 仪表盘 | [B1] | p.10 | Fig. 7 |

---

### 附：阅读工作记录
- 11 篇 PDF 全部在位并完成标题→编号映射（§0），无缺失。
- 每篇按任务 §5 的 5.1–5.16 模板完成拆解（§2–12）。
- 跨论文综合章节（§13–27）完成，含 12 个跨论文问题（§22）与证据索引（§27）。
- 证据等级按任务 §19 标注：[B4]/[B5]/[B11] 为 conference/proceedings，相关结论在与期刊冲突时以后者为主。

---
