# Phase 0 题目与过程数据来源审计

**审计日期：** 2026-08-14
**范围：** PELDiaG、2022 CSE 阅读推理研究、2026 Du/Shen/Ma GenAI Q-matrix 研究、Jin & Liu hybrid C-DA，以及 PISA 2012、ePIRLS 2016、PIAAC 1st Cycle、NAEP。
**证据规则：** 仅把 DOI 落地页、出版商正文、作者机构仓储、政府/国际组织项目页和可信 OA 仓储视为定论来源；迁移包、搜索摘要和二手转述只用于发现线索。本文不把“题名相近、作者相同、样本量相同”自动解释为同一测验或同一响应矩阵。

## 状态标签

- **CONFIRMED**：一手来源直接陈述，或合法取得的原文可直接核验。
- **INFERENCE**：多个一手事实相容，但来源没有直接陈述该关系；不得在论文中写成事实。
- **NOT FOUND**：截至审计日，限定的一手来源范围内未发现；不等同于资产不存在。

## 结论先行

1. **2022 → 2026 的“单一直线谱系”没有被证实。** 2026 *Journal of Intelligence* 论文明确承接的是 Du & Ma 2026 *Thinking Skills and Creativity*（TSC），不是 2022 《中国考试》；其参考文献没有列 2022 论文。2022 与 2026 J. Intell. 都出现 `N=1083`、同一组六项推理技能，这是很强的 **INFERENCE**，但不能据此声称同一响应矩阵。TSC 本地全文 `DOMAIN-002` 明确记录独立的 975 名入组、删除 89 名未完成者、最终 `N=886`（PDF pp.5–6），所以三篇必须使用不同 dataset/instrument version。[J. Intell. DOI](https://doi.org/10.3390/jintelligence14050079)；[TSC 出版商页](https://www.sciencedirect.com/science/article/pii/S1871187125002706)；[2022 CSE 官方页](https://cse.neea.edu.cn/html1/report/2403/249-1.htm)
2. **目前唯一取得“完整 20 题试卷”的是 2026 J. Intell. 补充材料 S2。** 该补充包还含 S1 prompts 与 S3 豆包输出示例；S3 中的答案属于模型输出，不是出版社或测验作者单独发布的官方答案键。[MDPI supplement](https://www.mdpi.com/article/10.3390/jintelligence14050079/s1)
3. **PELDiaG 与 2022 CSE 都不是可直接复用的公开题库。** 元数据、样本和构念可核验，但完整 passages/items、官方 answer key、逐题来源、响应矩阵和明确再部署许可均未找到。
4. **Jin & Liu 支持的是“自动难度预筛 + 目标群体真人 pilot”的方法，不提供可复用题库。** 其 33 篇材料来自 ETS TOEFL iBT；文章开放不等于第三方 TOEFL 刺激材料可再分发。
5. 外部大规模过程数据只应作为**字段设计、分布校准和分析方法参考**，不能代替本项目目标人群的真实性验证或效标标签。PISA 2012 与 PIAAC 有可下载过程日志；ePIRLS 有公开数据库但题目受限；NAEP 微观过程数据需要 NCES restricted-use license。

## 1. PELDiaG / Du & Ma (2021)

### 元数据与可核验事实

- **CONFIRMED — 题名与版本：** Wenbo Du & Xiaomei Ma, “Probing what’s behind the test score: application of multi-CDM to diagnose EFL learners’ reading performance,” *Reading and Writing* 34, 1441–1466 (2021), DOI [`10.1007/s11145-021-10124-x`](https://doi.org/10.1007/s11145-021-10124-x)；online 2021-01-22，issue date 2021-06。[Springer 版本记录](https://link.springer.com/article/10.1007/s11145-021-10124-x)
- **CONFIRMED — PELDiaG 含义与基本用途：** Springer 与 ERIC 摘要直接写明 PELDiaG 为 “Personalized English Learning: Diagnosis & Guidance”，研究使用该团队设计的 reading comprehension test 诊断 740 名大学新生。[Springer 摘要](https://link.springer.com/article/10.1007/s11145-021-10124-x)；[ERIC EJ1295478](https://eric.ed.gov/?id=EJ1295478)
- **CONFIRMED — 题本结构与分析样本：** 本地全文 `DOMAIN-003` 报告 5 passages、43 个四选一题；items 9/10 因询问前题策略被剔除，正式分数和分析使用 41 题，样本为 740 名大学新生（PDF p.7）。
- **CONFIRMED — Q-matrix 证据链：** 7 名专家编码；12 名学生参与 verbal report，排除不完整/含混材料后保留 9 份；附录给出 expert Q-matrix、student Q-matrix、revised Q-matrix 与 coding guide（PDF pp.7–8 及 Appendices）。
- **CONFIRMED — 访问/权利：** 出版商页面将正文标为 subscription content；页面版权元数据为 “The Author(s), under exclusive licence to Springer Nature”。因此 DOI 页面、摘要和可见表格可引用，但不能把文章或题目视作 OA/可再分发资产。[Springer access/permissions](https://link.springer.com/article/10.1007/s11145-021-10124-x)

### 资产状态

- **NOT FOUND — 完整题本：** 未在出版商、ERIC、作者机构页或可信 OA 仓储找到完整 passages/items、官方 answer key、逐题刺激材料来源。
- **NOT FOUND — 数据：** 未找到 740 人 item-response matrix、逐题过程数据、公开数据仓储或 data availability statement。
- **NOT FOUND — 复用许可：** 未找到允许把题目部署到本项目或公开仓库的明确许可。Q-matrix 的可见性不等于题目文本有再部署许可。
- **CONFIRMED — 原迁移包数字已由原文复核：** `5 passages / 43 items / 41 analyzed items / N=740` 现由 `DOMAIN-003` 支持；这只升级书目/方法事实，不升级题目复用权或数据可得性。

### 当前获取边界

全文已作为 `DOMAIN-003` 落地；仍需向作者请求完整题本、answer key、Q-matrix 原始表、去标识响应矩阵、逐题来源与研究/再部署许可。获得论文原文不等于获得这些资产的使用权。

## 2. Ma & Du (2022) CSE 阅读推理研究

### 元数据与可核验事实

- **CONFIRMED — 题名与引文：** 马晓梅、杜文博，《基于〈量表〉的英语阅读推理能力认知诊断模型构建与成绩报告》，《中国考试》2022(12): 1–9，DOI [`10.19360/j.cnki.11-3303/g4.2022.12.001`](https://doi.org/10.19360/j.cnki.11-3303/g4.2022.12.001)。DOI 可解析到 CHNDOI；西安交通大学作者主页也列出同一 DOI。[杜文博主页](https://faculty.xjtu.edu.cn/wenbo/zh_CN/zdylm/1004718/list/index.htm)；[马晓梅主页](https://faculty.xjtu.edu.cn/xiaomei/zh_CN/zdylm/1011383/list/index.htm)
- **CONFIRMED — 研究设计：** 教育部教育考试院 CSE 官方页明确写明在线阅读推理试卷、G-DINA、`N=1083`，以及主旨、时间、词汇、前提-结论、因果、回指六项推理技能。[中文官方页](https://cse.neea.edu.cn/html1/report/2403/249-1.htm)
- **CONFIRMED — 更详细的英文摘要：** CSE 官方英文页写明六项推理技能经 7 名专家和 16 名学生即时作答记录验证，并从学生过程数据增加“句子字面意义理解”和“语篇字面意义理解”两项语言知识属性；第二阶段分析 1,083 份有效响应。[英文官方页](https://cse.neea.edu.cn/html1/report/2505/31-1.htm)

### 资产状态

- **NOT FOUND — 正文/附件：** 未找到出版社或作者机构公开的合法全文 PDF、supplement、完整在线试卷、answer key、Q-matrix 文件。
- **NOT FOUND — 数据：** 未找到 1,083 份响应、16 名学生即时作答记录、专家编码或个性化报告样例的开放仓储。
- **NOT FOUND — 权利说明：** 官方摘要页未给出题目、数据或再部署许可。CNKI/CHNDOI 落地页的受限访问不能被绕过。

### 人工获取队列

- 建议文件名：`Ma_Du_2022_CSE_Reading_Inference_Cognitive_Diagnosis.pdf`
- 官方入口：[DOI](https://doi.org/10.19360/j.cnki.11-3303/g4.2022.12.001)；[CSE 中文官方摘要](https://cse.neea.edu.cn/html1/report/2403/249-1.htm)
- 获取方式：实验室 CNKI 机构访问或作者索取。
- 请求内容：论文 PDF、20 题与否的准确题本结构、Q-matrix、answer key、1083 份响应、16 人过程记录、刺激材料来源和允许的研究用途。

## 3. Du, Shen & Ma (2026) GenAI Q-matrix

### 元数据、附件与数据

- **CONFIRMED — 题名与版本：** Wenbo Du, Jiayi Shen & Xiaomei Ma, “Applying GenAI to Optimize Q-Matrix Construction for Cognitive Diagnostic Assessment in EFL Reading,” *Journal of Intelligence* 14(5), 79 (2026), DOI [`10.3390/jintelligence14050079`](https://doi.org/10.3390/jintelligence14050079)，PMCID [`PMC13208814`](https://pmc.ncbi.nlm.nih.gov/articles/PMC13208814/)，published 2026-05-05。
- **CONFIRMED — 测验：** 正文写明 CSE 5–6、20 题，包含 10 道选择、3 道句序排序、2 道简答和 5 道标题匹配；经验数据为 5 所中国高校的 1,083 名本科生。[MDPI article](https://www.mdpi.com/2079-3200/14/5/79)
- **CONFIRMED — 补充包：** S1 为完整 GenAI prompts，S2 为完整 diagnostic test paper，S3 为豆包输出示例。[官方 supplement 页](https://www.mdpi.com/article/10.3390/jintelligence14050079/s1)；[PMC OA 记录](https://www.ncbi.nlm.nih.gov/pmc/utils/oa/oa.fcgi?id=PMC13208814)
- **CONFIRMED — 数据访问：** 论文的 Data Availability Statement 为可向通讯作者合理请求，并非公开仓储；联系入口以期刊文章页当前列出的通讯作者信息为准。[MDPI article](https://www.mdpi.com/2079-3200/14/5/79)
- **CONFIRMED — 许可：** 文章与补充材料由 MDPI 按 CC BY 4.0 发布；可在正确署名与标注修改的前提下再分发。MDPI 同时提醒，其页面中的第三方材料未必可由 MDPI 再许可。[MDPI OA policy](https://www.mdpi.com/about/openaccess)；[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

### 重要权利与测量边界

- **NOT FOUND — 官方 answer key：** S2 没有独立答案键。S3 的 “Correct Answer” 属于豆包输出示例，不能作为 gold key，必须由至少两名内容专家独立作答并裁决。
- **NOT FOUND — 逐题来源/第三方权利：** S2 未逐题说明 passage/item 来源，也没有逐刺激材料的第三方权利清单。故可以保存和研究 CC BY 补充材料，但在对外公开部署题目之前，仍需完成 item-level provenance/rights audit。
- **NOT FOUND — 响应数据：** 1,083 人 item-response matrix 未随论文公开；需通过期刊文章页联系通讯作者，并明确伦理审批、去标识、数据使用协议与是否可共享给协作研究者。

## 4. 2022 → 2026 谱系判定

### 直接证据

- **CONFIRMED — J. Intell. 的直接前序是 TSC 2026：** 其方法写明八属性 “adopted from Du and Ma (2026)”，Qmat-E/Qmat-S “adapted from a previous study (see Du & Ma, 2026)”；参考文献对应 *From coarse to fine: A cognitive diagnosis of EFL learners’ inferential ability in EFL reading*, *Thinking Skills and Creativity* 59, 102022，DOI [`10.1016/j.tsc.2025.102022`](https://doi.org/10.1016/j.tsc.2025.102022)。J. Intell. 的参考文献没有列 2022 《中国考试》。[J. Intell. full text](https://www.mdpi.com/2079-3200/14/5/79)
- **CONFIRMED — TSC 测验与样本：** `DOMAIN-002` 报告初始 28 题；382 人 pilot 中 360 份有效响应，随后删除 8 题形成 20 题；主测 975 人中删除 89 名未完成者，最终 886 人（PDF pp.4–6）。题目来自/改编自 CET4、CET6 和既有推理测验，因此全文可读不等于题目可重新部署。

### 可写与不可写的结论

- **INFERENCE — 构念/测验家族关系：** 2022 与 2026 J. Intell. 作者重叠、均为 1,083、六项推理属性一致，2022 英文摘要还报告同样的两个字面理解属性。最合理的工作假设是它们来自同一研发项目或高度重叠的测验家族。
- **NOT FOUND — 同一题本：** 未有一手来源直接写明 2026 S2 就是 2022 的原题本。
- **NOT FOUND — 同一响应矩阵：** 未有一手来源直接写明两篇的 1,083 是同一批记录；相同 `N` 不是行级身份或数据版本证明。
- **NOT FOUND — 2022 → TSC 2026 的映射：** TSC 已明确自己的 `975 -> 886` 排除链，但没有把这些参与者或题本逐行映射到 2022 的 `N=1083`；不能把 TSC 解释为 2022 数据的清洗子集。

**论文写作约束：** 在获得作者声明、数据字典/subject IDs 或两篇全文的明确方法说明前，只能写“可能属于同一研发谱系”，不得写“2022 数据被 2026 复用”。

### 仍需作者确认

全文已作为 `DOMAIN-002` 落地。仍应向作者请求 2022、TSC 2026、J. Intell. 2026 三者的 `instrument_version_id`、采集批次、原始 N、排除规则、最终 N、item mapping 和数据复用声明。

## 5. Jin & Liu hybrid computerised dynamic assessment

### 元数据与版本

- **CONFIRMED — 题名：** Can Jin & Yongcan Liu, “Diagnosing and promoting learners’ L2 inferential reading development through hybrid computerised dynamic assessment in the Chinese EFL classroom,” DOI [`10.1080/09588221.2024.2421521`](https://doi.org/10.1080/09588221.2024.2421521)。Received 2023-12-19，accepted 2024-10-19，online 2024-11-12；卷期引文为 *Computer Assisted Language Learning* 39(3), 687–714 (2026)。因此“2024 online-first”和“2026 卷期年”都正确，但必须注明版本。[publisher full text](https://www.tandfonline.com/doi/full/10.1080/09588221.2024.2421521)；[2026 issue](https://www.tandfonline.com/toc/ncal20/39/3)
- **CONFIRMED — 合法开放版本：** Cambridge Apollo 收录 peer-reviewed accepted manuscript，repository DOI [`10.17863/CAM.113003`](https://doi.org/10.17863/CAM.113003)。[repository item](https://www.repository.cam.ac.uk/items/e93fe8f6-f83d-4b18-8d09-bd560f72ad67)
- **CONFIRMED — 版本许可不同：** Cambridge 条目标注 accepted manuscript 为 CC BY 4.0；Crossref 对 publisher Version of Record 记录 CC BY-NC-ND 4.0。不得把一个版本的许可泛化到另一个版本。

### 难度与 pilot 核验

- **CONFIRMED — 两次 pilot：** 正文明确用独立且英语水平相近的班级 `n=47` 做两项 pilot，用于检查材料难度/适切性与软件 beta。
- **CONFIRMED — 难度 pilot：** pilot G-DA 使用 4 篇阅读、每篇 2 道推理题，LanguageData 估计范围 CSE 5–7；结果认为约 CSE 5.5 能揭示当前能力。
- **CONFIRMED — 正式材料分层：** pre-test、7 次 EP 和 post-test 为 CSE 5.5–6.0，near-transfer 为 6–7，far-transfer 为 `>7`；最终选用 33 篇 TOEFL reading passages。
- **CONFIRMED — 题目选择规则：** 材料来自 ETS 官方 TOEFL iBT；通常每篇 2–3 道推理选择题。若同一段落有多个题，只保留一道，避免前题揭示后题答案。以上均可在合法取得的 accepted manuscript 中直接核验。[Cambridge accepted manuscript](https://api.repository.cam.ac.uk/server/api/core/bitstreams/933b2e88-bb15-474d-839f-e9a7c46aa450/content)

### 资产与权利结论

- **NOT FOUND — item bank/data：** 文章未附 33 篇题本、HTML5 测验包、逐题 mediations、原始数据仓储或 data availability statement。
- **PROHIBITED — 直接抽取并公开 TOEFL 刺激材料：** accepted manuscript 的开放许可不消除 ETS 对原始 passages/items 的第三方权利。除非取得 ETS 许可或改用自有/明确开放的材料，不能把这 33 篇复制进公开仓库或产品。
- **可采用的方法：** 用自动文本难度工具预筛候选材料，再用目标群体真人 pilot 决定实际难度；自动分数不能替代目标人群实测。

## 6. 外部过程数据：访问、许可与本项目角色

| 数据源 | 状态与访问 | 权利/许可边界 | 本项目允许角色 | 不允许的推断 |
|---|---|---|---|---|
| PISA 2012 CBA | **CONFIRMED**：OECD 页面提供问卷、认知响应/计分文件，以及已发布计算机题目的 process logs：problem solving 83 MB、digital reading 90 MB、computer mathematics 23 MB；本审计未下载。[官方数据库](https://www.oecd.org/en/data/datasets/pisa-2012-cba-database.html) | OECD 通用数据条款允许下载、改编和分享并要求署名，但明确要求检查数据集特定限制和第三方权利。[OECD terms](https://www.oecd.org/en/about/terms-conditions.html) | 优先级高：校准数字阅读中的导航序列、事件计数、任务时长分布；验证 ETL 与序列特征代码。 | 不代表中国大学 EFL 人群；released-item logs 之外的日志仍可能受限；不能充当本项目认知标签 ground truth。 |
| ePIRLS 2016 | **CONFIRMED**：公开版数据库可下载，含 ePIRLS achievement/背景文件、item information、IRT 参数、percent-correct、codebook；restricted-use 版需联系 IEA。[官方数据库](https://timssandpirls.bc.edu/pirls2016/international-database/index.html) | IEA 不再无许可公开题目；复制、再分发或把材料用作 assessment/learning materials 需遵守许可，第三方 passages 还需权利人许可。 | 适合参照在线信息阅读任务结构、achievement/背景变量和公开统计；实际变量存在性必须先查 ePIRLS codebook。 | **NOT FOUND**：未在公开数据库页确认可下载的原始逐点击 clickstream；不得把“报告有 navigation 章节”写成“公开数据含完整原始日志”。四年级人群也不是本项目目标人群。 |
| PIAAC 1st Cycle | **CONFIRMED**：17 国的去标识完整 respondent logs 以 raw XML 公共使用文件发布，可用 `SEQID` 与 PUF 对接；GESIS DOI [`10.4232/1.12955`](https://doi.org/10.4232/1.12955)。官方 LogDataAnalyzer 可生成 time-on-task、highlight、environment switching、webpage/email views/revisits 等变量。[OECD PIAAC database](https://www.oecd.org/en/data/datasets/piaac-1st-cycle-database.html) | 公共日志可下载；但 full log documentation 需申请并签 confidentiality agreement。OECD 通用数据条款仍要求核查特定限制/第三方权利。 | 最高优先级的过程分布与特征工程参考；适合测试 XML 解析、序列化、页面访问/重访与时间特征。 | 成人技能测评不是中国大学 EFL 阅读；能校准软件/分布，不能直接验证本项目构念解释或标签。 |
| NAEP | **CONFIRMED**：微观 respondent-level raw data 需 NCES restricted-use license；公开说明中的 process dataset 是 2017 数学（grade 8；另有 grade 4 selected block/form），不是公开阅读日志。[NAEP process page](https://nces.ed.gov/nationsreportcard/researchcenter/process_data_2017.aspx)；[RUD page](https://nces.ed.gov/nationsreportcard/researchcenter/variablesrudata.aspx) | 申请需机构 PPO/SO/SSO、安全计划和保密文件；学术 PPO 至少 postdoc。[NCES application](https://nces.ed.gov/statprog/instruct_apply.asp) | 近期仅作方法文献与数据治理参考；若实验室以后具备资质，再评估 restricted-use 申请。 | **NOT FOUND**：未确认公开可下载的 NAEP reading process microdata。不得把数学 process data 当成阅读效标；当前学生团队也不能独立满足 PPO 门槛。 |

## 7. 本地合法下载清单

以下文件均来自出版商/作者机构仓储或官方 OA 仓储；未绕过登录或认证。下载时间均为 2026-08-14（Asia/Shanghai）。

| 本地文件 | 来源与版本 | 页数 | SHA-256 | 可再分发判断 |
|---|---|---:|---|---|
| `sources/library/papers/domain/Du_Shen_Ma_2026_GenAI_Q_Matrix_EFL_Reading.pdf` | [PMC OA article PDF](https://pmc-oa-opendata.s3.amazonaws.com/PMC13208814.1/PMC13208814.1.pdf)，Version of Record | 23 | `416f4156aedae7e846e3d05d389d74fd51a638708019d582aed81159cb8b554a` | **YES, CC BY 4.0**，需署名/链接许可/标注修改。 |
| `sources/library/study-materials/items/Du_Shen_Ma_2026_GenAI_Q_Matrix_Supplement.pdf` | [MDPI official supplement archive](https://mdpi-res.com/d_attachment/jintelligence/jintelligence-14-00079/article_deploy/jintelligence-14-00079-s001.zip) 内 `jintelligence-4193271-supplementary.pdf` | 39 | `55032acdaa101bf3fa3b035c4a43f091649de9b8dd88cd41294cf71d8ed1ef12` | **CONDITIONAL**：补充材料容器为 CC BY；逐题第三方刺激材料权利仍未核清，公开部署前做 item-level audit。 |
| `sources/library/papers/domain/Jin_Liu_2024_Hybrid_CDA_Accepted_Manuscript.pdf` | [Cambridge Apollo bitstream](https://api.repository.cam.ac.uk/server/api/core/bitstreams/933b2e88-bb15-474d-839f-e9a7c46aa450/content)，Accepted Manuscript | 41 | `55f52afe131980a3a474e32e57c3939ddf1f4eea086ad17b4694ff4246462181` | **CONDITIONAL**：仓储条目标 CC BY 4.0，但文中 TOEFL 材料为第三方；不得抽取/再部署 TOEFL passages/items。 |
| `sources/library/papers/domain/2026_Du_Ma_From_Coarse_to_Fine.pdf` | 用户合法提供的 Elsevier VOR，catalog `DOMAIN-002` | 13 | 见 `sources/catalog.yaml` | **NO PUBLIC REDISTRIBUTION**；本地研究副本。 |
| `sources/library/papers/domain/2021_Du_Ma_Multi_CDM_EFL_Reading.pdf` | 用户合法提供的 Springer VOR，catalog `DOMAIN-003` | 27 | 见 `sources/catalog.yaml` | **NO PUBLIC REDISTRIBUTION**；本地研究副本。 |

## 8. 未取得资产与下一步

| 优先级 | 需要的文件/资产 | 官方入口 | 未取得原因 | 下一步 |
|---:|---|---|---|---|
| P0 | `Ma_Du_2022_CSE_Reading_Inference_Cognitive_Diagnosis.pdf` + items/Q/data | [DOI](https://doi.org/10.19360/j.cnki.11-3303/g4.2022.12.001) | CNKI/CHNDOI 受限；未发现授权 OA | 实验室 CNKI 或作者请求；先问清 1083 数据与 2026 的关系。 |
| P0 | TSC 2026 supplement/items/data | [DOI](https://doi.org/10.1016/j.tsc.2025.102022) | 正文已取得；未取得完整可部署题本、响应数据和权利 | 向作者请求 item mapping、数据字典和允许用途。 |
| P1 | PELDiaG answer key/items/data | [DOI](https://doi.org/10.1007/s11145-021-10124-x) | 正文已取得；未取得完整刺激材料、响应矩阵和复用许可 | 向作者请求资产与逐题权利，不重复请求正文。 |
| P1 | 2026 J. Intell. empirical response data + expert/student raw coding | [article](https://www.mdpi.com/2079-3200/14/5/79) | data on reasonable request | 通过文章页联系通讯作者，同时请求 data dictionary、伦理/DUA 条件、行级谱系说明。 |
| P2 | Jin & Liu 33 passages、mediations、HTML5 包、数据 | [publisher](https://www.tandfonline.com/doi/full/10.1080/09588221.2024.2421521) | 未附 supplement/data；TOEFL 第三方权利 | 只请求研究方法/去标识数据；除非 ETS 明确授权，不请求公开再分发 TOEFL 题本。 |

## 9. 采用门槛

1. 每个拟用题目必须有 `item_id`、`source_work`、`source_locator`、`stimulus_rights`、`answer_key_authority`、`construct_mapping_version` 和 `allowed_use`。
2. “论文 OA”与“题目可部署”分开判定；第三方 passage/item 未清权时只能用于内部审计，不能进入公开仓库或正式实验。
3. 作者提供的数据必须记录原始文件 SHA-256、提供日期、版本说明、去标识方式、伦理审批/同意范围、共享与销毁条件。
4. 对 2022/TSC 2026/J. Intell. 2026，在收到作者或数据字典的直接证据前，分配不同的 `dataset_id` 和 `instrument_version_id`；禁止按样本量自动合并。
5. PISA/PIAAC/ePIRLS/NAEP 只能用于外部校准、方法验证或软件测试；所有目标构念、认知标签和正式效度结论仍需本项目目标人群的独立真人证据。
