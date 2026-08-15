# D 组 — 原始事件 → 动作 / 活动分割

> 本文档为 D 组 7 篇论文（[D1]–[D7]）的深度阅读报告。D 组回答的核心问题：**面对混合离散 + 连续 + 异步的 UI 事件流，什么传统方法最适合把低层日志可靠地转换为稳定、可解释、可回放的 Action Episodes？** 本轮严格停在 Action / Activity Segmentation，禁止越过该层直接判断学生的 cognition。
>
> 报告继承 A/A+/B/C 组已建立的前提：`raw behavior ≠ reading cognition`、`revisit ≠ confusion`、`dwell ≠ difficulty`、`navigation ≠ strategy`、`cursor ≠ gaze`、`viewport ≠ attention`。D 组只输出**行为层 vocabulary**，不进入 Process / Cognition 层。
>
> 生成日期：2026-08-12。全部页码引用均基于本地 PDF 文件逐页核对（PDF 页 + 期刊页双标注）。D1–D7 编号严格按任务文件锁定，未重排。
>
> **方法说明**：本报告由主代理对 7 篇 PDF 全文（121 页）逐页亲自精读后撰写；论文关键数值（F1、accuracy、编辑距离、阈值、复杂度、错误率）均从 PDF 原文抽取核对，未编造任何阈值 / F1 / latency / 页码。凡不属于论文原文的推断一律标注 `PROJECT TRANSFER INFERENCE`（项目推论）或 `OPEN DESIGN QUESTION`（开放设计问题）。
>
> **核对审查记录（2026-08-12，初稿完成后的全面审查）**：(1) 结构与编号审查——对照任务文件 §31 结构逐章核验（§0–§31 全部在位），D1–D7 编号未重排、标题/作者/年份与 PDF 首页一致；(2) 页码审查——§30 证据索引全部 52 条页码与提取文本逐条核对（PDF 页 + 期刊页双标注，D1=2729 起、D2=1176 起、D3=339 起、D4=29 起、D5=标题页+期刊页、D6=489 起、D7=2657 起）；(3) 数值审查——抽查 D2 三分割 accuracy 94.89/95.58/96.22 与 99.80% F-Measure、D4 误分类率 18.38%/25%/30%/9%/18%、D5 n.ED 0.04/0.05/0.17 与延迟 1–107ms/2–4ms/40–150ms、D1 平均 P/R/F1 94.31/97.71/95.64 与消融 F1−52.0%、D6 coverage 95.43% 与 inter-rater 0.47→0.91→0.99、D5 Table 2 任务长度 10.1–73.5 与缓冲 250——均与 PDF 原文一致；(4) 概念边界审查——逐条核对任务文件 §32 的 22 条禁止事项（见 §31 自查表），重点复查 denoising≠segmentation、统计变点≠语义边界、classification F1≠boundary F1（D2 案例）、HSMM 条件性结论、低频≠噪声；(5) 微调——§15 表格首行证据改为 D5 ours 行实证（Perf. ident. 行仅 S_U1/S_U3 满分），并明确 R(ma) ≥0.95；(6) 复核中修正——D6 Table 1 参与者数经 PDF 原文坐标级重构核对（flight=15 / wildlife=17 / weather=16 / brightkite=16 / Liu-Heer flight=16 / Wall=24），初稿"39/17/16/4"系把 Min 交互数误读为参与者数，已修正；§15 表格 BL_co-oc 的 categorization R(ma) 修正为 0.57–0.80、BL_dfg 修正为 R(ma) 0.49–0.82。
>
> **反馈修正记录（2026-08-12；历史反馈原文未随迁移保存，谱系限制见 `../../provenance/LEGACY_REPORT_PROVENANCE.md`）**：① **D1 降权**——定位为 Methodological Inspiration / Supplementary Evidence，不再是 UI 去噪实现候选（§7.18 重写）；② **Technical noise 不"无条件删除"**——统一改为 derived 层标记排除（noise_flag / duplicate_of / excluded_from_segmentation）+ Raw Observable Events 永久保留（append-only），并明确系统生成事件 ≠ 噪声（§10、§27 Q10、§27 Q1）；③ **D2 评估协议不一致**（LOOCV / 70%–30% split / 10-fold CV 混用）写入 §7.15/§7.19/§1 EF-2/§30 #53，其 96.22%/99.80%/99.83% 不作为决定算法优劣的重要数值依据；④ **D5 online+offline 与 provisional+refinement 分离**——前者 SUPPORTED、后者 PROJECT ARCHITECTURE HYPOTHESIS（warm-up = delayed commitment 而非 retrospective revision；§7.7、§16、§27 Q12、§1 EF-6、§28 Moderate #11）；⑤ **D5 确定性拆分**——边界识别 largely deterministic（given model/history）、类型分类 adaptive history-dependent online clustering，不再把整套 D5 归入确定性方法（§7.13、§14 第 9 问、§11）；⑥ **§23 Confidence 重新分级**——SCROLL_BURST → MODERATE / PROJECT TRANSFER INFERENCE、POINTER_MOVEMENT_EPISODE → MODERATE、POINTER_TRANSITION → WEAK–MODERATE，ANSWER_CHANGE 注明 STRONG 前提（前后 answer atomic events 的确定组合），并新增分级逻辑注记；⑦ **机制分流结论降级**——"不同 action 类型用不同机制"从 Strong 降为 MODERATE evidence + high-confidence architectural synthesis（§28 Moderate #7、§1 EF-10），明确其为跨论文 synthesis 而非 head-to-head 实证；⑧ **HMM duration 措辞统一为 geometric**（8 处：EF-5、D4 §7.9/§7.10、§13 表格、§26 矩阵、§27 Q6、§30 #23）；另：§25 GT 协议标注 PROJECT TRANSFER INFERENCE，§28 新增"D 组正式结论（反馈整合，6 条）"。

---

## 任务符合性对照表（依据 `../../provenance/LEGACY_REPORT_PROVENANCE.md` 登记的 Chat 2 / Turn 14 原始任务书逐条核对）

| 任务文件章节 | 任务要求 | 本报告完成位置 |
|---|---|---|
| §0 | 严格锁定 D1–D7 编号，禁止重排，按标题匹配 | §0 PDF 映射（7/7 在位） |
| §4.1–4.4 | 严格区分 Denoising / Boundary / Segmentation / Activity Recognition 四个问题 | §1(EF-1)、§10、§15、§28 |
| §6 | 比较至少四类路线（Rule/Grammar、CPD、Latent State、UI-Specific） | §9、§26、§27 |
| §7.1–7.19 | 每篇统一拆解模板（19 小节） | §2–§8 每篇 19 小节逐项覆盖 |
| §8 | 专题一 Denoising ≠ Segmentation，含 `# What Is Noise in User Interaction Logs?` | §10 |
| §9 | 专题二 Rule / Grammar-Based Segmentation（优点/缺点） | §11 |
| §10 | 专题三 CPD，含 `# What Is a Change Point in UI Interaction?` | §12 |
| §11 | 专题四 HMM vs HSMM（对比表 + duration 重要性） | §13 |
| §12 | 专题五 UI-Specific Task Abstraction，含 `# From UI Events to Task-Level Events`（10 问） | §14 |
| §13 | 专题六 Boundary vs Label（四种情况） | §15 |
| §14 | 专题七 Online vs Offline（含 provisional + retrospective refinement 概念） | §16 |
| §15 | 专题八 Segmentation Uncertainty，含 `# How Certain Is an Action Boundary?` | §17 |
| §16 | 专题九 Mixed Event Streams（event sequence vs fixed-rate time series） | §18 |
| §17 | 候选 Action Vocabulary（表格式逐条判定） | §23 |
| §18 | Atomic Event vs Composite Action 三类区分 | §19 |
| §19 | 重点研究 Scroll（SCROLL_BURST） | §20 |
| §20 | 重点研究 Pointer Episodes（候选依据） | §21 |
| §21 | Multi-Scale Segmentation（Level 1→2 及部分 Level 2→block） | §22 |
| §22 | Evaluation Framework 四层（Event Cleaning / Boundary / Segment / Action） | §24 |
| §23 | Segmentation Ground Truth，含 `# Where Do Action Boundary Labels Come From?` | §25 |
| §24 | Method Comparison Matrix | §26 |
| §25 | 不要强行选一个万能算法（不同 action 不同方法） | §26、§27 Q18、§28 |
| §26 | 18 个跨论文问题 | §27（Q1–Q18 全部作答） |
| §27 | D 组确立了什么（Strong/Moderate/Weak/Unsupported + 7 条命题逐条证据） | §28 |
| §28 | 交给 Group E 的问题 | §29 |
| §29 | Evidence Independence / Evidence Quality（Algorithmic vs Domain transfer） | §1(EF-9)、§9、§26、§28 |
| §30 | 证据索引（页码真实核对） | §30（39 条） |
| §31 | 最终输出结构（§0–§30） | 本文件完全按该结构 |
| §32 | 严格禁止事项（22 条） | 逐条自查通过（见 §31 自查表） |
| §33 | 最终质量标准（条件化结论而非口号） | §1、§27、§28 |

---

## 0. PDF 映射

根据论文标题、作者、年份将本地 PDF 与 D1–D7 编号建立映射。**编号严格按任务文件锁定，未重排。**

| 编号 | 论文（任务文件标题） | 作者 | 本地 PDF 文件 | 期刊/场合 | 年份说明 |
|---|---|---|---|---|---|
| D1 | MMAD: Markov Model-Based Adaptive Denoising Method for User Interaction Logs | Wang, Zhou, Tu, Shi, Hu, Yu & Zhang | `D_2025_Wang_MMAD.pdf` | KSII Trans. Internet and Information Systems 19(8): 2729–2752 | 2025（Aug. 2025） |
| D2 | Online Change Point Detection in Application With Transition-Aware Activity Recognition | Thakur & Biswas | `D_2022_Thakur_ChangePointDetection.pdf` | IEEE Trans. Human-Machine Systems 52(6): 1176–1185 | 2022（Dec. 2022；published online Jun. 2022） |
| D3 | A Survey of Methods for Time Series Change Point Detection | Aminikhanghahi & Cook | `D_2017_Aminikhanghahi_ChangePointSurvey.pdf` | Knowledge and Information Systems 51(1): 339–367 | 2017 期刊卷；Received 4 Mar 2016 / online-first 8 Sep 2016（任务文件"2016 online-first 日期"属实） |
| D4 | Unsupervised Segmentation of Hidden Semi-Markov Non-Stationary Chains | Lapuyade-Lahorgue & Pieczynski | `D_2012_LapuyadeLahorgue_HSMM_Segmentation.pdf` | Signal Processing 92(1): 29–42 | 2012（Received Sep 2010；available online Jun 2011） |
| D5 | Recognizing Task-Level Events from User Interaction Data | Rebmann & van der Aa | `D_2024_Rebmann_TaskLevelEvents.pdf` | Information Systems 124: 102404 | 2024（available online 15 May 2024） |
| D6 | A Grammar-Based Approach for Applying Visualization Taxonomies to Interaction Logs | Gathani, Monadjemi, Ottley & Battle | `D_2022_Gathani_GrammarVisualizationTaxonomies.pdf` | Computer Graphics Forum (EuroVis 2022) 41(3): 489–500 | 2022 |
| D7 | Unsupervised Time Series Segmentation: A Survey on Recent Advances | Wang, Li, Zhou & Cai | `D_2024_Wang_UnsupervisedSegmentationSurvey.pdf` | CMC (Computers, Materials & Continua) 80(2): 2657–2673 | 2024（published 15 Aug 2024） |

**页码约定**：本报告全部页码以 PDF 文件内页码（PDFPAGE）为准，同时在 §30 证据索引中标注期刊页。各 PDF 文件内页码与期刊页的对应：D1 首版页=期刊 2729；D2 首版页=1176；D3 首版页=339；D4 首版页=29；D5 首版页为标题页（期刊页 1 未标号），正文第 1 版页=期刊页 2；D6 首版页=489；D7 首版页=2657（封面）、正文第 1 版页=2658。

---

## 1. 核心结论

以下为 D 组跨论文核心结论。每条都可在 §30 证据索引追溯原文。

### EF-1. 四个概念必须分离，D 组论文各自只覆盖其中一部分
任务文件 §4 的四个问题（Denoising / Boundary Detection / Segmentation / Activity Recognition）在 7 篇论文中各自有对应，但**没有一篇同时解决全部四层**：D1 只解决 Denoising（且其 Future Work 明确把"去噪后用于 task-level segmentation"列为下一步）；D2 做 Boundary（OCPD）+ 下游 Activity Recognition；D3/D7 是方法地图（分别覆盖 CPD 与 BD/SD）；D4 是 Latent-State Segmentation（MPM 逐点状态标签）；D5 做 Segmentation + Categorization + Object 关联（最接近端到端）；D6 是 Grammar 形式的 Task Abstraction（人工映射为主）。**结论：把"哪一篇方法最强"当作问题本身是错的，正确问题是"哪一层由哪种机制负责"。**

### EF-2. 没有任何 D 组论文把 boundary accuracy 与 segment/activity accuracy 分开报告完整
这是 D 组最重要的评估缺口：D2 报告的 99.80% F-Measure / 99.83% accuracy 是 **activity recognition（分类）指标**（且其评估协议描述不一致——LOOCV / 70%–30% 受试者 split / 10-fold CV 混用，§7.15），论文**没有**报告任何 boundary precision/recall/F1、tolerance 或位移指标；D4 报告的是逐点误分类率 t（等价 segment label 错误率，不是 boundary 指标）；D5 报告 task 数量与归一化编辑距离（segment 内容相似度），不报告 boundary F1；D1 报告的是 noise 检测的 P/R/F1（Event Cleaning 层）。D7 综述则明确指出 SD 方法"不重视边界点准确检测"。**因此任务文件 §33 要求的"如何评估 boundary 而非只评 activity label"在 D 组文献里是一个未被解决、需要我们自己建立 evaluation framework 的缺口（§24）。**

### EF-3. 统计变点 ≠ 语义 action 边界，CPD 的适用面有清晰边界
D3 的 CPD 正式定义（Def. 7）把变点定义为"分布 PXi 发生变化"（H0: 无变化 vs HA: 存在 k*）；D7 进一步区分 CPD（统计性质变化）与 BD（状态/制度变化，可发生在没有明显统计性质变化时）；D2 的 OCPD 就是"方差变化"（Bartlett 检验），其变点只反映统计矩变化，与"语义上发生了什么"无关。因此：**pointer 速度突变可以是 action 边界，也可以是同一 action 内的减速**；而 answer click / question navigation / underline commit 这类**自带语义的事件根本不需要统计变点**。CPD 适合连续数值流（pointer samples、scroll 密集段）的边界发现，不适合离散语义事件本身。

### EF-4. 规则 / Grammar 路线对确定型行为最合理，但表达力受三个已知缺陷限制
D6 的实证结论（对 3 个数据集 × 7 个分类学）显示：terminal 层覆盖良好（46–100%），但存在 (1) **log 粒度与结构不一致**、(2) **terminal 过度使用导致语义塌缩**（Tableau 的 8 种 log 记录全部映射到同一个 filter terminal；某数据集 95.43% 的事件映射到同一个 explore terminal）、(3) **无法表达交互时序**。D5 的 completion-keyword chunking 也是规则式，同样依赖人工关键词集（其 §7.2 承认关键词完整性不确定）。对 SCROLL_BURST / ANSWER_CHANGE / OPTION_ELIMINATION 这类**模式确定、语义可枚举**的行为，rule/grammar 明显比 ML 更可辩护；但规则集必须审计 terminal 是否有区分度、是否保留时序/上下文（§11）。

### EF-5. 显式 duration 建模的价值是"条件性"的，不是无条件更优
D4 的数学机制：standard discrete HMM 隐含 **geometric** 停留时间分布，HSMM 可显式指定任意（non-geometric）分布。实证（D4 §5.3，非平稳手工图像）：当数据真正满足 HSMC 假设时，NS-RHSMC 明显优于 NS-HMC（类错误率 25% vs 30%；纹理错误率 9% vs 18%）；但当数据只是 HMC 时，RHSMC 无增益、高噪声下甚至略差（§5.1）。D7 补充 HDP-HMM vs HDP-HSMM 的对比：HDP-HMM 因非马尔可夫行为导致状态数膨胀、过渡过快，HDP-HSMM 更适合真实数据。**结论：duration 建模值得，但证据是"在数据确实有可变时长结构时值得"；对 POINTER_TRANSITION（短）vs READING-LIKE EPISODE（长）这类时长差异明显的状态，HSMM 有理论优势，但需要先确认我们的行为状态真的具有稳定时长分布，且要承受 K/时长分布/在线能力的代价。**

### EF-6. 在线能力与自适应参数是 D 组文献的两大稀缺属性
D7 综述的三个核心发现之一是"现有方法对在线支持不足，只有少数支持在线部署"（其 Table 1 中 online 列只有 E2USD 和 StreamScope 打勾）；D3 引入 ε-real-time 概念说明"没有 CPD 算法在完美实时下运行"。D5 是唯一在 UI 场景下同时支持 online + offline 的端到端方法（事件到达即处理，缓冲 250 事件，task 识别延迟 2–4ms/事件、task 分类 40–150ms/task，平均交互间隔 >2.5s 可实时跟上）。参数自适应方面：D1 用截断正态分布自动算阈值（μ−3σ），D7 大多数方法仍需指定 K/N，D5 的 DenStream 聚类无需指定簇数但需缓冲大小。**结论：① "Online + Offline both feasible" 在文献中被支持（D5 直接实证）；② "online provisional + offline retrospective refinement"（先在线提交 provisional 边界、之后回头修改历史边界）没有文献演示——D5 的 warm-up 更接近 delayed commitment（推迟决断），E2USD 的延迟聚类、BCPD 的在线后验也属"推迟/可重估"，都不是"修改已输出边界"。因此后者应标为 PROJECT ARCHITECTURE HYPOTHESIS（§16）。**

### EF-7. Boundary uncertainty 有理论依据保留，但只有概率模型天然提供
D4 的 MPM 分割直接输出逐点后验 p(x_n|y)、p(v_n|y)（§2 Eq. 2.5–2.6）；D3 的 BCPD 输出 run-length 后验 P(r_t|x_1:t)；D2 的 OCPD 输出检验统计量与 p 值（变点显著性）。而 D5 的规则式边界、D6 的 grammar 匹配、D1 的噪声标记都只输出 hard decision，无置信度。**结论：如果后续系统要保留 boundary confidence 而非只存 boundary=TRUE，理论依据来自概率类方法（HSMM/BCPD/OCPD），规则类方法需自行设计置信度（如 D5 的 similarity score t 可作弱置信度）。**

### EF-8. Rare event ≠ noise：D1 明确反对"低频即噪声"，但它的机制仍可能误删低频真实行为
D1 的摘要直接批评"现有方法把低频动作当噪声"，其创新是识别**高频外部噪声**（如窗口拖拽），并给出证据：baseline（频率法）在外部噪声上表现差（Table 6：RT⊝ baseline F1 0.8375 vs MMAD 0.8899）。**但** MMAD 的删除标准是"转移概率 < μ−3σ"——一个真实但罕见的行为（如学生只修改一次答案）如果其转移概率低，**仍然会被删**。论文自己在 RQ3 讨论中承认"大体积真实数据集存在变体，会影响状态转移，导致正常变体动作被误判为噪声"，仅以"RPA 场景只允许单一 trace"为由辩解。**这对我们的场景是硬伤：英语阅读中"低频但语义重要"的行为（ANSWER_CHANGE、UNDERLINE_REMOVE、单次 OPTION_ELIMINATE）不能由统计去噪保护，必须在去噪规则里显式加入语义白名单。**

### EF-9. Evidence Independence：D 组没有一条"sensor/HAR 上成功 → UI 上也成功"的迁移证据
D 组的算法证据（D2/D3/D4/D7 的数值）全部来自 sensor HAR、雷达图像、EEG/运动数据、模拟信号，**没有一篇在真实 UI 交互流上验证过 CPD/HSMM 的分割性能**。UI 场景的实证只来自 D1（RPA 动作日志，合成注入噪声）、D5（RPA 风格交互日志，任务级）、D6（可视化交互日志，但评估的是分类学表达力而非分割质量）。因此，把 D2 的 OCPD 或 D4 的 HSMM 用到我们的 pointer/scroll 流上属于 **Algorithmic evidence + Domain transfer inference（项目推论）**，必须自建评估。

### EF-10. 项目最终形态是"分 action 类型选择机制"，不是单一万能算法 —— MODERATE evidence + high-confidence architectural synthesis
D 组文献支持任务文件 §25 的判断：不同 action 类型适合不同机制——确定性语义事件（answer click、question navigate、underline commit）直接作为 atomic actions（§19、§27 Q17）；scroll burst 适合规则聚合 + 时间间隔（§20）；pointer 连续流适合 CPD 或概率分割（§21）；已知交互模式适合 grammar（§11）；潜伏态/歧义态才需要 HSMM（§13）。**但必须说明证据性质：这是跨论文 synthesis（D5 消融 + D6 表达力 + D7 分类框架），不是 head-to-head empirical result——没有论文在 same UI dataset 上比较 Rules vs Grammar vs CPD vs HMM vs HSMM。它作为"目前最可辩护的架构原则"进入最终系统（§28 Moderate #7）。**

---

## 2. D1 — MMAD: Markov Model-Based Adaptive Denoising Method for User Interaction Logs

> **论文定位**：**Denoising**（用户交互日志噪声过滤）。任务文件 §8-注意"D1 主要是去噪论文，不要把它写成完整 action segmentation 方法"——本报告严格按其定位分析。Wang, Zhou, Tu, Shi, Hu, Yu & Zhang, KSII TIIS 19(8): 2729–2752, 2025。
>
> **D1 在 D 组中的角色（反馈修正后）**：**Methodological Inspiration / Supplementary Evidence，不是核心实现候选**。它提供"transition structure > raw frequency"的去噪思想与内/外噪声概念框架，但**不**提供可在我们系统上直接使用的去噪器（其输入是语义化 RPA 动作日志、噪声是人工注入的，见 §7.18）。

### 7.1 研究问题

论文要解决的问题：RPA（机器人流程自动化）场景下，真实用户交互日志含大量噪声，会破坏过程挖掘。三个被指出的现有方法局限（§1，PDF p.2）：(1) 多任务交错时存在共享动作，一个动作可能在一个任务是噪声、在另一任务是正常行为；(2) 数据偏差——重复动作被视为内部噪声、非常规动作（如窗口调整）被视为外部噪声，现有方法无法识别外部噪声；(3) 现有方法依赖人工设定阈值，无法跨场景泛化。RQ1–RQ3（§3.3）：去噪有效性 / 内外部噪声识别 / 各技术组件贡献。

**归属**：Denoising（不解决 boundary / segmentation / activity recognition）。

### 7.2 输入数据

RPA 动作日志：`UIL = {(t1, u1, a1, e1), ...}`，每行是一次用户-应用交互，含 timestamp、user、app、action event；另有 workbook / worksheet / URL / target element 字段（可能缺失，补 nan）。论文实际用两个真实日志：SR（把学生信息从 Excel 手动转到 web 信息系统的完整过程）与 RT（填写报销申请信息），并人工按 0.1% / 0.5% / 1.0% / 2.0% 比例**注入噪声**构造单任务、多任务、混合噪声场景（§3.1，PDF p.12–13）。

**与我们的 UI logs 接近度**：中。事件已是离散语义动作（copyCell / paste / editField / clickButton + 目标元素），粒度与我们的 click / underline / answer 语义事件同一层级；但**没有连续 pointer 流、没有 scroll 采样**。其多任务交错场景（任务共享动作节点）与我们的"passage 与 question 区域共享 pointer/scroll 事件类型"有结构相似性。

### 7.3 事件 / 观测粒度

一个 observation = 一行交互记录（一个 action：应用 + 事件类型 + 目标元素 + 时间戳）。论文进一步把它们抽象为 **log template** `w_ti = (u, e, te)`（应用综合标识、事件类型、目标元素），并基于"相似用户动作生成相同模板"的相关性假设做压缩（§2.2，PDF p.6–7）。即 observation 层级 = action，建模层级 = template。

### 7.4 预处理

§2.2.1 Event log Cleaning and Filtering（PDF p.7）：删除无效 / 重复 / 异常数据，空白标签填 nan，提取用于模板生成的 action 列，形成由多个执行 routine 组成的 log collection。这是**去重 + 过滤**级别的预处理；没有滑动窗口 / 重采样 / 特征提取。注意：**"删除重复数据"本身就是一种去噪**，且发生在噪声判别之前——这使其噪声指标（Precision/Recall）无法覆盖已被预删除的重复。

### 7.5 分割单位

**不切 segment**。输出是带噪声类别标签的日志（`U_denoised`，噪声节点/边被标记或移除）。单位是"噪声节点 / 噪声边 / 噪声标记的 action 行"，不是 episode。

### 7.6 边界定义

**无显式边界模型**。D1 不定义任何边界；它定义的是"哪些 action 行是噪声"，判断依据是模板转移概率是否低于自适应阈值（§2.4.1）。噪声节点分三类：外部噪声节点（与全部邻居互转移概率 < ξ）、内部噪声节点（自环转移概率 < ξ）、内部噪声边（两节点间转移概率 < ξ）。

### 7.7 在线 vs 离线

**OFFLINE**。§2.3.3 明确要求"跨多个时间段的大规模日志采样"（利用大数定律消除瞬时异常），且迭代式噪声删除需要反复重算全图转移概率。它是批处理、需要完整日志。**不可在线。**

### 7.8 监督

**Unsupervised / 无标签**（论文强调"不依赖日志的先验知识"，无需人工阈值）。但仍需人工设计：(1) 模板生成规则（自然语言模板的构造方式）；(2) 阈值统计方法的选择（截断正态分布 + μ−3σ）。无需 boundary / activity labels，无需任务模板。

### 7.9 模型 / 算法

流水线（§2.2–2.4，Fig. 2）：
1. **Log Template Generation**（Algorithm 1，O(N)）：清洗 → action 标识（表 2）→ 相似 action 聚为同一 template（标识 A/B/C/...）→ 生成自然语言模板。
2. **State Transition Calculation**（Algorithm 2 前半，O(g·V²)）：
   - 直接关系图 G_direct：有向循环加权图，节点 = template，边 = 相邻直接转移，权重 = 共现频次。
   - 图扩展：同一动作类型作用于不同目标元素拆分为不同节点。
   - **Markov model**：状态转移概率矩阵，p(s'|s, e)，∑p = 1，映射 S×E×S → [0,1]（PDF p.9）。
   - **自适应阈值**：观察到转移概率呈"高中心低尾"分布（大多集中在 0.7 附近），用**截断正态分布**（[0,1] 区间）拟合转移概率分布（KS 检验验证），阈值 ξ = μ − 3σ；转移概率 < ξ 判为噪声。两个防偏策略：跨时段大采样 + Tukey's fences（3×IQR）过滤极端离群值。
3. **Log Noise Removal**（Algorithm 2 后半）：识别噪声节点/边 → 迭代式临时移除 → 重算图/转移概率 → 若邻居间转移概率上升则确认噪声，否则恢复 → 重复直到候选列表不变。

Observation → Internal representation → Boundary/Segment 的关系：action 行 → 模板（压缩表示）→ 模板转移图 → 低转移概率标记为噪声。**核心可迁移思想：用"转移概率"而非"频率"判噪，是 D1 对"低频即噪声"假设的主要修正。**

### 7.10 时长建模

**无 duration 模型**。完全忽略时间间隔；时间戳只用于排序（UIL 定义要求 t1<t2<...<ti）。

### 7.11 噪声鲁棒性

D1 的**主题**就是噪声，重点分析（任务文件 §7.11 要求）：
- 偶发事件 / 重复事件：预处理删除重复（§2.2.1）。
- 外部噪声（非常规动作，如窗口调整、目标突变）：显式建模为"与邻接节点互转移概率低"的节点——**这是它对频率法的关键改进**，可在噪声比例高时仍识别（RQ2 结果，PDF p.15–17）。
- 高频外部噪声（如频繁窗口拖拽）：D1 声称能处理（baseline 频率法在此失效）。
- **误删风险（关键）**：判噪标准是转移概率 < μ−3σ。一个**低频但真实、且与任务语义相关**的行为（如学生仅改一次答案）若在转移图中是低概率孤立边，**仍会被删**。论文未提供任何"语义白名单"或"低频真实行为保护"机制。论文在 RQ3 讨论中承认变体（variant）会被误判为噪声（PDF p.17），仅以"RPA 允许单一 trace"自我辩解。**这是 D1 对本项目最重要的警示（→ §10 专题一）。**

### 7.12 多模态 / 多事件兼容性

原生支持离散动作事件的多种属性（app + event type + target element + 可选的 workbook/URL 等），通过 template 统一为自然语言文本处理（格式不一致通过模板生成解决，§2.2）。**不支持连续数值流**（无指针坐标、无 scroll delta）。没有时间戳利用、没有异步流概念。

### 7.13 可解释性

中等偏上。输出是"带噪声类别标签"（internal/external 已由节点类型区分）的日志；模板是自然语言文本（"In the first row, e1 affects te1 in a1: wb1: ws1"），可读。但**不输出任何 segment / action / episode**——它只告诉你哪些行是噪声。

### 7.14 不确定性

**无 uncertainty 输出**。噪声判定是 hard decision（转移概率 < ξ）。唯一的"软"信息是转移概率本身（可在图上读出，但论文不作为置信度输出）。论文的 KS 检验描述存在内部不一致（声称 p<0.05 却称"fail to reject H0"，PDF p.9）——其统计拟合的可靠性论证是有瑕疵的（详见 §7.19）。

### 7.15 评估

**只有 Event Cleaning 层指标**（任务文件 §22.1 的 noise precision/recall/F1）：
- 指标：Precision / Recall / F1，针对"噪声行是否被正确标记"（TP=噪声且标记为噪声，等）。提前人工标记噪声行作 GT。
- 结果（§3.3，Table 5–6，PDF p.14–18）：两场景平均 Precision 94.31%、Recall 97.71%、F1 95.64%；比 baseline[16]（Conforti 离群检测）平均 F1 高 3.3%、Recall 高 3.9%。单任务最佳 RT 1.0 的 F1 97.39%；多任务最佳 RT∪SR 1.0 的 F1 97.86%。
- 内/外/混合噪声（Table 6）：外部噪声 RT⊝ F1 88.99%（比 baseline 高 6.3%）；多任务 RT∪SR⊝ F1 91.97%（高 4.2%）。
- 消融（Table 7）：无 Markov 模型 → recall −6.5%、F1 −3.8%；**无 Log Template → recall −38.4%、F1 −52.0%**（模板贡献最大）；无 Adaptive Denoise → recall −3.2%、F1 −1.8%。
- **没有** boundary accuracy、segment quality、downstream（process mining）性能。任务文件 §7.15 明确要求严禁把三类混在一起——D1 恰好只做了第一类。

### 7.16 延迟 / 计算成本

Algorithm 1 复杂度 O(N)（N=事件数）；Algorithm 2 复杂度 **O(N + g·V²)**（g=迭代次数，V=唯一模板节点数，PDF p.11）。迭代式去噪需要多次全图重算，离线批处理成本随 V² 增长；论文未报告具体运行时间或内存。**不适合实时。**

### 7.17 超参数敏感性

论文卖点是"自适应阈值、无人工设定"（对比 baseline[16] 固定 0.05 阈值无法适配噪声比例，PDF p.14）。但仍有隐性人工参数：截断正态分布的拟合前提（"高中心低尾"是观察假设）、μ−3σ 的 3σ 选择、Tukey's fences 的 3×IQR、模板生成的自然语言规则、清洗阶段的删除规则。这些是否跨场景稳健论文未做敏感性分析。

### 7.18 迁移到我们的英语阅读系统

**定位判定（重要）：D1 = Methodological Inspiration / Supplementary Evidence，不是核心实现候选。** 两个根本性限制决定它不能迁移为"我们的 UI 去噪方案"：(1) D1 的输入是**高度语义化的 RPA action logs**（copyCell/paste/editField/clickButton + 目标元素），不是我们的 pointer/scroll 连续信号；(2) 其实验噪声是**在真实日志上按比例人工注入的**，不是真实自然产生的阅读交互噪声。因此它报告的平均 F1≈95.64% **不能解释为"MMAD 在我们的英语阅读日志上能 95%+ 识别噪声"**，更不能直接迁移成 "MMAD → pointer jitter denoising"。

- **Methodological Inspiration（可借鉴的思想）**：① **"transition structure > raw frequency"** 是值得借鉴的去噪思想——判噪依据转移概率而非单纯频率；② 内/外噪声二分法（内部=异常重复/执行异常，外部=非常规动作类型）作为噪声概念框架；③ 多任务共享节点问题与"passage/question 区域共享事件类型"结构同构（仅作概念类比）。
- **Supplementary Evidence（补充性证据）**：D1 的实证只证明"在 RPA 动作日志 + 人工注入噪声下，MMAD 比频率法好"；**在自然阅读 UI、连续 pointer/scroll 上的有效性完全未验证**。其任何数值（平均 F1 95.64% 等）不可外推到我们的场景。
- **Transfer With Modification（如需进一步使用）**：必须加入**语义白名单**保护低频但有意义行为（ANSWER_CHANGE / UNDERLINE_REMOVE / 单次 OPTION_ELIMINATE）——MMAD 无此机制；且"变体=噪声"的容忍度与我们"变体=有价值的个体差异"直接冲突。
- **不可迁移**：整体方法目标（得到"单一 trace"的 RPA 自动脚本）；模板生成假设（相似动作→相同模板）在我们语义事件下不成立；其 KS 检验统计表述自相矛盾，使"阈值自适应"的理论论证弱于宣传（§7.19）。

### 7.19 这篇论文未确立什么

- D1 未证明去噪提升**分割或下游识别**性能（其 Future Work 明说"将探索用去噪日志做 task-level segmentation"，PDF p.20——即 segmentation 是未来工作）。
- D1 未证明"低频但真实的语义行为不会被误删"——恰恰相反，论文承认变体会被误判（RQ3 讨论）。
- D1 未评估 **segmentation** 任何指标；其 P/R/F1 全部是噪声行标记指标。
- D1 未报告对时间间隔、连续流、在线场景的适用性；无 latency 报告。
- D1 的 KS 检验陈述自相矛盾（p<0.05 却称 fail to reject H0），其"截断正态拟合"的统计严谨性存疑——这一瑕疵不影响方法整体，但使"阈值自适应"的理论论证弱于宣传。

---

## 3. D2 — Online Change Point Detection in Application With Transition-Aware Activity Recognition

> **论文定位**：**Boundary Detection（在线变点）+ 下游 Activity Recognition**。Thakur & Biswas, IEEE Trans. Human-Machine Systems 52(6): 1176–1185, 2022。任务文件 §7.15 重点警告：论文报告的高 classification F1 不得自动当成 boundary detection 好——本节逐条核对。

### 7.1 研究问题

智能手机传感器数据流（加速度计 + 陀螺仪）的在线变点检测，用于区分基本活动（BA：sitting/standing/lying/walking/up/down）与**过渡活动**（TA：sit-to-stand、stand-to-sit 等短时活动），实现 transition-aware HAR。动机：过渡活动短时、易被固定窗口漏掉；HMM/semi-HMM 参数估计无解析方法且 forward-backward 计算代价高、数据不平衡（§1，PDF p.1）。

**归属**：Boundary Detection（OCPD 在线分割）+ Activity Recognition（ensemble 分类）。**边界检测性能与识别性能是两回事，论文只报告后者。**

### 7.2 输入数据

连续多元时间序列：智能手机加速度计 + 陀螺仪，50Hz，每点 x_i ∈ R^d。数据集 SBHARPT（UCI 公开，§4，PDF p.7）：30 名志愿者（19–48 岁），手机置于腰部，12 类活动（6 BA + 6 TA），815,614 实例。训练/测试按 70% / 30% 受试者划分（LOOCV），**同受试者数据不跨集**。

**与我们的 UI logs 接近度**：低。纯连续数值流，无离散语义事件、无事件类型、无界面元素。唯一相关点是"过渡活动 = 短时状态"与我们的 POINTER_TRANSITION（短时 pointer 状态）概念可比。

### 7.3 事件 / 观测粒度

一个 observation = 一个采样点（50Hz 的多元传感器读数向量）。分割后以 2.56s 窗口（128 样本）、50% 重叠为单位提取特征（§3，PDF p.5）。**observation 是传感器样本，不是事件。**

### 7.4 预处理

低通椭圆滤波器（20Hz 截止）去除高频噪声 + 高通椭圆滤波器（0.5Hz）去除重力分量 GAcc（§3，PDF p.5–6）。特征工程：155 个时/频域特征（mean、std、range、RMS、correlation、SMA、tilt angle 等 + 谱熵/能量等，§3，PDF p.6）；CFS 特征选择（选 67 个，优于 IG 的 96 个与 ReliefF 的 103 个）；SMOTE 重平衡（TA 是少数类）。

### 7.5 分割单位

先由 OCPD 找变点 c1..cn → 切成 segment S1..Sn（每段 = 两个变点之间的样本）→ **每段再切成 2.56s 固定窗口、50% 重叠**（§3，PDF p.5："Each segment Si is again divided into windows w1...wn, duration of 2.56 s with 50% overlapping"）。**关键：OCPD 只决定窗口的起始位置，segment 内部仍是均匀窗口**，不是变长语义段。最终分类单位是 2.56s 窗口。

### 7.6 边界定义

**统计变点**：OCPD 假设每窗口内至多一个变点；用递归均值/方差（Eq. 1–6）切分窗口，Bartlett's test 检验两侧方差齐性（H0: σ²i=σ²j），检验统计量 Ti（Eq. 7）最大的索引为候选变点；用 p 值与显著性水平 α 比较，α 经 **Benjamini–Hochberg** 过程调整（控制 FDR）以处理多重检验（PDF p.4–5）。**边界 = 方差分布发生统计显著变化的位置**。这是纯粹的统计边界，无任何语义。

### 7.7 在线 vs 离线

**ONLINE（名义）**：OCPD 设计目标"在智能手机上约 28Hz 执行、最小内存"（引用自 Ni et al. [12]，PDF p.4）。但按任务文件 §7.7 的严格标准：方法需要 **k+2p 样本的滑动窗口片段**才能判定一个变点（前后各 padding p 个点）——即它有**窗口级延迟**（至少需要观察变点两侧一段数据），不是 1-sample 实时。且后续分类需要 2.56s 窗口的 128 样本。论文没有报告精确检测延迟（detection delay）值。**名字叫 online，不代表没有 latency（任务文件原话）。**

### 7.8 监督

**两段式**：边界检测 OCPD 是**无监督**的（不依赖分布形式与标签，统计检验）；活动识别是**监督**的（ensemble classifier 需要活动标签，来自 SBHARPT 已有标签）。需要 activity labels，不需要 boundary labels。

### 7.9 模型 / 算法

- OCPD（hypothesis-and-verification，基于 Ni et al.）：递归均值/方差 → Bartlett 方差齐性检验 → 最大化 Ti → p 值 + BH 校正 α → 判定变点。
- 分类：两层 stacking ensemble（level-0: LR, RF, NB, J48, SVM；level-1 meta: LR，PDF p.6）。

Observation → Internal representation → Boundary/Segment：采样点 →（滤波/特征）→ 窗口特征向量 → Bartlett 统计 → 变点 → 分段。**变点产生过程完全基于矩（mean/variance），不建模任何行为语义。**

### 7.10 时长建模

**无显式 duration 模型**。只有固定 2.56s 窗口（50% 重叠）。论文 §1 明确批评固定窗口不适合 TA（"由于 TA 的短时性，难以决定窗口大小"），但它的解法是"变点引导窗口起点 + 固定窗长"，**没有可变时长 segment**。过渡活动被识别好主要靠 SMOTE 重平衡，而非时长建模（§4，PDF p.8）。

### 7.11 噪声鲁棒性

预处理滤波去除高频噪声与重力（§3）。论文对噪声的讨论有限；对"偶发异常点"无专门机制。**未显式建模**（除滤波外）。对类别不平衡专门处理（SMOTE）。

### 7.12 多模态 / 多事件兼容性

原生支持**多元连续数值流**（加速计 XYZ + 陀螺仪 XYZ + 合成量），但都是同构数值通道；**不支持异构事件类型 / 类别特征 / 离散语义事件 / 异步流**。这是传感器数据的"多通道"而非我们的"多模态事件"。

### 7.13 可解释性

输出 segment 标签 = 12 类活动名（walking、sit-to-stand 等），**人类可读**。但这来自监督分类器，不是分割算法本身；OCPD 的变点无语义标签。**分割层面不可解释（只有位置），识别层面可解释（活动名）。**

### 7.14 不确定性

**边界无概率输出**：OCPD 输出 hard change point（虽然内部有 p 值与检验统计量，可作为弱置信度，但论文不作为输出保留）。分类层输出 ensemble 决策，无 posterior。**若我们要保留 boundary confidence，D2 只提供"检验统计量/p 值"这种内部量，需要我们自己暴露。**

### 7.15 评估

**必须严格区分（任务文件 §7.15 核心检查项）**：
- **Boundary Accuracy：论文没有报告。** 全文无 boundary precision/recall/F1、无 tolerance、无 displacement、无变点定位误差（MAE/RMSE 等 D3 定义的变点时间差指标）。
- **Activity Recognition Accuracy（分类指标）**：Table I（PDF p.8）对比三种分割方案（non-overlap / 50% overlap / OCPD）在 2.56s 窗口 + EL 分类下的平均 accuracy：94.89% / 95.58% / **96.22%**。加特征选择 + SMOTE 后：F-Measure **99.80%**、accuracy **99.83%**（Abstract，PDF p.1）。混淆矩阵与逐活动 F-measure（Fig. 5/6）均为识别指标。
- **Downstream Performance：无**（其下游就是识别本身）。
- **评估协议描述不一致（重要，报告核对发现）**：论文 §IV-A 同时声称用 "leave-one-out cross-validation (LOOCV) iterator" 划分 train/validation/test，又说 "70% of the volunteers are selected for training and 30% for testing"（同受试者不跨集），而 §IV-C 的特征选择又使用 "10-fold cross-validation"。这些描述**并不构成一个清楚、标准的单一评估协议**——三种划分方式（LOOCV、70/30 受试者 split、10-fold CV）在同一论文中混用且未说明各自适用位置。因此 **96.22% / 99.80% / 99.83% 这些 downstream recognition 数值即使是真的，也不适合作为我们决定算法优劣的重要数值依据**；它们至多提供量级参考。
- **因此：论文的"OCPD 优于固定窗口"结论只能证明"变点引导窗口起点提升了分类 accuracy"（+1.6pp），完全不能推出"边界检测准确"**。任务文件 §7.15 警告的"不得把 classification F1 当 boundary accuracy"在 D2 上是直接案例。

### 7.16 延迟 / 计算成本

OCPD 目标 ~28Hz 运行（引用 Ni et al.，PDF p.4）；特征/分类阶段无报告。固定 2.56s 窗口意味着**识别延迟 ≥ 2.56s**（一个窗口的数据收集时间）。BH 多重检验增加统计成本但未量化。**Scalability 未讨论。**

### 7.17 超参数敏感性

高度依赖人工设定：窗口大小（2.56s 由图 4 错误率-窗口曲线选定，PDF p.7）、50% 重叠、显著性水平 α、BH 参数、特征选择方法、SMOTE k 值、ensemble 结构。**固定 2.56s 窗口对活动类型的普适性未被证明**（论文只在一个数据集上验证）。

### 7.18 迁移到我们的英语阅读系统

- **可直接迁移**：OCPD 的"滑动窗口内单变点 + 统计检验 + 多重检验校正"作为 **pointer 连续流或 scroll 密集段的在线变点检测器** 是现成候选（我们的 pointer samples 与其传感器流同构——都是高频数值序列）。
- **改造后迁移**：需要把 Bartlett 方差检验换成适合我们的量（如 pointer speed / scroll velocity 的分布变化），且必须验证它对"同 action 内减速"不误报（→ §12 专题三）。SMOTE/ensemble 部分与本项目无关。
- **不可迁移**：两段式（统计分割 + 监督识别）依赖预定义活动类别与大量标签；我们对 action 类别不做监督假设。其"过渡活动"概念可作为 POINTER_TRANSITION 的类比，但不是移植。

### 7.19 这篇论文未确立什么

- **D2 未证明其 activity-recognition F1（99.80%）等于 boundary F1。** 论文无任何边界质量指标。
- D2 未证明 OCPD 在 UI / 事件流 / 非平稳行为流上的适用性（仅在加速度计数据上）。
- D2 未报告检测延迟的精确值（"约 28Hz"来自其引用的 Ni et al.，非本文实测）。
- D2 未证明"统计方差变点 = 语义活动边界"——变点只反映矩变化。
- D2 未讨论时长建模；其"解决过渡活动"是通过重平衡而非时长。
- D2 的评估协议描述不一致（LOOCV / 70%–30% 受试者 split / 10-fold CV 混用），其 96.22% / 99.80% / 99.83% 数值的可靠性受此削弱，**不应作为决定算法优劣的重要数值依据**。D2 的可迁移价值应限定为"online statistical CPD 可作为 continuous stream segmentation 的算法候选"，而非"OCPD 已被证明接近 100% 准确的 segmentation 方法"。

---

## 4. D3 — A Survey of Methods for Time Series Change Point Detection

> **论文定位**：**经典 CPD 方法地图**（截至 2016 的综述）。任务文件 §7.7 特别提醒：不要把它当作截至 2026 的最新方法综述，现代分割方法由 D7 补充。Aminikhanghahi & Cook, Knowledge and Information Systems 51(1): 339–367, 2017。

### 7.1 研究问题

综述性质：枚举、分类、比较时间序列变点检测方法（监督 + 无监督），提出比较准则（online/offline、可扩展性、学习约束、评估方式），列出社区开放挑战。**归属：Survey（覆盖 boundary/segmentation 的方法学地图）。**

### 7.2 输入数据

综述覆盖的时间序列类型：医疗监测（ECG/EEG）、气候、语音、图像/视频、**人类活动（smart home / mobile sensor）**。形式化定义（§2.1，PDF p.3）：time series stream S = {x1,...,xi,...}，x_i ∈ R^d；stationary series；i.i.d.；滑动窗口矩阵 WM；Hankel 矩阵。

**与我们的 UI logs 接近度**：概念层高（定义可用），数据层低（几乎所有方法假设数值时间序列；少数接受离散；无事件语义）。

### 7.3 事件 / 观测粒度

x_t 是 d 维数值向量（按时间戳到达）。部分方法用滑动窗口 X^p 或 Hankel 区间 X_t 作为样本（Def 4/5）。

### 7.4 预处理

综述本身不规定预处理；提到的方法各自要求不同。对非平稳时间序列，部分参数化版本用 forgetting factor 去除旧观测影响（§4.3，PDF p.21）。MDL 方法要求离散化输入（§3.2.6，PDF p.18）。

### 7.5 分割单位

CPD 输出的单位是 **change point（时间位置）**；segment 是变点之间的区间。综述明确区分 change point 与 segmentation/edge detection/event detection/anomaly detection 是"相近概念"（§1，PDF p.1）。**注意：综述把变点检测的产物定义为变点/状态边界，不是 episode。**

### 7.6 边界定义

**统计分布变化**（Def 7，PDF p.4）：H0: PXm = ... = PXn（无变化）vs HA: 存在 m < k* < n 使 PXm = ... = PXk* ≠ PXk*+1 = ... = PXn。变点 = 分布 PXi 发生变化的 k*。这是 D 组对"变点定义"最权威的经典表述——**变点本质上是统计假设检验，与"语义上发生了什么"无直接关系**（→ §12 专题三）。

### 7.7 在线 vs 离线

两者都覆盖（§2.2.1 + §4.1 + Fig. 5，PDF p.4、p.19–20）。**关键概念：ε-real-time**——在线算法至少需要 ε 个新数据样本才能找到变点；完全在线 = 1-real time，完全离线 = ∞-real time。"In practice, no change point detection algorithm operates in perfect real time because it must inspect new data before determining if a change point occurred between the old and new data points." 方法实时度定位：监督方法 n-real time；likelihood ratio n+k-real time；subspace n+k-real time；probabilistic n-real time；kernel n+k-real time；SWAB w-real time；MDL/Shapelet ∞-real time；graph n-real time。**这为任务文件"名字叫 online 不代表没有 latency"提供了最直接的文献表述。**

### 7.8 监督

两者都覆盖：监督（§3.1：多类分类器、二分类器、virtual classifier）需要 boundary 或 state 标签；无监督（§3.2：likelihood ratio / subspace / probabilistic / kernel / graph / clustering）不需要标签，但假设"分布前后变化"。综述指出监督方法在训练数据充足且序列平稳时更准；否则无监督更实用（§4.4，PDF p.23）。

### 7.9 模型 / 算法

无监督六类（§3.2，PDF p.10–18）：
1. **Likelihood ratio**：CUSUM（累计偏差超阈值）、Change Finder（AR 模型 + 双层得分）、**直接密度比估计**（KLIEP / uLSIF / RuLSIF——估计 p(X)/p'(X') 而非密度本身，非参数）、SPLL（半参数）。精度"受数据噪声影响"。
2. **Subspace model**：SI（状态空间 + 噪声，SVD/LQ，观测矩阵 gap）、SST（轨迹矩阵 SVD，无噪声建模，对参数更敏感）。
3. **Probabilistic**：**BCPD（Bayesian online CPD，Adams & MacKay）**——run length 辅助变量 r_t，后验 P(r_t|x_1:t)，hazard function H(τ)；复杂度 n²→n；**输出 run-length 后验分布（uncertainty 的直接来源）**。GP change：用高斯过程做预测分布 + p 值检验。
4. **Kernel-based**：KFDR（kernel Fisher discriminant ratio），对核选择敏感。
5. **Graph-based**：图两样本检验（MST / 近邻 / visibility graph），非参数、高维友好，但"不利用时间序列观测本身的信息"。
6. **Clustering**：SWAB（滑动窗口+bottom-up）、MDL（离散数据）、Shapelet（u-shapelet）、Model fitting（新点不适合任何簇 = 变点）。

### 7.10 时长建模

**无显式 duration 模型**。BCPD 的 run-length 有 hazard 先验（对状态长度有几何式先验），但不是显式 duration 分布。综述不涉及 HSMM（HSMM 在 D4/D7 中）。**这是 D3 与 D4 的关键分野。**

### 7.11 噪声鲁棒性

综述级判断（§4.4，PDF p.23）："kernel-based methods、subspace models、CUSUM、AR 和 clustering 方法依赖参数建模时间序列动态，对噪声数据和高度动态系统表现不佳。"非参数方法（密度比、graph）通常更稳健；但无正式鲁棒性分析（§5 指出是开放问题）。

### 7.12 多模态 / 多事件兼容性

- 维度：似然比与子空间方法最初设计为 1-D（多维时合并为 d 值向量）；其他方法接受多维（成本随维度增加）。所有算法接受离散与连续输入（**唯一例外 MDL 只接受离散**，§4.3，PDF p.21）。
- **对异构事件流**：综述不涉及。全部方法都假设"同构数值序列"；无事件类型 / 类别属性 / 语义对象概念。**需要先编码/向量化才能用。**

### 7.13 可解释性

变点位置是硬输出，无标签（除非用监督分类器）。**Latent-ID only / 位置 only。** 对后续 process modeling 的可用性有限——需另行把变点映射到行为语义。

### 7.14 不确定性

部分方法天然有：BCPD 输出 P(r_t|x_1:t)（run-length 后验，即"距上个变点有多久"的概率分布）；GP 方法输出 p 值。其余（CUSUM、kernel、graph、clustering、subspace）输出 hard boundary 或得分阈值。**BCPD 是 D 组中边界不确定性最强的现成模板。**

### 7.15 评估

综述给出了 CPD 评估指标的权威分类（§2.3，PDF p.6–8）：
- **变点 yes/no（二分类）**：accuracy、sensitivity/recall、**G-mean**（CPD 类别高度不平衡，G-mean 比 accuracy 更适合）、precision、F-measure、ROC/AUC、PR curve。
- **变点时间差**：**MAE / MSE / MSD（带方向）/ RMSE / NRMSE**——"If the difference in time between the detected change point and the actual CP represents the measure of performance, then the above metrics [classification] are not appropriate."
- 实证（§4.4, Table 4）：各数据集分散（语音 CENSREC、ECG、法语电视语音、BCI、NDVI、Smart Home、HASC 活动数据）；"A majority of the studies do not provide any comparisons, or in some cases, even measures of performance"；RuLSIF 一致较准；监督在数据足+平稳时更准。**没有统一 benchmark，跨论文直接比较不成立（任务文件 §29）。**

### 7.16 延迟 / 计算成本

Table 2（PDF p.20）：CUSUM O(n²)、AR O(n³)、KLIEP < CUSUM、uLSIF < KLIEP、RuLSIF < uLSIF、SPLL O(n²)、Bayesian O(n)、GP O(n²)、KcpA O(n³)、SWAB O(Ln)。"非参数方法随维度增加更便宜；参数方法成本更高且扩展性差。"**没有现有 CPD 算法提供 interruptible/contract anytime 选项**（开放方向）。

### 7.17 超参数敏感性

综述指出：几乎所有方法依赖窗口大小（§5："change detection depends on the window size... variable window sizes may provide a good solution"）；阈值选择困难（"may be application dependent and they may change over time"，PDF p.24–25）；参数方法对初值敏感（§2.2.3）；核方法对核及参数敏感（§3.2.4）。

### 7.18 迁移到我们的英语阅读系统

- **可直接迁移**：① ε-real-time 概念——评估我们未来在线分割器"需要多少未来上下文/延迟"的语言工具；② 评估指标分类（分类 vs 时间差）直接构成我们 §24 Evaluation Framework 的 boundary 层；③ BCPD 的 run-length 后验作为"边界置信度"模板（→ §17）；④ RuLSIF 类的直接密度比作为 pointer 段变点的候选非参数方法。
- **改造后迁移**：CPD 假设平稳/i.i.d.（Table 3 显示 SPLL/SST/GP/BCPD 原始版/KcpA/graph 需要 i.i.d. 或平稳）——我们的 UI 流**非平稳、非 i.i.d.**，需用参数化变体或先做去趋势。多数方法需先向量化异构事件。
- **不可迁移**：语义事件本身（answer click 等）不需要 CPD；CPD 对"事件序列 + 语义对象"无建模能力。

### 7.19 这篇论文未确立什么

- D3 截至 2016，**不覆盖 2017–2024 的现代 BD/SD 方法**（由 D7 补）。
- D3 未给出"哪种 CPD 方法在 UI 交互流上有效"的证据——其数据集全部是传感器/生理/气候/语音。
- D3 未证明"统计变点 = 语义边界"；其定义恰恰暗示二者不同（Def 7 只说分布变化）。
- D3 未提供统一 benchmark 或鲁棒性分析（其 §5 明确列为开放问题）。

---

## 5. D4 — Unsupervised Segmentation of Hidden Semi-Markov Non-Stationary Chains

> **论文定位**：**Latent-State Segmentation（HSMM / 显式 duration / 非平稳）**。任务文件 §7.10 强调必须把**数学机制与领域实证分开**——本节严格分开：数学机制（§7.9、§13）可迁移；领域实证（雷达图像）仅作参照。Lapuyade-Lahorgue & Pieczynski, Signal Processing 92(1): 29–42, 2012。

### 7.1 研究问题

提出能**同时**处理 (1) semi-Markovianity（状态停留时间任意分布）与 (2) 非平稳性（有限个不同参数集合/stationarities）的隐藏链模型 NS-HSMC / NS-RHSMC，配合 ICE 参数估计实现**无监督贝叶斯分割**（MPM）。应用背景：雷达图像分割（论文自证领域）。**归属：Segmentation（latent-state / 逐点状态标签）——不是 boundary detection（边界是状态标签的副产品），不是 activity recognition（状态是 latent ID，非命名活动）。**

### 7.2 输入数据

一维序列 y = (y1,...,yN)，y_n ∈ R（论文实验用一维化像素序列，256×256 图像经 Hilbert–Peano 扫描转为一维）。观测服从 Gaussian 噪声分布 p(y_n|x_n)。无监督：参数从观测估计。

**与我们的 UI logs 接近度**：低（输入是连续数值标量序列）；但**机制可迁移性高**——若我们把 pointer 特征（速度、方向）或 scroll 特征重采样为连续序列，HSMM 可作用其上。

### 7.3 事件 / 观测粒度

一个 observation = 一个连续数值样本 y_n（如像素灰度）。隐藏状态 x_n ∈ {o1,...,oK}。无事件概念。

### 7.4 预处理

论文无专用预处理（信号本身）。实验把 2D 图像扫描成 1D 序列（Hilbert–Peano）。**无去噪、无特征提取。**

### 7.5 分割单位

输出是**逐点隐藏状态标签序列** x̂_n = argmax p(x_n|y)（MPM，§2，PDF p.2）。segment = 连续同状态标签的区间。**边界是状态标签变化的副产品，不是显式产物**（与 D7 对 SD 方法的定义一致）。

### 7.6 边界定义

**隐式边界**：边界发生在 p(x_{n-1}) ≠ p(x_n)（状态切换）处。状态的切换由转移概率 + 停留时间分布共同决定（§3.1）。**没有显式 boundary model / 变点检验**——边界是 MPM 状态解码的自然结果。这正是 D7 所说"SD 方法的边界是状态分配的天然副产品"。

### 7.7 在线 vs 离线

**OFFLINE（本文方法）**：forward-backward（α_n、β_n 递归，§5 Eq. 5.1–5.7）需要完整序列才能算逐点后验；ICE 参数估计也是批处理迭代。论文未提供在线推理。（D7 提到 HDP-HSMM 等变体，但其 Table 1 显示 SD 方法大多不支持在线。）

### 7.8 监督

**Unsupervised**：参数（转移、停留时间分布、Gaussian 噪声参数）全部从观测用 ICE 估计（§4.1）。**无需边界标签、状态标签、状态数以外的先验。** 但需指定状态数 K（本文固定 K=2 或 3）与停留时间上界 P（RHSMC 的 L1={0,...,P−1}）。

### 7.9 模型 / 算法

**数学机制（可直接迁移的核心）**：
- HMC（Eq. 2.1）：p(x,y) = p(x1)·∏p(x_{n+1}|x_n)·∏p(y_n|x_n)。**关键定理：standard discrete HMM 隐含 geometric 停留时间分布**——p_ok(m) = (λ_kk)^m·(1−λ_kk)（D4 §3.1 原话为 "necessarily of exponential form"，即离散情形下的 geometric；本报告统一用 geometric）。
- HSMC：停留时间分布可以是**任意形式**；X 由初始分布 + 转移 p*(x_{n+1}|x_n)（强制 x_{n+1}≠x_n）+ 每状态停留时间分布 p_ok(m) 定义。HSMC 可表示为 TMC T=(X,U,Y)，U_n = 状态 X_n 的**剩余停留时间**（§3.1，PDF p.3）。
- **RHSMC（Recent HSMC，论文关键变体）**：停留时间上界 P、U_n ∈ {0,...,P−1} 表示**最小停留时间**；允许自转移 q(x_{n+1}|x_n) ≠ 0；**计算复杂度线性 O(N)**（区别于经典 HSMC 的多项式/二次复杂度）。RHSMC 在最小停留时间为 0 概率为 1 时退化为普通 Markov chain。
- **NS（非平稳）扩展**：引入第三链 U2 建模不同参数集合（不同 stationarity），T=(X,U1,U2,Y)（§3.2–3.4）。
- **参数估计 ICE**（§4.1）：完整数据估计器 + 条件期望/抽样迭代；比 EM 更一般（不需要似然最大化）；与 EM 在指数族 + ML 估计器时序列等价；实验显示与 EM 效果相当。
- **分割**：MPM 用前向-后向归一化概率（Eq. 5.1–5.7）算逐点后验 p(x_n|y)、p(v_n|y)。

Observation → Internal representation → Segment：y_n →（模型参数 ICE 估计）→ 逐点后验 p(x_n|y) → MPM 标签序列 → 连续同标签段。**边界由"状态 + 停留时间"联合解码产生。**

### 7.10 时长建模

**核心论文，重点分析**：显式 duration 分布 p_ok(m)（HSMC）与最小停留时间分布（RHSMC）。**这正是任务文件 §7.10 要求的核心机制**：HMM 停留时间隐含 geometric（无法表达"最少停留 X 秒"或"平均停留 Y 秒且方差小"），HSMM 可显式指定任意时长分布。对"POINTER_TRANSITION（短）vs READING-LIKE EPISODE（长）"这种时长差异，HSMM 提供理论上的表达力（→ §13 专题四）。**但**：论文也给出反向证据——当数据其实没有时长结构时，显式时长模型无增益甚至略差（见 §7.19）。

### 7.11 噪声鲁棒性

Gaussian 噪声显式建模（观测分布），但对"偶发离群点/缺失事件"无专门处理（噪声被吸收进 emission 分布）。论文实验包含高噪声档（σ²=10、σ²=20），结论：噪声越强，复杂模型（RHSMC vs HMC）的优势越容易因参数估计变差而消失（§5.1 高噪声档 RHSMC 反而略差）。

### 7.12 多模态 / 多事件兼容性

**低**：模型面向一维连续观测；论文未讨论多维/离散观测（虽然理论上 emission 可推广）。对异构事件流需要先把所有事件编码/向量化为同构观测序列，且**必须重采样为等间隔或处理非等间隔**——论文未提供该机制。**Mixed events 需大量 encoding。**

### 7.13 可解释性

输出是 latent state ID（o1/o2/o3），**latent ID only**。论文在雷达实验中把状态人工对应"water/vegetation/others"（§5.4，PDF p.12），但这是事后命名。**任务文件 §7.13 警告：latent state 不能自动命名成 reading cognition**——D4 的状态必须由我们定义语义映射（如 pointer-active / pointer-inactive / text-following），且该映射需要独立验证。

### 7.14 不确定性

**强**（D 组最完整）：MPM 直接输出逐点后验 p(x_n|y)、p(v_n|y)、p(v_n,v_{n+1}|y)（§2 Eq. 2.5–2.6、§5 Eq. 5.5–5.7）。**每个时间点的状态概率都可得**——这是"boundary confidence 有理论依据"的最强来源（→ §17）。

### 7.15 评估

- **指标**：逐点误分类率（misclassification rate t = 误分类点比例），PDF p.8–12。这是 **Segment/State label accuracy**（点级），**不是 boundary accuracy**——没有变点定位误差/边界 F1。
- 实验 1（§5.1，数据是 HMC）：低噪声两模型一致（t≈0）；高噪声（σ²=10）RHSMC 略差于 HMC（t=18.38% vs 监督 17.42%）。
- 实验 2（§5.2，数据是 RHSMC）：极高噪声（σ²=20）两模型类似。
- 实验 3（§5.3，手工非平稳图像，数据既非 HMC 也非 HSMC）：**NS-RHSMC 类错误率 25% < NS-HMC 30% < HMC 32%**；纹理（U2）恢复 NS-RHSMC 9% << NS-HMC 18%。这是"数据满足 HSMC 假设时显式时长模型显著更好"的直接证据。
- 实验 4（§5.4，真实 SAR 图像）：无 GT；HSMC 与 NS-HMC 都比 HMC 好（HMC 产生假的"water"区域），但 **HSMC 与 NS-HSMC 差异可忽略**。
- **Bottom line**：唯一一次真实数据（SAR）实验没有 GT，结论定性；模拟实验显示模型收益完全依赖数据是否符合模型假设。

### 7.16 延迟 / 计算成本

RHSMC 的关键卖点是**线性复杂度 O(N)**（§3.3，PDF p.4："offering the possibility of Bayesian classification with complexity linear in time"）；经典 HSMC 停留时间无界导致多项式复杂度（U 状态数 O(N) 上界）。ICE 迭代估计（无迭代次数报告）。**在线无。**

### 7.17 超参数敏感性

需指定：状态数 K（核心超参，论文未讨论如何选）、RHSMC 停留时间上界 P（实验用 4/10）、非平稳数 L、Gaussian 分布形式、ICE 初始化与迭代。**NS-RHSMC 参数远多于 HMC**——这正是它在简单数据上反而差的机制原因（§5.1 明示"using HMC directly needs fewer parameters to be estimated"）。

### 7.18 迁移到我们的英语阅读系统

- **可直接迁移（数学机制）**：① HSMM 显式时长分布 → 对 POINTER_INACTIVE_EPISODE / READING-LIKE POINTER EPISODE 的时长建模（任务文件 §7.10/§11 的场景）；② RHSMC 线性复杂度变体 → 避免经典 HSMM 二次复杂度的工程路径；③ MPM 逐点后验 → boundary/state confidence 输出；④ 非平稳扩展 → 不同学生/不同会话的模型参数漂移。
- **改造后迁移**：需要先把异构事件流编码/重采样为等间隔数值序列（本论文不提供该机制）；需要把 latent state 映射到行为 vocabulary（需独立语义验证）；需要在线推理方案（论文是离线）。**全部属于 PROJECT TRANSFER INFERENCE。**
- **不可迁移**：雷达图像分割的实证数值（t=9%~32%）；"状态数=2/3"的假设；Gaussian emission。

### 7.19 这篇论文未确立什么

- D4 未证明 HSMM 在我们的 **UI 行为流**上有效——其全部实证在合成序列 + 雷达图像。
- D4 未证明"显式时长模型总是优于 HMM"——恰恰相反，它证明当数据是 HMC 时 RHSMC 无增益、高噪声下略差（§5.1）；只有数据真正有非马尔可夫时长/非平稳结构时才有优势（§5.3）。
- D4 未提供 boundary accuracy（只有点级误分类率）。
- D4 未提供在线推理、异构事件输入、语义可解释状态。

---

## 6. D5 — Recognizing Task-Level Events from User Interaction Data

> **论文定位**：**UI-Specific Task Abstraction（low-level UI interactions → task-level events）**，D 组最高优先级。任务文件 §12 要求详细还原其 pipeline 并回答 10 问；§14 要求明确"它所谓 task-level event 与我们 micro-action 粒度差多少"。Rebmann & van der Aa, Information Systems 124: 102404, 2024。

### 7.1 研究问题

用户交互数据（UI 事件）不能直接用于 process mining，因为不满足两个要求：(1) 事件不指明与 process-level activity 的关系；(2) 事件不指明与特定 process execution 的关系（§1，PDF p.1–2）。论文提出**无监督**方法把 UI 事件流转换为 task-level events：segmentation（识别任务）→ categorization（识别类型）→ object-instance 关联（识别任务与过程执行的关系）。**归属：Segmentation + Task Abstraction + Categorization**（其"任务边界"对应我们的 action episode 边界层，粒度不同，见 §7.18）。

### 7.2 输入数据

用户交互事件流：事件 u = (uid, ts, P, V)，P = context 属性集（交互类型 + 受影响的 UI 元素信息），V = data 属性集（用户输入的数据）（§3，PDF p.3）。示例：u6 = (u6, 15:43:29, {input, Chrome, field, Search}, {Pete Miller})。事件类是 context 属性的集合（如 {input, Chrome, field, Search}）。评估用 8 个任务日志（3 来源：Leno et al.、Agostinelli et al. tutorial、Abb & Rehse 的 SAP 数据），组合成 3 个评价日志 L_U1（200 任务/6114 事件）、L_U2（240/9054）、L_U3（120/1386）（§5.1，Table 2，PDF p.8）。

**与我们的 UI logs 接近度**：**D 组最高**。事件已带 (type, timestamp, context/UI element, data value) 结构，与我们的 click/underline/answer 语义事件同构（都是"离散语义动作 + 目标元素 + 数据"）。**唯一缺：连续 pointer/scroll 采样流**——D5 的事件是离散 UI action，不含连续数值序列。

### 7.3 事件 / 观测粒度

一个 observation = 一个用户交互事件（click button、input field、tick checkbox 等），带属性集。**比我们的 raw events 高一级**：我们已经把 pointer_sample、scroll 视为低层；D5 把 click/input 视为最低层（更接近我们预处理后的 semantic events）。

### 7.4 预处理

无显式去噪/重采样；但做了**数据清洗层的"语义去噪"**：识别"overhead sub-tasks"（登录、启动应用、开文件）并在任务识别中不把其当作独立任务（§4.2.2(3)，PDF p.6）。事件类统一用全局共现矩阵索引（增量构建）。**无 dedup 讨论、无窗口。**

### 7.5 分割单位

**Task**（任务级事件）：te = (tid, type, ts, D, objects)，D 含 lifecycle（start/complete），objects 是过程相关对象实例（§3，PDF p.3）。每个任务输出 start 和 complete 两个 task-level event（§4.4，PDF p.7）。**单位 = 任务（task），粒度明显大于我们的 micro-action episode**（详见 §7.18 与 §14）。

### 7.6 边界定义

**任务边界 = chunk 完成 + 四个分段检查**（§4.2，Algorithm 1 的 endsTask，PDF p.4–6）：
- **Chunking**（completesChunk）：用 20 个 completion 关键词（来自 IBM 设计指南：ok/submit/send/save 等）判定子任务完成点。
- **Segmenting**（endsTask）：chunk c_i 判定为任务终点当且仅当满足四个条件之一组合：
  1. **上下文不相关**：全局共现矩阵中 c_i 与 c_{i+1} 的 event-class 质心余弦相似度 sim < t（t 默认 0.3）；
  2. **无数据值重叠**：c_i 最后两事件与 c_{i+1} 前两事件的属性 V 无精确匹配（如订单号 O008102 跨 chunk 出现则不切）；
  3. **c_i 不是 overhead**：c_i 最后两事件类含 overhead 关键词（log in/sign up/reload/open）则不切；
  4. **控制流非确定性**：count(c_i.P) ≠ count(DF(c_i.P, c_{i+1}.P))（即 c_i 后行为并不总是相同）；仅当 count(c_i.P) ≥ 3 时应用。
- **边界定义本质**：语义（关键词）+ 上下文统计（共现相似度）+ 数据（值重叠）+ 控制流（直接跟随确定性）的**混合规则**。**不是统计变点、不是 duration 阈值**（其 Future Work §7.3 明说未利用时间戳——"does not consider event timestamps"）。

### 7.7 在线 vs 离线

**BOTH**（D 组唯一同时支持双设置的论文）：
- Online：事件到达即处理，缓冲 B 存单个任务的完整事件；object-instance 逐事件识别；task-identification 用增量共现矩阵；task-categorization 用在线聚类（DenStream）。可处理 unseen 任务类型（无需重训）。在线主要代价：categorization 因聚类模型训练需 warm-up，略降（§5.3.5，PDF p.12）。
- Offline：先对整日志做 task identification，再 categorization；categorization 相当于全日志 warm-up。
- **延迟**：object 识别 1–107ms/事件，task 识别 2–4ms/事件，task categorization 40–150ms/任务；平均交互间隔 >2.5s，可实时跟上（§5.3.7，PDF p.12）。内存 < 存全部事件所需内存的 1%。
- **关键含义（严格限定）**：D5 只证明 **"Online + Offline both feasible → SUPPORTED"**（同一套算法按运行模式切换）；它**没有**展示"先在线输出 provisional boundary，会话结束后离线修改历史 boundary"（即 retrospective revision）。其 warm-up 更接近 **delayed commitment**（推迟到模型成熟再决断），而非修改已输出的边界。因此 **"Online provisional + Offline retrospective refinement" 应标为 PROJECT ARCHITECTURE HYPOTHESIS，不能说已被 D5 验证**（→ §16、§27 Q12）。

### 7.8 监督

**Unsupervised**：无任务标签、无边界标签、无任务模板。但含人工知识：20 个 completion 关键词、overhead 关键词集、UI-object 去除词表 K_U、上下文相似度阈值 t、缓冲大小 b、向量长度 s_v。任务类型**无需预定义**，由在线聚类发现。Object GT 是作者人工标注（§5.1.1，PDF p.8）。

### 7.9 模型 / 算法

三组件流水线（Fig. 1、Algorithm 1）：
1. **Object-instance identification**（§4.1）：Type extraction（POS tagger spaCy 提取名词 → 去除 UI 对象名词 → 得对象类型 o_t）+ Instance recognition（正则识别数字 ID/URL/email + NER 识别命名实体 → 拼接成对象标识 o_i）→ 对象实例 (o_i, o_t)。
2. **Task identification**（§4.2）：Chunking（completesChunk）+ Segmenting（endsTask 四检查，见 §7.6）+ 后处理（dequeue 任务事件）。
3. **Task categorization**（§4.3）：任务 → 特征向量（唯一事件类数 + 每事件类频率，固定长度 s_v=1000 默认）→ **DenStream 在线密度聚类**（DBSCAN 变体，动态微簇，无需指定簇数）→ 簇 = 任务类型 → **tf-idf 最高词生成文本标签**（如 "Create order"）。

Observation → Internal representation → Segment/Task：事件流 →（对象识别）→ chunk（子任务）→（四检查）→ task 段 →（向量化 + DenStream）→ task type + 文本标签 → task-level events（start/complete + objects）。**边界 + 类型 + 关联一次性端到端产生。**

### 7.10 时长建模

**无显式 duration 模型**：不用时间戳（§7.3 明确 Future Work）。任务长度由事件数决定（feature 向量含事件类数）。对"短 burst vs 长 episode"的时长结构无建模能力。**这是 D5 对本项目最直接的缺口：SCROLL_BURST / READING-LIKE EPISODE 的时长是我们关心的，D5 不用时间。**

### 7.11 噪声鲁棒性

- overhead 检测（§4.2.2(3)）可视为语义噪声处理（登录/开应用不当作任务）。
- 对"偶发事件/重复/缺失"无显式机制；上下文共现矩阵对冷启动（warm-up 前）敏感（论文建议 warm-up）。
- **弱项**：若事件含噪（如误点击产生的孤立 chunk），共现相似度可能误判边界；论文未做专门噪声注入实验。**Robust 程度中等，靠 warm-up 与多检查互补。**

### 7.12 多模态 / 多事件兼容性

**原生支持异构事件**：事件 = (context 属性集 P, data 属性集 V)，天然容纳 click/input/checkbox 等多类型 + 多应用（Mail/Chrome/SAP）+ 数据值。**它是 D 组中对"异构语义事件流"兼容性最强的方法**（无需编码，直接处理类别化事件类）。但**不支持连续数值流**（pointer/scroll 采样需先聚合或映射成事件类才能进 pipeline）。

### 7.13 可解释性

**高（D 组最强），但必须拆开两种确定性（反馈明确要求）**：
- **Task identification（边界判定）**：由 completion 关键词 + 四检查（上下文/数据重叠/overhead/控制流）组成，**在参数与历史状态固定后，是 rule-based / largely deterministic 的边界逻辑**——同一事件流 + 同一历史 → 相同 chunk/段。
- **Task categorization（类型指派）**：用 **DenStream online clustering**，结果是**随 stream order、warm-up 位置、聚类模型既往状态动态变化**的——同一事件流在不同到达顺序/不同 warm-up 下可能得到不同簇指派。**这是 adaptive、history-dependent 的，不是 deterministic。**
- 输出 task-level events 带文本标签（tf-idf 生成）、对象实例、lifecycle，人类可读、可审计。

**因此不应把整套 D5 归入"确定性方法"：边界识别 largely deterministic（given model/history），任务类型分类是 history-dependent 的在线聚类。**

### 7.14 不确定性

**无概率输出**：边界判定是四个检查的硬决定；任务类型是硬簇指派。唯一"软"信号是上下文相似度 sim(c_i,c_{i+1})（可与阈值 t 比较），论文不作置信度输出。**任务文件 §7.14 需明确标记：D5 无 uncertainty。**

### 7.15 评估

**评估对象：task identification + task categorization + object identification，均非 boundary accuracy**：
- Object identification：Precision/Recall/F1（对人工标注 GT），S_U1 F1 0.90、S_U2 0.94。
- **Task identification**：`#tasks`（识别数量 vs GT 数量）+ **normalized edit distance (n.ED)**（识别任务与最近 GT 任务的归一化编辑距离，衡量 segment 内容相似度）——**这不是 boundary F1**，编辑距离对边界位置不敏感（一个任务整体错位但内容相似仍可得低距离）。Online 结果：n.ED 0.04/0.05/0.17（S_U1/2/3）。
- **Task categorization**：Rand index（micro/macro）+ Jaccard（micro/macro）——聚类指标，衡量"任务对是否同类型"。Online R(ma)：0.97/0.97/0.99。
- 消融（Table 5，PDF p.11）：full=0.04/0.05/0.17；control-flow+semantic=0.04/0.05/0.27；control-flow+data=0.35/0.33/0.17；control-flow only=0.42/0.38/0.27 → **语义视角对 S_U1/2 关键、数据视角对 S_U3 关键，只有三视角联合才整体好**。
- 对比 baseline：在线 BL_dfg（back-edge，Leno）n.ED 0.32–0.83 很差；BL_co-oc（Urabe 在线版）n.ED 0.33–0.37 但**结果高度依赖两个参数（不同配置编辑距离差高达 0.5）**。离线 ours 0.04/0.05/0.17 vs BL_urabe(best) 0.28/0.28/0.66、BL_leno 0.35/0.26/0.48。
- Warm-up（Table 4）：task identification 不受 warm-up 影响；categorization 在 warm-up 覆盖全部任务类型时提升（S_U1 从 0.84→0.97 R(ma)）。
- 个体日志（Table 7）：n.ED 0.01–0.29；Leno 在重复性任务（log 1/5/6）完美（0.00），说明 back-edge 对重复任务的强项。
- **Gap**：无 boundary precision/recall/F1、无 tolerance、无 displacement。**任务文件 §7.15 三类指标，D5 只报告了 Segment quality（编辑距离）与 Activity accuracy（聚类），且它自己承认"没有公开的含多任务类型的带 GT 交互流"（§5.1），用组合日志模拟——生态效度受限（§7.2 也承认）。**

### 7.16 延迟 / 计算成本

见 §7.7：object 1–107ms/事件、task-ident 2–4ms/事件、task-categorize 40–150ms/任务；内存 <1% 存全事件。缓冲区 b=250（覆盖最长任务事件数的 3 倍）。**成本可控，实时可行。**

### 7.17 超参数敏感性

人工参数：缓冲大小 b（250）、上下文相似度阈值 t（0.3）、completion 关键词集（20 词）、overhead 关键词集、UI 对象词表 K_U、向量长度 s_v（1000）、DenStream 密度参数、warm-up 长度。**其中关键词集与词表是领域知识（§7.2 承认其完整性不确定）；t 与 b 有默认值但未做敏感性网格分析**（对比：BL_co-oc 的参数敏感性差 0.5 编辑距离，论文借此说明自己不依赖用户参数——但自己不依赖的是"簇数"，关键词与阈值仍是人工的）。

### 7.18 迁移到我们的英语阅读系统

- **可直接迁移**：① 三组件架构（对象/任务识别/类型）——我们可用"语义目标（question/passage/选项/文本段）+ 事件类型"构建事件类；② **chunking + 四检查**作为 SCROLL_BURST/ANSWER_CHANGE/OPTION_ELIMINATION 等已知模式的分段规则模板（注意其边界识别 largely deterministic，类型分类是 history-dependent 在线聚类，§7.13）；③ overhead 检测（passage 无关的 UI 噪声）；④ DenStream 在线聚类发现未预定义的 action 类型；⑤ 双设置（online/offline both feasible）——**注意 "online provisional + offline retrospective refinement" 是项目假设而非 D5 验证的（§16）**；⑥ tf-idf 文本标签 → 可读 action label。
- **改造后迁移**：D5 不用时间戳——我们的 SCROLL_BURST 必须加时间间隔阈值（→ §20）；D5 无连续流支持——pointer/scroll 采样需先做一级聚合（→ §21）；D5 假设顺序任务（不交错）——我们的学生可能 passage/question 交替，需放宽（§7.2 承认该限制对全部无监督方法适用）。
- **不可迁移**：对象实例识别（我们无"订单号/客户名"这类跨任务对象，我们的"对象"是页面语义区域，可借用但语义不同）；RPA 任务级粒度（见下）。

**粒度差异（任务文件 §12 必须明确）**：D5 的 task（如"create order"，10–70+ 事件、跨多个应用）**明显大于**我们的 micro-action（SCROLL_BURST、POINTER_TRANSITION 是单一行为的短段）。我们的"action episode"在 D5 的粒度层级中大致对应它的 **chunk/子任务**级别，甚至是 chunk 内部模式。**因此 D5 的方法论（边界判定逻辑、聚类、双设置）可迁移，但其"任务边界"定义（completion 关键词 + 跨 chunk 语义）不能直接当作我们 micro-action 的边界定义**——我们需要自己的边界定义，粒度更细（→ §14）。

### 7.19 这篇论文未确立什么

- D5 未证明其边界在 **micro-action 粒度**上有效（其评估对象是任务级）。
- D5 未报告 boundary accuracy（编辑距离 ≠ 边界 F1）。
- D5 未建模 duration / 时间间隔（明言 Future Work）。
- D5 未处理连续流（pointer/scroll 采样）。
- D5 未在真实工作日的任务序列上验证（组合日志模拟，作者自认限制）。
- D5 未处理任务交错（顺序假设）。
- D5 的 completion/overhead 关键词集完整性与 UI 词表可能存在数据偏差（§7.2）。

---

## 7. D6 — A Grammar-Based Approach for Applying Visualization Taxonomies to Interaction Logs

> **论文定位**：**Rule / Grammar-Based Event Abstraction（Task Abstraction，deterministic / interpretable 路线）**。任务文件 §9 把它作为"规则/语法路线的代表"；它代表我们"确定性、可解释分割"的路线。Gathani, Monadjemi, Ottley & Battle, Computer Graphics Forum (EuroVis 2022) 41(3): 489–500。

### 7.1 研究问题

把已有的可视化任务分类学（taxonomies）形式化为 **regular grammar**，使高层任务/目标能**程序化**应用于交互日志分析，弥合"理论分类学"与"经验日志数据"之间的鸿沟。**归属：Task Abstraction（deterministic mapping）；它本身不做 segmentation 评估，而是评估 taxonomy 的表达力（coverage/diversity）。**

### 7.2 输入数据

3 个可视化交互日志数据集：Battle & Heer（Tableau 探索，4 个子数据集：flight performance 15 参与者、wildlife strikes 17、weather 16、brightkite 16，Table 1 核对）、Liu & Heer（imMens 大数据探索，flight performance 16 参与者）、Wall（政治家决策可视化，24 参与者）。日志记录是**离散交互事件**（如 mouseover_from_list、change_attribute_distribution、filter_changed）。**与我们的 UI logs 接近度：中**——同为离散交互事件流，但粒度是"界面动作级"（与 D5 相当），无连续采样；领域是可视化分析而非阅读。

### 7.3 事件 / 观测粒度

一个 observation = 一个**交互日志记录（distinct log record）**，如鼠标事件、过滤操作等。**terminal symbol 是最原始交互类别**（如 Brehmer & Munzner 的 11 类：encode/select/navigate/arrange/change/filter/aggregate/annotate/import/derive/record）。

### 7.4 预处理

**人工映射即预处理**：用定性编码（qualitative coding）把每个 distinct log record 映射到 terminal symbol（§4.3，PDF p.5–6）。流程：两名研究者独立编码（首轮 inter-rater reliability 0.47）→ 讨论（0.91）→ 另两名复核（0.99）。无法映射的记 null terminal（如 Tableau 的 reset 无法映射到 Gotz & Zhou）。**无去重/无归一化/无窗口；映射本身是人工建立的 code-book（JSON），这是巨大的预处理成本。**

### 7.5 分割单位

输出是 **terminal 序列（Σ 串）与 non-terminal 匹配（正则表达式匹配的 pattern 实例）**（§4.5，§5.2）。**单位 = 分类学类别映射 + 高层 pattern 的出现位置**；不是传统 segment，而是"日志中哪些片段匹配某个高层模式（如 information-seeking mantra）"。

### 7.6 边界定义

**Grammar 匹配**：non-terminal（高层模式）由 regular expression over terminals 定义（如 overview → (aggregate|arrange|encode)*），在 terminal 流上做正则匹配，匹配片段 = 模式实例（§3.2，PDF p.4）。**边界 = pattern 匹配的起止位置**。**有明确边界模型（正则匹配），但是"模式完成/开始"型，与统计变点无关。**

### 7.7 在线 vs 离线

**OFFLINE**（论文实现）：对所有日志先做 terminal 映射，再在完整序列上做正则匹配。**无在线讨论**——但正则表达式匹配本身可在流上增量做（属 PROJECT TRANSFER INFERENCE，论文未讨论）。

### 7.8 监督

**Rule-based / 人工定义**：terminal 映射（12 个 code-book = 3 数据集 × 4 低层分类学）、non-terminal 正则（12 个 = 4 底层 × 3 高层）。**不需要标签（无监督意义上的），但需要人工定义词汇表与语法**（任务文件 §9：优点是"no labels"，缺点"requires handcrafted grammar"）。inter-rater reliability 0.99（terminal）与 1.0（non-terminal）说明映射一致性高，但也说明映射是劳动密集型。

### 7.9 模型 / 算法

**Regular grammar**（§3.1）：G = (Σ, N, P)，Σ = terminals（低层交互），N = non-terminals（高层行为模式），production rules f: N → {Σ∪N}*。交互=词，交互模式=句子结构（语言学的结构平行）。示例（§3.2）：BM 的 11 terminal；Shneiderman ISM 的 non-terminals：overview → (aggregate|arrange|encode)*、zoom → (navigate)+、filter → (filter)+、details_on_demand → (select|derive)+。匹配用正则表达式引擎，递归支持多层嵌套。

Observation → Internal representation → Segment：log record →（人工 code-book）→ terminal →（正则）→ non-terminal pattern 实例。**完全确定性、可审计。**

### 7.10 时长建模

**无 duration 模型**；且论文明言 **grammar 无法表达交互时序**（§6："inability to express timing of interactions because of the use of grammar-based approach"）——这是对"语法路线"的根本限制之一。

### 7.11 噪声鲁棒性

**低**：无噪声机制。无关/无法映射的记录进 null terminal（丢失，不报错）；对偶发事件、重复、异常无专门处理。**未考虑。**

### 7.12 多模态 / 多事件兼容性

终端映射层面可处理任意事件类型（只要 code-book 覆盖）；但**粒度与结构不一致是论文发现的核心障碍之一**（§6：日志数据集之间的 granularity 与 structure 不一致）。不同系统日志（Tableau vs 研究原型）的相同交互被映射到不同/相同 terminal，导致模式表达力下降。**对异构流需要统一事件类 schema（类似 D5 的事件类）。**

### 7.13 可解释性

**最高**：输出是命名 terminal（如 filter）与命名 pattern（如 information-seeking mantra）。**人类可读、可审计、确定性**——任务文件 §9 的"优点"完全成立。

### 7.14 不确定性

**无**：映射与匹配都是 hard decision。无概率、无置信度。null terminal 是唯一的"无法判定"信号。

### 7.15 评估

**评估对象是 taxonomy 表达力，不是分割质量**（关键！）：
- **Coverage**（可映射的记录比例）：Wall 100%、Liu & Heer 85–100%、Battle & Heer 46–68%；Brehmer & Munzner 最佳（avg 89.63%）、Amar 最差（avg 65.56%）（§5.1.1，Table 2，PDF p.7）。
- **Diversity**（映射后符号分布）：**terminal 过度使用**问题严重——某数据集 86.99% 事件映射到同一 filter terminal（Amar）、95.43% 到 explore（Yi）（§5.1.2，PDF p.7–8）。**极端偏斜使模式分析无意义**（大多数事件看起来相同）。Fig. 5：Tableau 的 8 个不同 log 记录全部映射到 Brehmer & Munzner 的 filter，实际代表 3 类过滤。
- **Non-terminal coverage 很低**：Guo et al. 的模式几乎观察不到（只在特定工具开发）；Shneiderman ISM 很少出现；**跨三个数据集没有通用模式**（"we do not observe any common sequences that occur across all three log datasets"，§5.2.1，PDF p.9）。Gotz & Wen 模式最普遍。
- 模式长度可变性：`plus`/`numeric` 压缩后仍很少精确匹配——"even when users perform similar patterns, the number of interactions within these patterns often varies"（§5.2.2，PDF p.9）。
- **没有 boundary/segment/activity 指标**——这是一篇"用语法框架诊断分类学"的论文，不是分割方法评估。

### 7.16 延迟 / 计算成本

正则匹配 + 映射，成本小（论文未报告具体数字）。**规模取决于 code-book 与日志量；无流式优化。**

### 7.17 超参数敏感性

**高度依赖人工定义**：terminal 词表、non-terminal 正则、映射 code-book。粒度不一致时（不同数据集），同一模式表达力崩塌。**这是该路线的核心脆弱点**（任务文件 §9 的"maintenance cost"）。

### 7.18 迁移到我们的英语阅读系统

- **可直接迁移**：① **regular grammar 作为已知行为模式的确定型分段引擎**——SCROLL_BURST（scroll+ → burst）、ANSWER_CHANGE（answer_click 后短期内再次 answer_click）、OPTION_ELIMINATION（toggle 序列）可直接写成 terminal + 正则（→ §11）；② 确定性、可审计、无标签的性质正是我们对"明确语义行为"需要的；③ 其"terminal 要有区分度"的教训直接指导我们的 action vocabulary 设计（§23）。
- **改造后迁移**：需要把我们的连续流（pointer/scroll 采样）先聚合为 terminal（如 pointer-move、scroll）——grammar 本身不能处理连续值；需要加入时间约束（grammar 无时序），如"两个 scroll 事件间隔 < 阈值"需作为 terminal 定义的一部分；需要为我们的界面定义事件类 schema（借鉴 D5 的 P 属性）。**全部为 PROJECT TRANSFER INFERENCE。**
- **不可迁移**：可视化分类学内容本身（filter/select/aggregate 等与阅读任务无关）；其表达力诊断结论（coverage/diversity 数字）基于可视化日志。

### 7.19 这篇论文未确立什么

- D6 未证明 grammar 在**任何 UI 流上分割质量**（无 boundary/segment 指标）。
- D6 未提供在线能力、时序建模、噪声处理。
- D6 的负面发现必须正视：**即便有权威分类学，terminal 过度使用 + 粒度不一致会摧毁模式表达力**——若我们的 SCROLL_BURST 定义得太粗（把所有 scroll 都映射成一个 terminal），会重蹈 95.43% 单 terminal 的覆辙。

---

## 8. D7 — Unsupervised Time Series Segmentation: A Survey on Recent Advances

> **论文定位**：**现代无监督 segmentation 方法地图（CPD / BD / SD 三分类）**。任务文件 §7.7：D7 必须与 D3 联合使用（D3 = classic CPD map，D7 = modern segmentation map）。Wang, Li, Zhou & Cai, CMC 80(2): 2657–2673, 2024。

### 7.1 研究问题

综述性质，填补"现有综述偏 CPD、忽略 BD 与 SD 进展"的缺口：给出 CPD / BD / SD 的**统一定义与分类框架**，重点综述 BD 与 SD 的近期里程碑，并讨论评估方式。**归属：Survey（segmentation 方法地图）。**

### 7.2 输入数据

覆盖的输入：多元时间序列 x = {x_i}, x_i ∈ R^d（Def 1，PDF p.3）。数据集（§3.2，PDF p.5–6）：UCR-SEG（BD 专用）、TSSB（UCR-SEG 超集，半合成拼接）、WESAD（压力/情绪可穿戴）、EyeState（EEG）、MoCap（动作捕捉 62 通道）、ActRecTut、PAMAP2、USC-HAD、Synthetic（TSAGen）。**全部 sensor/生理/运动数据；无 UI 交互流。**

### 7.3 事件 / 观测粒度

一个 observation = 一个多元数值采样点 x_i（连续）。**无事件概念**（对 BD 方法可用滑窗子序列；对 SD 方法逐点标签）。

### 7.4 预处理

综述不规定；各方法自带。Time2State 用滑窗 + 自监督编码；ClaSP 用重叠窗口 + 分类特征；IGTS 用熵。**无统一预处理。**

### 7.5 分割单位

三分类的核心差别（§1，PDF p.2）：
- **CPD**：找**统计性质变化的变点**；segment = 变点之间。
- **BD**：找**状态/制度变化的边界**（由子序列形状特征定义；"these state/regime changes can occur even without obvious statistical property changes"）；**边界点但通常不标注 segment 标签**（"BD methods aim to find the boundaries between semantic segments, but generally do not assign labels"）。
- **SD**：给**每个时间点分配状态标签**，边界是副产品（"assign a state label to each time point, with boundary points being a natural byproduct of state assignment"）。
- **单位分别是：变点 / 边界点 / 逐点状态标签**。任务文件 §7.5"不要混用"在此得到综述级定义。

### 7.6 边界定义

- CPD：统计分布/性质变化。
- BD：**子序列形状特征定义的状态变化**（如 profile 曲线的局部极值——FLOSS 的 CAC 局部最小、ClaSP 的分类得分峰）；边界 = profile 极值。
- SD：边界 = 状态标签变化位置（隐式）。
- **综述明确：BD 与 CPD 的边界定义不同（形状 vs 统计性质）**——这是任务文件"统计边界 ≠ 语义边界"的现代综述版表述。

### 7.7 在线 vs 离线

**两者都覆盖，且综述的三大发现之一就是在线稀缺**：Table 1 中 online 列只有 **E2USD**（自适应阈值 τ + 延迟聚类）与 **StreamScope**（AutoPlait 的在线增量成本版）支持在线；FLOSS、ClaSP、IGTS、ESPRESSO、Time2State、AutoPlait 均离线。综述结论："Existing methods failed to provide sufficient support for online working, with only a few methods supporting online deployment"。**在线能力是 D 组综述明确标注的缺口。**

### 7.8 监督

**全部无监督**（综述主题）；但多数需指定参数：状态数 K（HMM/HSMM）、段数 N（FLOSS/ClaSP 原生需要 N）、浓度参数 α（HDP-HSMM、DPGMM）。**"大多数方法需要指定参数，阻碍自适应工作"是第二大发现。**

### 7.9 模型 / 算法

- **SD-统计/马尔可夫**：HMM（Ω=(S,O,A,B,π)，Viterbi 解码 + EM 学习）、**HSMM**（显式状态时长分布）、**HDP-HSMM**（非参数贝叶斯，HDP 先验自动估 K，但仍需浓度参数 α；对比：**HDP-HMM 因非马尔可夫行为导致状态数膨胀、过渡过快，HDP-HSMM 更适合真实数据**）、TICC（Toeplitz 逆协方差 + MRF 定义簇，EM 交替分割聚类）。
- **SD-表示学习**：Time2State（自监督编码器 LSE-Loss + 滑窗嵌入 + DPGMM 聚类 + 时间点多数投票）、E2USD（相似性负采样 + **自适应阈值 + 延迟聚类实现在线**，降低计算开销）。
- **SD-压缩**：AutoPlait（MDL + Multi-Level Chain Model/HMM，离线）、StreamScope（AutoPlait 在线版，增量成本函数）。
- **BD-profile**：FLOSS（CAC 曲线：matrix profile 的最近邻 arc 计数，边界区 arc 少 → 局部最小；**需指定 N**）、ClaSP（classification score profile，重叠窗口 + 分类器得分 + **递归分割策略**：每次只取全局最大，再递归——比 FLOSS 的局部极值法改进）。
- **BD-熵**：IGTS（信息增益成本函数，TopDown 贪心或 DP；knee point 估 N）、ESPRESSO（shape+entropy：profile 提候选 + 熵优化）。

### 7.10 时长建模

HSMM / HDP-HSMM 是显式时长建模的代表（综述明言 HMM"状态时长固定，无法捕捉可变时长的时序依赖"）。TICC/Time2State/FLOSS 等无显式时长。**综述支持"HSMM 比 HMM 更适合可变时长结构"的说法，并给出 HDP-HSMM vs HDP-HMM 的机理论证。**

### 7.11 噪声鲁棒性

综述对噪声的讨论有限：E2USD 的相似性负采样关注难例；ClaSP 分类得分对噪声敏感度未讨论；Time2State 表示学习对噪声有一定鲁棒性（未量化）。**整体：未系统考虑。**

### 7.12 多模态 / 多事件兼容性

**多元连续数值原生**（d 通道）；**不支持异构事件类型/类别属性**。BD 的 profile 方法支持多元（FLOSS 对每通道取 profile 再平均，§4.2）。**Mixed events 需编码。**

### 7.13 可解释性

BD 输出边界位置（无语义标签，需外部聚类补标）；SD 输出 latent state ID（Time2State/E2USD 的状态无语义名，需事后解释）；FLOSS/ClaSP 无语义。**整体 interpretability 低至中**（区别于 D5/D6 的文本标签）。

### 7.14 不确定性

HDP-HSMM 类贝叶斯方法有后验（综述未强调）；Time2State 的 DPGMM 给出簇后验（未作输出）；E2USD 的相似度阈值可作弱置信度。**整体：SD 概率方法有内置后验但被当作中间量；BD 方法无。**

### 7.15 评估

**评估指标分类是本综述对 D 组最有用的贡献之一**（§3.1，PDF p.4–5）：
- **BD 指标**：
  1. 朴素 F1（Precision/Recall on boundary points）——**问题：对微小时差不容忍**（GT 边界在 10000、预测在 10001，被计为 FP；"state transitions are not instantaneous, predictions near the ground truth boundary points should also be considered as correct"）。
  2. **容忍窗口 F1**：GT 边界加窗口 bracketing，预测落入窗口内算 TP；一个 GT 只认最近的预测，其余 FP。
  3. **评分函数（Gharghabi et al.）**：error = (1/(n·|cpts_pred|))·Σ_{p∈cpts_pred} min_{p'∈cpts_GT}|p−p'|，∈[0,1]——**问题：不做二部匹配**（多个预测可能匹配同一 GT）。
  4. **综述建议：同时用 F-Measure + 评分函数综合评估**（如 ESPRESSO 所做）。
- **SD 指标**：ARI、NMI（点级聚类指标）。**综述批评："SD 方法很少用 BD 指标作为评估指标，更关注点级状态分配性能。纳入 BD 指标会让 SD 评估更全面。"**——这是"boundary ≠ label"的综述级背书（→ §15）。
- **任务文件 §7.15 的三类指标（boundary/segment/activity）在 D7 的综述框架中得到精确对应：BD 指标 ≈ boundary accuracy；SD 的 ARI/NMI ≈ segment quality；下游识别 ≈ activity accuracy。且综述明确指出 SD 文献忽略了 boundary。**

### 7.16 延迟 / 计算成本

E2USD 的自适应阈值 + 延迟聚类是为降低在线计算开销（"greatly reduce redundant clustering and computational costs"）；StreamScope 的增量成本函数为在线。FLOSS/ClaSP（矩阵 profile / 分类）计算成本与窗口数相关（综述未给精确复杂度）。**在线稀缺与计算成本相关。**

### 7.17 超参数敏感性

**综述第三大发现**："Most existing methods require the specification of parameters, which hinders their ability to work adaptively"。K/N 是最难指定的（"K/N-Free" 是综述专门引入的属性维度，§4，PDF p.7）：FLOSS/ClaSP 原生需要 N；HMM/HSMM 需要 K；HDP-HSMM/DPGMM 虽自动估 K 但仍需 α。**"因为 unsupervised 就认为不需要人工定义"被综述否定（任务文件 §32-11）。**

### 7.18 迁移到我们的英语阅读系统

- **可直接迁移**：① **CPD/BD/SD 三分类**直接构成我们 action segmentation 的概念框架（我们的 SCROLL_BURST 是 BD 型（边界）还是 SD 型（状态）决定方法选择）；② **评估指标组合（F1 + 容忍窗口 + 评分函数 + ARI/NMI）**直接作为我们 §24 Evaluation Framework 的蓝本；③ HDP-HSMM 讨论补充 D4 的 HSMM 权衡；④ profile-based BD（FLOSS 的 CAC）作为 **pointer 连续段边界检测**的候选（profile 局部极值法），其"需指定 N"的缺陷提醒我们用 knee point 或启发式估 N。
- **改造后迁移**：所有方法面向连续数值流，我们的混合事件流需先编码/聚合；在线支持稀缺，需要我们自己开发在线方案（E2USD 的自适应阈值 + 延迟聚类是现成模板）。
- **不可迁移**：sensor/HAR/EEG/运动数据上的数值（综述无统一数值结论，且明确"没有统一 benchmark"）。

### 7.19 这篇论文未确立什么

- D7 未提供 UI 交互流上的任何分割证据（全部数据集为 sensor/生理/运动）。
- D7 未给出"哪种 BD/SD 方法在异构事件流上有效"的答案。
- D7 未解决在线稀缺与参数自适应问题（它只是指出问题）。
- D7 未统一各方法在相同 benchmark 上的比较（明确指出不存在这样的基准）。

---

## 9. 跨论文比较矩阵

任务文件 §7.15/§24/§33 要求把每篇论文的关键条件（输入流类型、observation 粒度、boundary 定义、监督、时长、在线、uncertainty、评估对象、UI 相似度）并排比较。下表汇总（详见各篇 7.x 小节）。

| 维度 | D1 MMAD | D2 OCPD | D3 CPD Survey | D4 HSMM | D5 Task-Level | D6 Grammar | D7 Seg Survey |
|---|---|---|---|---|---|---|---|
| **主归属** | Denoising | Boundary + Activity Rec. | Survey (CPD) | Segmentation (latent state) | Segmentation + Task Abstraction | Task Abstraction (grammar) | Survey (BD/SD) |
| **输入流** | 离散动作日志（RPA） | 连续多元传感器流（50Hz） | 数值时间序列（概念层） | 一维连续数值序列 | 离散 UI 交互事件（含属性集） | 离散交互日志（可视化） | 多元连续数值序列 |
| **Observation 粒度** | action 行（→template） | 传感器采样点 | x_t ∈ R^d | 数值样本 y_n | UI 事件 (uid,ts,P,V) | 日志记录（→terminal） | x_i ∈ R^d |
| **Boundary 定义** | 无显式边界（噪声标记） | 方差统计变点（Bartlett+BH） | 分布变化（H0/HA） | 隐式（状态切换副产品） | 关键词 chunk + 四检查混合 | grammar/正则匹配 | CPD:统计 / BD:形状 profile / SD:状态切换 |
| **Online/Offline** | OFFLINE | ONLINE（窗口级延迟） | 两者（ε-real-time 谱系） | OFFLINE | **BOTH** | OFFLINE | 多数离线（在线稀缺） |
| **Supervision** | Unsupervised（人工模板/阈值设计） | 边界无监督 / 识别监督 | 两者 | Unsupervised（需 K,P） | Unsupervised（人工关键词集） | Rule-based（人工 code-book） | Unsupervised（多数需 K/N/α） |
| **Duration 建模** | 无 | 无（固定 2.56s 窗） | 无（BCPD 有 hazard 先验） | **显式 duration 分布（HSMC/RHSMC）** | 无（明言不用时间戳） | 无（明言无法表达时序） | HSMM/HDP-HSMM 显式；其余无 |
| **Mixed events** | 部分（多属性动作） | 不支持 | 需编码 | 需编码 | **原生支持异构语义事件** | 部分（靠人工映射） | 需编码 |
| **Interpretability** | 中（模板文本） | 低（位置）+ 高（识别标签） | 低（位置） | 低（latent ID） | **高（文本标签）** | **高（命名 terminal/pattern）** | 低–中 |
| **Uncertainty 输出** | 无 | 内部 p 值/检验量（未输出） | BCPD 有 run-length 后验 | **逐点后验 p(x_n\|y)** | 无（仅 sim 分数） | 无 | SD 概率法有后验（作中间量） |
| **评估对象** | Noise P/R/F1（Event Cleaning） | Activity Rec. accuracy/F1（**非边界**） | 综述级指标分类 | 逐点误分类率（label） | #tasks + edit dist + Rand/Jaccard | Coverage/Diversity（非分割质量） | BD: F1+窗口+评分函数 / SD: ARI/NMI |
| **UI 相似度** | 中（RPA 动作日志） | 低（传感器） | 低（概念可用） | 低（雷达图像） | **最高（UI 事件）** | 中（可视化日志） | 低（sensor/EEG） |
| **可复用核心** | 转移概率判噪 + 自适应阈值 | 在线统计变点检验 | 评估指标谱系 + ε-real-time | 显式时长 + 后验 + 线性 RHSMC | 三组件端到端 + 双设置 | 确定性正则分段 + terminal 区分度教训 | CPD/BD/SD 框架 + 评估指标 |
| **主要缺口** | 误删低频真实行为；无分割 | 无边界指标；非 UI | 陈旧（2016） | 非 UI；无边界指标 | 粒度偏粗；不用时间戳 | 人工成本高；无时序 | 无 UI 证据；无统一 benchmark |

---

## 10. 去噪 ≠ 分割

> 对应任务文件 §8 专题一。重点使用 D1，区分 **Technical noise / Behavioral rarity / Semantic irrelevance**。

### # 什么是用户交互日志中的噪声？

**D1 对噪声的定义（§2.1）**：噪声 = "偏离预期模式的异常或错误动作数据"，分为：
- **内部噪声 N_in**：任务内异常重复动作或异常执行序列（导致时间差异或不一致模式）。典型：重复动作、异常循环。
- **外部噪声 N_out**：任务内动作类型的多样性，包括非常规动作（如窗口调整、目标突变）。

**关键：D1 定义的"噪声"全部是统计/模式层（Technical noise），不包含"Semantic irrelevance"**。它对"这个动作虽然符合统计模式但与当前阅读任务无关"（例如学生切到浏览器标签页又切回来）没有直接建模——这类在 D5 中由 overhead 关键词处理（log in/open/reload），在 D6 中靠人工 code-book 排除。**三个概念在我们项目中必须分开：**

| 概念 | 定义 | 处理方式（不物理删除） | 文献支持 |
|---|---|---|---|
| **Technical noise** | 系统生成事件、重复事件、采集伪影（pointer 抖动、双击产生的冗余事件） | **可从特定 derived analysis stream 中排除（标记 noise_flag / excluded_from_segmentation），但 Raw Observable Events 永久保留** | D1 预处理删除重复/无效、D2 滤波去噪——但那是文献流水线内部的物理删除；我们的架构原则是 append-only（见下） |
| **Behavioral rarity** | 低频但真实的行为（学生只改一次答案、只划一次线） | **不排除；可能是高价值行为** | D1 摘要反对"低频即噪声"，但其机制仍会误删（见下） |
| **Semantic irrelevance** | 与阅读任务无关的行为（切出页面、界面噪声、登录类 overhead） | **可标记并从 segmentation 流排除，但保留为显式事件（如 VISIBILITY_INTERRUPTION）** | D5 overhead 关键词；D6 null terminal |

**架构原则（与 C 组一致的 append-only 纪律）**：本项目原始日志**永久保存、可 replay**，这是后续重新跑算法、修正阈值的基础。去噪的正确表达是：

```
Raw immutable event
      ↓
noise_flag / duplicate_of / excluded_from_segmentation / analysis_weight
      ↓
Derived clean event stream
```

例如 `pointer_sample #382` 可以 `noise_flag = true`，但它**仍然存在于 Raw Log**，只是不在当前 Action Segmentation 中使用。此外，**系统生成事件 ≠ 噪声**：`visibility_changed`、`layout_changed` 虽是系统事件，却可能非常有价值——它们能告诉我们学生是否切出页面、页面布局是否变化（§19/§23 已把 VISIBILITY_INTERRUPTION 列为保留的显式语义事件）。

### 特别回答：低频行为是否可能恰恰是高价值行为？

**是，而且是 D 组最重要的反面教训。** 三个论据：

1. **D1 摘要直接点名**"现有方法把低频动作当噪声"是问题（PDF p.1）；它的外部噪声案例（窗口拖拽）恰恰说明**高频 ≠ 正常**。反过来必然成立：**低频 ≠ 噪声**。但 D1 没有给出保护低频真实行为的机制——它的判噪标准"转移概率 < μ−3σ"对"低频但真实、且转移概率低"的行为**仍然会删**。论文在 RQ3 讨论中承认变体会被误判为噪声，只以"RPA 场景只允许单一 trace"辩解（PDF p.17）。

2. **我们的场景反例是结构性的**：英语阅读中 ANSWER_CHANGE（学生只改一次答案）是一个低频、但在诊断上极其重要的行为。任何以"频率/转移概率"为判据的去噪器都会倾向删它。**结论：去噪规则必须含语义白名单，低频语义事件直接旁路，不进统计判噪。**

3. D3 综述也确认：CPD 方法（类似地基于统计）对"高度动态系统"表现差（§4.4），因为统计假设在行为高度可变时不稳。

### D1 如何防止"低频但真实"的 event 被误删？

**答案：D1 没有专门防止。** 它的唯一防线是"迭代验证"（§2.4.2）：临时移除候选噪声后重算图，若邻居转移概率上升则确认噪声，否则恢复。这个机制防止的是"删除后反而破坏图结构"的情况，**不保护"低频但语义相关"的行为**。此外，D1 的"噪声"判定发生在 template 层（相似 action 已聚为同一 template）——若一个低频动作与高频动作共享 template，它可能被高频 template 的转移统计"救下"；反之若独有 template，则暴露。**这是巧合式保护，不是设计。**

### 区分三者的操作含义

对**我们的去噪层**（Event Cleaning），D 组文献支持的操作性划分（**全部在 derived 层标记/排除，Raw 永久保留**）：
- **Technical noise → 从 segmentation 流排除（不物理删除）**：重复事件、采集伪影在 derived 层标记 `noise_flag`；`visibility_changed` / `layout_changed` 类系统事件**不是噪声**，保留为显式语义事件（§23 的 VISIBILITY_INTERRUPTION）。D1 清洗阶段（§2.2.1）与 D2 滤波可作"如何识别技术噪声"的参考，但物理删除动作不移植。
- **Behavioral rarity → 语义白名单保护**：ANSWER_CHANGE、UNDERLINE_REMOVE、OPTION_RESTORE 等语义事件**不进统计去噪器**，或至少带豁免标签。D 组无直接支持（这是 OPEN DESIGN QUESTION 的输入）。
- **Semantic irrelevance → 语义规则判定**：切出页面/界面外动作 → 用类似 D5 的 overhead 关键词集或 D6 的 code-book 排除，或保留为 VISIBILITY_INTERRUPTION 事件（我们候选 vocabulary 里的显式语义事件）。

**最终区分（任务文件 §8 要求）**：Denoising 回答"**哪些 event 不应进入后续分析**"；Segmentation 回答"**连续流如何切成 episodes**"。D1 只回答前者；没有任何 D 组论文把两者联合成一个流水线（D1 的 Future Work 明确把 segmentation 列为后续）。**因此"先 denoise 再 segment"还是"联合"是开放设计问题，但 D1 的"删除动作"发生在 template 层、独立于任何 episode 边界，至少说明去噪可以先行而不与分割耦合**（→ §27 Q10）。

---

## 11. 基于规则 / 语法的分割

> 对应任务文件 §9 专题二。重点使用 D6，并结合 D5。

### 原始事件 → 记号 → 语法 → 高层动作

D6 给出了完整形式化：log record →（人工映射 code-book）→ **terminal** →（正则 production rules）→ **non-terminal（higher-level pattern）**。D5 给出了另一个形式的规则化：事件类 →（completion 关键词）→ **chunk** →（四检查）→ **task**。两条路线的共同结构：

```
Raw Event → Token(terminal / event class) → Pattern(grammar rule / chunk+checks) → Higher-level Action
```

### 优点（D6 + D5 实证）

1. **可解释 / 确定性（Interpretable / Deterministic）**：D6 的 grammar 映射与匹配完全确定性（同一事件流 → 相同 terminal/pattern）；D5 输出文本标签（"Create order"）可读可审计——**但注意 D5 的确定性只在其边界识别（completion 关键词 + 四检查）成立，其任务类型分类（DenStream 在线聚类）是 history-dependent 的**（§7.13、§14 第 9 问）。
2. **无需标签（No labels）**：两者都无需训练标签（D6 需人工 code-book，D5 需人工关键词集，但都无监督）。
3. **无需状态数/段数估计**：规则定义即边界定义，没有 K/N 超参问题（对比 D7 中 FLOSS/ClaSP 需指定 N）。
4. **可与界面语义对齐**：规则可以引用"目标元素/对象"（D5 用 Label/Value 属性），把 UI 语义直接编进分段逻辑。

### 缺点（D6 的实证是 D 组最清醒的警告）

1. **需要人工构造语法（Requires handcrafted grammar）**：D6 的 12 个 code-book（3 数据集 × 4 分类学）+ 12 个 non-terminal 映射全是人工的；inter-rater 从 0.47 磨到 0.99。D5 的 20 个 completion 关键词 + overhead 词表 + UI 词表也是人工。**维护成本高**。
2. **Terminal 过度使用 → 语义塌缩**：D6 发现某数据集 95.43% 的事件映射到同一个 explore terminal；Tableau 的 8 种不同日志记录全部映射到 filter。**如果我们的 SCROLL_BURST 定义把所有 scroll 事件当成一个无区分的 terminal，会失去"连续滚动 vs 停顿"的区别**——必须保留关键属性（时间间隔、方向、区域）作为 terminal 的组成部分（→ §20）。
3. **无法表达时序**：D6 明言 grammar 无法表达 timing（§6）。**SCROLL_BURST 的定义核心恰恰是时间聚集**——因此纯正则不够，需要"时间约束 terminal"（把间隔阈值编码进 token 判定）。
4. **模式长度可变性**：D6 发现"even when users perform similar patterns, the number of interactions within these patterns often varies"——正则的 `+`/`*` 能覆盖长度变化，但代价是歧义（一个长串如何分块）。
5. **粒度不一致**：D6 的核心负面发现——跨数据集无通用模式。**规则必须按我们的界面 schema 定制，不能指望通用。**

### 重点研究：对我们比较确定的行为，rule/grammar 是否反而比 ML 更合理？

**是，对以下四类行为规则/语法明显更合理**（D5 的 chunking+检查是现成模板，D6 的教训用于约束设计）：

| 行为 | 为什么规则合理 | 规则示例（草案） |
|---|---|---|
| **SCROLL_BURST** | 连续 scroll 事件在时间/速度上有明确聚集结构；语义"学生在滚读"无需学习 | scroll 事件间隔 < τ 且同向 → 属于同一 burst；间隔 > τ 或 scrollend → 边界（→ §20） |
| **ANSWER_CHANGE** | 语义明确（同一题两次 answer_click，后值 ≠ 前值），与统计无关 | 检测同一 question 的两次 answer_option_clicked 且选项不同 → ANSWER_CHANGE |
| **OPTION_ELIMINATION** | 明确界面操作（option_elimination_toggled），本身已是语义原子 | 连续 toggle 序列聚合为 episode（可选） |
| **UNDERLINE / TEXT_SELECTION** | 明确语义操作序列（selection → underline） | underline_created 前紧邻 text_selection_committed → TEXT_MARKING_EPISODE |

**理由**：(1) 这些行为的边界由"界面语义事件"定义（D5 的关键词 chunk 逻辑），不需要统计推断；(2) 无标签、无 K/N、确定性、可审计（D6 的优点）；(3) D 组没有任何证据表明 ML 在这些确定型行为上更优。**但规则必须遵守 D6 的三条纪律：terminal 有区分度、保留时序约束、针对我们的界面 schema 定制。** 对**非确定型**行为（pointer 连续流中的潜伏态）规则不够，需要 CPD/概率模型（→ §12、§13、§21）。

---

## 12. UI 交互的变点检测

> 对应任务文件 §10 专题三。综合 D2 / D3 / D7。

### # 什么是 UI 交互中的变点？

**经典定义（D3 Def. 7）**：CPD = 假设检验 H0（无变化）vs HA（存在 k* 使两侧分布不同）。**变点 = 统计分布发生变化的 k*。** D7 进一步区分：CPD（统计性质变化）vs BD（状态/制度变化，可由形状定义，即使无统计变化）。D2 的 OCPD 是 CPD 的一个实例：方差齐性检验（Bartlett）。

**因此，在 UI interaction 语境中："统计分布变化" ≠ "action boundary" 是定义层面的必然**——CPD 只承诺"分布的矩/形状变了"，不承诺"语义上发生了什么"。

### 必须回答：pointer speed 突变是 action 边界还是同 action 内减速？

**两者都可能。** D2 的机制是决定性论据：它的变点检测只比较两侧方差（Bartlett），一个动作内的自然减速（pointer 靠近目标时速度下降）也会产生方差变化 → 统计变点 → 误报"边界"。D3 综述指出 CPD 对"高度动态系统"表现差（§4.4），D7 指出 CPD/BD 的边界由统计/形状定义而非语义。**没有任何 D 组论文证明了"pointer 速度分布变化 = 语义动作边界"。** 这是统计边界与语义边界的核心张力（任务文件 §10 原话）。

### 分析：CPD 适合解决哪些 action，不适合哪些

**适合（CPD 有理论优势的）**：
1. **Pointer movement episode**：pointer 连续采样是纯数值流（与 D2 的传感器流同构）；速度/方向分布变化与"移动→停顿→移动"的边界有较强对应（但需验证减速误报）。候选：D2 的 OCPD（Bartlett）、D3 的 RuLSIF/BCPD、D7 的 profile（FLOSS/ClaSP）。
2. **Scroll burst**：scroll 事件密度/速度的变化（从高频滚动到停止）是数值流特征；CPD 可在 scroll 序列上找 burst 边界（但规则聚合通常更简单，见 §20）。
3. **Long continuous behavior**：长时间同类行为（连续滚动阅读）内部边界难定义时，CPD 提供统计依据。

**不适合（本身已有明确语义事件的）**：
1. **Answer click / question navigation / underline commit**：这些是**语义原子事件**，边界就是事件本身发生/完成，无需统计变点（任务文件 §10 原话）。对它们用 CPD 是多余的推断。
2. **离散语义序列**（事件序列）：D3 的所有 CPD 方法面向数值序列；对事件序列，变点检测需要先编码为数值（丢失语义）。D5 的规则式边界（关键词+共现）比 CPD 更直接。

### 结论（供 §27 Q3 引用）

**Change Point Detection 不能直接等价 Action Boundary Detection。** CPD 是"统计边界检测"，它是否等于语义 action 边界取决于：(1) 该 action 的边界是否确实由底层数值流分布变化产生（pointer/scroll 是，click 不是）；(2) 是否排除了同 action 内的统计波动（减速、抖动）造成误报。**需要领域验证，不是定义保证。** 统计 boundary ≠ semantic boundary 在 D 组是强证据（D2 机制 + D3 定义 + D7 CPD/BD 区分），不是猜测。

---

## 13. HMM vs HSMM

> 对应任务文件 §11 专题四。重点使用 D4，并结合 D7。

### 对比表

| 维度 | HMM | HSMM |
|---|---|---|
| **隐状态** | X_n ∈ {o1..oK}，转移是 Markov | X_n ∈ {o1..oK}，转移 p*(x'|x) 强制 x'≠x（经典版） |
| **转移** | 一步转移矩阵 A，自转移允许 | 由转移 + 停留时间分布联合决定（D4 §3.1：p(x) = p(o1)p_o1(1)p*(o2\|o1)p_o2(3)...） |
| **时长** | **隐含 geometric**（discrete-time HMM 隐含 geometric 停留时间分布：p_ok(m)=(λ_kk)^m(1−λ_kk)；D4 §3.1 原话 "exponential form"） | **显式、可非 geometric** 时长分布 p_ok(m)（D4 §3.1；"variable duration HMMs"） |
| **在线推理** | 有（在线滤波/解码可行） | 经典 HSMC 前向后向是批处理；RHSMC 变体复杂度 O(N) 但论文无在线版（D4 离线） |
| **训练** | EM/Baum-Welch 成熟 | ICE/EM（D4 §4.1-4.2）；非参数版 HDP-HSMM 用 Gibbs（D7） |
| **可解释性** | latent ID，需事后命名 | 同 HMM（latent ID）+ 时长参数可读（"平均停留 X 步"） |

### 重点解释：为什么 duration 对 Action Segmentation 很重要

任务文件 §11 例子：**POINTER_TRANSITION（短）vs READING-LIKE POINTER EPISODE（长）**。在 HMM 中，状态时长被几何分布约束：**一个状态"平均停留"决定后，其时长方差也随之固定**（几何分布均值=1/(1−λ)，无法独立控制方差、无法表达"最少停留"）。这导致：
- 想表达"pointer 过渡状态通常只有 0.5–2 秒、且很少超过 5 秒"，HMM 做不到（几何分布右尾太厚）。
- HSMM 可以指定任意时长分布（如"最少 1s、平均 3s、上限 10s"的截断分布）。

D7 补充了机制性论证：**HDP-HMM 因非马尔可夫行为导致状态数膨胀、过渡过快**；HDP-HSMM 通过显式时长缓解，更适合真实数据。D4 的 RHSMC 变体把时长建模成"最小停留时间"（允许自转移），在线性复杂度下获得显式时长能力。

### 必须检查：显式 duration 分布是否真的比 HMM 更适合我们的高变异 UI 行为？

**条件性结论（不要因为 HSMM 更复杂就默认更好）**：
- **支持 HSMM 的证据**（D4 §5.3 唯一一次直接对比）：数据真的具有非马尔可夫时长/非平稳结构时，NS-RHSMC 显著优于 NS-HMC（类错误 25% vs 30%，纹理 9% vs 18%）。
- **反对 HSMM 的证据**（D4 §5.1）：数据只是 HMC 时，RHSMC **无增益**；高噪声下**略差**（t=18.38% vs 17.42%），因为参数更多、估计更不稳。D4 自己明说"using HMC directly needs fewer parameters to be estimated"。
- **对我们的判断**：如果我们的行为状态确实有稳定时长结构（如 READING-LIKE POINTER EPISODE 天然较长、POINTER_TRANSITION 天然较短），HSMM 的理论优势成立；但 (1) 需要先确认时长分布真的非几何（可以用时长直方图检验）；(2) 需要解决 K 的选择与在线推理（D7 显示在线支持稀缺）；(3) 我们的事件流是混合的，HSMM 需要先编码。**因此 HSMM 是"条件性更优"，不是默认更优**（→ §27 Q6/Q7）。

---

## 14. UI 特定任务抽象

> 对应任务文件 §12 专题五。这是整组最重要章节之一，重点使用 D5。必须详细还原 pipeline 并回答 10 问。

### # 从 UI 事件到任务级事件

**D5 pipeline 完整还原**（§4，Algorithm 1）：

```
low-level event stream (uid, ts, P, V)
  ↓ (per-event, online)
Object-instance identification: POS 名词提取 → UI 词表去除 → object type; 正则/NER → object id
  ↓
event 入缓冲 B
  ↓
Chunking: completesChunk(completion 关键词 ok/submit/send/save) → chunk（子任务）
  ↓
Segmenting: endsTask(四检查: 上下文不相关 / 无数据值重叠 / 非 overhead / 控制流非确定性)
  ↓
Task（事件段）→ 向量化（事件类数 + 频率）
  ↓
Task categorization: DenStream 在线聚类 → task type; tf-idf → 文本标签
  ↓
Task-level events: (tid, type, ts, lifecycle start/complete, objects)
```

### 10 问逐答（任务文件 §12 要求）

1. **task boundary 如何找？** → 关键词 chunk（completion actions）+ 四检查（上下文共现相似度、数据值重叠、overhead、控制流确定性）。**不是统计变点、不用时间戳**（§4.2）。
2. **task similarity 怎么定义？** → 任务向量（唯一事件类数 + 各事件类频率）的**密度聚类**（DenStream），簇 = 类型。相似度是特征空间距离，非编辑距离。
3. **control-flow 如何使用？** → 直接跟随（DF）计数：count(c_i.P) vs count(DF(c_i.P, c_{i+1}.P))，确定性检查（c_i 后行为是否恒定）→ 决定是否切分（§4.2.2(4)）。
4. **data semantics 如何使用？** → 数据值重叠检查（c_i 最后两事件与 c_{i+1} 前两事件的 V 精确匹配）→ 避免把共享数据值的子任务切开（§4.2.2(2)）；对象实例（ID/URL/实体）关联任务到过程执行（§4.1）。
5. **object information 如何使用？** → 对象实例识别（POS 名词 + 正则 ID + NER）→ task 的 objects 集合 → 判断两个任务是否处理同一对象（如同一订单）→ 关联 task-level events 到 process execution（§4.1、§4.4）。
6. **online 和 offline 有什么区别？** → 在线：增量共现矩阵 + DenStream 在线聚类，无需重训、可发现 unseen 任务；categorization 略降。离线：先全日志 identification 再 categorization（相当于全量 warm-up）。**同一套算法双设置**（§4、§5.3.5）。
7. **是否需要预定义 task types？** → **不需要**。DenStream 自动发现簇数（无 K 参数）；任务类型是涌现的（§4.3.2）。但仍需人工关键词集（completion/overhead/UI 词表）。
8. **unseen task 是否能发现？** → **能**（在线聚类动态建/删微簇，论文明确"if a new task is introduced into a process, our approach can recognize this without the need to retrain"，§1）。这是 D5 相对离线方法（Leno/Urabe）的核心优势之一。
9. **输出是否 deterministic？** → **分两部分回答**（反馈明确要求拆开）：**Task identification（边界）largely deterministic given current model/history**（completion 关键词 + 四检查在参数与历史状态固定后是确定逻辑，同一事件流 → 相同 chunk/段）；**Task categorization（类型）是 adaptive、history-dependent 的 online clustering**（DenStream 随 stream order / warm-up / 聚类模型既往状态变化，早期任务的类型指派可能不同）。**不要把整套 D5 归入"确定性方法"。**
10. **对 noisy event 是否 robust？** → 中等：overhead 检查处理语义噪声；但对偶发孤立事件、重复事件无专门机制；共现矩阵冷启动敏感（建议 warm-up）。**无噪声注入实验。**

### 它所谓的 task-level event，与我们所谓的 action episode 粒度是否相同？

**不相同。D5 的 task 粒度明显大于我们的 micro-action。**

- D5 任务实例（Table 2）：平均长度 10.1–73.5 个事件（Create structural unit 平均 10.9 事件，Fill in travel request 平均 73.5 事件）；一个"create order"任务跨登录、搜索、填表、保存多个子任务（u1–u8 共 8 事件 + 多个应用）。
- 我们的 micro-action（SCROLL_BURST、POINTER_TRANSITION、UNDERLINE_CREATE）通常由**同一类型连续事件的短段**组成（秒级、1–50 个样本），对应 D5 的 **chunk 级甚至 chunk 内部**。
- 类比：D5 的任务 ≈ 我们的"question→passage→question 循环"的上层（Level 3）；D5 的 chunk ≈ 我们的 action episode 或略粗（Level 2）；我们的 POINTER 样本 ≈ D5 不存在的最底层（Level 1）。

**粒度差异的操作含义**：D5 的四检查边界判定逻辑（共现相似度、数据重叠、控制流、overhead）在**跨 chunk 语义**层面有效，不能直接搬到 micro-action 层；我们的 micro-action 边界需要**更细粒度的时间/速度/语义事件依据**（→ §20、§21）。**但 D5 的架构模式（对象/识别/类型三组件、双设置、无 K、涌现类型、文本标签）整体可迁移到我们的 episode 层。** 任务文件 §14（Q8）的答案在 §27 Q8 汇总。

---

## 15. 边界 vs 标签

> 对应任务文件 §13 专题六。这是 D 组非常重要的一章，特别审查 D2。

### 四种情况分析

| 情况 | 含义 | 对后续过程建模的后果 | D 组证据 |
|---|---|---|---|
| **Boundary correct, Label correct** | 边界准、标签准 | 理想状态 | D5 ours 行是最近似实证（n.ED 0.04 + R(ma) 0.97，Table 3/6）；其完美识别对照行（Perf. ident.）categorization ≥0.95（S_U1/S_U3 为 1.00） |
| **Boundary correct, Label wrong** | 边界准，但 segment 类别错 | 段数/位置对，但语义错 → 过程级证据类型错 | D5 Table 3 中 BL_co-oc：identification 尚可但 categorization R(ma) 仅 0.71–0.80；D4：边界是状态标签副产品，标签错则边界重排 |
| **Boundary wrong, Label correct** | 边界错，但切出来的段被正确分类 | **最危险**：报告的分类 accuracy 高，但分割本身差 | **D2 就是典型案例**：99.80% F-Measure 是窗口分类准确率，其 OCPD 边界无任何直接验证 |
| **Boundary wrong, Label wrong** | 全错 | 无价值 | D5 中 BL_dfg：n.ED 0.32–0.83 且 categorization R(ma) 仅 0.49–0.82 |

### 为什么 activity classification accuracy 不能代替 segmentation quality

**机制论证（D2 是完美反例）**：
1. D2 的分割流程是"OCPD 定窗口起点 → 2.56s 固定窗口 → 分类"。**即使 OCPD 的边界全错（或根本没找到边界），只要 2.56s 窗口内主要是一个活动类型，分类器仍能给出高 accuracy**——因为窗口是均匀的，分类任务是"窗口内多数活动是什么"，这与"窗口边界是否与活动边界重合"是两回事。论文报告的 accuracy/F1 衡量的是"窗口被正确分类"，不是"边界被正确定位"。
2. D5 也提供了间接证据：**task identification 差（n.ED 0.56）时，task categorization 仍可达 R(ma) 0.78**（BL_urabe avg，Table 6，PDF p.12）——"事后分类能掩盖差的分割"是 D 组实证结论。
3. D7 综述直接批评："SD 方法不重视边界点准确检测"，并建议把 BD 指标纳入 SD 评估（§3.1.2）。

**因此（任务文件 §13 原话）**：boundary detection ≠ segment classification。一个方法可以 segment label 很准而 boundary 很差（D2），也可以相反。**评估必须分层报告（§24）。**

---

## 16. 在线 vs 离线分割

> 对应任务文件 §14 专题七。我们未来可能需要两套输出：online（做题时实时识别 SCROLL_BURST 等）与 offline（会话后重平滑/修正）。

### 各论文的在线支持盘点

| 论文 | 在线能力 | 具体形态 | 延迟 |
|---|---|---|---|
| D1 | OFFLINE | 批处理迭代去噪 | 无在线设计 |
| D2 | ONLINE（名义） | 滑动窗口内统计检验；需 k+2p 样本窗口 | 窗口级延迟（未报告精确值）；识别需 2.56s 窗口 |
| D3 | BOTH（谱系） | ε-real-time 框架 | 1-real（完全在线）到 ∞-real（完全离线） |
| D4 | OFFLINE | forward-backward + ICE 批处理 | 无在线 |
| D5 | **BOTH** | 事件到达即处理；缓冲 B；增量共现矩阵 + DenStream | object 1–107ms/事件、task-ident 2–4ms/事件、task-categorize 40–150ms/任务 |
| D6 | OFFLINE | 全日志映射 + 正则 | 无在线讨论（正则可在流上做，属推论） |
| D7 | 多数 OFFLINE | Table 1 中仅 E2USD、StreamScope 支持在线 | E2USD 自适应阈值 + 延迟聚类 |

### 核心问题：是否支持 online provisional segmentation + offline retrospective refinement？

**严格区分两个命题（反馈明确要求）：**
- **"Online + Offline both feasible" → SUPPORTED**：D5 是 UI 场景的直接实证（在线/离线双设置，延迟明确）；D2/D3/D7 提供在线 CPD 的机制。
- **"Online provisional + Offline retrospective refinement"（先在线输出 provisional boundary，之后离线修改历史 boundary）→ PROJECT ARCHITECTURE HYPOTHESIS**：D 组**没有**任何论文展示过"修改已输出的历史边界"这一操作。D5 的 warm-up 更接近 **delayed commitment**（推迟到模型成熟再决断、再指派类型），不是 retrospective revision（回头改已提交的边界）。这是两个不同的机制，不能混为一谈。

**支持性与不支持性的细分**：
- **支持性证据**：(1) D5 同一算法双设置，在线 categorization 因聚类未成熟而略降（说明在线结果可以是 provisional 的）；(2) D3 的 ε-real-time 谱系说明"在线"是延迟程度的连续体；(3) D7 的 E2USD"延迟聚类"（相似度低于自适应阈值才聚类）是"推迟决断"的工程模板；(4) BCPD（D3）的 run-length 后验允许在线输出"边界概率"，事后用全序列重估（这为 retrospective 提供了概率基础，但论文未展示该操作）。
- **不支持（缺口）**：没有任何 D 组论文研究"在线先给 provisional episode，会话后用另一个（更强的）模型**重新分割并修正已输出边界**"的显式两阶段架构。D5 没有做"Episode A [10s,15s] 在线输出 → 会话后修正为 [10s,13s] + [13s,15s]"这类演示。**因此该架构是合理的项目假设，但不是文献已验证的结论。**

### 对文献支持性的最终判断

- **Online + Offline both feasible → SUPPORTED**（D5 实证）。
- **Online provisional → 有间接支持**（warm-up 效应、E2USD 延迟聚类、BCPD 后验；但均属"推迟决断"，非"在线提交后修改"）。
- **Offline retrospective refinement → PROJECT ARCHITECTURE HYPOTHESIS**：这个架构思想仍然很好，但**不能说已经被 D5（或任何 D 组论文）验证**；具体架构是项目设计决策（任务文件 §14 只要求判断文献支持性，不提前设计最终系统）。

---

## 17. 分割不确定性

> 对应任务文件 §15 专题八。回答"后续系统是否有理论依据保留 boundary confidence 而非只存 boundary=TRUE"。

### # 动作边界有多确定？

| 方法路线 | 边界/状态输出的不确定性形态 | D 组证据 |
|---|---|---|
| **Rules / Grammar** | **hard boundary**；无置信度 | D6 正则匹配、D5 四检查、D1 噪声标记全部输出硬决定；D5 唯一的软信号是上下文相似度 sim(c_i,c_{i+1})（可与阈值 t 比较，但论文不作置信度输出） |
| **CPD（统计检验类）** | **检验统计量 + p 值**（变点显著性的直接度量） | D2 的 OCPD 输出 Bartlett 检验统计量 Ti 与 p 值（BH 校正后与 α 比较）；D3 的 GP 方法输出 p 值 |
| **CPD（贝叶斯类）** | **run-length 后验分布** P(r_t\|x_1:t)——最完整的边界概率 | D3 §3.2.3 BCPD（Adams & MacKay）：每个时刻都有"距上个变点多远"的概率分布 |
| **HMM** | **逐点状态后验** p(x_n\|y) | D4 §2（MPM 依赖前向后向算 p(x_n\|y)、p(v_n,v_{n+1}\|y)） |
| **HSMM** | **后验 + 时长后验** p(x_n\|y) 与停留时间分布 | D4 同前 + 显式时长分布 |
| **Task abstraction** | **聚类相似度/标签唯一性**（弱置信度） | D5 的 DenStream 可分置信度（微簇密度）、tf-idf 标签区分度（论文未输出） |

### 回答：是否有理论依据保留 boundary confidence？

**有，且证据较强（D3/D4 的概率方法）。** 三个独立来源：
1. **D4（HSMM/MPM）**：每个时间点的状态概率 p(x_n|y) 是分割的**直接产物**，不是额外计算——"boundary 的置信度"可定义为状态切换前后两侧概率的差距或后验不确定度。这是数学上免费获得的不确定性。
2. **D3（BCPD）**：run-length 后验直接给出"变点在 t 的概率"（r_t 从 0 重新开始 = 变点）。这是为在线场景设计的边界概率分布。
3. **D2（OCPD）**：检验统计量/p 值本身就是"此处有统计显著变化"的置信度，只是论文没把它作为输出。

**规则类方法（D5/D6/D1）不提供，但可自建弱置信度**：(1) D5 的 sim 分数与阈值 t 的距离；(2) D6 的匹配歧义度（同一片段匹配多个 pattern）；(3) D1 的转移概率值与阈值 ξ 的距离。这些都不是论文输出，**属于我们的设计选项**（PROJECT TRANSFER INFERENCE）。

**项目含义**：如果我们选用规则/grammar 为主干（§11 的结论），则必须自行设计 boundary confidence（如 sim 余量、匹配歧义度），否则只能存硬边界；如果对 pointer/scroll 连续流用 CPD/HSMM（§20/§21 的候选），置信度是免费副产品。**任务文件 §15 的问题"只存 boundary=TRUE 还是保留 confidence"——D 组文献明确支持后者有理论依据，且对概率路线零成本。**

---

## 18. 混合事件流

> 对应任务文件 §16 专题九。这是我们系统与传统 time-series segmentation 最大的区别。

### 我们的流是什么

```
t1 pointer(x,y)
t2 pointer(x,y)
t3 scroll(deltaY)
t4 pointer(x,y)
t5 question_navigated(Q2)
t6 click(option B)
...
```
= 连续（pointer/scroll 采样）+ 类别（事件类型）+ 语义（目标/对象）+ 异步（非等间隔、事件频率不均）。

### D1–D7 对 mixed events 的兼容性

| 方法 | 原生支持 | 需要 encoding | 基本不适合 |
|---|---|---|---|
| D1 MMAD | 部分（多属性离散动作） | — | 连续流、时间间隔 |
| D2 OCPD | — | 把流重采样为等间隔数值通道 | 离散语义事件（会丢失） |
| D3 各方法 | — | 全部需向量化（多数假设 i.i.d./平稳） | 事件序列语义 |
| D4 HSMM | — | 编码为等间隔数值观测（需离散化/重采样） | 异步事件（非等间隔） |
| D5 Task-Level | **原生支持异构语义事件**（P/V 属性集） | — | 连续采样流（pointer/scroll） |
| D6 Grammar | 部分（靠人工 code-book） | 需统一事件类 schema | 连续值、时序 |
| D7 各方法 | — | 多元连续数值原生；事件需编码 | 事件语义、时序约束 |

**核心格局**：**D5 是唯一"原生支持异构语义事件流"的方法**（事件类 = P 属性集，天然多类型）；所有连续值方法（D2/D3/D4/D7）都需要先把混合流**编码/重采样为等间隔数值序列**。D5 与连续方法刚好互补：D5 缺连续流能力，连续方法缺事件语义。

### 两种表示：event-based sequence vs fixed-rate multivariate time series

**（任务文件 §16 要求讨论各代价；这直接影响我们的数据架构，§27 Q9 汇总）**

**Event-based sequence（D5 式）**：
- **优点**：保留事件语义（类型、目标、数据值）；天然支持异步；不丢信息；事件类可聚合成任务/chunk。
- **代价**：(1) 连续流必须预先聚合（pointer samples → 事件，丢失轨迹细节或需额外保留）；(2) 规则/共现/聚类都基于事件类，对"同类型事件的时长/强度"不敏感（D5 不用时间戳即其后果）；(3) 事件类爆炸（s_v=1000 的向量）需控制。

**Fixed-rate multivariate time series（D2/D3/D7 式）**：
- **优点**：(1) 直接对接成熟的 CPD/HSMM/profile 方法库；(2) 等间隔使统计检验、时频特征、窗口化可用；(3) 可建模数值强度（pointer 速度、scroll velocity）。
- **代价**：(1) **异步事件必须重采样**——离散语义事件（click/navigate）要么被插值成数值通道（丢失语义位置），要么在采样间隙"丢掉"，要么需要同步标记（混合表示）；(2) 重采样引入时间对齐误差（事件发生在采样点之间）；(3) 语义（目标、对象）必须另行编码（one-hot/嵌入），编码维度与稀疏性成为负担；(4) 非平稳/非 i.i.d. 违反多数 CPD 假设。

**文献支持度**：D 组**没有**论文直接比较两种表示在 UI 流上的效果。D5 内部隐含支持"event-based 足够做任务级"（且其事件流里无连续量）；D2/D4/D7 内部隐含支持"数值序列足够做状态级"（其数据里无事件）。**混合表示（事件为主干 + 连续流作为子序列特征）是合理推论，但属于 OPEN DESIGN QUESTION。**

---

## 19. 原子事件 vs 组合动作

> 对应任务文件 §18。不是所有东西都需要 segmentation。

### 三类划分（D 组文献依据）

**1. Atomic Semantic Events（不需要 segmentation）**
本身已是语义原子，边界=事件发生/完成。D5 的"answer click"类操作、D2 中"click button"、D1 的 action 行都是这种。**证据**：D2 的识别正确性不依赖其内部边界（其 2.56s 窗口分类在事件上不需要精确位置）；D5 把单个 click/input 当作不可再分的事件单元。
→ **我们的候选**：`answer_option_clicked`、`question_navigated`、`underline_created/removed`、`option_elimination_toggled`、`text_selection_committed`（如果目标是单一原文段）。这些事件**带语义、带时间戳、带目标**，直接作为 atomic actions 进入事件序列，**不需要 segmentation**。

**2. Continuous Low-Level Streams（必须 segmentation）**
连续采样（pointer/scroll）若不聚合成 episode，只是无意义的样本堆。**证据**：D2 的整个动机就是"原始连续流必须分割才能做识别"（固定窗口/变点）；D4 对连续序列做状态分割；D7 的 BD/SD 全部针对连续流。
→ **我们的候选**：`pointer_sampled` × N → POINTER_MOVEMENT_EPISODE / POINTER_INACTIVE_EPISODE / POINTER_TRANSITION；`passage_scroll_sampled` × N → SCROLL_BURST。**这些必须 segmentation**（§20/§21 讨论边界依据）。

**3. Composite Multi-Event Actions（需要 pattern abstraction）**
由多个不同事件按模式组合而成。**证据**：D5 的 task = chunk 组合（四检查聚合子任务）；D6 的 non-terminal = 正则组合 terminal；D1 的模板=动作序列。
→ **我们的候选**：`TEXT_MARKING_EPISODE`（pointer move → text selection → underline 的组合）、`PASSAGE_TO_QUESTION_SWITCH`（passage 区域事件 → question 区域事件的转换）、`QUESTION_REVIEW`（question 内多事件序列）。**需要 pattern abstraction（grammar 或规则或聚类）。**

### D 组最终对数据架构的贡献（任务文件 §18 原话）

| 类别 | 处理方式 | 代表动作 |
|---|---|---|
| Atomic Semantic Events | 直接入事件序列，不分割 | ANSWER_SELECT、QUESTION_NAVIGATE、UNDERLINE_CREATE/REMOVE、OPTION_ELIMINATE/RESTORE |
| Continuous Low-Level Streams | 必须 segmentation（规则/CPD/状态模型） | pointer 流 → POINTER_*_EPISODE；scroll 流 → SCROLL_BURST |
| Composite Multi-Event Actions | pattern abstraction（grammar/规则/聚类） | TEXT_MARKING_EPISODE、PASSAGE↔QUESTION_SWITCH、QUESTION_REVIEW |

---

## 20. 滚动分割

> 对应任务文件 §19。我们系统非常依赖 scroll；不能"每个 wheel event = 一个 action"。

### 文献能支持什么（以及缺什么）

**直接 scroll 文献：D 组没有。** 没有一篇 D 组论文处理 scroll 事件的 burst 分割。因此本节依据是 **PROJECT TRANSFER INFERENCE**（任务文件 §19 明确允许：D 组没有直接 scroll 文献时，明确写 PROJECT TRANSFER INFERENCE）。

**可借用的机制**：
1. **规则聚合（推荐主线）**：把 scroll 事件按时间/速度/方向聚成 burst。依据：D6 的 grammar 框架（terminal = scroll 事件 + 时间约束），D5 的 chunking 思路（用"结束信号"判定 chunk 完成——对应我们的 scrollend 事件或间隔超时）。
2. **CPD（备选）**：D2/D3 的变点检验作用于 scroll velocity/density 序列——burst 的边界 = 滚动速度分布的变化。但需验证"scroll 减速"（段落末尾自然减速）不误报（§12 的教训）。
3. **HSMM（理论选项）**：D4 显式时长建模 scroll-active / scroll-inactive 状态——burst 长度分布可直接建模（但需先确认 scroll 状态时长非几何）。

### 需要回答：SCROLL_BURST 边界依据

| 候选依据 | 机制 | 支持文献（间接） | 我们的判断 |
|---|---|---|---|
| **time gap threshold** | 两 scroll 事件间隔 > τ → 边界 | D5 未用时间戳（明言缺口）；D3 窗口概念 | **核心依据**（PROJECT TRANSFER INFERENCE）。τ 必须实证标定，不能拍脑袋 |
| **scrollend 事件** | 浏览器原生 scrollend = burst 结束信号 | D5 的 completion keyword 思路（chunk 结束信号） | **最直接的语义边界**（若我们的系统记录 scrollend） |
| **velocity continuity** | 连续同向、速度 > 阈值 = 同一 burst | D2 的统计变点思路（数值特征变化） | 辅助依据，用于无 scrollend 时的兜底 |
| **direction** | 方向翻转 = 新 burst（回读） | 无直接文献 | 方向翻转是"回读"的证据，但**是否算新 burst 是语义决策**（可能属于同一阅读段落内的回读）——行为层定义需明确 |
| **change point** | 在 scroll 速度序列上跑 CPD | D2/D3/D7 | 备选；先验证不误报 |
| **窗口固定阈值** | 固定时间窗聚合 | D2 的固定 2.56s 窗教训 | **不推荐**：D2 证明固定窗口对短时状态失效 |

### 判断：rule-based aggregation 是否足够？

**对 SCROLL_BURST：是，规则聚合足够且更合理。** 理由：(1) 边界有明确语义信号（scrollend、间隔、方向翻转），规则直接编码；(2) 无标签、确定性、可审计（D6 的教训：terminal 要保留区分度——scroll terminal 必须含时间/方向属性，否则 95.43% 单 terminal 问题重演）；(3) D 组无证据表明 ML/CPD 在此确定型行为上更优。**CPD/HSMM 留给更模糊的 pointer 流（§21），scroll 用规则。**

---

## 21. 指针片段分割

> 对应任务文件 §20。结合 C + D。C 组已确定 active/inactive/text-following/action-click 四类 pointer 状态；D 组回答"怎样从连续 pointer samples 中分段"。

### 候选依据清单（任务文件 §20 要求"不要提前选最终算法"，但给出候选）

| 候选依据 | 机制 | D 组支持 | 备注 |
|---|---|---|---|
| **speed** | pointer 速度变化 = 状态切换（移动 vs 静止） | D2 的统计变点（数值流）、D7 的 CPD/BD | 最核心；但"减速"（接近目标）需防误报（§12） |
| **acceleration** | 加速/减速模式区分主动移动与过渡 | D2 的矩特征、D3 的统计检验 | 二阶特征；对噪声更敏感 |
| **direction** | 方向稳定（文本跟随）vs 方向变化（扫描） | 无直接文献 | TEXT_FOLLOWING_LIKE 的候选判据（PROJECT TRANSFER INFERENCE） |
| **pause / inactivity** | 长停顿 = 静止/阅读状态 | D2 的 TA（过渡短时）概念、D4 的时长建模 | 与 POINTER_INACTIVE_EPISODE 对应；时长分布是 HSMM 的用武之地（§13） |
| **semantic target** | pointer 所在语义区域（passage/question/选项）决定状态 | D5 的对象/上下文属性、C 组的 viewport | **关键**：把空间目标纳入分段（同区域 = 同 episode 倾向） |
| **click** | click 标记动作边界 | D5 的语义事件、§19 的 atomic events | click 本身是 atomic；click 前后 pointer 段需重标 |
| **change point** | 在速度/位置序列上跑 CPD/BCPD | D2、D3（BCPD run-length 后验）、D7（FLOSS profile） | 在线候选；FLOSS 的 profile 局部极值 + 需指定 N 的缺陷需处理 |
| **duration** | 显式时长建模 pointer 状态 | D4（HSMM）、D7（HDP-HSMM） | 候选主力之一（READING-LIKE 长 vs TRANSITION 短） |

### 分段路线（不锁定最终算法，只给文献支持的分层）

1. **最简可辩护路线**：**速度/停顿阈值 + 语义目标**（C 组的四状态 × 空间区域）→ 规则化 episode。理由：C 组已给出状态语义，D5 已给出空间/上下文编入事件的先例；规则确定、可审计。
2. **进阶概率路线**：在速度/位置特征序列上跑 **CPD/BCPD**（在线、带后验）或 **HSMM**（显式时长、离线）。理由：D2/D3/D4 提供机制；当规则无法处理"减速 vs 边界"歧义时，概率模型给出置信度。
3. **明确不推荐**：固定时间窗口（D2 的 2.56s 教训对短时 POINTER_TRANSITION 失效）。

**关键提醒**：把 pointer 段解释成 attention/reading 是 C 组明确禁止的（§7.13 任务文件 §32-13）——D 组只做行为层分段（active/inactive/transition），不命名认知。**D 组输出的是"pointer episode 的分段 + 行为层标签"，认知解释留给 E 组。**

---

## 22. 多尺度分割

> 对应任务文件 §21。可能存在多个层次：Level 1 pointer sample → Level 2 pointer episode → Level 3 question↔passage cycle → Level 4 strategy trace。D 组只负责 Level 1→2 及部分 Level 2→block。

### D5/D6 是否支持层级 abstraction？

**支持，且两者都显式支持层级**：
- **D5**：三层级 pipeline——事件 → chunk（子任务）→ task。其 Algorithm 1 中 chunk 聚合为 task 是显式层级抽象；task → task-level events（带 lifecycle）再加对象关联。**这就是"Level 1→2→3"的分层模板。**
- **D6**：terminal → non-terminal（正则递归支持 non-terminal 作为其他 non-terminal 的函数，§3.1"function of functions"）；四层分类学层级（interaction → sequence → task → goal，§2.1 Fig. 1）。**显式支持多层嵌套。**

### D 组对层级模型的职责边界（任务文件 §21 原话）

| Level | 内容 | D 组职责 |
|---|---|---|
| Level 1 | pointer sample / scroll event | 原始流（去噪 D1，聚合 §20/§21） |
| Level 2 | pointer episode / SCROLL_BURST | **D 组核心**（§19-21） |
| Level 3 | question→passage→question cycle | **部分**：D5 的 chunk→task 聚合逻辑可迁移（跨区域事件流聚合）；D6 的 grammar 可表达"PASSAGE_TO_QUESTION_SWITCH"模式 |
| Level 4 | reading strategy trace | **超出 D 组**（→ E 组） |

**操作含义**：(1) Level 1→2 用 §19-21 的方法（规则/CPD/状态模型）；(2) Level 2→3（stable behavioral blocks）用 D5 式的"跨 episode 聚合"（上下文/数据/控制流检查）或 D6 式的 grammar；(3) **不能直接跳到 strategy**——Level 3 的输出仍是行为块（如"阅读段落→做第 3 题"），不是策略判断。**任务文件 §21 的"不能直接跳到 strategy"由 D5/D6 的架构自然保证（它们都停留在行为/任务层）。**

---

## 23. 候选动作词汇表

> 对应任务文件 §17。基于 A/B/C + D 文献，提出候选 Action Vocabulary。**只允许行为层，不允许 cognition。** 对每个候选判定：是否作为 segment、是否已是 atomic event、是否需要聚合。

| 动作 | 原始事件 | 边界规则 / 候选方法 | 需要分割？ | 置信度 |
|---|---|---|---|---|
| **SCROLL_BURST** | passage_scroll_sampled × N | 时间间隔阈值 + scrollend + 方向/速度连续性（规则聚合为主，CPD 备选，§20） | **是**（连续流聚合） | **MODERATE / PROJECT TRANSFER INFERENCE**（规则机制确定，但 D1–D7 无任何一篇直接研究 scroll burst segmentation；阈值需 GT 标定） |
| **POINTER_MOVEMENT_EPISODE** | pointer_sampled × N（速度 > 阈值） | 速度/加速度阈值 + 语义目标（规则或 CPD/BCPD，§21） | **是** | **MODERATE**（速度/边界/时长/目标都需 GT 标定） |
| **POINTER_INACTIVE_EPISODE** | pointer_sampled（静止/微动）持续段 | 速度≈0 + 时长（规则；时长分布适合 HSMM） | **是** | MODERATE（inactive 判定依赖阈值与时长下限） |
| **POINTER_TRANSITION** | pointer 快速跨区域移动 | 速度峰值 + 区域切换（CPD/规则，§21） | **是** | **WEAK–MODERATE**（短时状态，与 MOVEMENT 的边界高度依赖阈值与时长标定） |
| **TEXT_FOLLOWING_LIKE_EPISODE** | pointer 沿文本行移动 | 方向稳定性 + 低速 + 文本区域（规则；判据需验证，§21） | **是** | WEAK（C 组概念，D 组无直接判据；需验证） |
| **QUESTION_NAVIGATE** | question_navigated(Q_i) | atomic（事件本身） | **否**（atomic semantic event，§19） | STRONG |
| **PASSAGE_TO_QUESTION_SWITCH** | 事件语义目标从 passage 区→question 区 | 语义目标区域变化（D5 上下文/数据检查思路、D6 grammar，§22） | **聚合**（跨 episode 模式） | MODERATE |
| **QUESTION_TO_PASSAGE_SWITCH** | 同上反向 | 同上 | **聚合** | MODERATE |
| **TEXT_SELECTION** | text_selection_committed | atomic | **否** | STRONG |
| **UNDERLINE_CREATE** | underline_created | atomic | **否** | STRONG |
| **UNDERLINE_REMOVE** | underline_removed | atomic | **否** | STRONG |
| **TEXT_MARKING_EPISODE**（组合） | pointer→selection→underline 序列 | grammar/规则（D6 terminal+正则，§19） | **聚合**（Composite） | MODERATE |
| **OPTION_ELIMINATE** | option_elimination_toggled（true） | atomic | **否** | STRONG |
| **OPTION_RESTORE** | option_elimination_toggled（false） | atomic | **否** | STRONG |
| **ANSWER_SELECT** | answer_option_clicked | atomic | **否** | STRONG |
| **ANSWER_CHANGE** | 同一 question 两次 answer_option_clicked 且选项不同 | 规则（同题两次 answer 且值变化；§11） | **聚合**（2 个 atomic → 1 个事件） | **STRONG**（定义为前后 answer atomic events 的确定组合；匹配规则本身是确定逻辑） |
| **VISIBILITY_INTERRUPTION** | visibility_changed / layout_changed | atomic（显式标记，不删除） | **否** | STRONG |

### 设计注记

1. **"是否应该作为 segment"由 D 组研究决定的结果**：绝大多数语义事件（answer/underline/navigate/eliminate）是 **atomic**，不需要 segment；只有**连续流**（pointer/scroll）需要 segment；**组合模式**（switch、marking、change）需要 pattern abstraction。这与 §19 的三类划分一致。
2. **Confidence 分级逻辑（反馈修正后）**：**atomic 语义事件 → STRONG**，因为它们（如 `option_elimination_toggled`、`answer_option_clicked`、`underline_created`）是系统直接观察到的事实，甚至不存在复杂 segmentation 问题；**连续流 → MODERATE 或更低**，因为 `pointer_sample × N → POINTER_TRANSITION` 涉及 threshold、boundary、speed、duration、target 等多处判断，而 D1–D7 没有任何一篇直接验证它们在英语阅读 UI 上的表现，全部需要 GT 标定。ANSWER_CHANGE 为 STRONG 的前提是它被定义为"前后 answer atomic events 的确定组合"（匹配规则确定）。
3. **与任务文件 §17 清单的差异**：任务文件列的 candidate 基本全部保留；差异点是明确标出 **ANSWER_CHANGE 是"2 个 atomic 的组合"** 而非单独事件（需要一个匹配规则）；**VISIBILITY_INTERRUPTION 不删除**（§10——它是系统事件但有价值：告诉我们学生是否切出页面、布局是否变化，作为显式语义事件保留，不是噪声）。
3. **所有 ACTION 的名称都是行为层**：不包含 reading/attention/strategy 语义（TEXT_FOLLOWING_LIKE_EPISODE 是"行为形态描述"，不是"正在阅读"的认知断言——这是 C 组 §7.13 的纪律）。

---

## 24. 评估框架

> 对应任务文件 §22。为未来实验建立 D 组专用评估框架，至少四层。文献依据：D3 的指标分类（§2.3）、D7 的 BD/SD 指标组合（§3.1）、D1 的 noise 指标、D5 的 identification/categorization 指标。

### 24.1 Event Cleaning（D1 模板）

```
noise precision = TP/(TP+FP)      noise recall = TP/(TP+FN)      noise F1
```
- TP = 噪声事件且被标记为噪声；FP = 非噪声被误标；FN = 噪声漏标。
- **关键**：必须先定义"什么是噪声"（§10 三类）并把 GT 做成事件级标注（人工或注入）。

### 24.2 Boundary Detection（D3 + D7 模板）

```
boundary precision / recall / F1          （以事件/采样点为单位的分类）
tolerance-window F1                        （GT 边界 ±w 内算 TP）
boundary displacement（MAE/MSE/MSD/RMSE）  （预测边界与实际边界的距离，D3 定义）
scoring function error（Gharghabi）        （D7 Eq. 2：平均最近距离，需注意不做二部匹配）
```
- **D7 的建议：F-Measure + 评分函数同时用**（§3.1.1）。
- **D3 的提醒**：若性能是"边界时间差"，MAE/RMSE 系指标；若是"变点 yes/no"，用分类指标——**不要混用**。

### 24.3 Segment Quality（D5 + D7 模板）

```
segment overlap / IoU（预测段与 GT 段）
edit distance（D5 的 normalized edit distance——衡量 segment 内容相似度）
ARI / NMI（D7 的 SD 指标，点级聚类质量）
```
- **D5 用 edit distance + Rand/Jaccard 的教训**：编辑距离对边界位置不敏感，必须与 §24.2 的边界指标联合使用。

### 24.4 Action Recognition（D5 模板）

```
accuracy / macro F1 / confusion matrix（对命名 action 的识别）
```
- 仅在 action 标签有语义名时适用（D5 的 task type + tf-idf label）。

### 重点回答任务文件 §22 的三个问题

**Q: 如果 boundary 相差 200ms，算错吗？**
D7 给出了直接答案：**200ms 的差不应算错**——"state transitions are not instantaneous, predictions near the ground truth boundary points should also be considered as correct"（§3.1.1）。状态转换本身是渐进的，GT 也有标注误差。**200ms 差应计入 tolerance window 的 TP，或通过 displacement 指标反映其小偏移，而不是二元判错。**

**Q: 如果 segment label 正确但边界偏差 1s，算什么？**
**分两层报告**（§15）：边界层按 §24.2 计 displacement 误差（1s 偏差被量化），segment/action 层按 §24.3-24.4 计 label 正确。**结论：label 正确 ≠ 边界正确**（D2/D5 已证明二者可分离）；报告必须同时给出两层，禁止合并成一个分数。

**Q: UI action segmentation 应采用怎样的 tolerance？**
**D 组无直接答案 → OPEN DESIGN QUESTION。** D7 的 tolerance 讨论针对 sensor 数据（秒级）；我们的 UI action 时间尺度（pointer episode 秒级、scroll burst 秒级、answer click 毫秒级）需要实证标定。**初步方向（PROJECT TRANSFER INFERENCE）**：tolerance 应与目标 action 的最小可区分时长同量级（如 pointer transition 的 tolerance 应远小于 reading-like episode 的 tolerance），并按 action 类型分别设定，不能用一个全局 tolerance。

---

## 25. 分割真值

> 对应任务文件 §23。单独研究 action boundary labels 的来源。

### # 动作边界标签从哪里来？

**D 组各论文实际使用的 GT：**

| 论文 | GT 来源 | 类型 | 可迁移性 |
|---|---|---|---|
| D1 | **人工注入噪声**（在真实日志中按比例注入并预先标记噪声行） | 噪声 GT（Event Cleaning） | 可迁移（但需注意注入噪声 ≠ 真实噪声） |
| D2 | SBHARPT 数据集自带活动标签（受试者按脚本执行 12 类活动） | 活动标签（Action Recognition 层） | **无边界 GT**（只有活动段标签） |
| D3 | 综述列举：ECG 医学专家手工分段、BCI 任务切换时间、smart home 活动标签等 | 变点/分段 GT | 展示了多来源（人工分段、任务脚本、传感器转换） |
| D4 | 合成序列（已知真实状态序列）+ 无 GT 的真实 SAR 图像 | 合成 GT；真实数据无 GT | 合成 GT 可迁移 |
| D5 | 任务日志自带 task ID（GT task instances）+ **作者两人人工标注 object instances**（独立标注→讨论调和） | Task GT + Object GT | **人工标注先例**（D5 的标注流程是模板） |
| D6 | 人工编码 code-book（inter-rater 0.99）；Wall 数据集带参与者任务 | 映射 GT（非边界 GT） | 人工编码流程可迁移 |
| D7 | 综述列举 UCR-SEG（每领域一个时间序列）、TSSB（**半合成拼接**：把同 class 的时间序列拼接，拼接位置标记为边界）、MoCap（**视频提供 GT**）等 | BD/SD GT 基准 | **拼接法**（TSSB）与**视频对照**（MoCap）是两种可迁移策略 |

**关键发现**：
1. **没有任何 D 组论文在真实 UI 交互流上有人工标注的 action 边界 GT**。D5 最接近（人工标注 object instances），但 task 边界 GT 来自任务日志自带 ID，不是人工标的。
2. **TSSB 的半合成拼接法**（D7）是获取边界 GT 的低成本路径：把同类型行为段拼接，拼接点即 GT 边界。
3. **MoCap 的视频对照法**（D7）：真实行为 + 视频记录作 GT——与我们的"screen replay + event timeline + human annotation"思路直接呼应。

### 我们未来英语阅读场景最可行的 GT 方式

**（任务文件 §23 要求分析；以下推荐均为 PROJECT TRANSFER INFERENCE，非"文献直接验证"）**
1. **Screen replay + event timeline + human annotation（推荐主线）**：把 session 录屏与事件时间线对齐，标注员标记"动作边界与动作类型"。方法学先例：D7 的 MoCap 视频对照标注、D5 的人工标注流程（独立标注 → 调和 → 一致性度量）、D6 的 inter-rater 流程（0.47→0.99 三轮迭代）。**但注意：没有论文直接做过"英语阅读页面 + screen replay + pointer/scroll timeline + micro-action boundary annotation"这个具体协议——它提供了方法学先例，不构成对该协议有效性的直接验证，实验仍需我们自己设计。**
2. **TSSB 式半合成拼接（低成本补充）**：把已标注的真实 episode 段拼接成合成 session，拼接点为"已知 GT 边界"，用于算法开发与调参。
3. **任务脚本（D2 式）**：受控任务（如"先读第一段，再答第 1 题"）产生可预测边界——但生态效度低（学生自然阅读不会按脚本），只适合开发期。

**注意（任务文件 §23 原话）**：这里只讨论 **action boundary ground truth**，不是 cognitive ground truth。标注员只标"行为层边界/类型"，禁止标"在理解/困惑"（后者是 E 组的 construct validation 领域，§29）。

---

## 26. 方法比较矩阵

> 对应任务文件 §24。最终比较七类方法族。任务文件 §25 警告：**不要强行选一个万能算法**——允许结论是"不同 action 类型适合不同方法"。

| 方法族 | 代表论文 | 在线 | 无监督 | 时长模型 | 混合事件 | 可解释性 | 边界不确定性 | UI 相似度 |
|---|---|---|---|---|---|---|---|---|
| 规则 / FSM | D5（chunking+四检查）；D1（模板+阈值） | ✓（D5 在线） | ✓ | ✗ | ✓（事件类） | 高 | ✗（硬边界） | **高** |
| 语法 | D6 | ✗（论文离线） | ✓（无标签，需 code-book） | ✗（明言无法表达时序） | △（靠人工映射） | **最高** | ✗ | 中 |
| 经典 CPD | D3（CUSUM/密度比/BCPD） | △（ε-real-time 谱系） | ✓ | ✗（BCPD 有 hazard 先验） | ✗（需编码） | 低 | **BCPD 有 run-length 后验** | 低 |
| 在线 CPD | D2（OCPD） | ✓（窗口级延迟） | 边界层 ✓ / 识别层监督 | ✗ | ✗ | 低–中 | 内部 p 值（未输出） | 低 |
| HMM | D4；D7 | ✗（离线） | ✓（需 K） | ✗（implicit geometric） | ✗（需编码） | 低 | ✓（逐点后验） | 低 |
| HSMM | D4；D7（HDP-HSMM） | ✗（离线） | ✓（需 K/P，HDP 版需 α） | **✓（显式时长）** | ✗（需编码） | 低–中 | **✓（后验+时长）** | 低 |
| UI 任务抽象 | D5 | ✓（双设置） | ✓（无需 K） | ✗（不用时间戳） | **✓（原生）** | **高（文本标签）** | ✗（仅 sim 分数） | **最高** |

### 结论（任务文件 §25 的允许性结论，D 组证据支持）

```
确定性 semantic event  （answer click、question navigate、underline）  → no segmentation（atomic，§19）
scroll burst            → rules + time-gap + scrollend（§20）
pointer activity        → rules / CPD / HSMM（§21；按状态类型选择）
known interaction pattern（switch、marking） → grammar / rules（§11、§22）
ambiguous latent activity → probabilistic model（HSMM/BCPD，§13、§17）
```

**必须强调**：**没有任何 D 组论文证明"单一算法对所有 action 最优"**；相反，D5 的消融（语义/数据/控制流各有分工）与 D6 的表达力教训、D7 的方法分类都指向"分 action 类型选择机制"。**报告不得强行宣布 HSMM 或 D5 为"最终最优方案"。**

---

## 27. 18 个跨论文研究问题

> 对应任务文件 §26，18 问逐答。每条标注证据强度（Strong / Moderate / Weak / Open）。

### Q1. `denoising` 和 `segmentation` 的边界是什么？

**答案**：Denoising 回答"**哪些 event 不应进入后续分析**"（标记/排除异常、重复、无关事件；Raw Observable Events 永久保留，只在 derived 层排除）；Segmentation 回答"**连续流如何切成 episodes**"（找边界）。二者独立：D1 只做前者（输出带噪声标签的日志，不切段）；D2/D3/D4/D7 做后者（不删事件）；D5 在两者之间有一层"overhead 过滤"（把登录等语义噪声排除在任务之外）但核心是切任务。**没有 D 组论文把去噪当作分割的一步或反过来。** 证据：D1 Future Work 明言"去噪后用于 task-level segmentation 是未来工作"。**Strong。**

### Q2. UI log 中什么才是可以合理定义的 `action boundary`？

**答案**：取决于 action 类型（任务文件 §4.2 的"action 从哪里开始/在哪结束"）：
- **语义原子事件**（answer click、question navigate、underline）——边界 = 事件发生/完成，**无需推断**（§19）。
- **连续流**（pointer/scroll）——边界 = 速度/方向/时间聚集状态变化（§20/§21），**需要推断**。D 组无 UI 直接证据，定义方式是 OPEN DESIGN QUESTION，但候选依据明确（时间间隔、scrollend、速度阈值、语义目标、时长分布）。
- **组合模式**（switch、marking）——边界 = pattern 完成（D5 chunk、D6 grammar）。
**没有单一答案：UI log 的边界定义必须按 action 类型分别给出。** Moderate（机制明确，数值待标定）。

### Q3. Change Point Detection 能不能直接等价 Action Boundary Detection？

**答案：不能。** 三个独立证据：(1) D3 定义：变点 = 分布变化（H0/HA），是统计假设检验，与语义无关；(2) D7：CPD（统计性质变化）≠ BD（状态/制度变化，可无统计变化）；(3) D2 机制：方差变点会把"同 action 内减速"误报为边界（§12）。**统计 boundary ≠ semantic boundary。** CPD 对"边界确实由底层数值分布变化产生"的 action（pointer/scroll 连续流）适用，对"自带语义的事件"（click）不适用。**Strong。**

### Q4. 哪些 action 最适合 `rules / grammar`？

**答案**：**模式确定、语义可枚举、边界有明确信号**的 action：SCROLL_BURST（时间/scrollend/方向）、ANSWER_CHANGE（同题两次 answer 值变化）、OPTION_ELIMINATION（toggle 序列）、UNDERLINE/TEXT_SELECTION（语义事件序列）、PASSAGE↔QUESTION_SWITCH（区域变化模式）。依据：D5 的关键词 chunking + 四检查、D6 的 grammar（terminal 区分度 + 正则）。**对确定型行为规则比 ML 更合理（无标签、可审计、无 K/N）。** Strong（对列出的行为）；Weak（对模糊连续流）。

### Q5. 哪些 action 更需要 `probabilistic segmentation`？

**答案**：**边界信号弱、状态潜伏、时长结构重要**的 action：POINTER 连续流的潜伏态（active/inactive/transition 的模糊边界，§21）、READING-LIKE 长时段（时长分布建模）、需要"边界置信度"的场景。依据：D4（HSMM 显式时长 + 逐点后验）、D3（BCPD run-length 后验）、D7（HDP-HSMM 处理非马尔可夫）。**当规则的边界信号不可靠时，概率模型提供置信度。** Moderate（机制支持，UI 实证缺失）。

### Q6. HMM 与 HSMM 对我们最大的实际区别是什么？

**答案**：**时长表达力**。HMM 的停留时间被 geometric 分布约束（均值决定方差、右尾厚、无最小停留），无法表达"POINTER_TRANSITION 通常短、READING-LIKE 通常长且时长可控"；HSMM 可显式指定任意（non-geometric）时长分布（D4 §3.1）。若我们的行为状态确实有非几何时长结构，HSMM 有理论优势；若没有，HSMM 只是多了参数负担（D4 §5.1：数据是 HMC 时 RHSMC 无增益甚至略差）。**最大实际区别 = 能否表达"状态通常持续多久"以及能否分离"时长"与"转移"两个概念。** Strong（机制）；应用条件待验证。

### Q7. explicit duration modeling 是否值得？证据有多强？

**答案：值得，但是条件性的。** 支持证据（D4 §5.3）：数据具有非马尔可夫时长/非平稳结构时，NS-RHSMC 明显优于 NS-HMC（类错误 25% vs 30%，纹理 9% vs 18%）。反对证据（D4 §5.1）：数据只是 HMC 时无增益、高噪声下略差（参数更多）。D7 补充 HDP-HSMM vs HDP-HMM（HDP-HMM 状态数膨胀）作为机制论据。**综合：证据强度 Moderate——显式时长在"状态确有稳定时长分布"时有明确收益；在"时长无结构"时有害；需要先用时长直方图/拟合检验确认我们的状态结构再决定。** 不因 HSMM 复杂就默认更好。

### Q8. D5 的 task-level segmentation 与我们的 micro-action segmentation 粒度差多少？

**答案：差一个到两个层级。** D5 的 task = 10.1–73.5 个事件的跨应用工作单元（create order）；我们的 micro-action（SCROLL_BURST、POINTER_TRANSITION）是秒级、单一行为类型的短段。D5 的 chunk ≈ 我们的 episode 级或略粗；D5 的 task ≈ 我们的"question↔passage cycle"上层。**粒度差异：D5 task >> 我们 micro-action。** 因此 D5 的四检查边界逻辑不能直接搬到 micro-action 层（需更细的时间/速度/语义依据）；但其架构模式（对象/识别/类型三组件、双设置、涌现类型）可迁移。**Strong（有 Table 2 事件数实证）。**

### Q9. 我们的 heterogeneous UI stream 应该表示为 event sequence 还是 fixed-rate time series？

**答案：文献不支持二选一的确定答案，合理路线是"事件为主干 + 连续流子序列特征"的混合表示。** 论据：(1) D5 证明 event-based 足以做任务级（且无连续量）；(2) D2/D4/D7 证明数值序列足以做状态级（且无事件）；(3) D 组没有论文在 UI 流上比较两种表示（无直接证据）。event sequence 代价：连续流细节需预先聚合、对时长/强度不敏感（D5 不用时间戳）；fixed-rate 代价：异步事件需重采样/编码、丢失语义、违反 i.i.d./平稳假设（D3 Table 3）。**结论：Q9 的答案部分是 OPEN DESIGN QUESTION，但 D 组强烈暗示"事件为主干"对 UI 流更自然（D5 是最接近我们数据的成功案例）。** Moderate（方向性）+ Open（细节）。

### Q10. 是否应该"先 denoise 再 segment"？还是 denoising 与 segmentation 联合完成？

**答案：文献支持"去噪可先行、且应与分割解耦"，但不支持联合。** 论据：(1) D1 的去噪发生在 template 层、独立于任何 episode 边界；(2) D5 的 overhead 过滤在 task-identification 之前（先滤语义噪声再切任务）；(3) 无任何 D 组论文做"去噪与分割联合优化"。**操作建议（PROJECT TRANSFER INFERENCE）**：在 **derived 层**做排除而非物理删除——技术噪声标记 `noise_flag` / `excluded_from_segmentation`，Raw Observable Events 永久保留（append-only，§10）；语义白名单事件（低频但重要）不经过统计去噪；语义无关事件用规则旁路。**去噪先行是 D 组文献的自然顺序，联合是 OPEN DESIGN QUESTION；且去噪的产物必须是"标记"而非"删除"。** Moderate。

### Q11. online segmentation 当前能做到什么？需要多少 future context / latency？

**答案：UI 场景下 D5 是完整实证**：事件到达即处理（object 1–107ms、task-ident 2–4ms、task-categorize 40–150ms/任务），缓冲 250 事件，平均交互间隔 >2.5s 可实时跟上；可发现 unseen 任务类型（在线聚类）。**传感器场景**：D2 的 OCPD 需 k+2p 样本窗口（变点判定有窗口级延迟），识别需 2.56s 窗口。**通用概念**：D3 的 ε-real-time——完全在线=1-real（每个数据点前判定），完全离线=∞-real；"no algorithm operates in perfect real time"（必须检查新数据）。**答案：online 分割可做（D5），但"未来上下文"需求因方法而异：规则/共现法几乎无延迟（D5）、统计检验法需要窗口（D2）、贝叶斯法需要 run-length 历史（BCPD）。** Strong（D5 数字）；不同方法的延迟对比 Open。

### Q12. offline segmentation 相比 online 能增加什么？

**答案：全局信息带来的改善。** 具体：(1) **更好的任务类型指派**：D5 离线 categorization 相当于全量 warm-up，聚类模型更成熟（在线有 warm-up 效应：S_U1 在 250 事件前 R(ma) 仅 0.84，250 后 0.97）；(2) **全局共现统计**：D5 离线可多次扫描（Urabe 的全局共现计数是离线优势）；(3) **全局 profile 找边界**：D7 的 profile 方法（FLOSS/ClaSP）需要全局 profile 才能找边界（离线专用）。**代价**：需要存储完整事件流（D5 在线省内存 <1% 存全量）。**答案：offline 增加的是"利用全局/未来数据精化结果"的能力（证据 Strong）——但注意，这支持"离线结果比在线更成熟"，不等于文献展示了"在线输出后回头修改历史 boundary"（后者仍是 PROJECT ARCHITECTURE HYPOTHESIS，见 §16）。** Strong（离线优势）；refinement 操作 Open。

### Q13. boundary uncertainty 是否值得保留？

**答案：值得，且有理论依据（§17）。** D4 的逐点后验、D3 的 BCPD run-length 后验、D2 的检验 p 值都是现成的边界不确定性来源；对概率路线零成本（后验是分割的副产品）。规则类方法（D5/D6/D1）无内置 uncertainty，需自行设计（sim 余量、匹配歧义度）。**若后续认知推断（E 组）需要"这个边界有多确定"来传播不确定性，概率路线天然支持，规则路线需补充。** Strong（概率路线支持存在）；规则路线的置信度设计 Open。

### Q14. 规则系统与 probabilistic model 是否应当是竞争关系？还是互补？

**答案：互补（D 组强证据）。** 三个论据：(1) **行为类型决定方法**（任务文件 §25）：确定型行为（scroll burst、answer change）规则最优，模糊连续流（pointer 潜伏态）概率最优；(2) **D5 本身就是混合体**：关键词 chunking（规则）+ 共现矩阵（统计）+ DenStream 聚类（学习）——成功案例是"规则打底 + 统计/学习增强"；(3) **D6 的教训**：纯规则在 terminal 表达力不足时崩溃，需要用统计/语义增强。**竞争关系是被 D 组证伪的框架。** Strong。

### Q15. 对 pointer stream：最可辩护的 segmentation 路线有哪些？

**答案（§21 完整展开）**：(1) **速度/停顿阈值 + 语义目标（规则）**——最简、可审计、与 C 组四状态对齐；(2) **CPD/BCPD 在速度/位置序列上**——在线、带后验，处理减速歧义；(3) **HSMM 显式时长**——对 inactive 时长建模、离线。共同约束：必须先定义"减速 vs 边界"的消歧（§12）；不能把 pointer 段解释成 attention（C 组纪律）。**三种路线都有文献支撑，选哪种取决于我们需要的边界置信度与在线性。** Moderate（机制）+ Open（标定）。

### Q16. 对 scroll stream：最可辩护的 segmentation 路线有哪些？

**答案（§20 完整展开）**：(1) **规则聚合（时间间隔 + scrollend + 方向/速度）**——推荐主线，确定性、无标签、可审计；(2) **CPD 在 scroll velocity 序列上**——备选，需防"段落末尾减速"误报；(3) **HSMM 时长建模 scroll-active/inactive**——理论选项。**rule-based aggregation 对 SCROLL_BURST 足够且更合理**（D6 教训：scroll terminal 须保留时间/方向属性避免塌缩）。**Strong（规则路线对确定型行为）+ Moderate（备选路线）。**

### Q17. 哪些事件根本不应该 segmentation，而应该直接作为 atomic actions？

**答案（§19）**：`answer_option_clicked`（ANSWER_SELECT）、`question_navigated`（QUESTION_NAVIGATE）、`underline_created/removed`、`option_elimination_toggled`（true/false）、`text_selection_committed`、`visibility_changed`（作为中断标记保留）。**判据**：这些事件自带语义 + 时间戳 + 目标，边界 = 事件本身（D5 把单个 click/input 当不可分单元；D2 的识别不依赖其内部边界）。**对它们 segmentation 是多余推断。** Strong。

### Q18. 截至 D 组：从 Raw Event 到 Action Episode 的传统方法能力上限究竟在哪里？

**答案（D 组最终判断）**：
- **能可靠做到**：① 去噪（D1，事件级 P/R/F1 95.64%，仅限 RPA 动作日志 + 人工注入噪声；对自然阅读 UI 未验证）；② 规则化已知模式的 episode 分段（D5/D6 模板）；③ 在连续数值流上做在线/离线变点（D2/D3/D7）与显式时长状态分割（D4）；④ 端到端"事件→任务→类型→关联"的**任务级**抽象（D5，n.ED 0.04–0.17）；⑤ **online + offline both feasible** 的概念（D5 直接实证；"online provisional + offline retrospective refinement" 仅为项目架构假设，§16）。
- **不能可靠做到（传统方法上限）**：① **micro-action 级、混合事件流的边界检测**——D 组无任何 UI 实证；② **边界置信度的统一输出**——只有概率路线天然有；③ **边界质量本身的评估基准**——D 组无统一 benchmark，每篇评估对象不同；④ **"语义边界"的自动发现**——统计方法只给统计边界，语义映射必须人工定义。
- **核心上限**：**统计方法只能保证"分布/状态变化"，不能保证"语义 action 切换"**。任务文件 §33 的最终标准（条件化回答）在 D 组已达成：我们清楚知道哪类输入、什么粒度、什么边界定义、需要什么标签、能否在线、有无 uncertainty、如何评估、与 UI 流多相似。**上限不是"算法不够强"，而是"UI 场景的边界语义尚未被任何传统方法直接验证"——这正说明下一步必须自建 GT 与评估（§24/§25）。**

---

## 28. D 组确立了什么

> 对应任务文件 §27。分四级证据强度，并逐条判定 7 个关键命题。

### D 组正式结论（反馈整合，6 条）

**① Raw Event 不应该全部走同一条 segmentation pipeline。** 最重要的分类先是三分法（Atomic Semantic Events → 不分割；Continuous Low-Level Streams → segmentation；Composite Event Patterns → pattern abstraction），而不是"所有事件进入一个分割模型"。

**② 统计边界 ≠ 语义动作边界（D 组最扎实的结论之一）。** "distribution changed" ≠ "student changed action"；pointer speed 下降可能是 new episode，也可能只是 approaching click target。**CPD 只能提供 boundary candidate，不是边界本身。**

**③ 明确的 semantic events 根本不应该 segmentation。** `question_navigated`、`answer_option_clicked`、`underline_created`、`option_elimination_toggled` 直接 `Raw Semantic Event → Atomic Action`；这一层没有必要塞进 HMM/HSMM。

**④ 模糊连续流才真正需要 segmentation。** 主要是 pointer samples 与 scroll samples；候选路线包括 rules / CPD / HMM / HSMM。**但现有 D 文献没有直接告诉我们哪一个在英语阅读 UI 上最好**（需 GT + 比较实验，见 ⑥）。

**⑤ HSMM 最大价值是 duration，不是"模型更高级"。** 未来若发现 Pointer Transition 与 Pointer Inactive Episode 的持续时间分布明显非 geometric 且具有稳定差异，HSMM 才值得；否则 HMM / simpler rules 可能更稳。

**⑥ Action Segmentation 最大剩余缺口已经不是算法，而是 GT。** D2/D3/D4/D7 已提供足够算法（CPD/BCPD/HMM/HSMM/BD/SD），D5/D6 又给了 UI semantics/rules/grammar/task abstraction。真正缺的是：**真实英语阅读 UI + pointer/scroll/semantic events → 人工标定的 micro-action boundaries**。有了 GT 才能回答"Rule vs CPD vs HMM vs HSMM 谁在我们的数据上最好"。

### 强证据（Strong Evidence）

1. **统计变点 ≠ 语义 action 边界**（D3 Def. 7 + D7 CPD/BD 区分 + D2 机制）。
2. **boundary accuracy 与 activity/segment accuracy 必须分离报告**，且 D 组论文普遍只报告后者（D2 99.80% F-Measure 是识别指标且其评估协议描述不一致；D4 是点级误分类；D5 是编辑距离+聚类；D1 是噪声 P/R/F1）。
3. **去噪不应按频率判噪**（D1 摘要 + 其外部噪声实证）；但 D1 机制仍会误删低频真实行为，需语义白名单。
4. **显式时长建模的价值是条件性的**（D4 §5.1 vs §5.3）：数据符合 HSMC 假设时显著更好，否则无增益甚至略差。
5. **事件语义/上下文是任务级分割的关键信息**（D5 消融：control-flow only 0.42 编辑距离 vs full 0.04）。
6. **在线分割可达到且已实现于 UI 场景**（D5 双设置 + 明确延迟数字）。

### 中等强度证据（Moderate Evidence）

7. **"不同 action 类型适合不同 segmentation 方法"（机制分流）→ MODERATE evidence + high-confidence architectural synthesis**：这个判断高度合理、很可能就是最终 baseline 的正确方向（Atomic → 不分割；Scroll → rules；Pointer → rules/CPD/HSMM；Known pattern → grammar；Ambiguous latent → probabilistic），**但它不是 head-to-head empirical result**——D 组没有论文在 same UI dataset 上比较 Rules vs Grammar vs CPD vs HMM vs HSMM。它是对跨论文证据的综合（D5 消融 + D6 表达力 + D7 分类框架），**应作为"目前最可辩护的架构原则"进入最终系统，但证据来源必须说清楚**。
8. **HDP-HSMM 比 HDP-HMM 更适合真实（非马尔可夫）数据**（D7 机制论证）。
9. **BCPD 的 run-length 后验是边界置信度的现成模板**（D3）；D4 的逐点后验支持 uncertainty 保留（§17）。
10. **grammar 的表达力受 terminal 区分度/粒度一致性的限制**（D6 的 coverage/diversity 诊断）。
11. **"Online + Offline both feasible" 有实证（D5 双设置）**；但 **"online provisional + offline retrospective refinement" 只是 PROJECT ARCHITECTURE HYPOTHESIS**——D5 的 warm-up、E2USD 的延迟聚类、BCPD 的后验都属"推迟决断/可重估"，没有任何 D 组论文演示"修改已输出的历史 boundary"（§16）。
12. **评估指标应组合使用**（D7：F-Measure + 评分函数同时用；容忍窗口处理微小时差）。

### 弱证据（Weak Evidence）

13. **显式时长分布"最适合"我们的高变异 UI 行为**——只有机制推断（D4），无 UI 实证；需先确认时长结构。
14. **规则聚合对 SCROLL_BURST 足够**——基于 D5/D6 类比与语义确定性（PROJECT TRANSFER INFERENCE），无直接 scroll 文献。
15. **pointer episode 的 speed/pause 分段在 UI 上有效**——基于 D2/D4 传感器先例 + C 组状态语义（算法迁移，需标定）。

### 不支持 / 仍开放（Unsupported / Still Open）

16. **UI 交互流上的边界检测数值性能**——D 组零实证（唯一 UI 论文 D5 评估对象是任务级非 micro-action 边界）。
17. **混合事件流（连续+离散+异步）的最优表示**——D 组无比较。
18. **UI action 的 tolerance 标准**（§24 三个问题）。
19. **低频真实行为在统计去噪中的保护机制**——D1 没有，需要项目自建。
20. **unseen action 类型的自动发现质量**（D5 声明可发现 unseen 任务，但其评估中 unseen 场景未单独量化）。

### 逐命题证据判定（任务文件 §27 要求的 7 条）

| 命题 | 判定 | 证据 |
|---|---|---|
| `rare event = noise` | **Unsupported（且被 D1 摘要反驳）** | D1 摘要明言"现有方法把低频当噪声"是缺陷；其机制仍会误删低频真实行为 |
| `statistical change point = semantic action boundary` | **Unsupported** | D3 Def. 7 + D2 机制 + D7 区分（§12） |
| `fixed time-gap threshold 足够完成 segmentation` | **Unsupported（对全部行为）** | 对 scroll burst 是可用初版（D5 未用时间戳是缺口）；对 pointer/其他行为无证据；阈值需实证标定 |
| `HMM automatically discovers meaningful actions` | **Unsupported** | HMM 状态是 latent ID（D4），语义命名需人工；D7 亦无此声明 |
| `HSMM is always better than HMM` | **Unsupported（且被 D4 §5.1 证伪）** | 数据是 HMC 时 RHSMC 无增益甚至略差 |
| `grammar is only suitable for known patterns` | **Moderate（部分支持）** | D6 显示 grammar 无法处理 terminal 表达力外的模式；但对已知模式高效 |
| `all UI events should pass through one segmentation model` | **Unsupported（且被 D5/D6/D7 证据反对）** | 分 action 类型选择机制是 D 组结论 |

---

## 29. 需要 E 组提供的内容

> 对应任务文件 §28。Group E 固定定义为"Process Evidence → Cognitive Diagnosis + Construct Validity"。D 组完成后把以下问题交给 E。

1. **segmented action → 对应学生什么 cognitive process？** D 组只输出行为层 episode（SCROLL_BURST、POINTER_INACTIVE_EPISODE、ANSWER_CHANGE...）。这些 episode 是否/如何对应理解、回读、检索、决策等认知过程，是 E 组的 construct validity 问题。D 组明确不能自称"reading evidence"（任务文件 §3）。

2. **segmentation uncertainty → 如何传播到 cognitive inference？** 若我们保留边界置信度（§17），E 组需要定义"行为证据的置信度如何影响认知推断的可信度"。D 组只保证 uncertainty 可输出，不保证其认知意义。

3. **human-labeled action episode + stimulated recall + eye tracking 的 construct validation 设计**。D 组建议的 GT 流程（§25）产出行为边界 GT；E 组需要设计：让受试者回看分段并报告当时在做什么（stimulated recall）、用眼动交叉验证 pointer episode 的语义、检验"行为 episode → 认知状态"映射的效度。

4. **语义白名单的认知边界**。D 组建议保护低频语义事件（ANSWER_CHANGE 等）；E 组需要判定"哪些低频行为在诊断上有认知意义"，以回馈去噪层的白名单（§10）。

5. **行为 vocabulary 与认知理论的对齐**。D 组产出候选 vocabulary（§23）；E 组需要判断这些行为块是否映射到既有的阅读/学习理论构念（如 rereading、lookback、option elimination 与元认知的关系）。

6. **D 组不得越界的明确声明**：pointer episode ≠ attention、scroll burst ≠ rereading、TEXT_FOLLOWING_LIKE_EPISODE ≠ 正在阅读。这些推断边界由 E 组的 construct validation 负责（任务文件 §32-13/14/15 纪律）。

---

## 30. 证据索引

> 对应任务文件 §30。页码均为本地 PDF 逐页核对（PDF 页 = 文件内页；期刊页标注于括号）。禁止编造。

| # | 结论 | 论文 | PDF 页码 | 章节 / 公式 / 表格 |
|---|---|---|---|---|
| 1 | 现有方法把低频动作当噪声是缺陷；MMAD 识别高频外部噪声 | [D1] | p.1（2729） | 摘要 |
| 2 | 噪声 = 偏离预期模式的异常数据；内/外噪声定义 | [D1] | p.4（2732） | §2.1 |
| 3 | 模板相关性假设：相似动作 → 相同模板 | [D1] | p.6–7（2734–35） | §2.2 |
| 4 | Markov 转移概率矩阵 p(s'\|s,e)，∑p=1 | [D1] | p.9–10（2737–38） | §2.3.2 |
| 5 | 自适应阈值：截断正态分布，ξ=μ−3σ；KS 检验 | [D1] | p.9–10（2737–38） | §2.3.3 |
| 6 | 迭代噪声删除：临时移除→重算→确认/恢复 | [D1] | p.11（2739） | §2.4.2 |
| 7 | 变体被误判为噪声；RPA 只允许单一 trace 的辩解 | [D1] | p.17（2745） | §3.3 RQ3 |
| 8 | 去噪平均 P 94.31% / R 97.71% / F1 95.64%；比 baseline +3.3% F1 | [D1] | p.1（2729）+ p.15（2743） | 摘要 / RQ1 |
| 9 | 消融：无 Log Template → F1 −52.0%（贡献最大） | [D1] | p.17（2745） | Table 7 |
| 10 | Future Work：去噪后用于 task-level segmentation | [D1] | p.20（2748） | §5 结论 |
| 11 | OCPD = hypothesis-and-verification；Bartlett 方差齐性 + BH 校正 | [D2] | p.4–5（1179–80） | §III-A, Eq.1–8 |
| 12 | 变点后仍切 2.56s 固定窗口（50% 重叠） | [D2] | p.5（1180） | §III-A |
| 13 | 报告指标是识别指标：F-Measure 99.80% / accuracy 99.83% | [D2] | p.1（1176） | 摘要 |
| 14 | 三分割方案下 EL 识别 accuracy：94.89 / 95.58 / 96.22 | [D2] | p.7（1182） | Table I |
| 15 | 变点 ≈ 28Hz 目标（引用 Ni et al.） | [D2] | p.4（1179） | §III-A |
| 16 | CPD 定义 = 假设检验 H0/HA；变点 = 分布变化的 k* | [D3] | p.4（342） | §2.1 Def. 7 |
| 17 | ε-real-time：在线算法至少需 ε 个新样本；无完美实时 | [D3] | p.4（342） | §2.2.1 |
| 18 | 评估指标分类：变点 yes/no（分类指标）vs 变点时间差（MAE/MSE/MSD/RMSE） | [D3] | p.6–8（344–46） | §2.3 |
| 19 | BCPD run-length 后验 P(r_t\|x_1:t)（边界概率） | [D3] | p.14（352） | §3.2.3 |
| 20 | 在线/离线谱系：likelihood n+k-real、probabilistic n-real、MDL/Shapelet ∞-real | [D3] | p.19–20（357–58） | §4.1, Fig.5 |
| 21 | 多数无监督方法受平稳/i.i.d. 约束 | [D3] | p.22（360） | Table 3 |
| 22 | 参数/计算成本对比：CUSUM O(n²)、AR O(n³)、Bayesian O(n)、GP O(n²) | [D3] | p.20（358） | Table 2 |
| 23 | discrete-time HMM 隐含 geometric 停留时间 p_ok(m)=(λ_kk)^m(1−λ_kk)（D4 原文 "exponential form"）；HSMC 任意分布 | [D4] | p.3（31） | §3.1 |
| 24 | RHSMC 线性复杂度 O(N)（最小停留时间建模） | [D4] | p.4–5（32–33） | §3.3 |
| 25 | ICE 参数估计（无监督，无需标签） | [D4] | p.5（33） | §4.1 |
| 26 | MPM 逐点后验 p(x_n\|y)、p(v_n\|y) | [D4] | p.2（30）/ p.7（35） | §2 / §5 Eq.5.1–5.7 |
| 27 | 数据是 HMC 时 RHSMC 无增益、高噪声略差（t=18.38% vs 17.42%） | [D4] | p.9（37） | §5.1 |
| 28 | 数据非平稳 semi-Markov 时 NS-RHSMC 优于 NS-HMC（25% vs 30%；纹理 9% vs 18%） | [D4] | p.11（39） | §5.3 |
| 29 | 真实 SAR 无 GT；HSMC/NS-HMC 均优于 HMC，但两者差异可忽略 | [D4] | p.12–13（40–41） | §5.4 |
| 30 | 事件 = (uid,ts,P,V)；P=context、V=data | [D5] | p.3（3） | §3 |
| 31 | chunking：20 个 completion 关键词（IBM 指南） | [D5] | p.5（5） | §4.2.1 |
| 32 | endsTask 四检查：上下文不相关/无数据重叠/非 overhead/控制流非确定性 | [D5] | p.5–6（5–6） | §4.2.2 |
| 33 | 上下文相似度 sim 阈值 t 默认 0.3 | [D5] | p.5（5） | §4.2.2(1) |
| 34 | DenStream 在线聚类（无需 K）+ tf-idf 标签 | [D5] | p.6–7（6–7） | §4.3 |
| 35 | 评估：#tasks + normalized edit distance + Rand/Jaccard（无边界 F1） | [D5] | p.9（9） | §5.2.4 |
| 36 | Online 结果：n.ED 0.04/0.05/0.17；R(ma) 0.97/0.97/0.99 | [D5] | p.9–10（9–10） | Table 3 |
| 37 | 消融：control-flow only 0.42 vs full 0.04（语义+数据关键） | [D5] | p.11（11） | Table 5 |
| 38 | 延迟：object 1–107ms、task-ident 2–4ms、task-categorize 40–150ms；内存<1% | [D5] | p.12（12） | §5.3.7 |
| 39 | Future Work：未利用时间戳；顺序任务假设是限制 | [D5] | p.14（14） | §7.2/7.3 |
| 40 | regular grammar：Σ=terminal、N=non-terminal、f:N→{Σ∪N}* | [D6] | p.3–4（491–92） | §3.1 |
| 41 | 映射 code-book 人工建立（inter-rater 0.47→0.91→0.99） | [D6] | p.5–6（493–94） | §4.3 |
| 42 | coverage 46–100%；某数据集 95.43% 事件映射到同一 explore terminal | [D6] | p.7（495） | §5.1, Table 2 |
| 43 | Tableau 8 种 log 记录全映射到 filter（语义塌缩） | [D6] | p.10（498） | Fig. 5 |
| 44 | grammar 无法表达交互时序 | [D6] | p.10（498） | §6 |
| 45 | 跨数据集无通用模式（非-terminal 表达力低） | [D6] | p.9（497） | §5.2.2 |
| 46 | CPD / BD / SD 三分类定义 | [D7] | p.2（2658） | §1 |
| 47 | BD 指标：朴素 F1 不容忍微差；容忍窗口；评分函数（无二部匹配）；建议 F1+评分函数联用 | [D7] | p.4–5（2660–61） | §3.1.1 |
| 48 | SD 指标 ARI/NMI；SD 方法忽视边界指标（综述批评） | [D7] | p.5（2661） | §3.1.2 |
| 49 | Table 1：在线仅 E2USD、StreamScope 支持（在线稀缺） | [D7] | p.7（2663） | Table 1 |
| 50 | 大多数方法需指定 K/N/α（自适应阻碍） | [D7] | p.7–8（2663–64） | §4 |
| 51 | HDP-HMM 状态数膨胀 vs HDP-HSMM 更适合真实数据 | [D7] | p.9（2665） | §4.1.1 |
| 52 | E2USD 自适应阈值 + 延迟聚类（在线模板） | [D7] | p.11（2667） | §4.1.2 |
| 53 | D2 评估协议描述不一致（LOOCV / 70%–30% 受试者 split / 10-fold CV 混用），削弱其数值可靠性 | [D2] | p.7（1182） | §IV-A / §IV-C |

---

## 31. 严格禁止事项自查（任务文件 §32）

| # | 禁止事项 | 自查 |
|---|---|---|
| 1 | 引入 LLM / AI Agent | ✅ 全文只综述传统方法，无 LLM/Agent |
| 2 | 提前设计最终完整系统 | ✅ 只给文献支持性与候选路线（§16/§20/§21），不设计最终架构 |
| 3 | 把 denoising 等价 segmentation | ✅ §10 独立区分 |
| 4 | 把 change point 等价 cognitive boundary | ✅ §12/§28 |
| 5 | 把 statistical boundary 自动等价 semantic action boundary | ✅ §12（明确否定） |
| 6 | 把 downstream classification accuracy 当 boundary accuracy | ✅ §15（D2 案例）|
| 7 | 把 activity label accuracy 当 segmentation accuracy | ✅ §15/§24 分层报告 |
| 8 | 把 rare event 自动当 noise | ✅ §10（语义白名单）|
| 9 | 把 fixed time threshold 当 universal truth | ✅ §20（标注为 OPEN/需标定）|
| 10 | 因为 HSMM 更复杂就默认比 HMM 更好 | ✅ §13/§28（条件性结论）|
| 11 | 因为 unsupervised 就认为不需要人工定义 | ✅ §7.17/§26（D5/D6 人工关键词与 code-book 被明确列出）|
| 12 | 把 latent state 自动命名成 reading cognition | ✅ §7.13（D4 latent ID 需人工语义映射）|
| 13 | 把 pointer episode 自动解释成 attention | ✅ §21（明确纪律，E 组负责）|
| 14 | 把 scroll burst 自动解释成 rereading | ✅ §20（行为层定义）|
| 15 | 把 task-level event 与 micro-action 混成相同粒度 | ✅ §14（粒度差异明确）|
| 16 | 用 sensor/HAR 结果直接宣称 UI 场景相同性能 | ✅ §1 EF-9（D2/D4/D7 数值仅作机制参照）|
| 17 | 忽略 online latency | ✅ §16/§27 Q11（ε-real-time、窗口延迟）|
| 18 | 忽略 boundary uncertainty | ✅ §17 专项 |
| 19 | 忽略不同事件类型适合不同分割方法 | ✅ §26/§28 |
| 20 | 修改 D1–D7 编号 | ✅ §0 未重排 |
| 21 | 编造 PDF 未报告的 threshold/F1/latency/页码 | ✅ 全部数值与页码来自 §30 索引（逐页核对）|
| 22 | 用一般知识补论文未证明的结论而不标注 | ✅ 非原文内容一律标注 PROJECT TRANSFER INFERENCE 或 OPEN DESIGN QUESTION |

---

*报告完成。D 组 7 篇论文全文（121 页）逐页精读；所有关键数值与页码经 §30 证据索引核对。*
