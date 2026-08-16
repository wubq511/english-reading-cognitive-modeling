# METHOD-038 全文证据提取笔记

## 头部

- **Source ID**: `METHOD-038`
- **本地路径**: `sources/library/papers/methods/2002_Kobayashi_MethodEffectsTextFormat.pdf`（28 PDF 页；物理页 = 打印页 − 192，页 1 = 打印 193）
- **完整书目**: Kobayashi, M. (2002). Method effects on reading comprehension test performance: Text organization and response format. *Language Testing*, 19(2), 193–220. DOI: `10.1191/0265532202lt227oa`
- **catalog 核对**: `sources/catalog.yaml` 条目（authors/year/venue/DOI）与 PDF 首页一致，无出入。
- **审计角色**: Class 2/4 L2 阅读测验格式效应。审计文件 `reports/research/ui-instrument-effects-evidence-audit.md` 中本条目仅出现在 E3 检索记录（p.91，排队说明），无既有 UIE 条目引用；本笔记为首次全文提取。

## 研究概览

- **研究问题**: text organization（Meyer 修辞结构，四类：association / description / causation / problem–solution）与 response format（cloze / open-ended questions / summary writing）是否系统影响 L2 阅读测验成绩；第三个变量是学习者英语熟练度（PDF p.6，Section II）。
- **设计**: 随机分配（intact classes 内随机分 12 组），**between-subjects**，无过程指标、纯产品分数；12 组 = 3 格式 × 4 文本类型，每组取同一格式同一文本类型的两篇文本（不同 topic），顺序 counterbalance（PDF p.10，Table 1；设计理由 PDF p.9）。
- **样本**: 754 名日本大学生（多数 18–19 岁、大一/大二、中学 6 年英语，熟练度 lower-intermediate ~ intermediate）（PDF p.6）；前测 50 题语法词汇 MC 熟练度测试（x̄=29.7/50, s.d.=8.07, α=.82, 组间 F=.39 (11,723) n.s.），据此分 Low/Middle/High 三组（PDF p.7）。
- **任务与材料**: 8 篇专写文本（2 主题 × 4 文本类型，平均 369.3 词，Flesch 64.4）；cloze 25 题（每 13 词删一）、open-ended 5 题、summary 10 个关键点；**open-ended 与 summary 用日语（学生 L1）作答**，以排除英语产出能力对阅读测量的污染（PDF pp.7–8）。admin 时间 50 分钟（熟练度 25 + 阅读 25，PDF p.9）。
- **变量**:
  - 产品分数: 三种格式的阅读测验百分制分数（PDF p.26，Appendix 2）；
  - 信度指标: 各格式 α、Spearman-Brown 等题数校正 α、评分者信度（PDF p.10）；
  - 构念指标: 各格式×文本类型与熟练度测试的 Pearson 相关（PDF p.15，Table 4）；
  - 缺失指标: **无**。全文无 missingness/未作答/放弃作答的报告（grep 无命中）。
- **评分**: cloze 按语义/句法可接受评分；15% 试卷双评/三评，open-ended r=.92（双评），summary r=.85–.90（三评）（PDF p.10）。

## 核心发现（按四类主张分组）

### Class 1 — 可用性/偏好

**无直接证据。** 纸笔测验，未测满意度/偏好/易用性。作者对格式选择的规范性告诫（"language testers ought not to choose formats of comprehension tests simply because the formats are familiar or convenient"）是观点声明而非可用性数据（PDF p.19）。对 Class 1 无贡献。

### Class 2 — 行为改变

**无直接证据。** 全部为纸笔产品分数，无行为日志、时间或交互过程指标；本研究的"response format"操纵是响应性质（Bachman method facet 4），text organization 是内容层面的输入结构（facet 3），两者均非 UI/布局/导航层面的操纵。对 Class 2 无直接贡献；其格式效应方向随文本条件翻转（见 Class 4）可作为"仪器效应是任务/材料条件依赖的"跨证据呼应，但不构成行为改变证据。

### Class 3 — 仪器信度与缺失

- **反应格式移动产品分数信度（可被题数解释）**: cloze α=.86~.90（各文本类型），open-ended 与 summary α=.69~.79；经 Spearman-Brown 校正到等题数（50 题）后，open-ended α=.91~.96、summary α=.85~.90，"open-ended questions and summary writing could be as reliable as cloze tests"（PDF p.10）。结论：格式间 α 差异主要源于题数/长度差异，作者自己将其归因于题数而非格式固有属性——用"格式降低信度"作为主张是 `OVERSTATED`，用"等长条件下信度可比"才是 `SUPPORTED`。
- **主观评分格式的测量误差成分**: open-ended 双评 r=.92、summary 三评 r=.85~.90（PDF p.10）。评分者误差是格式测量误差来源之一（与作答 UI 无关，但对"格式→测量误差"链路有参考）。
- **缺失: 无数据。** 未报告未作答率、放弃或任何数据完整性指标；无法对缺失维度作任何判定（`UNRESOLVED` 于此维度）。

### Class 4 — 学习/构念与 estimand（本论文核心贡献）

- **格式与文本结构都移动 L2 阅读产品分数，且二者交互**:
  - 文本结构主效应: cloze F(3,251)=4.819**, open-ended F(2,223)=6.401**, summary F(3,249)=5.247**, overall F(3,731)=4.846**（p<.005；PDF p.12, Table 2）；
  - 格式主效应: overall F(2,732)=10.395**；按文本类型分: association F(2,185)=8.644**, description F(2,179)=11.158**, causation F(2,178)=2.549 **n.s.**, problem–solution F(2,181)=7.987**（PDF p.12, Table 3）；
  - **交互显著**: F(11,723)=6.149, p<.005 —— 格式效应不是均匀的，随文本结构类型变化（PDF p.12）；
  - 作者推论: "a test score might be partly an artefact of test format"（PDF p.5），拒绝假设 1（PDF p.13）。
- **格式移动分数分布的次序，且方向相反**: cloze 在松散文本 association 最高（x̄=42.3）、在紧密 problem–solution 最低（x̄=31.8）；open-ended 与 summary 相反，association 最低（33.4 / 30.9），紧密文本更高（description 49.1 / causation 41.8）（PDF p.26 Appendix 2；图见 PDF pp.10–11, Figure 2）。即**反应格式改变了 text-organization 效应的方向本身**，不只是幅度。
- **格式效应是条件依赖的（阴性结果）**: causation 文本下格式效应不显著（F(2,178)=2.549, n.s.）——与 `B7` 的 task-contingent 格式效应（ordering vs categorization 方向翻转）形成跨领域呼应（PDF p.12）。
- **熟练度×格式×文本结构三向交互（对 L2 人群适用性的关键）**:
  - 格式效应集中在高熟练度组: response-format 主效应 Low 组总检验 n.s.、Middle F(2,235)=8.57*、High F(2,255)=14.28**；problem–solution 文本下 High F(2,71)=16.68**（PDF pp.16–17, Tables 6–7）；
  - 文本结构效应同样集中在高组: summary 中 text-type 效应 Low n.s.、Middle F(3,77)=3.89*、High F(3,86)=8.64**（PDF p.16, Table 5）；
  - 作者表述: "learners with higher English language ability are more susceptible to different test formats"（PDF p.17）；低熟练度学生"could not exploit text structure when summarizing"（PDF pp.14–15）；
  - 含义: 在 L2 阅读人群中，仪器效应按熟练度分层——高熟练度受试的分数更易被格式/材料组织移动（PDF pp.13–15, Figures 3–5; PDF pp.16–17, Tables 5–7）。
- **格式×文本组合改变"测到了什么"（构念效度证据）**: 与熟练度测试（外部语言能力标准）的相关在松散文本下显著下降: open-ended association r=.54 → problem–solution r=.81；summary r=.49 → .75；cloze 相对稳定（.66→.79）（均 p<.001；PDF p.15, Table 4）。作者: 结构化文本下 open-ended/summary 成绩"more accurately reflect learners' language proficiency"（PDF p.15）。
- **作者综合结论**: "different test formats seem to measure different aspects of reading comprehension"，且"different types of items within the same format"也如此（PDF p.19）——格式选择是构念定义的一部分，不是中性通道。

## 边界与局限

- **人群/任务边界**:
  - 日本大学生 EFL 群体，熟练度仅覆盖 lower-intermediate ~ intermediate；作者明确提示需向更高熟练度/母语者复制（PDF p.19）；
  - L2 阅读，且 open-ended/summary 用日语 L1 作答——作者有意隔离英语产出通道；与"英语作答 UI"场景无直接可比；
  - 纸笔测验、无 UI/无过程数据、**明确排除 multiple-choice 格式**（理由: 可猜测、效度存疑，PDF p.5）——本论文不覆盖审计 baseline 的 MC 作答 UI；
  - 25 分钟速度压力存在（PDF p.9），但无未完成/未作答报告。
- **作者自述局限**: 四类 Meyer 修辞结构"by no means exhaustive or perfect"；自然文本常为混合类型、类型识别困难，实用上只能区分"有无结构"（PDF pp.19–20）。
- **内部不一致（保留，未解决）**:
  - Table 2 open-ended 的 df=2（若 4 类文本结构 one-way ANOVA 应为 df=3，且 df 加和 223+2=225 < N=227）——可能是打印错误或作者合并类别，原文未解释（PDF p.12）；
  - Table 1 各组 n 合计 735 ≠ 正文 754"participants"（差 19，作者未解释排除原因）（PDF pp.6, 10）。
- **不可外推处**: 本研究的格式对比是**响应性质**层面的（cloze/简答/摘要，均纸笔呈现），不是 UI 变体（布局/导航/交互）层面的对比；任何"格式→分数分布移动"结论转移到我们的作答 UI 属于 `PROJECT-INFERENCE`，且 MC 被作者明确排除。

## 对审计的用途

- **支持/限定既有 UIE 条目**:
  - **扩展 `UIE-02`（B7: 格式移动产品分数）**: Kobayashi 在 L2 阅读测验（最近领域）独立证明 response format 移动产品分数分布，且与输入结构交互（F(11,723)=6.149**，PDF p.12）——"格式移动 estimand"不再只靠 ELA 排序/分类任务单点证据；
  - **限定 `UIE-19`（B5/B6: 同一行为对不同能力者意义不同）**: 本研究显示仪器效应本身按熟练度分层（High 组格式效应 F=14.28** vs Low n.s.）——对 baseline 的推论（`PROJECT-INFERENCE`）: UI 变体对高熟练度受试的分数影响可能大于低熟练度；
  - **补充 `UIE-26`（METHOD-011 模式效应综述）**: Kobayashi 是**同一投递模式（纸笔）内**的格式×材料效应，证明"移动 estimand"的不只是纸/屏投递模式，还有响应格式本身；
  - **扩展 Class 3**: 现有 Class 3 覆盖缺失率（UIE-11/12/27）与过程通道丢失（UIE-13/14）；本研究增加"产品分数信度随格式变化"的维度（但需按题数校正，见 UIE-33 草稿）。
- **不能直接使用的部分**: 无过程数据 → 对 Class 2 零贡献；无缺失数据 → 对缺失维度零贡献；MC 被排除 → 不能直接约束我们的 MC 作答 UI。
- **建议新 UIE 条目（4 条）**:

1. **UIE-31（Class 4）** — *claim*: 在 L2 阅读测验中，response format 移动产品分数分布且与文本组织交互，效应方向随文本类型翻转: cloze 在松散文本最优（association x̄=42.3）、open-ended/summary 在松散文本最差（association x̄=33.4/30.9）而紧密文本更优；格式主效应 overall F(2,732)=10.395**，text-type × format 交互 F(11,723)=6.149, p<.005。*pages*: PDF pp.10–11（Figure 2）、12（Tables 2–3 与交互）、26（Appendix 2）。*verdict*: `SUPPORTED`（within study）；跨到作答 UI 为 `PROJECT-INFERENCE`。*scope*: 日本大学生、L2 阅读、cloze/open-ended/summary 纸笔格式、非 MC、非 UI 实现层面；格式效应在 causation 文本下不显著（n.s.）——效应是材料条件依赖的，呼应 `B7` 的 task-contingent。
2. **UIE-32（Class 4）** — *claim*: 格式与文本结构效应在 L2 阅读人群中按熟练度分层: 高熟练度组受格式影响显著（total F(2,255)=14.28**；problem–solution 下 F(2,71)=16.68**）而低组 n.s.；text-structure 效应同样仅高组显著（summary High F(3,86)=8.64** vs Low n.s.）——仪器效应不是人群均匀的。*pages*: PDF pp.16–17（Tables 5–7）、17（"more susceptible to different test formats"）、14–15。*verdict*: `SUPPORTED`（within study）。*scope*: 同 UIE-31；熟练度范围 lower-intermediate ~ intermediate，"高熟练度更敏感"的外推边界明确。
3. **UIE-33（Class 3）** — *claim*: 反应格式移动产品分数信度（cloze α=.86~.90 vs open-ended/summary α=.69~.79），但 Spearman-Brown 校正到等题数后可比（open-ended α=.91~.96, summary α=.85~.90），作者将差异归因于题数而非格式。*pages*: PDF p.10。*verdict*: `SUPPORTED`（α 差异存在）；"格式固有地降低信度"为 `OVERSTATED`（作者自己排除该归因）。*scope*: 同一样本；提示格式间信度比较必须先控制题数/长度。
4. **UIE-34（Class 4，构念）** — *claim*: 格式×文本组织组合改变与外部语言能力标准的对应关系: 松散文本下 open-ended/summary 与熟练度测试相关显著下降（association r=.54/.49 vs problem–solution r=.81/.75；cloze 稳定 .66–.79）——同一格式测到的构念内容随材料组织漂移。*pages*: PDF p.15（Table 4）、15（"more accurately reflect"）、19（"measure different aspects"）。*verdict*: `SUPPORTED`（correlational）。*scope*: 同一 L2 阅读测量框架；相关差异为描述性统计，未做差异显著性检验（作者未报告 Fisher z 等检验）。

## 验证说明

- 全文 28 PDF 页经 `pdftotext -layout` 通读，非 `ABSTRACT-ONLY`；所有页码为 PDF 物理页。
- 统计量均直接抄录自论文 Tables 2–7 与正文；Table 2 open-ended df 与 Table 1/正文 N 合计的内部不一致已在上文标注。
