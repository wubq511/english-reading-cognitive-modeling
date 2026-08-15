# C 组 — 鼠标 / 光标 → 注意 / 焦点 / 意图

> 本文档为 C 组 8 篇论文（[C1]–[C8]）的深度阅读报告。C 组回答的核心问题：**在传统方法（不使用 LLM / AI Agent）框架下，加入 pointer/cursor 后，我们对「学生 attention/focus 在哪里」的概率判断究竟能提高多少；以及什么时候 pointer 可以作为 attention/focus 的 weak evidence、什么时候几乎没有信息。**
>
> 报告继承 A/A+/B 组已建立的前提：`viewport ≠ attention`、`pointer ≠ gaze ≠ reading`、行为含义依赖上下文、raw dwell 不能直接解释认知。C 组只提供 probabilistic reasoning 的证据基础，不设计最终算法。
>
> 生成日期：2026-08-12。全部页码引用均基于本地 PDF 文件逐页核对。
>
> **校验说明**：本报告的关键数值（对齐距离、AUC/F1/RMSE、相关、百分比、p 值、样本量）已经三轮核验：(1) 主代理对 8 篇 PDF 的逐页第一手核实；(2) 8 个并行抽取子代理的独立全文抽取报告交叉比对；(3) 针对数值与实验设计的核对审查复核（含 C3 Table 2 的 baseline-only/position 分解、C6/C7 的划分方式与 cross-user 泛化边界、C4 三轴评价修正）。三轮结果一致，个别页码与一处 block 数（C6 "six blocks" vs C7 "eight blocks"—2 warm-up，已调和）已修正。
>
> **核对审查修订记录（2026-08-12）**：(a) C4 三轴评价 Domain Similarity LOW→HIGH、Ground Truth → MEDIUM–HIGH；(b) C6/C7 的 AOI 级性能拆为「同分布+trial 级划分内的 Strong/Moderate」与「unseen student+阅读+paragraph+滚动的 Partial/Open」两层；(c) "AOI≈paragraph" 明确为 PROJECT TRANSFER HYPOTHESIS；(d) click/action 从 "Reliable attention anchor" 降为 "Moderate–Strong（最强 cursor spatial anchor，非 attention truth）"，interaction intent 另给更高等级；(e) C3 personalization 数字改为依任务分解（+1.2~4.9pp，位置校正另 +0.9–2.4pp）；(f) eye GT vs self-report 对比降级为"方向一致、非受控 GT-only 消融"；(g) §24 采样率不锁定 60–100Hz、C8 阈值改为 candidate operationalization、raw 定义改为 Raw Observable Events；(h) §25 Q11 改为"理论上辅助、具体增益无直接证据、需自行验证"；并新增 §26 的 6 条正式结论。

---

## 任务符合性对照表（依据 `../../provenance/LEGACY_REPORT_PROVENANCE.md` 登记的 Chat 2 / Turn 10 原始任务书逐条核对）

| 任务文件章节 | 任务要求 | 本报告完成位置 |
|---|---|---|
| §0 | 严格锁定 C1–C8 编号（禁止重排） | §0 PDF 映射（8/8 在位；C2 标题歧义已核查、C3/C8 年份差异已说明） |
| §1 | 传统方法上限研究，完全不使用 LLM/AI Agent | 全文未引入 LLM/Agent 方案（任务 §28-2） |
| §2 | 以双栏阅读界面为落点 | 各章 §x.16 迁移小节均按该界面分析 |
| §3 | 继承 viewport≠attention、pointer≠gaze≠reading、行为依赖上下文、raw dwell 不能解释认知 | 报告头注 + §13/§20/§23/§26 |
| §4 | 回答「pointer 何时是 weak evidence、何时几乎无信息」 | §1(11)、§13、§25 Q1–Q3、§26 |
| §5 | 严格区分 5 个概念（Cursor Position/Behavior、Gaze、Task Attentiveness、Difficulty） | §11 注意真值矩阵、§16/§17、§26 逐命题分级 |
| §6 | 三轴评价（GT Quality / Ecological Validity / Domain Similarity） | §10 跨论文对比矩阵（B/C 轴列 + GT 列） |
| §7 | 每篇统一拆解模板（§7.1–§7.17） | §2–§9 每篇 17 小节逐项覆盖 |
| §8 | 专题一 Mouse ≠ Gaze | §13（10 问逐答） |
| §9 | 专题二 Forced Coupling vs Natural Cursor | §14（C4 上限 vs C5 生态证据，禁止直接比较 performance） |
| §10 | 专题三 Pointer-Assisted Reading | §15（PAR 现象、普遍性边界、先检测再加权） |
| §11 | 专题四 Mouse → Difficulty | §16（mouse difficulty ≠ spatial attention） |
| §12 | 专题五 Mouse → Attentiveness | §17（cursor 双信号分层，不合并为一个 attention score） |
| §13 | 专题六 Self-Reported vs Eye GT | §18（C1 自评 vs C6/C7 眼动，非同一 construct） |
| §14 | C6/C7 数据独立性审查 | §19（审计表；禁止计为两次独立 replication） |
| §15 | Mouse Evidence Matrix | §20（21 类信号分级） |
| §16 | Focus Estimation 证据层级 | §26（Strong/Moderate/Weak/Unsupported） |
| §17 | 无信号也是信息吗 | §25 Q13（stale decay 标为 PROJECT HYPOTHESIS） |
| §18 | Personalization / Calibration | §21（个体差异最强效应、C3 基线校正法） |
| §19 | Spatial Attention vs Intent | §22（intent 比 reading gaze 更可靠） |
| §20 | 融合 B 组：pointer 解决 viewport≠reading | §23（情形 A–E 逐案，区分论文直接支持 vs 项目推论） |
| §21 | 重新审视 Pointer Raw Events（raw vs derived） | §24（Data Collection Implications） |
| §22 | Ground-Truth Hierarchy | §11 + §26（三轴，指出 GT 强但生态弱/生态强但 GT 弱） |
| §23 | 15 个跨论文问题 | §25（Q1–Q15 全部作答） |
| §24 | What Group C Establishes | §26（含逐命题判定速查表） |
| §25 | C 组之后交给 D/E 的问题 | §27（Group D）/ §28（Group E） |
| §26 | Evidence Index | §29（28 条，带 PDF 页码） |
| §27 | 报告输出结构（§0–§29） | 本文件完全按该结构 |
| §28 | 严格禁止事项（17 条） | 逐条自查通过（见报告正文，无 LLM/Agent、无 cursor=gaze、无改编号、无编造数字等） |
| §29 | 最终质量标准 | §1 + §26（以「条件性概率证据」而非「cursor=attention」作结论） |

---

## 0. PDF 映射

| 编号 | 论文 | 本地 PDF 文件 | 期刊/场合 | 出版年份（文件名年份） |
|---|---|---|---|---|
| C1 | Learning Efficient Representations of Mouse Movements to Predict User Attention（Arapakis & Leiva） | `C_2020_Arapakis_MouseAttention.pdf` | SIGIR '20, 43rd Intl. ACM SIGIR Conf. | 2020 |
| C2 | User See, User Point: Gaze and Cursor Alignment in Web Search（Huang, White & Buscher） | `C_2012_Huang_UserSeeUserPoint.pdf` | CHI 2012 | 2012 |
| C3 | Predicting respondent difficulty in web surveys: A machine-learning approach based on mouse movement features（Fernández-Fontelo, Kieslich, Henninger, Kreuter & Greven） | `C_2020_FernandezFontelo_QuestionDifficulty.pdf` | arXiv 预印本（2020）；期刊版 Social Science Computer Review（2023） | 2020（预印本） |
| C4 | Mouse Tracking for Reading (MoTR): A new naturalistic incremental processing measurement tool（Wilcox, Ding, Sachan & Jäger） | `C_2024_Wilcox_MouseTrackingReading.pdf` | Journal of Memory and Language 138, 104534 | 2024 |
| C5 | Virtual Finger-Point Reading Behaviors: A Case Study of Mouse Cursor Movements on a Website（Kirsh） | `C_2022_Kirsh_VirtualFingerPointReading.pdf` | Big Data Research 29, 100328 | 2022 |
| C6 | A Versatile Dataset of Mouse and Eye Movements on Search Engine Results Pages（Latifzadeh, Gwizdka & Leiva） | `C_2025_Latifzadeh_SERPDataset.pdf` | SIGIR '25 | 2025 |
| C7 | AdSight: Scalable and Accurate Quantification of User Attention in Multi-Slot Sponsored Search（Villaizán-Vallelado et al.） | `C_2025_Villaizan_AdSight.pdf` | 2025 | 2025 |
| C8 | Mouse movements reflect personality traits and task attentiveness in online experiments（Meidenbauer, Niu, Stier & Berman） | `C_2022_Meidenbauer_MouseMovementsPersonality.pdf` | Journal of Personality（DOI 10.1111/jopy.12736），2023 正式出版 | 2022（接受稿/早期在线） |

**编号说明**：
- 文件名年份≠出版年份的共有两处：[C3] 本地文件是 2020 年 4 月导出的 arXiv 预印本（经外部检索确认为 arXiv:2011.06916），期刊正式版 2023 年发表于 Social Science Computer Review 41(1), 141–162（任务给定标题措辞为 "Predicting Question Difficulty..."，PDF 标题为 "Predicting respondent difficulty..."，同一论文）；[C8] 本地文件为 2021 收稿/2022 接受的稿子，期刊 2023 年正式出版。
- [C2] 标题页与任务给定标题**逐字一致**（"User See, User Point: Gaze and Cursor Alignment in Web Search"），三位作者 Jeff Huang · Ryen W. White · Georg Buscher 全部在标题页（PDF 物理页 1）。**不是**任务警示的 "User See, User Point: Locating Users' Attention Using Cursor Movements on Web Pages" 那篇，无需替换。
- 8 篇全部在位，无 `C# — PDF NOT FOUND`。

---

## 1. 最高层结论

以下为 C 组跨 8 篇论文的最高层结论（详细证据见各章与 §29 证据索引）。

1. **`cursor ≠ gaze` 在点级上是被 C 组直接验证的，不是假设。** [C2] 用 36 被试/32 任务的受控眼动研究给出：cursor 平均滞后 gaze 约 700 ms（个体 250 ms–>1 s），且不存在反向（"gaze lagging behind the cursor—did not occur"，PDF p.5）；inactive（cursor 静止 ≥1s）时段占 58.8%，此时对齐距离 233 px（"the eye is still roaming the SERP"）。[C6] 在真实 Google SERP 上测到 eye–mouse 平均欧氏距离 **372.89 px——几乎是 [C2] 引用的 Huang et al. 数值（178 px）的两倍**。**点级 cursor 位置不能当作 gaze 位置。**

2. **cursor 与 gaze 的对齐是「行为状态 × 用户 × 任务」的条件函数。** 最强对齐发生在主动交互：action（click 前 1s）77 px、click 74 px；reading 150 px；examining 167 px；inactive 233 px（[C2] Table 1）。**主动交互（点击、划线、划掉选项）时的 cursor 是最可靠的 attention 锚点；静止 cursor 几乎不含位置信息。**

3. **个体差异是 C 组最强效应，且不是年龄/性别可解释的。** 个体平均对齐距离 SD=33.9，显著大于任务间 SD=20.2（Levene p=0.037）；性别、年龄均不显著（[C2] p.4）。[C3] 证明个人 baseline 校正**有明确价值、但增益依任务而异**：employment detail 未校正 60.97%→baseline 校正 65.87%（**+4.9pp**）；employee 55.48%→baseline 56.70%（**+1.2pp**）→+position 59.09%（位置校正再 +2.4pp）；education 56.22%→baseline 58.05%（**+1.8pp**）→+position 58.95%。**统一的全局 mouse→attention 映射不可辩护；personal calibration 有明确文献依据（但效果大小不能写死）。**

4. **区域级（region/AOI）聚合是 cursor→attention 推断的正确粒度；paragraph 级是项目迁移假设。** 点级预测 gaze 坐标的 RMSE 仍高达 181–237 px（[C2]）；而把眼动 fixation 聚合成广告 AOI 标签后，cursor 轨迹（前 5 s）+ AOI 框的 GRU 达到 F1 93%（organic）/73%（DD）（[C6]）；多槽模型预测 slot 级 TFT/TFC（NDCG≈96）与 noticed（平均 AUC 81.24）（[C7]）。**但两点必须限定**：(a) C6 的 F1 0.93/0.73 与 C7 的 AUC 0.81 均来自 **trial 级随机分层划分**（C6 "random disjoint and stratified splits of 70%...30%"；C7 的 3-fold CV 仅用于 Optuna 超参寻优）——**未做 participant-disjoint 划分，不能证明对完全未见的新学生（cross-user generalization）有效**；(b) C6/C7 的 AOI 是**广告槽位**（organic ad / direct-display ad / ad slot），**不是** Paragraph/Question stem/Option——"AOI≈paragraph" 目前是 **PROJECT TRANSFER HYPOTHESIS**，C 组未直接验证。**我们系统的段落/选项级 focus 推断是合理方向，但需自己实验验证。**

5. **眼动 GT 与自评 GT 不是同一 construct；[C6] 的对比与"fixation GT 更干净"一致，但这不是受控的 GT-only 消融实验。** [C1] 的 "attention" 是**任务后自评**（5 点 Likert "是否注意到广告"，页面已不可见，二值化后 66% 正类）——测量的是事后知觉/记忆。 [C6] 用同一 GRU 模型对比：自评 GT 数据集上 F1 仅 56%/69%，眼动 fixation GT 上 93%/73%。**方向一致、作者也这样解释**，但两个数据集在参与者、SERP、实验流程、布局上均不同，性能差异不只来自 GT 质量（还可能来自 dataset difficulty / class distribution / layout / participant behavior）。**"93% vs 56% = 完全由 GT 质量导致" 不能成立**；可作为验证设计原则（"眼动 GT 优先于自评 GT"），但不能量化为纯 GT 效应。[C3]/[C8] 的难度/投入度 GT 则与 spatial attention **完全无关**，任何跨论文改写都是越界。

6. **[C6] 与 [C7] 是同一实证来源，不是两次独立 replication。** AdSight 明确引用 "associated dataset paper [43]"（=C6），两者同 47 被试、同 2,776 trials、同 Gazepoint GP3 HD、同 mouse 日志、同事务性查询。所有综合必须把 C6/C7 当作 "dataset + modeling 来自单一实验源"。

7. **自然阅读界面中 cursor 的 reading 信号存在但稀疏、个体化。** [C5]（9,036 万个自然网页鼠标事件）证明 PAR（cursor 当"虚拟手指"沿文本读）是真实、跨大洲的现象，右向慢移（150–200 px/s≈阅读速度）与阅读一致；但鼠标在页面可见时间中移动 <2%、"PAR is not practiced by all users all the time"、PAR 松紧个体差异大。[C4]（MoTR）证明**当界面强制 mouse 耦合阅读位置时**（文本模糊、仅 mouse 尖端可读），word-level mouse reading times 与眼动相关可达 0.42–0.62——这是**强制耦合上限**，**不能推广**到用户可不动 mouse 的自然页面。

8. **mouse → difficulty 与 mouse → attention 是两条独立的证据通道。** [C3] 证明 mouse 特征（尤其 RT、initiation time、flips、hovers、max acceleration）在真实调查中预测实验操纵的难度，但增益小（~1–3 pp）、依赖难度来源（措辞→RT；顺序→动作特征），且全篇无眼动、无位置语义。[C8] 证明 click 类特征预测会话级投入度（atypical responding，r≈−0.18），但与空间注意无关。**C 组不支持任何"慢速=难=在看"的简化映射。**

9. **cursor 对 interaction intent 比对 reading gaze 更可靠。** cursor 在交互目标处（click 前后）与 gaze 对齐最紧（74–77 px），且 [C7] 显示轨迹时序索引是最关键特征。[C2] 明确 "the user looks at something and then moves their cursor to interact with it"。**`pointer near option B` 更可信地是"将点击/操作 B"的信号，而非"正在读 B"。**

10. **C 组的最可靠角色定位：cursor 是 contextual auxiliary evidence + interaction-intent signal + 会话级 engagement signal；在「active + 区域/AOI 粒度 + 个体校准」条件下是 weak spatial sensor；不能作为 primary sensor 或 attention truth。** 完整支持：`Viewport + Cursor + Temporal Context + Task Context + Student-specific Cursor Behavior → Probabilistic Focus Evidence`（任务 §29），**反对** `Cursor Position → Attention Truth`。

11. **C 组证据的空白区（重要）**：没有任何一篇处理「独立滚动文档 + cursor」（C 组全是静态 SERP / 单屏 / 自然浏览统计）；没有"滚动长 passage 下 cursor 语义"的研究；stale cursor 的 evidence decay 曲线无直接证据（PROJECT HYPOTHESIS）。**我们系统的双栏独立滚动布局是 C 组证据的外推边界。**

---

## 2. C1 — Learning Efficient Representations of Mouse Movements to Predict User Attention（Arapakis & Leiva, 2020）

**定位：raw mouse trajectory / representation learning → attention prediction（预测对 SERP 广告的注意）。**

### 2.1 研究问题
用 raw mouse cursor 轨迹（不经手工特征）的多种表示训练 RNN/CNN，预测用户对 SERP 上**直接展示（direct display）广告**的注意。论文明确动机是避免手工特征工程："previous work has relied heavily on handcrafted features, which is a time-consuming approach that often requires domain expertise"（Abstract）。

### 2.2 任务 / 环境
- 众包**事务性搜索任务**：给预定义查询 + 静态 Google SERP，要求"点击页面上最能回答该查询的元素"（例："You want to buy a Rolex watch ... click on the element that you would normally select"）。
- **natural interaction**（非强制 mouse 指向）；但页面被仪器化：**只保留一个广告**（single-slot auction 情形）、要求关闭 ad-blocker、行为偏快（众包）。
- 每个条件 1 个广告：organic 广告（左上/左下）、direct display 广告（右上或左上）；SERP 静态抓取、英语。

### 2.3 被试
**N = 3,206**，年龄 18–66、国籍混合，Figure Eight 众包平台，Level 3 经验贡献者，报酬 $0.20。每人只做一次（一个 query×广告条件）。未报告性别/设备。

### 2.4 原始鼠标数据
- 工具：EvTrack（JS 事件追踪库）。**mousemove 用 event polling 每 150 ms 采样一次**；其他事件（load/click/scroll）用 event listener。
- 字段：`(x, y), timestamp, event name, XPath of DOM element`。
- 过滤后 **2,289 个 sessions / 45,082 个鼠标坐标**（organic 763 / left-display 793 / right-display 733）。
- 坐标系：浏览器像素；水平坐标按 viewport 宽度归一化（垂直未归一化，因 SERP 固定宽）。

### 2.5 眼动数据
**NO EYE-TRACKING GROUND TRUTH。** 本实验完全没有眼动。论文仅综述转引 gaze-cursor 相关性（如 Huang et al.）。

### 2.6 注意真值（核查点 1：自评）
**GT = 任务后自评问卷**（非眼动）：
> "we collected ground-truth labels through an online questionnaire, which was administered at post-task and asked the user to what extent they paid attention to the ad using a 5-point Likert-type scale: 'Not at all'(1)... 'Very much'(5)."
- 二值化：Not at all / Not much → negative；Somewhat / Very much → positive；中性（I can't decide）丢弃。66% 正类。
- 作答时**页面已不可见**——测量的是**事后广告知觉/记忆**，不是在线注视。

### 2.7 鼠标预处理
- 会话过滤：<5 个坐标（≈1s）丢弃；固定序列长度 50 timesteps（≈均值+1SD），短 pad / 长截断；水平坐标 viewport 归一化；无平滑/去噪/插值/pause 提取/personalization。

### 2.8 鼠标特征
**无手工特征**。输入两类表示：
- **时间序列**：2D 坐标多元时间序列；
- **视觉图像**（5 种编码 × 有无 ad placeholder）：heatmap（25px Gaussian kernel）、trajectories、colored trajectories（温度梯度）、trajectories with line thickness、colored+thickness；1280×900 PNG，viewport 归一化，无数据增强。

### 2.9 Mouse ↔ Gaze 关系
**不适用**（无 gaze 数据，无距离/lag/AOI 分析）。

### 2.10 模型
- RNN：SimpleRNN / LSTM / GRU / BLSTM；输入 50 神经元、隐藏层 n∈[16..128]、dropout q∈[0.1..0.5]、sigmoid 输出；binary crossentropy + Adam；random search 调参；3-fold CV on validation。
- CNN：AlexNet / SqueezeNet / ResNet50 / VGG19，ImageNet 预训练 + transfer learning 微调。
- 划分：60-10-30 分层（per ad format）。

### 2.11 预测目标
**逐字：二分类 "did the user notice the ad?"**——给定 cursor 轨迹判断"是否注意到（那个唯一的）广告"。**不是** spatial attention（哪个广告被看）、不是连续注意量，是 session 级 per-ad 的 noticed 标签（基于自评）。

### 2.12 评估
- 指标：Adj. Precision/Recall/F-Measure + **AUC（关键指标）**。
- 最优：ResNet50（trajectories 表示，right-aligned 广告）**AUC 0.739 / F1 0.731**；organic 最佳 0.690；left-display 最佳 0.708。
- CNN 优于最佳 RNN：organic +3.24%(F1)/+9.35%(AUC)；left +13.91%/26.42%；right +18.65%/20.35%。
- 广告位置效应显著（left vs right AUC p<.0001, r=−0.88；大效应量）。
- 划分：per-format 分层 held-out；**无 within/cross-user 区分报告**（每 session=唯一被试）。

### 2.13 个体差异
**NOT REPORTED**（无 per-user 建模、无 personalization；每人只做一次）。

### 2.14 任务依赖
**是**：cursor→注意预测显著受 ad format 与 ad position 调节（大效应量）；ad placeholder 仅在 left-aligned 条件显著影响 F1（Mdn 0.718 vs 0.691, p=0.041）。

### 2.15 因果性 / 构念效度
predictive/correlational；**无因果论证**。论文自认 "While mouse tracking cannot substitute eye tracking technology"。GT 是事后自评，受记忆/期望影响；众包快节奏压低注意力。

### 2.16 迁移到我们的英语阅读系统
- **可直移**：raw trajectory→表示学习→二分类范式；时间序列+RNN 与图像+CNN transfer learning 技术栈；viewport 归一化；AUC 作为类别不平衡关键指标；60-10-30 分层。
- **要改造**：GT 需重新定义（自评"是否注意到广告"不可移植为客观注意；我们可能需眼动或受控任务标签）；序列/布局（SERP 固定宽、90% 坐标在首屏，我们的 passage 独立滚动需建模垂直与滚动）；预测粒度（C1 是 session 级单广告，我们需要元素/区域级）。
- **不可移**：自评 GT 的结论不能作为 cursor→客观视觉注意的证据；众包单任务快节奏场景与深度阅读差异大。

### 2.17 这篇论文不能确立什么
- **不能证明 cursor→客观视觉注意（gaze）**：GT 是自评，无眼动，作者自认 mouse 不能替代眼动。
- 不能声称预测了"空间注意"或"总注意量"：仅"唯一广告是否被注意到"的 session 级二分类。
- 不能声称优于手工特征模型：论文只对比 CNN vs RNN，**无 638-feature 手工 baseline 的数字对比**。
- 不能建立个体差异/个性化结论。
- "noticed" 是记忆/知觉型自评，且仅 1 广告/强制关 ad-blocker，notice 率可能被抬高。

---

## 3. C2 — User See, User Point: Gaze and Cursor Alignment in Web Search（Huang, White & Buscher, 2012）

**定位：真实 gaze ↔ cursor alignment 的基础论文。这是判断 `cursor ≠ gaze` 与「cursor 在什么条件下才含 visual-attention 信息」的核心证据。**

### 3.1 研究问题
确定 gaze 与 cursor 何时对齐、何时 cursor 位置能作为 gaze 位置的好的代理；研究 time、behavior pattern、user、search task 四类因素对 alignment 的影响；并据此用 cursor 特征预测 gaze 位置。

### 3.2 任务 / 环境
- **N=36 被试（38 招募，2 剔除），32 个 web search 任务**，在 Bing 上完成；一半导航型（找特定网页）、一半信息型（找事实）。每个任务给描述 + 预定义 query，之后自由浏览 SERP/后续网页/继续搜索。**natural interaction**（受控实验室眼动研究，不强制"眼到鼠标到"）。
- 显示器 1280×1024、17"；浏览器窗口 1040×996；每被试清除缓存/cookies。全程约 1 小时/人。

### 3.3 被试
36 分析（21 F / 17 M，38 招募）；年龄 26–60（M=45.5, SD=8.2）；user study pool（背景多样）；国别未报告。

### 3.4 原始鼠标数据
- cursor (x,y)、timestamp；行为（dwell/idle 由时间戳推、click 瞬时事件、scroll 提及）；**cursor 约每 100 ms 记录一次（≈10Hz）**。
- 总量：1,210 个 search tasks 中 **87,227 个 cursor positions**（移动时才记）。

### 3.5 眼动数据
- **Tobii x50，50 Hz，accuracy 0.5°（≈16px）**；gaze 约每 20 ms；开头有 calibration。
- 同步：以 cursor 时刻为基准对 gaze 线性插值（式 1）；cursor 位置仅在"相邻 gaze 间隔 ≤100ms"时被采用，减少插值噪声。
- 总量 **1,336,647 个 gaze positions**。

### 3.6 注意真值
GT = **眼动仪测得的连续 gaze 位置**（"the ground truth is the gaze position measured by the eye-tracking system"）。"attention" 作为动机构念（cursor 近似视觉注意），但实验目标始终是连续 gaze 位置预测。

### 3.7 鼠标预处理
- 滞后分析：cursor 与 gaze 在 50ms 间隔重插值，再在不同 shift 下算 RMSE。
- 预测：特征取 log(dwell)、log(距上次移动时间)；无平滑/插值/去噪；无个人 baseline 归一化（作者明确不把 user/query 当特征，理由：部署时无 gaze 数据训练、查询级数据不足、query 影响小）。
- 行为分类为启发式（"The process is ad-hoc"）。

### 3.8 鼠标特征
- Spatial：cursor position (cx, cy)。
- Temporal：dwell `log(td)`（页载入后时间）、behavior `log(tm)`（距上次移动时间）。
- 未来特征：fx（当前 gaze 最可能的后续 cursor 位置，仅当上次移动在目标未来时间 10s 内）。
- 交互项：cx×log(td)、cx×log(tm)。
- 回归式（x 坐标）：`gx ~ cx + log(td) + log(tm) + cx×log(td) + cx×log(tm) + fx`（式 2）。
- 行为分类规则：**Inactive**=静止≥1s；**Action**=click 前 1s；**Reading**=垂直≤50px + 右移≥150px + 回移≥50px；**Examining**=其余；Click=瞬时。

### 3.9 Mouse ↔ Gaze 关系
- 滞后：**cursor 滞后 gaze 平均 ~700ms**（个体 250ms–>1s；整体 700ms 时 RMSE 最低）。"the cursor lagged behind the gaze for each individual subject; the inverse situation—gaze lagging behind the cursor—did not occur"——**反驳"有人用 cursor 领跑视线"**。
- 时间进程：页载入后 0.5–1s 对齐达峰 ~240px，约 2s 后收窄（先扫视、后细读/准备点击）。
- 行为×对齐（Table 1）：inactive 233px/58.8%；examining 167px/32.9%；reading 150px/2.5%；action 77px/5.7%；click 74px。
- 个体/任务：个体 SD=33.9、任务 SD=20.2（Levene p=0.037）；性别 t(34)=1.31,p=0.20；年龄 ρ=0.22,p=0.18；click entropy 无相关（ρ=0.01,N=27,p=0.96，未复现导航/信息型差异）。

### 3.10 模型
**多元线性回归**（x、y 分别回归；OLS）；baseline = 直接用 cursor 位置；**36-fold leave-one-subject-out CV**（用 35 人系数预测留出被试 gaze）。

### 3.11 预测目标
预测 **gaze 位置（x 与 y 坐标）**（连续回归），ground truth = 眼动 gaze。

### 3.12 评估
- **RMSE（像素）**：baseline cursor 236.6 → +behavior+dwell 186.3（−21.3%）→ +future 181.1（−23.5%）；x 185.0→125.2→125.1；y 145.0→137.1→129.9。
- ANOVA 显著：x 轴 F(2,105)=59.72, p<.001；Euclidean F(2,105)=41.31, p<.001。
- **cross-user**（留出被试未见）、held-out。

### 3.13 个体差异
**本文最强效应**：个体对齐距离 SD=33.9；有人 ~130px、有人 ~280px；Levene 显示个体差异>任务差异；行为类别内个体差异依然很大（Subject 29 inactive 79%；Subject 12 examining 55%；reading≤2% 的有 22/36 人，最多 Subject 9 8%；Subject 33 全类距离都大）。作者："for each cursor behavior, gaze-cursor alignment still varied substantially among our subjects."

### 3.14 任务依赖
任务间差异适中但显著小于个体差异（SD=20.2）；click entropy 无相关；dwell time 与 behavior 调节对齐。导航/信息型差异未复现（contrast Guo & Agichtein）。

### 3.15 因果性 / 构念效度
correlate/predict；无操纵。唯一"时序因果"是 cross-correlation lag（cursor 跟随 gaze），支持假说 c（"user looks at something and then moves their cursor to interact with it"）。构念边界：lab 限制（休息/多任务、人为任务、SERP 外推广性）在 Discussion 明示。

### 3.16 迁移到我们的英语阅读系统
- **可直移**：行为标签大幅改善 gaze 代理的思想（cursor+behavior+dwell 把 RMSEd 236.6→186.3，再 +future 到 181.1）；**action/click 类行为对齐极近（77/74px）**——我们系统的划线/划选项动作可作为高置信 attention 锚点；个体差异大 → 需用户级 baseline。
- **要改造**：Reading 阈值（150/50/50px）针对 SERP 字号需重标定；行为 taxonomy（inactive/examining/reading/action/click）需映射我们的交互（划线=action 延伸、划掉选项=新 action 子类、passage 内滚动独立信号）；dwell 需按区块载入时间重定义。
- **不可移 / 边界**：仅 SERP 实验室搜索；58.8% inactive 时段 cursor 不携带注意信息；reading 型行为仅占 2.5%、22/36 人 ≤2%——**不能指望学生普遍"用 cursor 跟读"**。

### 3.17 这篇论文不能确立什么
- **不能证明 cursor=gaze 或 cursor 能近似 gaze**："claiming that the cursor approximates the gaze is misguided"（p.9）；baseline RMSEd 236.6px。
- 不能证明 cursor 停驻指示 attention："prolonged cursor fixation may not [be a positive signal of interest] ... the user's attention is probably elsewhere"（p.9）。
- 不能证明 alignment 规律推广到非 SERP 页面（论文明确非 SERP 更差、留作 future work）。
- 不能证明 reading 行为识别：reading 只是启发式行为类别，未验证 fixation 级关系。
- 不能证明个体/任务效应可预测：模型刻意不用 user/query 特征。
- "23.5% more accuracy" 是 RMSE 相对下降，不是分类准确率。

---

## 4. C3 — Predicting respondent difficulty in web surveys（Fernández-Fontelo et al., 2023 [预印本 2020]）

**定位：mouse features → experimentally manipulated question difficulty。研究的是 difficulty/response burden，不是 spatial gaze。**

### 4.1 研究问题
"When predicting response difficulty, what do we gain beyond response time through mouse-tracking features, and can we further improve prediction through personalization?"（PDF p.7）。补充：哪些特征最重要、用哪种 ML 算法。

### 4.2 任务 / 环境
- 德国 IAB 就业面板的**在线问卷**（SoSciSurvey），多选题点选。非阅读/搜索/广告任务。
- **natural interaction**（无强制 mouse）；每十秒向服务器上传 paradata。
- 三个目标题：employment detail（9 选项，措辞操纵）、employee level（4 选项，顺序操纵）、education level（11 选项+开放文本，顺序操纵）；另有 8 个无操纵 baseline 题。

### 4.3 被试
1,250 响应 / 1,213 完成；**886（73%）使用鼠标者纳入分析**；平均年龄 51（SD=10.8）、454 F/425 M。最终样本：employment detail 551、employee level 501、education level 548。国别：德国。

### 4.4 原始鼠标数据
- 客户端脚本采集（mousetrap-web；Henninger & Kieslich 2020），**每十秒批量上传**；从 paradata 抽取轨迹。
- **采样频率：NOT REPORTED**；click 数据未被使用（列为未来工作）。
- 处理：mousetrap R 包计算指标。

### 4.5 眼动数据
**NO EYE-TRACKING GROUND TRUTH。**

### 4.6 注意真值
不建模 attention。**GT = 实验操纵的难度条件（difficult vs easy）**："using the experimental condition (difficult or easy) as a target variable"（PDF p.17）。难度是操纵变量非测量变量（"we only manipulated but did not measure difficulty"）。

### 4.7 鼠标预处理
- 过滤：未作答、mouse 记录不完整、疑似重载、education 题自由文本者、age/gender 缺失/other、RT>7min。
- hover 阈值：测试 250/500/2000/3000ms（无唯一最优）。
- **personalization**：8 个 baseline 题回归取残差（baseline 校正）；再加答案位置校正（两步法 Eq.3–4）。

### 4.8 鼠标特征（9 个 + 年龄/性别）
- time：response time、initiation time；
- hovers：hover 次数、hover 总时长；
- distance：total distance；
- derivatives：max velocity、max acceleration；
- flips：x-flips、y-flips。
每模型共 11 个解释变量（9 mouse + age + gender）。

### 4.9 Mouse ↔ Gaze 关系
**不适用**（无眼动）。

### 4.10 模型
logistic regression、classification trees、random forest、gradient boosting、SVM（径向核）、单隐层 BP 神经网络。二分类 difficult vs easy；**嵌套 CV**（外环 10 折、内环 500 次 subsampling 75/25）；accuracy 评估；mlr/R 实现。

### 4.11 预测目标
**逐字：预测问卷问题的难度实验条件（difficult or easy 二分类）**——不是注意、不是 gaze 位置、不是难度评分。

### 4.12 评估（准确率）
| 题目 | 未校正 full | baseline 校正 | baseline+position | RT-only（best） |
|---|---|---|---|---|
| employment detail（措辞） | 61.0% | **65.9%**（GB） | 65.0% | 64.8% |
| employee level（顺序） | 55.5% | 56.7% | **59.1%**（GB） | 55.7% |
| education level（顺序） | 56.2% | 58.1% | **58.9%**（RF） | 56.4% |
- **personalization 分解（C3 Table 2 精确数值）**：employment detail 未校正 60.97%→baseline 校正 65.87%（**纯 baseline 增益 +4.90pp**，position 反而略降）；employee 55.48%→baseline-only 56.70%（**+1.22pp**）→+position 59.09%（位置校正再 +2.39pp）；education 56.22%→baseline-only 58.05%（**+1.83pp**）→+position 58.95%（再 +0.90pp）。**结论：个人 baseline 归一化有明确价值但增益依任务而异（+1.2~+4.9pp）；选项位置校正在「顺序被操纵」的题上还能额外贡献 +0.9~2.4pp。**
- 特征重要性（permutation accuracy 下降）：措辞题 RT(−0.142)、y-flips(−0.028)、x-flips(−0.014)；顺序题 initiation(−0.113)、x-flips(−0.041)、hovers(−0.033)——**顺序题上 permuting RT 只降 0.009**；education 题 max acceleration(−0.224) 最重要。
- 样本外（嵌套 CV）；被试间设计。

### 4.13 个体差异
**personal baseline 归一化有明确价值，但增益依任务而异（employment +4.9pp、employee/education +1.2–1.8pp）；选项位置校正在顺序操纵题再贡献 +0.9–2.4pp。** 动机：硬件/系统/交互习惯使 mouse 行为在受访者间系统性不同。**不同用户 mouse baseline 不同 → personalization 值得研究**（效果大小不能写死）。

### 4.14 任务依赖
**强调节**：不同操纵（措辞 vs 顺序）被不同 paradata 捕获——RT 对措辞题最重要，initiation/flips/hovers 对顺序题更重要；max acceleration 对 education 重要、对 employee 无用（选项数 11 vs 4 的差异）。答案位置影响指标（选项距提交按钮远时 RT/距离更大）。

### 4.15 因果性 / 构念效度
manipulated-difficulty + prediction 范式；难度是操纵的自变量、模型预测实验分组。坦诚混淆：只操纵未测量难度、不同操纵与不同题混淆。

### 4.16 迁移到我们的英语阅读系统
- **可直移**：9 项 mouse 指标 + mousetrap 管线；personalization 范式（baseline 回归取残差——增益依任务而异 +1.2~4.9pp，选项位置校正另有贡献）；嵌套 CV + 树模型优先；特征重要性分析。
- **要改造**：难度 GT 需自定（我们的 ground truth 可用答题正确性/自报难度，比实验条件更硬）；hover 阈值需重调；右栏 question 面板独立滚动 → 选项位置/滚动距离的混淆需显式建模；我们可引入 click/划线/划掉（本文明确未用 click）。
- **不可移**：任何 spatial attention / gaze location 推断——本文无眼动，结论只到 difficulty。

### 4.17 这篇论文不能确立什么
- **不能证明 cursor=gaze / mouse→visual attention location**。
- 不能证明实时干预有效（只离线预测）。
- 不能证明 mouse 可"可靠"预测难度（最高 65.9%，作者自认操纵强度不足以可靠预测）。
- 未报告采样频率/坐标系，无法复现采集层。

---

## 5. C4 — Mouse Tracking for Reading (MoTR)（Wilcox et al., 2024）

**定位：reading-specific mouse tracking。核心：MoTR 通过界面设计人为强制 mouse 与当前阅读位置 coupling。**

### 5.1 研究问题
提出浏览器可部署的词级渐进加工测量工具 MoTR，验证其能否以低成本、可线上部署获得**词级阅读时间与 scanpath**，且效度接近眼动追踪：实验 1 问能否用于自然阅读（Provo 语料），实验 2 问能否测到句法附着偏好（定向心理语言学效应）。

### 5.2 任务 / 环境
- **强制耦合界面（核查点）**：文本模糊、仅 mouse 尖端附近小区域清晰——"text, which is blurred except for a small region around the tip of the mouse. **Participants must move the mouse to reveal and read the text.**"（Abstract, PDF p.1）。"The purpose of the text blur... the blur was necessary to obfuscate enough material so that the participant must move the mouse to reveal the text"（PDF p.4）。spotlight 模拟 foveal/parafoveal 视野（渐变模糊，右侧约 5 字母全清晰 + 4 字母部分；左侧约 2 字母）。
- 读完后按底部按钮 → 移除 spotlight → 回答理解问题（必答）→ 下一屏。
- 实验 1：Provo 语料，3 个 sub-experiment；实验 2：附着偏好材料（adverb/coordination/relative clause），3 个 sub-experiment，各 59 items、平均 14 分钟。
- 界面参数：spotlight 宽 102px；光标偏置（左缘 39px/右缘 63px）；双倍行距；CSS blur 半径 3.5px；**sampling 20 Hz**（实测样本间隔 50.1±7.1ms）。

### 5.3 被试
- 实验 1：MoTR 101 采集/9 剔除（理解题 <80%）→ 隐含 92；BSPR 90/13 剔除 → 隐含 77。Prolific 招募、英语母语、IP 美国、台式机。
- 实验 2：240 招募→197 数据→187 分析；每条件 8×187=1496 obs。年龄/性别 NOT REPORTED。

### 5.4 原始鼠标数据
时间戳 + spotlight（略偏置的 cursor）x/y 屏幕坐标；不记录 click/hover；采样 20Hz；单屏文本无滚动。

### 5.5 眼动数据
本论文**不采集**眼动，但复用既有眼动语料作对照：实验 1 用 Provo 语料先前 84 名英语母语者眼动数据；实验 2 对照 Witzel et al. (2012) 眼动数据。无同步眼动-鼠标联合采集。

### 5.6 注意真值
GT 不是 "attention"，而是**词级阅读时间**与扫描路径。把 spotlight 覆盖某词的时间段称为 "attentional association"，"analyzed as a proxy for gaze"。验证真值 = 眼动阅读时间（gaze duration / go past / total duration / 回归/跳读概率）+ 实验 2 的操纵难度。

### 5.7 鼠标预处理
- association 提取：每个时间戳的 spotlight 位置关联最近词；连续同词样本合并为 association。
- 阈值：fmin=160ms（探索 120–240）、fmax=4000ms；覆盖 <20% 词数的试次剔除（skim）；理解题 <80% 剔被试；无平滑/重采样细节、无个人归一化。
- 度量族：gaze duration（首个 association）、total duration（全部 association）、go past time、FPAsc/FPReg（首遍关联/回归概率）。

### 5.8 鼠标特征
非 ML 特征；从 association 计算眼动类比度量（gaze/total/go past duration、回归/跳读概率）+ 运动类型五分类（true fixation / deceleration / constant velocity / acceleration / offscreen，δ=0.001 px/ms）。

### 5.9 Mouse ↔ Gaze 关系
无同步采集、无 per-sample 对齐。仅词级聚合相关（cross-participant 平均）：
- MoTR↔眼动相关：gaze duration 0.51、go past 0.42、total duration 0.62、回归概率 0.19、跳读概率 0.80（对比 BSPR 0.35/0.26/0.40；眼动 split-half 上界 0.75/0.63/0.81/0.58/0.91）。
- 回归触发词重叠：**98% 的 MoTR 回归触发词也是眼动回归触发词，但眼动回归触发词仅 38% 被 MoTR 捕获**（高精度低召回）——回归在 MoTR 中更难发起。
- MoTR 阅读时间相对眼动系统性右偏（更长）。

### 5.10 模型
贝叶斯统计：相关分析（Behseta 2009）、GAM（surprisal/freq/length→RT）、多层模型（实验 2，by-item/by-subject 随机效应）；对比 BSPR 自采 + Boyce et al. (2020) 的 A/G-maze/SPR。

### 5.11 预测目标
词级阅读时间（gaze duration / total duration / go past）与回归/跳读概率；实验 2 预测 RT 与 FPReg 作为 condition 的函数。**不是** attention score / 不是 spatial 分类。

### 5.12 评估
- 相关 + 95% CrI（表 1）；surprisal–RT 线性（ΔELPD 线性优于非线性）。
- 实验 2 效应量（critical 区 RT 差异 + 95% CrI；adverb/coordination/relative clause）。
- 功效分析：adverb 80% power 需 ~40 人、RC/coordination ~140 人；MoTR 敏感度介于 SPR 与 maze 之间。
- 分析层面：cross-participant 词级平均（同 Smith & Levy 2013）。

### 5.13 个体差异
运动类型个体差异大："we observe a handful of participants whose behavior is similar to eye-tracking... However, the median participant is relatively well-balanced between the five types of movements"（PDF p.7）。无 personalization 建模。

### 5.14 任务依赖
回归策略随语言现象变化（adverb/RC 即时回归、coordination 句末回归）；true-fixation 比例 item 间 16–34%（平均 23%）。耦合机制（blur）在所有条件恒定。

### 5.15 因果性 / 构念效度
correlate + manipulated-difficulty。明确承认构念假设："coordinates of the cursor are analyzed as a proxy for gaze"（PDF p.4）；"One additional benefit of the cursor is that it may direct participant gaze during reading, **although we do not test this experimentally**"。未做无 blur 对照、未排除"鼠标运动只是 UI 强制行为副产物"。

### 5.16 迁移到我们的英语阅读系统
- **可直移**：attentional association 概念与实现（把 cursor 停在某词附近的连续时长合并为词级时间）；词级阅读时间度量族 + 首遍关联/回归/跳读定义；质控过滤（理解题 <80%、<20% 覆盖试次、fmin/fmax）；运动类型五分类；贝叶斯相关/层次模型/功效分析方法。
- **要改造**：词与 mouse 的空间关系需自定（我们无 spotlight）；fmin/fmax、spotlight 直径需按我们字号重标定；需显式区分"mouse 移动是滚动/划词等操作行为"。
- **不可移（核心边界）**：**MoTR 的效度数字建立在"必须移动 mouse 才能读"的强制耦合上**；我们系统用户可不动 mouse 阅读，`mouse≈reading position` 不成立，0.51–0.62 相关只能作为**强制耦合条件下的上限**参考。其"回归高精度低召回"结论也提示我们的回归信号推断会更弱。

### 5.17 这篇论文不能确立什么
- **不能证明自然网页（无 blur）中 cursor=reading position**（耦合是界面制造的；未做无 blur 对照）。
- 不能证明 mouse 阅读时间可复现眼动回归行为（MoTR 回归率 4% vs 眼动 15%，相关 0.19，仅捕获 38% 回归触发词）。
- 不能证明 mouse 信号达到眼动的时间/空间精度（无同步对照、阅读时间右偏）。
- 不能证明光标引导注意力（"we do not test this experimentally"）。
- 不能外推到非英语/拉丁文字。

---

## 6. C5 — Virtual Finger-Point Reading Behaviors（Kirsh, 2022）

**定位：自然网页阅读中的 Pointer-Assisted Reading（PAR）——大规模 web analytics 观测研究。**

### 6.1 研究问题
从自然网页日志的大规模统计中研究 mouse 移动**方向与速度**的规律，并论证它们与文本阅读（PAR）相关。核心贡献是发现 PAR（cursor 当"虚拟手指"沿文本读）。

### 6.2 任务 / 环境
- **无实验任务**：公开技术文档网站（ObjectDB，Java Persistence API 教程）自然浏览阅读；匿名、无登录、read-only。
- **完全自然交互**；无眼动、无强制 mouse 使用。
- 137 个结构相似教学页；数据采集 6 个月（至 2020 年 6 月）。

### 6.3 被试
**NOT REPORTED**（匿名访客）。估计 ~375,569 独立访客（浏览器指纹，作者自认偏高）。无招募/众包/人口学。

### 6.4 原始鼠标数据
- 只记录 mouse move 事件（时间、x/y、页面区域）；click/scroll/keypress 未采集。
- **采样：最多 10 events/second**。
- 数据规模：**90,367,657 个 mouse move 事件 / 1,139,284 次页面浏览**；排除无移动 pageview → 1,015,587，平均每 pageview 89 个样本（8.9 秒移动）。

### 6.5 眼动数据
**NO EYE-TRACKING GROUND TRUTH。**

### 6.6 注意真值
不直接测量 attention。分析对象是**阅读行为（PAR）**，潜在假设"cursor 沿文本移动≈阅读位置"建立在**转引**前人 gaze-cursor 相关性文献（[6,14,31]）之上，非本数据实测。GT 类型 = implicit assumption。

### 6.7 鼠标预处理
- client-side 10Hz 上限；movement = 同方向（12 个 30° 扇区之一）+ 相邻间隔 ≤5s（作者自认任意）的连续序列；最小长度过滤（≥3/≥5/≥10 moves）；无重采样/平滑/归一化/personalization。

### 6.8 鼠标特征
描述性统计量：方向（4 扇区 Right/Up/Left/Down ±45° 与 12 扇区）、速度（px/s）、movement 大小（moves 数）、位置区域（content/left menu/top menu/elsewhere）。无 ML 特征。

### 6.9 Mouse ↔ Gaze 关系
无自有 gaze。仅转引："Previous work has shown a correlation between eye gaze and mouse cursor positions on a screen [14], and the correlation is higher during mouse activity [6,31]"（PDF p.2）。

### 6.10 模型
**NONE**（纯统计描述 + 定性轨迹分析；Fisher's exact test）。

### 6.11 预测目标
**NONE**。

### 6.12 评估
无分类/回归指标。唯一显著性：up 21.1% vs down 19.7%（Fisher's exact p<0.00001）。作者："the interesting question is not about statistical significance, but which observed differences indicate something meaningful"（PDF p.3）。

### 6.13 个体差异
证据弱：PAR 非人人用（鼠标移动 <2% 页面可见时间）；"the accuracy of PAR is varying"（tight vs loose）；开放问题——PAR 用户比例、horizontal-movers vs vertical-movers 分布。无 per-user 统计量。

### 6.14 任务依赖
内容区占 ~91.9% 的鼠标活动（content 83,017,547/90,367,657）；6 个流量最高国家方向/速度模式一致；阅读方向（LTR）解释右移慢、210° 方向对应"行尾回行首"；up>down 归因于滚动后光标上移回阅读位置。

### 6.15 因果性 / 构念效度
correlational/observational + 定性示例。方向-速度与阅读的关联靠三点间接论证：转引 gaze 相关性、右移峰值速度≈阅读速度（150–200px/s ≈ 180–240 wpm）、示例轨迹。作者承认 loose PAR 匹配困难（PDF p.14）。

### 6.16 迁移到我们的英语阅读系统
- **可直移**：概念层——方向+速度统计携带阅读信号；慢速右向水平移动≈跟随阅读、竖向移动≈标记行；PAR 方向模式跨国家一致（对环境稳健）。
- **要改造**：速度阈值（150–200 px/s、>600px/s）依赖其站点字号（约 49.7 px/word）需重标定；单栏布局 vs 我们双栏独立滚动；斜向速度解释、左右不对称百分比（72.3%）是聚合常量不可搬为通用阈值。
- **不可移**：无 per-user PAR 识别器（future work）；不能把光标"划过单词"当该词被阅读的强证据（loose PAR 匹配难）；无眼动 GT，无法支撑个体级 cursor→attention 量化。

### 6.17 这篇论文不能确立什么
- 未量化"多少用户使用 PAR"（开放问题）；只定性称 PAR "uncommon"、鼠标移动 <2% 页面时间。
- 未提供自动化 PAR 识别/分类方法（future work）。
- 未在自有数据建立 cursor=gaze 量化关系（全部转引）。
- 未证明方向/速度统计能对**个体**可靠识别阅读（所有百分比是 pageview 级聚合）。
- 未做单词级阅读内容验证；未覆盖 RTL 语言；未报告设备（mouse vs touchpad）占比。

---

## 7. C6 — A Versatile Dataset of Mouse and Eye Movements on SERPs（Latifzadeh, Gwizdka & Leiva, 2025）

**定位：mouse + eye tracking objective ground truth 的数据集论文（AdSERP）。**

### 7.1 研究问题
此前 mouse→注意工作依赖 post-task 自报 GT（"can be inaccurate and prone to biases"）；缺少「以眼动为客观标签、可用于训练 mouse 注意力预测模型」的公开大规模 SERP 数据集。贡献：(1) 大规模 in-lab 双模态数据集；(2) 复现既往 SERP 交互发现；(3) 以眼动 fixation 标签训练的 mouse attention baseline。

### 7.2 任务 / 环境
- **事务性查询**：给产品标题 + 对应查询（"buy" + Amazon Product Reviews 语料生成），要求想象购买并浏览 SERP、1 分钟内点击"通常会选择的元素"并确认。
- **natural interaction**（明确把"要求鼠标刻意跟随眼动"列为他人研究缺陷）。
- 静态 Google SERP（每 SERP 仅被一名被试看）；全屏 Chrome；平均 trial 22.16s（SD 13.20、中位 20s）；**主实验 6 blocks × 10 trials**（C6 原文 "The main experiment consisted of six blocks per participant"；C7 说明共 8 blocks、前 2 为 warm-up 不分析，故主实验 6 块；47×60−44 malformed = 2,776 ✓）；block 间休息 ≥1 分钟；每 block 前重校准眼动仪。

### 7.3 被试
**N=47（27M/20F）**；年龄 19–44（M=29.66, SD=6.46, Mdn=29）；University of Luxembourg mailing lists + flyer；英语 ≥B2（CEFR）；书面知情同意、20 EUR；伦理 ID 'ERP 21-055'。国别未报告。数据集 **AdSERP 公开发布于 Zenodo**（https://zenodo.org/records/15236546），预处理脚本于 GitHub（MIT 许可）；数据含源 HTML/CSS、SERP 截图（多配置）、mouse/eye 事件、AOI 边界文件。

### 7.4 原始鼠标数据
- 格式 `(t, x, y, e, xpath)`——时间戳、光标位置（相对屏幕左上角）、事件（scroll/mousemove/click）、相关 DOM 元素 xpath。
- 采集：evtrack 库；**采样频率 NOT REPORTED**。
- 设备：Dell MS116 鼠标。另有每 trial XML log（screen/window/document）。

### 7.5 眼动数据
- **Gazepoint GP3 HD，150 Hz**；原始 `(t, x, y, p_r, p_l)`（瞳孔径）。
- Fixation `(t, x, y, d)`：相对截图左上角像素；**<100ms 过滤**；注视提取算法 NOT REPORTED（Gazepoint Analysis 软件导出）。
- AOI：**"slot boundaries"**（广告 bounding box），由 DOM 程序化提取（Python + Selenium），`(x,y,w,h)` 相对截图；可提取细粒度元素（DD 广告的图片/价格；organic 的链接/描述/评分/评论）。校准：每 block 前重校准。

### 7.6 注意真值
**客观眼动 fixation**："use an eye tracker to construct an objective ground-truth of continuous visual attention"。
- `Attention_trial = Σ Fixation_Duration_AOI / Σ Fixation_Duration_total`（0–1，隐含次数与时长）。
- `label_trial = 1 if Attention_trial > τ`（τ=中位数）。
- 发布标签/基线 = trial 级二值（目标广告是否吸引注意）。

### 7.7 鼠标预处理
建模前 Mouse2Vec 输入**重采样到 20Hz**；轨迹取前 5/10/15/20s，短 pad / 长截断；fixation <100ms 过滤。无平滑/去噪/personalization 报告。

### 7.8 鼠标特征
- Mouse2Vec 嵌入（128-dim / 5s 窗口）+ AOI bbox (x,y,w,h)；
- 时序原始坐标 (x,y) + bbox（给 GRU）。
无手工特征（作者自述 GRU 做 automatic feature extraction）。

### 7.9 Mouse ↔ Gaze 关系（有量化）
- **Mutual Information**：0.02（right-align DD+organic）/ 0.01（仅 organic）/ 0.06（left-align DD+organic）；布局间不显著（F(2,2644)=0.81, p=.4451）。
- **KL divergence**：19.89 / 21.90 / 17.27；布局间显著（F=11.93, p<.0001）；post-hoc：**仅 organic 广告的 SERP 上 eye-mouse 分歧最大**。
- **平均欧氏距离 372.89px（SD=293.78, Mdn=329.83）——约为 Huang et al. (M=178, SD=139) 的两倍**；Δx/Δy 都在 0 附近有峰，但 **Y 轴距离大于 X 轴**。
- lag：NOT REPORTED。

### 7.10 模型（基线）
SVM / k-NN（Mouse2Vec）+ GRU（时序，hidden 150、dropout 0.25、Adam、100 epochs、early stopping）。70/30 分层划分（DD 2,443：1,710/733；organic 2,647：1,853/794）。

### 7.11 预测目标
**trial 级二值**：目标广告是否吸引注意力（由 Eq.1+Eq.2 定义）。不是 element-level、不是连续 score。

### 7.12 评估
- **最佳：GRU 前 5s → F1=93%（organic）/73%（DD）**；AUC organic 0.97（5s）。
- 表 3（DD）：GRU 5s 0.70/0.78；10s 0.73/0.82（DD 最优）；15s 0.72/0.77；20s 0.69/0.74。SVM/kNN 更低。
- **与自评 GT 对比**：同一 GRU 在 Attentive Cursor Dataset（自评）上 F1=56%/69%；本数据集 93%/73%——"self-reported labels are noisier than fixation-based labels"。
- held-out（70/30），非 within/cross-user 报告。

### 7.13 个体差异
NOT REPORTED（无 per-user 建模/personalization）。相关工作中转述 eye-mouse 协调随 task/scroll 变化。

### 7.14 任务依赖
布局依赖：MI/KL 随 ad 布局变化（仅 organic 分歧最大）；注意分配依赖布局（DD 广告"capture user attention in much larger proportions than previously known"）；前 5–10s 轨迹足够预测注意；点击 82.42% 落在非广告元素。

### 7.15 因果性 / 构念效度
correlate/measurement；无因果。attention 以注视时长占比定义（引用"longer fixation durations correspond to higher attentional focus"）；<100ms 过滤对齐文献。

### 7.16 迁移到我们的英语阅读系统
- **可直移**：Attention_trial 公式（AOI 注视占比）可复用于段落/选项 AOI；前 5–10s 轨迹预测注意的做法；fixation <100ms 过滤 + 中位数 τ；DOM/xpath 关联事件（天然 element-level）。
- **要改造**：坐标基准不同（gaze 相对截图、mouse 相对屏幕）——滚动长文需统一坐标、处理滚动位移；静态单屏 SERP 无双栏/滚动/划线交互，事件语义需重新定义；事务性购买任务 vs 阅读理解差异大。
- **不可移**：只有 trial 级二值广告预测，**不能**据此声称可做 element-level continuous attention prediction；DD 广告 AUC 仅 0.71–0.82 提示高竞争区域（如选项区）信号衰减。

### 7.17 这篇论文不能确立什么
- **不证明 cursor=gaze**：平均距离 372.89px、MI 0.01–0.06、KL 17–22——mouse 是弱、强依赖布局与轴方向的 attention 代理。
- 不证明可预测逐 element / 连续 attention（标签是 trial 级广告二值）。
- 未给注视提取算法/参数、鼠标采样率、eye-mouse 同步方法（复现缺口）。
- 未覆盖 trackpad/mobile；总时长未报告。

---

## 8. C7 — AdSight（Villaizán-Vallelado et al., 2025）

**定位：cursor trajectory → eye-tracking-derived attention（multi-slot sponsored search）。**

### 8.1 研究问题
把"注意力量化"显式化为两个 ML 任务：(1) 回归——cursor 轨迹能否预测 SERP 槽位的 TFT（总注视时长）/TFC（总注视次数）？(2) 分类——cursor 轨迹能否判断用户是否注意到某类 slot？

### 8.2 任务 / 环境
与 [C6] 相同：47 被试、事务性查询（"buy"+Product Reviews）、静态 Google SERP、8 blocks×10 trials（前 2 为 warm-up）、block 前重校准眼动仪、1 分钟/ trial 点击+确认。**natural interaction**。

### 8.3 被试
N=47（20F/25M；[C6] 报 27M/20F——性别数字小出入，见 §19）；年龄 19–44（M=29.66, SD=6.46）；mailing lists 招募、20 EUR。

### 8.4 原始鼠标数据
格式 `(t, x, y, e)`（e 为鼠标动作如 hover/click；[C6] 实际多 xpath）；**异步事件流，采样频率 NOT REPORTED**；坐标相对屏幕左上角，进模型前归一化到 [0,1]（viewport）；Dell MS116 鼠标。

### 8.5 眼动数据
**Gazepoint GP3 HD，150Hz**；17" Dell 1280×1024 60Hz；fixation `(t,x,y,d)`；**<100ms 过滤**；AOI = slot boundaries（ad blocks bounding box）。同步方式 NOT REPORTED。

### 8.6 注意真值
**objective eye-tracker fixations**："for both the regression and classification tasks, the ground truth is obtained from the eye-tracker's fixations"。
- 回归目标：**TFT**（slot 上总注视时长）/ **TFC**（总注视次数）；
- 分类标签：把 slot 内长 fixation 聚成 cluster，以 TFT/TFC 的**中位数**为阈值二值化（fixation 率 42%/46%/44%/29% per slot 类）。

### 8.7 鼠标预处理
x/y 归一化到 [0,1]；LSTM 输入固定 250 timesteps（pad/截断），Transformer 变长；无连续重复坐标；无平滑/去噪/personalization。

### 8.8 鼠标特征（每 timestep 4 个）
1. cursor coordinates (x,y)（viewport 归一化）；
2. 每个坐标停留时间；
3. **slot type at position**（−1..3：非 slot/direct-top/direct-right/organic-top/organic-bottom）；
4. **normalized sequence index**（轨迹时序位置）。
特征重要性：**sequence index 最关键**（移除→MSE 3.16 vs 基线 2.94）；slot type 次之（→3.10）；time（→3.05）。Slot metadata：归一化中心 (x_c,y_c)+type 最优；移除 type 影响最大。辅助 AOI：N=3 最优（MSE 2.94）；α=0.33 最优（2.86）。

### 8.9 Mouse ↔ Gaze 关系
NOT REPORTED（AdSight 内部无对齐/lag/AOI 一致分析；仅转引 "mouse movements are considered as a reasonable proxy for user's gaze, especially on SERPs"）。

### 8.10 模型
**Encoder-Decoder Transformer（Seq2Seq）**：encoder 处理 cursor 轨迹 embedding；decoder 输入 slot metadata + encoder 输出；共享 MLP readout 逐 slot 预测。Cursor embedding：共享 MLP + BiLSTM 或 Transformer encoder（l∈{16,32,64}）或 ViT（冻结+微调）。Loss：MSE 或 Listwise Rank Loss（auxiliary slots 用 α 加权）。Adam + Optuna 贝叶斯优化 + 3-fold CV。Baselines：MLP readout、以及 [C1] 的 BiLSTM/ResNet50 复现。

### 8.11 预测目标
- 回归：每 slot 的 **TFT（秒）或 TFC（次数）**（输出数 = SERP 槽位数，随 trial 变）；
- 分类：4 个二分类——用户是否注意到某 **slot 类**（direct-top/right、organic-top/bottom）。由于 **"only 31% of trials contain a direct-right slot"**，采用统一模型同时输出四个分数，而非四个独立模型（PDF p.7）。

### 8.12 评估
- **回归（表 1，Seq2Seq+Transformer）**：TFT MSE **2.86**±0.02（≈1.69s RMSE）/ NDCG 96.07；TFC MSE 50.07/NDCG 96.36。MLP baseline：4.99/82.36（TFT）。Wilcoxon：Seq2Seq>MLP 全组合 p<.05；Seq2Seq+Transformer 恒优于次优 p<.05。
- **分类（表 2，Seq2Seq+Transformer）**：平均 **AUC 81.24/F1 76.25**；per-class Direct-Top 80.79/73.90、Direct-Right 81.72/75.07、**Organic-Top 71.87/67.27（最弱）**、Organic-Bottom 85.85/82.57。MLP baseline 71.95/66.67；**C1 模型复现仅 66.20/63.29（BiLSTM）、68.29/62.48（ResNet50）**。
- slot 顺序无关性：任意顺序 MSE 2.9±0.03/NDCG 95.8±0.02。
- 划分方式未明说 within/cross-user。

### 8.13 个体差异
NOT REPORTED（无 per-user 分析、无 personalization）。

### 8.14 任务依赖
slot 类调节性能（organic-bottom 最好 85.85、organic-top 最差 71.87）；时序表示在 direct-top/right 更优、视觉表示在 organic-bottom 更优；auxiliary slots 提升性能。

### 8.15 因果性 / 构念效度
纯 predict/correlate；GT 客观（眼动）但只做相关性预测。"attention" 操作化为 TFT/TFC 与 cluster 二值标签。自述首创性表述"we are the first to introduce this methodology"与 [C6] 已用 fixation-AOI 标签训练 baseline 存在张力（见 §19 E 项）。

### 8.16 迁移到我们的英语阅读系统
- **可直移**："轨迹→区域标量注意力"的 Seq2Seq 框架（把 passage/question/选项当 slot）；auxiliary AOI 增强训练（N=3、α≈0.33）；"是否注意到某区域"分类建模；真实眼动 fixation 为 GT + <100ms 过滤。
- **要改造**：坐标定义——AdSight 是静态全屏 viewport 像素，我们 passage 独立滚动会破坏 slot 边界与坐标对应，需按滚动位置动态算 slot 框；slot type 需替换为 passage/question/option/line 语义类别；LSTM 250 timesteps 与 transformer 变长策略可沿用但分布不同。
- **不可移**：所有具体数值只对 Google SERP 事务搜索成立；未涉及阅读/滚动/双栏；未建立 cursor=gaze（proxy 是引用的）。

### 8.17 这篇论文不能确立什么
- **不是独立 replication**：使用 [C6] 同一数据集（47 人、2,776 trials、同 SERP/眼动仪/mouse 日志）；贡献是建模方法。
- 未建立 cursor=gaze（无 eye-mouse 对齐分析）。
- 未建立跨布局/跨任务泛化（仅 Google SERP 事务型）。
- 1.69s 是 RMSE（√MSE）非 MAE；回归无 random/naive baseline。
- 未报告被试/页面层面泛化（within/cross 未说明）；organic-top 类 AUC 仅 71.87。

---

## 9. C8 — Mouse movements reflect personality traits and task attentiveness（Meidenbauer et al., 2023）

**定位：mouse features → task attentiveness / atypical responding（+ 人格）。研究的是 attentiveness/response quality，不是 spatial visual attention。**

### 9.1 研究问题
"Are mouse movement patterns exhibited in a choice-making task reflective of a person's internal states and traits?"——检验从鼠标行为推断 Big Five 人格，并提出 atypical responding 作为通用不专注/随机作答的测量。

### 9.2 任务 / 环境
- **在线图片评分/选择任务**：每 trial 展示 12 张街道照片，按某属性选 4 张（最喜欢/最不喜欢/可步行性/秩序性/复杂性等）；正常 trial 需 5 次点击（4 选择+continue），attention-check trial 6 次（含拖拽）。
- **natural interaction**（任务要求点击选择，非强制"眼到鼠到"）。
- **attention check**：随机分布在 trials 中，要求把损坏图片拖进垃圾桶；**连续两次失败终止会话**。
- 每 trial 平均完成 14,849ms（SD 6,717）。

### 9.3 被试
**N=791（清洗后）**：483 M/303 F/5 Other；平均 38.8 岁（SD 10.8）。AMT 招募（CloudResearch/TurkPrime）；芝加哥大学两项研究合并。清洗前原始 N 未报告。

### 9.4 原始鼠标数据
- jQuery 采集，**约 60Hz（每 17ms）**，"a record is created whenever a movement occurs"。
- 每条 4 字段：timestamp(ms)、x、y、dummy-coded click。
- 坐标像素；无 viewport 归一化报告。

### 9.5 眼动数据
**NO EYE-TRACKING GROUND TRUTH**（全文无眼动、无 AOI）。

### 9.6 注意真值
"attention/attentiveness" = **session/task 级作答规范度**，操作化为 **atypical responding**：
- `Abs_Area_Under_Curve = |AUC − 0.5|`：对每被试，将其对每张图的选择（click or not）与群体平均选择做 leave-one-out ROC 得 AUC；偏离随机（AUC≈0.5）越远越异常。ρ=0.86 的评分者间信度保证"偏离群体=不专注"的合理性。
- **attention check 是数据质量门**（连续两次失败终止会话），Abs_AUC 才是进入分析的投入度指标。
- **不是 spatial visual attention**（无眼动、无位置语义）。

### 9.7 鼠标预处理
- 特征在**被试层面跨所有 trials 聚合**（Total_/Avg_ 前缀）。
- 阈值：**long pause = 静止 >4s**；**fixation = 25px 内微运动持续 >250ms**。
- 无个人 baseline 归一化（除按被试聚合）；PLS 前 z-scoring。

### 9.8 鼠标特征（11 个）
- Time：Total_pause_cnt、Avg_fixation_dur、Avg_agg_fixation_dur、Avg_fixation_cnt；
- Activity：Avg_euc_dist、Avg_euc_speed（ms/像素）、Avg_completion_time；
- Click：avg_click_att、reclick_percent_att、avg_click_norm、reclick_percent_norm。
第 12 变量：Abs_Area_Under_Curve。

### 9.9 Mouse ↔ Gaze 关系
**NOT REPORTED**（无 gaze）。

### 9.10 模型
Pearson 相关 + OLS（11 mouse + Abs_AUC 预测各 Big Five）+ **三套 PLS（multiverse）**（对 X（人格 791×5）与 Y（mouse 791×11）协方差矩阵 SVD；置换检验 10,000 + bootstrap 10,000 + e² 效应量）。**无 train/test、无 held-out 预测验证**。

### 9.11 预测目标
用鼠标特征预测 Big Five 特质与 Abs_AUC（投入度）——是关联/解释，非严格预测验证。**注意**：文中 AUC = atypical responding 的 ROC AUC（预测对象），与 ML 性能 AUC 完全不同。

### 9.12 评估
- 单变量（Bonferroni）：**click 类特征与 Abs_AUC 显著负相关**（全部 p<0.001）：avg_click_att r=−0.18、reclick_percent_att r=−0.19、avg_click_norm r=−0.17、reclick_percent_norm r=−0.17；**fixation 次数正相关 r=0.11（p=0.002）**。
- OLS 预测 Big Five：**R² 仅 0.03（Neuroticism）–0.08（Conscientiousness）**。
- PLS：LV1 显著（p=0.001，解释 91% 协方差）；效应量 model r=0.29/0.38/0.22、e² mouse 0.64–0.72。
- 无 held-out/预测性能指标。

### 9.13 个体差异
论文主题即个体差异（人格）。鼠标特征聚合到被试层与人格显著关联；提出用因子载荷预测未来用户特质轮廓（PDF p.11）——personalization 的前瞻提议，未做 held-out 验证。设备差异未记录（touchpad vs mouse 列为局限）。

### 9.14 任务依赖
作者明确承认任务依赖："the specific mouse movement patterns or traits of interest may be different depending on the task context"（PDF p.11）；加入 Age/Gender 会改变 PLS 模式。

### 9.15 因果性 / 构念效度
correlate/associate（PLS 协方差 + 相关 + OLS），无因果、无预测验证。对 Abs_AUC 的构念效度有明确保留（"additional work is needed to fully establish whether this measure of atypical responding does indeed reflect inattentiveness"）。未预注册。

### 9.16 迁移到我们的英语阅读系统
- **可直移**：click 类特征（avg_click_norm、reclick_percent）与异常/不专注作答的负相关逻辑——对选项的多余/反复点击可作为不投入/犹豫信号；pause >4s、25px/>250ms fixation 阈值**只能作为 candidate operationalization，必须按我们界面的字号/布局/任务重标定**（它们来自图片选择任务 + 特定设备，不是 universal cognitive boundary）；"偏离期望作答"的注意度量思路（我们有正确答案作 GT，比 group-average 更硬）；PLS/multiverse 稳健性检验模板。
- **要改造**：被试级聚合需下放到 trial/内容块级；atypical responding 需换成任务正确答案/专家标注。
- **不可移 / 不能引用为**：不能作为"cursor 位置≈视觉注意位置"的证据（无空间成分、无眼动）；图片选择任务与文本阅读/答题界面差异大。

### 9.17 这篇论文不能确立什么
- **不能证明 cursor=gaze / 光标位置反映视觉注意位置**：无眼动、无 spatial 分析；"task attentiveness" 是任务级作答规范度。
- 不能证明 Abs_AUC 就等同于不专注（论文自己声明尚需验证）。
- 不能证明"预测人格"的实用精度（无 held-out；R² 仅 0.03–0.08）。
- 不能把"click 注意追踪比眼动更有效"归为本研究结论（那是转引 Egner et al. 2018）。
- 不能推广到文本/阅读类任务（仅图片选择；作者承认任务依赖）。

---

## 10. 跨论文对比矩阵

| 论文 | GT 类型 | 眼动 | 生态效度（B 轴） | 领域相似度（C 轴） | N / 样本 | 任务 | 模型 | 预测目标 | 关键结果 | 个体差异 |
|---|---|---|---|---|---|---|---|---|---|---|
| [C1] Arapakis 2020 | 自评（post-task 5 点 Likert→二分类） | 无 | MEDIUM（自然交互，但众包单任务、页面被仪器化、仅 1 广告） | LOW–MEDIUM（SERP 广告） | 3,206 众包；2,289 sessions | 事务性搜索 + 点击 | RNN/CNN 表示学习 | "是否注意到广告"（session 级二分类） | 最优 AUC 0.739 / F1 0.731（ResNet50, trajectory 表示）；CNN>RNN；ad format 显著调节 | 未建模 |
| [C2] Huang 2012 | 眼动 gaze 位置 | 是（Tobii x50, 50Hz） | MEDIUM（实验室自然搜索） | MEDIUM–HIGH（web search，含阅读行为） | 36 被试（38 招募），32 任务 | Bing 搜索（导航+信息型） | 多元线性回归 | gaze 位置（x/y） | RMSEd 236.6→181.1 px（−23.5%）；cursor 滞后 700ms；inactive 58.8%/233px | 个体差异最强（SD 33.9>20.2） |
| [C3] Fernández-Fontelo 2023 | 实验操纵难度条件 | 无 | HIGH（真实网络调查，自然作答） | LOW–MEDIUM（问卷作答） | 886 用鼠标者→501–551/题 | 德国就业面板网络调查 | LR/树/SVM/NN（嵌套 CV） | 难度条件（easy/difficult 二分类） | accuracy 58.9–65.9%；mouse 优于 RT-only（+1–3pp）；personal baseline 校正 +1.2~4.9pp（依题而异）+ 位置校正额外增益 | personal baseline 差异被证实，增益依任务而异 |
| [C4] Wilcox 2024 | **MEDIUM–HIGH**（词级阅读时间，对照眼动语料） | 对照（Provo 眼动语料） | **LOW**（强制鼠标-阅读耦合） | **HIGH**（研究的就是文本阅读，领域与我们高度相似；但交互方式不同——强制耦合） | Exp1 101 MoTR/90 BSPR；Exp2 187 | 模糊文本 + spotlight 强制 mouse 读词 | 贝叶斯相关/GAM/层次模型 | 词级 RT、回归/跳读概率 | MoTR↔眼动 RT 相关 0.42–0.62；回归概率 0.19（低） | 运动策略个体差异大 |
| [C5] Kirsh 2022 | 隐式假设（cursor≈阅读，转引 gaze 文献） | 无 | HIGH（纯自然网页浏览） | HIGH（在线学习网站内容阅读） | ~90M mouse events；~375K 估计访客 | 自然浏览技术文档 | 无（聚合统计） | 无（描述性） | 水平>垂直、右>左、右慢左快（150–200px/s≈阅读速度）；PAR | PAR 松紧个体化；非人人使用 |
| [C6] Latifzadeh 2025 | 眼动 fixation→AOI 标签 | 是（Gazepoint GP3 HD, 150Hz） | MEDIUM（lab 受控，自然交互） | LOW–MEDIUM（SERP 广告 AOI） | 47 被试；2,776 trials | 事务性 Google 搜索 | GRU/SVM/kNN（baseline） | trial 级广告注意二分类 | F1 93%（organic）/73%（DD）；自评 GT 上同模型仅 56/69% | 未建模 |
| [C7] Villaizán 2025 | 眼动 fixation→slot TFT/TFC/noticed | 是（Gazepoint GP3 HD） | MEDIUM（lab 受控） | LOW–MEDIUM（SERP 多广告槽） | 47 被试；2,776 trials（=C6） | 事务性 Google 搜索 | Seq2Seq Transformer / ViT | slot 级 TFT/TFC（回归）、slot 类 noticed（分类） | TFT MSE 2.86/NDCG 96；分类平均 AUC 81.24 | 未建模 |
| [C8] Meidenbauer 2023 | atypical responding（偏离群体作答） | 无 | HIGH（在线图片任务，自然作答） | LOW（图片选择非文本阅读） | 791（清洗后） | AMT 在线图片评分/选择 | PLS / OLS / 相关 | 人格特质 + attentiveness | click 类特征与投入度负相关 r≈−0.18；R² 0.03–0.08 | 人格即个体差异主题 |

---

## 11. 注意真值矩阵

**这是 C 组最重要的概念表。每一篇的 "attention" 都必须按下面的定义理解，禁止跨论文混用。**

| 论文 | 被称作「attention」的内容 | 真值（GT） | 客观性 |
|---|---|---|---|
| [C1] | "user attention to the ad"（广告注意） | **post-task 自评问卷**（5 点 Likert "你注意到广告到什么程度" → 二分类 noticed/not-noticed，中性丢弃，66% 正类）；页面已不可见时作答 | 主观（事后知觉/记忆） |
| [C2] | gaze 位置 / gaze-cursor alignment | **眼动 gaze 位置**（Tobii x50, 50Hz, 0.5°≈16px）；alignment = 距离/滞后/RMSE | 客观（眼动） |
| [C3] | 不叫 attention——研究 **question difficulty** | **实验操纵的难度条件**（措辞 or 顺序），目标变量 = easy/difficult | 实验操纵（非注意） |
| [C4] | 不叫 attention——研究 **reading position / reading time** | 词在 spotlight 中心的停留（attentional association）；对照 Provo **眼动语料**的阅读时间 | 接口化测量 + 外部眼动对照 |
| [C5] | 不直接测量 attention；研究 **reading behavior（PAR）** | **隐式假设**：cursor 沿文本移动≈阅读位置（转引前人 gaze-cursor 相关性文献 [6,14,31]）；无自有眼动 | 隐式假设 |
| [C6] | "visual attention"（对 SERP AOI） | **眼动 fixation**（Gazepoint GP3 HD, 150Hz；<100ms 过滤）；Attention_trial = AOI 注视时长占比；τ=中位数二值化 | 客观（眼动） |
| [C7] | "user attention"（对 slot） | **眼动 fixation** → TFT（总注视时长）/ TFC（总注视次数）/ cluster 二值标签 | 客观（眼动） |
| [C8] | "task attentiveness"（任务投入度） | **atypical responding**（偏离群体作答的 Abs AUC）；attention check（拖图进垃圾桶）为数据质量门 | 行为（会话级，非空间） |

**判定**：
- 客观眼动 GT：C2、C6、C7（C4 为外部对照）。**其中 C6/C7 同一数据源**（§19）。
- 自评 GT：C1（注意）；C8 的投入度也是行为构造（非眼动）。
- 非注意 GT：C3（难度）、C8（投入度）——**这两篇证明的是 mouse→难度/投入，不是 mouse→注视**。
- 隐式假设 GT：C5（生态证据、无客观 GT）。

---

## 12. 鼠标特征矩阵

**按论文实际使用的特征归类（Spatial / Temporal / Movement / Interaction / Representation Learning）。**

| 特征 | 类别 | 定义/来源 | 论文 |
|---|---|---|---|
| cursor position (x,y) | Spatial | 原始坐标 | [C1][C2][C4][C5][C6][C7][C8] |
| 与 AOI 的距离 / bbox | Spatial | AOI bounding box (x,y,w,h) 拼接 | [C6][C7] |
| hover / 静止时长 | Temporal | inactive ≥1s（[C2]）；hover 阈值 250–3000ms（[C3]） | [C2][C3][C4][C8] |
| dwell time（页载入后） | Temporal | current_t − pageload_t | [C2] |
| response time | Temporal | 页载入到提交 | [C3] |
| initiation time | Temporal | 首次 cursor 移动延迟 | [C3] |
| 词级停留（attentional association） | Temporal | spotlight 覆盖词的时间（fmin 160ms / fmax 4000ms） | [C4] |
| 速度 | Movement | px/s | [C3][C5][C8] |
| 加速度 | Movement | max acceleration | [C3] |
| x/y-flips | Movement | 水平/垂直方向翻转次数 | [C3] |
| 移动距离/轨迹长度 | Movement | 欧氏距离总量 | [C3][C8] |
| 方向 | Movement | 极坐标 4/12 扇区（右/上/左/下） | [C5] |
| click | Interaction | 瞬时事件 | [C1][C2][C6][C8] |
| hover 次数 / 时长 | Interaction | | [C3][C8] |
| click/reclick 次数 | Interaction | 会话级聚合 | [C8] |
| 时间序列 (x,y,t,e) | Repr. Learning | raw trajectory（50 timesteps，[C1]；变长，[C7]） | [C1][C6][C7] |
| 轨迹图像/热图 | Repr. Learning | 5 种视觉编码（heatmap 25px Gaussian / trajectories / 彩色/粗细）；1280×900 PNG | [C1][C7] |
| Mouse2Vec 嵌入 | Repr. Learning | 20Hz 重采样、128-dim/5s | [C6] |
| 未来 cursor 位置 | 未来特征 | 距当前 10s 内最近的后继移动 | [C2] |
| 行为类别标签 | Interaction | inactive/examining/reading/action/click（启发式规则） | [C2] |
| slot type / 时序索引 | Interaction | 类别特征 + normalized sequence index | [C7] |

---

## 13. Cursor 与 Gaze 的对应有多紧密？

**结论先行：point-level（点级）上 cursor 与 gaze 的对齐是**条件性、稀疏**的——平均距离在 178–373 px 之间（因研究而异）、cursor 通常滞后 gaze 约 700 ms、inactive 时段（占 58.8%）几乎无对齐信息；但**行为标签化的 cursor**（action/click）以及 **区域级（region/AOI）聚合**要可靠得多。可以支持 `cursor near P2 → P(gaze in P2) increases` 这种概率推断，**不能**支持 `cursor in P2 → gaze = P2`。**注意："AOI≈paragraph" 是项目迁移假设（C6/C7 的 AOI 是广告槽位），不是 C 组直接验证的结论。**

基于 [C2]（36 被试、32 搜索任务、Tobii 眼动）与 [C6]/[C7]（AdSERP 数据集，47 被试、2,776 事务性查询、Gazepoint GP3 HD），逐问回答：

### 1. 空间距离有多近？
- [C2]：gaze–cursor 欧氏距离在 SERP 上呈宽分布（Figure 1，PDF p.3）；各行为类型下的中位距离为 inactive 233 px / examining 167 px / reading 150 px / action 77 px / click 74 px（Table 1，PDF p.6）。个体平均值从 ~130 px 到 ~280 px（PDF p.4）。
- [C6]：在真实 Google SERP + 事务性查询下，eye–mouse **平均欧氏距离 372.89 px（SD=293.78, Mdn=329.83）**——"[C6] 明确指出这是 Huang et al. [17]（= C2 引用）报告值 M=178, SD=139 的**几乎两倍**"（PDF §5.1，物理页约 5-6）。
- **判断**：点级距离大、跨研究差异大。即便在受控实验室 SERP 上，平均差距也接近两三个文本行宽。**point-level 的 cursor 位置不能直接当作 gaze 位置。**

### 2. 时间上有没有 lag？
- [C2]：用类似 cross-correlation 的方法，把 cursor 序列相对 gaze 平移 50 ms 整数倍后取 RMSE 最低点。**整体 cursor 滞后 gaze 约 700 ms**（Figure 5，PDF p.5）。个体从 250 ms（1 人）到 >1 秒不等，最快的约 350 ms。**"cursor lagged behind the gaze for each individual subject; the inverse situation—gaze lagging behind the cursor—did not occur"**（PDF p.5）——不存在「cursor 领跑 gaze」的用户。
- **对实时推断的意义**：cursor 是 gaze 的**过去式**信号，约晚 0.7 s。实时 focus 推断必须把 lag 考虑进去（例如用「光标最近到达的区域」而不是「当前所在位置」来支持 P(Focus)），且不能期待 cursor 预测 gaze 的即时落点。

### 3. AOI-level alignment 是否比 point-level 更可靠？
- [C6] 的 baseline 实验给出了直接证据：**把 eye-fixation 聚合成广告 slot 的 AOI 标签后，用 cursor 轨迹（前 5 秒）+ AOI bounding box 训练 GRU，F1 达 93%（organic）/73%（DD 广告）**（Table 3/4，PDF p.8）。[C7] 进一步：预测每个 slot 的 TFT/TFC（回归）NDCG ≈ 96，判断用户是否注意某 slot 类（分类）平均 AUC 81.24（Table 1/2）。
- **判断**：区域级（region/AOI）聚合的 cursor→attention 预测比 point-level 的 gaze 位置预测可行得多。这支持我们系统按**区域**粒度（如 passage/question/option 大区域）做 focus 推断。**但 paragraph/选项语义粒度是 PROJECT TRANSFER HYPOTHESIS**——C6/C7 验证的 AOI 是广告槽位，不是段落/题干/选项（详见 §1-4、§25-Q5）。**AOI-level alignment 明显比 point-level 可靠**（但 C6/C7 是同一数据源且未做 participant-disjoint 验证，只能算一次、且限于同分布）。

### 4. 哪类行为时 alignment 最强？
- [C2] Table 1（PDF p.6）：**action（77 px）与 click（74 px）时对齐最紧**；reading（150 px）次之；examining（167 px）再次；**inactive 时最差（233 px）**。时间占比：inactive 58.8%、examining 32.9%、action 5.7%、reading 仅 2.5%。
- **判断**：**主动交互（点击前、点击、划线等目标性动作）时 cursor 离 gaze 最近**；**纯停留/不移动时 cursor 几乎不携带 gaze 位置信息**（"the eye is still roaming the SERP"，PDF p.6）。我们系统里「划线/划掉选项」这类动作是最可靠的 attention 锚点。

### 5. 哪类用户 alignment 强？
- [C2]：个体间差异是**最强效应**。个体平均对齐距离 SD=33.9；Levene 检验显示个体差异 > 任务差异（statistic=4.529, p=0.037）；性别、年龄均无显著影响（p=0.20, p=0.18）。"users have individual preferences and these differences are stronger than the differences between search tasks"（PDF p.4）。**作者明言：每个行为类别内个体差异依然很大**（PDF p.7）。
- **判断**：不存在「全局统一的 cursor→gaze 强度」。需要 **user-level calibration**（见 §18、§21）。

### 6. 哪类 task alignment 强？
- [C2]：任务间差异 SD=20.2（显著小于个体差异）；**click entropy 与 alignment 无相关（ρ=0.01, N=27, p=0.96）**，未复现 Guo & Agichtein 的导航型/信息型任务差异（PDF p.4）。dwell time 与 cursor behavior 调节 alignment（Figure 4、Table 1）。
- [C6]：layout 影响——eye–mouse 的 KL 散度在「仅 organic 广告」的 SERP 上最大（分歧最大，p<.0001），互信息在三种布局间无显著差异（p=.4451）。
- **判断**：task/布局**确实调节** alignment（[C6] 的布局效应；[C2] 的 dwell/behavior 效应），但没有简单规则。

### 7. click 前后是否更强？
- [C2]：**是**。action 行为（click 前 1 秒内）与 click 本身是全部行为中对齐最紧的两类（77 px / 74 px，Table 1）。而且对齐在时间上呈「页载入 0.5–1 s 内先变差（峰值 ~240 px）→ 约 2 s 后收窄」的进程，与「先扫视、后细读/准备点击」一致（Figure 4，PDF p.5）。

### 8. cursor 静止时 gaze 是否仍持续运动？
- [C2]：**是**。inactive 时段（cursor 静止 ≥1s）占 58.8% 时间，此时 gaze–cursor 距离高达 233 px，说明 "the eye is still roaming the SERP"（PDF p.6）。**cursor 静止 ≠ gaze 静止。**

### 9. cursor 离开内容区后 gaze 是否仍在读？
- [C2] 的 inactive 证据 + Discussion 明言 "prolonged cursor fixation may not [be a positive signal of interest] since ... the user's attention is probably elsewhere"（PDF p.9）。[C5] 的环境里用户可完全不动 mouse 阅读。**cursor 离开内容区/静止时，gaze 可能仍在读——这是常见情形，不是特例。**

### 10. 能否支持 `cursor near P2 → P(gaze in P2) increases`？
- **能（弱-中证据）**：行为标签化的 cursor（action/click）把点级距离压缩到 ~74–77 px，AOI 级预测（[C6]/[C7]）在广告 AOI 上达 F1 0.73–0.93 / AUC 0.81，说明「cursor 接近某区域」确实提高「gaze 在该区域」的概率。但必须附条件：**用户需处于主动交互状态；区域需足够大（region/AOI 级）；且强度需按用户校准；且 C6/C7 未做 participant-disjoint 验证**。静止 cursor 除外（见 Q3/Q13）。「区域=段落」是迁移假设。
- **不能**推出 `cursor in P2 → gaze=P2`：点级距离 178–373 px + 58.8% inactive + 700ms lag 都否定了确定性映射。

### 13.x 综合表

| 问题 | 结论 | 主要证据 |
|---|---|---|
| point-level 距离 | 平均 178–373 px，跨研究差异大 | [C2] p.4/p.6；[C6] §5.1 |
| 时间 lag | cursor 滞后 gaze ~700 ms（个体 250ms–>1s），无反向 | [C2] p.5 |
| AOI 级 vs 点级 | 区域/AOI 级远更可行（F1 0.73–0.93）；"AOI=paragraph" 是迁移假设 | [C6]/[C7] Tables 3/4、1/2 |
| 最强行为 | action/click（74–77 px） | [C2] Table 1 |
| 最弱行为 | inactive（233 px，占 58.8% 时间） | [C2] Table 1 |
| 用户差异 | 最强效应（个体 SD=33.9 > 任务 SD=20.2） | [C2] p.4 |
| 概率推断 | 支持 `cursor near P2 → P(gaze in P2)↑`（条件性、弱-中） | 综合 |

---

## 14. 强制耦合 vs 自然 Cursor

**核心对比：[C4] MoTR 是「界面机制制造 mouse≈reading position」的受控上限；[C5] 是「自然网页中用户可完全不动 mouse」的真实生态证据。两类实验不能直接比较 performance。**

### 14.1 [C4] 的强制耦合机制（界面如何制造 coupling）

MoTR 的界面是**强制耦合**的直接证据：[C4] 中文本被模糊（"text, which is blurred except for a small region around the tip of the mouse, which is in focus"，PDF p.1、p.4），模糊用 "standard CSS blur() function with a radius of 3.5 pixels" 实现（PDF p.4），"Participants must move the mouse to reveal and read the text"（PDF p.1）。参与者被告知 "move the mouse to reveal and read the text"（PDF p.4）。因此：

```text
想看某个词 → mouse 必须移到那个词附近 → mouse≈reading position（由界面保证）
```

这一耦合是**机制性的**：不移动 mouse 就读不到文本，reading position 与 mouse position 之间的对应不是用户自发选择，而是唯一可选路径。MoTR 的 spotlight（"about five letters to the left" 的渐变过渡，PDF p.4）模拟 foveal/parafoveal 视野，进一步把 mouse 位置类比为注视位置。注意：这实际上是**界面强制行为耦合**，而非界面测量自然耦合——用户的阅读节奏仍由用户控制（自定步调），所以它测得的是「在 mouse 必须跟随阅读位置的约束下，mouse 时间序列能多忠实地反映 incremental processing」，即**人工加强耦合条件下的上限**。

### 14.2 [C5] 的自然生态证据（无强制耦合）

[C5] 是在自然网站（ObjectDB 在线学习网站，技术类内容）上对 **90,367,657 个 mouse move 事件**（PDF p.2、p.4）做的被动观测（JavaScript 追踪脚本，最多 10 事件/秒采样，PDF p.4），无实验任务、无眼动、无强制移动。在这种环境里用户**可以完全不动 mouse 仍照常阅读**——mouse 移动是用户自发的。因此 C5 反映的是「自然状态下的 cursor 行为」，与我们的自然阅读页面同属一类生态效度。

### 14.3 为什么两类实验不能直接比较 performance

1. **因果基础不同**：C4 的 mouse–reading 对应由实验界面保证（不移动就读不到）；C5 的对应是用户自发行为，可能不发生。因此 C4 报告的"reading times 与 eye-tracking 效度"（见 §5 的验证数字）**不能**被解读为自然阅读中 cursor 也会给出同样保真的 reading times。
2. **目标变量不同**：C4 测得的是词级 reading time 分布（被界面约束为顺序扫描）；C5 测得的是移动方向/速度统计（水平 vs 垂直、左右不对称）与 PAR 现象，无法直接换算成 word-level 的 reading proxy。
3. **对「无信号」的容忍度不同**：C4 中无 mouse 移动 = 无阅读（文本不可见），所以"静止"几乎不会发生、含义单一；C5 中静止/停放的 cursor 大量存在且与阅读兼容（用户在读但没动 mouse），静止的语义截然不同。

### 14.4 C4 提供的 upper-bound 是什么

C4 提供的上限是：**当系统允许/强制用户用 mouse 标记阅读位置时，word-by-word mouse-based reading times 能多大程度重现 eye-tracking reading times 的经典效应**（如句法歧义、低频词效应，见 §5）。对我们的启示：如果未来我们的系统在 passage 上加**划词/高亮**这类「自愿但低成本的 mouse-marking affordance」，我们可以期待相似上限；但**自然阅读页面默认并不具备这种 affordance**，C4 不能直接推广。

### 14.5 C5 提供的 ecological-validity evidence 是什么

C5 提供的是：在无任何强制下，**确实存在用户把 cursor 当"虚拟手指"沿文本移动**（PAR）这一自然现象，且聚合统计（水平主导、右移慢于左移、垂直标记行）与 PAR 一致（PDF p.14）；但 C5 也承认 "the accuracy of PAR is varying"（PDF p.14）——PAR 的松紧在用户间差异很大，不是每个用户每个时刻都精确沿词移动。这就是"自然环境下 cursor 能携带 reading 信号，但信号强度个体间不均"的直接证据。

### 14.6 结论

- [C4] = **强制耦合上限**（high ground-truth fidelity，low ecological validity for natural reading）。
- [C5] = **自然生态现象学证据**（high ecological validity，无客观 gaze/GT，只有聚合统计 + 个案轨迹）。
- 两者结合回答：cursor 与 reading position 的对应在自然环境下**存在但个体化、稀疏化**；界面 affordance 可以"买到"更高的对应性，但要付出生态效度代价。
- **禁止**把 C4 的 word-level reading-time 保真度直接外推到我们的自然阅读页面（任务 §28-11）。

---

## 15. 指针辅助阅读（PAR）

**结论先行：存在一类用户会自然把 cursor 当"虚拟手指"沿文本移动（Pointer Assisted Reading, PAR）。这是 [C5] 在大规模自然网站日志中发现的真实现象，聚合统计强烈支持（水平主导、右向慢移≈阅读速度、垂直标记行）。但 PAR 的普遍性是「现象层面」的（cross-continental 的聚合模式），**不是**「每个用户都精确沿词移动」——PAR 松紧在个体间差异大，且用户可完全不用。文献支持「先判断某 user/session 是否处于 PAR 模式、再决定 cursor signal 权重」这一研究方向，但 C 组没有现成的 per-user PAR 分类器，需由 Group D/E 构建。**

### 15.1 PAR 的定义与现象
- [C5] 定义：PAR = "a reading behavior consisting of moving the mouse cursor (also known as the mouse pointer) along the text while reading, **similar to following the text with a finger when reading a book**"（PDF p.1-2）。这是「指尖指读」的在线版。
- 发现的统计现象（对象是 90,367,657 个 mouse move 事件，ObjectDB 在线学习网站，137 页，最多 10 事件/秒采样；PDF p.2-4）：
  - **水平移动多于垂直**；**右向多于左向**；
  - **右向慢移、左向快移**（左右不对称，用于平衡总移动距离）；
  - 四主轴（Right/Up/Left/Down，±45°）中：0°(右) 21.3%、180°(左) 15.6%、90°(上) 11.5%、270°(下) 10.7%（Table 3）；up 与 down 差异显著（Fisher's exact p<0.00001）；
  - 更长的 movement（≥1 s）：0°(右) 占 72.3%、180°(左) 21.1%——**长右移是绝对主导**（PDF Table 3）；
  - 速度：**右移速度峰值 150–200 px/s ≈ 3–4 词/秒 ≈ 180–240 wpm**（与成人非虚构阅读速度一致，PDF p.8）；>600 px/s 时左移多于右移（回到行首/翻页）。
- 解读：慢速右向水平移动≈跟随文本逐词读；竖向移动≈标记当前阅读行（"Marking text lines using vertical movements seems like a less demanding version of marking words with horizontal movements"，PDF p.13）。

### 15.2 PAR 是不是普遍行为？user-level heterogeneity 的证据
- [C5] 声称 "the results of section 4 indicate that **PAR activity is universal and cross-continental**"（PDF p.14）——这是**聚合统计层面**的普遍性（6 个流量最高国家的方向/速度模式一致，PDF Tables 1/4/6）。
- 但 [C5] 同时承认：
  - "**PAR is not practiced by all users all the time**. There are many pageviews in this case study dataset with no sign of such mouse movement activity at all. As a rough indication, **the mouse was moved (for any purpose) less than 2% of the time that the page was visible**"（PDF p.15）；
  - "**the accuracy of PAR is varying**"——tight PAR（精确沿词）与 loose PAR（宽泛沿行）差异很大，"Matching mouse movements to text words seems relatively easy in the former and much more challenging in the latter"（PDF p.14）；
  - 开放问题："what is the proportion of visitors who use the mouse cursor as a reading assistant tool, and how they are divided between the horizontal movers who mark words and the vertical movers who mark lines"（PDF p.15）。
- **判断**：PAR 作为**现象**普遍存在，但作为**个体行为**高度不均——多数页面时段鼠标根本不动，少数用户/时刻才有 PAR。**不能默认我们的学生是 PAR 型用户。**

### 15.3 能否「先判断 PAR 模式、再决定 cursor signal 权重」？
- **文献支持这个研究方向**：
  - [C5] 引用了配套的 PAR 自动识别方法研究（"preliminary methods for automatic recognition of PAR activity have been defined and evaluated [20]"），说明 PAR 识别是可做的（PDF p.2-3）；
  - [C5] 明确把「loose PAR 与文本词匹配」列为 future work，"possibly using Machine Learning and Artificial Intelligence methods"（PDF p.14）；
  - [C2] 提供行为学基础：reading 类 cursor 行为（沿文本右移+回移）是四类启发式之一，有明确阈值定义（垂直≤50px、右移≥150px、回移≥50px，PDF p.6），但仅占全部时间 2.5%、且 22/36 人被试 reading≤2%（PDF p.6）——**用 C2 的 reading 定义检测 PAR 型 session 是可行的第一步**。
- **边界**：[C5] 自己没有发布 per-user 的 PAR 分类器（识别器列为 future work，PDF p.16）；C 组没有一篇论文做了「先用 PAR 检测给 cursor signal 加权」的端到端验证。**结论：研究方向得到文献支持，但组件需要 Group D（episode/模式分割）与 Group E（与 GT 校准）实现。**

### 15.4 PAR 对我们系统的意义
- 左 passage 是单栏文本（类似 C5 的 ObjectDB 内容区），PAR 的「慢速右向水平移动 / 竖向标记行」特征**可迁移**到 passage 阅读检测；右栏 question/option 区的光标含义不同（作答/操作，见 §22）。
- 需要用户/会话级 PAR 检测来决定 cursor signal 权重——**这正落在「全局 mouse→attention 映射不成立」的核心结论上**（§21）。

---

## 16. Mouse → 难度

### 16.1 difficulty 是否被实验操纵？
- [C3]：**是**。三个目标题（employment detail / employee level / education level）每题把被试随机分到 easy/difficult 两个条件之一：
  - employment detail：**操纵选项措辞**（简洁直白 vs 更长更复杂的描述与结构）；
  - employee level 与 education level：**操纵选项顺序**（按层级有序 vs 随机乱序）。
  - 另有 8 个**无操纵的 baseline 问题**（同类题型但不含难度操纵），用于建立个体的基线交互行为。（PDF p.8-9）
- 难度是**操纵变量**而非测量变量——论文明确承认 "we only manipulated but did not measure difficulty we cannot quantify this in the current study"，且不同操纵与不同题相混淆（PDF p.22）。**GT = 实验条件（difficult vs easy 二分类），不是真实难度值、不是自报难度。**

### 16.2 哪些 mouse features 最有预测力？
- [C3] permutational feature importance（permutation 后 accuracy 下降越多越重要）：
  - employment detail（措辞操纵）：**response time 最重要**（-0.142），其次 y-flips（-0.028）、x-flips（-0.014）；
  - employee level（顺序操纵）：**initiation time**（-0.113）、x-flips（-0.041）、hovers（-0.033）最重要，**permuting response time 只降 0.009**；
  - education level（顺序操纵）：**maximum acceleration**（-0.224）、initiation time（-0.049）、hovers（-0.033），response time 也不重要。（PDF p.19、Figure 2）
- **判断**：特征重要性随操纵类型而变——**措辞类难度主要由 RT 反映，顺序类难度主要由「初始延迟、方向翻转、停顿」反映**。没有单一的「困难=慢鼠标」规律；必须按难度来源选择特征。

### 16.3 response time-only baseline 表现怎样？
- [C3]：RT-only（+age+gender）accuracy 分别 **64.8%（employment detail）/ 55.7%（employee level）/ 56.4%（education level）**（PDF p.18-19）。注意：这些都显著高于随机 50%，说明 RT 本身已是强信号，尤其在措辞操纵题上。

### 16.4 加 mouse 是否真的增加信息？
- [C3]：**是，但很小**。full mouse model（9 个 mouse 指标 + age + gender）最佳 accuracy 65.9% / 59.1% / 58.9%，比各自 RT-only 高约 **1.1 / 3.4 / 2.5 个百分点**。论文结论："inclusion of all mouse movement measures improved predictive accuracy compared to the response-time-only model"（PDF p.20），但作者同时承认操纵强度不足以达到可靠预测（accuracy 最高仅 65.9%）。**mouse 特征对难度的边际增益存在但有限。**

### 16.5 personalization 是否改善表现？
- [C3]：**是，增益大于加特征本身**。用 8 个无操纵 baseline 题对每个指标做回归取残差（baseline 校正），再加答案位置校正（两步法）。未校正 full model accuracy 61.0% / 55.5% / 56.2% → 校正后 65.9% / 59.1% / 58.9%，**但 personal baseline 增益依任务而异（employment +4.9pp、employee +1.2pp、education +1.8pp；选项位置校正在顺序操纵题再贡献 +0.9–2.4pp）**（PDF p.18-19、Table 2）。位置校正在「选项顺序被操纵」的题上额外有益（PDF p.20）。hover 阈值在 250/500/2000/3000 ms 间无唯一最优（PDF p.18）。
- **判断**：**个体鼠标行为基线差异大、且个人归一化可操作性强**——这是 C 组支持 personalization 的最直接证据之一。

### 16.6 不同用户 baseline 差异多大？
- [C3]：个人校正的有效性本身说明基线差异大到影响预测。此外论文强调 RT 绝对值的个体差异问题（"each person has his or her own baseline speed" 引用 Mayerl et al., 2005，PDF p.8）。

### 16.7 边界
- **`mouse → difficulty` 证据 ≠ `mouse → spatial attention` 证据**（任务 §11 强制的概念边界）。[C3] 全程无眼动、无 AOI、无位置语义，模型输出的是难度条件标签。**我们的阅读系统中，若用 mouse 信号推断"题目难度"，这不等于推断"学生正在看哪里"——两者是独立证据通道（见 §26）。**

---

## 17. Mouse → 投入度

**结论先行：[C8] 证明 mouse 行为（尤其 click 类特征）可以预测 session/task 级的「作答投入度 / 异常作答」（atypical responding），并与人（Big Five）关联。这是**会话级**的 engagement 信号，**不是** spatial attention 信号。cursor 可以同时携带空间注意信号与会话级投入信号，但必须分层，不能合并成一个 attention score。**

### 17.1 "task attentiveness" 如何定义与测量
- [C8]：把「任务注意力」操作化为 **atypical responding（异常作答）**：每个被试对图片选择任务中每张图的点击与否，与其与群体平均选择的偏离程度做 ROC，得到该被试的 AUC；取 `Abs_Area_Under_Curve = |AUC − 0.5|` 作为投入度指标（PDF p.4-5，Equation 1 附近）。个体完全随机作答 → AUC≈0.5 → Abs_AUC≈0 → 低投入；越偏离群体平均 → 越异常/不专注。
- 依据：图片刺激有很高评分者间信度（ρ=0.86，PDF p.2），所以偏离群体均值可解释为不专注/随机作答。
- 另有 **attention check**（把损坏图片拖进垃圾桶；连续两次失败终止会话，PDF p.3）作为**数据质量门**，与 Abs_AUC 是两套机制。

### 17.2 哪些 mouse 特征与 attentiveness 相关
- [C8]：click 类特征与 Abs_AUC 显著负相关（Bonferroni 校正后 p<0.001）：avg_click_att r=−0.18、reclick_percent_att r=−0.19、avg_click_norm r=−0.17、reclick_percent_norm r=−0.17——**越多的多余点击/重点击，投入度越低**。fixation 次数与 Abs_AUC 正相关 r=0.11, p=0.002——**越多鼠标注视，投入度越高**。（PDF p.7）
- 其他 pause/速度特征在 LV1 中"未显示可靠关系"（PDF p.8）。

### 17.3 预测任务与结果
- [C8]：用 11 个 mouse 特征 + Abs_AUC 预测 Big Five 人格（OLS），R² 仅 0.03（Neuroticism）–0.08（Conscientiousness）（PDF p.7）；PLS 显示鼠标特征与人格的联合协方差结构显著（LV1 p=0.001，解释 91% 协方差，PDF p.8）。**注意：没有 held-out 预测验证，R² 极低。**

### 17.4 关键边界：这不是 spatial attention
- [C8] 的 "attention" 是 **session/task-level 的作答规范度**，与「光标当前位置对应视觉注意位置」**完全无关**：无眼动、无 AOI、无空间定位分析。任何把 C8 表述为"cursor→视觉注意位置"的写法都是越界（任务 §5.4、§12、§28-6）。

### 17.5 cursor 能否同时携带两个信号？
- **可以，且 C 组支持分层**：
  - **spatial focus 信号**：由 [C2]/[C6]/[C7] 支持——行为标签化、AOI 聚合下 cursor 反映"gaze 在哪区域"（见 §13）。
  - **session-level attentiveness 信号**：由 [C8] 支持——click/reclick/fixation 次数反映"作答投入度"。
  - 两者是**不同粒度、不同时间尺度**的独立通道（[C2] 的个体差异说明 spatial 信号强度因用户而异，[C8] 的 click 类特征说明 engagement 信号是会话级聚合）。**禁止合并成一个 attention score；应分别建模（见 §26、§20 鼠标证据矩阵）。**

---

## 18. 自评注意 vs 眼动真值

**结论先行：[C1] 的 GT 是任务后自评问卷（"你是否注意到那个广告"），[C6]/[C7] 的 GT 是眼动 fixation。两者不是同一个 construct：自评"注意"测量的是事后广告知觉/记忆，眼动测量的是在线注视。而且 [C6] 用同模型对比：在自评 GT 数据集上 cursor 预测 F1 仅 56%/69%，在眼动 GT 数据集上达 93%/73%——**这一结果与 "fixation-derived labels 比 post-task self-report 更干净" 的判断一致（作者也这样解释），但两个数据集在参与者/SERP/流程/布局上均不同，不是受控的 ground-truth-only 消融实验**（93% vs 56% 不能完全归因于 GT 质量）。作为验证设计原则（眼动 GT 优先）成立，作为纯 GT 效应不成立。**

### 18.1 C1 的 label 到底是什么
- [C1]：**post-task 自评**。"We collected ground-truth labels through an online questionnaire, which was administered at post-task and asked the user to what extent they paid attention to the ad using a 5-point Likert-type scale: 'Not at all'(1)... 'Very much'(5)"。二值化："Not at all"/"Not much"→negative；"Somewhat"/"Very much"→positive；中性" I can't decide"丢弃。66% 正类。（PDF §3.5/§3.8）
- 作答时**页面已不可见**（"at that point the participants did not have access to the webpage"，PDF §3.7）——测量的是**事后对广告的记忆/知觉（ad awareness）**，不是在线注视。
- 预测目标：二分类"该用户是否注意到（唯一的那个）广告"（session 级、per-ad），**不是 spatial attention**，不是总注意量。

### 18.2 自评注意与眼动注意是不是同一个 construct？
- **不是同一个 construct**（任务 §28-5 强制）。自评 = 事后记忆/知觉 + 实验者期望；眼动 = 在线视觉注意。C 组没有任何论文把两者校准为同一量纲。特别地：
  - [C1] 每 SERP 只保留 1 个广告、强制被试关闭 ad-blocker、刻意保留广告 → notice 率可能被抬高；
  - 众包快节奏（作者自述 "users often proceed as quickly as possible ... to maximize their profit"，PDF §4.1）进一步压低自评与真实注意的对应。

### 18.3 self-report GT vs eye-tracking GT 各自能支持什么结论
- **self-report GT（[C1]）能支持**：cursor 轨迹可以学习预测"用户事后自评注意到某广告"这一**行为/知觉标签**；性能上限 AUC≈0.74（最佳 ResNet50）。**不能支持** cursor→客观视觉注意。
- **eye-tracking GT（[C6]/[C7]）能支持**：cursor 轨迹可以预测"注视在广告 AOI 上的时间/次数/是否注意"；[C6] baseline F1 0.93（organic）/0.73（DD），[C7] 分类 AUC 0.81、回归 NDCG≈96。**限定**：这些数值只对 AdSERP 单一实验源成立（见 §19）、AOI 是广告槽位、且 C6 为 trial 级随机分层（C7 3-fold CV 仅超参寻优）——**未验证未见新学生的跨用户泛化**。
- **直接对比（[C6] 第 7 节）**：同一 GRU + 同一输入（mouse position + ad bbox），在 [C1] 的 The Attentive Cursor Dataset（自评 GT）上 F1=56%（organic）/69%（DD），在本数据集（fixation GT）上 93%/73%；作者结论 "self-reported labels are noisier than fixation-based labels"。**证据等级限定**：这是**跨数据集**对比（不同参与者/SERP/实验流程/布局），方向一致且合理，但**不是**严格控制其他变量的 GT-only ablation——93% vs 56% 的差距还可能受 dataset difficulty / class distribution / layout / participant behavior 影响。**作为设计原则可采信，作为纯 GT 效应不可量化。**

### 18.4 对项目的启示
- 若我们系统未来要校准 cursor→focus，**必须以客观 GT 为准**（眼动/受控任务），自评只能作为辅助通道；[C1] 与 [C6]/[C7] 的 GT 等级差异必须写进 Ground-Truth Hierarchy（§22）。

---

## 19. C6 / C7 数据独立性审计

**结论先行：[C6] 与 [C7] 基于同一个实证来源——同一批被试、同一次实验、同 2,776 个 trials、同一眼动仪、同一批 mouse 日志。它们的关系是「dataset 论文 + 在该数据集上的建模论文」，不是两次独立 replication。任何证据综合不得把它们计为两份独立实验。**

### 19.1 直接证据链

1. [C7] 在数据描述处明确指向 [C6]："**For more details, see the associated dataset paper [43]**"，而参考文献 [43] 正是 "Kayhan Latifzadeh, Jacek Gwizdka, and Luis A. Leiva. 2025. A Versatile Dataset..."（= [C6]）。（PDF 物理页 3 左栏 "Dataset." 一段；参考文献页）
2. [C7] 的被试描述与 [C6] **数值一致**：[C7] "A total of 47 participants (20 F, 25 M), aged 19–44 years (M = 29.66...)"（PDF p.3）；[C6] "Forty-seven participants (27 male, 20 female)... ages ranged from 19 to 44 years (M = 29.66, SD = 6.46, Mdn = 29)"（PDF p.2）。
3. [C7] "Our final dataset consisted of **2,776 trials**"（PDF p.3）；[C6] "Our dataset comprises **2,776 transactional queries** on Google SERPs"（PDF p.1）。
4. 眼动仪相同：[C7] "Eye-tracking data was collected using a **Gazepoint GP3 HD** eye tracker"（PDF p.3）；[C6] "Eye movements were recorded with a **Gazepoint GP3 HD** eye"（PDF p.3）。
5. 实验设计相同：都是事务性查询（"buy" + Amazon Product Reviews 语料生成的查询，[C6] PDF p.2；[C7] "used them as queries on Google"，PDF p.3）；block 结构一致——[C7] "divided into **eight blocks**, each comprising 10 trials. The **first two blocks (not considered for analysis)** were used as warm-up tasks"（PDF p.3），[C6] "The main experiment consisted of **six blocks** per participant, each containing 10 trials"（PDF p.3）——**8 总块 − 2 warm-up = 6 主实验块，两篇一致**；每次 block 前重校准眼动仪（[C6] PDF p.3；[C7] PDF p.3）。
6. 数据集名称：[C6] "The dataset, which we have named **AdSERP**"（PDF p.5）。

### 19.2 一份不一致的报告（不影响结论）

- 性别分布：[C6] 报告 "27 male, 20 female"；[C7] 报告 "20 F, 25 M"。男女人数在两篇中有 2 人的出入（25 vs 27 male），这是同一数据在两处报告的**小不一致**（大概率是其中一篇的笔误），不改变"同一批被试"的结论，但应在后续引用时以 [C6] dataset 论文为准。

### 19.3 对证据综合的影响

- **C6 = dataset + 描述性统计 + baseline 分类实验（基于 fixation 的 AOI 标签）；C7 = 同一数据上的 cursor→eye-attention 建模（fixation time / fixation count / noticed）。**
- 因此：
  - C7 在「cursor 能预测 eye-tracking-derived attention」上的证据，**与 C6 是同一实证来源**，不能与 C6 的任何发现叠加为"两次独立支持"。
  - C7 与 C1 的作者重叠（Arapakis、Leiva 均出现）但**数据来源不同**（C1 是自评 GT 的众包单广告 SERP；C6/C7 是眼动 GT 的 47 人多广告槽 Google SERP），是不同数据。
  - 任何跨论文结论（如专题 §13）引用 C6/C7 时，必须整体标注为"来自 AdSERP 单一实验源"。

### 19.4 审计结论表

| 检查项 | C6 | C7 | 是否同一 |
|---|---|---|---|
| 数据集 | AdSERP（命名于 C6） | "associated dataset paper [43]" = C6 | ✅ 同一 |
| 被试 | N=47（27M/20F） | N=47（25M/20F） | ✅ 同一（性别报告小出入） |
| 试次（Trials） | 2,776 个事务性查询 | 2,776 trials | ✅ 同一 |
| 查询来源 | Amazon Product Reviews + "buy" | Amazon Product Reviews 语料 | ✅ 同一 |
| 眼动仪 | Gazepoint GP3 HD | Gazepoint GP3 HD | ✅ 同一 |
| 实验流程 | 主实验 6 blocks × 10 trials（C6 措辞） | 总 8 blocks × 10 trials、前 2 为 warm-up（C7 措辞） | ✅ 同一（8−2=6；47×60−44=2,776 ✓） |
| Mouse 日志 | 同一次实验采集 | 同一批 mouse logs | ✅ 同一 |
| 关系判定 | **同一实证来源：dataset 论文 + 建模论文** | | 非独立 replication |

---

## 20. 鼠标证据矩阵

**依据 C1–C8 逐条分级。真值（GT）列按 §11 的客观性排序；Evidence Strength 指该信号对「空间注意/阅读位置」的支持强度（不是对 engagement 或 difficulty 的支持）。**

| Mouse 信号 | 可能含义 | 支持论文 | 真值（GT） | 证据强度 | 主要混杂 |
|---|---|---|---|---|---|
| cursor position（单独、无行为标签） | 当前注意位置 | [C2]（对齐 74–233px 因行为而异）；[C6]（平均距离 372.89px） | 眼动 | **Weak**（条件性；静止时近无信息） | inactive 时段（58.8%）；个体差异；700ms lag |
| cursor–gaze 距离（点级） | 对齐程度 | [C2] p.4/p.6；[C6] §5.1 | 眼动 | **Weak–Conditional** | 任务/布局/行为调节 |
| hover（静止） | 注意停留 / 思考 / 阅读 | [C2]（inactive 233px）；[C3]（hover 预测顺序题难度） | 眼动 / 操纵难度 | **Weak**（对注意）；hover 对难度/投入是另一通道 | 无法区分读/想/分心/忘动鼠标（§3.5 项目前提） |
| hover duration | 注意时长 | [C2]（行为×对齐）；[C4]（强制耦合下 spotlight 停留=词级 RT） | 眼动 / 强制耦合 RT | **Weak–Medium**（自然界面）；C4 是强制上限 | C4 不能推广到自然阅读 |
| cursor pause（≥1s） | 停止移动 | [C2]（inactive 58.8%，233px）；[C8]（pause 类特征与投入相关性弱） | 眼动 / 无 | **Uninformative（对位置）** | 静止时 gaze 仍在 roam |
| movement speed | 读 vs 扫/导航 | [C5]（右移 150–200px/s≈阅读）；[C2]（reading 行为定义） | 无（聚合统计） | **Weak**（方向+速度可区分粗读/导航，但无个体 GT） | 速度绝对阈值依赖字号/布局 |
| acceleration | 认知负荷/难度 | [C3]（education 题最重要 -0.224） | 操纵难度 | **对 difficulty：Medium**；对 spatial attention：Unsupported | 混淆难度来源与题目 |
| trajectory length / distance | 交互量 | [C3]（total distance 特征）；[C8]（avg_euc_dist） | 操纵难度 / 无 | **对 attention：Unsupported** | 与任务难度/题目长度混淆 |
| direction changes / x/y-flips | 犹豫/回读 | [C3]（y/x-flips 对措辞题重要）；[C5]（回移=回到行首/重读） | 操纵难度 / 聚合统计 | **对 difficulty：Weak–Medium**；对 reading：Weak | 选项顺序/措辞混淆 |
| click | 交互目标处 gaze–cursor 最近 | [C2]（click 74px 对齐最紧） | 眼动 | **Moderate–Strong（cursor 信号中最强的 spatial anchor，但不是 attention truth）**——74px 仍非 0，且 C2 未证明 click 选项 B → gaze 一定落在 B 的语义 AOI（选项文本小时 74px 可跨多个区域） | click 是瞬时事件；click 目标≠唯一注意点 |
| click proximity（click 前 cursor 轨迹） | **interaction intent**（"要操作 B"） | [C2]（action 77px）；[C1]/[C6]/[C7]（点击型任务） | 眼动 / 自评 / fixation-AOI | **Reliable（对 interaction intent）**——"click/trajectory toward B → 将操作 B" 比 "正在阅读 B" 更可信 | intent ≠ 持续阅读注意 |
| cursor follows text line（PAR） | 正在阅读该行 | [C5]（PAR 现象）；[C4]（强制耦合上限） | 聚合统计 / 强制耦合 | **Weak–Medium（自然界面）** | PAR 个体不均；loose PAR 匹配困难 |
| cursor parked outside content | 无内容注意信息 | [C2]（inactive）；[C5]（<2% 时间移动） | 眼动 / 聚合 | **Uninformative** | 用户可能仍在读（viewport 才是信号） |
| cursor enters paragraph | 开始关注该段 | [C2]（active 对齐原理） | 眼动 | **Weak** | 一次进入≠停留 |
| cursor stays over paragraph | 持续注意该段 | [C2]（examining/reading 对齐 150–167px） | 眼动 | **Medium**（条件性） | 可能是 cursor parked（此时无效） |
| cursor leaves paragraph | 注意转移 | [C2]（active→inactive 对齐变化） | 眼动 | **Weak** | 离开≠不再看（gaze 可滞后 700ms） |
| click 频率/reclick（会话级聚合） | 投入度 / 异常作答 | [C8]（r≈−0.17~−0.19 与投入度负相关） | atypical-response | **对 attentiveness：Medium**；对位置：不适用 | 与人格/年龄相关 |

---

## 21. 个体差异与个性化

**结论先行：C 组证据一致支持「不能假设每个人 mouse usage pattern 相同」。个人基线差异是 C 组最强的效应之一：个体差异 > 任务差异（[C2]）、个人 baseline 校正有明确价值但增益依任务而异（[C3]）、PAR 松紧个体化（[C5]）、人格与 mouse 行为相关（[C8]）。personal calibration 有明确文献依据——两个用户是否该用不同 cursor evidence strength，答案几乎必然是「是」（但效果大小不能写死）。**

### 21.1 证据
- **[C2]（最强）**：个体平均对齐距离 SD=33.9，范围约 130–280 px；Levene 检验显示个体间方差显著大于任务间方差（statistic=4.529, p=0.037）；性别、年龄均无显著影响（p=0.20 / p=0.18）→ "more likely to stem from personal habits rather than age or gender"；"for each cursor behavior, gaze-cursor alignment still varied substantially among our subjects"（PDF p.4, p.7）。**即使按行为分类，个体差异依然存在——行为标签不能替代用户标签。**
- **[C3]**：personal baseline 校正（用 8 个无操纵 baseline 题回归取残差）有明确价值但增益依任务而异——employment 未校正 60.97%→baseline 65.87%（**+4.9pp**）、employee 55.48%→56.70%（**+1.2pp**，再加位置校正至 59.09%）、education 56.22%→58.05%（**+1.8pp**，再加位置校正至 58.95%）；**是文中最重要的单一增益来源之一，但效果大小不能统一写成 +3–5pp**。
- **[C5]**：PAR 松紧个体差异大（tight vs loose，PDF p.14）；用户可完全不用 PAR（鼠标移动 <2% 页面时间）。
- **[C8]**：不同人格的被试（尽责性/开放性高者）表现出更审慎的作答 mouse 行为；"factor loadings ... can subsequently be used as weights to predict the trait profile of interest in future users"（PDF p.11）——明确把 per-user 建模作为下一步。
- **[C6]/[C7]**：**未做** per-user 分析（无 user effect、无 personalization）——它们用 47 人的混合数据训练全局模型，是「全局映射」的代表，但其效果上限可能低于 per-user 模型。

### 21.2 回答：是否该用不同的 cursor evidence strength？
- **应该**。Student A（cursor 与 gaze 高度一致）与 Student B（cursor 几乎不跟随）显然需要不同权重：[C2] 显示这种差异是真实且巨大的（130 vs 280 px 的个体平均）。
- **怎么做有文献依据**：
  - [C3] 的「baseline 问题校正」法：用无操纵/低难度任务建立个体 baseline，对所有 mouse 指标回归取残差——可直接迁移到我们的系统（如用「读题前序任务」或「简单题」建基线）。
  - [C2] 的行为标签法：检测用户是否主动用 cursor（examining/reading 比例），据此决定权重。
  - [C5] 的 PAR 检测方向：判断用户是否 PAR 型。
- **边界**：C 组没有一篇做了「完整的两用户差异化 cursor 加权」的端到端验证；具体校准参数需 Group E 用客观 GT（眼动/think-aloud）标定。

---

## 22. 注意 vs 意图

**结论先行：cursor 对「interaction intent（即将点击什么 / 正在考虑哪个选项 / 操作目标）」比「reading gaze（正在看哪里）」更可靠。这是由 [C2] 的行为对齐证据直接支持的：主动交互（click 前 1 秒内）与 click 时刻是全部行为中 cursor–gaze 对齐最紧的时段（77 px / 74 px），而纯阅读/停留时段对齐松散（150–233 px）。cursor 接近选项 B 时，它更可能反映「用户正要把鼠标指向 B 去点击/操作」，而不是「正在读 B 文本」。**

### 22.1 证据
- [C2] 时间进程（Figure 4）：页载入后 0.5–1 s 内对齐变差（用户在扫视页面、不移动鼠标），约 2 s 后收窄，"when the subject may start to examine the page more closely and **perhaps prepare to click a link**"（PDF p.5）——cursor 移动高峰与**准备交互**耦合。
- [C2] 假说 c（PDF p.5）："the cursor follows gaze because **the user looks at something and then moves their cursor to interact with it**"——cursor 的移动动机是交互而非记录阅读。
- [C2] Table 1：action（click 前 1 s）/ click 对齐最紧（77/74 px），说明 cursor 在交互目标处离 gaze 最近——**cursor 所在的交互目标是 gaze 的高置信位置**（双向印证：交互目标=注视处=鼠标处）。
- [C1] 的任务天然是"点击最能回答查询的元素"；cursor 轨迹预测自评"注意到广告"，其中 click/hover 是核心特征。
- [C6]/[C7] 的任务同样是"点击一个典型会选择的元素"；cursor 轨迹预测注视在广告槽的分配——但注意 [C7] 报告 normalized sequence index 是最关键特征（PDF p.9），说明**轨迹的时序/接近终点**编码了意图信息。

### 22.2 对建模的边界含义
- 我们系统里 `pointer near option B` 更可信地是「**交互意图信号**（学生正要把鼠标移向/移到 B，准备选择/划线/划掉）」而非「阅读 gaze 信号」。
- 这提示 focus 推断需要区分两个假设：`cursor near B → P(user is looking at B)`（弱-中，依赖行为状态）与 `cursor near B → P(user will interact with B)`（较强，尤其伴随 trajectory 向 B + hover）。
- **证据等级**：[C2] 支持「交互目标处 cursor≈gaze」；「cursor 提前指向后续点击目标」的 trajectory-to-target 预测在 C 组没有专门研究——标记为 **PROJECT INFERENCE（由 C2 action 对齐 + C1/C6/C7 点击型任务间接支持）**。

---

## 23. Pointer + Viewport 证据

**结论先行：加上 pointer 后，对 focus 的判断确实比 viewport-only 有增量，但增量是**条件性**的——取决于（a）cursor 是否处于 active 状态、（b）是否伴随 trajectory 指向、（c）用户个体基线。用 C 组证据逐情形判定：**

### 情形 A：viewport=P2 且 pointer=P2（active）
- **attention confidence 显著增加**（论文直接支持，中等强度；但限于广告槽 AOI、同分布、trial 级划分）。[C2] active cursor（examining/reading/action/click）的对齐距离 74–167 px（Table 1）；[C6]/[C7] 在 AOI 级证明 cursor 接近区域显著提高「gaze 在该区域」的预测（F1 0.73–0.93 / AUC 0.81）。**但强度要按用户校准（个体 SD=33.9）且需行为状态支撑，且 C6/C7 未验证跨用户（unseen student）泛化。** 不能把"显著增加"误读为"确定"。

### 情形 B：viewport=P2 且 pointer=Question（active）
- **支持「P(Focus=Question) 上升」**（项目迁移推论，弱-中）：[C2] 的 active 对齐原理说明 cursor 在 question 区域时 gaze 大概率也在那附近；[C1]/[C7] 说明 cursor 与交互/点击目标相关。**注意**：不能据此说"学生没在看 passage"——cursor 与 gaze 只是概率相关，且存在 cursor 在 question 而 gaze 扫视 passage 的情况。

### 情形 C：viewport=P2 且 pointer parked（静止 ≥1s）
- **pointer 应被视为近无信息**（论文直接支持）。[C2] inactive 占 58.8% 时间、对齐距离 233 px、"the eye is still roaming the SERP"（PDF p.6）。此时 viewport 仍是唯一可信信号。**项目推论**：pointer stale → mouse evidence 衰减（见 §25 Q13；C 组无显式 decay 曲线证据，标记 PROJECT HYPOTHESIS）。

### 情形 D：pointer follows P2 文本行（tracking）
- **是明显更强的 reading evidence**，但证据分级要小心：
  - [C4]（强制耦合）下 word-by-word tracking 保真度高（validity 见 §5），但那是**界面保证**的 tracking；
  - [C5]（自然）下 PAR（沿文本移动）确实与阅读相关，但无眼动 GT 且 PAR 松紧个体差异大（"the accuracy of PAR is varying"，PDF p.14）。
  - 结论：**在自然阅读界面里，cursor 沿文本行移动是比「停在某处」更强的 reading 证据（中等强度）**，但 [C5] 是聚合统计 + 个案，[C4] 是强制条件，都不是自然界面的直接 word-level 验证。

### 情形 E：pointer 短暂划过 P2
- **几乎无意义**（论文直接支持）。[C2] 点级距离大（个体平均 130–280 px），一次快速穿越无法建立对应关系；[C5] 中鼠标大部分时间不动（<2% 的页面可见时间在移动，PDF p.15）。单次 crossing 的信息量接近零。

### 23.x 区分「论文直接支持」vs「项目迁移推论」
| 情形 | 论文直接支持 | 项目迁移推论 |
|---|---|---|
| A | [C2] active 对齐；[C6]/[C7] AOI 预测 | 按段落粒度应用、按用户校准 |
| B | — | viewport=P2 + pointer=Question → P(Focus=Q)↑ |
| C | [C2] inactive=233px/58.8% | stale decay 曲线 |
| D | [C5] PAR 现象；[C4] 强制耦合上限 | 自然界面 word-level tracking 强度 |
| E | [C2] 点级距离大 | 单次穿越弱 |

---

## 24. 数据采集启示

**结论先行：根据 C 组证据，**Raw Observable Events** 必须持久化，derived features 一律从原始序列后处理重算、不存成不可回放的 raw truth。**Raw Observable Events** 至少包括：`pointer x/y/t`、`pointer event type`（mousemove/enter/leave/click/scroll）、`viewport/visibility/layout`、`question navigation`、`underline`、`option elimination`、`answer selection` 等；而 `speed / acceleration / trajectory shape / hover episode / PAR episode` 属于 **derived feature/action**（依赖阈值参数，必须可由 raw 重算）。**`(x,y,t)` 只是 Raw Observable Events 的一部分，不是"唯一 ground truth"。**

### 24.1 值得保留的原始字段
- [C2]/[C6]/[C7] 共同使用的最小集合：**cursor 位置 (x,y) + 时间戳 + 事件类型（mousemove/click/scroll 等）**。C6 甚至记录了事件关联的 DOM **xpath**（"(t, x, y, e, xpath)"，PDF §4.5）——这使事件天然 element-level，强烈建议我们也记录 `pointer target`（DOM 元素 id/xpath）。
- pointer_enter/leave、hover_start/end：可用 `(x,y,t)` 后处理判定（C2 的 inactive≥1s、reading 阈值、C3 的 hover 阈值 250–3000ms 都是后处理），**不必**单独存储为 raw——但若要区分「悬停起止」与「指针经过」，需事件边界，可记录 mousemove 流的起止标记。
- click：**必须记录**（C2 显示 click 是 **cursor 信号中最强的 spatial anchor**——注意不是 attention truth，74px 仍可跨多个文本区域；C8 显示 click 类特征是投入度信号）。
- scroll + viewport：**必须记录**（我们系统 passage 独立滚动，[C6]/[C7] 都是固定静态页面、无法处理滚动内容——这是 C 组证据的缺口，见 §25 Q5/Q6）。记录滚动位置才能把 cursor 屏幕坐标映射到文档坐标（paragraph/sentence）。

### 24.2 应从 (x,y,t) 后处理的派生特征（不要持久化为 raw）
- 速度、加速度、jerk（[C3] max velocity/acceleration、[C8] avg_euc_speed）
- 方向变化、x-flips、y-flips（[C3]）
- trajectory 长度/曲率（[C3] total distance、[C8] avg_euc_dist）
- pause / hover 时长（阈值依赖字号布局，需 Group D 重标定）
- "reading" 类事件（沿文本右移+回移，[C2] 阈值针对 SERP 字号）
- PAR 检测特征（[C5] 方向/速度分布）

### 24.3 关键启示与缺口
1. **采样率**：C 组论文采样从 10Hz（[C5]）到 150ms 轮询（[C1]）到 60Hz（[C8]）不等；20Hz 重采样被 [C6] 用于 Mouse2Vec。**C 组只能支持"必须保留足够细粒度的 (x,y,t) trajectory，使速度/方向/pause 等可在后处理中恢复"；具体采样率 C 组没有证明最优值，需 pilot / D 组进一步确定，此处不锁定 60–100Hz。**
2. **坐标归一化**：[C1] 用 viewport 宽度归一化水平坐标（PDF §4.1）；我们需**同时**记录 viewport 尺寸与滚动偏移，才能重建文档坐标。
3. **语义目标**：`semantic_target`（passage/paragraph_id/sentence_id/question/stem/option_id）应作为 click/enter/leave 的关联目标（如 C6 的 xpath 做法），使下游推断 element-level。
4. **不可回放性**：绝不把"速度序列"或"hover 判定"存为唯一数据源——它们依赖阈值参数，必须能由 (x,y,t) 重算（任务 §21 的 raw field vs derived feature 区分）。

### 24.4 C 组对「哪些字段有用」的直接指导
- 对 **focus/attention**：cursor position + 行为标签（click/action/active movement）最重要（[C2]）；单独 position 弱。
- 对 **difficulty**：RT、initiation time、flips、hovers、max acceleration 有用（[C3]），但需按难度来源选特征。
- 对 **engagement/attentiveness**：click 频率、reclick、fixation 次数（[C8]）。
- 对 **reading 位置**：方向+速度（PAR，[C5]）；强制耦合下 spotlight 停留（[C4]，但不可直接外推）。
- 对 **interaction intent**：click 前轨迹、trajectory 终点（[C2]/[C7]）。

---

## 25. 十五个跨论文研究问题


### Q1. cursor position 与 gaze position 到底有多可靠的对应关系？
**等级：Conditionally informative**（不是 Reliable、不是 Weak）。
- 受控 SERP 上点级平均距离 178–373 px（[C2] 个体平均 130–280 px；[C6] 平均 372.89 px），且**高度依赖行为状态**：active cursor 74–167 px，inactive 233 px（[C2] Table 1）。**只在「主动交互 + 区域/AOI 级聚合」条件下才接近可靠；「区域=段落」是迁移假设（PROJECT TRANSFER HYPOTHESIS）。**

### Q2. 什么条件最增强 cursor → gaze 关系？
按增强强度排序：
1. **click / action（click 前 1s）**：74–77 px，最强（[C2] Table 1）；
2. **cursor 主动移动中（examining/reading）**：150–167 px（[C2] Table 1）；
3. **区域/AOI 级目标定义 + 行为/时序特征**：cursor 前 5s 轨迹 + AOI bbox → F1 0.73–0.93（[C6]；AOI 为广告槽位，且未做 participant-disjoint 验证）；
4. **用户处于"习惯用 cursor 跟随"的模式（PAR 型 / 高对齐个体）**：个体差异是独立调节变量（[C2] p.4，[C5]）。

### Q3. 什么条件下 cursor 几乎没有 gaze 信息？
- **cursor 静止（inactive ≥1s）**：占 58.8% 时间，距离 233 px，"the eye is still roaming"（[C2]）；
- **cursor parked 在内容区外/边缘**（[C2] inactive；[C5] 鼠标移动仅 <2% 页面时间）；
- **cursor 短暂划过**（[C2] 点级距离大 → 单次穿越近无信息）；
- **用户几乎不移动鼠标**（[C5] 非 PAR 用户）。

### Q4. 是否存在明显的 gaze leads cursor 或 temporal lag？
- **是，cursor 一致滞后 gaze**：[C2] 整体约 700 ms，个体 250 ms–>1 s；"the inverse situation—gaze lagging behind the cursor—did not occur"（PDF p.5）。**实时推断含义**：cursor 是 gaze 的过去式（≈0.7s 前）；用「cursor 最近到达的区域」而非「当前位置」；且不能期待 cursor 预测 gaze 即时落点。

### Q5. point-level 预测 vs region/AOI-level 预测，哪个更可行？
**区域级（region/AOI）明显更可行；paragraph 级是迁移假设。**
- point-level：平均距离 178–373 px（[C2]/[C6]），预测 gaze 坐标的 RMSE 仍 ~181–237 px（[C2] Table 3）；
- region/AOI 级：cursor→AOI-attention F1 0.73–0.93 / AUC 0.81 / NDCG≈96（[C6]/[C7]）。**但两点限定**：(a) 两篇均未做 participant-disjoint 划分（C6 是 trial 级随机分层、C7 3-fold CV 仅用于超参寻优）——**不能证明对未见新学生有效**；(b) AOI 是**广告槽位**（organic/direct-display ad），**不是 Paragraph/Question/Option**。
- **我们系统应做区域级 focus 推断，不做 pixel 级；段落/选项语义粒度是合理迁移假设，需自己实验验证（PROJECT TRANSFER HYPOTHESIS）。**

### Q6. MoTR（[C4]）结果可以多大程度迁移到自然阅读？
**低——不可直接迁移**。[C4] 的 mouse≈reading position 由模糊界面强制制造（PDF p.1/p.4，"Participants must move the mouse to reveal and read the text"）。它代表**强制耦合上限**；自然阅读页面用户可不动 mouse 阅读（[C5]），[C4] 的 word-level reading-time 保真度不能外推。可迁移的是**方法**（attentional association 的定义、fmin/fmax 阈值思路、质控过滤），不是数值。

### Q7. Pointer-Assisted Reading 是否足够普遍，可以把 pointer 当阅读位置代理？
**否——不能作为默认假设**。[C5] 的普遍性是聚合现象层面（cross-continental 统计模式一致）；但 "PAR is not practiced by all users all the time"、鼠标移动 <2% 页面可见时间、PAR 松紧个体差异大（PDF p.14-15）。**必须做 per-user/session 的 PAR 检测后再加权**（§15.3）。

### Q8. 是否需要 user-specific calibration / personalization？
**是，证据强（但效果大小不能固定）**。[C2] 个体差异 > 任务差异（Levene p=0.037；个体 SD 33.9 vs 任务 20.2）；[C3] 个人 baseline 校正有明确价值（employment +4.9pp、employee/education +1.2–1.8pp，另位置校正 +0.9–2.4pp）；[C5] PAR 个体化；[C8] 人格相关。**统一的全局 cursor→attention 强度不可辩护。**（§21）

### Q9. mouse 是否能提供 difficulty 证据？与 attention 的关系？
- **能（对"作答难度"）**：[C3] 三题上 full mouse model 均优于 RT-only（65.9 vs 64.8；59.1 vs 55.7；58.9 vs 56.4）；特征重要性随难度来源变化（措辞→RT；顺序→initiation/flips/hovers）。
- **关系**：`mouse→difficulty` 与 `mouse→spatial attention` 是**两条独立证据通道**，C 组没有任何论文把两者挂钩。[C3] 无眼动、无位置语义。**禁止**把"学生难"写成"学生看 X"或反之（任务 §28-7）。

### Q10. mouse 是否能提供 task attentiveness / engagement 证据？
- **能（会话级）**：[C8] click/reclick 类特征与 atypical responding 显著负相关（r≈−0.17~−0.19），fixation 次数正相关（r=0.11）；PLS 显示鼠标特征与人格协方差结构显著。
- **边界**：这是 session/task-level 的作答规范度，**不是 spatial attention**；且 [C8] 无 held-out 预测验证、R² 仅 0.03–0.08。

### Q11. 对我们的系统，viewport + pointer 是否明显优于 viewport-only？证据多强？
**修正结论**：C 组证明 pointer 在**特定条件下**（active + 区域/AOI 级 + 个体校准）包含 viewport 没有的额外空间信息，因此**理论上可作为 viewport 的辅助信号**（`Viewport only + Active cursor → likely more informative`，此点可支持）。但**在「英语阅读 + 双栏 + 独立滚动 + paragraph focus」任务中，viewport+cursor 到底提高多少，目前没有任何直接实验证据**——`viewport+cursor 显著提高 paragraph-focus accuracy X%` 这句话 C 组**不能**支持。**这恰好应成为我们后续自己的验证实验。**（证据基础：[C2] active cursor 压缩不确定性 233→77 px；[C6]/[C7] AOI 级预测——但限于广告槽、同分布、trial 级划分。）

### Q12. cursor 对 Passage focus vs Option/interaction intent，哪一个更可信？
- **interaction intent 更可信**。cursor 在交互目标处（click 前 1s 到 click）与 gaze 对齐最紧（74–77 px，[C2]）；cursor 的移动动机是交互（假说 c）；[C7] 的时序特征（sequence index）最关键。**`pointer near option B` 更像"将点击 B"而非"正在读 B"**（§22）。Passage focus 的 cursor 证据是弱-中的条件性信号。

### Q13. cursor 长时间不动时，还应被当成当前 attention evidence 吗？
- **不应（强证据）**。[C2] inactive 时段 58.8%、距离 233 px、"eye still roaming"——静止 cursor 与 gaze 位置几乎无关。
- **"evidence decay"曲线本身 C 组无直接证据**——[C2] 只给了"静止时对齐差"的静态结论，没有随时间衰减的具体模型。**标记为 PROJECT HYPOTHESIS — NOT DIRECTLY ESTABLISHED**（任务 §17）。合理的项目推论：stale cursor 的权重应随静止时长衰减（源于 inactive 的 233px 距离），但曲线形态需 Group D/E 标定。

### Q14. C 组能否支持 P(FocusState | cursor evidence) 这种概率 focus estimator？
- **能支持建立（条件性）**，但只能作为 **evidence 层**、不是确定性标签层：
  - 支持：cursor→gaze 的关系存在且可量化（[C2] 距离/lag；[C6]/[C7] AOI 级预测——但限于广告槽 AOI、同分布、trial 级划分，未见新学生的跨用户验证）；
  - 支持：个体差异必须参数化（[C2]/[C3]）；
  - 不支持：任何"cursor 位置→确定注意位置"的确定性映射。
- 我们系统的 `P(Focus=P2 | cursor, viewport, task, user)` 可以以 [C2]/[C6] 的距离/AOI 预测为**先验基础**，以 [C3] 的个人 baseline 为**用户参数**，以 [C5] 的 PAR 检测为**模式切换**。**但这些都是证据锚点，不是已交付的模型。**

### Q15. 完全不用 LLM/Agent，mouse/cursor 在英语阅读认知建模中最可靠可以承担什么角色？
**答案：contextual auxiliary evidence + interaction-intent signal + engagement signal（弱传感器）；特定条件下可作为 weak spatial sensor；不能作为 primary sensor。**
- 最可靠的角色按证据强度排序：
  1. **interaction-intent signal**（click/action 附近）——[C2] 74–77px，最可靠；
  2. **contextual auxiliary evidence**——与 viewport、scroll、task state 联合后提升 focus 推断（[C2]/[C6]/[C7]）；
  3. **engagement signal**（会话级）——[C8]；
  4. **weak spatial sensor**——仅在 active + 区域/AOI 粒度 + 个体校准条件下（[C2]/[C6]）；
  5. **unusable**——作为独立/确定性 attention 传感器（静止、点级、无校准）。
- **不能被当作**：primary sensor、attention truth、gaze 替代品（任务 §29 质量标准）。

---

## 26. C 组确立了什么

### C 组正式结论（经核对审查修订后建议采用——6 条）

1. **Cursor 不能当 gaze（扎实）。** cursor ≠ gaze，且 **gaze 一般领先 cursor**（[C2] 直接眼动证据：cursor 滞后 ~700 ms，个体 250ms–>1s，无反向）。点级平均距离 178–373 px。
2. **Cursor 的价值强烈依赖行为状态。** click/action（74–77 px，最强）> active examining / text-following（150–167 px）> inactive / parked（233 px，很弱）。**绝不能只用 pointer current x/y，必须用 pointer state + temporal context。**
3. **Cursor 对 interaction intent 的价值高于对 reading location 的价值。** `pointer → option B → click B` 这类轨迹比 `pointer in P2 → 正在读 P2` 更可靠（[C2] action/click 对齐；[C7] 时序索引最关键）。
4. **自然 Pointer-Assisted Reading 确实存在，但不能默认。** [C5] 支持「有些人/有些时段：mouse≈virtual finger」，**不支持「all students, always」**。**cursor reliability 本身可能就是 student/session-specific latent variable**——这是 C 组最有价值的启示之一。
5. **Personalization 很重要，但效果大小目前不能固定。** [C2]+[C3]+[C5] 一致支持「mouse usage 因人而异」→ 未来可研究 **Student-specific cursor reliability**；但不要写死 "personalization = +3–5pp"（实测 +1.2~4.9pp 依题而异）。
6. **Region-level probabilistic focus 是合理方向，但仍缺阅读专项验证。** 目标应是 `P(Focus=Passage/P1/P2/Question/Option B/UNKNOWN)` 而非精确 gaze x,y；[C6]/[C7] 提供了方法学可行性证据，但 **paragraph-level + natural reading + independent scrolling + unseen student 四条件同时成立的验证，C 组还没有**。

### 强证据
1. **cursor ≠ gaze 在点级上普遍成立**：受控 SERP 上平均距离 178–373 px；cursor 静止时段（58.8%）对齐差（233 px）。[C2]/[C6]。
2. **cursor 一致滞后 gaze（~700 ms），无反向**：所有个体 cursor 滞后 gaze，不存在 cursor 领跑。[C2] p.5。
3. **个体差异 > 任务差异，且非年龄/性别可解释**：个体 SD 33.9 > 任务 SD 20.2；Levene p=0.037；个人 baseline 校正有明确价值（增益依任务而异：employment +4.9pp、employee/education +1.2–1.8pp，位置校正另贡献 +0.9–2.4pp）。[C2]/[C3]。
4. **主动交互（click/action）时 cursor 与 gaze 对齐最紧**（74–77 px）。[C2] Table 1。
5. **区域/AOI 级 cursor→attention 预测可行（限同分布 + trial 级划分）**：fixation-AOI 标签 + cursor 轨迹 → F1 0.73–0.93 / AUC 0.81 / NDCG≈96。**证据拆两层**：
   - **Strong/Moderate**：在同类 SERP 数据分布内，cursor trajectory 确实包含足够信息预测 eye-tracking-derived AOI attention（[C6]/[C7]，AdSERP 单一实验源）；
   - **Partial / Open**：**新学生（unseen student）+ 英语阅读 + paragraph AOI + 独立滚动** 四条件同时成立能否达到类似效果——**未被验证**（C6 是 trial 级随机分层、C7 3-fold CV 仅用于超参寻优，均未做 participant-disjoint 划分）。
6. **眼动 GT 与自评 GT 是不同 construct；[C6] 对比与"fixation GT 更干净"一致但非受控 GT-only 消融**：同一 GRU 在 self-report 数据集 F1 56%/69%、在 fixation 数据集 93%/73%；方向支持"眼动 GT 优先"的设计原则，但 93% vs 56% 的差距不能完全归因于 GT 质量（数据集/布局/流程均不同）。[C6] §7。
7. **mouse→difficulty 证据独立于 mouse→spatial attention**：[C3] 三题上 full mouse model 优于 RT-only，但这是难度标签、无位置语义。
8. **PAR 作为自然现象存在**：方向/速度聚合统计与"cursor 沿文本读"一致，且 cross-continental。[C5]。

### 中等证据
9. **cursor 反映 interaction intent 比 reading gaze 更可靠**：交互目标处对齐最紧（[C2]），时序特征关键（[C7]）。（intent 方向属合理推论。）
10. **cursor 沿文本行移动是更强的 reading 证据（自然界面）**：PAR 聚合统计 + 个案支持，但无眼动 GT、松紧个体化。[C5]。
11. **mouse 特征可预测 difficulty，但增益有限（~1–3pp）且依赖难度来源**；RT 仍是强 baseline。[C3]。
12. **mouse 特征可预测会话级投入度（atypical responding）**，但无 held-out 验证。[C8]。

### 弱证据
13. **cursor 静止/停留提示注意停留**：无法区分读/想/分心/忘动鼠标（[C2] inactive；[C3] hover 阈值敏感）。
14. **cursor 接近区域（如段落）提示注意该区域**：仅 active 条件下成立，且强度个体化；"区域=段落" 是迁移假设。
15. **速度/加速度等运动学特征**：与难度相关（[C3]）但对 spatial attention 无直接证据。

### 不支持 / 仍未解决
16. **`cursor = gaze`**：被 [C2] 明确反驳（"claiming that the cursor approximates the gaze is misguided"，PDF p.9）。
17. **`cursor near paragraph → likely attention there`**：作为**默认**命题不成立；只有 active + AOI + 校准条件下才是弱-中证据（条件性成立）。
18. **`cursor follows text → likely reading`（自然界面）**：现象存在（[C5]），但无自然界面+眼动的 word-level 验证；[C4] 是强制耦合不可外推。
19. **`mouse hesitation → difficulty`**：不能简化成"慢=难"。难度证据依赖操纵类型与特征组合（[C3]），且与注意无关。
20. **`mouse inactivity → disengagement`**：[C8] 中 pause 类特征与投入度相关性弱；inactive 更可能只是"在阅读没动鼠标"（[C2]）。**不成立。**
21. **`cursor trajectory → interaction intent`**：方向支持（[C2]/[C7]），但无专门的"提前指向未来点击目标"实验。
22. **stale cursor 的 evidence decay 曲线**：无直接证据（PROJECT HYPOTHESIS）。
23. **滚动/长文档下的 cursor 行为**：C 组全部是静态 SERP（[C1]/[C2]/[C6]/[C7]）或单屏文本（[C4]）或自然浏览统计（[C5]），**没有**一篇研究"独立滚动文档 + cursor"——我们系统的双栏独立滚动是 C 组证据的空白区。

### §24 逐命题判定速查
| 命题 | 证据强度 |
|---|---|
| cursor = gaze | **Unsupported（被反驳）** |
| cursor near paragraph → likely attention there | **Conditionally informative**（active + AOI + 校准） |
| cursor follows text → likely reading | **Weak–Moderate**（自然界面现象支持，无眼动 GT） |
| mouse hesitation → difficulty | **Weak–Moderate**（特征组合相关，非简单"慢=难"） |
| mouse inactivity → disengagement | **Unsupported（[C8] pause 特征弱相关）** |
| cursor trajectory → interaction intent | **Moderate**（方向支持） |

---

## 27. 需要 D 组提供的输入（原始事件 → 行为 / 活动切分）

C 组把以下问题交给 D 组（只列 D 组需要解决、而 C 组论文只给出启发式/未给出界面的问题）：

1. **pointer episode 切分**：连续 `(x,y,t)` 流何时算一段 movement episode？[C2] 用 inactive≥1s 切分（PDF p.6）、[C5] 用同向 + gap≤5s 切分（PDF p.4，作者自认任意）——都是启发式，需按我们界面的字号/布局重标定。
2. **scroll + mouse 的 action boundary**：我们 passage 独立滚动，scroll 与 mouse 并行。C 组没有一篇处理"滚动长文档 + cursor"（C6/C7 是静态 SERP、C4 是单屏、C5 是自然浏览统计）。D 组需定义"滚动中 cursor 语义"（滚动时 cursor 是否跟随、滚动后 cursor 是否仍视为在内容区）。
3. **hover/pause 阈值**：[C3] 测过 250/500/2000/3000ms 无唯一最优（PDF p.18）；[C8] 用 >4s long pause + 25px/250ms fixation 定义（PDF p.3）。需按我们的交互（划线、划掉、答题）确定。
4. **reading 类事件（PAR/text-following）检测**：[C2] 的 reading 规则（垂直≤50px、右移≥150px、回移≥50px，PDF p.6）针对 SERP 字号；[C5] 的方向/速度特征（150–200px/s）针对 ObjectDB 字号。D 组需产出**可迁移的"沿文本移动"episode 分割器**，供 C 组结论在自然 passage 上落地。
5. **行为分类器**：[C2] 的 inactive/examining/reading/action 分类是 ad-hoc 启发式（"The process is ad-hoc"，PDF p.6）。D 组需决定是沿用启发式还是用监督分割。
6. **注意**：D 组输出的是**行为/动作分割**，不是认知标签（认知标签属于 E 组）。

---

## 28. 需要 E 组提供的输入（过程证据 → 认知诊断 + 构念效度）

C 组把以下问题交给 E 组：

1. **cursor-derived focus probability 的 construct validation**：我们系统用 `P(Focus=区域 | cursor, viewport, task, user)` 做推断后，需用**眼动 / think-aloud / stimulated recall** 校准。C 组的黄金标准是眼动（[C2]/[C6]/[C7]），E 组需要设计"学生做题 + 眼动/回溯"的验证实验。
2. **个体校准参数的标定**：[C2]/[C3]/[C5] 强烈支持 per-user 参数（对齐强度、baseline、PAR 类型），但具体校准函数需 E 组用客观 GT 拟合。
3. **difficulty vs attention 通道分离**：[C3] 证明 mouse→difficulty、[C2] 证明 cursor→gaze，两条通道独立。E 组需验证我们的系统是否把两者混淆（例如"慢速移动"同时被算作难度证据和注意证据时的构念效度）。
4. **PAR 型 session 检测的构念效度**：把"cursor 沿文本移动"当作"正在阅读"证据前，需验证它与"真实阅读"（think-aloud/眼动）的一致程度（[C5] 只有聚合统计，[C4] 是强制耦合）。
5. **stale cursor / evidence decay**：C 组无 decay 曲线证据（PROJECT HYPOTHESIS），E 组需用数据决定"静止 cursor 多久后权重归零"。
6. **禁止**：E 组不能用 LLM/Agent 解读 cursor（任务 §28-2），必须保持传统推断链。

---

## 29. 证据索引

**所有会影响系统设计的结论（证据台账，含 PDF 页码）。页码 = PDF 物理页。**

| # | 结论 | 论文 | PDF 页码 | 章节 / 公式 / 表格 / 图 |
|---|---|---|---|---|
| 1 | cursor 平均滞后 gaze ~700ms，个体 250ms–>1s；无「gaze 滞后 cursor」 | [C2] | p.2, p.5 | Abstract; Fig. 5; Temporal Effects |
| 2 | inactive 占 58.8% 时间，对齐距离 233px；examining 32.9%/167px；reading 2.5%/150px；action 5.7%/77px；click 74px | [C2] | p.6 | Table 1 |
| 3 | 个体对齐距离 SD=33.9 > 任务 SD=20.2；Levene p=0.037；性别 p=0.20、年龄 p=0.18 不显著 | [C2] | p.4 | User and Task Effects; Fig. 2/3 |
| 4 | click entropy 与 alignment 无相关（ρ=0.01, N=27, p=0.96） | [C2] | p.4 | User and Task Effects |
| 5 | 页载入后 0.5–1s 对齐达峰 ~240px，约 2s 后收窄 | [C2] | p.5 | Fig. 4 |
| 6 | reading 行为规则：垂直≤50px、右移≥150px、回移≥50px | [C2] | p.6 | Distinguishing Between Cursor Behaviors |
| 7 | 预测 gaze：baseline RMSEd 236.6→186.3（+behavior+dwell,−21.3%）→181.1（+future,−23.5%） | [C2] | p.8 | Table 3; Experiment |
| 8 | "claiming that the cursor approximates the gaze is misguided"；非 SERP 页面对齐更差 | [C2] | p.9 | Discussion |
| 9 | C1 GT = post-task 自评 5 点 Likert→二分类；页面已不可见 | [C1] | p.3–4 | §3.5, §3.7 |
| 10 | C1 数据集：3,206 被试、2,289 sessions、45,082 坐标；150ms 轮询 | [C1] | p.3–4 | §3.4, §3.6, §3.8 |
| 11 | C1 最优：ResNet50（trajectory 表示）AUC 0.739/F1 0.731；CNN>RNN | [C1] | p.6–9 | Tables 2–4; §6.1, §6.3 |
| 12 | C3 难度操纵：措辞（employment detail）vs 顺序（employee/education）；8 题无操纵 baseline | [C3] | p.8–9 | Data & Design |
| 13 | C3 最优 accuracy 65.9/59.1/58.9%；RT-only 64.8/55.7/56.4%；personal baseline 校正 +1.2~4.9pp（依题而异）+ 位置校正另贡献 | [C3] | p.18–19 | Results; Table 2 |
| 14 | C3 特征重要性：措辞题→RT(−0.142)；顺序题→initiation/flips/hovers | [C3] | p.19 | Fig. 2 |
| 15 | C4 强制耦合：文本模糊仅 mouse 尖端可读（CSS blur 3.5px）；"must move the mouse to reveal and read" | [C4] | p.1–2, p.4–5 | Abstract; Intro; A MoTR trial; Sampling |
| 16 | C4 MoTR↔眼动 RT 相关 0.51(gaze)/0.62(total)；回归概率 0.19；跳读 0.80 | [C4] | p.9 | Table 1 |
| 17 | C5 数据集：90,367,657 mouse events、137 页、最多 10 事件/秒；~375K 估计访客 | [C5] | p.2–3 | §3.1–3.2 |
| 18 | C5 方向统计：0°(右)21.3%、180°(左)15.6%；≥1s movement 右 72.3%；右移峰值 150–200px/s≈180–240wpm | [C5] | p.6–8 | Tables 3/5; §5.1 |
| 19 | C5 PAR "universal and cross-continental" 但 "not practiced by all users all the time"；鼠标移动 <2% 页面时间 | [C5] | p.14–15 | §6; §7 |
| 20 | C6 数据集 AdSERP：47 被试、2,776 transactional queries、Gazepoint GP3 HD 150Hz | [C6] | p.1, p.3 | Abstract; §3 |
| 21 | C6 eye–mouse 平均距离 372.89px（≈Huang 178px 的两倍）；MI 0.01–0.06；KL 17–22 | [C6] | p.5–6 | §5.1; Fig. 10 |
| 22 | C6 baseline：GRU 前 5s → F1 93%（organic）/73%（DD）；自评 GT 上同模型 56%/69% | [C6] | p.8–9 | Tables 3/4; §7 |
| 23 | C7 使用 C6 数据（"associated dataset paper [43]"；2,776 trials；47 被试；Gazepoint GP3 HD） | [C7] | p.3 | §3; Ref [43] |
| 24 | C7 回归 TFT MSE 2.86(≈1.69s)/NDCG 96.07；TFC MSE 50.07/NDCG 96.36 | [C7] | p.7–8 | Table 1 |
| 25 | C7 分类平均 AUC 81.24/F1 76.25；organic-top 最弱 AUC 71.87 | [C7] | p.8 | Table 2 |
| 26 | C8 投入度 = atypical responding（Abs AUC）；click 类特征负相关 r≈−0.17~−0.19 | [C8] | p.4–5, p.7 | §2.4.4; §3.2.1 |
| 27 | C8 预测人格 R² 仅 0.03–0.08；PLS LV1 解释 91% 协方差 | [C8] | p.7–8, p.10 | §3.2.2; Table 3 |
| 28 | C8 attention check = 拖损坏图进垃圾桶、两次失败终止会话（数据质量门） | [C8] | p.3 | §2.1 |

**注意**：页码均按 PDF 物理页（与各论文的印刷页码可能有偏移；[C2] 印刷页=物理页+1340；[C1] 印刷页=物理页+1308；[C6] 印刷页=物理页+3411；[C7] 印刷页=物理页+254）。
