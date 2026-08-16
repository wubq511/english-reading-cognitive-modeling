# UI 仪器效应证据审计

Status: `CURRENT`
审计日期：2026-08-15（第一轮：本地盘点 + 开放网络检索 + 钉页证据 UIE-01..30）；2026-08-16（第二轮：24 篇队列文献全文提取与综合，证据表扩至 UIE-01..64）
范围：作答 UI 的布局、导航、反馈、无障碍与交互 affordance 是否影响行为、缺失、测量信度或被测量（estimand）的一手证据（Wayfinder 研究票，GitHub Issue #5）

## 结论速览

- **核心结论**：作答 UI 的选择是测量仪器设计，不是 UX 偏好。反应格式会同时移动过程指标与产品分数（`B7`，OR=1.40；本轮新增四个独立收敛证据：UIE-31/35/42/44）；投递模式（纸/屏/设备）会移动阅读分数分布，但**方向是任务条件化的**——说明文/限时语境纸优（g ≈ −.21 ~ −.32，UIE-46/47/53）、叙事与非速度语境统计等价于零（UIE-48）、高速度标准化考试屏优（`METHOD-012`，d=.16–.22，UIE-27）、儿童标准化语境屏劣（UIE-54）——任何单方向断言都不受支持。WCAG 2.2 的 SC 2.5.7 / 1.4.10 / 2.2.1 / 2.5.8 作为规范性约束直接进入仪器合同（baseline UI 冻结前必须满足）。住宿/无障碍特征「可用 ≠ 被用」，且其效应是层级依赖的（item 参数 / scale 分布 / 方差结构三层各自独立，UIE-60/62/63）。
- **怎么得出的**：第一轮为本地 80 源盘点 + 2026-08-15 当日 Crossref / Semantic Scholar / WebSearch / ERIC 检索与五个种子文献的引用链追踪；第二轮（2026-08-16）对第一轮定位的 25 项队列文献中的 24 篇做全文逐页提取（24 个并行提取代理，每篇一份钉页笔记，见 `ui-instrument-effects-evidence-audit/METHOD-016..039.md`），外加 CNKI/万方人工检索轮（评估为近阴性，唯一直接命中即库存 `METHOD-011`）。全部负载结论钉到本地 PDF 物理页码；四类主张（可用性偏好 / 行为改变 / 信度与缺失 / 学习与构念）全程分离，不混用。
- **未决项**：Class-1 可用性/偏好实证仍 `UNRESOLVED`——本轮确认这是领域级共识缺口（UIE-61），不是本地语料不足。队列 #12（Lovett & Lewandowski 2015 书章）经影响评估后标记为不可获取（住宿实证已由 5 篇入库文献覆盖，见「获取队列」节）。「within-mode 阅读 MC 作答 UI 变体是否移动构念/estimand」仍无直接证据，须由 H2-gated 变体研究回答。

## 目的与判定规则

本审计回答 Wayfinder #5：UI 变体不能凭视觉偏好或通用可用性惯例来选择，因此本审计确立本地一手文献与正式标准**实际显示了什么**、**没有显示什么**关于 UI-仪器效应的证据。审查单位是关于 UI-仪器效应的主张（claim），不是论文摘要。本审计不把先前的 ChatGPT 分析或 migration package 当作证据；`reports/literature/` 的深读报告只用作索引，以下每条负载主张都对本地持有的 PDF 重新核验过。

标签（沿用 `reports/research/existing-literature-validation-audit.md`）：

- `SUPPORTED`：本地来源在其研究的人群、任务、变量与设计范围内直接支持该主张；
- `PARTIAL`：来源只支持主张的一部分或只支持更窄的设定；
- `PROJECT-INFERENCE`：本项目做出的可辩护设计推断，但不是所引来源报告的发现；
- `OVERSTATED`：措辞超出证据，不得用作事实前提；
- `UNRESOLVED`：本地语料不足以做决定。

下文页码定位除明确说明为印刷页外，一律指 PDF 物理页。文件身份以 `sources/catalog.yaml` 的 SHA-256 为准；本审计不修改 catalog、checksums 或任何来源文件。只在摘要层面核验过的主张标 `ABSTRACT-ONLY`；取自深读报告且无法复核到表级的钉点会显式标出并降级。

## 方法与检索边界

### 本地语料筛查

- 筛查语料：本地 catalog（`sources/catalog.yaml`）——B 层数字阅读测评论文（B1–B11）、C 层光标/眼动论文（C1–C8）、D 层分段论文（D1–D7）、E 层诊断/效度论文（E1–E8）、UIB 层交互日志论文（UIB-001..018）、`STANDARD-001`（Standards for Educational and Psychological Testing, AERA/APA/NCME 2014），以及第二轮新增的方法层论文 `METHOD-010..039`。
- 用作索引的报告语料：六份 A/A+/B/C/D/E 深读报告、`reports/literature/ui-interaction/A_tier_notes.md` 与先前的验证审计。以下所有页码钉点都通过打开本地 PDF（`pdftotext -layout`）复核；源报告中章节级的钉点在此处或重新钉到 PDF 页、或显式标出。
- 本票的四类主张全程分离：可用性/偏好、行为改变、仪器信度与缺失、学习与构念及 estimand。混用这四类正是本审计要防止的失败模式。

### 开放网络检索协议（2026-08-15）

本地语料单独不足以回答本票；当日对 Crossref、Semantic Scholar 与（尝试的）OpenAlex 做了 dated 检索，外加定向的出版商/仓储抓取。所有查询于 2026-08-15 经 `curl --retry 5 --retry-all-errors --retry-delay 2` 执行。筛查按标题/摘要/元数据记录；按 DOI 去重；近似命中保留排除理由。total-results 是索引级相关性排序命中数，不是筛查集大小。

Crossref（`api.crossref.org/works`，`query.bibliographic`，rows=5）：

| # | 查询串 | total-results | 筛查结果 |
| --- | --- | --- | --- |
| C1 | "The effect of drag-and-drop item features on test-taker performance and response strategies" | 314,578 | 命中：Arslan et al. 2020（10.1111/emip.12326）——目标定位，当时 gated（第二轮已入库为 `METHOD-016` 并读毕）。另浮出 OECD 2024 脱离投入工作论文（10.1787/7abea67b-en，第二轮入库为 `METHOD-023`）。 |
| C2 | "response format effects computer-based assessment process data" | 17,598,485 | 近似命中排除：Haaf 1999（言语-语言软件，超范围）；Breuer et al. 元分析记录为 PsycEXTRA 数据集条目（二手）。 |
| C3 | "reading from paper compared to screens meta-analysis" | 15,803,775 | 命中：Clinton 2019（10.1111/1467-9817.12269）——当时 gated（第二轮入库 `METHOD-019`）。近似命中：Richardson 2022 SpringerBrief 章节（字体可读性，超范围）。 |
| C4 | "effects of reading media on comprehension meta-analysis" | 10,476,434 | 命中：Delgado et al. 2018（10.1016/j.edurev.2018.09.003，第二轮入库 `METHOD-018`）；Schwabe et al. 2022（10.1080/15213269.2022.2070216）——反向记录（第二轮入库 `METHOD-020` 并已裁决，见 UIE-48）。 |
| C5 | "mode effects paper versus computer-based testing reading comprehension" | 13,419,233 | 命中筛查：Mangen et al. 2013（10.1016/j.ijer.2012.12.002，第二轮入库 `METHOD-027`）；Prisacari & Danielson 2017（10.1016/j.chb.2017.07.044）——近似命中（化学测验模式 + 认知负荷；记录，未入核心队列）。 |
| C6 | "navigation log file data digital reading assessment students" | 7,228,159 | 命中：OECD 章节 "Navigation in the PISA 2009 digital reading assessment"（10.1787/888932435397）——OA 但抓取被挡（见盲区）；其完整载体整卷第二轮入库为 `METHOD-024`。近似命中排除：数字取证/钻孔日志记录（同形异义噪声）。 |
| C7 | "universal design computer-based assessment accommodations accessibility" | 12,257,805 | 命中筛查：Lovett & Lewandowski 2015 章 "Universal design for assessment"（10.1037/14468-010）——书章，gated（第二轮经影响评估标记为不可获取，见「获取队列」节）；Cawthon & Shyyan 2022 百科条目——近似命中（二手综述）。 |
| C8 | "rapid guessing test-taker disengagement computer-based assessment response time" | 980,158 | 命中：OECD 2024 WP（10.1787/7abea67b-en，与 C1 去重，第二轮入库 `METHOD-023`）；Papanastasiou et al. 2026——近似命中（时间管理焦点；记录）。 |
| C9 | "PISA 2015 mode effects computer-based delivery field trial OECD" | 1,200,125 | 命中：PISA 2015 Results Vol. V（10.1787/9789264285521-en，第二轮入库 `METHOD-025`）——**第二轮修正**：该卷只含 field trial 的过程声明，量化等值结果不在其中（见 UIE-59）。Ezike 2020 AERA 会议论文——近似命中（细节贫乏）。 |
| C10 | "cursor movements disengagement process data low-stakes assessment Pokropek" | 7,368,410 | 命中：Pokropek et al. Mouse Chase——EJPA 2023（10.1027/1015-5759/a000758）及 OA PsyArXiv 预印本（10.31234/osf.io/9kpmn）→ 第一轮已获 `METHOD-010`。 |

Semantic Scholar（`api.semanticscholar.org/graph/v1/paper/search`，limit=6）：

| # | 查询串 | total | 筛查结果 |
| --- | --- | --- | --- |
| S1 | "effect of drag-and-drop item features on test-taker performance and response strategies" | 1 | 确认 Arslan 2020 记录；`isOpenAccess=false`，无 OA PDF → 当时 gated（第二轮已入库 `METHOD-016`）。 |
| S2 | "response format effects digital assessment cognitive processes" | — | 限流（HTTP 429），8 次退避重试后放弃；盲区已记录。 |
| S3 | "reading comprehension paper versus screen meta-analysis" | 447 | 命中筛查：Fesel/Salmerón 系手持设备元分析（10.1037/edu0000830，第二轮入库 `METHOD-021`）；Li & Yan 2024 Teler 元分析（10.1016/j.teler.2024.100142，第二轮入库 `METHOD-022`）；Schwabe 2022（去重）。近似命中排除：药学教育复制研究（人群超范围）。 |
| S4 | "paper versus computer-based testing mode effects" | — | 限流（HTTP 429）；盲区已记录。 |
| S5 | "test accommodations universal design accessibility assessment" | 7,905 | 命中筛查：Taylor & Banerjee 2023 Language Testing（10.1177/02655322231186222，第二轮入库 `METHOD-026`）；Ogut et al. 2025 EMIP "Universal by Design…through Process Data"（10.1111/emip.70007，第二轮入库 `METHOD-017`）。近似命中排除：城乡规划 UD 论文、护理课堂住宿（领域不符）。 |

WebSearch 广域发现通道（通用网络索引，2026-08-15）：

| # | 查询串 | 筛查结果 |
| --- | --- | --- |
| W1 | "screen versus paper reading comprehension meta-analysis digital reading medium effect" | 确认 Clinton/Delgado/Schwabe/Salmerón/Li–Yan 簇。新增：Kong, Seo & Zhai 2018 元分析（Computers & Education 123, 138–149；10.1016/j.compedu.2018.05.005，第二轮入库 `METHOD-029`）；儿童模式效应实验（挪威，n=1139，IRT 建模；10.1016/j.compedu.2020.103861，第二轮入库 `METHOD-030`）。二手/三手命中（博客、教学站）排除。 |
| W2 | "computer-based versus paper-based test mode effects K-12 assessment meta-analysis comparability" | 新增：Wang, Jiao, Young, Brooks & Olson K-12 阅读模式效应元分析（EPM 68(1), 5–24；10.1177/0013164407305592，第二轮入库 `METHOD-028`）；Kingston 2009 综述记录（未核实 DOI，未入队）；ACT 技术报告 R1842/R1847 浮出——R1847 第一轮已获 `METHOD-012`。 |
| W3 | "item response format effect test performance drag-and-drop multiple choice constructed response measurement" | 噪声主导（临床推理 CR/SR 格式；CR 题投入度）。无在范围内的命中。 |
| W4 | "digital assessment accessibility accommodations score comparability students with disabilities computer-based testing" | 新增：延长时间住宿 × 过程数据分数可比性研究（10.1002/pits.23275，第二轮入库 `METHOD-031`）；其引用的住宿使用率线索（Lee et al. 2021，第二轮入库 `METHOD-037`；Witmer & Bouck 2023）已记录。**第二轮修正**：本行原把 Lee et al. 2021 概括为「住宿实际使用率低」的证据——全文核验后该概括需限定（对获批者使用率并不低），见 UIE-64，否则构成 `OVERSTATED`。实务指南作为非证据排除。 |
| W5 | "WCAG conformance large-scale educational assessment delivery platform accessibility" | 仅实务/厂商材料；一条框架注记（WCAG 符合 ≠ 复杂测评任务的可用无障碍；辅助技术用户面对两层界面——ictaccessibilitytesting.org 白皮书）作为非同行评审语境记录。未定位到一手证据——强化 Class-1 实证缺口。 |
| W6 | "阅读测评 机考 纸笔测验 等值 对比研究 考试模式效应"（中文模式效应扫查） | 命中：陈平/代艺/黄颖诗 2023 测验模式效应综述（心理科学进展 31(10), 1966–1980；10.3724/SP.J.1042.2023.01966）→ 第一轮已获 `METHOD-011`。二手线索：一份 PISA-2015 field-trial 报告称 65/103 题模式等价、38 题难度漂移（chuimin.cn 摘要）。**第二轮修正**：该量化内容经全文核验不在 PISA 2015 Vol. V（`METHOD-025`）中，真实出处应为 PISA 2015 Technical Report（OECD 2017b）；该数字未经一手核验，不作负载使用。新闻/实务条目排除。 |

Semantic Scholar 图 API 引用链追踪（2026-08-15；请求间隔 ≥6 秒以尊重共享限流）：

| 种子 | References（后向） | Citations（前向） | 在范围内的产出 |
| --- | --- | --- | --- |
| Arslan 2020（`10.1111/emip.12326`） | 不可得——Wiley 在 S2 中隐去参考文献（"elided by the publisher"） | 筛查 22 条 | Jiang et al. 2021 NAEP D&D 过程数据 → 第一轮已获 `METHOD-013`；JECR 2020 TEI 拖拽表现/效率（10.1177/0735633120969666，第二轮入库 `METHOD-032`）；EMIP 机考分散注意（10.1111/emip.12485，第二轮入库 `METHOD-033`）；两篇 OA 过程数据综述（10.1016/j.compedu.2025.105245；10.1186/s40536-024-00202-1）作为方法语境记录。近似命中排除：K-12 数学 TEI 效率、土耳其作答速度预测、韩国数学模式研究（领域不符）。 |
| `B7` Arslan 2026（`10.1016/j.cedpsych.2026.102461`） | S2 中 0 条 | S2 中 0 条 | 太新，引用图尚未形成；无链可追。 |
| `E6`（`10.1027/1015-5759/a000790`） | 不可得——参考文献被隐去 | 筛查 9 条 | 仅 `B7` 自身与一篇仿真探究论文（UI 超范围）；无新命中。 |
| `METHOD-010`（`10.31234/osf.io/9kpmn`） | S2 中 0 条（预印本无引用图） | 筛查 7 条 | LSAE 2024 量表格式 × 粗心作答研究（10.1186/s40536-024-00205-y，OA，第二轮入库 `METHOD-034`）；其余偏离（MTurk 数据质量、IDRIS 量表、XR 问卷副数据）或跑题。 |
| `C2`（DOI 经 Crossref 解析：`10.1145/2207676.2208591`） | 未追（CHI 参考文献是十年 HCI，测评先验低） | 筛查 100 条 | 光标即注意力的 HCI 脉络仍在延续（如阅读区域估计 10.1145/3588015.3588404；光标阅读行为挖掘 10.1016/j.bdr.2022.100328），但无一是阅读测评仪器效应研究——这确认了 C 层迁移边界（UIE-05/06/13）而非扩展它。无队列新增。 |

ERIC（`api.ies.ed.gov/eric/`，JSON API，无需 key，rows=20；全部 2026-08-15 执行）。numFound 为索引级；按标题/摘要记录筛查，按 accession/DOI 去重：

| # | 查询串 | numFound | 筛查结果 |
| --- | --- | --- | --- |
| E1 | "computer-based testing mode effects comparability" | 677,691 | 顶部命中含队列项 14（Wang K-12 阅读元分析，EJ782104，第二轮入库 `METHOD-028`）与已持有 `METHOD-012`（ED610238）——确认覆盖。新增在范围内：Lin 2018 早期小学模式可比性学位论文（ED599537，免费全文）→ 入队记录；Pan 2016 K-12 数学可比性元分析（ED596649）——近似命中（仅数学，记录）；EJ1347750 是 ACT 差异速度性线索的期刊版（与 `METHOD-012` 相关，记录）。 |
| E2 | "reading comprehension screen versus paper digital" | 459,585 | 新增：Furenes, Kucirkova & Bus 2021 儿童纸 vs 屏元分析（39 研究，n=1,812；EJ1301549，第二轮入库 `METHOD-035`）；Goodwin et al. 2020 AERJ（371 名中学生，免费全文 EJ1260522）→ 第一轮已获 `METHOD-014`；另一篇 2021 元分析（EJ1294459）记为近似重复。 |
| E3 | "item format response format effects test performance" | 560,803 | 新增：Kobayashi 2002 L2 阅读理解测验文本组织 × 反应格式效应（EJ647287，第二轮入库 `METHOD-038`）；Woodcock et al. 2020 小学低年级题目格式被试内实验（EJ1239083，第二轮入库 `METHOD-039`）。近似命中：IRT 链接/混合格式建模、TIMSS 科学格式效应（领域不符）。 |
| E4 | "testing accommodations accessibility comparability computer-based" | 570,700 | 新增：Dembitzer & Kettler 2023 机考阅读理解测验上的普适设计住宿（131 名 12 年级学生；EJ1402960，第二轮入库 `METHOD-036`）；Lee, Buzick, Sireci & Lee 2021 州级 CBT 内嵌住宿使用（EJ1327403，第二轮入库 `METHOD-037`）；DePascale/Dadey/Lyons 2016 CCSSO 设备可比性报告（ED610777，免费全文）→ 第一轮已获 `METHOD-015`。NCEO 综述报告（2002/2010）记为过时背景。 |
| E5 | "navigation process data digital reading assessment log" | 848,159 | 顶部命中即已持有 `B2`（EJ1378569）——确认 ERIC 索引了持有语料；其余（电子书日志、超媒体导航画像）与 B 层相邻，没有超出语料已有的负载内容。 |

获取队列中所有出版商落地 URL 均于 2026-08-15 经 `doi.org` HTTP 重定向解析（HEAD 请求，不触碰 bot-wall 内容端点）。ERIC 全文 URL 遵循稳定模式 `files.eric.ed.gov/fulltext/<ACCESSION>.pdf`。

明确盲区与访问边界（全部于 2026-08-15 遇到；第二轮状态见各条末尾）：

- **OpenAlex**（2026-08-15 的 dated 边界）：尝试查询 O1–O6（Arslan 2020 查找；反应格式效应；纸 vs 屏元分析；CBT 模式效应；导航日志数据；普适设计/测评）。首次尝试挂起 >5 分钟无响应（代理传输故障）；其后单次探测返回 HTTP 429 "Insufficient budget … Resets at midnight UTC"（`retryAfter: 62853`）。根因当日已核实：匿名日额度**按出口 IP** 计费，本机走共享代理，额度被同出口其他用户烧掉——加 `mailto` 不能修复。持久修复是免费 OpenAlex API key（项目约定：环境变量 `OPENALEX_API_KEY`）；Semantic Scholar 的共享限流同理（环境变量 `S2_API_KEY`，也是上文 S2/S4 失败的原因）。**第二轮更新（2026-08-16）**：`OPENALEX_API_KEY` 已配置并经 curl 验证（HTTP 200 JSON）；S2 key 申请在审批中。第一轮缺失的 OpenAlex 覆盖当时由 Crossref/S2/WebSearch/ERIC 加人工获取队列替代；同题 OpenAlex 复检轮留作可选 TODO，不阻塞本审计结论。
- **Google Scholar**：未查询——设计上拒绝自动化；记为常设边界，非勤勉度缺口。
- **CNKI/万方**：本环境无合规自动化路径——对 Agent 是常设边界。第一轮部分缓解：经 WebSearch 定位中文模式效应综述并从期刊官网获取（`METHOD-011`）。**第二轮更新（2026-08-16）**：用户完成人工检索轮（5 条检索式），原始结果存 `human-tasks/search_results.md`，Agent 评估为近阴性——唯一直接命中即库存 `METHOD-011`；万方 3 条 CAT/认知诊断候选排除；两条边际候选仅记录不下载；Q3/Q4/Q5 因 CNKI 反爬默认填充与万方未登录 0 条而失效——这是检索通道限制，不能解读为「中文无相关文献」；如需补强走 `METHOD-011` 参考文献引文追溯。评估全文见 `human-tasks/wayfinder-5-ui-instrument-effects.md`。
- **Unpaywall**：未查询——API 要求个人邮箱，项目未为此注册邮箱。（S2 对 Arslan 2020 的隐去通知也路由经 Unpaywall，故此边界也阻断了该处的后向引用链。）
- **出版商 bot-wall**：自动 PDF 抓取被拒绝（HTTP 403，Cloudflare 或同类）：`oecd-ilibrary.org`（OECD 工作论文，尽管形式上 OA）、`sciencedirect.com`（gold-OA Teler 文章）、`onlinelibrary.wiley.com`（Arslan 2020；Ogut 2025）、`journals.sagepub.com`（Taylor & Banerjee 2023）、`roderic.uv.es`（Salmerón et al. 2024 仓储存档）。这些是传输层拒绝，不是权利判定；条目进入获取队列走人工渠道（第二轮已全部经人工下载解决）。
- **W3C TR 端点**：`www.w3.org/TR/WCAG22/` 于 2026-08-15 从本网络被 Cloudflare 挑战，当日规范文本改经 W3C 自己的 `w3c/wcag` GitHub 源仓库（`guidelines/sc/` 树，`main` 分支）获取；2026-08-16 重试 TR 端点成功，WCAG 2.2 规范全文（W3C Recommendation 12 December 2024，单文件 HTML）归档为 `STANDARD-003`（sha256 固定字节身份，canonical TR URL 可重取核验），审计引用的 4 条 SC（2.5.7 / 1.4.10 / 2.2.1 / 2.5.8）逐字文本已对归档件核验一致。归档形式的决策与 supersession 见「获取队列」节。

### 第二轮：队列文献全文提取（2026-08-16）

第一轮定位的 25 项获取队列中，24 项由用户人工下载至 `tmp/pdfs/`，Agent 逐篇首页核验（标题/作者/年份/DOI/许可）后入正式库（`METHOD-016..039`，catalog/checksums/crosswalk 同步，`scripts/sources doctor` 通过）。随后 24 个并行提取代理（每篇一个）对全文做逐页证据提取：每篇产出一份钉页笔记 `ui-instrument-effects-evidence-audit/METHOD-0xx.md`，含研究概览、按四类主张分组的核心发现（结论 + 效应量/统计量 + PDF 物理页 + 英文原文短引文）、边界与局限、对既有 UIE 条目的支持/限定与新增条目草稿。本审计证据表第二轮新增条目（UIE-31..64）即从这些笔记综合而来，负载数字均经笔记与原文钉点核对。提取中发现的 8 处 catalog 作者名拼写与 PDF 首页不符（METHOD-016/017/021/028/030/031/035/037），已以 PDF 首页为准修正 catalog。唯一未获取项为 #12（见「获取队列」节）。

## 发现

### 证据表

| ID | 受审主张 | 来源 + 证据（PDF 页码） | 判定 | 范围边界 |
| --- | --- | --- | --- | --- |
| UIE-01 | 反应格式（drag-and-drop vs drop-down vs click-on-grid）改变可观察过程指标——多余事件、完成时间、信息检索停顿、最终作答复查停顿——且方向随任务类型而变。 | `B7`，被试内随机实验，443 名美国八年级学生；停顿定义与排序任务结果 PDF p.6，分类任务结果 PDF pp.7–9，讨论 PDF p.9。 | `SUPPORTED` | 八年级 ELA 排序/分类任务，封闭数字测评。D&D 在排序任务减少构念无关加工指标，在分类任务则没有（摘要，PDF p.1）。不是阅读理解 MC 格式研究。 |
| UIE-02 | 反应格式改变的是产品结果而不只是过程：drop-down 的 ELA 任务分数高于 D&D（OR = 1.40, p = .026），尽管交互更多——过程–产品解离。 | `B7`，PDF p.6（OR），PDF p.9（讨论："process–product dissociation"；"plausible explanation"；指标是需要出声思维/眼动验证的 "indirect proxies"）。 | 解离本身 `SUPPORTED`；作者「更受控更反思的投入」解释被他们自己标为需未来研究的 plausible explanation——当作事实使用即 `OVERSTATED`。 | 同 UIE-01。时长/交互含义的方向不固定：本研究中更长的停顿伴随更高分数。 |
| UIE-03 | 超文本布局 affordance（标签页位置）塑造导航选择：单页簇「图方便地」选择了离首页标签更近的书评标签。 | `B2`，PDF p.10（印刷 p.728）。 | `PARTIAL`——论文自己的解释性保留（"might also explain"），相关性聚类分析，非布局操纵。 | PISA 2018 Rapa Nui 单元，16,957 名 15 岁学生，3 页超文本；样本排除了 66.3% 从未导航者（PDF p.5）。 |
| UIE-04 | 任务访问需求同时移动导航量与导航-成绩关系：访问需求 → 访问 b = 3.16；访问行为 → 数字阅读 b = 0.35（超出印刷技能）；访问行为斜率高需求任务 b = 0.51 vs 低需求 b = 0.19；交互 b = 0.16。 | `B3`，PDF p.7（b = 3.16），PDF pp.11–12（b = 0.35/0.51/0.19/0.16）。 | `SUPPORTED`（相关性调节证据）。 | PISA 2009 数字阅读，29,395 名 15 岁学生，17 国；多页超文本，页级计数。论文声明预测不蕴含因果。**第二轮注**：这些系数是 Naumann 再分析层；其测量底稿原始出处整卷已入库（`METHOD-024`，UIE-56/57）。 |
| UIE-05 | SERP 布局改变眼–鼠标联合分布：三种广告布局 KL 散度 19.89/21.90/17.27，F(2,2644) = 11.93, p < .0001（纯自然结果布局分歧最大）；互信息 0.01–0.06 不显著；平均眼–鼠标距离 372.89 px。 | `C6`，PDF pp.5–6。 | `SUPPORTED`（本研究内）。 | 47 名实验室成人，静态 Google SERP，事务型搜索。非阅读；确立布局同时移动注意力分配与光标–注视耦合，因此光标证据强度是布局依赖的。 |
| UIE-06 | UI 设计可以凭空制造自然界不存在的光标–阅读耦合：MoTR 模糊鼠标尖端以外的文本，参与者「必须移动鼠标来揭示并阅读」。 | `C4`，PDF pp.1–2。 | `SUPPORTED`（强制耦合的存在性证明）。 | 强制耦合仪器是刻意的设计干预；其对齐数字不得外推到自然阅读 UI（`C4` 迁移限制已在 C 层报告登记）。 |
| UIE-07 | 游戏化 SRL 仪表盘（反馈显示）重组了学习行为：游戏化组的 FOMM 中心移到「查看 SRL 仪表盘」（到「查看推荐材料」的 TP = 0.695）；对照组以「查看学习任务」为中心。 | `B1`，仪表盘特征 PDF pp.5–6，FOMM 结果 PDF pp.10–11。 | 行为重组 `SUPPORTED`；总体 `PARTIAL`（准实验整班分配，平台级 SRL 轨迹，无篇章内事件）。 | 177 名中国大一学生，EFL 翻转课堂，学习（非测评）情境。阅读分数是结果变量；未建立行为→分数的中介。 |
| UIE-08 | 指导语措辞间接调节阅读过程：目的指导语塑造学生的任务模型，任务模型成分（如重读计划 β = .29）预测阅读过程；同一指导语产生不同任务模型。 | `B10`，摘要 PDF p.1；回归值在 Tables 6–7 附近（PDF pp.8–9 区域；表格单元未逐格复核）。 | `PARTIAL`——仅摘要与结果正文级核验。 | 大学生，四篇互补文本（自然选择），学习情境；探索性研究。 |
| UIE-09 | 题目表面特征（选项措辞与选项顺序）改变交互行为，并支持用鼠标特征预测难度。 | `C3`，操纵描述 PDF pp.8–9。 | 操纵存在与特征级预测 `SUPPORTED`；难度标签是问卷题目特征，不是空间注意。 | 成人网络问卷受访者；三道操纵题 + 基线题。 |
| UIE-10 | 编辑综合：只改题目表面设计、内容恒定，显著改变过程数据指标（引 Arslan et al., 2020）；构念无关过程数据方差来源包括题目内容、措辞、显示设计与多媒体元素。 | `E6`，PDF p.6。**第二轮升级**：底层实验 Arslan et al. 2020 已入库并全文读毕（`METHOD-016`，UIE-31/32）——编辑断言获一手验证。 | `SUPPORTED`（第一轮为 `PARTIAL` 二手；第二轮一手验证后升级；「显示设计」需限定为内容/组织/题干特征——纯空间布局只动 transition pause 不动分数）。 | 机考测评一般；成人数学分类 D&D 组间实验；阅读特异实例仍无（见 UIE-42/44 的格式级阅读证据）。 |
| UIE-11 | 导航行为以巨大的、需求依赖的比率缺失：66.3% 被分配单元的学生没有导航事件（被排除出分析）；题目无应答 30.6%。 | `B2`，PDF p.5。 | `SUPPORTED`。 | 此缺失是行为与设计依赖的，不是随机仪器故障——但它意味着基于导航的 estimand 是在选择性子样本上计算的。PISA 2009 的任务级等价物见 `METHOD-024`（UIE-56）。 |
| UIE-12 | 仪器与情境事件侵蚀完整性：B7 排除一所学校（76 名学生，题目泄露）、1 名学生（系统崩溃）、16 名学生（英语熟练度）；工作记忆任务 24% 非随机缺失；ELA 分数缺失 0.09%；故事被分页为 3–4 页「以防止滚动」——一个压缩可观察行为空间的设计选择。 | `B7`，PDF pp.4–5。 | `SUPPORTED`（研究报告操作）。 | 单研究操作，但它们证明事件完整性乃至行为空间本身都是仪器设计决策。 |
| UIE-13 | 指针信号缺席是常态而非错误：光标 58.8% 时间不活跃（该状态下注视–光标距离 233 px，点击/动作时 74–77 px）。 | `C2`，PDF p.6（Table 1）；滞后证据 PDF pp.2, 5。 | `SUPPORTED`（网页搜索内）。 | 27 名成人，SERP 浏览。把不活跃光标当缺失数据还是当证据是设计决策；论文反驳光标即注视（"misguided"，PDF p.9）。 |
| UIE-14 | 传感器级过程通道遭受严重且不可预测的数据丢失或偏倚；神经多样性与残障会以可使个体级推断失效的方式改变过程数据。 | `E6`，PDF pp.6–7。 | `SUPPORTED`（含引证的编辑框架主张）。 | 框架层；非本地测量。激励保守的个体级推断与无障碍处理。 |
| UIE-15 | 系统生成的 UI 事件（`visibility_changed`、`layout_changed`）作为一等语义事件保留而非按噪声过滤，使标签切换与布局变化留在测量链内。 | 项目词汇决策（D 组报告 §19/§23；`SYSTEM_DESIGN.md` §4），依据 `D5` 的任务级抽象先例（PDF pp.2–3；先前审计 LIT-D5-01：作为架构先例 `SUPPORTED`）。 | `PROJECT-INFERENCE` | 没有本地论文测量这些事件在阅读 UI 中的价值；这是我们的仪器合同，由架构先例而非实证结果支撑。 |
| UIE-16 | 题目类型标签不保证预期作答过程：与预期答案构念的出声思维对齐率总体 41%、按题型 20–58%；Rasch PCA 解释 41.2% 方差。 | `E8`，PDF p.10（Table 4 区域），PDF p.11。 | 中等强度 `SUPPORTED`——出声思维 n = 5 小、单编码者、未报告评分者间信度。 | 八年级阅读理解 MC 测评，33 名学生，单篇章，美国东北。 |
| UIE-17 | 轨迹通道与言语通道证据不可互换：仅 17.18% 的已识别时段两通道过程匹配；27.17% 分歧共现；约 45% 由单一通道贡献。 | `E7`，PDF p.1（摘要）与结果表（PDF pp.12–19，依先前审计 LIT-E7-01）。 | `SUPPORTED`（不可互换性）；把任一通道当认知真值即 `OVERSTATED`。 | 44 名大学生，学习任务中的 SRL 过程。百分比是任务与编码特异的；不得变成项目先验。 |
| UIE-18 | 公平性/效度框架：公平的测验「对所有考生反映相同的构念」，不因构念无关特征而优待或亏待个体；普适设计要求从设计之初「反映预期构念、最小化构念无关特征」；无障碍「实际上是测验偏差问题，因为无障碍障碍会导致不同群体对分数的不同解释」。 | `STANDARD-001`，PDF pp.59–60（印刷 49–50），PDF p.62（印刷 52）。 | `SUPPORTED`（治理性标准框架）。 | 标准文本，不是任何具体 UI 变体的实证证据；它定义 UI 变体决策必须履行的义务。 |
| UIE-19 | 同一导航行为的构念含义因人而异：理解技能对数字阅读的效应很大程度上经导航中介（直接 b = 0.17 vs 导航 b = 0.70；策略知识完全中介，间接 b = 0.15），理解 × 问题解决在导航 Precision 上补偿性交互（b = −0.08）但在时间分配上不交互。 | `B5`，PDF pp.8–9；`B6`，PDF pp.9, 11–12。 | `SUPPORTED`（相关路径模型证据）。 | PISA 2009/2012，15 岁学生，19/32 国。同一行为 ↔ 跨个体不同技能含义；不支持单一全局行为→构念映射。原始出处的任务级佐证见 UIE-56（`METHOD-024`）。 |
| UIE-20 | 任务透明度决定导航是否反映问题解决：不透明的搜索引擎式任务 vs 透明的互链电子课本任务要求不同（交互 vs 加性）模型。 | `B6`，讨论 PDF pp.12–13。 | `PARTIAL`——讨论层理论调节，非操纵比较。 | 同 UIE-19。 |
| UIE-21 | 可用性问题表现为发散的用户行为，使其可从交互日志检测（移动 app：「我们预期用户在遇到可用性问题时以不同方式交互」；基于 GUI 变化的异步可用性测试日志；多模态可用性异味数据集 11 类异味报告最高 92% 检测准确率）。 | `UIB-009`，PDF p.1；`UIB-010`，PDF p.1（摘要）；`UIB-001`，PDF p.1（摘要）。 | `PARTIAL` 且跨域；UIB-001/UIB-010 为 `ABSTRACT-ONLY`。 | 移动 app / GUI 测试 / 情感计算数据集。基于行为的可用性检测方法词汇；这里没有任何阅读测评发现。 |
| UIE-22 | 光标移动副数据可筛查粗心/无动机作答：构造的光标指标与经典粗心作答指标中度相关，部分指标（水平移动距离；垂直速度与加速度）对实验诱导的动机状态与经典指标同等敏感。 | `METHOD-010`（2026-08-15 获取，EJPA 2023 的 PsyArXiv 预印本），摘要 PDF p.2；设计 PDF p.6（三种指导语条件；>2000 名受访者，PDF p.4）。 | `SUPPORTED`（网络问卷范围内）。 | 成人网络问卷受访者（prolific 式面板），Likert 量表；非阅读测评。确立 UI 通道数据质量筛查，不是认知。正式版 EJPA 为引用版本；本地文件是作者预印本。筛查指标的不可互换性与失败模式见 UIE-41/58。 |
| UIE-23 | Web 无障碍标准直接约束作答 UI affordance：WCAG 2.2 SC 2.5.7（Dragging Movements，Level AA）——"All functionality that uses a dragging movement for operation can be achieved by a single pointer without dragging, unless dragging is essential"。 | WCAG 2.2，W3C Recommendation，SC 2.5.7；canonical URL `https://www.w3.org/TR/WCAG22/#dragging-movements`；归档件 `STANDARD-003`（Recommendation 12 December 2024 单文件 HTML），引文逐字核验一致（2026-08-16）。 | `SUPPORTED`（规范性标准文本）。 | Web 内容一般，非测评特异。约束任何拖拽作答/排除 affordance：必须存在单指针替代路径。与 UIE-01/02 交互：替代路径本身是携带不同过程指标的另一种反应格式（UIE-31 提供直接实证）。 |
| UIE-24 | 布局必须经得起缩放/重排：WCAG 2.2 SC 1.4.10（Reflow，Level AA）——内容在 320 CSS px 等效宽度（1280 px 下 400% 缩放）必须「不丢失信息或功能、不要求二维滚动」地呈现。 | WCAG 2.2，SC 1.4.10；`https://www.w3.org/TR/WCAG22/#reflow`；归档件 `STANDARD-003`（同 UIE-23）。 | `SUPPORTED`（规范性标准文本）。 | 对冻结的双栏「左篇章 + 右题目」baseline 的直接约束：并排栏在高缩放必须重排，否则布局不达 AA。也与 BENCH-E0 相关：缩放/resize 事件改变被测量的布局状态。屏上距离/滚动的实证代价见 UIE-34。 |
| UIE-25 | 计时与命中目标约束：WCAG 2.2 SC 2.2.1（Timing Adjustable，Level A）要求时限可关闭/调整/延长，「essential」例外限于「时限是必要的且延长会使活动无效」；SC 2.5.8（Target Size Minimum，Level AA）要求指针目标至少 24×24 CSS px（含列明例外）。 | WCAG 2.2，SC 2.2.1 与 SC 2.5.8；`https://www.w3.org/TR/WCAG22/#timing-adjustable` 与 `#target-size-minimum`；归档件 `STANDARD-003`（同 UIE-23）。 | `SUPPORTED`（规范性标准文本）。 | 测验计时政策与无障碍义务相交；「essential」例外是标准给真正速度性测验的机制——使用它是构念主张（速度属于构念），必须照此记录。计时作为模式效应 moderator 的实证见 UIE-46/50。目标尺寸约束选项与排除/恢复控件设计。 |
| UIE-26 | 投递模式效应（test mode effect, TME）是公认的公平性/选拔/等值威胁，且有 UI 层来源：屏幕分辨率/尺寸/可读性（更大屏幕改善可读性从而提高表现，引 Bridgeman et al. 2003）、是否允许答案回看/修改、计时显示选项；效应与年级和题型交互；约 1/3 被观察学生在两模式间使用不同作答策略（Johnson & Green 2006）；PISA 跨周期模式切换威胁趋势等值（Feskens et al. 2019）。 | `METHOD-011`，摘要 PDF p.1；TME 来源分类 PDF p.2（显示因素、回看/修改政策、计时；PISA 等值威胁）；题目级交互与策略证据 PDF p.3。 | `SUPPORTED`（同行评审中文方法综述）；每条继承的单研究效应为综述中介 `PARTIAL`（未对其全文逐篇本地复核）。 | K-12/大规模 PBT↔CBT 一般（TOEFL/GRE/PISA/NAEP 示例）；非阅读 UI 变体特异。计时维度的元分析级证据见 UIE-46/50。中文数据库检索轮（2026-08-16）确认该综述是中文「测验模式效应」文献的锚点，未产生新的必读中文来源。 |
| UIE-27 | 投递模式在操作性大规模阅读测验中移动产品分数分布：跨 ACT 2019–2020 三项研究，在线阅读量表分高于纸笔 +1.06/+1.19/+1.50（1–36 量表；d = .16–.22, p < .0001）；阅读模式效应集中在后段题目（累计 p 值差到第 ~30 题 ≈0.5，最后 10 题升到 ≈1.5——与差异速度性一致）；遗漏是模式依赖的（遗漏 ≥1 题的学生：阅读纸笔 11.1% vs 在线 8.3%，最后 1–2 题反转）；每项研究有少量阅读题被标记模式 DIF；作者的缓解是跨模式等值，而非等价声明。 | `METHOD-012`，结论 PDF p.2；后段集中 PDF p.8；遗漏率 PDF p.10；模式 DIF 计数 PDF p.13（Table 4）；阅读量表分行 PDF pp.14–15（Table 5）。 | `SUPPORTED`（ACT 范围内）。 | 美国 ACT 入学考试，模式在 2019–2020 操作性施测中随机分配。模式级（纸 vs 在线投递），不是 within-mode UI 变体证据。**第二轮补充**：方向不可普适化——说明文/成人实验语境纸优（UIE-46/47/53），叙事/非速度语境等价于零（UIE-48），本条目为高速度操作性语境屏优；方向由任务语境决定。 |
| UIE-28 | 操作性数字测评中的拖拽题产出的过程数据可区分正确率组：时间分配、答案修改行为与动作序列揭示了作答数据单独看不到的策略差异与误解点。 | `METHOD-013`，摘要 PDF pp.1–2（NAEP 2017 首次数字操作性施测；4、8 年级各一道 D&D 题）。 | `SUPPORTED`（探索性过程数据证据）。 | NAEP 数学 4/8 年级 D&D 题；描述性策略分析，非格式操纵——与 `METHOD-016`（Arslan 2020 格式操纵实验，第二轮已入库，UIE-31/32）互补而非替代。 |
| UIE-29 | 阅读媒介改变存在哪些过程行为及其含义：371 名美国 5–8 年级学生在类标准化测验阅读任务中，纸上划线与注释多于数字；纸对较长文本部分的理解略有支持；数字划线与理解正相关而纸上划线与理解负相关（行为质量因媒介而异，不只是数量）。 | `METHOD-014`，摘要 PDF p.1（AERJ 57(4), 1837–1867）；主张钉在摘要/结果正文级。 | `SUPPORTED`（本研究内）；行为–理解联系为媒介内相关。 | 美国 5–8 年级，类标准化测验的说明文阅读任务。直接切题的媒介 × 过程行为 × 结果证据；是纸 vs 数字对照，不是 within-UI 变体对照。 |
| UIE-30 | 跨设备分数可比性是明确的测评义务，且有举证责任规则：可比性主张要求跨设备题目内容相同 + 有计划的研究证明设备不引入构念无关方差（PDF p.8）；设备效应是题型权变的（计算机条件利于 MC 但不利于技术增强题——Eberhart 2015；平板出声思维：D&D 为触控设计时有利，小/近目标有问题——Davis et al. 2013，PDF p.15）；屏幕尺寸骤降、键盘移除或触控引入的新设备不得在无先验可比性证据时大规模引入（PDF p.20）。 | `METHOD-015`，PDF pp.8, 15, 20（CCSSO TILSA SCASS 委托报告，2016）。 | `SUPPORTED`（委托指南 + 文献综合）；内嵌研究结果为综述中介。 | 美国 K-12 州问责测验政策语境（Title 1 Peer Review）；指南文档而非一手实验——但其举证责任规则是我们跨设备 `BENCH-E0` 证据的操作模板。 |

第二轮新增条目（UIE-31..64）由 24 篇队列文献的全文提取笔记综合而来；每条括注来源 ID，完整逐篇笔记见 `ui-instrument-effects-evidence-audit/METHOD-016..039.md`。

| ID | 受审主张 | 来源 + 证据（PDF 页码） | 判定 | 范围边界 |
| --- | --- | --- | --- | --- |
| UIE-31 | 只改题目表面特征、内容恒定，可同时移动过程指标与产品分数；分数移动方向随特征的构念相关性而异——source/target 内容对调（作者判为构念无关）B=−.428, p=.053（预测概率低约 5pp）；题干比较数 1→3（作者判为构念相关）B=−.450, p=.039；全部四个操纵均移动至少一个过程指标（策略分布对数优势比 swapped B=4.690、no-PS B=.922，均 p<.001；动作数 B=.208；拖时间 B=.264）。 | `METHOD-016`，PDF pp.1, 4, 6–9。 | `SUPPORTED` | 476 名 MTurk 成人、10 道同内容数学分类 D&D 题、组间随机。不是阅读 UI；迁移到阅读 baseline 为 `PROJECT-INFERENCE`。此研究即 `E6` 编辑综合（UIE-10）的原始出处。 |
| UIE-32 | 反向过程–产品解离：纯空间布局（targets first）与删除问题陈述移动过程指标（transition pause B=.073, p=.041；target-focused 策略 B=.922, p<.001）但不移动分数（p=.462/.467）与完成时间（p=.121/.350）。 | `METHOD-016`，PDF pp.7–9。 | `SUPPORTED` | 同 UIE-31。与 UIE-02 方向相反的另一型解离——强化「过程指标变化不能直推 estimand 变化」。 |
| UIE-33 | 过程指标估计天然建立在选择性子集上：4.8%（24/500）被试因过程数据捕获失败整人剔除；完成时间分析剔除 8% IQR 离群；策略估计仅基于 65.07% 的序列（33.11% mixed + 1.84% 不可归类被排除）；策略分类前算法剔除修订/未完成动作；α 跨设计变体 .61–.74。 | `METHOD-016`，PDF pp.3–7。 | `SUPPORTED`（研究报告操作） | 单研究操作；完整性是仪器属性，与 UIE-11/12/13 同教训。 |
| UIE-34 | 屏上距离与滚动需求改变交互时序：dragging time 仅在距离更大的 swapped content 条件显著更长（B=.264, p<.001，作者归因 Fitts' law）；需要滚动的两题 transition pause 普遍更长；作者在 Implications 明确建议最小化 source–target 距离、避免滚动（"test takers should not have to scroll…"，PDF p.10）。 | `METHOD-016`，PDF pp.7–10。 | `SUPPORTED`（本研究内；Fitts' law 归因是作者解释） | 对双栏滚动篇章 + 题目 baseline 的直接约束：滚动需求进入行为空间与时间分布；与 UIE-24（reflow）呼应。 |
| UIE-35 | 反应格式（drag-and-drop vs 键入数字/字母）在三种阅读理解任务（句序/图形组织器/完形填空）一致移动执行层过程指标——响应时间合并 d=−0.62、鼠标点击合并 d=−1.13（均 p<.001，节省 14.4–17.5%），年级 × 格式无交互（p=.560–.622）；而平均产品分数不动（合并 d=0.14, p=.295），但低表现学生 D&D 显著更高（d=0.57, p=.010）、高表现无差异（d=0.08）——平均 null 掩盖亚组分布移动。 | `METHOD-032`，PDF pp.12–13, 16–17, 20–22。 | 过程效应 `SUPPORTED`；亚组交互 `PARTIAL`（作者自标探索性） | 智利 4/6/8 年级西语阅读理解，桌面眼动仪实验室，无限时低利害；非 MC 作答 UI；注视时长大多 n.s.（d=0.08~−0.34），效应定位在执行层而非加工层。 |
| UIE-36 | 最小必需操作数相等的格式变更仍减少实际交互量：E3 传统与 D&D 最小点击同为 23，实际点击仍显著更低（中位数 34 vs 37，d=−0.71, p=.006）——事件最小集约束不保证执行层等价。 | `METHOD-032`，PDF pp.18, 20。 | `SUPPORTED` | 八年级完形填空/图形组织器；对 `BENCH-E0` 事件最小集设计与 `B7` 多余事件构造有直接含义：事件记录还需含冗余/纠错成分。 |
| UIE-37 | 布局的空间整合（图例嵌入图形）显著降低解题时间（log-time γ=−0.27, t=−5.07, p<.001；74.7s→55.4s）但对成绩无显著主效应（γ=0.24, z=1.67, p=.094）；时间效应随先验知识增强（integration × PK γ=−0.02, p=.005）。 | `METHOD-033`，全文钉页见笔记。 | `SUPPORTED` | 成人 MTurk、几何单选 MC、无限时 CBT、被试内随机；非阅读任务，迁移阅读作答 UI 为 `PROJECT-INFERENCE`；null 成绩结果须与 UIE-02/31 并列，不得合成「布局一定移动分数」。本地语料第一个布局操纵因果实验，Class-2 的布局空白从纯 `PROJECT-INFERENCE` 升为跨域 `SUPPORTED`。双栏分离布局的代价可直接被此范式测量。 |
| UIE-38 | 交互式 UI 辅助功能（hover 高亮）自发采用率 206/208 ≈ 99%，但单独可用不降时（γ=−0.08, p=.163），仅在 integrated 项内生效（交互 γ=−0.12, p=.007），且仅对高先验知识者提升成绩（signaling × PK γ=0.08, z=2.04, p=.041）——「功能被使用 = 测量中性」不成立。 | `METHOD-033`，全文钉页见笔记。 | `SUPPORTED`（行为/成绩两部分各自成立；成绩交互为单研究探索性） | 同 UIE-37；hover 依赖鼠标定点，跨子群外推谨慎。 |
| UIE-39 | 时间类过程指标的分析分布由显式筛查决策塑造：8.6% 被试（34/397）因快速猜测整体剔除；逐项按 item×condition 自定义下阈值（15% 平均时间）与上阈值（mean+2.5SD）；时间与成绩分析采用不同剔除集；7 人过程数据因技术故障缺失。 | `METHOD-033`，全文钉页见笔记。 | `SUPPORTED`（研究报告操作） | 单研究规则，不是统一标准；含义：time-on-task 的样本、分布形状与跨条件可比性都是仪器 + 分析决策的产物——`BENCH-E0` 必须预先固定快速猜测/离群处理规则。 |
| UIE-40 | 标签措辞级量表格式操纵（agreement↔frequency；abstract↔approximate 标签）对粗心/低投入作答（C/IER）行为零效应：q-implied 污染率双方 .08 [.04; .11]，组级差异围绕 0；但作者明示零效应 ≠ 数据质量等价（构念效度与 response styles 可能仍被格式移动）。 | `METHOD-034`，PDF pp.22–23, 27。 | `SUPPORTED`（零效应；不升级为「格式无效应」普遍结论） | PISA 2022 field trial 背景问卷（N=206,153）、Likert 标签措辞变化、作答模式不变；不覆盖反应模式级格式变化（对照 UIE-01/31/35——效应随格式变化粒度而变）。 |
| UIE-41 | 单源行为通道的 C/IER 筛查可严重过度标记且阈值敏感：long-string 单指标 64% vs 多源 6%；纯屏时混合分解 85% vs 多源 4%；Mahalanobis 阈值 .01→.05 使单指标中位污染率 .05→.08 而多源不变（相关 .99）；「快而认真」者可被误标。污染率还随仪器位置单调上升（首 .05 → 末 .10/.08）——污染/缺失率是仪器长度与位置设计的函数。 | `METHOD-034`，PDF pp.16–22。 | `SUPPORTED`（示例性演示；百分比为 scale-by-group 个案，非通用误判率） | PISA 2022 背景问卷；不量化阅读作答 UI 的筛查误判率。含义：任何单通道筛查的绝对数值不构成行为真值（呼应 UIE-22）。 |
| UIE-42 | L2 阅读测验中反应格式移动产品分数分布且与文本组织交互：text-type × format F(11,723)=6.149, p<.005；cloze 在松散文本最优（x̄=42.3）而 open-ended/summary 在松散文本最差（x̄=33.4/30.9）——方向随文本类型翻转；效应按熟练度分层（高组 total F(2,255)=14.28** vs 低组 n.s.）。 | `METHOD-038`，PDF pp.10–12, 16–17, 26。 | `SUPPORTED`（本研究内）；迁移到作答 UI 为 `PROJECT-INFERENCE` | 754 名日本大学生，L2 阅读，cloze/open-ended/summary 纸笔格式，非 MC、非 UI 实现层；open-ended/summary 用日语 L1 作答。英语阅读测评领域的格式 × 材料一手证据，呼应 `B7` 的 task-contingent。 |
| UIE-43 | 反应格式移动产品分数信度（cloze α=.86~.90 vs open-ended/summary α=.69~.79），但 Spearman-Brown 等题数校正后可比（.91~.96 / .85~.90）——「格式固有地降低信度」为 `OVERSTATED`；格式 × 文本组织组合改变与外部语言能力标准的相关（association 松散文本 r=.54/.49 vs problem–solution r=.81/.75）——同一格式测到的构念内容随材料组织漂移。 | `METHOD-038`，PDF pp.10, 15, 19。 | α 差异存在 `SUPPORTED`；「格式固有降信度」`OVERSTATED`；构念漂移为相关证据 `SUPPORTED`（未做差异显著性检验） | 同上。格式间信度比较必须先控制题数/长度。 |
| UIE-44 | 内容等价、被试内反平衡下，反应格式移动产品估量：正确率层级 MC > open > error-correction/explain（ηp²=.44/.26/.18），Rasch 难度最大约 2 logit 位移（reading MC −.80 vs explain 1.02）；且高分格式（MC）测量质量最差（PSI .68–.73、misfit 25–48%），低分格式（explain）区分度最好——分数水平与测量质量解耦。 | `METHOD-039`，PDF p.1（摘要）, pp.4–6（Tables 1–2）。 | `SUPPORTED`（范围内） | 澳大利亚三年级英语母语生，纸笔 NAPLAN 退役题；格式级而非 UI/布局级；无过程指标。第二个独立的被试内格式实验（继 `B7`），且扩展到 IRT 难度/区分度。 |
| UIE-45 | 减少构念无关文字负荷（numeracy low-literacy MC）未提升成绩也未降低难度（43.7% vs 44.7% ns；−.76 vs −.69 logits ns）——住宿式需求缩减的阴性结果，与相关证据（Howard et al. 2017）方向相反。 | `METHOD-039`，PDF pp.1, 5, 7。 | `SUPPORTED`（范围内报告的 null） | 仅 numeracy、三年级；作者推测效应可能随年龄/复杂度出现；不能外推为「需求缩减永远无效」。 |
| UIE-46 | 投递模式（屏幕 vs 纸）移动阅读分数分布，纸优：between g=−0.21 [−0.28,−0.14]（k=56）与 within dc=−0.21 [−0.37,−0.06]（k=18）两设计独立同向；时间压力放大（限时 −0.26 vs 自定步调 −0.09，QB=4.12, p=.04）；文本类型调节（信息类 −0.27 / 混合 −0.30 vs 纯叙事 0.01）；纸优逐年递增（b=−0.01/yr, p=.03）；开放回看不改变模式效应（ns）；三法一致无发表偏倚。 | `METHOD-018`，PDF pp.1, 9–13, 15。 | `SUPPORTED`（方向须限定：I²=72/90、预测区间跨零；与 UIE-27 的 ACT 屏优方向相反，须并列） | 2000–2017 线性文本阅读/测验任务；mode-level 非 within-mode variant。timing moderator 为 UIE-26 的计时维度提供元分析级证据。 |
| UIE-47 | 投递模式移动阅读分数分布，方向由体裁决定：总体 g=−.25（k=33, n=2,799, p<.001）；说明文 g=−.32（屏幕显著更差）vs 叙事 g≈−.04（无差异）；literal −.33 / inferential −.26；年龄无调节。过程指标对模式敏感度不一致：阅读时间 ns（g=.08, I²=92.47）且方向可被作答通道颠倒（鼠标圈答 vs 铅笔圈答 → g=−1.72），校准显著恶化（屏幕更过度自信，g=.20, p=.002）。 | `METHOD-019`，PDF pp.19, 23–24, 26–29。 | `SUPPORTED`（范围内；作答通道颠倒时间方向为 `PARTIAL`——单研究异常值） | 2008–2018 随机分配实验元分析；操作投递模式而非作答 UI；屏幕侧 UI 细节不可控；排除残疾与学阅读者。与 UIE-48（叙事等价零）一致而非冲突。 |
| UIE-48 | 叙事文本、非速度语境下屏幕 vs 纸阅读理解统计上等价于零（d=0.10, p=.12，TOST ±0.25 界显著等价；k=32, N=2239）；而数字文本的多媒体/交互增强显著正向移动分数（d=0.37, p<.01, k=12，全为学龄儿童样本）。 | `METHOD-020`，PDF pp.12–15。 | `SUPPORTED`（叙事/非速度/元分析层面） | 1982–2021，11 国；不触及作答 UI/反应格式/导航/反馈变体。**第一轮「反向记录」的裁决**：Schwabe 不是 Delgado/Clinton 的简单反向，而是体裁调节限定——三者叙事子样本方向一致；方向张力应表述为任务/体裁/速度条件性（见 Class 4 节）。 |
| UIE-49 | 设备尺寸调制投递模式效应：手持设备 vs 纸的纸媒优势（between g=−0.113，within dc=−0.103）约为电脑为主元分析（g≈−.21~−.25）的一半；学业阶段（大学生 −0.227 vs 中小学 +0.057）与施测情境（单人 −0.230 vs 团体 +0.004）显著调节；平板 vs 电纸书、翻页 vs 滚动、时间压力在手持设备上均 null（滚动仅 5 效应量，低功效 null，不得当等价证据）；信度与标准化程度不调节。 | `METHOD-021`，PDF pp.1, 11–17。 | `SUPPORTED`（含脆弱性：between 效应含离群值即不显著、PI 跨零） | 平板/电纸书 vs 纸，阅读理解产品分数；94% 便利样本；不覆盖作答界面内布局/导航。 |
| UIE-50 | 投递模式总体效应小且不显著（随机 g=0.046, p=.706, I²=91.79%），但条件效应大且方向交替：限时 −0.468（p=.001）vs 自由阅读 +0.192（ns）；大学及以上 −0.432 vs 低年级正 ns；中国样本 −0.66 vs 外国 +0.279；交互型数字阅读 +0.959 vs 非交互 −0.172（ns）。 | `METHOD-022`，全文钉页见笔记。 | `SUPPORTED`（总体小效应 + 条件调节）；交互 affordance 分支 `PARTIAL`（二值编码、与学段/文本混杂） | 37 研究/46 效应；学生群体阅读理解任务；阅读场景非作答场景。任何「数字阅读总体更差/更好」的断言不受支持。 |
| UIE-51 | 作答格式恒定（两组都数字化作答）的 RCT 中，仅阅读呈现模态不同（纸 vs 屏 PDF）即移动阅读理解分数：屏组显著更低（标准化 β=−.216, p=.025，ΔR²=4%，控制词汇/字词阅读/前测/性别）；叙事/说明体裁不调节（p=.707）。作者未记录滚动/时间/疲劳等任何过程通道，明示机制不可判定。 | `METHOD-027`，PDF pp.4–5, 7。 | `SUPPORTED` | 挪威 72 名 10 年级学生，两篇线性文本（约 4 页），PISA 式 MC+CR，1 小时时限；n 小、分组不平衡 25:47。比 UIE-27 更直接地切中「阅读 UI 呈现本身是测量仪器的一部分」。 |
| UIE-52 | K-12 阅读 CBT vs PPT 模式效应平均为 null（排除速度化研究后 d_w=−.004, p=.782），但异质性显著（Q(41)=356.54；12/42 单研究显著）；被排除的 6 个速度化研究呈全部 CBT 更低的最大效应（d=−.31 至 −.56），其 CBT 逐项未作答率递增、9%–17% 学生自报时间不足；moderator：design、sample size、computer practice、delivery algorithm（linear > CAT）显著，grade level 不显著；等值义务是 test-specific（任何双模式测验须单独做可比性分析）。 | `METHOD-028`，PDF pp.12, 15–17。 | `SUPPORTED` | K-12 英语阅读，1988–2005 研究；模式级；缺失率为作者转述的自报，非逐题日志；重复测量相关缺失使 ES 为上界；「type of test」指测验类别非题目格式。第一轮元数据级「small/null」记录确认，但须以「平均零 + 高异质 + 缺失驱动离群」三件套替换简单表述。 |
| UIE-53 | 屏 vs 纸阅读理解纸优势 g=−0.21 [−0.38,−0.03], p=.02（47 ES/16 研究/n=4831，I²=73.2%）；速度无显著差异（g=0.48, p=.11）但 I²=93.4% 且 k=8——低功效高方差 null，不是等价证据；moderators（年份/国家/屏幕类型）均不显著（屏幕类型 df=4.78 低功效）。 | `METHOD-029`，PDF pp.1, 5–11。 | `SUPPORTED`（理解分数）；速度 null 与 moderator null `PARTIAL` | 2000–2016 研究，多为大学生说明性学术文本（11/17 大学生，属成人阅读媒介线，第一轮归入 K-12 组已修正）；表 5a 截距排版歧义以 CI 为准。 |
| UIE-54 | 儿童标准化阅读模式效应被试内实验（n=1139，IRT 2PL+PCM）：CBA 平均显著低于 PBA（p<0.05；30.5% 学生 PBA 高约 1 分 vs 13.6% CBA 高约 1 分）；效应随能力反向增大（Q1 d=0.31 → Q4 d=0.44，方向性假设被数据拒绝）；Q4 女孩效应最大（d=0.53 vs 男孩 0.33）；CBA 末尾缺失明显更多，且末尾连续 5 响应缺失按 null-response（未接触）而非错误计分——缺失的计分规则直接改变 estimand。 | `METHOD-030`，PDF pp.1, 6–9。 | `SUPPORTED` | 挪威 10 岁儿童，2015，限时 90 分钟；模式效应与能力/性别交互（形状改变非平移）；与 UIE-27 方向相反——模式效应大小与方向都不可先验，必须在本仪器上实测。 |
| UIE-55 | 幼儿段（1–8 岁，39 研究/n=1,812）无统一屏幕劣势：故事理解聚合 null（g=−0.07，CI 含 0），纸优仅存于纯数字化对照（k=10, g=−0.22）、学校情境（g=−0.28）与低 SES（g=−0.19）；设计特征是方向翻转器——story-related enhancements 翻向数字（g=0.17），内嵌词典促进词汇（g=0.49）却损害故事理解（−0.20）；儿童段方向与成人段不一致（VOC 偏数字；nonfiction 更偏数字 g=0.42，与 Delgado 相反）——跨段外推即 `OVERSTATED`。 | `METHOD-035`，PDF pp.1, 16–23。 | `SUPPORTED`（儿童段、元分析层面；数据质量注记见笔记——正文/表数值有小口径差，引用采保守口径） | 幼儿叙事图画书共读/听读；迁移到独立识字者与测评文本为 `PROJECT-INFERENCE`；行为证据为元分析内二手引用（`PARTIAL`）。 |
| UIE-56 | PISA 2009 数字阅读原始出处：页级导航指标在控制印刷阅读后仍有大额增量预测（相关页数 ΔR² 平均 23%、f² 均值 0.83、1 SD ≈ +66 分）；访问量–成绩为倒 U（−20 次访问 ≈ −64.6 分，+20 次仅 +30.5 分）；回访意义任务依赖（JOB SEARCH 回访为有益策略 vs SMELL Q1 额外回访与低能力相关）；产品分数与过程证据可解耦——不访问关键页仍得满分（IWANTTOHELP Q2 3.9%、SMELL Q1 <5%、JOB SEARCH Q2 0.7%），且猜答者能力显著更低。 | `METHOD-024`，PDF pp.98–103, 107, 109, 116–121。 | `SUPPORTED` | 19 国约 5 万名 15 岁学生；页级超文本 log；任务型页式导航，映射到单篇滚动文档为 `PROJECT-INFERENCE`。此卷即 B3/B5/B6 再分析的测量底稿（其回归系数属再分析层，UIE-04/19/20 不变）。 |
| UIE-57 | 大型机考的 log 采集与投递技术故障直接制造系统性缺失：官方自述页访问数据「因技术问题未能完全准确采集」；日本/丹麦整校技术故障使数字阅读学生响应率降至 56%/69%，且不做无响应调整、以 PV 补缺；6 种测试版本（3 cluster × 2 顺序）须按测试居中再按国家居中、另做标准化稳健分析结果方一致；导航未进 PV 模型故只能用 WLE。 | `METHOD-024`，PDF pp.94, 123, 230–231, 247–248。 | `SUPPORTED`（报告操作与官方披露） | PISA 2009 数字阅读；技术故障缺失是投递层事件，非随机；版本/题本组合变更必须显式纳入仪器合同。 |
| UIE-58 | 操作性大规模阅读 CBT 中，反应格式与题目表面特征系统性移动脱离与缺失：simple MC 的 rapid guessing 几率为 open-ended 的 OR=23.10（501+ 词刺激 OR=2.03；交互材料降 RG OR=0.785 但升 breakoff HR=1.104；hot spot/match 升 breakoff HR=1.28）；1.6% 作答被判 RG、另 1.6% 因 breakoff 缺失（7.4%/8.0% 学生）；RG 有效作答按对/错进入计分（分数效应可正可负），breakoff 缺失与非 reached 同处理——格式改变分数中猜测性作答的成分；RG 与 breakoff 跨国家相关 ≈0（筛查指标不可互换）；作者明确要求接口/设计变更（休息、跳过提醒、会话长度）引入前经 pilot/field-trial 实验验证。 | `METHOD-023`，PDF 物理页 15–16, 19–20, 22–23, 25（Table 3.1/3.2）。 | `SUPPORTED`（观察性关联，非随机操纵；计分处理细节部分依赖文本层外公式，笔记已标注） | PISA 2018 阅读 CBT，67 国 499,387 名学生；格式效应方向随格式–行为组合翻转，不可外推至布局/设备变体。与 `B7` 的任务权变呼应，并提供 estimand 污染路径（格式 → 被计分猜测）。 |
| UIE-59 | 强制作答设计把 item 缺失率结构性归零：PISA 2015 协作问题解决（CPS）UI 要求每题必答、不可跳过，117 题无 item 缺失——缺失可被设计消灭，代价是丧失缺失率的行为信息。**并修正第一轮归属**：「65/103 题模式等价、38 题难度漂移」的量化等值结果不在本卷（全文逐项搜索确认）；本卷仅承载「field trial 用于建立 CBT/PBT 等价」的过程声明（物理页 28–29），量化结果真实出处为 PISA 2015 Technical Report（OECD 2017b，未获取）。 | `METHOD-025`，PDF 物理页 28–29, 50–51, 57, 68, 86–88, 175。 | `SUPPORTED`（设计事实）；「65/103」数字未一手核验，不作负载使用 | CPS 交互机考专属，不可外推；agent 替换真人仅小幅移动分数（统计显著但实际无关，转述未出版手稿，`PARTIAL`）；自报 ICT 经验解释机考成绩方差仅 0.6%、方向不明。 |
| UIE-60 | 住宿效应实证（过程数据）：延长时间（ET）住宿使用使 SWDs item 正确率 +3.5–4.2pp（logit/IPW/DR 三模型一致 p<.01）；TTS 只在未用 ET 的 SWDs 中正相关（+2.4–2.7pp）、对 ET 用户无效应——住宿组合改变「特征—分数」关系，standard vs accommodated 路径的指标可比性不能假定；equation editor 使用与正确率全模型显著负相关（SWDs DR −.213、SWODs DR −.341）；仅 31.2% ET 合格 SWDs 实际使用——资格 ≠ 使用；「使用」依赖显式阈值（≥2 秒/≥1 句），阈值即数据质量筛查。 | `METHOD-017`，PDF pp.3, 5–12。 | `SUPPORTED`（观察性；残余内生性不可排除，作者自认） | 八年级数学、低 stakes；机制未测。为第一轮 Class-4 段的推论（住宿移动子群过程分布）提供钉页实证。 |
| UIE-61 | 语言测评领域编辑共识（特刊 Post-Script）：辅助工具与被测构念交互（multiple listening 可把 gist item 变成 detail item）；是否设时限本身是构念决策；无障碍功能间交互——增大字体可破坏屏幕文本布局并对部分考生不利（与 UIE-24 直接交互）；工具菜单选项本身可能构成额外测试挑战（choice burden）；工具 uptake/激活的实证理解有限是领域自认的开放问题。 | `METHOD-026`，PDF pp.2–3（打印 1001–1002）。 | `PARTIAL`（资深编辑的框架主张，非实证测量；听力模态） | Language Testing 40(4) 特刊结语；不支持任何方向性/量级实证前提；把审计 Class-1 的 `UNRESOLVED` 升级为「领域共识的开放问题」。 |
| UIE-62 | 延长时间住宿（30→90 min 可用）在操作性大样本数字测试中未移动 item 测量参数：no-use 组 0/15 项 DIF，use 组 1/15 项（δ=−0.226, small），Poly-SIBTEST 两轮确认；「使用」的操作化是粗代理（duration>30min 二分，无法区分额外时间用途）；约 17%（1010/6011）有资格者未使用（自愿、self-regulation 与 stakes 依赖、随测试进程下降）；焦点组边际分数显著更低但 DIF 极少——分数分布移动与 item 测量等价是正交事实。 | `METHOD-031`，PDF pp.1, 5–11。 | `SUPPORTED`（范围内）；「住宿非必要」的作者推断为讨论级，不作事实采用 | NAEP 2017 八年级数学、低 stakes、单 block；非阅读、非 scale 分布层、非高 stakes；**不得**被引用为「时间住宿测量中性」的普遍证据。仪器效应必须按层级（item 参数 vs scale 分布）表述。 |
| UIE-63 | 同一任务内普适提供的 UI 住宿路径（音频朗读 + 额外时间）零分数移动（boost 组间 t(90)=−.782, p=.44，无 differential boost，信度跨条件稳定 α .79–.86），但移动有损伤子群的构念无关方差结构（fluency–comprehension 相关 r=.26, p=.048 → r=.12, p=.220）；住宿使用量 person-dependent（SWFI 3.01 次 vs SWOFI 2.38 次）；偏好（98% 认为易用）、有用性评价（53%）与实际使用（M=3.01 次）三方分离。 | `METHOD-036`，PDF 物理页 6–8。 | `SUPPORTED`（本研究内） | 131 名 12 年级学生、非 speeded、高可及性平台（TAMI 2.8）、自愿使用、NAEP 公开题 MC；不可外推到 speeded 测试；过程分布移动与产品分布不动可以并存。 |
| UIE-64 | log 派生的「支持使用率」无稳定真值：三种操作化（点击计数/至少一次/使用题目数）产生不同排序，点击计数把少数人高频使用呈现为广泛使用；清洗阈值（同支持单题 >10 次动作删除）删去约 4% 交互且可能含有效反应；供给 ≠ 参与——全员开放的 universal support 仅约 37–52% 考生至少用过一次，获批 TTS-entire 也有 16–39% 获批者全程未用（获批者中至少一次比例 61–84%——「低使用」须限定）；使用行为测验内前载且跨页衰减。 | `METHOD-037`，PDF 物理页 6, 8–10, 14, 19–21。 | `SUPPORTED`（描述性；熟悉度解释 `PARTIAL`——作者假设未检验） | 单一州六年级 Smarter-Balanced 衍生 CAT（ELA+数学），2018 春；无分数数据。第一轮 W4 行把本文概括为「低实际使用率」证据——须带上述限定，否则构成 `OVERSTATED`。任何「X 用了多少」的 UI/无障碍指标必须先固定操作化并报告敏感性。 |

### Class 1 — 可用性 / 偏好主张

本地语料确立的只有方法词汇。`UIB-009`、`UIB-010`、`UIB-001`（UIE-21）确立可用性问题在行为上可检测——用户遇到可用性问题时会发散，日志筛查能标记异味型模式。这只支撑把可用性筛查纳入仪器 QA，别无其他。

开放网络检索补充的是规范性地板而非实证证据。WCAG 2.2 SC 2.5.7 / 1.4.10 / 2.2.1 / 2.5.8（UIE-23..25）从标准原文引用——约束 Web 投递作答 UI 能做什么，但它们是 Web 内容标准，不是测评特异标准，且对偏好、易用或测量后果一无所言。

第二轮新增的是**间接操作性证据**，仍非可用性测量：语言测评领域资深编辑自认工具 uptake/激活的实证理解有限、工具选项本身可能构成额外测试挑战（UIE-61，`METHOD-026`）——本类的实证缺口是**领域共识级**开放问题，不是本地语料不足的产物；普适住宿平台上偏好（98% 认为易用）、有用性评价（53%）与实际使用（M=3.01 次）三方分离（UIE-63）；操作性州考中供给 ≠ 参与，universal support 仅 37–52% 考生至少用过一次（UIE-64）；交互辅助 99% 自发采用但测量效应条件化——「被使用 = 测量中性」不成立（UIE-38）。

**仍未确立**：没有本地持有或开放可得的来源研究阅读/测评 UI 中的可用性、易用性、满意度或偏好测量；没有来源把「用户偏好变体 X」与「变体 X 测得更好」分离；没有来源显示可用性改进是测量中性的。阅读测评 UI 的实证可用性证据保持 `UNRESOLVED`。

### Class 2 — 行为改变主张

本类仍是证据最充分的一类，且第二轮大幅加强。`B7`（UIE-01）是被试内随机实验：反应格式改变事件计数、完成时间与情境定义停顿，D&D 优势方向在排序与分类任务间翻转。`B3`（UIE-04）跨 17 国显示任务访问需求同时移动导航量与导航的预测含义。`C6`（UIE-05）显示布局改变眼–鼠标联合分布（p < .0001）。`B1`（UIE-07）显示反馈仪表盘重组交互序列；`B10`（UIE-08）与 `C3`（UIE-09）显示指导语措辞与题目表面特征调节行为；`C4`（UIE-06）是 UI 凭空制造行为–可观察性耦合的极限演示；`B2`（UIE-03）补充布局邻近混淆；`METHOD-014`（UIE-29）显示媒介本身改变存在哪些过程行为（纸/数字划线量与方向相反）。

第二轮新增：`METHOD-016`（UIE-31/32/34）把 `E6` 的编辑断言升为一手——表面特征操纵移动策略分布、停顿、动作数与拖时间，且屏上距离/滚动需求改变交互时序；`METHOD-032`（UIE-35/36）在三种阅读理解任务中一致复现格式 → 执行层过程指标（时间 d=−0.62、点击 d=−1.13），并证明事件最小集约束不保证执行层等价；`METHOD-033`（UIE-37/38）是本地语料第一个布局操纵因果实验——空间整合降解题时间、交互辅助的采用与测量效应解耦；`METHOD-023`（UIE-58）在操作性 50 万人阅读 CBT 中显示格式是脱离行为的最强预测因子（simple MC 的 RG OR=23.10）；`METHOD-024`（UIE-56）提供导航任务依赖性的原始出处级证据（回访意义随任务翻转）；`METHOD-034`（UIE-40）划定效应的粒度边界——标签措辞级变化在 N=206,153 中零效应。

必须随这些结果同行的反向发现：`B7` 分类任务中 D&D 无优势且 click-on-grid 在时间与事件上更优——格式效应是任务权变的；`B3` 低需求任务中更多访问仍正向预测成绩，「更多导航 = 更差」不是可用规则；`B2` 导航簇为事后标注（其印刷 η² = .11/.25 与自身 F/df 内部不一致，B 组深读报告重算 ≈ .011/.025——此处只保留显著性与 ~55 分簇对比）；`METHOD-016` 的纯布局变体只动过程指标不动分数（UIE-32）；`METHOD-034` 的零效应不得升级为「格式无效应」的普遍结论。

**本类未确立的**：没有本地持有研究在英语阅读理解作答 UI 中操纵布局、导航方案或反馈并测量对自然阅读行为的因果效应。到我们双栏可滚动篇章 + 单题面板设计的每一次迁移都是 `PROJECT-INFERENCE`——包括从 B7 的 Story/Questions 标签页到我们左/右栏的看似合理迁移；`METHOD-033` 把「布局改变行为」升为跨域 `SUPPORTED`，但它是几何 MC 而非阅读。

### Class 3 — 仪器信度与缺失主张

已确立：缺失与完整性是行为与设计依赖的，不只是技术噪声。`B2`（UIE-11）在导航指标上丢了 66.3% 的被分配学生；`B7`（UIE-12）记录了系统崩溃与泄露驱动的排除、24% 非随机缺失与分页压缩行为空间；`C2`（UIE-13）显示指针缺席是常态（58.8% 时间）；`E6`（UIE-14）概括传感器通道的严重不可预测丢失/偏倚；保留 `visibility_changed`/`layout_changed` 为语义事件（UIE-15）是与上述证据一致的 `PROJECT-INFERENCE`。`METHOD-010`（UIE-22）确立指针流的数据质量筛查角色（非认知角色）；`METHOD-012`（UIE-27）把同一教训扩展到产品层——题目遗漏本身模式依赖（纸笔 11.1% vs 在线 8.3%）。

第二轮新增四条独立证据链：(a) **产品层缺失的格式/位置/时段依赖**——`METHOD-023`（UIE-58）：RG 与 breakoff 两类缺失方向相反、计分处理不同、筛查指标跨国正交；`METHOD-028`（UIE-52）：速度化 → 逐项未作答递增 → 最大分数效应同源；`METHOD-030`（UIE-54）：CBA 末尾缺失更多，null-response 计分规则直接改变 estimand；`METHOD-025`（UIE-59）：强制作答把缺失率设计归零、同时丧失其信息量。(b) **过程通道完整性的仪器层失效**——`METHOD-024`（UIE-57）：官方自述 log 采集不准、整校故障致 56%/69% 响应率、PV 补缺、6 版本居中校正；`METHOD-016`（UIE-33）：4.8% 捕获失败整人剔除、策略估计仅基于 65% 序列。(c) **筛查层的失败模式**——`METHOD-034`（UIE-41）：单通道筛查严重过度标记且阈值敏感；`METHOD-033`（UIE-39）：时间指标分布由显式清洗决策塑造；`METHOD-037`（UIE-64）：使用率操作化翻转排序、清洗阈值携带构念代价；`METHOD-031`（UIE-62）：「使用」代理只能区分超时与否。(d) **信度随格式变化**——`METHOD-038`（UIE-43）：α 差经等题数校正消失；`METHOD-039`（UIE-44）：PSI/misfit 随格式变化，分数水平与测量质量解耦。

**本类未确立的**：没有本地来源测量阅读作答 UI 的事件完整性、顺序稳健性、重放保真度或跨浏览器/跨设备可比性；没有量化 resize、缩放、后台标签、重复或乱序事件如何侵蚀重建。本语料中已发表的仪器论文自己就省略重放关键细节（`C6` 未报告鼠标采样率与注视提取算法——PDF pp.3–5）。我们仪器的信度因此由文献 `UNRESOLVED`，必须由 `BENCH-E0` 工程证据确立——这正是 `MEASUREMENT_VALIDATION_FRAMEWORK.md` 已声明的合同；第二轮证据补充了合同义务：快速猜测/离群/清洗规则必须预固定（UIE-39/41），缺失的计分规则（null-response vs 错误）必须作为仪器决策记录（UIE-54）。

### Class 4 — 学习 / 构念与 estimand 主张

已确立：`B7`（UIE-02）是最切题的单一结果——反应格式在改变过程分布的同时移动产品分数（drop-down OR = 1.40），即格式移动了 estimand；`E6`（UIE-10，及 PDF p.2 的 process data ≠ response processes 区分）提供框架：过程指标是需要与产品分数同等验证的显性痕迹，显示设计是具名的构念无关方差来源；`STANDARD-001`（UIE-18）提供规范框架；`E8`（UIE-16）显示预期题型也不保证预期作答过程；`E7`（UIE-17）显示轨迹与言语通道不可互换；`B5`/`B6`（UIE-19/20）显示同一导航行为跨能力水平与任务透明度携带不同构念含义。

**第二轮对「方向张力」的裁决**（第一轮遗留的最大未决）：投递模式对阅读产品分数的效应是**任务/体裁/速度/人群条件性的**，三档方向并存且各有全文级锚点——(i) 说明文/限时/成人实验语境纸优：Delgado g=−0.21（UIE-46）、Clinton 说明文 g=−.32（UIE-47）、Kong g=−0.21（UIE-53）、Mangen RCT β=−.216（UIE-51）；(ii) 叙事/非速度语境统计等价于零：Schwabe d=0.10 TOST 等价（UIE-48），与 Clinton 叙事子样本 g≈−.04 一致；(iii) 高速度操作性标准化考试屏优：ACT d=.16–.22（UIE-27）。边界条件进一步细化：K-12 平均 null + 高异质（UIE-52）、儿童标准化语境屏劣且与能力/性别交互（UIE-54）、幼儿段完全条件化（UIE-55）、总体 null + moderator 方向交替（UIE-50）、设备尺寸梯度（UIE-49）。第一轮的「反向记录」（Schwabe）由此裁决为体裁调节限定而非矛盾。**任何单方向模式断言都不受支持；「仪器变化 ⇒ estimand 变化」的存在性前提反而更稳。**

格式级 estimand 移动现在有五个独立证据：`B7`（UIE-02，ELA 八年级被试内）、`METHOD-016`（UIE-31，成人数学组间，构念相关/无关特征方向不同）、`METHOD-038`（UIE-42，L2 阅读，与文本组织交互、按熟练度分层）、`METHOD-039`（UIE-44，三年级，IRT 难度最大 ~2 logit）、`METHOD-032`（UIE-35，西语阅读，平均 null 掩盖低表现亚组 d=0.57）。阴性对照同样入表：`METHOD-034` 的标签粒度零效应（UIE-40）与 `METHOD-039` 的需求缩减 null（UIE-45）。

住宿/无障碍层的实证缺口大部分闭合：`METHOD-017`（UIE-60）——ET 移动 SWD 分数、TTS×ET 交互、资格 ≠ 使用（31.2%）；`METHOD-031`（UIE-62）——延长时间未移动 item 参数（DIF 层 null）；`METHOD-036`（UIE-63）——零分数移动但移动构念无关方差结构；`METHOD-026`（UIE-61）——工具 × 构念交互的编辑框架。三篇合在一起给出**层级表述义务**：住宿效应在 item 参数 / scale 分布 / 方差结构三层可各自独立出现或不出现，「住宿移动/不移动分数」的裸断言两类都不可接受。WCAG 交互点保留并获实证支撑：为 D&D 的过程优势（UIE-01/02）选拖拽触发 SC 2.5.7（UIE-23）——单指针替代路径本身即另一种反应格式，携带自己的过程与可能的产品分布（UIE-31/35 直接支持），两路径的过程指标可比性不能假定、必须实测。

反向约束与刹车：`B7` 的分数结果与「更少交互 = 更干净测量」的天真规则相反；`E8` 证据为 n = 5 单编码者无 IRR；`STANDARD-001` 设定义务但不操作化 Web-UI 无障碍标准——WCAG 2.2 提供规范地板（UIE-23..25），测评特异的操作标准仍只有框架级文献（UIE-61）；`METHOD-039` 显示高分格式测量质量最差（UIE-44），「分数更高的格式 = 更好的测量」同样 `OVERSTATED`。

**本类未确立的**：没有本地持有来源证明阅读 MC 作答 UI 的**具体变体**（同模式内的布局/导航/反馈变体）改变所测构念或技能估计的 estimand，也没有量化无障碍适配在阅读测评中的此类效应。「我们的 UI 变体构念等价」目前无法从本地证据证伪，在 H2-gated 变体研究之前不得断言。

## 局限

- 无障碍覆盖：标准层（UIE-23..25，含逐字快照）与住宿实证层（UIE-60..64）已建立，但 ATAG/UAAG 仍未覆盖；队列 #12（Lovett & Lewandowski 2015 的 universal design for assessment 书章）无机构权限可获取，经影响评估标记为不可获取——其框架性内容由 `STANDARD-001`（UIE-18）与 `METHOD-026`（UIE-61）承担，实证落点由 UIE-60/62/63/64 覆盖，缺口对本审计结论影响小。Class-1 可用性/偏好实证保持 `UNRESOLVED`，且为领域共识级缺口（UIE-61）。
- 开放网络覆盖仍不完整：OpenAlex 缺席 2026-08-15 检索（当日根因：共享代理出口 IP 的匿名日额度；`OPENALEX_API_KEY` 已于 2026-08-16 配置并验证，同题 OpenAlex 复检轮留作可选 TODO）；Semantic Scholar 的 S2/S4 查询当日被限流；Unpaywall 未查询（需个人邮箱）；Google Scholar 与 CNKI/万方自动化为常设边界。CNKI/万方人工检索轮（2026-08-16）已完成并评估为近阴性，但 Q3/Q4/Q5 因反爬/未登录失效是**通道限制**，不能解读为「中文无相关文献」；补强路径为 `METHOD-011` 参考文献引文追溯。
- 元分析样本重叠：Delgado 2018（UIE-46）、Clinton 2019（UIE-47）、Kong 2018（UIE-53）、Salmerón 2024（UIE-49）、Li & Yan 2024（UIE-50）的纳入窗口部分重叠，其效应量不可简单相加；本审计并列引用而非聚合。
- B 层导航证据（B2/B3/B5/B6）是 PISA 超文本页级导航（原始出处 `METHOD-024` 确认全部为页级 log 指标）；把「页访问」映射到单篇可滚动文档的「段落/区域可见性」是未验证的 `PROJECT-INFERENCE`。
- C 层布局证据是静态 SERP，非滚动长文阅读；没有本地论文研究独立滚动双栏文档上的光标行为。
- 可用性层来源（UIB）是跨域的；它们支撑检测方法，不支撑阅读 UI 设计选择。
- `B10` 的表级 β 钉点在结果正文级核验，未对 Tables 6–7 逐格复核；具体系数按报告级对待。
- 「65/103 题模式等价、38 题难度漂移」的 PISA 2015 field-trial 量化结果经全文核验不在 `METHOD-025`（Vol. V）中，真实出处 PISA 2015 Technical Report（OECD 2017b）未获取；该数字不作负载使用，获取该报告为可选后续。
- 第二轮提取由并行子代理完成，每篇笔记含提取验证记录；个别论文存在文本层不可提取的公式/图形（如 `METHOD-023` 的 RG 阈值公式）与原文排印错误（笔记中逐处标注），引用这些细节前须回到 PDF 原文。

## 获取队列

第一轮定位的 25 项队列：24 项已人工下载、核验、入库（`METHOD-016..039`）并全文读毕（逐篇提取笔记 `ui-instrument-effects-evidence-audit/METHOD-016..039.md`）；唯一未获取项 #12（Lovett & Lewandowski 2015）经影响评估决策为不可获取（2026-08-16）。CNKI/万方人工检索轮已完成（评估见上文方法节与 human-tasks 文件）。WCAG 2.2 归档形式经两轮决策定稿（supersession 记录见 human-tasks「已决策事项」）：规范全文（W3C Recommendation 12 December 2024，单文件 HTML）登记为 `STANDARD-003` 入 catalog——`media_type` 校验为通用 MIME 正则、magic 检查仅覆盖 pdf/zip/json，`text/html` 可直接登记，无需工具链改动；4 条引用 SC 逐字文本已对归档件核验一致（2026-08-16）。登记与完成状态的 owner 是 [`reports/research/human-tasks/wayfinder-5-ui-instrument-effects.md`](human-tasks/wayfinder-5-ui-instrument-effects.md)；两个 API key 配置任务在 [`human-tasks/setup.md`](human-tasks/setup.md)。第一轮的 INTERIM 限定随队列清空（24/25 + #12 决策关闭）解除。

## 决策含义

面向 Wayfinder 目标（baseline UI 变体冻结与 `BENCH-E0` 仪器合同）：

1. **把 UI 变体选择当仪器设计，不是 UX 偏好。** `B7`（格式同时移动过程与产品）+ `STANDARD-001`（公平 = 对所有考生同一构念）意味着任何冻结后变体变更都是潜在 estimand 变更，必须版本化为仪器变更。第二轮的格式簇（UIE-31/35/42/44）与模式簇（UIE-46..55）把此前提从两个单点证据升级为跨人群、跨任务、跨层级的稳定模式。baseline 变体必须在 `BENCH-E0` 前冻结，其事件词汇、布局常量与反馈面记录为仪器合同。
2. **按任务类型对照假设认知过程选择反应格式与作答 affordance 细节**，并记录每种格式的最小必需事件数（`B7` 的 superfluous-event 构造，PDF p.6），使过程指标可计算、可比较；注意 `METHOD-032`（UIE-36）证明最小事件数相等不保证执行层等价——合同还需定义冗余/纠错事件的记录口径。
3. **仪器合同必须把 `visibility_changed`、`layout_changed`、resize/缩放、分页/滚动上下文记录为一等事件**，`BENCH-E0` 必须测量跨浏览器与设备的事件完整性、缺失与重放保真度。文献不能替代：语料确立这些因素重要（UIE-11..15, 33, 39, 57）但不含阅读 UI 信度测量。第二轮补充合同义务：快速猜测/离群/清洗规则预固定（UIE-39/41），缺失的计分规则（null-response vs 错误）显式记录（UIE-54），多源筛查而非单通道阈值（UIE-41/58）。
4. **预 H2 主张预算。** 允许：工程级主张（重放保真、事件完整性、schema 不变量）与开发者仪器行为分布检查。不允许：关于学习或认知的可用性优越主张、无障碍合规主张、跨变体构念等价主张——这些需要 H2-gated 变体研究 + `STANDARD-001` 公平性框架 + `E6`/`E8` 作答过程验证。新增：任何方向性的模式/格式效应断言（「X 变体提高/降低分数」）同样超出预算——第二轮证据显示方向是任务/体裁/速度/人群条件性的（UIE-46..55），只能先在本仪器上实测。
5. **缺失政策**：把缺席的指针/滚动/导航信号当作有设计依赖成因的默认状态（UIE-11, UIE-13），绝不当可插补的仪器错误，也绝不当脱离投入证据（`C2` 不活跃；`C8` 停顿–投入弱关联，见 C 层报告）。第二轮补充：产品层遗漏同样是模式/格式/位置依赖的（UIE-27/52/54/58），且「把缺失设计成零」（UIE-59）是放弃缺失率信息量的设计选择——缺失的定义、阈值与计分处理都是仪器合同条目。
6. **把 baseline UI 的 WCAG 派生约束冻结为仪器合同的一部分**：任何拖拽操作（含拖拽作答或排除/恢复 affordance）必须附带单指针、免拖拽替代路径（SC 2.5.7，UIE-23），且替代路径本身即另一种反应格式，其过程/产品分布可比性须实测（UIE-31/35）；双栏布局必须在 320 CSS px 等效宽度满足重排（SC 1.4.10，UIE-24）；任何时限须遵循 SC 2.2.1，援引其「essential」例外本身是构念主张（速度属于构念）须记入仪器合同；指针目标至少 24×24 CSS px（SC 2.5.8，UIE-25）。
7. **住宿与可比性义务（新增）**：住宿/无障碍变体的测量效应是层级依赖的——item 参数（UIE-62）、scale 分布（UIE-27/60）与构念无关方差结构（UIE-63）三层须分别测量分别表述；「可用 ≠ 被用」，任何住宿路径须实测并报告使用率及其操作化定义（UIE-60/64）；住宿组合会改变特征–分数关系（UIE-60 的 TTS×ET 交互），standard 与 accommodated 路径的指标可比性不能假定。
8. **计时政策是构念决策（新增）**：时限调节模式效应（UIE-46 的限时 −0.26 vs 自定 −0.09；UIE-50 的 −0.468 vs ns），速度性是 TME 的具名来源（UIE-26），SC 2.2.1 的 essential 例外是标准层对应（UIE-25），领域编辑共识同样把「是否设时限」列为构念决策（UIE-61）。baseline 是否限时、限时值与计时显示方式必须在仪器合同中显式声明并论证。

## 已核对文件

本审计打开并钉页的 PDF（定位为 PDF 物理页）：

- `sources/library/papers/literature/a-e/B/B1_2025_Maimaiti_GamifiedSRL.pdf`（pp.3, 5–7, 9–11）
- `sources/library/papers/literature/a-e/B/B2_2022_He_DTW_Navigation.pdf`（pp.5, 10）
- `sources/library/papers/literature/a-e/B/B3_2015_Naumann_OnlineReadingEngagement.pdf`（pp.7–13）
- `sources/library/papers/literature/a-e/B/B4_2023_Soyoye_SequenceMining.pdf`（pp.21, 24）
- `sources/library/papers/literature/a-e/B/B5_2022_Naumann_StrategyKnowledge.pdf`（pp.4, 8–9）
- `sources/library/papers/literature/a-e/B/B6_2025_Naumann_SkilledComprehenders.pdf`（pp.9, 11–14）
- `sources/library/papers/literature/a-e/B/B7_2026_Arslan_ResponseFormatsCognitiveProcesses.pdf`（pp.1, 4–9）
- `sources/library/papers/literature/a-e/B/B9_2023_Arslan_InterpretingPausesProcessData.pdf`（pp.1–3）
- `sources/library/papers/literature/a-e/B/B10_2026_Lyu_PurposeInstructionsTaskModels.pdf`（p.1；Tables 6–7 附近结果正文）
- `sources/library/papers/literature/a-e/B/B11_2025_Wijerathne_RereadBeforeAnswer.pdf`（pp.6, 9）
- `sources/library/papers/literature/a-e/C/C2_2012_Huang_UserSeeUserPoint.pdf`（pp.2, 5–6, 9）
- `sources/library/papers/literature/a-e/C/C3_2020_FernandezFontelo_QuestionDifficulty.pdf`（pp.8–9）
- `sources/library/papers/literature/a-e/C/C4_2024_Wilcox_MouseTrackingReading.pdf`（pp.1–2）
- `sources/library/papers/literature/a-e/C/C6_2025_Latifzadeh_SERPDataset.pdf`（pp.3, 5–6）
- `sources/library/papers/literature/a-e/D/D5_2024_Rebmann_TaskLevelEvents.pdf`（pp.2–3）
- `sources/library/papers/literature/a-e/E/E6_2023_Lindner_ProcessDataBlackBox.pdf`（pp.2, 5–7）
- `sources/library/papers/literature/a-e/E/E7_2023_Fan_SRLTraceThinkAloud.pdf`（p.1 及结果表）
- `sources/library/papers/literature/a-e/E/E8_2018_Severino_ReadingComprehensionValidation.pdf`（pp.10–11）
- `sources/library/papers/literature/ui-interaction/UIB-001-amused-a-multi-modal-dataset-for-usability-smell-identification.pdf`（p.1，`ABSTRACT-ONLY`）
- `sources/library/papers/literature/ui-interaction/UIB-009-detecting-usability-problems-in-mobile-applications-on-the-basis-of-dissimilarity.pdf`（p.1）
- `sources/library/papers/literature/ui-interaction/UIB-010-gui-information-based-interaction-logging-and-visualization-for-asynchronous-usabi.pdf`（p.1，`ABSTRACT-ONLY`）
- `sources/library/standards/2014_AERA_APA_NCME_Testing_Standards.pdf`（PDF pp.59–60, 62, 67–68, 73）
- `sources/library/papers/methods/2022_Pokropek_MouseChase_CursorCareless.pdf`（`METHOD-010`，2026-08-15 获取；pp.2, 4, 6）
- `sources/library/papers/methods/2023_Chen_TestModeEffect_Review.pdf`（`METHOD-011`，2026-08-15 获取；pp.1–3, 12–13）
- `sources/library/papers/methods/2020_Steedle_ACT_Mode_Comparability.pdf`（`METHOD-012`，2026-08-15 获取；pp.2, 8, 10, 13–15）
- `sources/library/papers/methods/2021_Jiang_NAEP_DragDrop_ProcessData.pdf`（`METHOD-013`，2026-08-15 获取；pp.1–2）
- `sources/library/papers/methods/2020_Goodwin_DigitalVsPaper_ReadingProcesses.pdf`（`METHOD-014`，2026-08-15 经 ERIC EJ1260522 获取；p.1）
- `sources/library/papers/methods/2016_DePascale_Device_Comparability.pdf`（`METHOD-015`，2026-08-15 经 ERIC ED610777 获取；pp.8, 15, 20）
- 第二轮（2026-08-16 全文逐页提取，逐篇钉页笔记见 `ui-instrument-effects-evidence-audit/` 同名目录）：`METHOD-016`（2020_Arslan_DragDrop.pdf）、`METHOD-017`（2025_Ogut_UniversalByDesign.pdf）、`METHOD-018`（2018_Delgado_DigitalVsPaper.pdf）、`METHOD-019`（2019_Clinton_DigitalVsPaper.pdf）、`METHOD-020`（2022_Schwabe_ScreenVsPrintComprehension.pdf）、`METHOD-021`（2024_Salmeron_HandheldVsPaper.pdf）、`METHOD-022`（2024_Li_DigitalVsPaper.pdf）、`METHOD-023`（2024_OECD_ItemDisengagement.pdf）、`METHOD-024`（2011_OECD_StudentsOnLine.pdf）、`METHOD-025`（2017_OECD_CollaborativeProblemSolving.pdf）、`METHOD-026`（2023_Taylor_LanguageAssessmentAccommodations.pdf）、`METHOD-027`（2013_Mangen_PaperVsScreen.pdf）、`METHOD-028`（2008_Wang_TestModeEffects.pdf）、`METHOD-029`（2018_Kong_ScreenVsPaper.pdf）、`METHOD-030`（2020_Stole_PaperVsScreen.pdf）、`METHOD-031`（2024_Witmer_ExtendedTimeScoreComparability.pdf）、`METHOD-032`（2021_Ponce_DragDropResponseEffects.pdf）、`METHOD-033`（2022_Moon_SplitAttention.pdf）、`METHOD-034`（2024_Ulitzsch_ScaleFormatCIER.pdf）、`METHOD-035`（2021_Furenes_PaperVsScreen.pdf）、`METHOD-036`（2023_Dembitzer_UniversalAccommodations.pdf）、`METHOD-037`（2021_Lee_EmbeddedAccommodationUsage.pdf）、`METHOD-038`（2002_Kobayashi_MethodEffectsTextFormat.pdf）、`METHOD-039`（2020_Woodcock_ItemFormatEffects.pdf）——均位于 `sources/library/papers/methods/`
- WCAG 2.2（W3C Recommendation）SC 2.5.7 / 1.4.10 / 2.2.1 / 2.5.8——canonical URL `https://www.w3.org/TR/WCAG22/#dragging-movements`、`#reflow`、`#timing-adjustable`、`#target-size-minimum`；规范全文归档为 `STANDARD-003`（Recommendation 12 December 2024 单文件 HTML，2026-08-16 经 TR 端点重取，4 条 SC 逐字文本核验一致；首轮 2026-08-15 曾经 `w3c/wcag` GitHub 源仓库获取）。

项目文档（作为索引/框架阅读，不作为来源主张的证据）：`CONTEXT.md`、`reports/project_state/CURRENT_STATE.md`、`reports/project_state/RESEARCH_QUESTIONS.md`、`sources/catalog.yaml`、`reports/literature/a-e/group-B-deep-reading.md`、`group-C-deep-reading.md`、`group-D-deep-reading.md`、`group-E-deep-reading.md`、`reports/literature/ui-interaction/A_tier_notes.md`、`reports/research/existing-literature-validation-audit.md`，以及只读参考 `reports/synthesis/SYSTEM_DESIGN.md`、`MEASUREMENT_VALIDATION_FRAMEWORK.md`、`OBSERVABILITY_TARGETS.md`、`LITERATURE_SYNTHESIS.md`。

## 剩余审计债

- **within-mode 变体等价性仍无法证伪**：没有本地来源证明阅读 MC 作答 UI 的具体变体（布局/导航/反馈，同模式内）改变所测构念或技能估计 estimand；「我们的 UI 变体构念等价」在 H2-gated 变体研究前不得断言。这是本票答案的核心边界：文献确立了「仪器变化可以移动 estimand」的存在性与条件结构，但我们自己变体的等价性只能由 BENCH-E0 工程证据 + H2 真人证据确立。
- **Class-1 可用性/偏好实证 `UNRESOLVED`**（领域共识级缺口，UIE-61）；WCAG 合规 ≠ 可用无障碍；ATAG/UAAG 未覆盖。
- **#12 Lovett & Lewandowski 2015 不可获取**（决策与影响评估见「获取队列」节）；如未来获得权限按 supersession 增补。
- **PISA 2015 Technical Report 的模式效应量化未获取**（「65/103 题」数字的潜在真实出处；可选获取，不阻塞结论）。
- **OpenAlex 同题复检轮**（可选 TODO；key 已配置）。
- B 层页级导航 → 区域可见性迁移与 C 层 SERP → 双栏阅读迁移保持 `PROJECT-INFERENCE`，需 `BENCH-E0` 加 H2-gated 真人证据才能实证约束变体选择。
- 中文文献覆盖停在 `METHOD-011` 综述层（CNKI 轮近阴性但 Q3–Q5 通道失效）；如需更强中文实证，走 `METHOD-011` 参考文献引文追溯。
