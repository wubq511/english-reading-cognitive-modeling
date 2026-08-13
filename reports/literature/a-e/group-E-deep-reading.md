# Group E — Process Evidence → Cognitive Diagnosis / Construct Validity

> 本文档为 E 组 8 篇论文（E1–E8）的深度阅读报告。E 组回答的核心问题：**我们已经可以从学生 UI 日志中恢复出一定可信度的 Action / Process Evidence，那么这些过程证据能否、以及如何被合法地解释成学生的 cognitive process / skill / misconception，并最终进入 cognitive diagnosis？**
>
> 报告继承 A/A+/B/C/D 组已建立的前提：`raw behavior ≠ reading cognition`、`revisit ≠ confusion`、`long dwell ≠ difficulty`、`question switching ≠ strategy`、`rereading ≠ low ability`、`cursor ≠ gaze`、`eye fixation ≠ cognitive understanding`、`behavioral action ≠ cognitive state`。E 组负责从 Process Evidence 到 Cognitive Interpretation / Construct Validation 再到 Cognitive Diagnosis 的最后桥梁。
>
> 生成日期：2026-08-12。全部页码引用均基于本地 PDF 文件逐页核对（PDF 页 + 期刊页双标注）。
>
> **方法说明**：本报告由主代理对 8 篇 PDF 全文（184 页）通过 6 个并行深读子代理逐页全文阅读 + 主代理抽查复核后撰写；论文关键数值（classification accuracy、agreement/disagreement、parameter recovery、inter-rater reliability、DIC/AIC/BIC 等）均从 PDF 原文抽取核对，未编造任何数字 / 页码。凡不属于论文原文的推断一律标注 `PROJECT TRANSFER INFERENCE`（项目推论）、`CROSS-PAPER SYNTHESIS`（跨论文综合）或 `GENERAL METHODOLOGICAL CONTEXT`（一般方法学背景）。正文出现的论文内部矛盾（E2 表 3 与正文 SABIC 表述不符、E8 推断题 2/3 处不一致等）均如实标注。
>
> **核对审查记录（2026-08-12，初稿完成后的全面审查）**：(1) 结构与编号审查——对照任务文件 §47 结构逐章核验（§0–§46 全部在位），E1–E8 编号未重排、标题/作者/年份与 PDF 首页一致；(2) 页码审查——§46 Evidence Index 全部 62 条页码与提取文本逐条核对（PDF 页 + 期刊页双标注，E1=421 起、E2=481 起、E3=PDF 页、E4=736 起、E5=586 起、E6=241 起、E7=1303 起、E8=印刷页 1 起），页码映射已逐一验证；(3) 数值审查——抽查 E7 Table 5 五情形（6.37/11.34/34.48/17.18/27.17）与单路检出（57.82%/80.21%）、E5 Table 2 相关系数（能力−相似性 0.990 [0.987, 0.992]、能力−效率 −0.543 [−0.586, −0.498]）与 ACA/PCA（0.863/0.650 vs 0.84/0.598）、E4 FC 增量（5.49% 与 <1%）、E4 Σperson 实证相关（−0.125/0.182/−0.959）、E3 筛选链（228→60→14）与 corr(θ1,θ2)=0.826 与 t(3759)=−115.58、E8 Rasch（item reliability 0.91、separation 3.23、PCA 41.2%、第一对比 12.5%）与 think-aloud 对齐率（41%/58%/48%/20% 等）、E2 模式数（13→74）——均与 PDF 原文一致；(4) 概念边界审查——逐条核对任务文件 §48 的 30 条禁止事项（见 §47 自查表），重点复查 diagnostic utility ≠ construct validity（§13）、key action≠skill mastery（§11）、错误 action≠misconception（§12）、fixation≠认知技能（§10.5 E4）、efficiency 负相关（§10.5 E5）、17.18% 可互换（§15）、题型标签≠认知技能（§16）、simulation≠construct validation（§37）、model fit≠心理真值（§38）、correlation≠cognitive identity（§39）、E2/E3/E4 非独立 replication（§36）；(5) 论文内部矛盾如实标注——E2 正文 SABIC 表述与表 3 数字矛盾、E2 正文"FB 需 a1"与 Q 矩阵 FB={a2,m1} 不一致、E8 推断题 2/3 处不一致与题目数 10/11 不一致、E7 章节交叉引用笔误、E4 图形内嵌标签与正文 ACCR 表述细微出入；(6) 微调——§1 新增 EF-15（对项目最可辩护的结论），§10 跨论文矩阵增加"独立 response-process 证据"维度。
>
> **反馈修正记录（2026-08-12；历史反馈原文未随迁移保存，谱系限制见 `../../provenance/LEGACY_REPORT_PROVENANCE.md`）**：① **E2/E3 数据关系修正**——两篇不是同一道 PISA 题、也不是同一分析数据集（E2=TICKETS CP038Q02、买 2 张全价乡村火车单程票、N=3547、28 个 phantom items、自身不含迷思 baseline 为 10；E3=TICKETS Task 2 CP038Q01、坐 4 次地铁最便宜方案、N=3760、14 个）；"E2 = E3 的 14 题 + 迷思 → 28"的错误表述已删除，E2 自身 baseline 为 10→28；Evidence Independence 改为 "methodologically dependent but empirically distinct applications"，不猜测学生是否重叠（§36、EF-14、§11 注、E2/E3 定位段、Evidence Index #60）；② **EF-13 修正**——补 E2 为 real-data empirical（N=3547），E 组证据分布改为 E1 综述 / E2-E3 实证 / E4-E5 模拟+小实证 / E6 框架 / E7-E8 实证；③ **local independence 降级**——"几乎必然违反"改为"存在显著 local-dependence risk；marginal dependence ≠ conditional dependence given attributes；E3 假设 conditional independence 但未用专门 residual/local-dependence model 充分检验，E2 更未处理"（E2 §10.10、E3 §10.10、§31 Q5、Evidence Index #24）；④ **"Process data improves diagnosis" 条件化**——拆为条件化 STRONG/MODERATE-STRONG（response-only 信息不足 + 过程变量与目标 latent trait 共享信息时）+ 一般命题 UNSUPPORTED（§42、§41）；⑤ **E7 17.18% 定义明确**——"占学习会话时长的中位比例（median duration %）"，每次出现注明单位；S5 降为 unresolved cross-method disagreement / co-occurrence（至少三种可能 + coding error），不作为"同时认知过程"的直接证据（EF-9/EF-10、§15、E7 §10.5/§10.22）；⑥ **E8 题型标签 STRONG→MODERATE**——"Item-type labels do not guarantee intended response processes"（n=5、单人编码、无 IR，对齐率不是 latent skill classification accuracy）（EF-11、§41、§42）；⑦ **cognitive ground truth 收窄**——"No single evidence source in Group E qualifies as standalone cognitive ground truth"（STRONG），不推"世界上不存在任何 cognitive ground truth"的哲学命题（EF-12、§33、§42）；⑧ **Directly Transferable 降级**——E3 item expansion → Transfer With Modification / Methodological Candidate（5–95% 频率过滤是 operational choice，不迁移为固定 threshold）；E4 NBF → "count-valued process data 可经显式测量模型纳入，先检查 overdispersion/zero inflation/exposure/window/dependence，再选 Poisson/NB/ZIP/ZINB/hurdle"；E5 LCS 算法 technically transferable、expert-reference similarity 作认知指标 → NOT VALIDATED / PROJECT HYPOTHESIS；E7 Bannert taxonomy → Candidate theoretical coding framework（EVIDENCE_SEARCH 等 construct ≠ Bannert categories）（§10.22 E3/E4/E5/E7）；⑨ **E5 0.990/−0.543 标为推论**——"相似性在重新测能力"与"近冗余"标注 CROSS-PAPER / ANALYTICAL INFERENCE（非论文直接证明）；−0.543 限定"在该 PSTRE 数据与该 efficiency 定义下"（EF-8、E5 §10.5/§10.15、§14/§18/§31/§39）；⑩ **E1 ζ 修正**——ζ = item time-intensity（population-average time），不是 cognitive load parameter（E1 §10.5/§10.6、§14 表）；⑪ **E8 fNIRS 修正**——fNIRS 是 physiological / neurophysiological evidence（supplementary，consistent with text engagement/dependence），不是 behavioral evidence、也不是"正在阅读文本"的直接证明（§19、§33、E8 §10.15）；⑫ **新增 E 组正式结论（反馈整合，7 条）**（§42 末尾）。

---

## 任务符合性对照表（依据 `../../provenance/LEGACY_REPORT_PROVENANCE.md` 登记的 Chat 2 / Turn 18 原始任务书逐条核对）

| 任务文件章节 | 任务要求 | 本报告完成位置 |
|---|---|---|
| §0 | 严格锁定 E1–E8 编号，禁止重排，按标题/作者/年份/DOI 匹配 | §0 PDF Mapping（8/8 在位） |
| §1–§7 | 继承项目背景与 A/A+/B/C/D 已建立前提 | 头部说明 + §1(EF-1/EF-13) |
| §8 | Track A（诊断效用）与 Track B（构念效度）两轨始终区分 | §1(EF-1)、§10、§13、§42 |
| §9 | 三种"有效"（Predictive / Measurement / Construct）严格区分 | §1(EF-3)、§13、§18、§29 |
| §10.1–10.23 | 每篇统一深读模板（23 小节） | §2–§9 每篇逐项覆盖 |
| §11 | 专题一 Key Action → Cognitive Attribute（Q1–Q5） | §11 |
| §12 | 专题二 Misconception vs Non-Mastery | §12 |
| §13 | 专题三 Diagnostic Utility ≠ Construct Validity | §13 |
| §14 | 专题四 RT / Fixation / Action Sequence 对比 | §14 |
| §15 | 专题五 Trace ↔ Think-Aloud（Q1–Q4，17.18% 等数字回 PDF 核对） | §15 |
| §16 | 专题六 Reading-Specific Response Process Validity | §16 |
| §17 | 专题七 Validity Framework（Level 0–4 分层） | §17 |
| §18 | 专题八 Construct Validity vs Criterion Validity | §18 |
| §19 | 专题九 Triangulation（Strength/Weakness/Best Use 表） | §19 |
| §20 | 专题十 Think-Aloud vs Retrospective Replay（三级判定） | §20 |
| §21 | 专题十一 Circularity（重点审查 E2/E3） | §21 |
| §22 | 专题十二 Uncertainty Propagation | §22 |
| §23 | 专题十三 Student-Specific Interpretation | §23 |
| §24 | 专题十四 Item-Specific Interpretation | §24 |
| §25 | 候选 Cognitive Evidence Vocabulary（表格 + 不硬凑） | §25 |
| §26 | Cognitive Skill / Attribute Vocabulary（不创造复杂 taxonomy） | §26 |
| §27 | Process Evidence 进入 DCM 的三条路线（A/B/C） | §27 |
| §28 | Key Action Coding vs Sequence Modeling | §28 |
| §29 | Validity Evidence Matrix | §29 |
| §30 | Evidence Ladder（A–E 五级） | §30 |
| §31 | 20 个跨论文问题 | §31（Q1–Q20 全部作答） |
| §32 | 对 explicit report 的定位（normal input vs validation） | §32 |
| §33 | Ground Truth Hierarchy | §33 |
| §34 | Construct Validation Pipeline（文献约束下候选） | §34 |
| §35 | Cognitive Evidence Confidence / provenance | §35 |
| §36 | Evidence Independence（禁止 E2/E3/E4 当独立 replication） | §36 |
| §37 | Simulation ≠ Construct Validation | §37 |
| §38 | Model Fit ≠ Psychological Truth | §38 |
| §39 | Correlation ≠ Cognitive Identity | §39 |
| §40 | Reading Process Mapping（矩阵） | §40 |
| §41 | 四类证据强度（STRONG/MODERATE/WEAK/UNSUPPORTED） | §41 |
| §42 | What Group E Establishes（逐命题证据强度） | §42 |
| §43 | E 组给系统增加了什么 | §43 |
| §44 | A–E 最终整合（Integrated Pipeline） | §44 |
| §45 | 保留 UNKNOWN | §45 |
| §46 | Evidence Index（页码真实核对） | §46 |
| §47 | 最终输出结构 | 本文件完全按该结构 |
| §48 | 严格禁止事项（30 条） | 逐条自查通过（见报告末尾自查表） |
| §49 | 最终质量标准（条件化结论而非口号） | §1、§13、§42、§43 |
| §50 | 最终核心目标 | §42、§43、§45 |

---

## 0. PDF Mapping

根据论文标题、作者、年份、DOI 将本地 PDF 与 E1–E8 编号建立映射。**编号严格按任务文件锁定，未重排。**

| 编号 | 论文（任务文件标题） | 作者 | 本地 PDF 文件 | 期刊/场合 | 年份说明 |
|---|---|---|---|---|---|
| E1 | Utilizing Process Data for Cognitive Diagnosis | Hong Jiao, Dandan Liao & Peida Zhan | `E_2018_Jiao_ProcessData_CognitiveDiagnosis.pdf` | *Handbook of Diagnostic Classification Models* (Springer), Ch.20, pp.421–436 | 书章版权 2019（文件名为 2018，对应正文引用的 Zhan, Jiao & Liao 2018 模型论文） |
| E2 | 引入迷思概念的关键行动编码及其在过程数据诊断分类分析中的应用 | 詹沛达、高方方、陈琦鹏 | `E_2025_詹沛达_迷思概念编码.pdf` | 《心理科学》48(2): 481–494 | 2025 |
| E3 | Diagnostic Classification Analysis of Problem-Solving Competence Using Process Data: An Item Expansion Method | Peida Zhan & Xin Qiao | `E_2022_Zhan_ItemExpansionMethod.pdf` | *Psychometrika*（online-first，无卷期/页） | 2022（收稿 2020-08，定稿 2021-10） |
| E4 | Cognitive Diagnosis Modeling Incorporating Response Times and Fixation Counts: Providing Comprehensive Feedback and Accurate Diagnosis | Peida Zhan, Kaiwen Man, Stefanie A. Wind & Jonathan Malone | `E_2022_Zhan_ResponseTimesFixationCounts.pdf` | *Journal of Educational and Behavioral Statistics* 47(6): 736–776 | 2022 |
| E5 | Incorporating Process Information Into Cognitive Diagnostic Models: A Four-Component Joint Modeling Approach | Mehdi Rajeb, Wenchao Ma, Qiwei He & Qingzhou Shi | `E_2026_Rajeb_FourComponentJointModeling.pdf` | *Journal of Educational and Behavioral Statistics* 51(3): 586–624 | 2026（© 2025 AERA；收稿 2023-12，录用 2025-03） |
| E6 | Process Data in Computer-Based Assessment: Challenges and Opportunities in Opening the Black Box | Marlit Annalena Lindner & Samuel Greiff | `E_2023_Lindner_ProcessDataBlackBox.pdf` | *European Journal of Psychological Assessment* 39(4): 241–251 | 2023（Editorial / special issue） |
| E7 | Towards a Fuller Picture: Triangulation and Integration of the Measurement of Self-Regulated Learning Based on Trace and Think Aloud Data | Yizhou Fan, Mladen Rakovic, Joep van der Graaf, Lyn Lim, Shaveen Singh, Johanna Moore, Inge Molenaar, Maria Bannert & Dragan Gašević | `E_2023_Fan_SRLTraceThinkAloud.pdf` | *Journal of Computer Assisted Learning* 39(4): 1303–1324 | 2023 |
| E8 | A Validation Study of a Middle Grades Reading Comprehension Assessment | Lori Severino, Mary Jean Tecce DeCarlo, Toni Sondergeld, Meltem Izzetoglu & Alia Ammar | `E_2018_Severino_ReadingComprehensionValidation.pdf` | *RMLE Online* 41(10): 1–16 | 2018（online 17 Oct 2018） |

**编号说明**：
- E1 任务文件标注 "2019"，本地文件名为 2018：该书章（*Handbook of Diagnostic Classification Models*）版权年为 2019，DOI `10.1007/978-3-030-05584-4_20`；文件名中的 2018 对应正文引用 Zhan, Jiao & Liao (2018) 的 RT-DINA 模型论文。以任务文件编号为准，编号仍为 E1。
- E5 任务文件要求"正式发表信息以 PDF 为准"，已核对：JEBS 2026, 51(3), 586–624。
- E3 为 Psychometrika online-first 版，PDF 内无印刷页码，全文只标 PDFPAGE 1–19。
- 8 篇全部在位，无 `E# — PDF NOT FOUND`。

**页码约定**：E1 印刷页 = PDFPAGE + 420（PDFPAGE 1 = 印刷 421）；E2 印刷页 = PDFPAGE + 480（PDFPAGE 1 = 印刷 481，附录在 PDFPAGE 15–19）；E4 印刷页 = PDFPAGE + 735（PDFPAGE 1 = 印刷 736）；E5 印刷页 = PDFPAGE + 585（PDFPAGE 1 = 印刷 586）；E6 印刷页 = PDFPAGE + 240（PDFPAGE 1 = 印刷 241）；E7 印刷页 = PDFPAGE + 1302（PDFPAGE 1 = 印刷 1303）；E8 印刷页 = PDFPAGE − 1（PDFPAGE 1 为 T&F 封面页，正文从印刷页 1 起）。E3 无印刷页码。

---

## 1. Executive Findings

以下为 E 组跨论文核心结论。每条都可在 §46 Evidence Index 追溯原文。

### EF-1. E 组 8 篇论文严格分属两个轨道，没有一篇同时提供"诊断效用"与"构念效度"两套完整证据
Track A（Process → Diagnosis）：E1（背景章）、E2、E3、E4、E5——它们回答"加入 process information 能否提高 cognitive diagnosis"（classification accuracy / parameter recovery / latent classification）。Track B（Process → Construct Validity）：E6（效度框架）、E7（trace↔think-aloud 三角验证）、E8（阅读理解效度实证）——它们回答"process indicator 是否真的是我们声称的认知构念的证据"。**没有任何一篇论文同时完成两者**：E1–E5 的诊断增益几乎全部来自 simulation 或模型拟合，没有一篇附带独立 response-process / construct validity 验证；E6/E7/E8 提供效度框架与证据，但不提供 CDM 建模。任务文件 §8 的两轨区分被 8 篇论文天然验证（§10、§42）。

### EF-2. "加入过程数据提高认知诊断"是条件性结论，不是无条件收益
E1 转述 Minchen & de la Torre (2016) 与 Zhan et al. (2018) 的模拟结论：**当测验长度充分、题目质量好（guess/slip 低）、Q-matrix 可识别时，加入 RT 对参数估计精度与 attribute 分类没有增益；当 Q-matrix 不可识别、测验短、题目 guess/slip 高时，加入 RT 的改进才明显**（PDFPAGE 10–11）。E4 的模拟：加入 fixation count 的分类精度绝对增量多数条件 <0.01、相对增量 <1%，最大相对增量 5.49% 只出现在 Q-matrix incomplete + 人参数高相关条件下（Table 6）。E5 的模拟：低人参数相关条件下四分量无优势、甚至略低于 response-only 基线（Low/500/30：HO-LLM PCA 0.711 vs 四分量 0.710）。**共同结论：过程数据的信息价值在"响应信息不足"时最大——这与"过程数据本身具有认知语义"无关（§13、§42）。**

### EF-3. 三种"有效"必须分离，E 组提供了完整的分层证据
任务文件 §9 的三分法在本组被逐篇验证：(1) **Predictive utility**——adding process variable improves classification accuracy（E4 的 FC、E5 的 similarity/efficiency、E3 的 phantom items）；(2) **Measurement / Diagnostic utility**——adding process data reduces attribute classification error / SE（E3 的 SE 比较 t(3759)=−115.58、E5 的 ACA 0.863 vs 0.84）；(3) **Construct validity**——behavior X represents cognitive process Y——**没有一篇论文提供独立证据**。E4 自己明确把 FC 语义限定为 "visual cognitive process loading amount endorsed by FCs" 而非完整注意（PDFPAGE 4）；E5 的 efficiency 实证上与能力负相关（−0.543）；E2/E3 的 mapping 是研究者预设。**前两者不能自动推出第三者，这是 E 组报告反复检查的推断边界（§13、§18、§29）。**

### EF-4. 过程数据进入 CDM 有两条主路线，E 组论文各自只走一条
Route A（Process as additional indicators / phantom items）：E2/E3 把行动序列编码为 phantom items 0/1，进入 DCM 的 Q-matrix（E3：1 题→14 个 phantom items；E2：1 题→28 个）。Route B（Process as auxiliary continuous variables + joint model）：E1/E4/E5 把 RT / fixation count / sequence similarity / sequence efficiency 作为额外观测，经 person 层相关结构与 ability 联合（joint-hierarchical 框架）。**两条路线的代价不同**：Route A 需要定义"哪个行动对应哪个属性"（Q-matrix 输入），代价是 interpretative circularity（§21）；Route B 需要给每个过程变量选测量模型（lognormal RT / NBF / logit 序列指标），代价是"该变量到底测什么认知构念"未经验证（§13）。§27 给出完整比较。

### EF-5. key action → skill / misconception 的映射全部由研究者 / 专家预设，没有独立 response-process 证据
这是 E 组最重要的跨论文事实之一。E2：Q-matrix 由作者从任务状态转移结构直接转写，错误状态转移→迷思概念属性是**编码假设**（"假设仅当参与者掌握了各行动序列所需的潜在属性后才能呈现该行动序列"，PDFPAGE 5），全文无 think-aloud / 眼动 / 专家评审 / 编码者一致性。E3：Q-matrix "based on expert judgment and is essentially retrofitting...in a post hoc manner"（PDFPAGE 7），PVAF 经验验证被否决、专家输入获胜（PDFPAGE 12）。E4：Q-matrix 沿用外部数据集，构建与验证过程 NOT CLEARLY REPORTED。E5：reference sequence 由内容专家定义，但"接近最优序列 = 高能力"无独立证据。**§11 强制回答的 Q1–Q5 结论：key action 是 expert-defined + 出现率筛选的复合标准，非独立验证的认知指标。**

### EF-6. E2/E3 落入 interpretative circularity 的实质风险，E 组无法从内部打破
循环链：研究者假设"行动 A = 技能 X"→ Q-matrix 编码 A→X（模型输入）→ DCM 估计学生缺 X → 论文结论"行动 A 成功诊断 X"。E3 明确承认 Q-matrix 是 post hoc retrofitting；E2 的迷思概念属性甚至直接由错误选项转写（内建了"错误行动 = 迷思概念"）。**模型拟合好（E3 RMSEA2=0.032、E2 GDINA SRMSR=0.0756）不能独立验证映射正确，因为映射是前提。** 打破循环必须靠 Track B 的独立证据：E6 要求"像产品数据一样验证"、E7 的两路三角验证、E8 的 think-aloud + fNIRS + Rasch 三方互证——**这是 E 组文献内部能提供的唯一出路（§21、§33、§34）。**

### EF-7. E4 中 fixation count 的认知语义被论文自己明确限定，诊断增益不等于认知效度
E4 的 MJ-DINA 把 FC 建模为 latent visual engagement ε 的负二项计数指示，**FC 不加载在任何 attribute 上**（条件独立假设 8：Vni ⊥ αn,τn | εn，PDFPAGE 10），FC 与 RT、accuracy 通过 Σperson 相关结构共享信息。论文原话限定 visual engagement "reflects only the visual cognitive process loading amount endorsed by FCs rather than the entire visual attention"（PDFPAGE 4），且 "depends on the context"。Table 2 的认知特征分类（fluency、reflective–impulsive、focuser–nonfocuser）被明确标注为 "relatively rough...rather than an accurate measurement or diagnosis"（PDFPAGE 11）。**结论：加入 FC 提高分类精度 ≠ FC 测量了认知技能——C 组"fixation ≠ cognitive understanding"的边界在 E4 中被论文自己维持（§13、§14）。**

### EF-8. E5 的 sequence similarity 与 ability 相关 0.990、efficiency 与 ability 负相关 −0.543，但"相似性=重新测能力/效率=策略能力"只是推论，不是论文证明的结论
E5 实证：能力−相似性相关 0.990 [0.987, 0.992]、能力−效率相关 −0.543 [−0.586, −0.498]（Table 2，PDFPAGE 12）。**仅凭 r=.990 只能说这两个 latent person parameters 在该数据集中呈现极强的经验重叠 / near-collinearity；"相似性在重新测能力（merely re-measuring ability）"是一种解释，但非直接证明——还可能涉及 construct overlap、model-induced dependence、reference-sequence design、shared task demands（CROSS-PAPER / ANALYTICAL INFERENCE，非论文结论）。** 同理，能力−效率 −0.543 的稳妥表述是：**在该 PSTRE 数据和该 efficiency 定义下，高 latent ability 与较低 efficiency parameter 相关**（不要泛化为"高能力学生更低效"）。论文自己也承认 "findings regarding similarity and efficiency parameters could not be compared with any previous studies"（PDFPAGE 16）。**sequence indicators 的作用被定位为提高分类精度的辅助指标 + 事后弱解释，而非经效度验证的认知构念（§13、§28）。**

### EF-9. E7 是最关键的 validity 证据：trace 与 think-aloud 只有 17.18% 时段匹配、45% 互补、27.17% 分歧
E7 把 trace 与 think-aloud 对齐到同一时间轴，切成细粒度段，逐段归入五类：S1 两路皆无 = 6.37%、S2 仅 think-aloud = 11.34%、S3 仅 trace = 34.48%、S4 匹配（同一过程）= 17.18%、S5 分歧（不同过程）= 27.17%（Table 5，PDFPAGE 11）。**单位说明：这些百分比是该情形段总时长占学习会话时长的中位比例（median duration (%)，Table 5），不是匹配段数量占全部段数量的比例；精确表述为：两路被判为同一 SRL 过程的时段，占学习会话时长的中位比例为 17.18%。** 互补段 S2+S3 ≈ 45%，共现段 S4+S5 ≈ 44%。**可互换仅 17.18%——直接否定"trace 与 think-aloud 可互换"的命题。** 过程级交叉表进一步显示：think-aloud 编码的 MC.E 有 0%、MC.P 4.45%、MC.M 4.70% 被 trace 同过程匹配，而 LC.F 达 75.01%（Table 7，PDFPAGE 12）——**元认知过程的 trace↔verbal 一致性尤其低（§15、§29）。**

### EF-10. 论文没有把 think-aloud 当 cognitive ground truth；两路被同等对待
E7 明确采取中立立场："we considered the measurement results based on trace data and think aloud data as equally valid...neither of the two methods can be considered as fully 'truth' in measuring SRL processes"（PDFPAGE 18），对 S5 分歧不判定谁对。**注意：论文对 S5 给出"学习者同时进行多个过程"的解读，但它只是可能解释之一——E7 原文同时承认至少三种可能（① 真正同时发生两个 process；② 极细粒度地先后发生、因测量分辨率导致重叠；③ 当前理论框架缺了一个真正 process），并提及 measurement/coding error 的可能；因此 S5 最稳妥的标签是 unresolved cross-method disagreement / co-occurrence，不能作为"同时认知过程"的直接证据。** E6 区分 process data（显性行为痕迹）与 response processes（潜在构念），明确否定"追踪过程必然提供有用信息"的朴素观点（PDFPAGE 2）。E8 把 think-aloud 作为五种效度证据之一与 Rasch/fNIRS 三角互证，但**在 Q6 决策中实际上让它充当了构念解释的仲裁者**（心理测量说拟合好、think-aloud 说不对齐 → 重写构念）——这是论文未明说的事实（§15、§33）。

### EF-11. 题型标签不能保证诱发预期过程：E8 提供 MODERATE 证据（Item-type labels ≠ guaranteed response processes）
E8 的 think-aloud 演绎编码显示各题型对齐率差异巨大：literal 58%、inferential 48%、vocabulary 20%、main idea 35%、best evidence 50%、key idea 20%、author's purpose 55%、text structure 45%（Table 4，PDFPAGE 10），整体 41%。Rasch PCA 显示仅 41.2% 方差被题目解释（<60% 强单维阈值）、第一对比 12.5%（PDFPAGE 11）。**注意证据强度的边界：这些对齐率测的是"学生口头表述支持预期答案构念的比例"（student verbal responses supporting the intended answer constructs），不是 latent cognitive skill classification accuracy；Rasch PCA 只能说明该评估的维度不够干净，不能告诉我们哪个题型对应哪个 latent skill；且 think-aloud 为 n=5、演绎编码、单人编码、无 inter-rater reliability。** 因此 E8 的可靠结论是 **MODERATE**："Item-type labels do not guarantee that students engage in the intended response processes"——题型标签不能保证诱发预期过程。"题型标签 ≠ 认知技能"可以继续作为我们的概念边界，但 E8 不是它的强实证证明。这对我们项目"题目类型 → 所需技能"的设计是直接警告（§16、§26）。

### EF-12. E 组无单一证据源可单独充当 cognitive ground truth（收窄表述），更合理的是 triangulated validation evidence
综合 E6/E7/E8：E6 认为过程数据需要"理论 + 经验/实验验证"共同支撑，单一过程指标不能自证；E7 两路同等有效、无 one truth；E8 用五类效度证据（content / response process / internal structure / relations / consequences）迭代互证，Rasch 说 Q6 好、think-aloud 说不好、fNIRS 佐证，最终重写构念。**收窄表述：E 组能 STRONG 支持的是"E 组考察的证据源——trace、think-aloud、eye/fNIRS、expert mapping、Q-matrix、latent-model output——没有一个可单独当作 cognitive ground truth"；不能推出"世界上不存在任何 cognitive ground truth"的哲学命题（§33）。** 任务文件 §33 的预判被 E 组文献支持（§33）。

### EF-13. E 组证据分布：三篇真实数据实证 + 两篇 simulation 主导 + 三篇框架/效度实证，simulation 只证明参数恢复、不证明真实认知
E 组 8 篇的证据类型分布为：**E1** → background chapter，无自身实证（转述模拟结论）；**E2** → real-data empirical（PISA 2012，N=3547）；**E3** → real-data empirical（PISA 2012，N=3760）；**E4** → simulations + empirical（N=93）；**E5** → simulations + empirical（N=935）；**E6** → editorial/framework；**E7** → empirical（N=44）；**E8** → empirical（N=33，think-aloud n=5，fNIRS n=7）。**Simulation 证明"若模型假设为真则参数可恢复"，不证明"真实人类认知遵循这些假设"；而真实数据实证的（E2/E3/E7/E8）也不等于 construct validation——它们同样缺少 ground truth 对照或独立认知标签。** 任务文件 §37 的强制检查项在 E 组得到系统性确认（§37）。

### EF-14. 证据独立性：E2/E3/E4 属同一方法学谱系，但 E2 与 E3 并非同一道题、同一分析数据集
E2（詹沛达，浙江师大）、E3（Zhan & Qiao）、E4（Zhan, Man, Wind & Malone）共享第一作者 Peida Zhan，且 E2 明确自述为 E3（Zhan & Qiao 2022）"基于虚拟题目拓展的关键行动编码"的方法学拓广，E4 与 E3 同属 Zhan 的 joint-hierarchical DCM 体系。**但 E2 与 E3 不是同一道 PISA 题、也不是同一份分析数据**：E2 用 TICKETS CP038Q02（目标：买 2 张全价乡村火车单程票；最终样本 N=3547；28 个 phantom items，其自身不含迷思概念的 baseline 编码为 10 个），E3 用 TICKETS Task 2、CP038Q01（目标：找在城市坐 4 次地铁的最便宜方案；N=3760；14 个 phantom items）。二者共享 PISA 2012 TICKETS 环境与作者方法学谱系，属 **"methodologically dependent but empirically distinct applications"**，不能视为完全独立的方法复制，其一致性部分是设计内建的（§36）。E2/E3 是否有部分学生重叠，仅凭这两篇 PDF 无法确定，不猜测。E5 的 He 也是 E 组外部引用源；E6/E7/E8 相对独立，提供真正的外部效度视角。

### EF-15. 对项目最可辩护的结论：行为证据进入认知诊断，必须经过独立验证的映射
综合 E 组全部：**(1) 直接可用的**——item expansion（phantom item）流程、joint-hierarchical CDM 框架、序列 LCS 度量框架、S1–S5 三角验证模板、五类效度证据组织框架；(2) **必须修改的**——key action→attribute 映射需我们自己的领域专家 + 独立 response-process 证据（think-aloud / stimulated recall / expert coding）重建；phantom item 的局部独立假设在自由阅读中更脆弱；(3) **不可用的**——把任何 UI 行为直接解释为认知技能、把 fixation/cursor 当注意测量、把专家最优序列当阅读"正确路径"（§40、§42、§43）。

---

## 2. E1 — Utilizing Process Data for Cognitive Diagnosis

> **论文定位**：**Background / Overview**——2019 年"process data → cognitive diagnosis"领域的方法学综述章（*Handbook of Diagnostic Classification Models* Ch.20）。任务文件明确"E1 是 background chapter，不要把它当成强实证论文"。Jiao, Liao & Zhan (2019)，PDFPAGE 1 = 印刷 p.421。

### 10.1 Research Question
该章要回答：如何把 process data（重点是 response time）作为辅助信息整合进 cognitive diagnosis，以提升能力估计精度、促进认知诊断、检测异常作答。类别归属：process-data modeling（RT 建模）+ cognitive diagnosis / diagnostic classification。response-process validity / construct validity 仅在结尾作为"需要注意的效度考量"提出（PDFPAGE 11）。**不是实证论文**：无数据、无模拟、无 recovery 指标。

### 10.2 Construct
用论文自己的术语：认知诊断针对被试在精细属性上的 **attribute mastery status αjk（属性掌握状态）**；higher-order 层有 **general (higher-order) ability θj**；RT 侧有 **person speed parameter τj（作答速度）** 与 **time-intensity parameter ζi**（PDFPAGE 5–7）。θj 与 τj 是两个不同的潜变量。

### 10.3 Observable Process Data
- **Raw Observable**：item-level response time Tji（log 文件直接记录）、item response Yji。论文列举的其他原始过程数据（**仅提及、未建模**）：number of clicks、frequency of use of help features、frequency of answer changes、eye-tracking data（PDFPAGE 1）。
- **Derived Process Indicator**：log(Tji)、person speed τj、item time-intensity ζi、slipping/guessing 参数 si/gi、IDIi = 1 − si − gi（PDFPAGE 5）。

### 10.4 Process Feature Construction
RT 直接从 log 文件获得；唯一加工是取对数以正态近似：
$$\log T_{ji} = \zeta_i - \tau_j + \varepsilon_{ji}, \quad \varepsilon_{ji} \sim N(0, \sigma_{\varepsilon i}^2)$$
即 van der Linden (2006) lognormal RT 模型（PDFPAGE 5，印刷 p.425）。τj 与 ζi 是模型估计出的潜在参数，非人工编码。可扩展项：time-discrimination 参数、person-specific growth 参数、Box-Cox 变换、线性变换模型（PDFPAGE 5）。click/eye-tracking 的 feature 构造本章未涉及。

### 10.5 Cognitive Interpretation
- (a) Explicitly defined by theory：RT→speed（τj）的解读（论文提及高 RT 可能反映更大的认知挑战 / 工作速度，PDFPAGE 3；**但这是对 RT 整体解读的一种，ζi 的正式定义是 item time-intensity（population-average time），不是 cognitive load parameter**，反馈修正）属理论假设；higher-order θj→attribute mastery 是 de la Torre & Douglas (2004) 的理论结构（PDFPAGE 6）。
- (b) Defined by expert / Q-matrix：Yji→αjk 的映射通过 Q-matrix，本章将 Q-matrix 视为 CDM 标准输入，未说明构建者。
- (d) Interpreted post hoc：本章明确承认 RT 的解释 "intricate"，统计考量不能脱离实质考量（引 Goldhammer et al. 2014，PDFPAGE 11）。

### 10.6 Mapping
链 1：Observable（log Tji）↓ [lognormal 模型] → Process Feature（τj, ζi）↓ [理论假设] → Cognitive Construct（**τ = processing / working speed；ζ = item time-intensity，即 population-average time needed to complete item i——ζ 不是 cognitive load parameter**，反馈修正）。链 2：Observable（Yji）↓ [DINA + Q-matrix] → Cognitive Construct（αjk 掌握状态）。两段箭头均缺乏独立外部验证。

### 10.7 Who Defines the Mapping?
- RT→speed：existing theory / model（van der Linden 2006 lognormal 框架），非实证标定。
- Response→attribute：Q-matrix 定义者本章未交代 → **NOT CLEARLY REPORTED**。全章把 Q-matrix 当作 DCM 既定的 measurement input。

### 10.8 Q-Matrix / Attribute Structure
Q-matrix 为标准 I×K 二元矩阵（Tatsuoka 1983），qik 指示题目 i 是否要求属性 k（PDFPAGE 5）。**Q-matrix 是研究者预设的 measurement input，非数据自动发现**。attribute 分布用 higher-order 结构：logit P(αjk=1) = γkθj − λk，作用是降参数、解释属性相关、给出整体能力 θj（PDFPAGE 6）。无 attribute hierarchy 讨论。

### 10.9 Key Action
**NOT REPORTED / 不适用**。本章只处理 item-level RT，不处理 action sequence，未定义 key action。action sequences、clicks 仅作为其他过程数据类型被点名（PDFPAGE 1）。

### 10.10 Phantom Item / Item Expansion
**NOT REPORTED / 不适用**。本章的 RT-CDM 在原始题目层建模，不做题目展开。

### 10.11 Misconception Diagnosis
**NOT REPORTED**。只讨论 attribute mastery 的估计精度，不区分 lack of mastery 与 misconception。

### 10.12 Multimodal Joint Modeling
本章核心贡献是 joint RT-DINA 模型（Zhan et al. 2018 框架）：
- Level 1：Yji 用 DINA（式 20.2），log Tji 用 lognormal（式 20.1），分别建模。
- Level 2：item 参数（βi, δi, ζi）服从三元正态（式 20.7）；person 参数（θj, τj）服从二元正态，含相关 ρθτ（式 20.8）。**是 separate latent variables（ability θj 与 speed τj）通过 person 层相关 ρθτ 连接，attributes 再由 higher-order θj 驱动**。
- 四条局部独立假设：(a) αjk 给定 θj 条件独立；(b) Yji 给定 αj 条件独立；(c) log Tji 给定 τj 条件独立；(d) 同题 Yji 与 log Tji 给定所有人参数条件独立（PDFPAGE 7）。
- 识别约束：μθ = 0，σθ = 1，μτ = 0（PDFPAGE 7）。

### 10.13 Added Value of Process Data
本章自身无实证结果。关键结论以**转述**形式给出：引述 Minchen & de la Torre (2016) 与 Zhan et al. (2018) 的（模拟）发现——**当测验长度充分、题目质量好（guess/slip 低）、Q-matrix 可识别时，加入 RT 对参数估计精度与 attribute mastery 分类准确率没有带来增益**（PDFPAGE 10）；**当 Q-matrix 不可识别、测验短、题目 guess/slip 高时，加入 RT 对参数估计的改进明显**（PDFPAGE 10–11）。这是 referenced simulation 结论，不是本章自己的数据。唯一给出的数字是模拟超先验设定：μζ 均值对应平均 RT = 20.086 s，模拟平均 RT 范围 4.883–82.617 s；mean guessing 0.1（对应 logit −2.197，范围 0.026–0.314），mean slipping 0.1（对应 logit 4.394，范围 0.007–0.653）（PDFPAGE 8）。
> **Improved diagnostic performance does not by itself establish construct validity**——本章转述的"加入 RT 提高分类"只是 simulation 中参数恢复的证据，不验证 RT 的认知语义。

### 10.14 Validation Evidence
全部 **NOT PROVIDED**：无 Content / Response-process / Internal structure / Relations to other variables / Consequences / Convergent / Discriminant / Expert / Think-aloud / Retrospective / Eye tracking / External criterion。章末仅呼吁"应提供更多实证与理论论证来回应 process data 作辅助信息时的效度考量"（PDFPAGE 11）。

### 10.15 Ground Truth
本章无实证分析，不存在 ground truth。引述的模拟研究中 α 由模拟设定（仿真 ground truth），本章不报告具体数值。

### 10.16 Circularity Risk
RT→speed 的认知解读是模型假设本身，无独立证据链支持"RT 模式 = 特定认知状态"；RT 也可由速度化作答、低动机、作弊/押题导致短 RT（PDFPAGE 3）。attribute 映射依赖预设 Q-matrix。本章以"加入 RT 是否提升估计"来评估价值，但提升与否并不验证 mapping 本身对错——**存在"假设指标 = 认知构念 → 模型估计该构念 → 结论该指标诊断该构念"的循环风险，且本章没有独立验证手段**。

### 10.17 Alternative Explanations
论文自己列出的 RT 替代解释：任务难度、time-on-task 效应、speeded responding（低 stakes 低动机）、item preknowledge/作弊（更短 RT）（PDFPAGE 3）。还指出 accuracy–speed 关系在被试群体间不一致、存在 within-subject differential speed effects（随能力与难度变化）（PDFPAGE 11）。即：长 RT = 高认知挑战只是诸多解释之一，本章不排除其他解释。

### 10.18 Temporal Alignment
仅使用整题作答时长，不涉及 action 级时间定位；"答题前 vs 答题后"的过程区分未讨论。未对齐子过程时间轴。

### 10.19 Person / Item / Context Dependency
明确承认：accuracy–speed 关系随群体不同而变化；speed 效应随 ability 与 item difficulty 变化（PDFPAGE 11）；RT 依赖题目特征与作答反应（PDFPAGE 3）。即 process indicator（τj、RT）的意义是 person/item/difficulty 依赖的。

### 10.20 Generalization
**NOT REPORTED**。本章无数据演示，无法验证 new student / new item / new task / new domain。

### 10.21 Evaluation
不是 empirical/simulation 论文，无 recovery 指标。评估仅以两种形式出现：(1) 转述的模拟结论（PDFPAGE 10–11）；(2) 供未来仿真用的超先验设定（PDFPAGE 8）。

### 10.22 Transfer to Our English Reading System
- **Directly Transferable**：joint RT-DINA 建模框架（log RT 作为辅助信息、θ 与 τ 双潜变量、person 层相关）可直接搬到"阅读能力 + 阅读速度"联合诊断；其"加入 RT 仅在题目质量差/信息不足时有增益"的结论对项目是重要警示（不要指望 RT 是万能补充）；识别约束与四条局部独立假设可直接复用。
- **Transfer With Modification**：该框架是 item-level RT 模型，而我们的系统有 action-level 数据（滚动/回看/划线/选文本、改答案、划掉选项）。需要把 action 级信息先聚合成 item/段落的 derived indicator 才能进入此类联合模型。Q-matrix 需由阅读领域专家针对阅读理解属性重建。
- **Not Transferable**：eye-tracking、click count、help-feature 频率等，本章只提及、未给出任何建模方法，不能直接迁移。expert-defined Q-matrix 与属性定义也不通用。

### 10.23 What This Paper Does NOT Establish
1. 未建立"加入 RT 能提升认知诊断"的实证结论（反而转述了在理想测验下"无增益"）。
2. 未建立 RT→认知状态的 construct validity（承认 RT 解释复杂、依赖情境）。
3. 未处理 click / answer-change / help-feature / eye-tracking 的任何建模方法（仅点名）。
4. 未做任何真实数据或模拟数据分析，无任何 recovery / 分类精度数值。
5. 未建立 within-subject differential speed 下的 RT-CDM（列为未来工作，PDFPAGE 11）。

---

## 3. E2 — 引入迷思概念的关键行动编码及其在过程数据诊断分类分析中的应用

> **论文定位**：**Key Action Coding → Skills + Misconceptions Diagnosis**，E 组核心论文之一。詹沛达、高方方、陈琦鹏，《心理科学》2025, 48(2): 481–494。E2 是 E3（Zhan & Qiao 2022）的**方法学**拓广：在关键行动编码中引入"迷思概念"作为附加属性，实现技能 + 迷思概念的联合诊断（**方法思想承袭 E3，但二者不是同一道 PISA 题、也不是同一分析数据集：E2=CP038Q02、N=3547、28 题，其自身不含迷思概念的 baseline 为 10 题，§36**）。

### 10.1 Research Question
核心问题：现有基于关键行动编码（key-action coding）的过程数据诊断分类分析"仅考虑问题解决能力与技能对行动的影响，忽略了迷思概念（misconception）对问题解决行动的影响"（PDFPAGE 2）。本文提出**引入迷思概念的关键行动编码**，实现基于过程数据（行动序列）对**问题解决技能和迷思概念的联合诊断**，以"进一步明确学生出现错误的具体原因，并提供同时包含技能和迷思概念的综合诊断反馈"（PDFPAGE 3）。类别归属：cognitive diagnosis / diagnostic classification（DCM）、process-data modeling（key-action coding + phantom item）、misconception diagnosis。

### 10.2 Construct
论文自己的术语（原文引用）：
- **"潜在属性"** = **"问题解决技能"**（a1~a4）+ **"迷思概念"**（m1~m4），共 8 个属性（PDFPAGE 5）。
- **迷思概念**："基于个人经验构建地对一些事件、对象或观点的错误理解（Martin et al., 2001），包括非科学信仰、先入为主的理解、天真理论或概念误解等"（PDFPAGE 2）。并强调"即使参与者呈现正确作答，迷思概念也可能与他们的正确概念共存"（PDFPAGE 2），即技能与迷思概念**可共存、非互斥**（PDFPAGE 5）。
- 4 技能：a1 理解需要购买郊区火车票（country trains）；a2 理解需要购买全价票（full fare）；a3 理解需要购买次票（individual）；a4 理解需要购买 2 张票（2 tickets）（PDFPAGE 5）。
- 4 迷思概念：m1 理解需要购买城市地铁票（city metro）；m2 理解需要购买优惠票（discount）；m3 理解需要购买包日票（daily）；m4 理解需要购买 2 张以外的任意张票（other trips）（PDFPAGE 5）。
- 前提假设（沿用 Zhan & Qiao 2022）：参与者在整个施测过程中其心理构念（技能、迷思概念）"具有相对稳定性"（PDFPAGE 5）。

### 10.3 Observable Process Data
原始任务：PISA 2012 计算机化问题解决测验 TICKETS（CP038Q02），要求购买两趟单程的全价乡村火车票；正确得 1 分。操作界面依次为（a）交通网络→（b）优惠类型→（c）车票类型→（d）搭乘次数，四阶段有顺序，点 BUY 前无退出选项；任一面点 CANCEL 回到初始"交通网络"界面（PDFPAGE 3）。最优行动序列 = "COUNTRY TRAINS → FULL FARE → INDIVIDUAL → 2 → BUY"（PDFPAGE 3）。
- **Raw Observable**：log-file 逐事件记录（cnt、schoolid、StIDStd、event=START_ITEM/各阶段选择/CANCEL/BUY、event_value）（附录 S1.1）。
- **Derived Process Indicator**：(1) 行动序列——把状态事件压缩为状态字母序列；(2) 虚拟题目作答向量——对 28 个 phantom items 的 0/1 编码。
- 样本：原样本 3769 人（美 429、新加坡 470、澳 1865、土 1005），删 4 名信息不全 + 218 名中途放弃，最终 **3547 名**（PDFPAGE 4）。

### 10.4 Process Feature Construction
完整流程（PDFPAGE 4–6；附录 S1）：
1. **状态定义**：中间状态用字母 A–I 编码（图 2）。每个问题状态只包含 1 个关键行动（脚注⑤）。起始/目标状态无测量信息，不编码。
2. **清洗**：删除 CANCEL 事件（返回初始状态）；把连续重复的问题状态缩减为 1 个。示例：F→B→CANCEL→A→B→C→D→D 压缩为 **FBABCD**（同时含正确与错误状态转移）。
3. **N-gram 特征提取**：把行动序列拆分为 uni/bi/tri/quad-gram 的"字节片段序列"，构建"行动序列空间"。
4. **虚拟题目初选与删题**：表 1 全部 38 个字节片段为初选（uni 8、bi 10、tri 12、quad 8）；删除出现频率 <5% 或 >95% 的序列（删 10 个），并"保留一个单位矩阵以满足 Q 矩阵完备性和模型可识别性"。**最终 28 道虚拟题目**（PDFPAGE 5–6）。对比：不含迷思概念时仅 10 道（附录 S3.1/S3.2）。
5. **作答编码**：行动序列**包含**某虚拟题目对应序列 → 该题"正确作答"=1，否则 =0（PDFPAGE 6）。示例：FBABCD 的 28 位向量 = (1111100010100110001000100001)'。
- **谁编码**：自动算法 + 作者依据任务结构定义。**论文未报告 coding scheme 文档、编码者一致性 / agreement、conflict resolution。**

### 10.5 Cognitive Interpretation
- (a) Explicitly defined by theory：**部分**。属性界定"根据任务要求、评分规则和测量目标（探索与理解，OECD 2014）"（PDFPAGE 5）。但具体属性是研究者从任务界面选项直接转写的。
- (b) Defined by expert / Q-matrix：**是，这是主渠道**。Q 矩阵由作者基于任务状态转移结构界定："若呈现行动序列 i 需要参与者掌握潜在属性 k，则 q_ik=1"；正确状态转移→技能、错误状态转移→迷思概念（PDFPAGE 5）。
- (c) Derived statistically：**无**。
- (d) Interpreted post hoc：**有**。图 4 相关矩阵解读、5 道低质量虚拟题目高失误参数的事后解释、个案解释（PDFPAGE 7–9）。

### 10.6 Mapping
三段链（逐箭头看依据）：
- **Observable → Process Feature**：log-file 事件 ↓（预处理规则：剔除起止状态、删 CANCEL、压缩重复、字母编码）→ 行动序列（A–I 字母串）；↓（N-gram 包含编码）→ 28 个虚拟题目 0/1 作答向量。**依据：作者定义的编码规则（可复核、透明）。**
- **Process Feature → Cognitive Construct**：字节片段/状态转移 ↓（Q 矩阵，q_ik=1 iff 呈现序列 i 需要掌握属性 k）→ 技能 a1–a4 与迷思概念 m1–m4。**依据：作者从任务结构直接规定的假设（"假设仅当参与者掌握了各行动序列所需的潜在属性后才能呈现该行动序列"，PDFPAGE 5）。这是无独立证据的关键环节。**
- 例：状态 F（选城市地铁）→ m1；转移 FB → {a2, m1}；转移 AG → {a1, m2}；转移 GC → {a3, m2} 等（表 2 Q 矩阵，PDFPAGE 6）。

### 10.7 Who Defines the Mapping?（强制）
**映射由论文作者（研究者）定义**，依据是 TICKETS 任务的"清晰的问题状态转移结构"、任务要求、评分规则和 OECD 测量目标（PDFPAGE 5）。**论文没有说明是否有独立专家小组、编码手册、专家一致性检验或 OECD 官方验证 → NOT CLEARLY REPORTED**（全文无"专家/编码者一致性/kappa/访谈"等字样）。**迷思概念 = 界面错误选项对应的理解**：在每个强制二选一界面中，正确选项→技能属性，错误选项→迷思概念属性。凡行动序列包含相应错误状态转移，就认为需要对应迷思概念属性。"错误→迷思"的对应是**输入假设，不是经验发现**。

### 10.8 Q-Matrix / Attribute Structure
8 个属性（4 技能 + 4 迷思概念）。Q 矩阵由研究者按状态转移结构界定；表 2：8 个一元题目 A–I 构成单位子矩阵（A→a1、B→a2、C→a3、D→a4、F→m1、G→m2、H→m3、I→m4）；二元/三元/四元题目的负载 = 构成状态的属性并集，部分行同时含技能与迷思概念（AG={a1,m2}、FB={a2,m1}、BH={a2,m3}、CI={a3,m4}、GC={a3,m2}、GH={m2,m3}、ABH={a1,a2,m3}、AGC={a1,a3,m2}、FBC={a2,a3,m1} 等）。
- **专家参与**：只有作者本人；无独立专家评审（NOT REPORTED）。
- **Q 矩阵验证**：**无**（未用 de la Torre 2008 之类实证 Q 验证；仅"保留单位矩阵"保证可识别性）。
- Attribute hierarchy：无正式层级分析；但任务结构隐含路径顺序（A→B→C→D），较长 n-gram 负载 = 状态属性并集。
- **关键回答：Q 矩阵是 measurement input，不是数据自动发现。**

### 10.9 Key Action（重点）
定义："关键行动（操作）编码（key-action coding），即判断每一名参与者的过程数据中是否包含**解决问题所必需的关键行动**，并进行编码（1='包含'，0='不包含'）"（PDFPAGE 2）。脚注⑤："一个问题状态仅包含 1 个关键行动，即参与者在特定任务界面所进行的具体操作"（PDFPAGE 4）。
- 与 correct / necessary / efficient / diagnostically informative action 的关系（按原文还原）：最优行动序列 = "能正确解决问题的最短行动序列"（脚注③，PDFPAGE 2），即正确且高效路径；本文的"关键行动"**不限于正确/必要行动**，同时包含"正确状态转移"（考查技能）与"错误状态转移"（考查迷思概念）两类可诊断信息（PDFPAGE 5）；排除无测量信息的行动（起止状态、CANCEL、连续重复）。**本文的 key action 实质是 diagnostically informative action（正确→技能，错误→迷思概念），而非仅"正确/必要"行动。**

### 10.10 Phantom Item / Item Expansion（重点）
完整链条：原始题目 TICKETS ↓ 行动序列（FBABCD 等）↓ N-gram 拆解 ↓ 28 个虚拟题目（phantom items）↓ DCM（GDINA）。
- **response 编码**：行动序列**包含**该虚拟题目对应字节片段 → 1，否则 0。
- **一道原始题变多少 phantom items**：含迷思概念 28 道；不含迷思概念 10 道（PDFPAGE 5–6）。
- **dependency 是否考虑**：**完全未考虑**。28 道虚拟题目全部来自同一道原始题、同一段行动序列，且是互相嵌套重叠的 n-gram（如 ABCD 含 AB/BC/CD/ABC/BCD），存在结构性重叠。
- **local independence 是否可能被违反**：**存在显著 local-dependence risk**。同一序列派生的题目大量嵌套重叠（呈现 ABCD 则几乎必然同时呈现 A/B/C/D/AB/BC/CD 等），构成结构性共现；但 **marginal dependence ≠ conditional dependence given attributes**——不能仅因两个 phantom items 重叠就在数学上直接证明 Y_i ⊥⊥̸ Y_j | α。稳妥结论：E2 假设/未检验 conditional independence（全文无 residual/local-dependence model），其 28 个 phantom items 的局部独立风险显著且未做处理。
- **共用同一原始任务的风险**：所有属性信息来自单次任务、单次尝试窗口；CANCEL 重启轮被压缩合并，无法区分"多次尝试"与"单次尝试"；保留单位矩阵、删 5%–95% 之外题目的做法使虚拟题目集合对样本频率敏感。

### 10.11 Misconception Diagnosis（最重要）
- **模型里如何区分 lack of mastery 与 misconception**：论文**没有**在同一潜变量模型中把"未掌握技能"和"持有迷思概念"作为竞争性解释同时估计；而是把迷思概念编码为**附加的 4 个二元属性**，与技能属性并列进入 Q 矩阵（PDFPAGE 5）。属性可共存。
- **一个错误 action 为什么能解释成 misconception，而不是偶然错误？** 论文的答案是**纯假设**："假设仅当参与者掌握了各行动序列所需的潜在属性后才能呈现该行动序列"（PDFPAGE 5）。即"呈现错误状态转移"被规定为"需要具备对应迷思概念"，因此错误行动→迷思概念是**编码假设，不是经验证据**。模型层面允许的"随机性"只有 DCM 的 guess/slip 参数，但没有独立证据说明某次错误点击是"迷思概念"还是"偶然失误"。
- **misconception attribute 如何定义/验证**：定义 = 界面错误选项；验证 = 仅内部一致性（分类信度高、与原始得分负相关、模型拟合好），无外部标准。
- **强制核对：论文是否真的区分了"稳定执行错误规则"与"未执行关键步骤"？** **没有。** 论文只是把"出现错误状态转移"编码为需要迷思概念属性；整个行动序列（含 CANCEL 重启的多次尝试）被压缩为一条序列、一张 28 位作答向量，"稳定执行错误规则"的时间一致性证据被丢弃。作者在讨论中承认用了常规 DCM（Kuo et al., 2018; Ma et al., 2024）而非专门含迷思概念的 DCM，理由是两种属性在本文编码下对"呈现概率"影响方向一致（PDFPAGE 11）——**本文把"迷思概念"当作普通的"错误路径属性"处理，没有机制性区分偶然错误与系统性迷思。不要替论文补它没有的理论。**

### 10.12 Multimodal Joint Modeling
**否**。只建模行动序列一种 modal；结果数据（原始得分）仅用于事后描述性相关（图 4），未联合建模。作者把"把行动时间视为虚拟题目作答时间并引入题目作答时间模型/联合模型"列为未来工作（PDFPAGE 11）。

### 10.13 Added Value of Process Data
全部为实证结果（无 simulation；无参数恢复、无 classification accuracy 对照 ground truth）。对比"含迷思概念（a+m）"与"仅技能（a）"两种编码：
- **分类粒度**：仅技能 → 13 种属性掌握模式；引入迷思概念 → 74 种模式；原（1111）类被细分为 15 个子类，约 80% 为（11110000）"无迷思概念"，约 20% 带至少一种迷思概念（PDFPAGE 9）。"高效正确（ABCD）"与"低效正确（FBABCD）"在纯技能编码下同被诊断为（1111），引入迷思概念后可区分。
- **分类信度**（Kreitchmann et al. 2023 修订分类精度，表 4）：a+m 各属性 a1=.9980、a2=.9974、a3=.9975、a4=.9986、m1=.9947、m2=.9996、m3=.9977、m4=.9998，测验水平 **.9899**；a 各属性 a1=.9934、a2=.9961、a3=.9937、a4=.9999，测验水平 **.9852**。结论："额外引入迷思概念不仅没有降低分类信度，还使分类信度略有提高"（PDFPAGE 8、10）。
- **属性-原始得分相关**（图 4）：技能间中到高正相关、与原始得分高正相关（a1=.89、a2=.84、a3=.76、a4=.91）；迷思概念与原始得分中到高负相关（m1=−.78、m2=−.65、m3=−.71）；技能与迷思概念间多为中到高负相关（a1−m1、a2−m2、a3−m3 高负相关）。
- **模型-数据拟合**（表 3）：a+m 编码（28 题）下仅 GDINA 拟合（SRMSR=.0756<0.10）；DINA SRMSR=.1006、DINO=.2483、ACDM=.1554 均不拟合。a 编码（10 题）下仅 DINO 不拟合（SRMSR=.1316）；DINA SRMSR=.0243、GDINA=.0246、ACDM=.0498。作者声明两种编码的数据不可比（PDFPAGE 7）。
- **⚠ 论文内部矛盾（发现）**：正文称 a+m 下"SABIC 倾向于选择 GDINA"（PDFPAGE 7），但按表 3 数字 SABIC GDINA=29718.24 > DINA=29455.78（应选 DINA），与正文矛盾。AIC（GDINA=28522.69 < DINA=28523.91）选 GDINA，BIC/CAIC 选 DINA，与正文一致。仅 SABIC 一处矛盾。
- **题目质量**（图 3 / 表 S2.1）：除 AG（IDI=.6797）、GC（.6932）、ABH（.6504）、AGC（.4559）、FBC（.5928）外，其余题目 IDI 较高；作者解释这 5 题需"跨最优-非最优问题状态转换"（PDFPAGE 7–8）。
- **个案**：AUS000014102620，原始得分 0，纯技能模式（1111），引入迷思概念后（11111110）；作者称其得 0 分"很有可能是共存的迷思概念导致的，并非简单地归因于失误"（PDFPAGE 9）——**这是事后改标签，不是对随机性的检验。**

### 10.14 Validation Evidence（最重要之一）
- Content evidence：**弱**。仅由作者按任务要求、评分规则与 OECD"探索与理解"构念转写（PDFPAGE 5）；无独立内容专家评审。
- Response-process evidence：**NOT PROVIDED**（无 think-aloud、无 retrospective report、无 eye-tracking、无认知访谈）。
- Internal structure：**有内部证据**——模型拟合（a+m 下 GDINA SRMSR=.0756）、题目质量（23/28 高 IDI）、分类信度（属性级 ≥.9947）、相关矩阵方向与任务逻辑一致（事后解释）（PDFPAGE 8）。
- Relations to other variables：仅原始得分相关（技能正、迷思概念负）；无外部测验、无成绩/学业变量。
- Consequences：**NOT PROVIDED**（无干预研究；只声称"有助于实施有针对性干预"）。
- Convergent evidence：**NOT PROVIDED**。
- Discriminant evidence：**NOT PROVIDED**（技能与迷思概念虽声称可共存，但其区分效度未检验；a1−m1、a2−m2、a3−m3 的高负相关甚至给区分效度带来疑虑，作者归因于"二选一任务"的特殊性，PDFPAGE 8）。
- Expert evidence：**NOT PROVIDED**（作者自任定义者）。
- Think-aloud / Retrospective / Eye tracking / External criterion：全部 **NOT PROVIDED**。

### 10.15 Ground Truth
cognition / process label 来源：**expert（作者）/ task design / Q-matrix**。无 think-aloud、无学生自报、无外部测验、无正确解题路径的独立导出。**存在"模型输出即被当作真值"的结构**：DCM 输出的属性掌握模式本身就是诊断结果，没有独立真值核对分类正确率。

### 10.16 Circularity Risk（强制，重点）
链条：作者假设"状态 F=需 m1、转移 FB=需 {a2,m1}…"→ 写入 Q 矩阵（输入）→ 参与者的行动序列按**同一套映射**编码为 28 位作答向量 → DCM 估计属性 → 结论"该生具有迷思概念 m1"。**模型基本是把研究者假设重新输出了一遍**。缓和因素：(1) DCM 引入潜变量结构与 guess/slip 参数，同一错误行动并非强制推断为属性缺失/持有；(2) 拟合指标、题目质量、相关方向是经验结果。**但**：(a) 作答向量与 Q 矩阵同源于作者的状态图定义，两者高度一致是编码自洽而非独立验证；(b) 分类更细（13→74 模式）是属性数翻倍的必然结构后果；(c) 信度微升（.9852→.9899）与 28 个互相重叠 n-gram 的题目冗余高度相关；(d) 迷思概念与原始得分负相关在很大程度上是**内建**的（错误转移→低分概率高，而迷思概念属性恰由错误转移定义）。**E2 落入该循环：key action→attribute 的映射是模型输入，而非被检验对象。**

### 10.17 Alternative Explanations
呈现状态 F（选城市地铁）：随机误点、界面理解偏差、未读清提示、先探索后纠正，均可解释；论文一律归为 m1。呈现 FB：探索/犹豫/发现错误后纠正；论文解释为"既掌握 a1（或按 Q 矩阵应为 a2）又具有 m1"（PDFPAGE 5）。呈现 ABCD：可能靠记忆/复制策略/运气；论文归为 a1–a4 全掌握。缺失某 n-gram：可能是界面约束（须先选 INDIVIDUAL 才能到搭乘次数；CANCEL 重置；允许漏选直接 BUY），而非属性未掌握。连续重复点击：被压缩丢弃（论文自认可能含"犹豫不决"信息，局限六，PDFPAGE 11）。**论文未系统排除这些替代解释。**

### 10.18 Temporal Alignment
**几乎不考虑**。仅序列内顺序经 n-gram（转移）体现；绝对时间、行动时距、点击次序的时间间隔均被忽略（局限五，PDFPAGE 11）。CANCEL 重启的尝试轮次被压缩，"答题前/答题后的关键行动"区分不复存在。

### 10.19 Person / Item / Task / Context Dependency
属性与状态字母（A–I）**完全任务特异**，作者自认"属性颗粒度小→定义具体、跨任务适用性低、需逐任务重定义属性/虚拟题目/Q 矩阵、多任务测验'昂贵'"（局限二，PDFPAGE 11）。二选一界面使技能与迷思概念呈现"互斥性假象"（局限四，PDFPAGE 11）。n-gram 频率删题（5%–95%）使题目集依赖样本分布。

### 10.20 Generalization
**无**。仅一道 PISA 2012 题（CP038Q02）、仅 well-defined 任务。无 new student / new item / new task / new domain 验证。作者自认"结构良好任务"与"不良结构任务"是否适用新方法"尚不明确"（局限三，PDFPAGE 11）。

### 10.21 Evaluation
- 分类精度/参数恢复/RMSE/bias：**无**（无 simulation study）。
- 分类信度：Kreitchmann et al. (2023) 修订分类精度指标，表 4（见 §13）。
- 模型拟合：SRMSR、AIC、BIC、CAIC、SABIC、卡方——表 3 全部数字见 §10.13。
- 题目质量：IDI（de la Torre, 2008），表 S2.1/S2.2。
- 实证样本量：N=3547；软件：R 包 GDINA。

### 10.22 Transfer to Our English Reading System
- **Directly Transferable**：总体范式——把"是否出现某类可诊断行动"编码为 phantom item 0/1 并跑 DCM（GDINA）；"把潜在属性细化为小颗粒度并检验其在 Q 矩阵下的稳定估计"的框架；相对拟合指标 + SRMSR + 分类信度的评价思路。
- **Transfer With Modification**：① 本文要求离散状态图（A–I）与二选一结构；我们的自由阅读是连续事件流（滚动/悬停/划线/选区），需先定义"有意义状态/行动"，状态空间需自定义且更开放。② 迷思概念的转写：本文把"界面错误选项"直接当迷思；我们在阅读 + 多选题里需把"错误作答模式/错误划掉选项/对某段落的错误关注"映射为迷思属性，映射的合理性与稳定性需额外验证（本文对此没有答案）。③ 无强制顺序下"包含某 n-gram"的定义需改（自由行为可重复、无固定转移图）。④ 本文忽略时间/重复信息，我们系统天然记录时间戳与回看次数，可做得更好。⑤ 多题/多 passage 时需处理 phantom item 依赖（本文未处理）。
- **Not Transferable**：本文的具体 Q 矩阵、状态字母、28 题集合、m1–m4 迷思清单；"单一 well-defined 任务"的分析设定；**"错误行动 = 迷思概念"未经检验的编码假设若直接搬用，会把我们的系统带入同样的循环风险。**

### 10.23 What This Paper Does NOT Establish
1. 未建立"错误 key action = 迷思概念"的 construct validity：无独立证据（无 think-aloud/访谈/眼动/外部标准/专家评审）说明"呈现错误转移"反映稳定迷思概念而非偶然错误、界面因素或探索行为；该映射是输入假设。
2. 未建立 Q 矩阵的经验有效性：无 Q 矩阵验证、无编码者一致性、无内容专家评审。
3. 未充分检验 phantom items 的 local independence：28 题同源于一条序列、互相嵌套，存在显著 local-dependence risk；论文仅假设 conditional independence 并以 item-level fit 检查，未用专门的 residual/local-dependence model 验证。
4. 未提供分类正确率 / ground truth 对照：无模拟研究、无参数恢复、无外部准则。
5. 未建立"引入迷思概念更优"的外在证据：更细分类是属性扩容的结构后果；信度增益微小（.9899 vs .9852）；负相关部分由编码内建。
6. 未区分"稳定执行错误规则"与"未执行关键步骤"；未建模错误一致性 / 多次尝试。
7. 未推广到不良结构任务、多路径任务、多任务测验；未建模行动时间与重复行动的犹豫信息。
8. 未检验技能与迷思概念的区分效度（a1−m1、a2−m2、a3−m3 高负相关仅被归因于任务结构）。
9. 另：正文关于"a+m 下 SABIC 倾向 GDINA"的表述与表 3 自身数字（DINA 更小）矛盾；正文"FB 呈现者既掌握 a1 又具有 m1"与表 2 Q 矩阵中 FB={a2,m1} 不一致（疑为 a1/a2 笔误）。

## 4. E3 — Diagnostic Classification Analysis of Problem-Solving Competence Using Process Data: An Item Expansion Method

> **论文定位**：**E2 的方法学基础**——Key Action → Phantom Item → Q-matrix → DCM。Zhan & Qiao (2022)，*Psychometrika*（online-first）。E3 是 E2 的方法学前身：**E2 把 E3 的 item-expansion / phantom-item 方法思想扩展到 skills + misconceptions 的联合诊断，但二者不是同一道题、也非同一分析数据集（E2=CP038Q02、N=3547、28 题，其自身不含迷思概念的 baseline 为 10 题；E3=CP038Q01、N=3760、14 题，§36）——不能写成"E2 是 E3 的 14 个 phantom items 加迷思概念扩容到 28"**。

### 10.1 Research Question
提出 item expansion method，把 action-level process data 从 DCM 视角做诊断分类分析，目的同时 (a) 沿连续谱估计 problem-solving ability 与 (b) 按 problem-solving skills 的掌握状态对被试分类（PDFPAGE 1–2）。类别归属：process-data modeling + diagnostic classification / cognitive diagnosis；涉及 construct validity（4.5 节 reliability & validity）。**真实数据实证论文（PISA 2012），非模拟。**

### 10.2 Construct
用论文自己的术语：**problem-solving competence**（测量对象）、**problem-solving ability**（higher-order 潜能力 θn）、**problem-solving skills**（5 个 latent attributes α1–α5）：α1 理解城市地铁及正确轨道交通网、α2 理解有优惠票价、α3 理解日票或四张单程票可乘车四次、α4 比较两种票价找最便宜的、α5 做出购票决定（PDFPAGE 9）。对应 PISA 目标认知过程 "exploring and understanding"（OECD 2014）（PDFPAGE 9）。

### 10.3 Observable Process Data
- **Raw Observable**：unformatted process data——log 文件中顺序记录的 action sequence（鼠标点击等）+ 对应 time stamps + ID 指标（PDFPAGE 2）；本文具体为虚拟售票机上的 13 种离散 action：city subway、country train、concession、full fare、daily、individual、trip1–5、cancel、buy（PDFPAGE 9–10）。
- **Derived Process Indicator**：phantom items——由 action sequences 经筛选后形成的二分变量（出现=1，否则=0），构成 formatted process data 矩阵（PDFPAGE 7）。
- **time stamps 虽在原始数据中，但本研究未使用**（明确列为限制，PDFPAGE 17）。

### 10.4 Process Feature Construction
三步流水线（自动 + 专家判断混合）：
1. 由 action space A（13 个动作）生成相邻组合的 action sequences S，长度 1–5，X = **228** 条（PDFPAGE 10）。
2. 筛选 S*：(i) 出现率 <5% 或 >95% 的剔除（引 Tang et al. 2020）→ 剔除 <5% 后剩 **60** 条，无 >95% 的；(ii) 保留理论上能反映前述技能的动作序列（Sao Pedro et al. 2012）→ 剩 **14** 条；(iii) 满足 DINA 可识别性条件（Gu & Xu 2019：含单位阵、每属性至少 3 题、非单位阵各列互异）（PDFPAGE 10）。**S* 中的动作序列即 phantom items，14 个。**
3. 编码：重复动作全部二分（出现 ≥1 次即记 1）；"ind → other → trip 4" 与 "ind → trip 4" 合并；日票与 trip4 视为等价（共指 α3），生成 "daily/trip4" 类 phantom items（PDFPAGE 10）。最终 3,760 人 × 14 个 phantom items 的 0/1 矩阵。
无独立 coder/agreement 报告；筛选与合并依赖专家判断（PDFPAGE 10）。

### 10.5 Cognitive Interpretation
- (a) Explicitly defined by theory：5 个 skills 由 test blueprint、scoring rules 与目标认知过程（OECD 2014 的 PISA 框架）确定（PDFPAGE 9）。
- (b) Defined by expert / Q-matrix：Q-matrix 由 expert judgment 构建，论文明确写 "based on expert judgment and is essentially retrofitting...aligned the phantom items to the problem-solving skills in a post hoc manner"（PDFPAGE 7）。
- (d) Interpreted post hoc：latent classes 的解释是事后回读 action sequences 得出的（如 pattern 01001 → "买了 country train 单张优惠票"、pattern 11001 → "买了 city subway 两张优惠单程票"），见 PDFPAGE 14–15。
- (c) Derived statistically：没有用纯统计方法定义指标；PVAF 只做 Q-matrix 验证且被否决（见 §8）。

### 10.6 Mapping
Observable（动作序列/点击）↓ [item expansion + 出现率筛选 + 理论筛选 + 二分编码] → Process Feature（phantom item 0/1）↓ [Q-matrix：专家事后 retrofitting] → Cognitive Construct（problem-solving skill αk）↓ [HO-DINA 合取规则 + higher-order θ] → ability。
箭头依据：(1) 出现率筛选是数据驱动（5–95% 规则）；(2) 理论/技能筛选与 Q-matrix 是研究者/专家判断（PDFPAGE 7）；(3) 合取规则是模型选择结果（HO-DINA 拟合最优）而非先验设定（PDFPAGE 12–13）。

### 10.7 Who Defines the Mapping?
**明确报告**：研究人员/领域专家——"use the test blueprint, scoring rules, and assessment framework to determine the required problem-solving skills"（PDFPAGE 6）；Q-matrix "based on expert judgment and is essentially retrofitting...in a post hoc manner"（PDFPAGE 7）。无 think-aloud、无学生自报、无外部标准。

### 10.8 Q-Matrix / Attribute Structure
14×5 Q-matrix（Table 1，PDFPAGE 11），由专家预设。**Q-matrix 是 measurement input（研究者预设），不是数据自动发现**。假设 5 个 skill 间**无 attribute hierarchy**（Leighton et al. 2004）（PDFPAGE 10）。用 higher-order 结构（HO-GDINA/HO-DINA）处理属性间相关并给出整体能力 θn（PDFPAGE 4）。**Q-matrix 验证：PVAF 法（de la Torre & Chiu 2016）得到的 revised Q 拟合反而更差（RMSEA2 = 0.085 [0.079, 0.091] > 0.05），结合专家判断保留 original Q（PDFPAGE 12）——经验验证被否决，专家输入获胜。**

### 10.9 Key Action
"key actions" 出现在 3.1 节对 phantom items 的定义："phantom items, expanded from the CBA item, representing key actions or action sequences produced by respondents during their completion of the CBA item"（PDFPAGE 4）。即 **key action = 被选入 S* 的、理论上与技能相关的 action/action sequence（phantom item）**。
- 与 correct action 的关系：对 phantom item 的 "correct response"（yni=1）就是"出现了该动作序列"（PDFPAGE 7）；"答对"含义被重定义为"执行了动作"。
- 与 efficient action 的关系：题目不考效率，低效路径（"ind → other → trip 4"）与直接 "ind → trip 4" 合并处理（PDFPAGE 10）。
- 与 diagnostically informative action 的关系：按 Sao Pedro et al. (2012) 只保留理论上能反映技能的序列（PDFPAGE 10）。
**即 key action 既非"最终正确动作"，也非"必要动作"，而是"专家认为有诊断信息且出现率适中的动作序列"。**

### 10.10 Phantom Item / Item Expansion（重点）
完整链路：Original Problem（TICKETS task 2，CP038Q01，单一 PISA 题）↓ Action Sequence（13 动作 → 228 序列 → 14 个 S*）↓ Phantom Items（14 个二分题）↓ DCM（HO-GDINA → HO-DINA）。
- **phantom item 的 response**：0/1 = 该动作序列在被试解题过程中是否出现至少一次；出现记 1（即 "correct response"）（PDFPAGE 7）。
- **1 道原始题 → 14 个 phantom items**（PDFPAGE 10）。
- **dependency 是否考虑**：论文显式假设所有 phantom items 在给定 latent attributes 下条件独立，并把局部独立检验交给 item-level 拟合（PDFPAGE 10）。
- **local independence 是否可能被违反**：**存在显著 local-dependence risk**。所有 phantom items 来自同一道题、同一被试的同一段 log，结构性共现明显（做长序列必然做了其前缀序列，如 phantom 14 "city→con→daily/trip4→buy" 出现则 phantom 1 "city" 必出现）。**但 E3 原文明确定义 phantom-item responses are assumed to be conditionally independent given requisite latent attributes，且作者主张 item-level model-data fit 可反映 local independence 情况；marginal dependence 不等于 conditional dependence given attributes，不能仅因重叠就证明 Y_i ⊥⊥̸ Y_j | α。** 稳妥结论：E3 假设 conditional independence，但没有通过专门的 residual/local-dependence model 做充分检验（只靠 item-level fit）。
- **共用同一原始任务的风险**：共用一个作答场景导致共享情境变异（item context effect）、前缀决定关系造成近似确定性依赖、样本量被同一批被试重复使用（14 个 phantom items 都来自同 3,760 人），分类精度估计可能被高估。论文承认这是 item-specific 方法（PDFPAGE 5）。

### 10.11 Misconception Diagnosis
论文不建模 "misconception" 潜状态，而是：一个动作序列按 Q-matrix 只要求部分属性，执行它只反映"会做购买决定"，不代表掌握其他技能（PDFPAGE 10）。缺失技能（αk=0）与"错误动作"通过 Q-matrix 绑定：错误路径 = 缺乏相应 skills 的证据。对特定错误类型（01001、11001）的解释是**事后回读**动作序列完成的（PDFPAGE 14–15）。"错误动作 vs 偶然错误"靠 Q-matrix（专家判断）+ latent class 频率（01001 有 72 人、11001 有 157 人）支撑，无个体错误的归因检验。

### 10.12 Multimodal Joint Modeling
**未实现联合建模**。只使用 action sequence 单通道；time stamps 未用（PDFPAGE 17）。outcome data（0/1/2 分）不作为 joint likelihood 一部分，只作为外部比较对象——PCM 单独拟合 outcome data，与 HO-DINA 的 θ1 比较（PDFPAGE 11、15）。无 common latent variable 跨通道联合似然，无 cross-loading。

### 10.13 Added Value of Process Data
真实数据（PISA 2012），非模拟。核心数字：
- **潜在类别比观察得分类别更细**：得分 2 → 全部为 11111（n=1093）；得分 1 → 11111（n=156）与 11101（n=1481）；得分 0 → 25 种 pattern（PDFPAGE 13–14）。
- **能力估计**：θ1（HO-DINA）与 θ2（PCM）相关 **0.826（p < 0.001）**（PDFPAGE 15）；PCM 只给出 3 个能力值（−0.733、−0.012、0.709），而 HO-DINA 在得 0 分组内显示差异。
- **SE 比较**：依赖 t 检验 **t(3759) = −115.58, p < 0.001**，θ1 的平均标准误显著小于 θ2（PDFPAGE 15）。论文据此主张"即使只有一道题，过程数据的高阶能力比 outcome 单维能力更精确"。
- **分类可靠性**：classification accuracy index（Wang et al. 2015），细节在在线附录 S2（不在主 PDF 内）。
> **Improved diagnostic performance does not by itself establish construct validity**——"更细的分类 + 更小的 SE"是模型对过程数据的再组织结果，不验证 phantom item→skill 的映射正确。

### 10.14 Validation Evidence
- Content evidence：弱专家证据——skills 来自 blueprint/scoring rules/框架（PDFPAGE 9）。
- Response-process evidence：**NOT PROVIDED**（无 think-aloud、无回溯报告）。
- Internal structure：**有**——test-level fit RMSEA2 = 0.032 [0.025, 0.041]，SRMSR = 0.033；item-level fit 经 Fisher 变换相关检验，phantom 5 "buy" 失配（PDFPAGE 12）。
- Relations to other variables：**有**——corr(θ1, θ2) = 0.826（PDFPAGE 15）。
- Consequences：**NOT PROVIDED**。
- Convergent evidence：与 outcome 的 PCM 能力相关 0.826，可算弱趋同证据；无独立判别证据。
- Expert evidence：Q-matrix 为专家判断（PDFPAGE 7）。
- Think-aloud / Retrospective / Eye tracking / External criterion：**NOT PROVIDED**。
- 论文声称的 "validity evidence"（4.5 节）主要是对 latent classes 的解读与对能力的解释，属后验解释，非外部效标验证（PDFPAGE 15）。

### 10.15 Ground Truth
skills 与 Q-matrix：expert-defined（researchers 依据 blueprint/scoring rules/framework，PDFPAGE 6–7）。"正确解法路径"由题目设计给定（买 4 张 city subway 优惠单程票并比较价格，PDFPAGE 8）。observed score categories（0/1/2）作为外部锚点。无 think-aloud / student self-report。**循环嫌疑**：Q-matrix 的构建依据与 outcome scoring rule 同源（OECD 2014），latent classes 又与 observed scores 比较，因此"潜在类别比观察得分更细"部分是"用同源规则重排后"的结果。

### 10.16 Circularity Risk
存在。研究者用专家判断把 action sequence ↔ skill 的映射（Q-matrix）作为**模型输入**；HO-DINA 在此输入下估计出 latent classes；论文结论"特定动作序列只在掌握全部所需技能时出现（合取规则）"来自模型输出，而该模型正是在这套 mapping 输入上拟合最优。**模型拟合良好不能独立验证 mapping 正确，因为 mapping 是前提。** 误分类解释（n=3 与 n=29）被归为估计误差，也无独立手段检验（PDFPAGE 15）。

### 10.17 Alternative Explanations
论文排除/承认的替代解释有限：
- "buy" 动作的高 guess 参数 gi = 0.442（IDI = 0.558）：归因于"题目说明里写着要买票"，不需要多少认知努力（PDFPAGE 12–13）——这是论文主动给出的替代解释。
- 得分 1 但 pattern 11111 的 156 人：可能比较了价格但仍选择更贵的日票——即**替代策略/偏好**，而非技能缺失（PDFPAGE 14）。
- 未系统排除：未执行某动作可能是界面困惑、随机点击、探索性点击、时间不足，而非技能未掌握；某些动作出现可能只是顺手的必然步骤。

### 10.18 Temporal Alignment
时间戳未使用（PDFPAGE 17）。但动作顺序被保留——phantom items 是相邻动作的有序组合，序列顺序编码在 item 定义中（PDFPAGE 6、10）。**顺序维度对齐，时间维度未对齐**（无动作时距、无先答后答的时间结构分析）。

### 10.19 Person / Item / Context Dependency
方法 item-specific：论文明确承认各 CBA 题目场景差异巨大，方法逐题实施（PDFPAGE 5）。skills 与 Q-matrix 依题目而定；本题目只含一条正确解决策略，多策略情形未被验证（PDFPAGE 17）。被试来自 4 国，国家差异未进入模型（background variables 未考虑，PDFPAGE 17）。

### 10.20 Generalization
**仅在单题内验证**。只有 1 个 PISA 题（CP038Q01）、一个认知过程（exploring and understanding）、4 国样本。sensitivity analysis 只是对同一道题构造"更少/更多 phantom items"的 Q-matrix 与数据，分类结果相似（PDFPAGE 15）——这是 within-item 稳健性，不是 cross-item / cross-domain 概化。无 new student / new item / new task 验证。

### 10.21 Evaluation
- 模型拟合：original Q：RMSEA2 = 0.032 [0.025, 0.041]，SRMSR = 0.033；revised Q：RMSEA2 = 0.085 [0.079, 0.091]，SRMSR = 0.017（PDFPAGE 12）。
- 相对拟合（Table 3，PDFPAGE 13）：HO-GDINA（#par=92, −2LL=16,951.31, AIC=17,135.31, BIC=17,708.67）；HO-DINA（#par=38, −2LL=17,014.83, AIC=17,090.83, BIC=17,327.65；LRT χ²=63.52, df=54, p=0.180）；HO-DINO（AIC=31,380.61；χ²=14,353.31, df=54, p<0.001）；HO-ACDM（#par=54, AIC=20,287.61；χ²=3,228.31, df=38, p<0.001）。HO-DINA 最优且与 HO-GDINA 无显著差异 → 采纳合取规则。
- Item 参数（Table 4）：gi、si、IDIi = 1 − si − gi 逐题列出；除 phantom 5（buy）外 gi 均很小，si 多为 0。
- 分类：26 个观测 latent patterns；得分 2/1/0 人数 1093/1637/1030；理论 pattern 数 2⁵ = 32（PDFPAGE 13）。
- 能力：corr(θ1, θ2) = 0.826；t(3759) = −115.58, p < 0.001（PDFPAGE 15）。
- 可靠性：classification accuracy index（Wang et al. 2015），数值在主 PDF 外的附录 S2。
- 真实数据，非 simulation；无 parameter recovery / RMSE / bias 类指标。

### 10.22 Transfer to Our English Reading System
- **Transfer With Modification / Methodological Candidate**（反馈修正：不再列为 Directly Transferable）：item expansion 的完整流程（action space → action sequences → 筛选 → phantom items → 0/1 → Q-matrix → GDINA）可作为**方法学候选**迁移，但有两个结构性差异：(1) PISA TICKETS 是 well-defined finite action space + structured interface + clear task path，而自然阅读是 open behavior space + multiple valid strategies + no canonical action sequence——action 的定义与序列化需针对阅读行为重设计；(2) **5%–95% 出现率过滤只是 E3 的 operational choice，绝不能直接迁移为我们的固定 threshold**，需按我们的行为分布重新标定。识别条件（单位阵、每属性 ≥3 题、列互异）与模型选择逻辑（AIC/BIC/LRT）可借鉴；Q-matrix 需阅读领域专家重建；技能定义（α1–α5）不可照搬；多 passage 需把单题扩展改为多题联合；本论文未用时间戳，而我们系统有作答时间，可借鉴 E1 的 RT-CDM 补充。
- **Not Transferable**：具体的 PISA 售票机技能集与 Q-matrix；"合取规则"结论（HO-DINA 在该题上最优）不能外推到阅读任务；"latent class 比 observed score 更细"的论断不能直接移植（它是该题 scoring rule 与模型输入同源的结果）。

### 10.23 What This Paper Does NOT Establish
1. 未建立"action sequence = skill mastery"的 construct validity——mapping 是专家输入，没有外部效标、think-aloud 或独立测量验证。
2. 未实证排除 phantom items 的 local dependence（仅假设 + item-level fit 检查；前缀确定性依赖结构明显）。
3. 未建立跨题目/跨领域概化（单题、单认知过程）。
4. 未使用时间戳/速度信息，对"过程数据 = 行动 + 时间"中的时间维度零贡献。
5. 未给出 classification accuracy 的具体数值（附录 S2 不在主 PDF，且是基于模型自身的一致性/精度指数，无真值对照）。
6. 未做"有无过程数据"的对照（同属性集下 process 版 vs outcome 版的分类精度差）来量化过程数据增益；其"更精确"的主张只来自 SE 比较与和 PCM 的相关。
7. 未处理多策略题目、未考虑背景变量、未联合建模多道 CBA 题（均为论文自陈限制，PDFPAGE 17）。

---

## 5. E4 — Cognitive Diagnosis Modeling Incorporating Response Times and Fixation Counts

> **论文定位**：**Multimodal Process Evidence → Cognitive Diagnosis**。Zhan, Man, Wind & Malone (2022)，*JEBS* 47(6): 736–776。注意：当前 E4 已正式替换为这篇（任务文件标注），不是早期计划的 "Using Process Data to Improve Classification Accuracy of Cognitive Diagnosis Model"。

### 10.1 Research Question
解决"如何在认知诊断框架下同时纳入 outcome（RA）、process（RT）、biometric（FC）三类数据，提供更全面反馈与更准确诊断"（PDFPAGE 5）。提出 **MJ-DINA（Multimodal Joint-Hierarchical DINA）**，同时建模 RA、RT、FC。类别归属：process-data modeling + cognitive diagnosis + multimodal measurement（作者用 "multimodal data / parallel data" 概念，引 Jeon et al., 2021）。具体问题：(a) 参数能否恢复（Simulation 1）；(b) joint modeling 相对 separate modeling 是否有增益（Simulation 1）；(c) 忽略 FC 会有什么后果（MJ-DINA vs JRT-DINA，Simulation 2）；(d) 实证应用。

### 10.2 Construct
用论文自己的术语，测量/推断的 construct 有四类：
- **latent attributes αnk**（knowledge structure，如 arithmetic/algebra/geometry/data analysis）（PDFPAGE 6、25）；
- **higher-order latent ability θ**（attribute 之上的二阶能力）（PDFPAGE 6）；
- **latent processing speed τ**（问题解决效率）（PDFPAGE 7）；
- **latent visual engagement ε**（视觉投入，FC 背后的潜在变量）（PDFPAGE 8）。
推断层面还有 **cognitive characteristics**：cognitive fluency、reflective–impulsive cognitive style、focuser–nonfocuser style（PDFPAGE 2、12）。

### 10.3 Observable Process Data
- **Response accuracy Yni**：二分正确/错误，每 item 一个（传统 outcome data）。
- **Response time Tni**：每 item 耗时（process data，计算机化 TEA 系统记录）。
- **Fixation count Vni**：每 item 的注视次数（biometric data，实验室眼动仪）。实证设备为 **Gazepoint**；FC 由设备自动生成，采用 **position-variance（基于 visual displacement，Jacob 1995）** 算法（Gazepoint 默认注视检测算法）；注视中心可随新数据漂移；注视点聚集在一个局部区域计为一次 FC（PDFPAGE 25–26）。Note 3 明确：FC = "位于 area of interest 内的 fixation 数"（PDFPAGE 35）。
- **Raw Observable**：Yni（0/1）、Tni（连续秒）、Vni（非负整数计数）。
- **Derived Process Indicator**：log(Tni) 对数变换；FC 直接作为计数观测，经 NBF 模型分解为 person 项 εn 与 item 项 mi。

### 10.4 Process Feature Construction
- **RT**：对数正态模型，`log(T_ni) ~ N(ξ_i − τ_n, ω_i^(−2))`（Eq. 3/4）。分解为 item time-intensity ξ_i、person processing speed τ_n、time-precision ω_i。
- **FC**：负二项模型 `V_ni ~ NB(exp(ε_n + m_i), d_i^(−2))`（Eq. 5/6），E(V_ni) = exp(ε_n + m_i)；ε_n 为 person latent visual engagement，m_i 为 item visual-intensity，d_i 为 visual-discrimination 参数。假设 person 的 latent visual engagement 全程恒定（PDFPAGE 8）。
- **Simulation 生成**：Yni 按 Eq.(1) Bernoulli；log(Tni) 按 Eq.(4) 正态；Vni 按 Eq.(6) 负二项；αnk 按 Eq.(2) Bernoulli。item 参数从四维 MVN 抽取（μb=−2.197, μd=4.394, μξ=4, μm=4；相关 r_bd=.5, r_bx=−.5, r_bm=−.5, r_dx=−.5, r_dm=−.5, r_xm=.5，PDFPAGE 15）。

### 10.5 Cognitive Interpretation
- (a) Explicitly defined by theory/文献：FC 被解释为"对目标视觉区域注意强度（intensity of attention）"的指标、attention 强度的代理（surrogate）、认知过程负荷的代理（PDFPAGE 4，引 An et al. 2017; Justice & Lankford 2002; Aslin 2012）。**限定句**："the term 'visual engagement' reflects only the **visual cognitive process loading amount endorsed by FCs rather than the entire visual attention**...the engagement level **depends on the context**"（PDFPAGE 4）。
- (b) Defined by expert / Q-matrix：属性与 RA 的对应由 Q-matrix 定义（确认式输入）；FC/RT 与 latent 变量的对应不由 Q-matrix 定义。
- (c) Derived statistically：RT→τ、FC→ε 的映射由所选测量模型（lognormal RT、NBF）定义；ε 与 θ、τ 的关联通过 Σperson 相关结构统计估计（不预先限定正负）。
- (d) Interpreted post hoc：Table 2 把 (θ, τ, ε) 高低组合推断为 fluency + focuser 等 8 类认知特征；**论文明确警示 "relatively rough...rather than an accurate measurement or diagnosis"**（PDFPAGE 11）。

### 10.6 Mapping
1. **RA (Yni) ↓ latent attributes αnk**——依据：DINA item response 函数（Eq.1）+ Q-matrix（研究者/专家输入）。
2. **RT (Tni) ↓ latent processing speed τn**——依据：lognormal RT 模型的测量假设（van der Linden 2006 理论设定）。
3. **FC (Vni) ↓ latent visual engagement εn**——依据：NBF 模型 + 眼动文献"FC≈注意强度/视觉注意负荷"的理论背书（PDFPAGE 4）。
第二层把 α、τ、ε 与 θ 用 trivariate MVN 相关结构连接（Σperson，Eq.8），属性再经更高阶结构链接到 θ。**关键点：FC 不加载在属性 α 上**（条件独立假设 8：Vni ⊥ αn,τn | εn，PDFPAGE 10）。

### 10.7 Who Defines the Mapping?
- 模拟中：Q-matrix 由研究者构造并作为真值输入；RT→τ、FC→ε 由作者选定的测量模型定义；ε→focuser 等标签由作者在 Table 2 中事后定义。
- 实证中：Q-matrix 沿用 Man & Harring (2019) 数据集，本文**未说明**其构建与专家参与过程 → **NOT CLEARLY REPORTED**（Note 8，PDFPAGE 35）。

### 10.8 Q-Matrix / Attribute Structure
模拟 K=5（PDFPAGE 15）；实证 K=4（arithmetic, algebra, geometry, data analysis）（PDFPAGE 25）。**Q-matrix 是输入/确认式，非自动发现**。Study 1 的 Q-matrix 含 1–2 个 identity 子阵以保证可识别（Q-matrix completeness，Chiu 2013; Gu & Xu 2021）。Study 2 比较 complete（Q1）与 incomplete（Q2）。**实证 Q-matrix 的构建/验证过程未报告；论文没有做 Q-matrix validation。**

### 10.9 Key Action
论文**不涉及 key action**。用每 item 的三个聚合观测（RA、总 RT、总 FC），没有对答题内部动作序列建模。讨论中提到可用 Markov/multilevel mixture 模型处理 operating steps 数据作为未来方向（PDFPAGE 32）。

### 10.10 Phantom Item / Item Expansion
**本论文不涉及**。联合建模是三个独立测量模型 + 两层相关结构，没有制造虚拟项目。同一作者组在其他论文（E3，即同目录 Item Expansion Method）处理该问题。

### 10.11 Misconception Diagnosis
**不涉及**。只做属性掌握与否（α∈{0,1}）的认知诊断；参考文献含 Tatsuoka (1983) rule space，但未实施迷思概念诊断。

### 10.12 Multimodal Joint Modeling（最重要小节）
结构：**三合一联合似然 + 两层相关结构**，属 **joint-hierarchical / simple-structure（无 cross-loading）** 框架（沿 van der Linden 2007; Zhan, Jiao & Liao 2018）。

第一层三个测量模型：
- DINA（Eq.1）：logit P(Yni=1) = bi + di·∏αnk^qik
- 更高阶（Eq.2）：logit P(αnk=1) = γkθn − λk
- 对数正态 RT（Eq.4）：log(Tni) ~ N(ξi − τn, ωi^(−2))
- NBF（Eq.6）：Vni ~ NB(exp(εn + mi), di^(−2))

第二层两个 MVN：
- item 参数 Ψi = (bi, di, ξi, mi)' ~ MVN(μitem, Σitem)（Eq.7）
- person 参数 Θn = (θn, τn, εn)' ~ MVN(μperson, Σperson)，Σperson 含 σθ²、στ²、σε² 与相关 σθτ、σθ ε、στε（Eq.8）

**关键设定**：
- RT 和 FC 加载在**各自的独立 latent 变量** τ 和 ε 上，不加载在 attribute 上（simple structure，无 cross-loading）。条件独立假设 (6)–(8)：Yni ⊥ τn,εn | αn；log(Tni) ⊥ αn,εn | τn；Vni ⊥ αn,τn | εn（PDFPAGE 10）。
- 三者相关通过 Σperson 相关项建模，**不约束正负**，"context- and application-specific"（PDFPAGE 9）。信息传导机制 = person 参数间的相关（相关越高信息共享越多）。
- 可识别性：μθ=μτ=με=0，σθ²=1；μd>0；Σperson 用 Cholesky 分解。估计用 JAGS / MCMC。
- 实证估计的 Σperson：r_θτ=−0.125, r_θε=0.182, r_τε=−0.959（PDFPAGE 28）。

### 10.13 Added Value of Process Data
**Simulation Study 1（MJ-DINA vs separate model）**（Table 3，PDFPAGE 17–18）：
- ACCR > 0.9 全条件；最低 PCCR 约 0.7（PDFPAGE 16）。
- Φ=0.8 时 MJ-DINA 的 PCCR 比 separate 高约 **2%**（PDFPAGE 17）。
- joint 相对 separate 的主要收益在**更高阶能力 θ 的恢复**：如 N=100, I=15, Φ=0.8，θ 的 RMSE 从 .698（separate）降到 .507（MJ），Cor 从 .706 升到 .860；而 τ、ε 的恢复几乎不受影响（Table 3）。RT 与 FC 为 θ 的估计提供了有用信息（PDFPAGE 17）。
- item 参数上 joint 的主要收益在 RA 的 item intercept b 与 interaction d（Table 4）。

**Simulation Study 2（MJ-DINA vs JRT-DINA，加入 FC 的增量）**（PDFPAGE 22–24）：
- PPMC：两模型对 RA、RT 的 ppp 均接近 .5（Table 5）；忽略 FC 不会造成 RA/RT 联合建模失配。
- LCPO：ryE/rtE 低（0.2）时 MJ 略差于 JRT；中（0.4）高（0.8）时 MJ 更好。
- PCCR 绝对/相对增量（Table 6）：Q1：Φ=.2/.4/.8 时绝对 .001/.002/.011，相对 0.15%/0.24%/1.58%；Q2：绝对 .003/.004/.030，相对 0.63%/0.68%/**5.49%**。**最大相对增量 5.49%，多数条件 <1%**（PDFPAGE 24）。论文承认收益有限，援引 Ranger (2013)：joint-hierarchical 框架内精度增益普遍有限；只有在 Q-matrix incomplete 时附带信息才有实质增益。
- 论文反复强调 FC 的主要价值是**丰富反馈（comprehensive feedback）**，而非提高参数精度（PDFPAGE 31）。
> **Improved diagnostic performance does not by itself establish construct validity**——FC 的增益经 Σperson 相关结构的信息传导实现，不验证 FC 测量了注意或任何认知技能。

### 10.14 Validation Evidence
- Content evidence：实证为 10 道数学题、4 属性，属性定义列出，但 Q-matrix 构建过程与内容效度论证未报告 → 部分 NOT PROVIDED。
- Response-process evidence：FC 答题过程实时采集（眼动仪），属过程证据；PPMC 表明模型-数据拟合可接受。无 think-aloud/追溯报告。
- Internal structure：模拟参数恢复（bias/RMSE/Cor）、PPMC、LCPO、Σperson 相关结构（Table 9）。
- Relations to other variables：属性掌握数量与 latent ability 正相关；同一属性模式下 θ、τ、ε 仍不同；r_xm=.590（item 时间强度与视觉强度正相关）、r_bx=−.238、r_bm=−.267。
- Consequences：个体反馈示例（Table 10）与针对性干预建议。
- Convergent evidence：item m_i 估计与 Figure 6 原始 FC 箱线图一致；实证 r_xm≈.590 与模拟设定 .5 一致（PDFPAGE 27–28）。
- Discriminant evidence：**NOT PROVIDED**。论文特意提醒强相关不代表同一特质（"height and weight are highly correlated but reflect separate traits"，PDFPAGE 28）。
- Expert evidence：**NOT REPORTED**（实证 Q-matrix 无专家验证描述）。
- Think-aloud / Retrospective：**NOT PROVIDED**。
- Eye tracking：有，Gazepoint，position-variance 注视检测。
- External criterion：**NOT PROVIDED**（数据因高利害考试敏感信息不公开，PDFPAGE 35）。

### 10.15 Ground Truth
Simulation：attribute ground truth 由 Eq.(2) 从已知参数生成真实 α。实证：没有外部认知标签；attribute 分类与 θ/τ/ε 估计全是 **latent model 输出**（后验均值）。"cognitive characteristics"（fluency、reflective–impulsive、focuser）由 (θ,τ,ε) 与 0 比较的粗分类事后贴上（Table 2）。

### 10.16 Circularity Risk
**风险显著**。映射链由研究者预设：Q-matrix 为输入；RT→τ、FC→ε 由作者选定模型定义；模拟用 MJ-DINA 生成数据再自拟合（自我验证）；joint 增益几乎完全由模拟设定的 person 参数相关驱动（Φ 越高增益越大），可视为"重放研究者假设"。实证部分无外部标准，仅描述性。论文自己在 Note 5/6 承认模拟相关假设 "in practice...not always correct...depend on actual situations"（PDFPAGE 35）。

### 10.17 Alternative Explanations
- 高 FC 的可能原因：item 视觉复杂度（论文承认："the more visually complex the item...the more visual effort is required, and the more FCs are observed"，PDFPAGE 26）、个体阅读效率、注意强度、动机、分心、item 难度等。论文把 item 级视觉需求归入 m_i、person 级归入 ε_n，但**未排除**"低效搜索/阅读能力/分心"等替代解释；engagement 意义被限定为 context-dependent。
- 长 RT：论文引入 reflective vs impulsive 风格解释（PDFPAGE 2），但未排除难度、分心等。认知特征推断仅为粗推断，无排除性检验。

### 10.18 Temporal Alignment
**NOT CONSIDERED**。FC 是每 item 的总计数，不区分答题前/答题中/答题后；NBF 假设 ε_n 全程恒定（PDFPAGE 8）。RT 也是每 item 单一总耗时，未分解到动作序列。

### 10.19 Person / Item / Context Dependency
论文**明确建模 person 与 item 依赖**：person 侧 ε_n（person engagement），item 侧 m_i（visual-intensity）、d_i（visual-discrimination）、ξ_i（time-intensity）。但**界面/任务类型/难度**对 FC 意义的调节未检验；"engagement level depends on the context"仅作口头声明（PDFPAGE 4）。

### 10.20 Generalization
Simulation：N=100/500, I=15/30, K=5, Φ=0.2/0.4/0.8（Study 1）；N=100, I=15, Q complete/incomplete（Study 2）。每条件 50 数据集。实证：**N=93 大学生, I=10 数学题, K=4**（PDFPAGE 25）。**仅 within-sample**，无 cross-generalization。作者自认局限：仅小规模（93 人）、模型最简化、硬件限制（PDFPAGE 31–32）。

### 10.21 Evaluation
- **ACCR/PCCR**：MJ 全条件 ACCR > 0.9，最低 PCCR ≈ 0.7；Φ=0.8 时 PCCR 比 separate 高约 2%。Study 2 中 MJ vs JRT 的 PCCR 最大相对增量 5.49%（Q2, Φ=0.8），多数条件 <1%。
- **Person 参数恢复（Table 3）**：θ 的 RMSE .462–.691（条件全距）、τ .104–.150、ε .080–.123；Cor：θ .706–.885、τ .953–.978、ε .966–.987。例 N=500, I=30, Φ=0.8：θ RMSE .462/Cor .885；τ .104/.978；ε .084/.986。
- **Item 参数恢复（Table 4）**：例 N=500, I=30, Φ=0.8：b RMSE .221/Cor .970，d .455/.889，ξ .029/.998，m .026/.999，ω .054/.971。
- **Bias**：各参数 mean bias 接近 0（如 θ bias −.005–.005）。
- **Model fit**：PPMC ppp 均接近 .5（Table 5 模拟 .518–.521(RA)/.499–.502(RT)；Table 7 实证 MJ：RA .511, RT .509, FC .537）。
- **LCPO（实证, Table 8）**：Test-level RA MJ −481.331 vs JRT −481.713；RT MJ −3858.372 vs JRT −3867.084（MJ 优于 JRT）。
- 收敛：PSRF < 1.2，约 99% < 1.05；2 条链各 35,000 迭代，25,000 burn-in。

### 10.22 Transfer to Our English Reading System
（我们的系统无眼动仪，只有鼠标/滚动/UI 事件。）
- **Directly Transferable**：(1) joint-hierarchical CDM 框架（RA+RT+count 类过程指标，两层 MVN 相关结构）；(2) **count-valued process data 可通过显式测量模型纳入**（反馈修正：E4 展示的是"计数值过程数据可经显式测量模型纳入 CDM"，**不是"UI counts 应该用 Negative Binomial"**）——我们若要把滚动/划线/切换次数作为 count 纳入，需先检查 overdispersion? zero inflation? item exposure? window length? person-item dependence?，然后才在 Poisson / NB / ZIP / ZINB / hurdle / ... 中选择；(3) 反馈呈现方式；(4) 论文对"认知特征只能粗推断、不能诊断"的克制立场。
- **Transfer With Modification**：(1) FC 需替换为 **UI 事件计数**（cursor/scroll/selection），但 latent 变量必须改名（如 "behavioral engagement" / "UI engagement"），**不能叫 visual engagement**；cursor ≠ gaze 是 C 组已确认的；(2) RT 直接可用；(3) 论文中 FC/RT 是"答该题期间"聚合值，我们系统无强制顺序、阅读与答题交错，需先定义每个 item 的时间窗与归属规则；(4) Σperson 相关结构、PPMC/LCPO 拟合检验可直接用。
- **Not Transferable**：(1) 眼动 FC 及其"注意强度/视觉注意负荷"语义；(2) focuser–nonfocuser 等基于视觉注意的风格推断；(3) 任何"事件计数 ≈ 认知投入/注意"的直接主张。

### 10.23 What This Paper Does NOT Establish
1. **FC 具有明确认知语义**：论文明确说 visual engagement 只是 "visual cognitive process loading amount endorsed by FCs"，不是完整视觉注意，且 "depends on the context"（PDFPAGE 4）。
2. **FC 提高分类精度 ⇒ FC 有效测量注意力/认知技能**：FC 的增益经 Σperson 相关结构信息传导，而非 FC 自身认知效度；增益很小（多数条件 PCCR 相对增量 <1%，最大 5.49% 仅在 Q-matrix incomplete + 高相关条件下）；FC 不加载在属性上（假设 8）。
3. **"认知特征"（fluency、reflective–impulsive、focuser–nonfocuser）被测量或诊断**：论文明确仅为 "rough inference"，非 accurate measurement/diagnosis（PDFPAGE 11、32）。
4. **实证 Q-matrix 的内容/专家效度**：未报告构建与验证。
5. **FC 与 RT 的时间动态/策略解释**：只用了每 item 聚合值，无时间位置、动作序列分析。
6. **跨情境泛化**：仅 N=93、10 题的数学小样本。
7. **任何关于 cursor/scroll 等替代数据源有效性的结论**：论文只涉及眼动 FC。
8. **joint 模型的相对优势独立于研究者假设**：模拟中的增益由预设 person 参数相关驱动，属自证性结果；实证无外部标准。

---

## 6. E5 — Incorporating Process Information Into Cognitive Diagnostic Models: A Four-Component Joint Modeling Approach

> **论文定位**：**Response + Response Time + Action Sequence Characteristics → Joint CDM**，E 组非常重要的一篇现代联合建模论文。Rajeb, Ma, He & Shi (2026)，*JEBS* 51(3): 586–624。

### 10.1 Research Question
核心主张："the process data can improve respondents' classification accuracy under varied conditions and support the interpretation of the association between process and response data"（PDFPAGE 1）。背景：虽已有大量研究把 RT 纳入 CDM，但"同时增补多种过程数据类型"的研究稀缺，尤其是把动作序列的相似性与效率放进 CDM 框架内从未有人做过（印刷页 588）。类别归属：process-data modeling（log file 动作序列）+ cognitive diagnosis（CDM/LLM + higher-order structure）+ multimodal / multivariate joint measurement。

### 10.2 Construct
- 通过 CDM 测量 **binary attributes（技能掌握/未掌握）**。实证为 PSTRE（PIAAC 2012）的三个属性：**e-mail use (a1)、web use (a2)、spreadsheet use (a3)**（Q-matrix 见 Table 1，PDFPAGE 11）。
- 同时测量三个过程性个人潜在特质：**speed (τn)、similarity (ζn)、efficiency (ηn)**。相似性 = "个体动作序列与最优参考序列的接近程度"；效率 = "相对最优序列的冗余动作程度"。

### 10.3 Observable Process Data
- **任务/平台**：PIAAC 2012 "problem solving in technology-rich environments (PSTRE)"，Module 2 共 7 题（3 题二分、4 题多分，多分题按正确/错误二分化为 binary；印刷页 596–597）。
- **Raw Observable**：(1) item response Yni（正确/错误）；(2) response time Tni（log file 直接收集）；(3) **action sequence**——"records of all human-computer interactions, such as mouse clicks and keystrokes, during the whole process of an individual solving a digital problem"（印刷页 589）。
- **Derived Process Indicator**：相似性 Sni、效率 Eni——"both similarity and efficiency variables are indirect measures based on test-takers' action sequences"（印刷页 589）。
- 样本：美国样本中完成 Module 2 全部题目的 **935 人**（印刷页 597）。

### 10.4 Process Feature Construction（最重要）
四个 component 与其计算（公式见印刷页 590–592）：
1. **Response Accuracy**：LLM（Maris 1999）：logit P(Yni=1|a*nli) = λ0i + Σ λik a_nlk；λik 约束非负保证单调性（印刷页 590）。
2. **Response Time**：对数正态 RT：log(Tni) = τn − bi(T) + εni，εni ~ N(0, σ²Ti)。
3. **Response Action Similarity**（Eq.3，印刷页 591–592）：**Similarity = Length(LCS) / Length(Reference Sequence)**。
   - **度量**：LCS（最长公共子序列）计算的"个体观测序列与参考序列之间的序列距离"（定义来自 He, Borgonovi & Paccagnella 2019）。
   - **参考序列来源**："optimal action sequence defined by the content experts and item developers"（印刷页 591）。**谁定义：内容专家与题目开发者。**
   - **多参考序列**：对多最优解题目，与每个参考序列算 LCS，取**最长 LCS** 作为"最可能采用的策略"，相似度 = 最长 LCS 长度 / 该对应参考序列长度（印刷页 591–592）。
   - 取值 [0,1]；进入模型：logit(Sni) = ζn − bi(S) + ψni，ζn 为个人相似性参数。
4. **Response Action Efficiency**（Eq.4，印刷页 592）：**Efficiency = Length(LCS) / Length(Observed Sequence)**。
   - 度量：个体 LCS 与**自身观测序列**长度之比，检测"冗余动作"程度。取值 [0,1]，越接近 1 越高效。
   - 进入模型：logit(Eni) = ηn − bi(E) + νni。
- **序列长度与动作类型**：两者都是基于长度的比值；动作"类型"通过 LCS 的字符匹配隐式进入。论文没有单独处理序列长度、动作类型的计数或加权重，也没有给出动作字母表/动作分类法的具体定义（引用 He et al. 2019，本论文中 NOT CLEARLY REPORTED）。

### 10.5 Cognitive Interpretation
- 底层序列度量公式、参考序列概念来自 He, Borgonovi & Paccagnella (2019)（专家定义最优序列 + 统计计算）；其被引用的实质性声明是"can reliably capture and characterize the strategies followed by respondents across a variety of problem-solving assessment items"。
- 本论文自己的解释：(a) similarity = 个体与最优参考序列的接近度；(b) efficiency = 冗余动作程度；(c) **事后解释**：效率参数可提供"how carefully a test-taker is solving each item in a test"的信息（印刷页 604）；相似度低可解读为"deviating from the optimum response sequence, indicating less clarity of the respective test item"（印刷页 618）。
- **关键判断**：效率在模型中**不是被当作一个已确立的认知 construct 来测量**，而是被当作**提高分类精度的辅助/预测性指标（predictive indicator）**，附加以事后、弱实质解释。实证显示能力与效率**负相关**（−0.543），论文原文解释为 "higher ability group 更可能使用更长动作序列，偏离最优序列"（印刷页 601、616）——这是论文的事后解读，与"效率=策略能力"的朴素解读相反。相似性与能力相关系数高达 0.990——**仅凭该相关只能判断两个 latent 参数呈现极强的经验重叠 / near-collinearity；"相似性是能力的近冗余指标 / 在重新测能力"是 CROSS-PAPER / ANALYTICAL INFERENCE，不是论文直接证明的结论。** **两者更多被定位为 predictive indicators 而非独立 construct indicators；论文未做任何 construct validity 论证。**

### 10.6 Mapping
三段链：
- **Observable ↓**：观测 = 正确/错误作答 Yni（以及 log file 中原始动作序列 + 耗时）。由 PIAAC 系统采集，无争议。
- **↓ Process Feature**：对动作序列计算 Sni = |LCS(观测,参考)|/|参考|、Eni = |LCS(观测,参考)|/|观测|，再经 logit 链接进入模型。**依据**：He et al. (2019) 的 LCS 序列挖掘方法；参考序列由内容专家定义。这是"数据压缩 + 专家标准的距离度量"，依据是**外部专家标准**而非认知理论。
- **↓ Cognitive Construct**：S、E 的潜在参数（ζn, ηn）与高阶能力 θn 通过四元正态协方差结构相联，θn 再经高阶模型驱动属性掌握 ank。**依据**：研究者设定的统计结构（层次联合建模，van der Linden 2007），"序列越接近参考 → 能力越高"的因果方向没有被验证，只有相关证据（0.990）。
- 三个箭头中，第一个是直接观测；第二个依据专家标准 + 统计摘要；第三个依据研究者假设的统计关联结构。**"接近最优序列 = 高能力"的实质性断言没有独立证据支持（无 think-aloud、无实验操纵）。**

### 10.7 Who Defines the Mapping?
- 属性与 Q-matrix：PIAAC/OECD PSTRE 框架定义，本论文**直接采用为输入**，未做构建或验证（印刷页 596–597）。
- 参考序列：**内容专家与题目开发者**定义（印刷页 591；多参考序列信息引 He et al. 2021）。本论文没有参与定义；且明确 Module 1 的参考序列未经内容专家验证，故拒用 Module 1 作基准（印刷页 618）。
- 统计层面的 mapping（S、E 的 logit 测量模型 + 四元正态结构）：由**研究者**（本文作者）设定。
- 序列特征汇总为 S/E 的算法：来自 He et al. (2019)（外部研究者）。

### 10.8 Q-Matrix / Attribute Structure
K=3 binary attributes（e-mail a1、web a2、spreadsheet a3），来自 PSTRE 框架（OECD 2016）。Table 1 给出 7 题 × 3 属性的 Q-matrix：Unit 19a=(1,0,1)、Unit 19b=(1,0,1)、Unit 07=(0,1,0)、Unit 02=(1,1,0)、Unit 16=(1,0,0)、Unit 11b=(1,0,0)、Unit 23=(1,1,0)。**Q-matrix 是 input 而非自动发现**：论文未做 Q-matrix 验证/估计。模拟研究 2 用了 de la Torre & Chiu (2016) 的 5 属性 Q-matrix。属性相关通过 higher-order 结构处理："all attributes are assumed to be independent given θ"（印刷页 593）。

### 10.9 Key Action
**不使用 key action 概念**。明确采用 sequence-level 的 LCS 摘要量（similarity、efficiency），而非"关键动作"指标。讨论中与 Liang et al. (2023, 动作计数)、Qiao et al. (2023, Conway-Maxwell-Poisson) 对比时强调本文优势在于"使用动作**序列**信息而非仅仅动作计数"（印刷页 617）。

### 10.10 Phantom Item / Item Expansion
**本论文不涉及**。四个分量是同一批真实题目的四个观测通道，不是扩题。

### 10.11 Misconception Diagnosis
**不涉及**。属标准 binary-attribute CDM。

### 10.12 Multimodal Joint Modeling（最重要）
模型结构是**层次联合建模框架（hierarchical joint modeling, van der Linden 2007）**——四个独立测量模型 + 一个人参数层面的协方差结构模型（印刷页 589）。
- Response accuracy 有自己的一套 K 个 binary 属性 ank，由高阶能力 θn 驱动（higher-order structure, Eq.5）：P(ank=1|θn) = e^(θn−gk)/(1+e^(θn−gk))。
- RT、similarity、efficiency 各有一个**个人层面潜在参数**（τn, ζn, ηn），**没有属性向量**；它们通过人参数的四元正态分布与 θn 相关（Eq.6）：Ln = (θn, τn, ζn, ηn)' ~ N(μ, Σperson)，Σperson 含方差与相关 ρuτ, ρuζ, ρuη, ρτζ, ρτη, ρζη。
- **链接函数**：响应 = logit（LLM）；RT = log-normal；similarity 与 efficiency = logit 链接（处理 [0,1] 有界量）。
- 联合似然（Eq.7）：L(Y, logT, logitS, logitE | Θ) = ∏∏ P(Yni|an,Lk)·f(logTni|bi(T),τn,σ²Ti)·f(logitSni|bi(S),ζn,σ²Si)·f(logitEni|bi(E),ηn,σ²Ei)。
- **依赖结构**：是"common-person latent variable + correlation structure"型——不是共同属性因子、不是分层因果模型。分量间依赖**只通过人参数相关矩阵捕捉**；给定人参数后各分量条件独立。论文承认此假设可能过强（引 van der Linden 2007 认为响应与 RT 条件独立 "counterintuitive"），把 RT/similarity/efficiency 间的条件依赖列为未来研究（印刷页 617）。
- 识别约束：μθ=0、σθ=1；μτ=μζ=μη=0。Σperson 用 ΔΩΔ 分解，Ω 的 Cholesky 因子用 LKJ 先验 dlkj_corr_cholesky(1.3)。估计用 NIMBLE（MCMC）。

### 10.13 Added Value of Process Data
**经验数据（DIC, 印刷页 598–599）**：
- 四分量 DIC=6,574.08；三分量含相似性=6,571.47；**三分量含效率=8,886.51**；二分量=8,559.29；HO-LLM=8,695.12。四分量与"三分量含相似性"几乎相同，且明显低于其它模型。**三分量含效率的 DIC 甚至高于二分量，提示单独加效率并不改善拟合。**
- 四分量 PPP：响应 0.662、RT 0.516、相似性 0.515、效率 0.514（印刷页 598）。
- Figure 2 显示四分量 PSD（后验标准差）最低，其次"三分量含相似性"；**similarity 比 efficiency 贡献了更多信息**（印刷页 600）。

**Simulation Study 1（基于实证参数，30 次重复，N=1,000；Table 8，印刷页 611）**：

| 模型 | 加入的组件 | ACA | PCA |
|---|---|---|---|
| HO-LLM（基线, response only） | — | 0.84 | 0.598 |
| 二分量 | +RT | 0.845 | 0.609 |
| 三分量含效率 | +RT+Efficiency | 0.846 | 0.611 |
| 三分量含相似性 | +RT+Similarity | 0.862 | 0.649 |
| **四分量** | **+RT+Similarity+Efficiency** | **0.863** | **0.650** |

（ACA 分属性：四分量 a1=0.894、a2=0.866、a3=0.828，印刷页 611。）人参数 RMSE（Table 4）：四分量 θ=0.451、τ=0.155、ζ=0.386、η=0.166；**例外：四分量 θ 的 RMSE（0.451）略高于"三分量含相似性"（0.447）**（印刷页 607）。

**Simulation Study 2（变化条件；印刷页 610–615）**：I=15/30；N=500/1,000；人参数相关高（r=0.7 或 −0.7）vs 低（r=0.3 或 −0.3）；5 属性；每条件 30 次重复。结果（Table 11）：I=30 时所有模型 ACA>0.90；I=15 时 ACA>0.84。**四分量在高相关条件下 PCA 一致略高（如 High/1,000/30：四分量 0.912/0.647 vs 二分量 0.912/0.646 vs HO-LLM 0.910/0.641）；低相关条件下四分量无优势，甚至略低于 HO-LLM（如 Low/500/30：HO-LLM 0.930/0.711 vs 四分量 0.929/0.710）**。人参数 RMSE（Table 10）四分量一致最低（如 High/15/500：θ 0.580 vs 二分量 0.639 vs HO-LLM 0.781）。论文结论：过程数据贡献随**人参数相关性**增强而增大；相关低时"使用四分量可能不方便"（印刷页 613、616）。
> **Improved diagnostic performance does not by itself establish construct validity**——相似性/效率的分类增益是"加入额外预测指标"的统计收益，不验证这些指标测量了特定认知构念（实证甚至显示效率与能力负相关）。

### 10.14 Validation Evidence
- Content evidence：属性与 Q-matrix 来自 OECD/PSTRE 框架，参考序列由内容专家定义——间接内容证据，但本论文**未**自行做内容效度研究。Module 1 参考序列未经专家验证即被弃用（印刷页 618），侧面说明专家验证被当作前提。
- Response-process evidence：**NOT PROVIDED**（无 think-aloud、无眼动、无回溯报告）。
- Internal structure：**有**——模型拟合（PPP、DIC、R̂<1.05）、人参数相关结构、item-wise PPP（响应模型 [0.242, 0.436]，RT/相似性/效率接近 0.5，可接受区间 [0.05, 0.95]，印刷页 599）。
- Relations to other variables：**有**——能力与各过程参数的相关（Table 2）、跨模型分类一致性、与 He et al. (2021) 结论对照。
- Consequences：**NOT PROVIDED**。
- Convergent evidence：部分——能力−相似性相关 0.990 与 He et al. (2021) 一致；能力−RT 0.411 与前人一致（印刷页 601）。但这不是标准多方法收敛效度检验。
- Discriminant evidence：**NOT PROVIDED**（0.990 的相关反而提示相似性与能力几乎不可区分）。
- Expert evidence：有（参考序列、Q-matrix 的专家来源），但论文自身没有报告专家评审/专家打分程序细节。
- Think-aloud / Retrospective / Eye tracking / External criterion：全部 **NOT PROVIDED**。Module 1 能力作为外部基准被讨论但**未执行**（印刷页 618）。

### 10.15 Ground Truth
- **Simulation**：两种模拟的真值都是**模型自生成**的。Simulation 1 把实证四分量模型的估计参数当作真值生成 30 组 × 1,000 人数据（印刷页 605）。Simulation 2 用指定分布与 de la Torre & Chiu Q-matrix 生成真值（印刷页 612）。
- **实证**：没有外部 cognition label；掌握状态是模型估计输出。
- **Reference sequence 是否算 ground truth**：参考序列是**专家定义的"最优动作序列"**，作为计算 S/E 的基准，但**不是认知真值**，也没有被独立验证为唯一最优（论文承认存在 2–18 个参考序列/题，印刷页 597）。
- **"model output = ground truth" 循环**：在模拟中**存在**（同一模型结构同时生成并拟合数据）；在实证中，能力−相似性 0.990 的高相关提示相似性可能与能力高度重叠（CROSS-PAPER / ANALYTICAL INFERENCE），而非独立证据。

### 10.16 Circularity Risk
**存在实质循环风险，论文未讨论。** 逻辑链：
1. 参考序列由内容专家预设为"最优/专家序列"（印刷页 591）；
2. similarity 定义为"个体序列与参考序列的 LCS 长度比"，即**奖励按专家最优路径行事的人**；
3. 作答正确与否大概率与是否按最优路径操作相关；
4. 于是模型发现"能力与相似性相关 0.990"——**这个近乎完美的高相关很可能是构造出来的（definitional alignment），而非独立因果证据**。
此外，效率的构造（分母 = 观测序列长度）意味着**多走动作就扣效率**，而实证却发现高能力者**效率更低**（−0.543，印刷页 601）——说明"专家最优序列"并不等于"最高效序列"，两者方向相反，进一步表明 S/E 的实质解读不可靠。论文既没有检验"按参考序列行动是否确实提高正确率"，也没有讨论"专家序列未必穷尽所有有效策略"。

### 10.17 Alternative Explanations
效率低/相似度低在 PSTRE 语境下可能由多种原因造成，论文**未系统排除**：题目难度（印刷页 601 提到 U02 最难、作答时间最长）；界面复杂度/技术环境交互负担；合法但不同的解题策略（每题 2–18 个参考序列，印刷页 597，说明存在多种有效策略，但参考集未必穷尽）；深思熟虑 vs 盲目试错（论文对高能力者低效率的解释是"PSTRE 决策过程性质"，印刷页 616，属事后解释）；猜测、错误点击等噪声动作。论文观察到的负相关证据（RT−效率 −0.940、"更长耗时更可能伴随低效率"，印刷页 599）被当作描述性事实，未用于排除替代解释。

### 10.18 Temporal Alignment
**NOT REPORTED（基本不涉及）**。LCS 本身保持动作的**相对顺序**（子序列的定义性质），但论文没有区分"序列前段 vs 后段动作意义不同"，没有时间加权、没有动作位置建模。时序信息仅以整体 RT 粗糙地进入模型。

### 10.19 Person / Item / Context Dependency
论文承认并建模了 **item 层面依赖**：每题有独立的 bi(T)、bi(S)、bi(E)、σ² 参数；item-wise 相关显示 U02、U16 上相似性−效率相关绝对值特别高，U11b 上相似性−效率相关为正 0.224，其余均为负（印刷页 599）。**能力水平依赖**：能力−效率负相关意味着效率的"好/坏"含义随能力而异——高能力者"不高效"反而是策略性的。**Context/先验知识**：没有建模。**结论：efficiency/similarity 的意义明确依赖题目与能力水平，但论文没有把这种依赖做成可解释的调节机制。**

### 10.20 Generalization
**未做跨新学生/新题/新任务/新领域的泛化验证**。实证仅 PIAAC 2012 PSTRE Module 2（7 题、3 属性、935 名美国成人、单一领域）。Simulation 2 变化了 I、N、相关条件与属性数（5 属性），但仍是同一类生成模型。跨样本基准验证（Module 1 能力）被**提及为未来工作但未执行**，原因明确：Module 1 参考序列未经内容专家验证（印刷页 618）。全部结果属 **within-sample**。

### 10.21 Evaluation
- **经验（印刷页 598–601）**：PPP（四分量：响应 0.662、RT 0.516、相似性 0.515、效率 0.514；响应 item-wise [0.242, 0.436]）；DIC（6,574.08 / 6,571.47 / 8,886.51 / 8,559.29 / 8,695.12）；R̂<1.05；人参数相关（Table 2，印刷页 602）：能力−RT 0.411 [0.356, 0.462]、能力−相似性 0.990 [0.987, 0.992]、能力−效率 −0.543 [−0.586, −0.498]、RT−相似性 0.342 [0.284, 0.397]、RT−效率 −0.940 [−0.950, −0.927]、相似性−效率 −0.489 [−0.536, −0.438]；方差 s²τ=0.119、s²ζ=0.759、s²η=0.117。Item 参数（Table 3）：如 b(T)U02=1.26 → 中位作答时间 e^1.26≈3.53 分钟。
- **Simulation 1（印刷页 605–611）**：30 重复 × 1,000 人；bias 近 0；人参数 RMSE（Table 4）：四分量 θ 0.451/τ 0.155/ζ 0.386/η 0.166；item 参数 bias/RMSE 范围 [−0.02, 0.03] 与 [0.02, 0.09]；高阶 g 的 RMSE 四分量最低（Table 7）；ACA/PCA 见表 8（见 §13）。
- **Simulation 2（印刷页 610–615）**：条件 2×2×2（I=15/30, N=500/1,000, 高/低相关）×30 重复；人参数 bias 近 0（Table 9）；RMSE 见表 10；ACA/PCA 见表 11（见 §13）。
- **未报告**：标准意义的模型 reliability（论文承认 "further evaluation of the estimation reliability...would be valuable"，印刷页 617）、无 AIC/BIC。

### 10.22 Transfer to Our English Reading System
- **Directly Transferable**：(1) 四分量层次联合建模架构（响应 + RT + 序列摘要指标分别建模，通过人参数协方差结构关联）；(2) 有界 [0,1] 指标的 logit 链接测量模型与 LKJ 先验/Cholesky 分解的 Σperson 处理；(3) **LCS 算法本身 technically transferable**（反馈修正：算法可直接算，但 LCS → similarity/efficiency → cognition 不能直接迁移，见下）；(4) 经验上"过程数据降低能力估计 PSD"的机制性结论。
- **Transfer With Modification / PROJECT HYPOTHESIS**（反馈修正）：**expert-reference similarity 作为认知指标 → NOT VALIDATED / PROJECT HYPOTHESIS**——LCS 算法可算，但"与专家参考序列的相似度"当作阅读认知指标未经验证。具体：(1) **Similarity 需要专家预定义参考/最优序列**。阅读理解**没有天然唯一的"最优阅读序列"**——学生可以任意顺序阅读、回看、划线。需改为：由教研专家定义"参考阅读轨迹"，或用数据驱动（如高分组典型序列）作参考；且论文显示每题需要 2–18 条参考序列，成本高。(2) **Efficiency（=LCS/观测长度）度量"冗余动作"在阅读中语义不稳**：回看、划线、选中文本是正常理解策略而非冗余；且本文实证发现高能力者效率更低（−0.543，限该 PSTRE 数据与该效率定义），指标方向在阅读领域未必可迁移。(3) 二分响应/二分属性假设需调整。(4) 条件独立假设在阅读中更易被违反（阅读行为强受 passage 内容驱动）。
- **Not Transferable**：(1) PSTRE 的三个属性与对应 Q-matrix；(2) PSTRE 各题的参考序列及其"专家最优路径"定义；(3) 实证结论"能力与相似性 0.990、能力与效率 −0.543"是 PSTRE 任务特性，不构成通用规律；(4) 模拟生成模型假设（四分量结构为真）不适用于阅读数据规模与真实误差结构。

### 10.23 What This Paper Does NOT Establish
- **未建立** "efficiency = 策略能力/战略胜任力" 的 construct validity。实证中效率与能力负相关，方向与朴素解读相反；论文把效率定位为辅助指标并做事后解释，没有验证。
- **未建立** "sequence similarity 反映真实认知过程"。无 think-aloud、无眼动、无回溯报告；相似性只是对专家参考序列的距离度量。
- **未建立** 参考序列是"唯一最优"或"穷尽有效策略"。每题存在 2–18 条参考序列，专家定义的完备性未检验。
- **未处理/未承认** 参考序列→相似性→能力之间的**构造性循环**（§16），尤其 0.990 高相关未被批判性检验。
- **未验证** Q-matrix（直接当作 input）。
- **未建立** 泛化性：无新题、新任务、新领域、新人群验证；Module 1 外部基准被放弃。
- **未建立** 分量间的条件依赖/因果关系：仅在条件独立假设下建模人参数相关。
- **未提供** 模型可靠性（reliability）估计（论文自认未来工作）。
- **未提供** 多方法收敛/区分效度证据，或任何后果性效度（consequences）证据。
- **未比较** 更优的 response-only 替代（如更丰富的 CDM 响应模型），无法证明"过程数据收益不能被更好的响应模型复制"。
- **未处理** 多分属性/多分响应、缺失机制、动作字母表/序列粒度对结果的敏感性。

## 7. E6 — Process Data in Computer-Based Assessment: Challenges and Opportunities in Opening the Black Box

> **论文定位**：**Process Data Validity / Theoretical Grounding Framework**。Lindner & Greiff (2023)，*European Journal of Psychological Assessment* 39(4): 241–251（Editorial / special issue）。E6 不提供最强算法，它的主要价值是回答：**"Process-data indicator 要被解释成 psychological / cognitive construct，需要什么证据？"**

### 10.1 Research Question
社论目标不是提出单一经验问题，而是为"计算机化测评中的过程数据"提供**综合框架与路线图**：回顾过程数据在测评中的演变，讨论三大挑战：(1) **过程数据指标的理论基础与验证**（theoretical grounding and validation of process indicators）；(2) **过程数据的测评设计**（assessment design for process data）；(3) **伦理标准**。结论提出三个未来重点：强而整体的过程数据验证理论框架、可靠的标准化数据采集（最好自上而下设计题项 + 预注册假设）、以及负责任推断的伦理规范（PDFPAGE 1）。类别归属：process-data modeling 的理论框架 / process indicator 的构念效度论证 / validation framework 综述类。

### 10.2 Construct
用论文自身术语：过程数据可以指向的 construct 包括 **cognitive, metacognitive, and affective-motivational processes**（PDFPAGE 1）；cognitive and metacognitive processes、self-regulatory processes、careless response behavior、response tendencies to positively/negatively worded items、self-control、test-taker disengagement / rapid-guessing（PDFPAGE 1–3）。**关键区分（借 Zumbo et al. 2023）**：process data = 显性采集的行为数据（process 的痕迹，manifest traces）；response processes = 我们想推断的潜在构念与底层过程（latent）。**二者不可混淆（PDFPAGE 2）。**

### 10.3 Observable Process Data
- **官方定义**：process data = "any behavioral measure that can be repeatedly and automatically logged during a test using technological devices, such as system events and test-taker actions together with their time stamps, eye movements, heart rates, or facial expressions"（引 Lindner & Greiff 2021，PDFPAGE 1）。更广义还包括 verbal protocols、重复调查题、观测数据、生理测量（PDFPAGE 2）。
- 本期收录的**原始可观测数据**：action sequences 与 pauses（Arslan et al. 2023）；带时间戳的鼠标点击、触屏输入、击键（Drake; Hahnel; Veerbeek & Vogelaar 2023）；鼠标光标移动（Pokropek et al. 2023）；眼动记录（Koutsogiorgi & Michaelides 2023）（PDFPAGE 1）。
- **Derived process indicators 示例**：rapid-guessing（超低作答时间）与 response time effort / RTE（Wise & Kong 2005）；pauses = "两个相邻事件之间的时间间隔"；光标距离、平均速度、方向改变；在无关货架/产品上停留时间与访问频率（PDFPAGE 3、5）。

### 10.4 Process Feature Construction
社论本身无数据，转述了本期论文的构造方式：
- **Hahnel et al. (2023)**（网页搜索任务）：研究者**先定义 4 个基于日志的指标**，假定反映特定的 search 与 stopping rules；据此把学生分成 **4 个互斥的假设性搜索策略组**（"学生应该如何表现的理想行为"）；再用**多重聚类分析**在大数据库上经验验证预测，结果**只复现了 4 个预测簇中的 2 个**（PDFPAGE 5）。这是"理论先验定义指标 → 统计验证"的范式。
- **Arslan et al. (2023)**（pauses）：提出基于认知的理论化方法解释停顿，并主张**不同类别的停顿需按具体题项分别建模**（PDFPAGE 5）。
- **Veerbeek & Vogelaar (2023)**：用**分段时间区间**推断类比推理动态测验中的学习进步（PDFPAGE 3）。
- **Drake et al. (2023)**：从日志提取 **4 个行为指标**（在无关货架/产品的停留时间、访问频率）测自我控制（PDFPAGE 5）。
- **Pokropek et al. (2023)**：基于光标移动构建 **4 组指标**（距离、平均速度、方向改变等）（PDFPAGE 3）。
- 社论主张：为克服自下而上（bottom-up，利用既有副产品数据）的局限，应转向**自上而下（top-down）**的 "by-design" 设计，即在数据采集前预定分析与假设、预注册、并基于理论对行为做有信息量的分段（引 Keehner et al. 2022）（PDFPAGE 5）。

### 10.5 Cognitive Interpretation
- (a) 理论显式定义：Hahnel（基于搜索/停止规则的理论假设）、Arslan（认知中心化解释停顿）、Drake（自我控制）都属"理论驱动定义指标"。
- (c) 统计导出：Hahnel 用聚类分析验证（只 2/4 簇可复现）。
- (b) 专家/Q-matrix：本期未涉及。
社论明确要求：指标的解释必须"建立在理论之上 **并** 像产品数据一样经过验证"，理论是必要条件但**不充分**（PDFPAGE 4）。

### 10.6 Mapping
**Observable**（日志动作序列、停顿、光标轨迹、眼动）→ **Process Feature**（分段时间、停顿时长、搜索/停止规则指标、无关货架停留时间）→ **Cognitive Construct**（认知/元认知过程、搜索策略、自我控制、努力程度）。
箭头依据审查：社论指出"可观测行为如何能指示与构念相关的心理过程往往是不清楚的"（PDFPAGE 4）；强理论框架应"识别相关过程与指示性参数，并提供如何采集与分析数据以检验构念相关过程的假设"（PDFPAGE 4）。**每个箭头的证据都必须由"理论 + 经验/实验验证"共同支撑，不能默认成立。**

### 10.7 Who Defines the Mapping?
**研究者基于理论预先定义**（Hahnel 定义搜索/停止规则指标；Drake 定义自我控制指标；Arslan 定义停顿解释），随后用统计（聚类）验证。社论层面：要求研究者在数据采集**之前**完成设计、预注册假设（PDFPAGE 5）。未涉及学生自报、think-aloud 编码等来源。

### 10.8 Q-Matrix / Attribute Structure
**NOT APPLICABLE**（无属性/认知诊断矩阵）。相关论述：测评设计需"为过程数据设计任务与题项特征"，引 evidence-centered design 扩展版（Goldhammer et al. 2021）与 Keehner et al. (2022) 的分步流程（PDFPAGE 4–5）。

### 10.9–10.11 Key Action / Phantom Item / Misconception
全部 **NOT APPLICABLE**。

### 10.12 Multimodal Joint Modeling
社论未提出形式化联合模型。论述的是**多源互补**：过程数据与产品分数（product scores）联合以作整体构念推断（PDFPAGE 2）；多种过程指标的组合（PDFPAGE 4）。**形式化 joint modeling：NOT REPORTED**；是一种概念性的"多来源 triangulation/互补"论证。

### 10.13 Added Value of Process Data
- 支持**效度论证、改进产品分数的解释**；以及**评估超出原测验诊断目的的额外心理构念**（PDFPAGE 1）。
- Drake et al.：过程取向"成功地为解释**增加了超越表现（performance）的另一个维度**"（PDFPAGE 5）。
- 快速猜测检测用于**动机过滤**或统计补偿脱离投入的作答（PDFPAGE 3）。
- 光标指标：Pokropek 发现**仅 2 个**过程指标对动机相关的实验操纵"有一定敏感性"，但与其他脱离投入测量呈**中等相关**——"tentative evidence"（PDFPAGE 3）。
- **没有数字化的增量增益声明**；价值论证是概念性的。**反面教训**：Veerbeek & Vogelaar 在训练后产品分数上升、但基于时间的指标**大多数无实质变化**，证明"有理论基础的指标也可能检测不到决定成功的复杂心理过程"（PDFPAGE 5）。

### 10.14 Validation Evidence（重点）
社论性质，以下多为框架性/转述性：
- Content evidence：**NOT PROVIDED**。
- Response-process evidence：历史回顾指出 think-aloud 协议与认知访谈曾用于为具体题项/任务/构念建立效度论证（PDFPAGE 2）；反复强调验证过程数据指标的必要性（PDFPAGE 4）。
- Internal structure：**NOT PROVIDED**。
- Relations to other variables：Pokropek 光标指标与其他脱离投入测量中等相关（PDFPAGE 3）；Drake 过程维度超越表现维度（PDFPAGE 5）。
- Consequences：重点讨论 **consequential validity**——基于过程数据做决策须极度谨慎（PDFPAGE 4）；伦理簇（知情同意、隐私、透明度；责任、效度、最小化不良影响、干预）（PDFPAGE 6–7）。
- Convergent evidence：Pokropek 的中等相关（仅试探性）；其他 **NOT PROVIDED**。
- Discriminant evidence：**NOT PROVIDED**。
- Expert evidence：**NOT PROVIDED**。
- Think-aloud：作为早期效度实践被回顾（PDFPAGE 2）；并展望 AI 自动评分 think-aloud 协议以补充可解释性与验证策略（PDFPAGE 7）。
- Retrospective report：**NOT REPORTED**。
- Eye tracking：作为过程数据类型出现，并讨论其局限——校准失败、设备昂贵、难在大样本使用（PDFPAGE 6）。
- External criterion：**NOT PROVIDED**。
- **关键论点：过程数据指标必须像产品数据一样被验证（引 Goldhammer et al. 2021; Zumbo et al. 2023）（PDFPAGE 4）。**

### 10.15 Ground Truth
E6 明确**不把"过程→认知"标签当 ground truth**：process data（显性痕迹）≠ response processes（潜在构念）（PDFPAGE 2）。"过程追踪必然提供有用信息"的朴素观点被明确否定（PDFPAGE 2）。标签来源需"理论 + 经验/实验验证"共同建立（PDFPAGE 4）。

### 10.16 Circularity Risk
社论直接处理了该风险：即使有理论基础的指标，其与决定解题成功的认知过程的关系**仍可能未知**（Veerbeek & Vogelaar 的负结果，PDFPAGE 5）；"naïve view that tracking a process will inevitably provide useful information...does not necessarily apply"（PDFPAGE 2）。社论要求的预注册、by-design、统计/实验验证正是为防"研究者预设的解释被循环确认"。

### 10.17 Alternative Explanations
- 过程数据易受**构念无关方差**污染：测试情境干扰与情境因素（噪音、房间意外事件）、题项特征（内容、措辞、显示设计、多媒体元素）、学生特征（神经多样性谱系差异）（PDFPAGE 6）。
- **Arslan et al. (2020)**：保持题面内容不变、仅改表面设计，过程数据指标即显著变化（PDFPAGE 6）。
- **Koutsogiorgi & Michaelides**：正/负向措辞改变不同受访者的加工方式（眼动模式可见）（PDFPAGE 6）。
- 传感器数据（眼动、心率）易出现严重且不可预测的数据丢失或偏差（传感器失真）（PDFPAGE 6）。
- 神经多样性/残障以不可预见方式改变过程数据（如 time on task），对偏离常模个体产生无效推断（Zumbo et al. 2023，PDFPAGE 7）。

### 10.18 Temporal Alignment
过程数据本质基于时间：pauses = 两事件间隔（PDFPAGE 3）；**分段（segmentation）是构造指标的前提**，而分段方式取决于题项显示与作答动作（Veerbeek & Vogelaar，PDFPAGE 3）；Arslan 主张**停顿的类型必须结合具体题项建模，不能跨题直接推广**（PDFPAGE 5）。

### 10.19 Person / Item / Context Dependency
**高度依赖**：题项特征（内容、措辞、显示、多媒体）、学生特征（神经多样性）、情境（噪音、意外事件）都改变过程数据（PDFPAGE 6）；停顿推断不能跨题推广（PDFPAGE 5）；即便对"平均应试者"有效的指标，也不保证在个体层面、对偏常群体同样有效（Zumbo et al. 2023，PDFPAGE 7）；引入 **differential response time（DIR）** 分析概念（对应产品数据的 DIF；Ercikan et al. 2020）（PDFPAGE 7）。

### 10.20 Generalization
暂停/动作序列的解释**不能跨题泛化**（需知任务细节）（PDFPAGE 5）；大尺度测验中题项保密不放行为过程数据加剧此问题（PDFPAGE 5）。眼动等传感器手段**目前限于小样本/实验室研究**（成本、校准）（PDFPAGE 6）。**个体层面推断的可行性与公平性未解决**（PDFPAGE 7）。AI/ML 有望自动化复杂过程分析（AI 可扩展）（PDFPAGE 6–7）。

### 10.21 Evaluation
无自身实证数据；评价其**论证框架**：
1. 过程数据的三类挑战（理论验证、数据采集与分析、伦理）——Figure 1 以"要点图"总结关键挑战与最佳实践（PDFPAGE 4）。
2. 三个未来方向：强理论框架、可靠标准化采集（top-down + 预注册）、伦理规范与克制推断（PDFPAGE 1、7）。
3. 用 7 篇专辑论文作为正反例（尤其 Veerbeek 的负结果与 Hahnel 的 2/4 簇复现）。

### 10.22 Transfer to Our English Reading System
- **Directly Transferable**："process data ≠ response processes"的区分——我们应把滚动/回看/划线当作**行为痕迹**，而不是直接等同"理解了"；给每个指标配"理论 + 统计验证"论证链；三大挑战清单（尤其**构念无关方差**：题项措辞、显示设计、学生差异会污染滚动/时间指标）可直接作为指标开发检查清单；自上而下 by-design + 预注册假设的工作方式；指标需"像分数一样验证"；神经多样性/个体层面推断谨慎、伦理。
- **Transfer With Modification**：具体指标构造范式（先理论定义互斥行为模式，再用聚类验证，如 Hahnel 的 4 簇→复现 2 簇）——可迁移为"回看模式/划掉选项序列/改答案序列"的行为分型，但需为阅读理解重新定义（无现成理论链）；停顿分段思想可迁移为"阅读区 vs 答题区停留"的分段，但"不能跨题推广"的告诫意味着需按 passage/题项分别建模；"过程指标能增加超越产品分数的维度"（Drake）支持把行为指标作为答题正确率之外的增量信息。
- **Not Transferable**：眼动/心率/面部表情等**传感器生理指标**（我们 UI 无此设备）；网页搜索/虚拟超市任务的特定指标（领域绑定）。

### 10.23 What This Paper Does NOT Establish
- **没有**提供任何经验证据证明某个具体过程指标对应某个具体构念。
- **没有**建立"过程数据一定能改进效度"——恰恰通过 Veerbeek 负结果否定了这种必然性。
- **没有**给出个体层面基于过程数据做决策可行/公平的证明（明确列为未解决问题）。
- **没有**形成最终伦理规范（仅概述，引 GDPR 等）。
- **没有**处理具体统计模型（IRT/序列挖掘的联合建模细节不在本文）。

---

## 8. E7 — Towards a Fuller Picture: Triangulation and Integration of the Measurement of Self-Regulated Learning Based on Trace and Think Aloud Data

> **论文定位**：**Trace Data ↔ Think-Aloud Triangulation**，整个 E 组 validity 侧最重要的论文之一。Fan et al. (2023)，*Journal of Computer Assisted Learning* 39(4): 1303–1324。

### 10.1 Research Question
核心问题：think-aloud 与 trace 两路数据能否、如何在**同一时间轴、同一理论框架**下对齐、三角验证与整合，以获得比单一数据通道更完整的 SRL 测量（PDFPAGE 3）。两个正式 RQ：
- **RQ1**：think aloud 与 trace 数据在测量 SRL 过程时可整合到什么程度？两路数据可互换（interchangeable）或互补（complement）到什么程度？
- **RQ2**：基于整合数据测得的 SRL 过程，与基于各自单独数据通道测得的 SRL 过程，其**时间与序列关联**有何差异？
类别归属：process-data modeling / response-process evidence / triangulation / construct validity 论证 + process mining（FOMM）。关键定义（PDFPAGE 5）：**interchangeable** = 两路数据在同一时间段揭示同一 SRL 过程；**complement** = SRL 过程只能被其中一路数据通道揭示。

### 10.2 Construct
声称测量的 construct 是 **Self-Regulated Learning（SRL）的认知与元认知子过程**，采用 **Bannert (2007) 理论框架**（Table 1）。编码类别：Metacognition（MC.O 定向、MC.P 计划、MC.M 监控、MC.E 评价）；Cognition（LC.F 首读、LC.R 重读、HC.E/O 精细加工/组织）；Motivational and Procedural（Other）；No_process（不可编码）。

### 10.3 Observable Process Data
- **Trace 侧**：44 名学生在技术增强学习环境（TEL）中学习，采集导航日志、键盘敲击、鼠标轨迹（移动/点击/滚动）、眼动数据（Tobii TX300，300 Hz），经本地 PHP 服务器存储（PDFPAGE 6）。TEL 界面：左侧目录+导航、中部阅读/写作、右侧工具（标注、计划器、搜索）+ 计时器、评分量规。
- **Think-aloud 侧**：网络摄像头和麦克风录音；实验开始时提供 15–20 分钟出声思维训练；长时间沉默会被提醒继续说话（PDFPAGE 6）。任务为 45 分钟，读三个主题材料（AI 约 11 页/2300 词、课堂分化 9 页/1400 词、scaffolding 11 页/1900 词）+ 多源写作任务（写 300–400 词"2035 年学校学习"愿景短文）（PDFPAGE 5）。
- **Derived Process Indicator**：trace 侧：action library（18 个动作标签）→ process library（31 个动作序列 → SRL 过程）；think-aloud 侧：自动切分的"有声片段"经 3 名编码者编码为 SRL 过程。两路数据**在同一时间轴上同步**（PDFPAGE 6）。

### 10.4 Process Feature Construction
**Trace 侧（自动规则）**：
- 在既有文献基础上构建 **trace parser**，含 action library 与 process library。
- **Action library（Table 2）**：18 个动作标签（GENERAL_INSTRUCTION、RUBRIC、RELEVANT_READING、RELEVANT_RE-READING、IRRELEVANT_READING、NAVIGATION、WRITE_ESSAY、COPY_PASTE、NOTE_EDITING、NOTE_READING、HIGHLIGHT_EDITING、HIGHLIGHT_READING、HIGHLIGHT_LABELLING、TIMER、SEARCH_CONTENT、SEARCH_HIGHLIGHT_NOTE、PLANNER 等）。用多通道数据（眼动+鼠标+键盘）交叉验证动作标注。
- **Process library（Table 3）**：3 主类、7 子类、31 个动作序列，每序列映射一个 SRL 过程。"->"表动作转移，"<->"表双向，"()"表可选，"*"表连续重复。例：GENERAL_INSTRUCTION <-> NOTE_EDITING → Orientation。
- **No_Process 处理**：trace 中无法映射到任何序列的动作标为 No_Process，不进入后续分析。

**Think-aloud 侧（人工编码）**：
- Audacity 插件（自动声音检测）把音频切成"有声片段"：音频低于 **26 dB** 视为沉默；**0.30 秒**及以上沉默则分段；编码者存疑时可讨论并修改（PDFPAGE 7）。
- **3 名编码者**用基于 **Bannert (2007) 与 Molenaar et al. (2011)** 的 coding scheme 编码 utterance 为 SRL 过程；用 **ELAN** 处理编码时间。
- **Inter-rater reliability：κ = .53–.65，kmax = .81–.82**（PDFPAGE 7）。
- 切分单元是**基于声音的片段**（非按句/按行为）。

### 10.5 Cognitive Interpretation
两路数据的 SRL 过程解释均**以 Bannert (2007) 理论框架为主导**。解释类型：(a) 理论明确界定（过程类别来自 Bannert 框架）；(b) 部分由研究者依据既有 trace-SRL 文献设定研究者定义规则（trace 侧映射）；(d) post hoc 解释——如对"不匹配共现"（S5）给出"学习者同时进行多个 SRL 过程"的解读（PDFPAGE 18，**这是论文给出的解释之一，非唯一解释——E7 同时承认细粒度先后发生、理论框架缺失、measurement/coding error 等可能，§10.17**）。论文明确讨论两路方法各自的局限：think-aloud 的反应性（reactivity）、沉默片段难分析、编码者偏差（PDFPAGE 2–3）；trace 的"动作→过程"映射涉及研究者多重推断，可能误判（PDFPAGE 4）。

### 10.6 Mapping
**Trace 侧**：Observable（导航/键盘/鼠标/眼动）↓ action library（18 动作标签）↓ process library（31 序列 → SRL 过程段，有起止时间戳）↓ Bannert 框架类别（MC.O/MC.P/MC.M/MC.E/LC.F/LC.R/HC.E/O）。箭头依据：基于既有 trace-SRL 文献与 Bannert 框架，由研究者以自动化规则定义（PDFPAGE 6–7）；文献承认此映射含"多重推断"，易出错（PDFPAGE 4）。
**Think-aloud 侧**：Observable（语音 utterance）↓ Audacity 自动切分 + 3 编码者编码（κ=.53–.65）↓ 同一 Bannert 框架 + Other + No_process。箭头依据：人类编码者依据 Bannert (2007) 与 Molenaar et al. (2011) 编码方案。

### 10.7 Who Defines the Mapping?
- trace event → SRL 过程：**研究者定义**——研究者依据既有文献与 Bannert 框架手工构造 action/process library，再以**自动化 parser（规则）**应用于日志数据。
- think-aloud 编码：3 名人类编码者，依据基于 Bannert (2007)、Molenaar et al. (2011) 的编码方案。
- **两路映射的类别定义同源（同为 Bannert 框架）。**

### 10.8 Q-Matrix / Attribute Structure
不涉及 CDM 的 Q-matrix。SRL 编码类别结构即 Table 1 的层级：3 主类 → 7 子类 + Other + No_process。trace 侧 process library（31 序列）覆盖 7 个子类，但**不含 Other/动机类**（动机/程序性过程仅 think-aloud 能测）；think-aloud 编码方案含 9 个代码（8 个过程 + No_process）。

### 10.9–10.11 Key Action / Phantom Item / Misconception
**NOT APPLICABLE**。

### 10.12 Multimodal Joint Modeling
联合分析分三步（PDFPAGE 6–8）：V1=trace 测得的过程；V2=think-aloud 测得的过程；V3=整合结果。
1. **对齐**：两路结果对齐到同一时间轴（毫秒级），把时间轴按"两路所有段的起止时间戳"切成**细粒度段（grey boxes）**。
2. **五类对齐情形（S1–S5）**：S1 No_measurement（两路皆 No_process）；S2 Only think aloud（V1 为 No_process，V2 为某过程）；S3 Only trace；S4 Matched co-occurrences（两路检出同一过程）；S5 Unmatched co-occurrences（两路检出不同过程，**两个过程都赋给该段**）。
3. **整合**：生成整合 SRL 过程集（V3）；部分重叠按情况处理（如 MC.P 前半段算 S4、后半段算 S2）。**整合段数不是两路之和**（图 3 例：trace 6 个过程 + think-aloud 6 个过程，整合后 14 个），因为 think-aloud 极细粒度且大量短沉默段被标为 No_process。实际数字：44 人共得 trace 9,993 个过程、think-aloud 38,856 个、整合 83,121 个（PDFPAGE 14）。
统计比较：因数据非正态，报告 25th/中位数/75th；用 **Friedman 检验 + Bonferroni 校正的 Wilcoxon 符号秩检验**。RQ2 用 **pMineR** 建**一阶马尔可夫模型（FOMM）**三张过程图，边阈值 5%，比较时若转移概率差 <10% 用黑边，≥10% 用绿/红（PDFPAGE 9–10、13）。

### 10.13 Added Value of Process Data（重点，所有数字已核对原文）
**分母与单位说明（关键）**：Table 5/6 表头均为 "Median (25th, 75th) duration (%)"，单位是**学习任务总时长的百分比**（按时间加权），报告 44 名学生的**中位数**。
- 仅用 think-aloud 检出 SRL 过程占整个学习会话的 **57.82%**（中位数），仅用 trace 占 **80.21%**（中位数）（PDFPAGE 10）。
- 对齐后逐段归入 S1–S5，各情形百分比 = 该情形段总时长/学习会话总时长。摘要表述"17.18% of all the time segments"（PDFPAGE 1）即匹配段占全部时间轴段（按时长计）的中位比例。由于是中位数，五数之和 ≠100%（6.37+11.34+34.48+17.18+27.17=96.54）。
- **五类情形（Table 5）**：S1 No_measurement = **6.37% (4.18, 11.68)**；S2 Only think aloud = **11.34% (4.65, 16.84)**；S3 Only trace = **34.48% (26.10, 39.91)**；S4 Matched = **17.18% (13.71, 23.63)**；S5 Unmatched = **27.17% (21.47, 33.72)**。
- **互补与可互换**：S2+S3 = 45.82% ≈"around 45%"——约 45% 的时间段只能被其中一路检测到（互补）；S4+S5 = 44.35% ≈"around another 45%"为共现情形（PDFPAGE 11）。**可互换（匹配）仅 17.18%**，结论句："think aloud and trace data could be interchangeably used to measure SRL processes for only a small percent (17.18%) of all time segments in a learning task"（PDFPAGE 14）。
- **逐过程明细（Table 6）**：各行分母 = 该过程在**任一通道**中被检出的全部时间（并集）；中位百分比：

| 过程 | S2 仅TA | S3 仅trace | S4 匹配 | S5 不匹配 |
|---|---|---|---|---|
| MC.O | 1.96 | 43.76 | 6.24 | 40.37 |
| MC.P | 12.65 | 0.00 | 0.00 | 75.98 |
| MC.E | 0.00 | 5.70 | 0.00 | 66.62 |
| MC.M | 11.14 | 12.89 | 1.11 | 68.05 |
| LC.F | 9.07 | 29.27 | 26.73 | 30.84 |
| LC.R | 0.02 | 38.44 | 0.00 | 56.38 |
| HC.E/O | 4.93 | 30.02 | 11.30 | 45.25 |
| Other | 11.69 | 0.00 | 0.00 | 88.31 |

- **交叉表（Table 7）**：分母每行为"think-aloud 标为该代码的全部时长"，列显示该时段内 trace 检出的过程分布（行和≈100%）。对角元（think-aloud 某代码被 trace 同代码匹配的比例）：MC.O 45.27%、MC.P 4.45%、MC.E 0.00%、MC.M 4.70%、LC.F 75.01%、LC.R 9.66%、HC.E/O 36.56%；OTHER 行无对应 trace 列，其时间内 trace 多判为 LC.F（32.44%）与 HC.E/O（38.42%）。正文强调："0% of MC.E, only 4.45% of MC.P and 4.70% of MC.M...was also detected as the matched processes in trace data"（PDFPAGE 12）。原因：MC.E/MC.P/MC.M 频率极低（总和 <8%）、时长极短（查计时器 <2s），trace 难以在完全同一时刻检出。
- **Inter-rater reliability**：κ=.53–.65，kmax=.81–.82（PDFPAGE 7）。
- **三通道时长对比（Table 8，中位数%）**：MC.O trace 7.31/TA 1.97/整合 7.23；MC.P 0.00/2.36/2.21；MC.E 0.00/0.00/0.08；MC.M 2.20/5.20/6.06；LC.F 33.78/21.78/35.75；LC.R 5.07/0.45/4.91；HC.E/O 25.33/16.40/26.22；Other 0.00/7.84/5.84（PDFPAGE 12）。**元认知过程两单通道各约 10%，整合后升至 15.58%**（PDFPAGE 14）。

### 10.14 Validation Evidence
- Content evidence：过程类别源于 Bannert (2007) 理论框架；trace 侧映射基于既有 trace-SRL 文献。属研究者按理论定义。
- Response-process evidence：论文主旨即是——两路"测量同一学习时段的同一 SRL 过程"只有 17.18% 匹配、45% 互补、27.17% 分歧，且两路测得的时序转移图在元认知→认知转移上相互印证（如 Planning/Monitoring→Elaboration/Organization、First-reading 的转移在两图中都显著；PDFPAGE 18）；think-aloud 独有的 MC.E→LC.F 转移（25%）在 trace 图中为 0%（PDFPAGE 16）。
- Internal structure：过程类别层级结构如 Table 1；未做因素/结构方程类检验。
- Relations to other variables：**NOT PROVIDED**（全文未涉及学习结果变量）。
- Consequences：**NOT PROVIDED**。
- Convergent evidence：17.18% 匹配（S4）与 LC.F 上 75.01% 的交叉表匹配可视为两路汇聚证据；process map 层面元认知→认知转移在两路都出现（PDFPAGE 18）。
- Discriminant evidence：部分体现为两路各检测到对方测不到的过程（动机/程序类仅 think-aloud；Orientation/Re-reading/HC.E/O 大量仅 trace）。
- Expert evidence：**NOT PROVIDED**。
- Think-aloud：全文核心数据通道之一；编码一致性 κ=.53–.65。
- Retrospective report：**NOT USED**（本研究为并发 think-aloud，非回溯报告）。
- Eye tracking：作为 trace 的一路通道（300Hz，Tobii TX300），用于提高动作标注粒度与效度。
- External criterion：**NOT PROVIDED**。
- 论文自认局限性："没有充分展开测量协议的有效性问题"，指向姊妹篇 Fan, van der Graaf et al. (2022)（PDFPAGE 19）。

### 10.15 Ground Truth
**没有把 think-aloud 当作 ground truth**。论文明确采取**中立立场**："we adopted a neutral position towards two methods and considered the different measurement results based on trace data and think aloud data as equally valid. Therefore, in situation 5, we considered two unmatched SRL processes co-occurred without presuming only one process as the correct result and the other one as the incorrect result"（PDFPAGE 8）。讨论再次强调："neither of the two methods can be considered as fully 'truth' in measuring SRL processes (Winne, 2019). Therefore, instead of considering the unmatched cooccurrences as contradictions where researchers need to choose one, we adopt that such unmatched co-occurrences may reflect SRL processes that a learner **simultaneously has engaged in**"（PDFPAGE 18）。

### 10.16 Circularity Risk
存在**类别定义同源导致的潜在循环**：trace 侧 process library 与 think-aloud coding scheme 都基于同一 Bannert (2007) 框架，两路被"强制"映射到同一套预设类别——这保证了可比性，但**也意味着一部分"一致"是设计出来的**（框架错则两路一致地错）。不过，具体检测过程相互独立（自动 parser 对人工编码），17.18% 的低匹配率说明"一致"并未被机械制造；且论文承认对齐结果严重受两套操作化方式影响："how the SRL processes operationalized in the think aloud coding scheme (Table 4) and the trace-based measurement protocol (Table 3) heavily influenced the alignment results"（PDFPAGE 19）。

### 10.17 Alternative Explanations
论文对 trace 与 think-aloud 不一致给出多种替代解释（PDFPAGE 11、18–19）：
1. **未语言化的行为**：trace 捕捉了学习者没有（或无法）出声表述的 SRL 过程，如重读。
2. **think-aloud 捕捉了无对应可观察行为的陈述**：如口头表达 Planning/Monitoring 但没有对应的鼠标/键盘交互。
3. **同一过程但说话时间短**：30 秒的 Orientation（trace 检出）中学习者只口头说了一句话（约 5 s），其余 25 s 无声音 → 算 S3（仅 trace）。
4. **方法本身缺陷**：think-aloud 的编码者偏差、学习者无法对所有过程及时出声、trace 动作模式被误推断为 SRL 过程。
5. **同时发生但测量精度限制**：S5 共现可能 (i) 实为极细粒度先后发生、因测量精度有限在时间轴上重叠，或 (ii) 实为一个当前理论框架尚未定义的新 SRL 过程。
6. **工作记忆限制**：有观点认为同时活跃的信息元素数量很少，质疑同时多过程的真实性。
7. 无观察交互不等于无认知交互。

### 10.18 Temporal Alignment（重点）
- **对齐方式**：两路 SRL 过程段对齐到**同一时间轴（毫秒为单位）**，以两路所有段的起止时间戳为断点切成**细粒度段**（grey boxes），逐段分配 S1–S5（PDFPAGE 8）。
- **对齐单位**：由事件边界定义的时间段（非固定长度窗）；每段长度可长可短。
- **困难与处理**：think-aloud 极细粒度且大量 No_process 短沉默段导致整合时产生大量新段（9,993 + 38,856 ≠ 83,121）；部分重叠时段按重叠与否拆分（MC.P 例子）；编码者代码可重叠到不同范围，用 ELAN 处理计时；"不匹配"可源于时间对齐/测量精度，而非真正的过程差异。注：正文出现章节交叉引用笔误（对齐规则实为 3.2.4 节，正文多处写 "Section 4.2.4"）。

### 10.19 Person / Item / Context Dependency
- **个体差异**：think-aloud 有效性受"学习者用有用数据表达思想的能力差异及同时学习+出声的认知负荷"影响（PDFPAGE 17）。
- **任务/环境依赖**：SRL 测量情境敏感（Winne 2017）——学习材料如何排版、环境如何设计、提供哪些工具都影响可测性；例如 planner 工具才使 Planning 过程可被双路测量（PDFPAGE 19）。"泛化到其他任务/工具需特别关注情境要素"。
- 特定过程与任务的耦合：trace 中 HC.E/O 突出，部分因任务是多源写作（PDFPAGE 15）。

### 10.20 Generalization
**样本**：44 名大学生（39 本科 + 5 研究生），平均年龄 21.70 岁（SD=2.99），荷兰某大学实验室环境（PDFPAGE 5）。**任务/情境**：45 分钟、3 主题阅读 + 多源写作短文、专用 TEL 环境（23 英寸屏、Windows 10、Tobii TX300）。**泛化范围**：所有数值均为 within-sample 描述（中位数/IQR）；无交叉验证或跨任务验证。论文明确承认复制困难——"replication of our study may pose challenges...may not be able to collect both think aloud and trace data at the same time, due to practical constraints"（PDFPAGE 19）；强调对齐/整合方法在"两路遵循同一理论模型"的前提下有一定普适性；具体 SRL 过程类别与动作库则高度绑定本环境。

### 10.21 Evaluation（全部数值核对原文）
- **核心百分比（分母=学习任务总时长，按段时长加权；报告 44 人中位数）**：think-aloud 单路检出 57.82%，trace 单路 80.21%；对齐后 S1=6.37%、S2=11.34%、S3=34.48%、S4=17.18%、S5=27.17%（Table 5）；S2+S3≈45%（互补）、S4+S5≈44%（共现）。
- **Inter-rater reliability**：κ=.53–.65，kmax=.81–.82。
- **过程级交叉表匹配率（分母=各 think-aloud 代码总时长）**：MC.O 45.27%、MC.P 4.45%、MC.E 0.00%、MC.M 4.70%、LC.F 75.01%、LC.R 9.66%、HC.E/O 36.56%。
- **显著性检验**：Friedman + Bonferroni 校正 Wilcoxon，标记 a（trace vs 整合）、b（think-aloud vs 整合）：MC.O b***；MC.P a***；MC.E b*；MC.M a***；LC.F b***；LC.R b***；HC.E/O b***；Other a*** 且 b*（PDFPAGE 12）。
- **FOMM 转移概率（trace 图）**：LC.F→LC.F 自环 81%；LC.F→HC.E/O 10%；LC.F→MC.M 9%。think-aloud 图：MC.O→MC.O 自环 78%；MC.E→LC.F 25%（trace 图对应 0%，PDFPAGE 16）。整合 vs trace 对比：LC.R→LC.R 自环高 12%，HC.E/O→HC.E/O 自环高 16%（PDFPAGE 17）。
- **过程计数**：44 人 trace 9,993、think-aloud 38,856、整合 83,121。
- 无 correlation/regression 类效度统计。

### 10.22 Transfer to Our English Reading System
（我们的系统无全程 think-aloud；拟用答题后的 stimulated retrospective report，即回放界面+提问。）
- **Directly Transferable**：
  - **对齐-比较框架本身**：E7 的"同一时间轴 + 细粒度分段 + S1–S5 情形分类"与**交叉表**（Table 7）方法不依赖具体环境，可原样用于我们的 trace（滚动/回看/划线/选项操作）↔ 回放式 verbal 报告。
  - **过程挖掘对比（FOMM、5% 边阈值、绿/红叠加比较）**：迁移无碍。
  - **中立立场/不设 ground truth、把分歧视为 unresolved co-occurrence（而非必须判定单一真值）的处理**：可直接采用（但"同时进行多个过程"只是论文对 S5 的可能解释之一，不能作为"同时认知"的直接证据，§10.17）。
  - Bannert 框架的类别（MC.O/MC.P/MC.M/MC.E/LC.F/LC.R/HC.E/O）是相对 domain-general 的 SRL 框架，可作 **Candidate theoretical coding framework / Transfer With Modification**（反馈修正：不列 Directly Transferable）——它作为我们阅读任务 verbal 编码的候选类别可用，但 E7 并没有验证它在我们这种英语阅读理解 + 选择题 UI 中就是正确的 cognitive state taxonomy；我们的 EVIDENCE_SEARCH / OPTION_EVALUATION / EVIDENCE_INTEGRATION 等 construct 并不完全等于 Bannert SRL categories。
- **Transfer With Modification**：
  - **trace 侧动作库/过程库必须重写**：Table 2/3 的 18 个动作与 31 个序列针对"多源写作 TEL"构建；需替换为我们的阅读-答题动作库（reading、re-reading/backward scrolling、highlight/underline、text selection、option selection、answer change、option elimination），并重新定义动作序列→SRL 过程映射。
  - **时间对齐方式**：E7 的毫秒级同步基于**并发采集**。stimulated retrospective report 是事后采集，无法并发毫秒同步；需改为**回放锚点对齐**——以回放界面时间轴和关键 trace 事件（滚动、划线、答题）为锚，把 verbal 报告片段贴到这些事件上。E7 的"细粒度段"方法仍可用，但段边界取决于回放锚点而非两路并发生成的时间戳，粒度更粗。
  - **"只出声/只 trace"情形的语义变化**：E7 把"仅 trace 检出"解释为"有行为但未出声"；在回溯式报告中，未口头报告的时段可能有"记得但未说"与"当时无此过程"两种混杂，需在访谈设计上区分。
- **Not Transferable**：
  - **并发同步假设与 26 dB/0.30 s 的自动切分**不适用于回溯报告；回溯数据的切分单元需另定。
  - **具体数字本身**（如 17.18% 匹配、34.48% 仅 trace）完全绑定该任务/工具/人群，不可外推为我们的预期匹配率。
  - 动机/程序性过程在 trace 中的缺失结构在阅读 UI 中同样存在，但不构成"可迁移成果"。
- **对"stimulated retrospective report 后做 trace↔verbal 对齐比较"的总体评估**：E7 的**比较与分析层（情形分类、交叉表、过程图、中位数/IQR 报告）可迁移性很高**，值得照搬其模板；**对齐层需从"并发毫秒同步"改为"回放锚点对齐"**，这正是 E7 未覆盖（它只用并发 think-aloud）；大约 60–70% 的方法论可迁移，剩余部分需针对回溯数据特性自行设计。

### 10.23 What This Paper Does NOT Establish
- **没有确立 think-aloud 是认知 ground truth**：论文明确说两路都 "cannot be considered as fully 'truth'"（PDFPAGE 18）。
- **没有确立 trace 与 think-aloud 可互换**：恰恰相反——只有 17.18% 时间段可互换，且 "should not be used interchangeably for certain SRL processes such as Planning, Evaluation and Monitoring"（PDFPAGE 17）。
- **没有解决"不匹配共现（S5）"的机制**：未判定 S5 究竟是真同时过程、测量伪影还是未定义的新过程。
- **没有建立整合测量"更有效"**——只表明整合"更完整、更复杂、信息更丰富"，未提供整合结果 vs 外部效标（如成绩）的效度证据。
- **没有完成测量协议本身的效度验证**（指向姊妹篇 Fan, van der Graaf et al. 2022）。
- **没有覆盖动机/情感过程**（只聚焦认知与元认知）。
- **没有提供跨任务/跨情境的泛化证据**，且承认并发双路数据采集的复制困难。
- **没有把 45% 互补、27.17% 分歧解释为方法的"错误率"**：论文把它们解读为两路各自捕捉不同侧面的合法测量结果，而非某一方的失效。

---

## 9. E8 — A Validation Study of a Middle Grades Reading Comprehension Assessment

> **论文定位**：**Reading-Specific Response-Process / Construct Validity**，是 E 组与**英语阅读理解场景最接近**的一篇。Severino et al. (2018)，*RMLE Online* 41(10): 1–16。

### 10.1 Research Question
总体研究问题："To what extent do ACE Assessment data provide validity evidence that meets criteria for being considered a valid and reliable assessment of student reading comprehension?"（PDFPAGE 3）。目的：让课堂教师能用其结果指导教学。类别归属：reading validation / construct validity / response-process validity（think-aloud）/ 多来源效度证据 triangulation。

### 10.2 Construct
用论文自身术语：**reading comprehension（阅读理解）**，以 **adolescent reading model**（Deshler & Hock, 2006）为框架，整合 **simple view of reading**（Gough & Tunmer, 1986; Hoover & Gough, 1990）与 **construction-integration theory**（Kintsch, 1994）。模型含三个相互依赖成分：**word recognition（词汇识别）**、**language comprehension（语言理解：背景知识、文本结构）**、**executive processes（执行过程）**（PDFPAGE 3）。ACE 声称是阅读理解的**直接测量**（PDFPAGE 2 摘要）。

### 10.3 Observable Process Data
- **Raw observable**：
  - **测试成绩**：33 名八年级学生在 ACE（web 应用）上作答 1 篇信息文本 + 11 道四选一选择题，每题 4 选项、赋分 3/2/1/0，正确=3 分；干扰项按"学生常见错误构念"编写（PDFPAGE 6）。
  - **think-aloud 口头协议**：5 名学生的**同步（concurrent）口头报告**（Ericsson & Simon 的 Level 1 直接言语化 + Level 2 编码言语化）（PDFPAGE 7）；录音并专业转写。
  - **fNIRS 血氧数据**：7 名学生佩戴 fNIRS（730/850 nm，前额 16 通道），记录答题期间前额叶氧合血红蛋白变化（PDFPAGE 9）。
  - **作答日志/时间**：总分、阅读时间、回看次数、每题耗时（PDFPAGE 3）。
  - **现场笔记**：小组施测、think-aloud、fNIRS 时的观察。
- **Derived process indicator**：think-aloud 被**演绎编码**为"答案选择与预期构念是否对齐"；fNIRS 数据被提取为每题氧合变化与文本依赖性指标。

### 10.4 Process Feature Construction
- **Think-aloud 采集**：研究者先朗读脚本介绍流程并**用数学题示范/演练**（"What is 10 squared?"；"What is the average of 10, 15, and 5?"）以避免数学之外的题目污染自述（Pressley & Afflerbach 1995 观点）；随后读改编自 Cordon and Day (1996) 的指导语：可静默读 passage，但**答题时须出声说出所想**，无时间限制、不计分（PDFPAGE 7–8）。研究者追问："How do you know that is the correct answer?" 等。
- **编码**：**演绎编码（deductive coding）**；**closed codes 镜像此前编写题干/答案/干扰项所用的多选题构念**；研究者为每种题型制作数据收集表（Table 3 示例为 literal 题），逐份转录读，找"学生选择或不选择某答案的理由与预期干扰项构念对齐"的言语证据；表结构：第 1 列 key+干扰项、第 2 列打勾（对齐）、第 3 列答案构念、第 4 列转录原文引文（PDFPAGE 8）。
- **literal 题干扰项构念示例**（Table 3）：干扰项 1"基于文本的字面事实但信息不完整/与问题部分相关"；干扰项 2"基于文本的字面事实但与问题无关"；干扰项 3"文本中没有的共同背景知识"。
- **编码者**：**一名研究者**逐份编码；**coder agreement / inter-rater reliability / conflict resolution：NOT REPORTED**。
- **fNIRS 处理**：原始强度检查后剔除；有限脉冲响应低通滤波（截止 0.1 Hz）；经修正 Beer–Lambert 定律转为氧合/脱氧血红蛋白变化（相对任务前静息基线）；每 16 通道按"问题开始到最后一个答案"切 epoch，用问题前 **5 s** 做基线校正；取 epoch 均值用于题型与作答比较；聚焦氧合血红蛋白（PDFPAGE 9）。

### 10.5 Cognitive Interpretation
- (b) 专家/标准定义为主：答案构念由专家面板（受心理测量学家训练）依据 CCSS ELA 标准预先定义，并用于写题、写 key、写干扰项（PDFPAGE 7）。**演绎编码方案直接从这些构念导出。**
- (a) 理论显式：adolescent reading model 提供理论框架（PDFPAGE 3）。
- (d) 事后解释：think-aloud 结果事后用于**修订构念**（词汇题、关键观点题）或决定不改（主旨题）（PDFPAGE 10）。
- fNIRS 氧合高/低被解释为"是否使用前额叶/阅读文本"，即**文本依赖性**（PDFPAGE 11）。

### 10.6 Mapping
- ① 口头言语化（think-aloud）↓ 演绎编码后的"答案选择理由与预期干扰项构念是否对齐"↓ 预期阅读理解构念（literal/inference/vocabulary/main idea 等）。
- ② 选择题作答（对/错、选项）↓ 对/错、选择某干扰项↓ 阅读理解能力（经 Rasch 定位为单一潜在构念）。
- ③ fNIRS 氧合变化（前额叶）↓ 每题平均氧合水平↓ "文本依赖 / 是否真正阅读了文本"。
- 箭头依据：①是研究者把学生言语与"编写题目时所用的构念"比对（专家定义的封闭编码）——**内在循环依赖见 §16**；②依据 Rasch 单维拟合与 PCA；③依据"前额叶活动=注意/工作记忆/对文本的加工"的脑成像文献假设（引 Landi et al. 2013; Perfetti & Hart 2002 等）。

### 10.7 Who Defines the Mapping?
**研究者 + 专家面板**：专家面板（n=3）定义文本难度与题型；研究人员预设"每个问题类型→相应答案构念"；think-aloud 编码由**研究者**按预设构念完成；fNIRS→文本依赖的映射由研究者依据神经科学文献设定。学生自报仅作为被编码的原始数据，不直接定义映射。

### 10.8 Q-Matrix / Attribute Structure
题型/内容结构 = **blueprint 式**：11 题按题型与 CCSS ELA 八年级标准对齐：2 literal、2 inference、1 vocabulary、1 summary、1 best evidence、1 key idea、1 author's point of view、1 text structure、1 author's purpose；每题 4 选项（PDFPAGE 6）。文本复杂度经 Lexile（1070）与 CCSS Text Complexity 量表评估（PDFPAGE 7）。
**"题型分类 ≠ 潜在认知技能"问题存在（论文数据支持）**：Rasch PCA 显示仅 **41.2%** 方差被题目解释（<60% 阈值），第一对比残差 **12.5%**（可能次要维度但不足 3 题）（PDFPAGE 11）；think-aloud 对齐率各题型差异巨大（20%–58%），说明题型标签与真实认知过程并不一一对应（PDFPAGE 10，Table 4）。另：论文内部把推断题写"two inference questions"（PDFPAGE 6）又在 think-aloud 结果中说"the three inferential questions"（PDFPAGE 10），存在不一致。

### 10.9–10.11 Key Action / Phantom Item / Misconception
Key Action / Phantom Item：**NOT APPLICABLE**。Misconception：**部分相关但非正式**——干扰项被设计为"学生阅读时的常见错误"构念，教师可据此做教学决策（如按错误类型分组）（PDFPAGE 6）；主旨题混淆（主旨 vs 作者目的）被识别为"常见错误、可通过直接教学解决"（PDFPAGE 10）。但**没有正式的迷思概念诊断模型**。

### 10.12 Multimodal Joint Modeling
**有三角验证，但非形式化统计联合模型**：Rasch 心理测量、fNIRS 氧合、think-aloud、现场笔记被**迭代地交叉比较**（"each data source independently, then comparing multiple sources of evidence";"Rasch psychometric analysis findings were compared with fNIRS oxygenation outcomes and student think-aloud results"）（PDFPAGE 10、13）。Q6 案例三种证据共同决定改写构念；Q7 案例三种证据一致判定保留题目。**无联合似然/贝叶斯模型。**

### 10.13 Added Value of Process Data
- **think-aloud/response process 的增量贡献是本文核心论点**：仅凭心理测量无法发现 Q6 的问题——Rasch 认为 Q6 拟合良好、干扰项工作正常，但 think-aloud 显示学生作答与答案构念不对齐，教师将无法据此分析错误类型，于是构念被重写；"Using psychometric analysis (internal structure validity evidence) alone would not have illuminated this important discrepancy, which required response processing validity evidence to uncover"（PDFPAGE 13）。**这是概念性/案例论证，无数值化增量统计。**
- **fNIRS 的增量**：验证题目是否"文本依赖（text dependent）"，可剔除无需阅读即可作答的题（PDFPAGE 11–12）。词汇题低氧合→可能不需要读 passage 就能答。
- 论文提供的量化描述：think-aloud 总体对齐 41%、按题型 20%–58%（Table 4）——数字用于**定位有问题的题目**，而非证明"过程数据带来 XX 增益"。
> **Improved diagnostic performance does not by itself establish construct validity**——反过来说，E8 的响应过程证据不是用来"提高分类精度"，而是直接检验"item 是否诱发了预期认知过程"，这正是 Construct validity 侧的证据类型。

### 10.14 Validation Evidence（最重要，逐项）
按 AERA/APA/NCME (2014) Standards 五类效度证据组织，并有 fNIRS 作为内部结构证据的额外来源（Table 2，PDFPAGE 7）：
- **Content evidence**：专家面板（n=3）评审；Lexile 1070（在 6-8 年级 955–1155 带内）、Flesch Kincaid 八年级；CCSS "Standards Approach to Text Complexity" 量表；共识标准=至少 2/3 成员同意，本 passage 全部达成共识；两名专家共同审题，部分题与干扰项在施测前被修改（PDFPAGE 7、10）。
- **Response-process evidence**：think-aloud（n=5）同步协议 + 演绎内容分析；总体对齐 **41%**；literal **58%**；inferential **48%**；词汇 **20%**、主旨 **35%**、最佳证据 **50%**、关键观点 **20%**、作者目的 **55%**、文本结构 **45%**（Table 4，PDFPAGE 10）。据此修订词汇题与关键观点题构念；主旨题因三角验证保留。
- **Internal structure**：Rasch 测量。Rasch infit/outfit 的 ZSTD 均在 −2.0 到 2.0、均方 0.5–1.5 logits 内；无负 point-biserial；Rasch PCA **41.2%** 方差被题目预测（<60% 强单维阈值）、第一对比 **12.5%**；平均题难 M=**0.0**（SEM 0.49）vs 平均学生能力 M=**0.15**（SEM 0.81），在 ±2 SEM 内判定"测验难度合适"（PDFPAGE 11）。信度：item reliability **0.91**、separation **3.23**（判读基准：0.90/3.00 优秀，Duncan et al. 2003）。fNIRS（n=7）作为**文本依赖性**证据：词汇题低氧合（正确与错误作答均低）→可能无需读 passage（PDFPAGE 11）。
- **Relations to other variables**：学校间总分 ANOVA F(2,28)=**0.476**, p=**0.627**（无显著差异）；无 IEP 均值 **24.3 (74%)** vs 有 IEP **23.2 (70%)**；总阅读时间与总分相关 r=**0.305**（M=711.09 s, SD=415.87）、回看次数 r=**0.260**（M=4.15, SD=3.78），均不显著（Table 5，PDFPAGE 12）。论文原预期"读得快的分高"未获支持。
- **Consequences**：现场笔记与观察；**平均 7 分钟**完成一 passage（对比 Roe & Burns IRI 估计 30–50 分钟、Easy CBM 约 30 分钟）；无学生表现出焦虑/压力；低利害（low-stakes，不计入成绩）（PDFPAGE 12）。
- **Convergent evidence**：**NOT PROVIDED**（预期的时间-成绩正相关未出现，不能算汇聚证据）。
- **Discriminant evidence**：**部分**——学校类型、IEP 状态间总分无显著差异被用于论证"无显著偏见"（PDFPAGE 11–12）。
- **Expert evidence**：专家面板（n=3），受心理测量学家训练；共识标准≥2 人。
- **Think-aloud**：见上，响应过程证据核心。
- **Retrospective report**：**NOT REPORTED**（用的是同步并发协议，非回溯）。
- **Eye tracking**：**NOT PROVIDED**（用 fNIRS 而非眼动）。
- **External criterion**：**NOT PROVIDED**——未施测任何外部标准化阅读测验（如 Gates-MacGinitie、州考）作效标。所有关系分析都是内部变量。
- **补充（信度类）**：think-aloud 编码的 inter-rater reliability **NOT REPORTED**（单人编码）。

### 10.15 Ground Truth
think-aloud **未被正式称为 ground truth**，而是五种效度证据之一，与 Rasch、fNIRS 三角互证（"In light of triangulation with the statistical data...";"comparing multiple sources of evidence"）（PDFPAGE 10）。**但在 Q6 决策中它实际上被当作决定性证据**（心理测量说拟合好，think-aloud 说不对齐→决定重写构念，且 fNIRS 佐证），即"响应过程证据在个案层面充当构念解释的仲裁者"（PDFPAGE 13）。fNIRS 氧合（答题是否使用前额叶）被当作"是否读了文本"的补充生理代理——**但 higher prefrontal oxygenation ≠ 直接证明学生正在阅读文本；E8 自己的表述是 helped determine / represented the possibility...（反馈修正：fNIRS 是 supplementary physiological / neurophysiological evidence consistent with text engagement/dependence，不是文本阅读的 ground truth）**。

### 10.16 Circularity Risk
**存在明显循环风险，论文未明确讨论**：think-aloud 的编码方案（closed codes）"镜像"了**编写题目/key/干扰项所用的同一套构念**（PDFPAGE 8），然后"验证"学生是否按这些构念作答——相当于用产物的构念框架去检验产物本身。缓解因素（论文未明说）：总体对齐率仅 **41%**，各题型 20%–58%，说明编码并非必然自我确认；且 align 失败恰恰用于**修改**构念。另一角度：如果某题对齐率低，论文解读为"构念需要改"而非"编码方案需要改"——方向选择是研究者的。

### 10.17 Alternative Explanations
E8 对替代解释讨论有限：
- fNIRS：词汇题"正确与错误作答都低氧合"被解释为"不必读 passage 也能答"（可能依赖背景知识）（PDFPAGE 11）——这是对"低氧合"的一个替代解释。
- Q7 主旨题：学生能正确注意文本（fNIRS 高氧合）却答错，被归为"主旨 vs 作者目的混淆"（PDFPAGE 13）。
- 阅读速度与成绩不相关，论文承认**未追踪逐词阅读流畅度，只有总阅读时间**（PDFPAGE 12），即时间指标替代解释未排除。
- think-aloud 无反应/低质量反应的可能替代解释（抑制、任务负担、练习效应）**NOT DISCUSSED**。
- 未讨论"学生因出声思考而改变作答过程"的反应性（仅引用 Pressley & Afflerbach 说明指导语会影响自述，PDFPAGE 7）。

### 10.18 Temporal Alignment
- think-aloud 是**并发协议**：阅读时静默、**答题时出声**（PDFPAGE 8），因此 verbalization 与作答时刻对齐，但与**阅读阶段**无口头对齐。
- fNIRS：每题的 epoch 从"问题开始"到"收到最后一个答案"，用问题前 **5 秒**作基线校正（PDFPAGE 9）——与答题窗口对齐，不含独立阅读段。
- ACE 自身记录"阅读时间""回看次数""每题耗时"（PDFPAGE 3），但论文未报告逐事件时间线分析。

### 10.19 Person / Item / Context Dependency
- **学生特征**：样本阅读水平大致对齐 2017 NAEP 八年级（本样 proficiency+basic 约 **69%** vs NAEP **72%**）（PDFPAGE 6）；58% 有 IEP；有语言学习障碍私立校学生（IEP）与无 IEP 学生成绩相近（24.3 vs 23.2）。
- **题项**：think-aloud 对齐率强烈依赖题型（20%–58%）；fNIRS 文本依赖性逐题判断。
- **上下文/年级**：仅八年级、单一 passage（1070 Lexile 信息文本），结果不能推广到其他 passage（PDFPAGE 14）。

### 10.20 Generalization
- **样本代表性**：33 名学生、4 校（私立郊区 n=10、私立郊区 n=7、公立城区 n=12、公立郊区 n=4）；全来自美国东北部，**地理泛化受限**（PDFPAGE 6、14）。作者称样本量满足所用统计方法的最低要求（PDFPAGE 14）。
- **题项/文本泛化**：只验证了 ACE 中**一篇** passage（ACE 共 6-8 年级各 10 叙事 + 10 信息文本）；明确 "across passages cannot be assumed"（PDFPAGE 14）。
- think-aloud n=5、fNIRS n=7 的子样本很小，结论为探索性。

### 10.21 Evaluation（所有数字核对原文）
- **Content**：Lexile 1070（Flesch Kincaid 8 年级）；专家共识全部达成（≥2/3）。
- **Response process**：整体对齐 41%；literal 58%；inferential 48%；vocabulary 20%；main idea 35%；best evidence 50%；key idea 20%；author's purpose 55%；text structure 45%（Table 4）。
- **Internal structure**：item reliability **0.91**、separation **3.23**；fit ZSTD −2.0~2.0、MNSQ 0.5~1.5；PCA 预测方差 **41.2%**；第一对比 **12.5%**；题难 M=0.0（SEM=0.49）、能力 M=0.15（SEM=0.81）（PDFPAGE 11）。
- **External relationships**：ANOVA F(2,28)=0.476, p=0.627；r(读时)=0.305；r(回看)=0.260；M/SD 见 Table 5。
- **Inter-rater reliability**：**NOT REPORTED**（think-aloud 单人编码）。
- **fNIRS**：无统计检验报告，呈现为逐题氧合模式描述（词汇题低、Q7 高但无人答对）。

### 10.22 Transfer to Our English Reading System
- **Directly Transferable**：
  - **五类效度证据的组织框架**（content / response process / internal structure / relations / consequences）与"迭代交叉比较、不单靠心理测量"的整体方法论，可直接用于我们系统每套 passage 的效度论证。
  - **核心教训**：即便题目在心理测量上拟合良好，也可能存在"作答与预期构念不对齐"的隐性问题（Q6 案例）——这对我们双栏 UI 下"学生为何选某个选项"的解释尤其重要。
  - "题型标签≠潜在认知技能"的证据（对齐率 20%–58%、PCA 41.2%）提醒我们：literal/inference/main-idea 这类题型划分**不是**认知过程的保证，需过程数据佐证。
  - 干扰项"常见错误构念"设计思想可迁移到我们选题系统的选项设计，使错误答案带诊断语义。
- **Transfer With Modification**：
  - think-aloud 协议本身不可照搬（我们无 think-aloud），但其"演绎编码、把作答理由映射到构念"的逻辑可以改造为：**用回看/划线/选文本/改答案/划掉选项等行为痕迹**推断学生用了什么策略，即"行为代理版 think-aloud"。
  - 文本依赖性检查：用 fNIRS 证明"题需读文本才能答"的做法，在我们系统可近似为"检查某题是否仅凭常识/题干即可作答"（如高正确率 + 极短作答时间 + 无回看）。
  - Rasch 单维/信度检验需更大样本才可靠（n=33 太小），可作为后续规模化验证阶段的方法。
- **Not Transferable**：
  - fNIRS 脑成像文本依赖性验证（设备依赖、n=7）。
  - 具体 ACE 题型的答案构念表（我们的题目未按这套 CCSS 构念编写）。
  - 学校类型/NAEP 对标等本地样本结论。

### 10.23 What This Paper Does NOT Establish
- **没有**建立跨 passage、跨年级（仅 8 年级、仅 1 篇）、跨地域（仅美国东北）的推广性。
- **没有**建立外部效标效度：未与任何已确立的阅读理解测验做关联，其 "direct measure" 结论建立在内部证据链而非黄金效标上。
- **没有**报告 think-aloud 编码的评分者间一致性（单人编码），编码可靠性未量化。
- **没有**建立 ACE 能测出 adolescent reading model 的全部成分：对大多数学生"word recognition 不是问题"，词汇识别成分实际未被逐一测量（PDFPAGE 12）；执行过程仅靠 fNIRS 间接代理。
- **没有**证明"回答正确 = 真正阅读了文本"的充分性；fNIRS 数据显示有题（词汇）无需阅读即可作答。
- **没有**提供任何效应量级别的效度数值（仅显著性检验与描述统计）。

## 10. Cross-Paper Comparison Matrix

对应任务文件 §10 的跨论文比较。下表汇总 E1–E8 在关键维度上的分布。

| 维度 | E1 | E2 | E3 | E4 | E5 | E6 | E7 | E8 |
|---|---|---|---|---|---|---|---|---|
| 轨道 | A（背景） | A | A | A | A | B | B | B |
| 证据类型 | 综述 | 实证（真实数据） | 实证（真实数据） | 模拟 + 小实证 | 模拟 + 实证 | 框架/社论 | 实证 | 实证 |
| 领域 | 一般 CDM | PISA 售票机 | PISA 售票机 | 数学题（TEA） | PIAAC PSTRE | 计算机化测评 | 多源写作学习 | 英语阅读 |
| 过程数据类型 | RT | action sequence | action sequence | RT + fixation count | RT + sequence similarity/efficiency | 多类综述 | trace + think-aloud | think-aloud + fNIRS + 日志 |
| 进入 CDM 方式 | Route B | Route A | Route A | Route B | Route B | N/A | N/A | N/A |
| Key action 概念 | 无 | 有（核心） | 有（核心） | 无 | 无 | 无 | 无 | 无 |
| Phantom item | 无 | 28 个 | 14 个 | 无 | 无 | 无 | 无 | 无 |
| Q-matrix | 输入（未述构建） | 研究者预设，未验证 | 专家 retrofitting，PVAF 被否决 | 沿用外部，未验证 | OECD 输入，未验证 | N/A | N/A | blueprint（题型） |
| Mapping 定义者 | Q-matrix 未述 | 作者（研究者） | 专家/研究者 | 研究者（模型设定） | 专家（参考序列）+ 研究者 | 研究者（理论） | 研究者 + 编码者 | 专家面板 + 研究者 |
| 独立 response-process 证据 | 无 | 无 | 无 | 无 | 无 | 要求有（未提供） | 有（think-aloud 对 trace） | 有（think-aloud + fNIRS） |
| Think-aloud | 无 | 无 | 无 | 无 | 无 | 回顾提及 | 核心 | 核心 |
| Simulation 依赖 | 转述 | 无 | 无 | 主体 | 主体 | 无 | 无 | 无 |
| 循环风险 | 有（RT→speed） | 高 | 高 | 显著 | 显著 | 指出（要求破环） | 中（同源类别） | 中（封闭编码） |
| 泛化 | 无 | 单题 | 单题 | 无（N=93） | 无（N=935） | 否定跨题泛化 | 无（N=44） | 无（N=33） |
| Added value 结论 | 条件性增益 | 分类更细 | SE 更小 | 增量多数 <1% | 高相关才有增益 | 概念性 | 17.18% 可互换 | 案例性 |

**跨论文核心图景**：Track A 的 5 篇论文全部以"提高诊断精度"为叙事，但全部依赖研究者/专家预设的映射，无一附带独立 response-process 证据；Track B 的 3 篇论文恰好提供了 Track A 缺失的证据类型——但它们的结论（E7 的 17.18% 可互换、E8 的题型标签≠认知、E6 的指标需验证）恰恰动摇了"过程数据直接解释为认知"的默认假设。**E 组整体呈现"诊断工具已成熟、效度证据仍空缺"的结构性不对称（§42、§43）。**

---

## 11. 专题一：Key Action → Cognitive Attribute

对应任务文件 §11。本节完整还原 E2/E3 的 "From Key Actions to Cognitive Attributes"，并强制回答 Q1–Q5。

### 完整还原（E2/E3 合并；注意二者是不同题目）

```
Problem（E2: PISA TICKETS CP038Q02——买 2 张全价乡村火车单程票；E3: PISA TICKETS Task 2, CP038Q01——找坐 4 次地铁的最便宜方案）
↓
Action Sequence（log-file 逐事件，状态字母编码 A–I；删 CANCEL、压缩重复）
↓
Key Action Identification（N-gram 拆解：uni/bi/tri/quad；E3 从 228 序列按出现率+理论筛选到 14）
↓
Coding（包含编码：序列出现 ≥1 次记 1）
↓
Phantom Item（E2：28 个，其自身不含迷思概念的 baseline 为 10 个；E3：14 个二分题）
↓
Q-matrix（研究者从任务结构转写：正确状态→技能属性，错误状态→迷思概念属性）
↓
Attribute Diagnosis（HO-DINA/GDINA 估计属性掌握模式）
```

> 注：E2 与 E3 是**同一方法思想在不同 PISA 题目上的应用**（E2 在 E3 的 item-expansion/phantom-item 框架上扩展到 skills + misconceptions），**不是同一道题、也不是同一分析数据集**：E2 = CP038Q02、N=3547、28 题（不含迷思 baseline 为 10 题）；E3 = CP038Q01、N=3760、14 题（§36）。

### Q1. key action 是 necessary / statistically discriminative / expert-defined？
**三者混合，但以 expert-defined 为主。** E3 的筛选规则是：出现率 <5% 或 >95% 剔除（数据驱动统计规则）+ 保留理论上能反映技能的序列（Sao Pedro et al. 2012，专家理论判断）+ DINA 可识别性条件（Gu & Xu 2019）。E2 同样用 5%–95% 频率删题 + 作者从任务状态图定义。**"能反映技能"这一步是专家判断；出现率筛选是统计；"解决问题所必需"的措辞是任务设计给定的。** key action 既非"最终正确动作"（E3 的 phantom "correct response" = 动作出现），也非"必要动作"（低效路径被合并），而是"专家认为有诊断信息且出现率适中的动作序列"（§10.9 E3、§10.9 E2）。

### Q2. 学生没有执行 key action：是否一定代表 attribute non-mastery？
**不是一定，且论文没有排除替代解释。** E3 对 "buy" 动作的高 guess 参数（gi=0.442）承认"题目说明里写着要买票，不需要多少认知努力"——即该动作的出现不是属性掌握的证据。反方向：未执行某 key action 可能是界面困惑、随机点击、探索性点击、时间不足（E3/E2 均未系统排除，§10.17）。DCM 的 guess/slip 参数允许动作与属性之间的概率连接，但**没有独立证据说明未执行动作的具体原因**。**答案：不能自动等价 non-mastery。**

### Q3. 学生执行 key action：是否一定代表 attribute mastery？
**不是一定。** E3 中 pattern 11111 但得分 1 的 156 人，可能比较了价格但仍选择更贵的日票——即"替代策略/偏好"而非技能缺失（PDFPAGE 14）。执行了某动作序列也可能靠记忆/复制策略/运气（E2 的替代解释，§10.17）。且 E2/E3 的 "correct response" 定义为"动作序列出现"，**执行动作 ≠ 理解技能**——这是 key-action 编码的固有模糊。

### Q4. key action 是否可能被偶然完成 / 模仿完成 / 通过另一策略绕过？
**是，三者都可能。** 偶然完成：E4 的 guess 概念、E3 的 gi=0.442（buy）。模仿完成：E3 中"ind→other→trip 4"与"ind→trip 4"被合并为等价（低效路径），说明同一技能可由不同动作表达。绕过：E2 中允许漏选直接点 BUY（PDFPAGE 3），说明学生可以不完全走"标准路径"而完成购买。**key action 编码把"不同路径 → 不同属性需求"强加在 Q-matrix 上，但替代路径的语义未被验证。**

### Q5. Q-matrix 本身是否经过独立验证？
**没有。** E3 的 PVAF 经验验证被否决（revised Q 拟合更差 RMSEA2=0.085>0.05），专家输入获胜（PDFPAGE 12）。E2 无任何 Q-matrix 验证（仅"保留单位矩阵"保证可识别性）。E4 实证 Q-matrix 构建过程未报告。E5 直接采用 OECD Q-matrix。**Q-matrix 是测量输入而非被检验对象——这是 E 组最一致也最关键的缺口（§21）。**

---

## 12. 专题二：Misconception vs Non-Mastery

对应任务文件 §12。重点 E2。

### 理论上的区分
```
Wrong Outcome
        │
        ├── lack of mastery（没有执行关键步骤）
        │
        └── misconception（稳定执行一个错误规则）
```
行为序列上，"没有执行关键步骤"与"稳定执行一个错误规则"理论上可能分别对应 non-mastery 与 misconception。

### E2 实际做了什么
E2 **没有**在同一模型中区分这两种解释，而是把迷思概念编码为**附加的 4 个二元属性**（m1–m4），与技能属性并列进入 Q-matrix。错误状态转移（如选城市地铁 F）被编码为"需要对应迷思概念属性 m1"。"错误行动→迷思概念"是**编码假设**（"假设仅当参与者掌握了各行动序列所需的潜在属性后才能呈现该行动序列"，PDFPAGE 5），**不是经验证据**。模型层面允许的随机性只有 guess/slip 参数，但没有独立证据说明某次错误点击是"迷思概念"还是"偶然失误"（§10.11）。

**强制核对：论文是否真的区分了"稳定执行错误规则"与"未执行关键步骤"？没有。** 整个行动序列（含 CANCEL 重启的多次尝试）被压缩为一条序列、一张 28 位作答向量，"稳定执行错误规则"的时间一致性证据被丢弃。论文用常规 DCM（Kuo et al. 2018; Ma et al. 2024），把"迷思概念"当作普通的"错误路径属性"处理，**没有机制性区分偶然错误与系统性迷思**。个案 AUS000014102620（得 0 分 → 归因于共存迷思概念）是事后改标签，不是对随机性的检验（§10.11、§10.13）。

### E3 的补充
E3 不建模 misconception 潜状态。缺失技能与"错误动作"通过 Q-matrix 绑定（错误路径 = 缺乏相应技能的 evidence）；对特定错误类型（01001、11001）的解释是事后回读动作序列。无个体错误的归因检验。

### 对我们的意义
> 对英语阅读理解，是否可能诊断 skill deficit vs systematic misunderstanding？**目前只是可能性，不是文献支持**：E2 展示了把"错误选项→迷思概念属性"编码进 DCM 的机械流程，但其"错误=迷思"的映射无独立验证、无稳定错误的时间证据。我们的多选题里，一个学生稳定选同一干扰项（跨题）比单次选错更接近"systematic misunderstanding"——但这需要跨题的一致性证据，E 组没有直接模型。**标注：PROJECT TRANSFER HYPOTHESIS。**

---

## 13. 专题三：Diagnostic Utility ≠ Construct Validity（Process Data Improves Diagnosis ≠ Cognitive Meaning Is Valid）

对应任务文件 §13。综合 E1–E5，建立明确逻辑链：

```
Process Variable
↓
adds predictive information（E4 FC 的 5.49%、E5 的 ACA 0.863 vs 0.84、E3 的 SE 更小）
↓
classification improves
```

这只能支持：**process variable is diagnostically informative**。不能自动支持：**process variable represents construct X**。

### E 组论文中存在的 inference gap（逐条列出）

1. **fixation count improves CDM ⇒ fixation count = deep comprehension**（E4 禁止）：
   E4 的 FC 增益经 Σperson 相关结构的信息传导实现，FC 不加载在属性上（假设 8），且论文自己把 visual engagement 限定为 "loading amount endorsed by FCs" 而非完整注意（PDFPAGE 4）。增益最大 5.49% 仅在 Q-matrix incomplete + 高相关条件下。**推论：FC 提高分类 ≠ FC 测量认知技能。**

2. **sequence efficiency improves classification ⇒ efficiency = strategic competence**（E5 禁止）：
   E5 实证中能力−效率相关 −0.543（高能力者更不高效），与"效率=策略能力"相反；相似性−能力相关 0.990（近乎冗余）。论文把两者定位为提高分类精度的辅助指标 + 事后弱解释。**推论：efficiency/similarity 提高分类 ≠ 它们测量了策略胜任力。**

3. **phantom items 分类更细 / SE 更小 ⇒ key action = skill mastery**（E2/E3 禁止）：
   E3 的"更细分类 + 更小 SE"是模型对过程数据的再组织结果；E2 的 13→74 模式是属性扩容的结构后果；信度微升（.9899 vs .9852）与 28 个互相重叠 n-gram 的题目冗余相关。mapping 是模型输入，拟合好不验证映射正确。**推论：分类更细 ≠ mapping 正确。**

4. **RT improves diagnosis ⇒ RT = difficulty / speed construct**（E1 部分禁止）：
   E1 转述：RT 的认知解读（高 RT = 认知挑战）只是诸多解释之一，RT 也可由速度化作答、低动机、作弊导致（PDFPAGE 3）。**推论：RT 含预测信息 ≠ RT 的认知语义已确立。**

### 核心结论
E1–E5 提供的全部是 predictive / measurement utility 证据，**没有一篇提供 construct validity 证据**。construct validity 需要理论、任务设计、response-process 证据、convergent evidence、expert coding、verbal report、独立测量——这些在 Track B（E6/E7/E8）中出现，但 Track B 不建模诊断。**"诊断效用"与"构念效度"在 E 组文献内部是分离的，必须由我们自己对接。**

---

## 14. 专题四：Response Time / Fixation / Action Sequence 各自能提供什么

对应任务文件 §14。综合 E1/E4/E5。

| Process Data | What Is Directly Observed | Possible Information | Cognitive Meaning Strength |
|---|---|---|---|
| Response Time | 每 item/每动作的耗时（log 时间戳） | speed τ（person processing speed）+ item time-intensity ζ（E1/E4/E5 的 lognormal RT 模型，**ζ 不是 cognitive load**）；答题努力、脱离投入（E6 的 rapid-guessing）；难度相关 | **测量信号强**（RT 模型成熟、参数恢复好：E4 τ Cor .953–.978）；**认知语义弱**（RT 可由速度化/动机/作弊解释，E1 明确列出替代解释） |
| Fixation Count | 每 item 注视次数（眼动仪） | latent visual engagement ε（E4 NBF 模型） | **测量信号中**（ε 恢复好 Cor .966–.987）；**认知语义被论文限定**：只是注意负荷代理，"depends on context"；FC 不加载在属性上 |
| Action Sequence | 离散动作的有序流（log） | 动作的集合与顺序（E3/E2 的 key action、E5 的 LCS） | **测量信号依赖编码**（phantom item 0/1 或 LCS 摘要）；**认知语义取决于 mapping**——key action→skill 是研究者预设，未独立验证 |
| Sequence Similarity | LCS(obs, ref)/|ref|（E5） | 与最优参考序列的接近程度；能力−相似性相关 0.990 | **测量信号强，但与能力 0.990 高度重叠（推论）**；**认知语义可疑**（参考序列是专家预设，构造性循环风险） |
| Sequence Efficiency | LCS(obs, ref)/|obs|（E5） | 冗余动作程度；RT−效率相关 −0.940 | **测量信号中**（η 恢复 Cor 高）；**认知语义负向**（高能力者效率更低，与"效率=策略"相反） |
| Key Action | 特定动作/序列是否出现（0/1） | 对应技能/迷思概念属性（E2/E3） | **测量信号强**（分类信度 .99）；**认知语义完全依赖专家 Q-matrix，无独立验证** |

**严格区分**：Measurement Signal（该指标能被可靠建模、参数可恢复、能提高分类）与 Cognitive Construct（该指标代表某种认知过程/技能）。E 组全部论文的 Measurement Signal 都较强，但 Cognitive Construct 侧只有 E6/E7/E8 提供证据，且它们证明的是"**不能**轻易把行为当认知"。

---

## 15. 专题五：Trace ↔ Think-Aloud

对应任务文件 §15。重点 E7。所有数字已回 PDF 核对。

# Do Trace Data and Think-Aloud Measure the Same Cognitive Process?

### 采集方式
- **trace data**：TEL 环境自动记录导航、键盘、鼠标、眼动（Tobii TX300, 300Hz），经 trace parser（18 动作标签 + 31 动作序列）自动映射为 SRL 过程（E7 PDFPAGE 6–7）。
- **think-aloud**：麦克风录音 → Audacity 自动切分（26 dB 阈值、0.30 s 沉默分段）→ 3 名编码者按 Bannert (2007) + Molenaar et al. (2011) 方案编码（κ=.53–.65）。
- **temporal unit**：trace 是事件段（有起止时间戳）；think-aloud 是基于声音的片段。
- **alignment**：两路对齐到同一时间轴（毫秒），切成细粒度段，逐段归入 S1–S5。
- **agreement**：S4 匹配 = 17.18%；LC.F 交叉表匹配 75.01%。
- **disagreement**：S5 分歧 = 27.17%；S2+S3 互补 = 45%。
- **unmatched processes**：元认知过程（MC.P 4.45%、MC.M 4.70%、MC.E 0%）在 trace 中几乎不被同过程匹配；动机/程序类（Other）仅 think-aloud 能测。

### 论文报告的 agreement/disagreement 数值核对
- **17.18%**：S4 Matched（两路检出同一过程）占全部时间轴段（按段时长计）的中位比例，分母 = 学习任务总时长（Table 5，PDFPAGE 11）。不是"全部 think-aloud 编码段"的匹配率，也不是"全部 trace 事件"的匹配率。
- **27.17%**：S5 Unmatched（两路检出不同过程，两个过程都赋给该段）。
- **6.37% / 11.34% / 34.48%**：S1 No_measurement / S2 Only TA / S3 Only trace。
- 五数之和 96.54% ≠ 100%（因为是 44 人的中位数，非同一人的分解）。

### Q1. 为什么 trace 和 think-aloud 会不一致？
E7 给出多种替代解释（§10.17）：未语言化的行为（重读）、无对应可观察行为的陈述（口头计划）、同一过程但说话时间短、方法本身缺陷（编码者偏差、动作被误推断）、同时发生但测量精度限制、未定义的新过程。**核心原因：两路的操作化方式不同——一个捕获"做了什么"（可观察行为），一个捕获"说了什么"（可言语化过程），两者在时间上、语义上都不完全重合。**

### Q2. 哪一种更接近 cognition？think-aloud 是 ground truth 吗？
**论文明确说不。** E7 采取中立立场：两路 "equally valid"，"neither of the two methods can be considered as fully 'truth' in measuring SRL processes"（PDFPAGE 18）。think-aloud 有反应性、沉默片段难分析、编码者偏差、学习者表达能力差异；trace 有研究者多重推断的映射误差。**不能简单说 think-aloud = ground truth。**

### Q3. 两者应该 replace 还是 complement / triangulate？
**complement / triangulate。** E7 的整合方法把 S2/S3 互补段与 S4/S5 共现段都保留（S5 中两个过程都赋给该段），整合后元认知过程占比从两单通道各约 10% 升至 15.58%。**"互补"是论文的直接结论，可互换仅 17.18%。**

### Q4. verbal report 本身有哪些 measurement limitations？
论文讨论的：反应性（reactivity）、沉默片段难分析、编码者偏差（PDFPAGE 2–3）、学习者用语言表达思想的差异 + 同时学习+出声的认知负荷（PDFPAGE 17）。**只有论文讨论的才能说成论文结论。** 关于 incomplete verbalization、memory limits、non-verbal processes 等更一般的 verbal report 局限，E7 未系统讨论——如需引用，标注 **GENERAL METHODOLOGICAL CONTEXT**。

### 对我们的核心启示
E7 证明：**trace 与 verbal report 的 17.18% 可互换率（占学习会话时长的中位比例），意味着用 trace 单独推断认知过程会漏掉约 45% 的互补信息，并留下约 27% 的无法仅凭 trace 判定的分歧（unresolved co-occurrence）。** 如果我们只用 UI 行为 trace 做认知推断，等于只用了 E7 中 "Only trace + Matched" 的 ~51.66% 信息，且无法区分 S4（真匹配）与 S3（仅 trace）——**这是我们必须用 stimulated recall / 其他独立通道来补偿的缺口（§32、§34）。**

---

## 16. 专题六：Reading-Specific Response Process Validity

对应任务文件 §16。重点 E8。

# What Does Validating a Reading Comprehension Process Actually Look Like?

### 完整链条（E8）
```
Reading Construct（adolescent reading model：word recognition / language comprehension / executive processes）
↓
Item Design（blueprint：11 题按题型与 CCSS 对齐；干扰项按"常见错误构念"编写）
↓
Student Response Process（think-aloud：阅读时静默、答题时出声）
↓
Think-Aloud / Evidence（演绎编码：作答理由与预期构念对齐性）
↓
Validity Argument（五类证据：content / response process / internal structure / relations / consequences）
```

### 不同题型的 response process 证据（Table 4）
| 题型 | think-aloud 对齐率 |
|---|---|
| Literal | 58% |
| Inferential | 48% |
| Vocabulary | 20% |
| Main idea | 35% |
| Best evidence | 50% |
| Key idea | 20% |
| Author's purpose | 55% |
| Text structure | 45% |
| **总体** | **41%** |

**关键发现**：literal 题诱发预期过程的比例最高，词汇题最低（20%——fNIRS 显示词汇题可能无需读 passage 即可作答，即"背景知识依赖"而非"文本阅读"）。**题型标签与真实认知过程并不一一对应。** 论文据此重写了词汇题与关键观点题的构念、保留了主旨题（三角验证下 fNIRS 高氧合 + think-aloud 合理）。**这是"用 response-process 证据修订测试设计"的完整示范，也是我们最可能直接借鉴的方法学（§22 E8 的 Transfer）。**

---

## 17. 专题七：Validity Framework

对应任务文件 §17。综合 E6/E7/E8。

# What Evidence Is Required Before Calling a Process Feature "Cognitive Evidence"?

以下分层在 E 组文献中有不同程度支持。**总体框架是我们对 E6/E7/E8 的综合，标注 CROSS-PAPER SYNTHESIS。**

### Level 0 — Observable（E6 支持）
例如 ANSWER_CHANGE、SCROLL_BURST、UNDERLINE。E6 定义 process data = "任何可重复自动记录的显性行为测量"（PDFPAGE 1）。只是事实。

### Level 1 — Behavioral Interpretation（E6 支持）
回到 passage、改了选项、划了句子——仍然是行为描述。E6 强调 process data 是 manifest traces，不是 latent 构念（PDFPAGE 2）。

### Level 2 — Candidate Cognitive Interpretation（E6/E7 支持为 hypothesis）
evidence search、monitoring、uncertainty、integration——只是假设。E6 要求"理论 + 经验/实验验证"共同支撑（PDFPAGE 4）；E7 证明同一行为段（S5）可以对应多个候选过程，无法单靠 trace 消歧（PDFPAGE 18）。**Level 2 未经验证前只是 hypothesis。**

### Level 3 — Validated Cognitive Evidence（E6/E7/E8 给出方法）
需要理论 + 任务相关性 + 独立 response-process 证据 + 收敛/三角验证。E7 的两路对齐（S4 匹配）、E8 的 think-aloud + fNIRS + Rasch 三角互证、E6 的 "像产品数据一样验证" 都是这一层的操作。

### Level 4 — Diagnostic Attribute（E1–E5 的 DCM 输入层）
information integration skill、inference skill、evidence-location skill 等进入 CDM。**但 E 组没有一篇论文完成了 Level 2→3→4 的完整验证链**：Track A 直接跳到 Level 4（Q-matrix 预设），Track B 停在 Level 3（不做 CDM）。**这个断层正是我们项目的核心工作（§34、§43）。**

---

## 18. 专题八：Construct Validity vs Predictive Validity

对应任务文件 §18。

```
feature predicts score（criterion / predictive validity）
≠
feature measures intended cognition（construct validity）
```

一个 behavior feature 与正确率高度相关，仍然可能只是 general ability、reading speed、item difficulty、engagement 的 proxy。E 组的证据：
- **E4**：FC 与 attribute 的关系经 Σperson 相关结构实现，FC 预测 attribute 分类 ≠ FC 测量注意/认知技能。
- **E5**：相似性−能力相关 0.990 提示"预测能力强的特征"可能与能力高度重叠（CROSS-PAPER / ANALYTICAL INFERENCE），而非独立认知构念。
- **E2**：迷思概念属性与原始得分负相关（m1=−.78 等）——**但该负相关部分是内建的**（迷思概念属性由错误转移定义，而错误转移天然与低分相关）。预测相关 ≠ 构念同一性。
- **E7**：两路测量同一构念的一致率仅 17.18%——即使特征"预测"成绩（未测），也不能直接当构念证据。
- **E8**：阅读时间与成绩相关 r=0.305 不显著（论文原预期"读得快分高"未获支持）——一个看似直觉的预测相关直接被证伪。

**结论：Predictive correlation ≠ Construct validity。** 对项目：任何"行为特征与正确率相关"的发现只能作为候选证据，不能作为构念成立的依据（§39）。

---

## 19. 专题九：Triangulation

对应任务文件 §19。综合 E6/E7/E8。

### 各证据源能提供什么（基于论文）

| 证据源 | Strength | Weakness | Best Use（E 组论文内） |
|---|---|---|---|
| Trace（行为日志） | 自动、连续、生态（E7）；可规模化 | 只捕获可观察行为；研究者映射含多重推断（E7 PDFPAGE 4）；漏掉未语言化过程的语义 | E7：作为 SRL 过程的一路测量，与 think-aloud 对齐 |
| Think-aloud | 直接进入可言语化的认知过程；捕获无行为对应的陈述（E7） | 反应性、沉默段、编码者偏差（E7）；对齐率低（E8 41%） | E7/E8：作为 response-process 证据核心，与 trace/Rasch/fNIRS 互证 |
| Retrospective Report | （E 组未使用） | （E 组未提供证据） | — |
| Eye Tracking / fNIRS | 提供注意 / 文本依赖性的独立证据（E4 FC 是行为性注视计数；**E8 的 fNIRS 是生理 / 神经生理证据——supplementary physiological evidence consistent with text engagement/dependence，不是"正在阅读"的直接证明**，反馈修正） | 设备昂贵、校准失败、小样本（E6 PDFPAGE 6）；fixation ≠ 认知（C 组 + E4 限定）；前额叶氧合升高 ≠ 直接证明读了文本 | E4：visual engagement 的 indicator；E8：文本依赖性验证 |
| Task Outcome（成绩） | 可判定的成功/失败（A 组依赖） | 无法区分"策略正确"与"过程正确"；替代路径（E3） | E3：作为外部锚点与 latent 能力比较（r=0.826） |
| Expert Coding / Q-matrix | 提供领域理论（E2/E3/E5） | 无独立验证时是预设输入，形成循环（§21） | E2/E3/E5：定义 key action→skill 映射 |
| Rasch 心理测量 | 内部结构证据（单维性、信度）（E8） | 无法发现"拟合好但构念错"的问题（E8 Q6） | E8：与 think-aloud/fNIRS 三角互证 |

**基于论文的结论**：E7 证明两路数据互补（45%）；E8 证明单靠心理测量会漏掉构念问题（Q6 案例），必须响应过程证据介入；E6 证明过程指标必须像产品数据一样验证。**三角验证的价值在 E 组是"用独立来源约束解释"，而不是"找到唯一真值"。**

---

## 20. 专题十：Think-Aloud vs Retrospective Replay

对应任务文件 §20。我们的项目倾向 natural solving → session finished → screen/event replay → stimulated retrospective report，而非全程 think-aloud。

**强制问题：E 组文献能否直接支持 retrospective replay？**

### DIRECT SUPPORT
**没有。** E7 与 E8 全部使用**并发（concurrent）think-aloud**（E7：出声思维训练 + 全程出声；E8：答题时出声）。E7 明确 "Retrospective report: NOT USED"。E 组没有一篇直接研究 stimulated retrospective replay 的效度。

### INDIRECT SUPPORT
**有，但有限。** E7 证明 verbal response-process evidence（think-aloud 形式）与 trace 的 17.18% 可互换、45% 互补——这为"用 verbal 报告补充 trace"提供了原理支持，但**不验证 retrospective 形式的 verbal 报告**。E8 证明 verbal response-process 证据能发现心理测量发现不了的问题（Q6），支持"verbal 报告在效度论证中的角色"，但同样是并发协议。**把 think-aloud 的 validity 自动迁移成 stimulated recall 的 validity 是禁止的**（任务文件 §48-21）。

### PROJECT HYPOTHESIS
retrospective replay 需要我们自己验证。E7 给我们可迁移的**比较与分析层模板**（S1–S5 情形分类、交叉表、FOMM 过程图），但**对齐层需从"并发毫秒同步"改为"回放锚点对齐"**——这正是 E7 未覆盖的（§10.22 E7 的 Transfer）。retrospective 特有的风险（记忆重构、事后合理化、漏报自动化过程）在 E 组无直接证据，标注为 **PROJECT TRANSFER INFERENCE + 需自行验证**。

---

## 21. 专题十一：Circularity

对应任务文件 §21。

# How Can Cognitive Diagnosis Become Circular?

典型链：
```
Researcher assumes: Action A = Skill X
↓
Q-matrix encodes: A → X
↓
DCM estimates: Student lacks X
↓
Conclusion: A successfully diagnoses X
```

**模型可能只是把 researcher assumption 重新输出了一遍。**

### E2 的循环（具体化）
1. 作者假设"状态 F（选城市地铁）= 需要迷思概念 m1"（PDFPAGE 5）。
2. 该假设写入 Q-matrix（模型输入）。
3. 参与者的行动序列按**同一套映射**编码为 28 位作答向量。
4. GDINA 估计出"该生具有迷思概念 m1"。
5. 结论："引入迷思概念能诊断学生错误原因"。

**缓和因素**：DCM 的 guess/slip 参数允许动作与属性的概率连接；拟合指标、题目质量、相关方向是经验结果。**但**：作答向量与 Q-matrix 同源；13→74 模式是属性扩容的结构后果；信度微升与 28 个重叠 n-gram 的冗余相关；迷思概念−得分负相关是内建的。**E2 落入循环。**

### E3 的循环（具体化）
Q-matrix 明确是 "post hoc retrofitting"（PDFPAGE 7）；PVAF 经验验证被否决。HO-DINA 在此 mapping 输入上拟合最优，然后论文用模型输出（latent classes）与 observed scores 比较得出"更细"——但 scoring rule 与 Q-matrix 同源（OECD 2014）。**E3 落入循环。**

### E5 的循环（参考序列）
参考序列由内容专家预设 → similarity 定义为与参考序列的 LCS 比 → 作答正确与按最优路径操作相关 → 能力−相似性 0.990。**这个高相关很可能是构造出来的（definitional alignment），论文未讨论（§10.16 E5）。**

### 打破循环：E6/E7/E8 提供什么 independent validation？
- **E6**：要求预注册、by-design、"像产品数据一样验证"——把 mapping 从"默认成立"变成"必须被检验"（PDFPAGE 4–5）。
- **E7**：两路独立测量（自动 parser vs 人工编码）比较，17.18% 低匹配率证明"一致"没有被机械制造——**两路独立来源的对齐本身就是打破单一路径循环的方法**。
- **E8**：think-aloud + fNIRS + Rasch 三方互证，且 align 失败用于**修改构念**（Q6）——**独立响应过程证据可以推翻预设构念**。
**结论：打破循环的唯一出路是用独立于 Q-matrix/mapping 的证据源（verbal、专家、生理、任务设计）来检验映射。这是 §34 validation pipeline 的核心逻辑。**

## 22. 专题十二：Uncertainty Propagation

对应任务文件 §22。D 组指出 Action Episode 有 segmentation uncertainty；B/C 指出 behavior→cognition 有 semantic uncertainty。E 组必须检查：E1–E5 的 cognitive diagnosis model 是否允许 process indicators 带 uncertainty？

### 检查结果
- **E2/E3（phantom item）**：**全部使用 hard 0/1 指标**。行动序列包含某序列 → 1，否则 0。无概率化过程指标、无 segmentation confidence。phantom item 的 0/1 是确定性编码，但其"是否真正呈现该行动"的判定本身可能有测量误差（如日志噪声），论文未建模。
- **E4/E5（joint modeling）**：RT/fixation/sequence 指标进入模型时**不是作为已知固定值，而是作为观测数据经测量模型分解**（lognormal / NBF / logit 链接）——这天然带观测误差。但**"该过程指标反映什么认知过程"的语义不确定性没有被建模**：ε（visual engagement）被当作一个 latent trait 的点估计，其"是否真的是注意投入"的构念不确定性没有概率表达。
- **E1（RT-CDM）**：同 E4，RT 经测量模型处理观测误差，但 RT→speed 的构念解读是确定性的（假设）。
- **E6**：指出过程数据易受构念无关方差污染（噪音、题项、学生差异），但未提供量化方法。
- **E7**：S5（分歧）情形中两个候选过程都被赋给同一段——**这是"多候选解释 + 不消歧"的处理，最接近 uncertainty 的表达**，但论文未给每个候选赋概率。

### 结论
E1–E5 的 cognitive diagnosis model **基本不允许 process indicators 带构念不确定性**：过程指标要么是 hard 0/1（E2/E3），要么是经测量模型分解的观测（E4/E5），其"语义"被视为确定。**"P(Action) × P(Cognition | Action, Context) × P(Attribute | Cognitive Evidence)" 的完整不确定性链在 E 组文献中不存在。** 任务文件 §22 的预判被确认。E7 的 S5 处理是唯一接近"多候选 + 不强制消歧"的先例，但无概率化。

---

## 23. 专题十三：Student-Specific Interpretation

对应任务文件 §23。检查：同一个行为对不同学生是否可能意义不同？

### E 组证据
- **E7**：think-aloud 有效性受"学习者用有用数据表达思想的能力差异及同时学习+出声的认知负荷"影响（PDFPAGE 17）。同一 trace 行为（如重新打开阅读页）在不同学生身上可能对应"重读"（理解过程）或"没找到信息"（失败）——E7 承认 trace 侧映射可能误判（PDFPAGE 4）。S5 分歧中两个过程都赋给该段，正是承认"同一行为段可对应不同过程"。
- **E6**：神经多样性/残障以不可预见方式改变过程数据（如 time on task），对偏离常模个体产生无效推断（Zumbo et al. 2023，PDFPAGE 7）；即便对"平均应试者"有效的指标，也不保证在个体层面有效。
- **E4**：visual engagement "depends on the context"（PDFPAGE 4），未检验界面/任务类型/难度对 FC 意义的调节。
- **E5**：能力−效率负相关意味着"效率低"在高能力者身上反而是策略性的——**同一个效率指标在不同能力学生身上意义相反**。

### 结论
**SUPPORTED PRIMARILY BY GROUP B/C（revisit 对学生 A 是 evidence verification、对学生 B 是 comprehension failure），NOT RESOLVED BY GROUP E。** E7 承认个体差异影响 verbal 数据、E6 承认个体层面推断不可靠、E5 显示指标意义随能力变化，但**没有一篇 E 组论文提供"行为意义随学生变化"的系统建模**。这是需要我们自行处理的（结合 B 组的补偿性交互证据）。

---

## 24. 专题十四：Item-Specific Interpretation

对应任务文件 §24。过程行为必须放到 item context 中。

### E 组证据
- **E6**：停顿的类型"必须结合具体题项建模，不能跨题直接推广"（PDFPAGE 5）；题项特征（内容、措辞、显示设计、多媒体元素）改变过程数据（PDFPAGE 6）；大尺度测验题项保密不放行为过程数据加剧"无法跨题解释"的问题。
- **E3/E2**：Q-matrix 与 phantom items **完全题目特异**（"attributes have small granularity→low applicability across tasks"，E2 局限二）；E3 的 key action 定义只对 TICKETS 任务有效。
- **E5**：item-wise 相关显示 U02、U16 上相似性−效率相关绝对值特别高，U11b 上为正（0.224）——同一对指标在不同题目上关系方向都不同。
- **E8**：think-aloud 对齐率强烈依赖题型（20%–58%）——同一"对齐"指标在不同题目上意义不同。

### 结论
**E 组强证据支持"行为意义必须放回 item context"**：E6 明确要求按题建模、E8 显示题型调节、E5 显示题目调节。对我们项目：**回到 P2 这个行为，只有知道 Q3 的正确 evidence 是否在 P2，才能判断其意义——E 组文献直接支持这一 item-specific 原则（§24 的 Action + Item Semantics → Cognitive Evidence 是关键）。**

---

## 25. 候选 Cognitive Evidence Vocabulary

对应任务文件 §25。注意：不是确定 cognition，而是根据 E 组研究提出候选。**每一个必须给证据强度，E 文献不足则标 UNKNOWN，不硬凑。**

| Candidate Cognitive Evidence | Observable Support（E 组内） | Task Context Needed | Independent Validation Needed | Evidence Strength |
|---|---|---|---|---|
| EVIDENCE_SEARCH（搜索/定位关键证据） | 无直接 E 组论文研究 UI 搜索行为 | 需知道题目所需 evidence 位置 | E8 的 fNIRS 文本依赖性 + think-aloud 对齐 | **UNKNOWN**（E 组无直接证据；B 组 access demands 相关但非 E） |
| ANSWER_MONITORING（作答监控） | E7：MC.M 监控，但 trace 侧匹配率仅 4.70% | 需知道答题/检查行为的时间窗 | E7 的 think-aloud 编码 + 交叉表 | **WEAK**（E7 显示 trace 几乎无法检出 MC.M，think-aloud 可） |
| EVIDENCE_INTEGRATION（证据整合） | E7：HC.E/O 精细加工/组织，交叉表匹配 36.56% | 需知道 passage 结构 | 两路对齐 + 独立编码 | **MODERATE**（E7 的 HC.E/O 有一定 trace 可测性） |
| OPTION_EVALUATION（选项评估） | 无直接 E 组论文（E8 的干扰项构念设计相关） | 需知道选项内容与干扰项语义 | E8 式 think-aloud 对齐 + 干扰项构念 | **UNKNOWN**（E 组无直接行为证据） |
| LOCAL_COMPREHENSION_CHECK（局部理解核查） | E7：LC.F/LC.R（首读/重读），LC.R 匹配率 0%–9.66% | 需知道重读的语义 | E7 两路对齐 | **WEAK–MODERATE**（trace 能检测重读行为但无法验证其认知语义） |
| REREADING_AS_STRATEGY（策略性重读） | E7：LC.R 仅 trace 检出 38.44%（S3）、匹配 0% | 需区分策略性回读与困难驱动重复 | B 组 RBA 证据（非 E）+ E7 对齐 | **WEAK**（E 组只证明行为存在，不证明策略意图） |

**E 组文献没有为任何 UI 可观测行为提供"已验证的认知证据"标签。** 上表全部标 WEAK 或 UNKNOWN。要升级必须走 §34 的 validation pipeline。

---

## 26. 候选 Cognitive Skill / Attribute Vocabulary

对应任务文件 §26。根据阅读场景和 E8，只提出被文献支持的候选 attribute。**如果 E8 只是题型分类而非 validated latent skills，必须明确区分 Item Type ≠ Cognitive Attribute。**

### E8 的题型分类（Item Type，blueprint 层面）
literal、inference、vocabulary、summary、best evidence、key idea、author's point of view、text structure、author's purpose。

**关键：E8 没有把这些题型验证为独立的 latent skills。** 证据：Rasch 单维拟合尚可（item reliability 0.91）但 PCA 方差仅 41.2%（<60% 单维阈值），think-aloud 对齐率 20%–58%（题型间差异巨大但不等于多因子结构）。**E8 的题型是题目设计维度，不是 validated cognitive attributes。**

### E 组真正支持的 attribute 候选
- E1–E5 的 attribute 定义全部任务特异（PISA 售票机技能、数学属性、PSTRE 的 e-mail/web/spreadsheet），**无一可迁移到阅读理解**。
- 唯一接近阅读场景的是 E8 的 adolescent reading model 三成分（word recognition / language comprehension / executive processes）——但论文明确承认对大多数学生 "word recognition 不是问题"，该成分实际未被逐一测量。

### 结论
**E 组不支持我们创建一套 validated 阅读技能 taxonomy。** 项目层面的候选（literal comprehension、inference、vocabulary-in-context、main idea、text structure、author purpose、evidence use）只能作为 **item-level blueprint 分类** 或 **待验证的研究假设**，进入 CDM 前必须走 §34 管线完成"题型标签 → 独立 response-process 证据 → 技能属性"的验证。**Item Type ≠ Cognitive Attribute（CROSS-PAPER SYNTHESIS，E8 数据支持）。**

---

## 27. 专题十五：Process Evidence 如何进入 DCM？

对应任务文件 §27。综合 E2–E5，建立三条路线。

### Route A — Process as Additional Indicators / Phantom Items（E2/E3）
```
Key Action
↓
Binary Coding（出现=1/不出现=0）
↓
Phantom Item（E3: 14 个；E2: 28 个）
↓
DCM（HO-DINA/GDINA）
```

### Route B — Process as Auxiliary Continuous Variables（E4）
```
Response Time / Fixation Count
↓
Joint Model（lognormal RT / NBF 测量模型）
↓
Shared / Related Latent Variables（τ, ε 经 Σperson 与 θ 相关）
```

### Route C — Sequence-Level Characteristics（E5）
```
Action Sequence
↓
Similarity / Efficiency（LCS 摘要）
↓
Joint Model（logit 链接进四分量模型）
```

### 三者比较

| Dimension | Route A（E2/E3） | Route B（E4） | Route C（E5） |
|---|---|---|---|
| Interpretability | 高（phantom item 直接绑定属性） | 中（latent 变量经相关结构间接连接） | 中低（LCS 摘要 + 相关结构） |
| Required Labeling | 高（需定义 key action + Q-matrix） | 中（需选测量模型 + Q-matrix） | 高（需专家参考序列 + Q-matrix） |
| Q-matrix Dependency | 完全依赖（每 phantom item 一行） | 属性侧依赖，过程侧不依赖 | 属性侧依赖，过程侧不依赖 |
| Construct Assumption | key action=属性（预设） | RT/FC=速度/投入（理论模型） | 参考序列=最优（专家预设） |
| Continuous / Discrete | 离散 0/1 | 连续（RT）+ 计数（FC） | 连续（[0,1] 摘要） |
| Sequence Information Retained | 部分（n-gram 序） | 无（聚合值） | 部分（LCS 保持相对顺序） |
| Uncertainty | 无（hard 0/1） | 观测误差有、构念语义无 | 观测误差有、构念语义无 |
| Scalability | 题目特异、需逐题重定义 | 通用框架但 FC 需设备 | 需专家参考序列（2–18 条/题） |

### 项目建议
对我们系统，**Route A（phantom item）对"可枚举的确定性行为"（ANSWER_CHANGE、OPTION_ELIMINATE、UNDERLINE_CREATE）最合适，Route B（joint modeling）对连续/计数指标（RT、scroll count、selection count）最合适，Route C（LCS）需要参考序列而阅读无天然"最优路径"，最不直接适用。** 但三者共享同一前提：**进入 CDM 前 mapping 必须经过独立验证（§34）**（CROSS-PAPER SYNTHESIS）。

---

## 28. 专题十六：Key Action Coding vs Sequence Modeling

对应任务文件 §28。重点比较 E2/E3 与 E5。

### Key-action coding（E2/E3）
**优点**：interpretable（phantom item 直接绑定技能/迷思概念属性）；directly tied to skills（Q-matrix 明确）；compatible with DCM（GDINA/DINA 直接可用）。
**潜在缺点**（论文验证）：loses ordering（n-gram 只保留局部序，CANCEL 重启轮被压缩）；researcher-defined key actions（mapping 是作者预设）；Q-matrix dependency（题目特异、无独立验证）；circularity（§21）；**n-gram 重叠导致 phantom items 局部依赖**（E2 的 28 题互相嵌套）。

### Sequence-level modeling（E5）
**可能保留**：order（LCS 保持相对顺序）、efficiency（长度比）、similarity（参考序列距离）。
**但**：less interpretable（LCS 摘要的认知意义需要事后解释）；参考序列成本高（2–18 条/题）；**实证显示相似性与能力近乎冗余（0.990）、效率与能力负相关（−0.543），其"语义"未经验证**。

### 论文验证的判断
**两种方法都有 E 组实证，但没有 head-to-head 比较**（E5 讨论中与动作计数方法对比，未与 E2/E3 的 key action 方法对比）。E3 的 GDINA + phantom items 与 E5 的四分量模型在各自数据集上都"有效"，但：
- 如果目标是有诊断反馈的解释（"该生缺技能 X / 有迷思概念 Y"）→ key-action coding 更直接（E2 的 74 种模式）。
- 如果目标是提高分类精度的辅助信息 → sequence-level 贡献（E5 四分量 ACA 0.863 vs 0.84）。
**不能只靠 E 组决定二选一**；对我们项目，答案可能是分层：确定性语义事件用 key-action 编码，连续流（scroll/pointer）用 joint modeling，sequence 特征作为探索性补充（CROSS-PAPER SYNTHESIS）。

---

## 29. Validity Evidence Matrix

对应任务文件 §29。

| Cognitive Claim | Observable Indicator | E2/E3 Evidence | E4/E5 Evidence | E6 Validity Requirement | E7 Triangulation | E8 Reading Evidence | Final Strength |
|---|---|---|---|---|---|---|---|
| Key action indicates skill mastery | phantom item 0/1 | 分类信度 .99、拟合好（E2/E3） | N/A | 要求独立验证（未满足） | N/A | N/A | **WEAK**（预测/测量效用强，构念效度缺失 + 循环风险） |
| Failure to perform key action = lack of mastery | phantom item = 0 | 高 guess 参数案例（E3 buy gi=.442）说明"出现≠掌握"；未排除替代解释 | N/A | 要求排除替代解释 | N/A | N/A | **WEAK–UNSUPPORTED** |
| Systematic wrong action = misconception | 错误状态转移 | E2 编码假设，无独立验证；未区分偶然 vs 系统 | N/A | 要求稳定性证据 | N/A | 干扰项"常见错误"构念（非正式） | **UNSUPPORTED** |
| Fixation count contains cognitive diagnostic info | FC 计数 | N/A | 分类增量 <1%–5.49%（E4）；ε 恢复好 | 要求 context 限定 | N/A | N/A | **MODERATE（作为测量信号）/ UNSUPPORTED（作为认知语义）** |
| Trace reliably identifies cognitive process | action→process 映射 | N/A | N/A | 要求验证 | 17.18% 匹配、45% 互补（E7） | N/A | **WEAK–MODERATE**（能测行为，不能单独确认认知） |
| Think-aloud reflects intended reading process | verbal 对齐 | N/A | N/A | 支持 | 两路同等有效（E7） | 对齐率 41%、题型间 20–58%（E8） | **MODERATE**（有证据但编码无 IR、样本小） |
| Process data improves cognitive diagnosis | 各类 | SE 更小（E3） | 分类增益（E4/E5） | N/A | N/A | N/A | **STRONG（作为诊断效用）** |
| Better classification = better construct validity | 各类 | 循环风险（E2/E3） | 自证性模拟（E4/E5） | 明确否定 | N/A | N/A | **UNSUPPORTED（被 E 组证据否定）** |

---

## 30. Evidence Ladder

对应任务文件 §30。把认知推断分成 A–E 五级，并放入我们项目的例子。

```
A. Direct Observable（事实）
B. Behavioral Inference（行为描述）
C. Process Interpretation（候选认知，hypothesis）
D. Validated Cognitive Evidence（独立验证）
E. Diagnostic Attribute（进入 CDM）
```

### 我们项目中的例子
| 例子 | 最低级别 | 能否上升 | 需要的证据 |
|---|---|---|---|
| answer changed B→C | A（Direct Observable） | → B（changed selected option）确定；→ C（monitoring/uncertainty）是 hypothesis；→ D（validated monitoring）需独立证据 | E7 式两路对齐 + E8 式 think-aloud 对齐 + 专家编码 |
| returned to passage P2 | A→B（returned to passage） | → C（evidence search）需知道 Q 的 evidence 位置（§24 item-specific）；→ D 需验证 | item context + 独立 verbal/眼动 |
| marked sentence | A→B（underlined sentence） | → C（integration/emphasis）是 hypothesis；→ D **E 组无直接支持** | B 组 underline 无证据（§40）+ 需自行验证 |
| scroll burst before answer | A→B（scrolled rapidly） | → C（rereading/search）多候选、无法消歧（E7 S5） | 需多通道 + 时间对齐 |
| eliminated option D | A→B（eliminated option） | → C（option evaluation）是 hypothesis；→ D 无 E 组证据 | E8 式干扰项构念 + think-aloud |
| high dwell on passage | A（dwell） | B 组已证 dwell ≠ difficulty（前提）；→ C 是 hypothesis | B 组 + E 组均未解决 |
| pointer inactive | A（pointer idle） | → C（reading/思考）多候选；C 组已证 pointer ≠ reading | C 组边界 + E 组无证据 |

**规则**：A/B 是确定的；C 必须标 hypothesis；D 必须走 §34 管线；E 只能放通过 D 的属性。**禁止为了"完整认知画像"把 A 直接跳到 E（§45）。**

---

## 31. Twenty Cross-Paper Research Questions

对应任务文件 §31。逐条回答。

### Q1. Process data 加入 CDM 后，最稳定的收益是什么？
**补充响应信息，改善高阶能力 θ 的估计与属性分类，且收益在"响应信息不足"时最大**：E1 转述（Q-matrix 不可识别/题短/guess-slip 高时 RT 增益明显）；E4 的 θ RMSE 从 .698 降到 .507；E5 的 ACA 0.84→0.863；E3 的 SE 更小（t(3759)=−115.58）。**最稳定收益是"测量效用的提升"，不是认知语义的确立。**

### Q2. 这些收益能否证明 process indicator 具有正确 cognitive meaning？
**不能。** E1–E5 没有一篇附带独立 construct validity 验证；E4 自己限定 FC 语义；E5 的 efficiency 与能力负相关；E2/E3 的 mapping 是预设。**Predictive/measurement utility ≠ construct validity（§13、§18）。**

### Q3. E2/E3 中的 key action 是如何定义和验证的？
定义：从任务状态图转写 + 出现率筛选（5%–95%）+ 理论相关性筛选 + 可识别性约束（§11 Q1）。验证：**只有模型内部拟合与分类信度，无独立 response-process 验证（§10.14 E2/E3）。**

### Q4. Key action → attribute mapping 是否存在 circularity？
**是。** E2/E3 的 Q-matrix 是模型输入、与作答编码同源，模型表现好不验证映射正确（§21）。

### Q5. Phantom-item expansion 会不会人为增加 evidence amount？以及 local dependence？
**存在显著 local-dependence risk。** E2 的 1 题→28 题、E3 的 1 题→14 题全部来自同一原始任务，n-gram 互相嵌套（呈现 ABCD 则同时呈现其子序列），构成结构性共现；但 **marginal dependence ≠ conditional dependence given attributes**——E3 假设 conditional independence 且主张以 item-level fit 检验，E2 完全没有处理该问题（§10.10 E2/E3）。信度微升（.9852→.9899）与题目冗余相关。

### Q6. 如何区分 skill non-mastery 和 misconception？
**E2 没有真正区分。** 它把迷思概念编码为附加属性（错误选项→m1–m4），但没有区分"稳定执行错误规则"与"未执行关键步骤"，无错误一致性证据（§12）。

### Q7. E2 对 misconception 的证据到底有多强？
**很弱。** "错误行动→迷思概念"是编码假设；无 think-aloud/眼动/访谈/外部标准/专家评审；区分效度未检验（a1−m1、a2−m2、a3−m3 高负相关）；个案是事后改标签（§10.11、§10.23 E2）。

### Q8. E4 中 fixation count 的 cognitive meaning 到底是什么？
**visual engagement ε = "FC 所背书的视觉认知过程负荷量"**，论文自己限定不是完整视觉注意、context-dependent；FC 不加载在属性上（§10.5 E4）。

### Q9. E4 是否证明 eye-tracking indicator 具有 construct validity，还是只证明 diagnostic utility？
**只证明 diagnostic utility。** FC 增益经 Σperson 相关结构传导；分类增量多数 <1%；无外部效标、无 think-aloud、无判别证据（§10.14 E4）。

### Q10. E5 的 sequence similarity / efficiency 到底如何定义？
Similarity = |LCS(obs, ref)| / |ref|；Efficiency = |LCS(obs, ref)| / |obs|；ref 由内容专家定义，多参考序列取最长 LCS（§10.4 E5）。

### Q11. 它们是否真正对应某个 cognitive construct？
**没有验证。** 相似性−能力 0.990 与效率−能力 −0.543 只能说明极强的经验重叠 / 负相关；"相似性近冗余"与"效率=策略"的解读是 CROSS-PAPER / ANALYTICAL INFERENCE（§10.5 E5）；论文定位为 predictive indicators + 事后弱解释。

### Q12. Trace 与 think-aloud 一致程度有多高？
**仅 17.18% 时间段匹配（S4）**；45% 互补（S2+S3）；27.17% 分歧（S5）（§10.13 E7）。过程级：LC.F 75.01% 匹配、MC.P 4.45%、MC.E 0%。

### Q13. Trace 和 think-aloud 不一致意味着什么？
**多种可能**：未语言化行为、无行为对应的陈述、同一过程但说话时间短、方法缺陷、测量精度限制、未定义的新过程、真同时多过程（§10.17 E7）。**不是简单的一方出错。**

### Q14. Think-aloud 能不能当 cognitive ground truth？
**不能。** E7 明确两路 "equally valid"、无 one truth；E8 中 think-aloud 是五类证据之一（但 Q6 决策中实际充当仲裁者）；E6 区分 process data 与 response processes（§15、§33）。

### Q15. Reading comprehension 的 response-process validity 应该如何验证？
**E8 示范**：同步 think-aloud 演绎编码（对齐预期构念）+ fNIRS 文本依赖性 + Rasch 内部结构 + 多来源迭代互证；用 response-process 证据发现并修订构念问题（Q6）（§16）。

### Q16. Predictive validity / diagnostic accuracy 与 construct validity 有什么区别？
Predictive = 特征提高分类/预测（E4/E5 全部）；Construct = 特征测量预期认知（E 组只有 E6/E7/E8 提供证据，且证明的是"不能轻易当认知"）。**前者不蕴含后者（§18）。**

### Q17. 在我们的系统中，ANSWER_CHANGE / REVISIT / UNDERLINE / OPTION_ELIMINATION / POINTER_ACTIVITY 哪些最多停在 behavioral evidence？
**全部最多停在 behavioral evidence**（D 组词汇的 Atomic Semantic Events 层）：ANSWER_CHANGE（B→C）→ 行为确定，→ monitoring 是 hypothesis；REVISIT → 行为确定，→ evidence search 需 item context；UNDERLINE → 行为确定，→ integration 无 E 组支持；OPTION_ELIMINATION → 行为确定，→ option evaluation 无 E 组支持；POINTER_ACTIVITY → 行为确定，→ reading 被 C 组否定为直接证据。**进入 cognitive evidence 必须走 §34 验证。**

### Q18. 我们未来是否必须收集 explicit verbal data？
**需要，但定位应是 validation / labeling data only，不是 normal production input。** 依据：E7 证明 trace 单独漏掉 ~45% 互补信息、27% 分歧无法消歧；E8 证明没有 response-process 证据会发现不了构念问题（Q6）；E6 要求"像产品数据一样验证"。**如果系统要求每次作答都解释理由/持续出声，会改变自然行为（§32、§34）**。这属于 **PROJECT DESIGN IMPLICATION**（E7/E8 没有直接回答"normal input vs validation"，但证据指向 validation）。

### Q19. 行为→cognitive interpretation 的 uncertainty 应该怎样被表达？文献有没有直接模型？
**E 组没有直接模型。** E1–E5 用 hard 指标或测量模型（观测误差），无构念不确定性；E7 的 S5（多候选不消歧）是唯一接近的表达，但无概率化（§22）。**这是我们自己的设计空间**（如 CognitiveEvidence 带 confidence 字段，§35）。

### Q20. 截至 A–E 全部文献：传统方法对自然英语阅读过程认知建模的能力上限在哪里？
**上限 = 能够从行为 trace 中恢复行为证据（A–D 已建立），能够在统计层面用 DCM/joint model 把（已验证的）过程指标映射到 latent attribute（E1–E5 提供工具），但"行为 → 认知过程"的解释只能以 hypothesis 形式存在，无法仅凭 UI 行为 trace 达到"已验证认知证据"级别**——除非引入独立 verbal/专家/任务设计的 response-process 证据（E6/E7/E8 提供方法）。**单个 UI 行为的认知语义普遍是 UNKNOWN 或多候选 + 置信度（§43、§45）。**

---

## 32. Role of Explicit Reports

对应任务文件 §32。我们的系统不希望要求学生每次解释理由/持续 think aloud/持续报告 confidence（会改变自然行为）。

### Explicit Report 最适合什么？
**Validation / Ground Truth / Labeling，而非 Normal inference input。** 证据：
- **E7**：两路数据互补（45%）、可互换仅 17.18%，且 think-aloud 有反应性——说明 verbal 报告的价值在于"提供 trace 看不到的补充过程"，适合作为**校准/验证通道**而非日常输入。
- **E8**：think-aloud（n=5 小样本）用于**发现构念问题**（Q6 重写），不是用于评分——验证用途。
- **E6**：要求预注册、by-design——验证流程的一部分。

### PROJECT DESIGN IMPLICATION
- **正常系统**：只收集自然 UI 行为 trace（不打扰学生）。
- **验证/校准子研究**：对小样本学生采集 stimulated retrospective report / 有条件的 think-aloud / 专家编码，用 E7 的 S1–S5 对齐 + 交叉表方法，验证"行为 → 认知"映射，产生 calibration 数据。
- **映射验证后**：已验证的映射才进入生产诊断（§34）。
- **明确警告**：E7/E8 没有直接回答 "normal input vs validation" 的分工问题——这属于 **PROJECT DESIGN IMPLICATION**，由我们根据证据推导（任务文件 §32 允许结合证据给 PROJECT DESIGN IMPLICATION）。

---

## 33. Cognitive Ground Truth（No single evidence source in Group E qualifies as standalone cognitive ground truth）

对应任务文件 §33。

# What Can Be Ground Truth for Cognition?

| 候选 | 分析（基于 E6/E7/E8） | 能否算 ground truth |
|---|---|---|
| Task correctness | 可判定、客观（A 组依赖） | **能作 outcome 的 ground truth，不能作 cognition 的 ground truth**（E3 证明同分可有不同模式；E8 证明正确作答不保证真正阅读了文本） |
| Expert judgment | 领域理论（E2/E3/E5 的 Q-matrix、参考序列） | **是权威输入，但无独立验证时是预设而非 truth**（PVAF 被否决：E3） |
| Think-aloud | 可言语化过程（E7/E8） | **不能**（E7 明确两路 equally valid、无 one truth；E8 中仅五类证据之一） |
| Retrospective verbal report | E 组未使用 | **E 组无证据，不能自动继承 think-aloud 的效度**（§20） |
| Eye tracking / fNIRS | 注意/文本依赖代理（E4/E8） | **不能**（fixation ≠ 认知，C 组 + E4 限定；fNIRS 是 supplementary physiological / neurophysiological evidence，consistent with text engagement/dependence，不是"正在阅读文本"的直接证明） |
| Behavior trace | 显性行为（E7） | **不能单独**（17.18% 可互换；S5 无法消歧） |
| Q-matrix | 专家输入（E2/E3/E5） | **不能**（是模型输入，循环风险） |
| Latent model output | 模型估计（E2–E5） | **绝对不能**（model output ≠ ground truth；模拟中自证） |

### 结论
**收窄表述：E 组能 STRONG 支持的是 "No single evidence source in Group E qualifies as standalone cognitive ground truth"**——E 组考察的证据源（trace、think-aloud、eye/fNIRS、expert mapping、Q-matrix、latent-model output）没有一个可单独当作 cognitive ground truth（E7 的 "neither...fully 'truth'"、E6 的 process data ≠ response processes、E8 的多来源互证）。**但不能推出"世界上不存在任何 cognitive ground truth"的无限泛化哲学命题。** 更合理的是 **triangulated validation evidence**：E8 的 Rasch + think-aloud + fNIRS 三方互证、E7 的两路对齐 + 过程图。**但 triangulation 也不是"找到唯一真值"，而是"用独立来源约束解释空间"（§19）。**

## 34. Construct Validation Pipeline

对应任务文件 §34。根据 E 组研究，提出一个**文献约束下的候选 validation pipeline**（只到方法论层，不设计完整生产系统）。

```
Step 1  Define cognitive construct from reading theory / item design
        （E8 的 adolescent reading model / 题型 blueprint；E6 要求 by-design 预注册）
Step 2  Define candidate observable process indicators
        （E1–E5 的 RT/action/sequence 框架；E6 的指标定义）
Step 3  Collect natural trace data
        （我们的 UI 行为日志；E7 的 trace parser 思路）
Step 4  Collect independent response-process evidence
        （think-aloud / retrospective report / expert coding）
        （E7 的 think-aloud 协议 + 编码方案；E8 的演绎编码；§20 对 retrospective 的 PROJECT HYPOTHESIS）
Step 5  Temporal alignment
        （E7 的细粒度段对齐 + S1–S5；回溯式则改为回放锚点对齐，PROJECT TRANSFER INFERENCE）
Step 6  Test convergence / disagreement
        （E7 的交叉表 + 中位数/IQR + FOMM 过程图比较；E8 的多来源互证）
Step 7  Revise mapping
        （E8 的 Q6 案例：response-process 证据推翻/修订构念）
Step 8  Only validated mappings enter CDM
        （E2–E5 的 DCM 工具，但仅对通过 Step 4–7 的映射使用）
```

**标注**：Step 1–8 的整体编排是我们对 E6/E7/E8 的综合 → **CROSS-PAPER SYNTHESIS**。其中 Step 4 的 retrospective report 形式无 E 组直接证据 → **PROJECT HYPOTHESIS**；Step 5 的回放锚点对齐 → **PROJECT TRANSFER INFERENCE**。Step 8 的"只让已验证映射进入 CDM"是 E 组最关键的纪律：**E1–E5 提供了 CDM 工具，E6–E8 提供了验证方法，两者必须串联，不能直接用未验证映射跑 DCM（§43）。**

---

## 35. Cognitive Evidence Confidence

对应任务文件 §35。只研究理论依据，不设计数据库 schema。

### E 组是否支持"cognitive evidence 应带 confidence / evidence provenance"？
**间接支持，且明确要求。**
- **E6**：要求预注册、by-design、理论 + 验证共同支撑——即证据必须带"来源说明"（theory / experiment / validation）。
- **E7**：S5 分歧中两个候选过程都被赋给同一段（多候选不消歧），而"哪个更可能"没有给出——**这正是一个 confidence 缺口**；E7 也承认"不匹配"可能源于测量精度（时间重叠），即同样的 trace 行为在不同情况下解释可信度不同。
- **E8**：五类效度证据的强度不同（content 是专家评审、response process 是 think-aloud 对齐、internal structure 是 Rasch），**不同来源的证据类型不同，需要 provenance**。
- **E1–E5**：全部使用点估计（latent 后验均值、0/1 分类），**没有在属性诊断层输出置信度**——这是模型层的缺口。

### 理论依据
E 组支持如下设计方向（CROSS-PAPER SYNTHESIS）：
```
CognitiveEvidence {
    type                // 候选过程类型（如 EVIDENCE_SEARCH）
    source_action       // 原始行为证据（如 SCROLL_TO_P2）
    item_context        // 题目上下文（Q3 的 evidence 在 P2）
    confidence          // 该解释的可信度（E7 S5 提示多候选，需概率/分级）
    evidence_sources    // provenance：trace / think-aloud / expert / task design
}
```
**支持理由**：E6 要求"理论 + 经验/实验验证"共同支撑（对应 evidence_sources）；E7 证明同一行为段可有多个候选（对应 confidence 的必要性）；E8 证明不同证据源强度不同（对应 provenance）。**但 E 组没有一篇实现这样的结构——它是我们基于文献约束的设计方向（§45 保留 UNKNOWN 的载体）。**

---

## 36. Evidence Independence

对应任务文件 §36。

### E2/E3/E4 的关联
- **共享作者**：E2（詹沛达）、E3（Zhan & Qiao）、E4（Zhan, Man, Wind & Malone）都含第一作者 **Peida Zhan**；E1（Jiao, Liao & Zhan）也是同一谱系。E2 明确自述是 E3（Zhan & Qiao 2022）的拓广（PDFPAGE 3）。
- **共享方法体系**：三者都在 joint-hierarchical DCM / item expansion 的同一框架内（E1 的 RT-DINA 来自 Zhan et al. 2018；E4 的 MJ-DINA 是其多模态扩展；E3 的 phantom item 是 E2 的基础）。
- **共享数据/模拟设计**：**E2 与 E3 高度共享方法学谱系，都使用 PISA 2012 TICKETS 环境，但并非同一道题、也非同一分析数据集**：E2 用 TICKETS CP038Q02（买 2 张全价乡村火车单程票，N=3547，28 个 phantom items，自身不含迷思概念的 baseline 为 10 个），E3 用 TICKETS Task 2、CP038Q01（坐 4 次地铁的最便宜方案，N=3760，14 个 phantom items）。二者属 "methodologically dependent but empirically distinct applications"；E2/E3 是否有部分学生重叠仅凭这两篇 PDF 无法确定，不猜测。E4 的实证数据（数学题、Man & Harring 2019 数据集）独立于 E2/E3，但其 Q-matrix 沿用了 Man & Harring 的数据集。
- **E5**：作者 Rajeb, Ma, He & Shi——He 是 E3 引用的外部源（He, Borgonovi & Paccagnella 2019 是 similarity/efficiency 度量的提出者），但 E5 作者体系与 Zhan 谱系**不重叠**，方法（四分量 joint model）也独立。
- **E6/E7/E8**：作者与 Zhan 谱系无关；E7（Fan & Gašević 等）与 E8（Severino 等）是独立实证。

### 结论
**禁止把 E2/E3/E4 当成 3 次独立 replication。** E2 与 E3 高度共享作者与方法学谱系、并都使用 PISA 2012 TICKETS 环境，因此不能视为完全独立的方法复制；但二者并非同一道题、也非同一分析数据集，属于 "methodologically dependent but empirically distinct applications"（其"一致性"部分是方法学设计内建的，不是同一数据上的重复）。E4 与 E3 的关联是方法学谱系而非数据。**E 组真正独立的证据来自 E6/E7/E8（作者独立、方法独立、领域独立）**。在最终结论中，E2/E3/E4 的发现必须作为"同一研究谱系的一组证据"加权，而非独立复现。

---

## 37. Simulation ≠ Construct Validation

对应任务文件 §37。强制检查项。

### E 组中 simulation 的分布
- **E1**：无自身模拟，转述 Minchen & de la Torre (2016) 与 Zhan et al. (2018) 的模拟结论。
- **E3**：**真实数据（PISA 2012）**，非模拟。
- **E4**：Simulation 1/2 为主体，外加 N=93 实证。
- **E5**：Simulation 1/2 为主体，外加 N=935 实证。
- **E2**：真实数据，无模拟。

### Simulation 能证明 vs 不能证明
Simulation 可以证明：**if model assumptions are true → parameter recovery is good**（E4 的 θ/τ/ε RMSE、E5 的 ACA/PCA）。
Simulation 不能证明：**real human cognition actually follows those assumptions**。

**关键检查**：E4/E5 的 simulation 全部是"用目标模型生成数据 → 用同一模型拟合"，这只能证明参数可恢复，不能证明真实认知遵循模型假设。且 E4 的 joint 增益由预设 person 参数相关驱动（Φ 越高增益越大）、E5 的增益随人参数相关增强——**这些增益是"假设的统计结构"的复现，不是"真实认知"的证据**。

**结论**：
```
Simulation evidence → model recovery evidence
NOT → construct validity evidence
```

---

## 38. Model Fit ≠ Psychological Truth

对应任务文件 §38。

### E 组中的 model fit 证据
- **E3**：RMSEA2=0.032、SRMSR=0.033、AIC/BIC/LRT 选 HO-DINA——拟合好。
- **E2**：GDINA SRMSR=0.0756——拟合好。
- **E4**：PPMC ppp≈0.5——拟合好。
- **E5**：PPP、DIC、R̂<1.05——拟合好。

### 关键判断
模型拟合好只能说明：**model fits observed data better under specified assumptions。** 不能推出：**latent attribute has true psychological meaning。** E2/E3 的拟合好不能证明"key action=技能/迷思概念"映射正确（mapping 是输入）；E5 的 DIC 好不能证明"参考序列=最优策略"。**模型拟合是必要但不充分条件。**

### 特别注意
- E5 的经验 DIC 显示"三分量含效率"（8,886.51）比二分量（8,559.29）**更差**——拟合更好的模型不一定更有心理意义，反之拟合差的"效率分量"只是不增加预测信息，不代表"效率不反映认知"。
- E8 的 Rasch 拟合良好（item reliability 0.91）却存在 Q6 的构念问题——**最好的反例：心理测量拟合好 ≠ 题目测量了预期构念**。

---

## 39. Correlation ≠ Cognitive Identity

对应任务文件 §39。

### E 组中的 correlation 证据
- **E3**：corr(θ1, θ2)=0.826——过程数据能力与 outcome 能力高度相关。这只能说"相关"，不能说"相同"。
- **E4**：r_τε=−0.959——速度与视觉投入强负相关，论文自己提醒"height and weight are highly correlated but reflect separate traits"（PDFPAGE 28）。
- **E5**：能力−相似性 0.990、能力−效率 −0.543——**0.990 恰好是"相关 ≠ 同一"的反面教材**：它提示相似性与能力可能是近冗余 / 代理关系（CROSS-PAPER / ANALYTICAL INFERENCE），而非独立构念。

### 结论
如果 process indicator 与 accuracy/ability/score 相关，只能说 **associated with**，不能写 **represents**，除非有额外 validity evidence。E 组内部的证据反而示范了"高相关 = 可疑的冗余或代理"，而不是"构念同一"。

---

## 40. Reading Process Mapping

对应任务文件 §40。针对我们的英语阅读任务。

| Observable Action | Possible Process Interpretation | Required Context | Alternative Explanation | Validation Needed |
|---|---|---|---|---|
| SCROLL_BURST | 快速浏览/搜索段落（candidate） | 题目当前状态、evidence 位置 | 鼠标滑过、界面惯性滚动、分心 | E8 式 think-aloud/fNIRS 对齐（UNKNOWN） |
| BACKWARD_SCROLL / REVISIT | 回读/验证证据（candidate） | Q 的 evidence 是否在被回看的段落（§24） | 找不到信息、困惑、重读失败（B 组） | item-specific + 独立 verbal |
| QUESTION_NAVIGATE | 切换题目/任务目标转移（candidate） | 是否已回答当前题、是否跳题 | 随意浏览、跳过难题 | 需任务上下文（E6 不能跨题推广） |
| ANSWER_CHANGE | 监控/修正/不确定性（candidate） | 改答案前后的事件（§30） | 误点纠正、测试界面问题 | E7 式两路对齐（B 组已证 ≠ uncertainty） |
| OPTION_ELIMINATE | 选项评估/排除（candidate） | 被划选项的语义（E8 干扰项构念） | 随机操作、对选项不熟 | E8 式干扰项设计 + think-aloud（E 组无直接证据） |
| UNDERLINE | 强调/标记证据（candidate） | 划线内容与题目相关性 | 习惯性操作、视觉辅助 | **B 组 underline 无证据 + E 组无证据 → UNKNOWN** |
| TEXT_SELECTION | 复制/精读/标记（candidate） | 选中内容 | 复制粘贴、误选 | 无 E 组证据 → UNKNOWN |
| PASSAGE↔QUESTION SWITCH | 证据检索/答题-原文对照（candidate） | 切换频率、方向、停留 | 来回核对、迷失 | item-specific + 时间对齐（E6 分段） |
| POINTER_INACTIVE | 阅读/思考（candidate） | 指针停留位置、其他事件 | 发呆、离开、读屏幕外（C 组 pointer ≠ reading） | C 组边界 + 多通道（E7 眼动） |

**纪律**：以上全部是 possible / candidate / hypothesis，除非 E 组有直接支持（E 组基本没有针对这些 UI 行为的直接支持——E2/E3/E5 的 key action / sequence 是任务特定的售票机/搜索任务，E7 的动作库是 TEL 写作环境，E8 无 UI 行为数据）。**进入诊断前必须走 §34 验证。**

---

## 41. Evidence Strength Matrix

对应任务文件 §41。四类证据强度。

### STRONG（直接实证 + 独立验证 + 恰当领域）
- "过程数据在特定条件下可提供增量诊断信息（response-only 信息不足、且过程变量与目标 latent trait 共享充分信息时）"（E1 转述 + E3/E4/E5 模拟/实证，跨论文一致；条件化表述见 §42）。
- "E7：trace 与 think-aloud 只有 17.18% 时段匹配（占学习会话时长的中位比例）、45% 互补、27.17% 分歧"（直接实证，E7）。
- "E6：过程数据指标必须像产品数据一样验证"（框架性，E6 + E7/E8 佐证）。
- "E 组无单一证据源可单独充当 cognitive ground truth（trace、think-aloud、eye/fNIRS、expert mapping、Q-matrix、latent-model output 均不可单独作为 ground truth）"（E7 "equally valid" + E6 process data ≠ response processes + E8 多来源互证，§33）。

### MODERATE（机制 + 部分实证，但 domain transfer 或独立验证有限）
- "题型标签不能保证诱发预期过程（Item-type labels do not guarantee that students engage in the intended response processes）"（E8 对齐率 20%–58%、PCA 41.2%，但 think-aloud n=5、单人编码、无 IR；不构成对"哪个题型 = 哪个 latent skill"的强证明）。
- "think-aloud 反映预期阅读过程"（E8 对齐率 41%，但编码无 IR、n=5）。
- "E4：joint-hierarchical CDM 框架是通用方法学"（方法学可迁移，但实证仅 N=93 数学）。
- "E5：sequence similarity/efficiency 提高分类精度"（模拟 + N=935，但认知语义未验证、循环风险）。

### WEAK（主要是 theory / association / model assumption）
- "key action 反映 skill mastery"（E2/E3 分类信度好但 mapping 是预设，循环风险）。
- "fixation count 含认知诊断信息"（E4 模拟增益，但语义被限定、无独立验证）。
- "E7：两路各自检测到互补过程"（有证据但任务绑定）。

### UNSUPPORTED / OPEN（目前没有足够证据）
- "错误 action = 迷思概念"（E2 编码假设，无独立验证）。
- "未执行 key action = 非掌握"（E3 未排除替代解释）。
- "fixation count = 认知技能测量"（E4 明确否定）。
- "sequence efficiency = 策略能力"（E5 实证与预期相反）。
- "think-aloud 是 cognitive ground truth"（E7 明确否定）。
- "trace 与 think-aloud 可互换"（E7 明确否定）。
- "Q-matrix 验证了 action→skill mapping"（E3 PVAF 被否决、E2 无验证）。
- "latent model fit 验证了心理解释"（E8 的 Q6 反例）。
- "行为 → 认知过程能确定性映射"（E7 S5、E6 构念无关方差）。

---

## 42. What Group E Establishes

对应任务文件 §42。逐条判断以下命题。

### Strong Evidence
1. **Process data can provide incremental diagnostic information under some conditions（尤其当 response-only 信息不足、且过程变量与目标 latent trait 共享充分信息时）** —— **STRONG / MODERATE-STRONG（条件化）**。E1 转述 + E3（SE 更小 t(3759)=−115.58）+ E4（θ RMSE .698→.507，但 FC 增量多数条件 <1%）+ E5（ACA 0.84→0.863，但低相关时无优势）。**配套命题 "Adding process data generally / always improves cognitive diagnosis" —— UNSUPPORTED**（E4 多数条件相对增量 <1%、E5 低相关条件下四分量无优势甚至略低于 baseline、E1 理想测验下 RT 无增益）。
2. **Trace 与 think-aloud 的匹配率低（17.18%，占学习会话时长的中位比例）、互补率高（45%）** —— STRONG。E7 直接实证。
3. **No single evidence source in Group E qualifies as standalone cognitive ground truth** —— STRONG。E7 "equally valid"、E6 process data ≠ response processes、E8 多来源互证。**收窄表述**：这是"E 组考察的证据源（trace、think-aloud、eye/fNIRS、expert mapping、Q-matrix、latent-model output）没有单独一个可当作 cognitive ground truth"，不是"世界上不存在任何 cognitive ground truth"的哲学命题（§33）。

### Moderate Evidence
4. **Think-aloud 反映预期阅读过程（在合理对齐率内）** —— MODERATE。E8 41%，但编码无 IR、n=5。
5. **Item-type labels do not guarantee that students engage in the intended response processes（题型标签不能保证诱发预期过程）** —— MODERATE。E8 对齐率 20–58%、PCA 41.2%，但 think-aloud n=5、单人编码、无 IR；"题型标签 ≠ 认知技能"可继续作为我们的概念边界，但不是 E8 的强实证证明。
6. **Joint-hierarchical CDM / item expansion 是通用方法学** —— MODERATE。E1–E5 方法成熟，但迁移到阅读需重定义。
7. **过程数据价值随"响应信息不足"增大** —— MODERATE。E1 转述 + E4（Q-matrix incomplete 时增益最大）+ E5（高相关时增益）。

### Weak Evidence
8. **Better classification = better construct validity** —— **UNSUPPORTED（被 E 组证据否定）**。E4 自己限定、E5 负相关、E2/E3 循环。
9. **Key action = skill mastery** —— WEAK。E2/E3 分类信度好但 mapping 预设、循环风险。
10. **Failure to perform key action = lack of mastery** —— WEAK–UNSUPPORTED。E3 未排除替代解释。
11. **Systematic wrong action = misconception** —— UNSUPPORTED。E2 编码假设。
12. **Fixation count measures cognitive skill** —— **UNSUPPORTED（E4 明确否定）**。
13. **Response time measures difficulty** —— WEAK。E1 列出多种替代解释（速度化、动机、作弊）；RT 与 difficulty 相关但不等于。
14. **Trace data reveals cognition** —— WEAK–MODERATE。E7 证明能测行为、17.18% 匹配、45% 互补。
15. **Think-aloud is cognitive ground truth** —— **UNSUPPORTED（E7 明确否定）**。
16. **Trace and think-aloud are interchangeable** —— **UNSUPPORTED（E7 明确否定）**。
17. **Q-matrix validates action→skill mapping** —— **UNSUPPORTED（E3 PVAF 被否决、E2 无验证）**。
18. **Latent model fit validates psychological interpretation** —— **UNSUPPORTED（E8 的 Q6 反例）**。

### Unsupported / Still Open
见 §41 UNSUPPORTED 列表 + §45 UNKNOWN。

---

### E 组正式结论（反馈整合，7 条）

按本报告头部已保存的历史修订记录（谱系限制见 `../../provenance/LEGACY_REPORT_PROVENANCE.md`），E 组只保留以下 7 条正式结论：

1. **诊断效用和构念效度是两个问题**：Process data improves estimation ≠ Process data has valid cognitive meaning。这是整个 E 组最强的结论（§13、§29、§42-1）。
2. **Process data 可以提供增量诊断信息，但收益高度条件化**：取决于 response-only information、Q-matrix quality、test length、process–ability correlation、process measurement quality（§42-1 拆分）。
3. **Key Action → Attribute 是最危险的 inference gap**：E2/E3 提供好用的 Key Action → Phantom Item → DCM 技术框架，但真正缺的是"Key Action 为什么代表 Skill X"的独立验证（§11、§21）。
4. **Q-matrix 是 measurement assumption，不是 validity proof**（§11 Q5、§21、§42-17）。
5. **Trace 和 verbal evidence 互补，但均不能单独当 cognition truth**（§15、§33、E7）。
6. **Reading assessment 必须验证 actual response process**：E8 最大价值不是 20%/58% 那几个数字，而是完整逻辑——Intended Construct → Item → Student actually solves it → Response-process evidence → 发现不一致 → 反过来修改 item/construct（§16、E8 Q6 案例）。
7. **最终缺口是 Construct-validated Behavior → Cognition Mapping**：A–E 全部结束后，Raw Events → Actions → Contextualized Process Evidence 之后的缺口不是"更复杂的 HMM、CDM 或 sequence model"，而是"construct-validated Behavior → Cognition mapping"（§44、§43）。

---

## 43. What Group E Adds to the System

对应任务文件 §43。不要只说"我们可以使用 CDM"。

### Before E
```
Behavior → Cognition
存在一个巨大 inference gap
```

### After E，我们明确获得

**哪些 mapping 可以用（经过 E 组验证或 E 组直接支持）**：
1. 过程数据能作为 CDM 的**辅助信息**提高诊断效用（E1–E5）——但只在信息不足时收益明显，且只支持测量效用、不支持认知语义。
2. E7 的对齐-比较框架（S1–S5、交叉表、FOMM）可迁移到我们的 trace ↔ verbal 验证（§20、§10.22 E7）。
3. E8 的五类效度证据组织框架 + "用 response-process 证据修订构念"的方法可迁移到我们的 passage/题项验证（§16）。
4. E6 的三大挑战清单（理论验证、设计、伦理）作为指标开发的检查清单（§10.22 E6）。

**哪些 mapping 只能是假设**：
1. 任何 UI 行为 → 认知过程的单跳映射（E7 S5 多候选无法消歧；E6 构念无关方差）。
2. key action → skill 映射（E2/E3 预设、循环）。
3. 错误行为 → misconception 映射（E2 编码假设）。
4. efficiency/similarity → 策略能力（E5 实证与预期相反）。

**哪些需要 validation**：
1. 我们自己的 key action / 行为 → 阅读技能映射（需阅读领域专家 + 独立 response-process 证据，§34 Step 1–8）。
2. 题型标签 → 技能属性（E8 证明题型 ≠ 认知，需逐一验证）。
3. phantom item 的局部独立假设（E2/E3 未处理，我们的自由阅读中更脆弱）。
4. stimulated retrospective report 的效度（E 组无直接证据，§20 PROJECT HYPOTHESIS）。

**哪些 cognition 根本无法从 trace 推断**：
1. 元认知过程（计划、监控、评价）——E7 显示 trace 侧匹配率仅 0%–4.70%。
2. 动机/情感状态——E7 的 Other 仅 think-aloud 能测。
3. 未语言化、无行为对应的内部过程——E7 的 S5 无法消歧。
4. 错误行为的"偶然 vs 系统"判定——E2 无稳定性证据。

### E 组最终交付
E 组把"行为 → 认知"的推断从"默认成立"转变为"必须经过验证链"：**E1–E5 给了我们诊断工具，E6–E8 给了我们验证工具，两者必须串联（§34 Step 8），否则系统会落入"行为特征相关性好 → 宣布检测到 cognition"的陷阱。**

---

## 44. Integrated A–E Traditional Cognitive Modeling Pipeline

对应任务文件 §44。总结 A–E 角色，只总结不设计工程实现。

```
Raw Observable Events
        │  D
        ▼
Behavioral Actions（SCROLL_BURST / ANSWER_CHANGE / OPTION_ELIMINATE...）
        │  B + C
        ▼
Process Evidence（behavioral action，语义依赖 context）
        │  E validity（§34 pipeline）
        ▼
Validated Cognitive Evidence
        │  A / A+
        ▼
Latent Cognitive Model（SRM / MSRM / TEM / RT-DINA / MJ-DINA / item expansion DCM）
        ▼
Skill / Ability / Misconception Profile
```

### 每个箭头旁的标注
| 箭头 | 状态 | 依据 |
|---|---|---|
| Raw Events → Behavioral Actions | **DIRECT**（规则/统计可确定，D 组已建立；保留边界 uncertainty） | D 组 |
| Behavioral Actions → Process Evidence | **PROBABILISTIC / VALIDATION REQUIRED**（行为语义依赖 context + 学生 + 题目，B/C 组建立） | B/C 组 |
| Process Evidence → Validated Cognitive Evidence | **VALIDATION REQUIRED**（E 组核心：必须走 §34 pipeline，否则只是 hypothesis） | E 组（E6/E7/E8） |
| Validated Cognitive Evidence → Latent Cognitive Model | **PROBABILISTIC**（但 mapping 必须先验证；E2–E5 提供统计工具） | E 组（E1–E5）+ A 组 |
| Latent Model → Profile | **PROBABILISTIC**（后验/分类概率；model output ≠ ground truth） | A/A+ 组 + E 组纪律 |

**关键**：E 组填上的是第 3 个箭头（Process Evidence → Validated Cognitive Evidence）——它**不是 DIRECT 也不是 PROBABILISTIC，而是 VALIDATION REQUIRED**。没有这个验证，整个链在"行为→认知"处断裂。E2/E3 的循环正是跳过了验证直接进入 latent model 的后果（§21）。

---

## 45. Remaining UNKNOWNs

对应任务文件 §45。**禁止为了"完整认知画像"强制猜测 cognition。**

### E 组明确未解决的 UNKNOWN
1. **任何 UI 行为 → 具体认知过程的映射**（我们的 UI 行为没有一篇 E 组论文直接验证；§40 全部标 candidate）。
2. **错误行为 = 迷思概念 vs 偶然错误**（E2 无稳定性证据）。
3. **stimulated retrospective report 的效度**（E 组只用并发 think-aloud）。
4. **phantom item 在自由阅读中的局部独立性**（E2/E3 是单任务售票机）。
5. **行为意义随学生/题目的调节机制**（E7/E6 承认依赖，未建模）。
6. **元认知过程从 trace 的可测性**（E7 显示匹配率 0%–4.70%）。
7. **"高 dwell / 高 fixation / 快 scroll" 的认知语义**（E4 限定 context、B/C 组否定直接映射）。
8. **S5（分歧）究竟是同时过程、伪影还是新过程**（E7 明确留待探索）。
9. **skill 与 misconception 的区分效度**（E2 的 a1−m1 高负相关未解释）。
10. **阅读领域的 validated attribute taxonomy**（E8 只有题型分类，无 latent skills）。

### 处理原则
对以上任意一项，如果行为 X 有多个合理认知解释且 E 组无足够证据消歧，输出应为 **UNKNOWN** 或 **multiple candidate interpretations + confidence**（E7 的 S5 处理是文献先例）。**禁止强制猜一个 cognition（任务文件 §45）。**

---

## 46. Evidence Index

对应任务文件 §46。页码均为本地 PDF 逐页核对（PDF 页 + 期刊页双标注）。禁止编造。

| # | Conclusion | Paper | PDF Page | Section / Eq / Table | Evidence Type |
|---|---|---|---|---|---|
| 1 | RT-CDM：lognormal RT 模型 log Tji = ζi − τj + εji | E1 | PDFPAGE 5（印刷 425） | Eq. 20.1 | Theory |
| 2 | joint RT-DINA：person 二元正态含 ρθτ，四条局部独立假设 | E1 | PDFPAGE 7（印刷 427） | Eq. 20.8 | Theory |
| 3 | 加入 RT 仅在 Q-matrix 不可识别/题短/guess-slip 高时有明显增益；理想测验无增益 | E1 | PDFPAGE 10–11（印刷 430–31） | §转述 Minchen & de la Torre 2016; Zhan et al. 2018 | Simulation（转述） |
| 4 | RT 替代解释：难度、speeded responding、低动机、preknowledge/作弊 | E1 | PDFPAGE 3（印刷 423） | §Intro | Theory |
| 5 | 迷思概念定义：基于个人经验的错误理解，可与正确概念共存 | E2 | PDFPAGE 2（印刷 482） | §Intro | Theory |
| 6 | 关键行动编码定义：是否包含解决问题所必需的关键行动 | E2 | PDFPAGE 2（印刷 482） | §Intro | Expert-defined |
| 7 | 状态压缩规则：删 CANCEL、连续重复缩减；FBABCD 示例 | E2 | PDFPAGE 4（印刷 484） | §方法 | Expert-defined |
| 8 | 38 个字节片段初选 → 删 <5%/>95% 与不可识别 → 28 道虚拟题目 | E2 | PDFPAGE 5（印刷 485） | Table 1 | Expert-defined |
| 9 | Q-matrix：正确状态→技能、错误状态→迷思概念；q_ik=1 iff 呈现序列 i 需要掌握属性 k | E2 | PDFPAGE 5（印刷 485） | §方法 | Expert-defined |
| 10 | "假设仅当参与者掌握了各行动序列所需的潜在属性后才能呈现该行动序列"（循环假设） | E2 | PDFPAGE 5（印刷 485） | §方法 | Expert-defined |
| 11 | 分类粒度：仅技能 13 种模式 vs 引入迷思概念 74 种模式 | E2 | PDFPAGE 9（印刷 489） | §结果 | Empirical |
| 12 | 分类信度：a+m 测验水平 .9899 vs a .9852 | E2 | PDFPAGE 8（印刷 488） | Table 4 | Empirical |
| 13 | 迷思概念与原始得分负相关：m1=−.78、m2=−.65、m3=−.71 | E2 | PDFPAGE 8（印刷 488） | Fig. 4 | Empirical |
| 14 | a+m 下仅 GDINA 拟合（SRMSR=.0756）；SABIC 正文与表 3 矛盾 | E2 | PDFPAGE 7–8（印刷 487–88） | Table 3 | Empirical |
| 15 | 正文 SABIC 表述与表 3 数字矛盾（SABIC GDINA=29718.24 > DINA=29455.78） | E2 | PDFPAGE 7（印刷 487） | Table 3 vs 正文 | Project finding |
| 16 | 无 think-aloud/眼动/访谈/专家评审/编码者一致性（grep 全文确认） | E2 | 全文 | — | Project finding |
| 17 | item expansion：1 题 → 228 序列 → 60 → 14 phantom items | E3 | PDFPAGE 10 | §3.2 | Empirical |
| 18 | phantom item "correct response" = 动作序列出现 | E3 | PDFPAGE 7 | §3 | Empirical |
| 19 | Q-matrix "based on expert judgment and is essentially retrofitting...post hoc" | E3 | PDFPAGE 7 | §3 | Expert-defined |
| 20 | PVAF revised Q 拟合更差（RMSEA2=.085>0.05），保留 original Q | E3 | PDFPAGE 12 | §4.4 | Empirical |
| 21 | HO-DINA 最优：AIC=17,090.83、BIC=17,327.65；LRT p=0.180 与 HO-GDINA 无差异 | E3 | PDFPAGE 13 | Table 3 | Empirical |
| 22 | corr(θ1, θ2)=0.826；SE 比较 t(3759)=−115.58 | E3 | PDFPAGE 15 | §4.5 | Empirical |
| 23 | "buy" 高 guess gi=0.442（IDI=0.558） | E3 | PDFPAGE 12–13 | Table 4 | Empirical |
| 24 | phantom items 假设 conditional independence（marginal dependence ≠ conditional dependence），但未用专门 residual/local-dependence model 检验；前缀确定依赖明显 | E3 | PDFPAGE 10 | §3.2 | Project finding |
| 25 | MJ-DINA：RA+RT+FC 三合一联合似然 + 两层 MVN | E4 | PDFPAGE 6–9（印刷 741–44） | Eq. 1–8 | Theory |
| 26 | FC 负二项模型 Vni ~ NB(exp(εn+mi), di^(−2)) | E4 | PDFPAGE 8（印刷 743） | Eq. 5–6 | Theory |
| 27 | FC 不加载在属性上（Vni ⊥ αn,τn \| εn） | E4 | PDFPAGE 10（印刷 745） | Assumption 8 | Theory |
| 28 | visual engagement "loading amount endorsed by FCs...not the entire visual attention" | E4 | PDFPAGE 4（印刷 739） | §Intro | Theory |
| 29 | FC 分类增益：多数条件相对增量 <1%，最大 5.49%（Q2 Φ=.8） | E4 | PDFPAGE 23–24（印刷 758–59） | Table 6 | Simulation |
| 30 | θ RMSE .698→.507（joint vs separate），Cor .706→.860 | E4 | PDFPAGE 17–18（印刷 752–53） | Table 3 | Simulation |
| 31 | 实证 Σperson：r_θτ=−0.125, r_θε=0.182, r_τε=−0.959 | E4 | PDFPAGE 28（印刷 763） | Table 9 | Empirical |
| 32 | 认知特征（fluency/focuser）仅 "rough inference" 非诊断 | E4 | PDFPAGE 11（印刷 746） | Table 2 | Theory |
| 33 | 实证 N=93、10 题、K=4；无外部效标 | E4 | PDFPAGE 25、35（印刷 760、770） | §实证 | Empirical |
| 34 | similarity = \|LCS(obs,ref)\|/\|ref\|；efficiency = \|LCS(obs,ref)\|/\|obs\| | E5 | PDFPAGE 6–7（印刷 591–92） | Eq. 3–4 | Theory |
| 35 | 参考序列由内容专家与题目开发者定义 | E5 | PDFPAGE 6（印刷 591） | §Component 3 | Expert-defined |
| 36 | 能力−相似性 0.990 [0.987, 0.992]；能力−效率 −0.543 [−0.586, −0.498] | E5 | PDFPAGE 12（印刷 602） | Table 2 | Empirical |
| 37 | 四分量 vs HO-LLM：ACA 0.863 vs 0.84；PCA 0.650 vs 0.598 | E5 | PDFPAGE 11（印刷 611） | Table 8 | Simulation |
| 38 | 低相关条件下四分量无优势（Low/500/30：HO-LLM 0.930/0.711 vs 四分量 0.929/0.710） | E5 | PDFPAGE 15（印刷 615） | Table 11 | Simulation |
| 39 | 三分量含效率 DIC=8,886.51 高于二分量 8,559.29 | E5 | PDFPAGE 8–9（印刷 598–99） | §Empirical | Empirical |
| 40 | process data ≠ response processes（manifest traces vs latent） | E6 | PDFPAGE 2（印刷 242） | §Intro | Theory |
| 41 | 过程指标必须"像产品数据一样验证" | E6 | PDFPAGE 4（印刷 244） | Figure 1 | Theory |
| 42 | Hahnel 4 预测簇只复现 2 簇 | E6 | PDFPAGE 5（印刷 245） | §专辑论文 | Empirical（转述） |
| 43 | Veerbeek 训练后产品分升、时间指标无实质变化（负结果） | E6 | PDFPAGE 5（印刷 245） | §专辑论文 | Empirical（转述） |
| 44 | 构念无关方差：噪音、题项、学生特征污染过程数据 | E6 | PDFPAGE 6（印刷 246） | §挑战 | Theory |
| 45 | 对齐五情形：S1=6.37%、S2=11.34%、S3=34.48%、S4=17.18%、S5=27.17% | E7 | PDFPAGE 11（印刷 1313） | Table 5 | Empirical |
| 46 | 互补约 45%（S2+S3）、可互换仅 17.18%（S4） | E7 | PDFPAGE 1、11、14（印刷 1303、1313、1316） | Abstract / Table 5 | Empirical |
| 47 | 交叉表对角元：MC.O 45.27%、MC.P 4.45%、MC.E 0%、MC.M 4.70%、LC.F 75.01%、LC.R 9.66%、HC.E/O 36.56% | E7 | PDFPAGE 12（印刷 1314） | Table 7 | Empirical |
| 48 | think-aloud 编码 κ=.53–.65, kmax=.81–.82 | E7 | PDFPAGE 7（印刷 1309） | §方法 | Empirical |
| 49 | 两路 "equally valid"、无 one truth、S5 不消歧 | E7 | PDFPAGE 8、18（印刷 1310、1320） | §整合规则 / §讨论 | Theory |
| 50 | 单路检出：think-aloud 57.82%、trace 80.21%（中位数） | E7 | PDFPAGE 10（印刷 1312） | §结果 | Empirical |
| 51 | 过程计数：trace 9,993、TA 38,856、整合 83,121 | E7 | PDFPAGE 14（印刷 1316） | §结果 | Empirical |
| 52 | Rasch：item reliability 0.91、separation 3.23；PCA 41.2%、第一对比 12.5% | E8 | PDFPAGE 11（印刷 10） | §Internal structure | Empirical |
| 53 | think-aloud 对齐率：总体 41%；literal 58%、inferential 48%、词汇 20%、主旨 35% 等 | E8 | PDFPAGE 10（印刷 9） | Table 4 | Empirical |
| 54 | Q6 案例：心理测量拟合好但 think-aloud 显示不对齐 → 重写构念 | E8 | PDFPAGE 13（印刷 12） | §Discussion | Empirical |
| 55 | fNIRS 词汇题低氧合 → 可能无需读 passage | E8 | PDFPAGE 11（印刷 10） | §Internal structure | Empirical |
| 56 | 阅读时间与总分 r=0.305、回看 r=0.260（均不显著） | E8 | PDFPAGE 12（印刷 11） | Table 5 | Empirical |
| 57 | think-aloud 编码为单人、inter-rater reliability NOT REPORTED | E8 | PDFPAGE 8（印刷 7） | §方法 | Project finding |
| 58 | 无外部效标（未施测 Gates-MacGinitie 等）；跨 passage 不可假设 | E8 | PDFPAGE 12–14（印刷 11–13） | §Relations / §Limitations | Project finding |
| 59 | 题型内部不一致：推断题 "two"（PDFPAGE 6）vs "three"（PDFPAGE 10）；题目数 10 vs 11 | E8 | PDFPAGE 6、10 | §方法 / §结果 | Project finding |
| 60 | E2 自述为 E3（Zhan & Qiao 2022）的方法学拓广；E2/E3 均用 PISA 2012 TICKETS 环境，但 E2=CP038Q02（N=3547，28 题）与 E3=CP038Q01（N=3760，14 题）非同一道题/同一分析数据集 | E2 | PDFPAGE 3（印刷 483） | §Intro | Project inference |
| 61 | 认知特征粗推断：Table 2 警示 "relatively rough...not accurate measurement" | E4 | PDFPAGE 11（印刷 746） | Table 2 注 | Theory |
| 62 | MC.E→LC.F 转移：think-aloud 25% vs trace 0% | E7 | PDFPAGE 16（印刷 1318） | §RQ2 | Empirical |

---

## 47. 严格禁止事项自查（任务文件 §48）

| # | 禁止事项 | 自查 |
|---|---|---|
| 1 | 把 process-data prediction improvement 等价 construct validity | ✅ §13/§18/§29/§42 反复区分 |
| 2 | 把 model fit 等价 psychological truth | ✅ §38（E8 Q6 反例）|
| 3 | 把 simulation recovery 等价真实 cognition validation | ✅ §37 |
| 4 | 把 correlation 等价 construct identity | ✅ §39（E5 0.990 案例）|
| 5 | 把 response time 直接解释成 difficulty | ✅ §10.17 E1（替代解释）|
| 6 | 把 fixation count 直接解释成 comprehension | ✅ §10.5/§10.23 E4（明确限定）|
| 7 | 把 eye tracking 当 cognition ground truth | ✅ §33（fixation ≠ 认知）|
| 8 | 把 think-aloud 自动当 cognition ground truth | ✅ §15/§33（E7 明确否定）|
| 9 | 把 trace 和 think-aloud 当可互换 measurement | ✅ §15（17.18%）|
| 10 | 把 key action 自动等价 skill mastery | ✅ §11 Q3（E3 替代策略）|
| 11 | 把没有执行 key action 自动等价 non-mastery | ✅ §11 Q2（E3 gi=0.442）|
| 12 | 把错误 action 自动解释成 misconception | ✅ §12（E2 编码假设）|
| 13 | 把 Q-matrix 当 action→skill mapping 的独立验证 | ✅ §11 Q5（PVAF 被否决）|
| 14 | 用 DCM 输出反过来证明输入 mapping 正确 | ✅ §21（循环风险）|
| 15 | 忽略 circularity | ✅ §21 专项 |
| 16 | 忽略 alternative explanations | ✅ §10.17 每篇 |
| 17 | 忽略 student/context/item dependency | ✅ §23/§24 |
| 18 | 把 E2/E3/E4 当成完全独立的 replication | ✅ §36 |
| 19 | 忽略相同作者/研究谱系 | ✅ §36（Zhan 谱系）|
| 20 | 把 reading item type 自动等价 latent skill | ✅ §16/§26（E8 对齐率、PCA 41.2%）|
| 21 | 把 think-aloud 的结论自动迁移到 retrospective recall | ✅ §20（三级判定：PROJECT HYPOTHESIS）|
| 22 | 把 validation data 当生产系统必须收集的数据 | ✅ §32（validation/labeling only）|
| 23 | 把 action segmentation uncertainty 当成 0 | ✅ §22（E 组无构念不确定性建模）|
| 24 | 把 cognitive interpretation 写成 deterministic mapping | ✅ §22/§35（S5 多候选 + confidence）|
| 25 | 删除 UNKNOWN | ✅ §45 保留完整 UNKNOWN 列表 |
| 26 | 为了完整 cognitive profile 强制猜测 cognition | ✅ §30/§45（禁止 A→E 单跳）|
| 27 | 使用 LLM / AI Agent 作为认知诊断方法 | ✅ 全文只综述传统统计/心理测量方法 |
| 28 | 修改 E1–E8 编号 | ✅ §0 未重排 |
| 29 | 编造 PDF 中不存在的样本量/F1/分类精度/模型参数/页码 | ✅ 全部数值与页码来自 §46 索引（逐页核对）|
| 30 | 用一般知识补论文没有证明的结论却不标来源 | ✅ 非原文内容一律标注 PROJECT TRANSFER INFERENCE / CROSS-PAPER SYNTHESIS / GENERAL METHODOLOGICAL CONTEXT |

---

*报告完成。E 组 8 篇论文全文（184 页）经 6 个并行子代理逐页精读 + 主代理抽查复核；所有关键数值与页码经 §46 Evidence Index 核对。*
