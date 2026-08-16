# METHOD-024 证据提取笔记：PISA 2009 Results: Students On Line（Vol. VI）——导航章节

## 结论速览（中文）

- **核心结论**：本卷是 PISA 2009 数字阅读评估的官方整卷报告，第 3 章（Navigation in the PISA 2009 digital reading assessment）为 B-tier 导航证据（B3/B5/B6）的原始出处与测量底稿。它提供三类硬证据：(1) 页级导航过程指标（页访问数、相关页访问次数、相关页数）与数字阅读成绩强相关且在控制印刷阅读后仍有大额增量（平均 ΔR²=23%，f²=0.83，1 SD 相关页数 ≈ +66 分）；(2) 缺失与数据质量是仪器依赖的：整卷自述“页访问数据因技术问题未能完全准确采集”，日本/丹麦整校技术故障导致数字阅读学生响应率仅 56%/69%，且“对未参与数字阅读评估的学校/学生不做无响应调整”，改用 plausible values 补缺；(3) 导航行为随任务要求而变（无需导航的任务 83.5% 学生留在起始页；复杂任务满分者平均 8.2 页、最高 125 次访问），访问量-成绩呈负二次（倒 U）关系，回访（revisit）的意义因任务而异。
- **怎么得出的**：用 `pdftotext -layout` 通读第 3 章全文（PDF 物理页 91–123），并补读执行摘要（p.22）、第 2 章框架（pp.44–46）、Annex A1b 导航指数构造（pp.230–231）、Annex A2 抽样与响应率（pp.247–248）。页码均为 PDF 物理页（= 印刷页 + 2）。
- **未决项**：本卷不报告聚合的“从未导航者比例”（B2/UIE-11 的 66.3% 是 PISA 2018，不在此卷）；log 文件缺记率的总体量未披露；所有导航-成绩关系是相关/回归证据，作者明确声明不可作因果解读。

## 头部信息

- **Source ID**: `METHOD-024`
- **本地路径**: `sources/library/papers/methods/2011_OECD_StudentsOnLine.pdf`（SHA-256 `32d755023a2775334b4b989693268436229edbab0ab1e1c8a0b39154339770cc`，与 catalog 一致）
- **完整书目**: OECD (2011), *PISA 2009 Results: Students on Line: Digital Technologies and Performance (Volume VI)*, OECD Publishing, Paris. DOI: 10.1787/9789264112995-en; ISBN 978-92-64-11299-5 (PDF); © OECD 2011。与 `sources/catalog.yaml` 的 METHOD-024 条目逐项一致，无出入。
- **PDF 首页核对**: 与 catalog 一致（title/authors/year/venue/DOI）。本章（第 3 章）贡献作者含 Johannes Naumann 与 Jean-François Rouet（卷首 Foreword 致谢名单，PDF p.5）——印证其作为 B3/B5/B6（Naumann 系列）原始出处的位置。

## 研究概览

- **研究问题**：PISA 2009 数字阅读评估（世界首个大型国际数字阅读机考）中，学生的导航行为与数字/印刷阅读成绩是什么关系？学生在个别任务中的导航行为呈现什么模式？（本卷第 3 章聚焦；整卷还覆盖成绩分布、背景、ICT 熟悉度等）
- **样本**：19 个国家/经济体（16 个 OECD 国 + 哥伦比亚、中国香港、中国澳门）约 50,000 名学生参加数字阅读评估（PDF p.28, p.31）。数字阅读样本是从纸笔 PISA 样本中再抽样（目标每国 1200 名已评估学生；Target Cluster Size 14 人/校），所有数字阅读参与者必须先参加纸笔评估（PDF p.247）。案例研究在整样本层面（log 数据可得者）分析，不按国家拆（国家层组太小，PDF p.105）。
- **设计**：观察性大规模国际测评（相关/回归分析），非随机实验。回归模型：数字阅读成绩 (WLE) ~ 印刷阅读 (WLE) + 导航指标，含二次项变体（PDF pp.100–102）。
- **任务与材料**：9 个单元（unit）、3 个 cluster，每生 2 个 cluster、两种顺序之一 → 共 6 种测试版本（PDF p.230）。所有任务刻意要求导航才能得满分（PDF p.93）；每单元页面按 necessary / relevant / irrelevant 三类预分类（PDF p.93）。第 3 章案例研究选 3 个单元（IWANTTOHELP、SMELL、JOB SEARCH）的 6 个任务（PDF pp.103–106）。
- **变量**：
  - 产品分数：数字阅读与印刷阅读 WLE 成绩（导航指标未进入 PV 背景模型，故用 WLE 而非 PV 做回归——PDF p.94 脚注）。
  - 过程指标（log 文件构建）：PAGES（页访问数）、REL_PAGES（相关页访问次数）、UNI_REL_PAGES（相关页数），另有每页停留时间、所用导航设备（菜单/文内链接）；log 含“访问了哪些页、什么顺序、用什么设备、每次停留多久”（PDF p.230）。
  - 缺失指标：数字阅读学生/学校响应率（表 A2.5/A2.6，PDF pp.247–248）；逐题未作答率（案例研究表格，如 IWANTTOHELP Q4 约 40% 未作答，PDF p.110）。

## 核心发现（按四类主张分组）

### Class 1 — 可用性/偏好

- 本卷**无任何可用性/满意度/偏好测量**。仅有的相关点是仪器设计动机表述：测试开发者主动限制每任务可用页数并给予显式导航指引，理由是“没有价值去包含大量学生因找不到必要页面而迷失、困惑、沮丧（disoriented, confused and frustrated）的任务”（PDF p.106）。这是设计理性陈述，不是实测数据。
  - 判定：`UNRESOLVED`（本卷不提供 Class 1 实证）。
- 相关背景否定性发现：执行摘要明确反驳“数字原生代自动会操作数字环境”的说法——“significant numbers of students still cannot locate crucial pages”即便指引显式（PDF p.22）；第 3 章结论重申（PDF p.122）。与偏好无关，但提示“数字原住民即熟悉导航”不应作为 UI 默认假设。

### Class 2 — 行为改变（导航行为随任务/仪器设计而变）

- **导航需求是任务设计变量，并移动行为分布**：任务被“刻意构建为必须导航才能得满分”（PDF p.93）；部分任务提供“最有效路径”指引，但即便如此学生仍在三个导航指标上差异巨大——“It is thus a significant finding that students differ to a large degree in the number of relevant pages visited… even in tasks where guidance was provided”（PDF p.98）。同一仪器的行为空间由测试设计决定（可访问页数 63/73/76 随测试版本而变，PDF p.98）。
- **任务要求决定行为模式（任务 × 行为交互）**：
  - 无需导航的任务（IWANTTOHELP Q1）：83.5% 学生没有离开起始页；70.8% 学生在起始页上直接得满分（PDF p.107）。男生（19.3%）比女生（13.7%）更可能访问额外页面（PDF p.107）。较好读者倾向不为不必要导航（PDF p.108）。
  - 复杂导航任务（IWANTTOHELP Q4）：满分学生平均访问 8.2 页；全体有响应者平均约 13 次访问；最大 125 次；满分时间跨度 46–1511 秒（PDF p.111, p.113）。成绩好者访问更多相关页、更少无关页（满分组平均 0.8 个无关页 vs 无分者 3.7 个，PDF p.111–112）。
  - 搜索式任务（SMELL Q1）：访问目标页 P02 者（评分 552）显著优于未访问者（456）；在评分档内“访问必要页”者能力始终更高（PDF p.116）。
  - 页面往返任务（JOB SEARCH Q2）：42.7% 走指令给出的直线路径，但满分者中更高能力者反而多次往返（P03 与 P13 之间切换；女生最优组访问 4 次，2.5% 女生，均值 598；男生 ≥4 次 6.8%，均值 580–588）（PDF p.120）。
- **访问量-成绩呈非单调（倒 U）关系**：对“相关页访问次数”和“页访问数”，二次项系数每国均为负；OECD 平均：比均值少 20 次相关页访问 → 预测分数 −64.6 分；比均值多 20 次 → 仅 +30.5 分；中等效应量（PDF pp.102–103, Figure VI.3.8）。唯一例外是“相关页数”（UNI_REL_PAGES），与成绩呈线性（PDF p.103）。负二次项与本卷案例中的“无向漫游”（undirected navigation）及“back-and-forth = 迷失”的文献判断一致（PDF p.102，引 Richter et al. 2005; Savayene et al. 1996）。
- **回访（revisit）的意义是任务依赖的，不是固定信号**：“while revisiting pages is often regarded a sign of disorientation… there are examples where revisits are fruitful. This also means that **task demands must be taken into account when analysing revisits as an indicator of navigation across different tasks**”（PDF p.120）。JOB SEARCH 回访有益（信息量超单次记忆容量），SMELL Q1 额外回访与低能力相关（PDF p.117）。
- **组间行为分布差异（同一仪器内）**：无条件时女生导航“更好”（相关页数显著占优：14 个 OECD 国显著）；控制印刷阅读后多个国家转而为男生占优（如智利、西班牙、波兰、中国澳门、哥伦比亚；相关页访问次数上另加法国、韩国）（PDF pp.103–104）。即同一行为指标的人群基线受能力结构影响，跨组直接比较导航量需谨慎。
- 判定：`SUPPORTED`（任务要求移动导航行为与行为-成绩关系；相关/回归证据，非操纵实验）。

### Class 3 — 仪器信度与缺失

- **log 数据完整性本身被技术问题损伤**：第 3 章 Note 1 明示——“As a result of a technical problem, data for page visits could not be collected with complete accuracy in all cases. This means that there are some minor inaccuracies in some of the figures provided for the numbers of page visits, or number of visits to relevant pages… for the same reason, the figures are not always exactly aligned between the aggregated data and the case-study data”（PDF p.123）。即：聚合统计与案例研究数字之间因 log 缺失而不完全对齐。
- **投递/技术故障造成大规模单元缺失**：表 A2.5 学生响应率从 56%（日本）到 99%（中国澳门）不等；日本（56%）与丹麦（69%）显著偏低，脚注明确“lower response rates because of whole schools that were unable to participate because of technical difficulties”（PDF p.247，脚注同 p.248 表 A2.6 学校响应率）。即约四成（日本）至三成（丹麦）学生因技术故障未参加数字阅读评估。
- **缺失处理策略是“不做无响应调整 + PV 补缺”**：“No non-response adjustments were made for schools or students sampled for the digital reading assessment which did not participate… Plausible values were generated for these students”（PDF p.247）。数字阅读缺失被当作“domain not assigned”（如数学/科学领域未分配到题本）处理；导航指标本身只对“确实参加者”计算。
- **导航指标是测试版本依赖的，必须按版本居中/标准化才能跨版本比较**：6 种测试（3 cluster × 2 顺序）→ 指数按测试均值居中（“centred on the respective index's mean for the tests that were administered”，以去除 test composition 与 cluster order 效应），再按国家均值居中；稳健性分析另做每测试标准化（mean=0, SD=1），结果一致（PDF pp.230–231）。→ 仪器版本（题本组合/顺序）会移动导航指标均值，官方处理是统计校正而非假设版本不变性。
- **选择 WLE 而非 PV 的原因是导航指标未进 PV 背景模型**：即“哪些变量进背景模型”直接决定下游估计量可选集合（PDF p.94 脚注）。
- **任务级未作答与“未导航”缺测**：IWANTTOHELP Q4 约 40% 未作答（PDF p.110）；IWANTTOHELP Q2 约 20% 未访问关键页、3.9% 未访问而得满分（疑似猜答）（PDF p.109）；SMELL Q1 18.6% 未访问目标页即作答（猜答），其中 <5% 猜对（PDF p.116）；JOB SEARCH Q2 11.2% 未访问招聘页（PDF p.120）。案例研究所有人数统计基于“有 log 数据的学生”（PDF p.105）；IWANTTOHELP Q4 有 22,036 名学生的数据（PDF p.113）。
- **偏态处理**：三个导航指标分布偏态“中等”，未做对数变换；回归残差正态（PDF p.123 Note 2）。相关页数左偏（均值<中位）、页访问数右偏（均值>中位）（PDF p.95）。
- 判定：`SUPPORTED`（上述均为官方报告的操作性事实）。

### Class 4 — 学习/构念与 estimand

- **导航是数字阅读构念的组成部分，非印刷阅读的副产物**：本卷显式检验了“导航好只是印刷阅读好的副产品”这一竞争模型（若真，控制印刷阅读后导航应无增量预测力），结果拒绝之：相关页数在控制印刷阅读后平均增量 ΔR²=23%（16% 韩国 – 31% 法国），f²=0.38–1.32（均值 0.83，按 Cohen 为大）；回归系数平均 6.40 分/相关页（5.22–6.93）（PDF p.100）。对照：相关页访问次数 ΔR² 平均 11%；页访问数 ΔR² 平均 5%（印刷阅读反而 ΔR² 平均 34%）（PDF pp.101–102）。
- **相关强度（同源指标，页级）**：导航 × 数字阅读 r 平均 0.81（相关页数）/ 0.62（相关页访问次数）/ 0.42（页访问数）；× 印刷阅读分别为 0.62 / 0.48 / 0.33（PDF pp.99–100）。国家层：平均相关页数 × 平均数字阅读成绩 r=0.98（Pearson 与秩相关一致，PDF p.96）。标准化指标下 1 SD 相关页数 ≈ +66 数字阅读分（相关页访问次数 +40；页访问数 +24，均控制印刷阅读后）（PDF p.231）。
- **同一导航行为在不同任务/能力层含义不同**：回访意义因任务翻转（见 Class 2）；“未导航”在无需导航任务中是优等策略（IWANTTOHELP Q1 最优组留在起始页），在需要导航任务中是失败信号；单次点击无关页（无后续）与低能力相关（PDF p.108, p.122）。
- **数字 vs 印刷阅读成绩差随任务/作答状态变化**：JOB SEARCH Q2 满分者数字−印刷 = +17 分（570 vs 553）；无分者约 −20 分；未作答者 −40 分（363 vs 409）（PDF p.119）。→ 同一产品的数字/印刷分差本身就是任务与作答状态的函数，单一“模式效应”数字不成立。
- **产品分数不能保证预期过程发生**：多处显示“不访问关键页也可得满分”（猜答证据：IWANTTOHELP Q2 3.9%、SMELL Q1 <5%、JOB SEARCH Q2 0.7% 共 150 人，且其能力显著更低）（PDF p.109, p.116, p.121）。即产品分数与过程证据可解耦——正是项目 RQ0 关心的“产品分 vs 过程轨迹”分离。
- **作者明确声明不可作因果解读**：“Although the data provided here cannot ascribe causality, the statistical dependency of digital reading performance on navigation appears not to be a mere by-product of students' print reading proficiency”（PDF p.104）。结论章同样限定于相关证据（PDF p.122）。
- 判定：`SUPPORTED`（相关性/增量预测证据，非因果）；任何把“导航→成绩”写成因果的表述为 `OVERSTATED`。

## 边界与局限

- **人群**：15 岁学生，19 个国家/经济体（16 OECD）；非一般成人或低龄阅读者；纸笔与数字都参加的样本。
- **任务/工具边界**：数字阅读 UI 为 PISA 2009 专用测试环境——页式超文本（tabs、菜单、文内链接、下拉菜单、站点地图、滚动条），页面数被刻意限制（每任务最多 31 页，多数 8–31 页）；作者自述“necessarily presents extremely constrained options for navigation – far less than the almost infinite range of navigation possibilities readers face when they use the Internet”（PDF p.122）。这与项目 baseline 的单篇滚动式双栏 UI 属不同导航范式，**页级访问 ≠ 段落/区域可见性**——该映射仍为 `PROJECT-INFERENCE`。
- **测量边界**：导航指标全部是页级 log 计数；无注视、无段落级可见性；log 完整性有已知技术缺陷（PDF p.123）；案例研究为整样本非加权、无国家层推断（PDF p.105）；6 测试版本效应靠居中校正（PDF p.230）。
- **作者自述局限/保留**：不可因果（PDF p.104）；小样本子组需谨慎（“The numbers making multiple visits to P02 were small, so caution is needed”，PDF p.117）；偏态未对数化（PDF p.123 Note 2）；f² 韩国离群受总解释率影响（PDF p.123 Note 3）。
- **本卷不提供**：任何 UI 变体操纵实验；可用性/偏好数据；log 缺失率的总体量；聚合“从未导航”比例。

## 对审计的用途

### 支持/限定既有 UIE 条目（在 `reports/research/ui-instrument-effects-evidence-audit.md` 中以 B3/B5/B6 为锚）

- **UIE-04（B3，任务访问需求移动导航量及导航-成绩关系）**：本卷是 B3 的测量底稿与主要证据来源，提供初级支持——任务要求移动导航行为（Class 2）与导航增量预测（ΔR²=23%、f²=0.83）均可在原始出处钉到（PDF pp.98–101）。但 UIE-04 引用的具体回归系数（b=3.16/0.35/0.51/0.19/0.16，PDF 页码来自 B3 论文本身）在本卷中不存在——它们是 Naumann 的再分析，本卷只提供指标构造与总体关系；B3 的 17 国/29,395 人是其分析子集（本卷为 19 国/~50,000 人）。→ 复核结论：UIE-04 的总体主张 `SUPPORTED`（原始出处一致），但其系数细节仍属 B3 分析层，不可归为本卷原话。
- **UIE-19/20（B5/B6，同一导航行为的意义因能力/任务透明度而异）**：本卷提供直接初级支持——回访意义因任务翻转的明确表述（“task demands must be taken into account…”，PDF p.120）、无导航任务中最优行为是“不导航”（PDF p.107）、导航×成绩相关跨国 0.68–0.86 的异质性（PDF p.99）。→ `SUPPORTED`。
- **UIE-11（B2 的 66.3% 从未导航）**：本卷不包含该数字（那是 PISA 2018 Rapa Nui）。本卷提供的是任务级等价物：无需导航任务 83.5% 留在起始页（PDF p.107）、IWANTTOHELP Q4 约 40% 未作答（PDF p.110）等。→ 不改 UIE-11，但可加注“PISA 2009 亦有任务级未导航/未作答比例，见 METHOD-024”。
- **UIE-12（B7 的仪器设计压缩行为空间）**：本卷独立佐证——开发者刻意限制页数与加指引（PDF p.106），且 log 完整性问题导致数据不准（PDF p.123）。→ 佐证性，`SUPPORTED` 作为操作性事实。
- **审计结论“B-tier 页级导航 → 区域可见性为 PROJECT-INFERENCE”**：本卷确认 B-tier 全部为页级 log 指标（PDF p.230），边界成立。

### 建议的新 UIE 条目草稿

1. **UIE-31（Class 3）**：大型机考中 log 采集与投递技术故障直接制造系统性缺失——整卷自述页访问数据“未能完全准确采集”（PDF p.123）；日本/丹麦整校技术故障使数字阅读学生响应率降至 56%/69%，且官方“不做无响应调整”、以 PV 补缺（PDF pp.247–248）。Verdict：`SUPPORTED`。Scope：PISA 2009 数字阅读，19 国；技术故障缺失是投递层事件，非随机。
2. **UIE-32（Class 3/Class 4）**：导航过程指标的版本可比性靠统计校正而非设计不变性——6 种测试（3 cluster × 2 顺序）须按测试居中、再按国家居中，另做每测试标准化稳健分析，结果方一致（PDF pp.230–231）；估计量选择受背景模型影响（导航未进 PV 模型 → 只能用 WLE，PDF p.94 脚注）。Verdict：`SUPPORTED`。Scope：题本组合/顺序改变会移动过程指标均值；校正后结论稳定——对项目 baseline 的启发是版本变更必须显式纳入仪器合同。
3. **UIE-33（Class 2/Class 4）**：访问量-成绩关系是倒 U 而非单调——相关页访问次数与页访问数的二次项系数逐国为负（OECD 平均：−20 次访问 ≈ −64.6 分，+20 次 ≈ +30.5 分；中等效应）；唯一线性的是相关页数（PDF pp.102–103）。Verdict：`SUPPORTED`。Scope：任务型页式超文本；提示“更多导航=更差/更好”都不是可用规则（呼应审计 Class 2 中 B3 的相反向证据）。
4. **UIE-34（Class 2/Class 4）**：回访（revisit）的意义任务依赖，同一行为不能固定解读——JOB SEARCH 中回访是有益策略（最优组 4 次访问），SMELL Q1 中额外回访与低能力相关；本卷原话要求“任务需求必须纳入回访分析”（PDF p.120, p.117）。Verdict：`SUPPORTED`。Scope：为审计 UIE-19/20 的任务透明度调节提供初级出处级支持；对项目“revisit != confusion”的基线约束是直接佐证。
5. **UIE-35（Class 4）**：产品分数与过程证据可解耦——不访问关键页仍可得满分（猜答）：IWANTTOHELP Q2 3.9%、SMELL Q1 <5%、JOB SEARCH Q2 150 人（0.7%），且猜答者能力显著更低（PDF p.109, p.116, p.121）。Verdict：`SUPPORTED`。Scope：MC/开放型数字阅读题；产品分不能担保预期过程发生——支持项目“response-only baseline 永久保留、process feature 需独立效度”的边界。
6. **UIE-36（Class 4，可选草稿）**：同一产品的数字-印刷成绩差随任务与作答状态变化（JOB SEARCH Q2：满分 +17 分、无分 −20 分、未作答 −40 分，PDF p.119）——单一“模式效应”不成立，模式差异须按任务/作答状态分解。Verdict：`SUPPORTED`（描述性）；不可外推为一般模式效应。

## 复核备注

- 页码均为 PDF 物理页（= 印刷页 + 2，已用卷内多处页脚核对，如印刷 89 = PDF 91）。
- 图/表 DOI `10.1787/888932435397`（Figure VI.3.1 等）即审计 C6 检索命中的“Navigation in the PISA 2009 digital reading assessment”章节的 iLibrary 章节 DOI——本卷即该章节的完整载体（PDF p.95, p.96）。
- 未改 catalog、checksums、审计主文件或任何其他文件；临时提取文件在 `tmp/extract/`（method024_*.txt），可删除。
