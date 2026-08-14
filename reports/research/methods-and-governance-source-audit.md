# 方法与治理来源 / 原文获取审计

- 审计日期：2026-08-14
- canonical 输入：`reports/protocols/AI_RESEARCH_TOOLING_POLICY.md`、`reports/protocols/HUMAN_RESEARCH_GATES.md`
- 覆盖范围：上述两份协议中的全部 25 个不重复外链（AI 工具政策 12 个；人类研究 gates 13 个）
- 获取原则：只接受出版商、作者所在机构、正式标准组织、政府或高校伦理机构的公开入口；未使用 Sci-Hub、认证绕过、聚合站下载或搜索结果缓存。
- 许可口径：`可本地研究使用` 只表示可以从公开入口合法获取、在本地阅读和引用；不等于可以把 PDF 随公开 GitHub 仓库再分发。`可公开再分发` 只在具体文件存在明确开放许可或机构级再利用政策时判为“是”。

## 结论先行

初始审计取得 9 个方法/标准 PDF；2026-08-14 用户又合法提供 Shin (2025) 和 GRRAS 的期刊版本，现共 11 个本地原件。两份新增文件已经过格式、文本、首屏、版本和权利审计；arXiv:2306.00176 与正式 ICWSM 后继版本属于同一研究链，本地仍只保留正式版。

对计划公开的 GitHub 仓库，当前文件不能“一刀切”提交：

- 可公开再分发（按许可署名并保留许可信息）：Morris 2019、Bisbee et al. 2024、Shumailov et al. 2024、Wachinger et al. 2024/2025、NIST AI 600-1（须遵守 NIST courtesy attribution，并检查第三方材料的单独 credit line）。
- 仅可本地研究使用、不要默认随公开仓库发布：AERA/APA/NCME 2014 Standards（PDF 内写明 all rights reserved 且禁止复制/分发）、两篇 ICWSM 2025 PDF（PDF 内写明 AAAI copyright / all rights reserved，页面未给出适用于该文件的开放许可）、World Bank WPS10597 本地副本（公开可下载，但本次未在文件或作品记录中验证到足以支持仓库再分发的明确许可）。
- 新增本地受控文件：Shin 2025 为 `METHOD-008`，载明 CC BY-NC-ND，但本地容器存在 iText 后处理记录，任何公开分发前必须先确认未改动版本；GRRAS IJNS 再发表版为 `METHOD-009`，未核验开放再分发许可。两者均不进入首个公共 Git 快照。

## A. AI_RESEARCH_TOOLING_POLICY 来源逐项审计

### A1. Standards for Educational and Psychological Testing (2014 edition)

- 类型：正式专业共识标准；AERA、APA、NCME 联合出版。
- 标识：无 DOI；[官方 open-access 入口](https://www.testingstandards.net/open-access-files.html)。
- OA / 许可证据：官方页面明确 2014 English edition “now open access”并提供 PDF；但 PDF 版权页同时写明 copyright 2014、all rights reserved，未经书面许可不得 reproduction or distribution。这里的 open access 是免费读取，不是开放再分发许可。
- 可本地研究使用：是。
- 可公开再分发：否；不要把该 PDF 提交到公开仓库，除非三家出版组织另行书面授权。
- 本地文件：`sources/library/standards/2014_AERA_APA_NCME_Testing_Standards.pdf`
- SHA-256：`78182353e8cd877535f6f3c8967da52d4d3af64725146c08606d38825941ac61`

### A2. Using simulation studies to evaluate statistical methods

- 类型：期刊方法论文；Tim P. Morris, Ian R. White, Michael J. Crowther；*Statistics in Medicine* 38 (2019), 2074-2102。
- DOI：[10.1002/sim.8086](https://doi.org/10.1002/sim.8086)。
- 获取入口：[UCL Discovery 作者机构 PDF](https://discovery.ucl.ac.uk/10066118/1/2019%20-%20Morris%20-%20simulation%20studies%20tutorial%20-%20stat%20med.pdf)。
- OA / 许可证据：PDF 首页声明 Creative Commons Attribution License；出版商登记元数据指向 CC BY 4.0。
- 可本地研究使用：是。
- 可公开再分发：是，须保留署名、来源、DOI 与许可信息。
- 本地文件：`sources/library/papers/methods/2019_Morris_Using_Simulation_Studies.pdf`
- SHA-256：`3aec72851ec6dc1e61a8921c4e0fa69b4b7722b73d26a764b423e53d0e6f106d`

### A3. Synthetic Replacements for Human Survey Data? The Perils of Large Language Models

- 类型：期刊研究论文；James Bisbee, Joshua D. Clinton, Cassy Dorff, Brenton Kenkel, Jennifer M. Larson；*Political Analysis* 32 (2024), 401-416。
- DOI：[10.1017/pan.2024.5](https://doi.org/10.1017/pan.2024.5)。
- 获取入口：[Cambridge University Press 官方 PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/B92267DC26195C7F36E63EA04A47D2FE/S1047198724000056a.pdf/div-class-title-synthetic-replacements-for-human-survey-data-the-perils-of-large-language-models-div.pdf)。
- OA / 许可证据：出版商页面和 PDF 均声明 CC BY 4.0，可在正确署名条件下 re-use、distribution、reproduction。
- 可本地研究使用：是。
- 可公开再分发：是，须署名并保留许可；单独 credit line 排除的第三方材料除外。
- 本地文件：`sources/library/papers/methods/2024_Bisbee_Synthetic_Replacements.pdf`
- SHA-256：`36a0d04cacac5bdb2f24e7022bcbc6fd01493dfcbc6104c588123eb0c7f3b744`

### A4. AI models collapse when trained on recursively generated data

- 类型：期刊研究论文；Ilia Shumailov, Zakhar Shumaylov, Yiren Zhao, Nicolas Papernot, Ross Anderson, Yarin Gal；*Nature* 631 (2024), 755-759。
- DOI：[10.1038/s41586-024-07566-y](https://doi.org/10.1038/s41586-024-07566-y)。
- 获取入口：[Nature 官方 PDF](https://www.nature.com/articles/s41586-024-07566-y.pdf)。
- OA / 许可证据：PDF 声明 CC BY 4.0，允许 use、sharing、adaptation、distribution、reproduction；单独 credit line 排除的材料须另行授权。
- 可本地研究使用：是。
- 可公开再分发：是，须署名、链接许可并标明改动。
- 版本提醒：Crossmark/Crossref 已关联后续 correction DOI [10.1038/s41586-025-08905-3](https://doi.org/10.1038/s41586-025-08905-3)；正式引用或复现实验前应同步核对 correction。本轮不额外下载未被 canonical 协议引用的 correction。
- 本地文件：`sources/library/papers/methods/2024_Shumailov_AI_Models_Collapse.pdf`
- SHA-256：`474c820b5224b6bfa337e98a0ff942eca4b7808b44236121af828c6122a860ae`

### A5. Co-Coding Classroom Dialogue: A Single Researcher Case Study of ChatGPT-Assisted Analysis in Science Education

- 类型：期刊研究论文；Eunhye Shin；*Journal of Computer Assisted Learning* 41(4), e70089 (2025)。
- DOI：[10.1111/jcal.70089](https://doi.org/10.1111/jcal.70089)。
- OA / 许可证据：出版商登记的 OA endpoint 为 `https://onlinelibrary.wiley.com/doi/pdfdirect/10.1111/jcal.70089`，许可为 CC BY-NC-ND 4.0。
- 可本地研究使用：是；用户提供的本地文件已核验为 Wiley VOR 内容与版式。
- 可公开再分发：许可为 CC BY-NC-ND，但本地 PDF metadata 记录 iText 后处理，不能仅凭版式相同断言 bitstream 未改动；公开前应从正常浏览器重取官方原件并逐字节/内容比较。
- 本地文件：`sources/library/papers/methods/2025_Shin_Co_Coding_Classroom_Dialogue.pdf`（catalog `METHOD-008`）。
- 获取限制：官方 `pdf` 与 `pdfdirect` 对自动化环境返回 HTTP 403，因此 catalog 保持 `MANUAL_ONLY`。

### A6. Guidelines for Reporting Reliability and Agreement Studies (GRRAS) were proposed

- 类型：报告指南 / 期刊论文；Jan Kottner, Laurent Audige, Stig Brorson, Allan Donner, Byron J. Gajewski, Asbjorn Hrobjartsson, Chris Roberts, Mohamed Shoukri, David L. Streiner；*International Journal of Nursing Studies* 48(6), 661-671 (2011)。
- DOI：[10.1016/j.ijnurstu.2011.01.016](https://doi.org/10.1016/j.ijnurstu.2011.01.016)。
- 辅助正式入口：[EQUATOR Network 指南记录](https://www.equator-network.org/reporting-guidelines/guidelines-for-reporting-reliability-and-agreement-studies-grras-were-proposed/)。
- OA / 许可证据：DOI 元数据只给出 Elsevier text-and-data-mining 条款，不是 OA / 再分发许可；未找到出版商或作者机构提供的该 DOI 完整 OA PDF。
- 可本地研究使用：是；用户提供的 IJNS 再发表 VOR 已本地核验。
- 可公开再分发：否 / 未获授权。
- 本地文件：`sources/library/papers/methods/2011_Kottner_GRRAS_IJNS.pdf`（catalog `METHOD-009`）。它是 IJNS 对 JCE 版本的经许可再发表，必须保留 IJNS DOI；两个 DOI 不得合并为同一版本记录。

### A7. Automated Annotation with Generative AI Requires Validation

- 类型：arXiv 预印本；Nicholas Pangakis, Samuel Wolken, Neil Fasching；提交于 2023-05-31。
- 标识：[arXiv:2306.00176](https://arxiv.org/abs/2306.00176)；DataCite DOI [10.48550/arXiv.2306.00176](https://doi.org/10.48550/arXiv.2306.00176)。
- OA / 许可证据：arXiv 作品页直接链接 CC BY 4.0。
- 可本地研究使用：是。
- 可公开再分发：是，按 CC BY 4.0 署名；但本轮未保存该 PDF。
- 未下载原因：同一研究链已有 canonical 协议另行引用的正式 ICWSM 版本（A8），本地只保留正式版，避免 preprint + VOR 重复。两版题名和署名不完全相同（预印本含 Neil Fasching，正式版只列 Nick Pangakis 与 Sam Wolken），因此引用时不可把两条书目信息混写。

### A8. Keeping Humans in the Loop: Human-Centered Automated Annotation with Generative AI

- 类型：正式会议论文；Nick Pangakis, Sam Wolken；*Proceedings of the International AAAI Conference on Web and Social Media* 19(1), 1471-1492 (2025)。
- DOI：[10.1609/icwsm.v19i1.35883](https://doi.org/10.1609/icwsm.v19i1.35883)。
- 获取入口：[AAAI 官方作品页](https://ojs.aaai.org/index.php/ICWSM/article/view/35883)；[官方 PDF](https://ojs.aaai.org/index.php/ICWSM/article/download/35883/38037)。
- OA / 许可证据：官方页面免费直接下载；PDF 版权页写明 copyright 2025 AAAI, all rights reserved，作品页未显示适用于本文 PDF 的 Creative Commons 许可。
- 可本地研究使用：是。
- 可公开再分发：否 / 未验证到授权；免费获取不能替代再分发许可。
- 本地文件：`sources/library/papers/methods/2025_Pangakis_Keeping_Humans_in_the_Loop.pdf`
- SHA-256：`b1b11280862c25e87ede674e464dc1cda10b51ce54afc8add57f2b696d36843b`

### A9. Using Large Language Models for Qualitative Analysis can Introduce Serious Bias

- 类型：期刊研究论文；Julian Ashwin, Aditya Chhabra, Vijayendra Rao；*Sociological Methods & Research*，online first 2025-05-27，卷 55(3) 于 2026-08 出版。
- DOI：[10.1177/00491241251338246](https://doi.org/10.1177/00491241251338246)。
- OA / 许可证据：SAGE 官方作品页明确该期刊 VOR 使用 CC BY 4.0，允许署名后的 use、reproduction、distribution。
- 期刊 VOR 获取结果：官方 PDF endpoint 在本环境返回 HTTP 403，未使用绕过手段。
- 本地替代版本：作者所在机构 World Bank 的 *Policy Research Working Paper 10597* (2023)，同题名但早于期刊 VOR；官方记录 DOI [10.1596/1813-9450-10597](https://doi.org/10.1596/1813-9450-10597)，[World Bank 官方记录](https://documents.worldbank.org/en/publication/documents-reports/documentdetail/099433311072326082)，[官方机构 PDF](https://openknowledge.worldbank.org/bitstreams/301eff0a-c936-456f-bb0b-af6f5bf7e4f4/download)。
- 可本地研究使用：是。分析时须把 WPS 视为早期版本，引用期刊结论前回到 SAGE 当前 VOR 核对。
- 可公开再分发：期刊 VOR 是 CC BY 4.0，但本地保存的不是 VOR；本次未在 WPS PDF 或作品记录中验证到足以支持 GitHub 再分发的明确许可，故本地 WPS 文件判为“否 / 待权利确认”。
- 本地文件：`sources/library/papers/methods/2023_Ashwin_LLM_Qualitative_Analysis_Bias_WPS10597.pdf`
- SHA-256：`6ba35401c1d22e0442b0ec841c5c922617656019d5a34af088f1582d6de1959e`

### A10. What's in a Prompt?: A Large-Scale Experiment to Assess the Impact of Prompt Design on the Compliance and Accuracy of LLM-Generated Text Annotations

- 类型：正式会议论文；Shubham Atreja, Joshua Ashkinaze, Lingyao Li, Julia Mendelsohn, Libby Hemphill；ICWSM 19(1), 122-145 (2025)。
- DOI：[10.1609/icwsm.v19i1.35807](https://doi.org/10.1609/icwsm.v19i1.35807)。
- 获取入口：[AAAI 官方作品页](https://ojs.aaai.org/index.php/ICWSM/article/view/35807)；[官方 PDF](https://ojs.aaai.org/index.php/ICWSM/article/download/35807/37961)。
- OA / 许可证据：官方页面免费直接下载；PDF 版权页写明 copyright 2025 AAAI, all rights reserved，作品页未显示适用于本文 PDF 的开放许可。
- 可本地研究使用：是。
- 可公开再分发：否 / 未验证到授权。
- 本地文件：`sources/library/papers/methods/2025_Atreja_Whats_in_a_Prompt.pdf`
- SHA-256：`4563d8c92978d81a2f038664e71522d3ec254270cf5e18c54abd7f4b953d40c7`

### A11. Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile

- 类型：NIST Technical Series 政府技术报告 / 自愿性风险治理 profile；NIST AI 600-1，2024-07。它不是一项独立的强制法规，也不应误称为 ISO 式产品合格标准。
- DOI：[10.6028/NIST.AI.600-1](https://doi.org/10.6028/NIST.AI.600-1)。
- 获取入口：[NIST 官方 PDF](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf)。
- OA / 许可证据：[NIST Technical Series 政策](https://www.nist.gov/nist-research-library/nist-publications)说明 NIST 员工作品在美国不受版权保护，并对其可主张的境外权利授予 worldwide、royalty-free 的重印和衍生使用权；同时警告第三方作品可能仍受版权保护。
- 可本地研究使用：是。
- 可公开再分发：是，但须使用推荐引文，并加注 “Republished courtesy of the National Institute of Standards and Technology”；第三方材料按各自 credit line 处理。
- 本地文件：`sources/library/standards/2024_NIST_AI_600-1_Generative_AI_Profile.pdf`
- SHA-256：`6e73620ab6b64e90ef2c04bf0e0d6246185a2f4b1b13cab0df494496cff89b6a`

### A12. Prompts, Pearls, Imperfections: Comparing ChatGPT and a Human Researcher in Qualitative Data Analysis

- 类型：期刊研究论文；Jonas Wachinger, Kate Barnighausen, Louis N. Schafer, Kerry Scott, Shannon A. McMahon；*Qualitative Health Research*，online first 2024-05-22，35(9), 951-966 (2025)。
- DOI：[10.1177/10497323241244669](https://doi.org/10.1177/10497323241244669)。
- 获取入口：[SAGE 官方作品页](https://journals.sagepub.com/doi/10.1177/10497323241244669)；[University of the Witwatersrand 机构库 VOR](https://wiredspace.wits.ac.za/bitstreams/0b9061ee-889f-4043-bb2f-a100cd5036ec/download)。
- OA / 许可证据：SAGE 官方页面明确 CC BY 4.0，允许署名后的 use、reproduction、distribution；机构库文件与 SAGE VOR 的题名、卷页、DOI 和版式一致。
- 可本地研究使用：是。
- 可公开再分发：是，须署名、保留 DOI 与 CC BY 4.0 信息。
- 本地文件：`sources/library/papers/methods/2024_Wachinger_Prompts_Pearls_Imperfections.pdf`
- SHA-256：`ce7f0c37874658254d07af82ed16057c73591928f25763c201f0fb34b0f5f15f`

## B. HUMAN_RESEARCH_GATES 来源逐项审计

以下 13 项都是网页型法律、政府说明、联邦指导或高校 IRB 流程。本轮按“官方网页可保持网页来源”的规则只登记，不人为打印/转换成 PDF。项目可在公开仓库保存题名、链接、访问日期和必要摘录；没有取得各网站对整页复制的授权，因此不应把完整网页镜像当作可公开再分发资产。

### B1. 关于印发《科技伦理审查办法（试行）》的通知 / 科技伦理审查办法（试行）

- 类型：中国多部门规范性文件；国科发监〔2023〕167号；成文 2023-09-07，发布 2023-10-08，2023-12-01 起施行。
- 官方入口：[中华人民共和国科学技术部](https://www.most.gov.cn/xxgk/xinxifenlei/fdzdgknr/fgzc/gfxwj/gfxwj2023/202310/t20231008_188309.html)。页面标注“有效”“主动公开”。
- 本地研究使用：是，以官方网页为准。
- 本地文件 / SHA：无；网页型正式来源，不伪造 PDF。

### B2. 中华人民共和国个人信息保护法

- 类型：全国性法律；2021-08-20 第十三届全国人大常委会第三十次会议通过。
- canonical 官方入口：[工业和信息化部转载全文](https://www.miit.gov.cn/jgsj/zfs/fl/art/2022/art_515a4b20c12f430eab54bb4f56d89f56.html)。该链接是中央部委官网的法律全文转载，不是全国人大原始发布页。
- 本地研究使用：是；需要精确法律版本或修法状态时，仍应复核全国人大/国家法律法规数据库的当前文本。
- 本地文件 / SHA：无；网页型法律来源。

### B3. Lesson 2: What is Human Subjects Research?

- 类型：美国 HHS Office for Human Research Protections (OHRP) 官方培训材料；聚焦 Revised Common Rule。
- 官方入口：[HHS OHRP](https://www.hhs.gov/ohrp/education-and-outreach/online-education/human-research-protection-training/lesson-2-what-is-human-subjects-research/index.html)；页面标注 content last reviewed 2021-06-28。
- 适用性：权威的美国联邦培训 / 解释材料，不是中国法，也不能替代项目所属高校伦理机构的认定。
- 本地文件 / SHA：无；保留网页来源。

### B4. Quality Improvement Activities FAQs

- 类型：HHS OHRP 官方 FAQ / 非约束性指导。
- 官方入口：[HHS OHRP](https://www.hhs.gov/ohrp/regulations-and-policy/guidance/faq/quality-improvement-activities/index.html)。
- 适用性：用于理解美国 Common Rule 下质量改进与 research 的边界；不能直接决定中国高校项目是否免审。
- 本地文件 / SHA：无。

### B5. 关于印发涉及人的生命科学和医学研究伦理审查办法的通知 / 涉及人的生命科学和医学研究伦理审查办法

- 类型：中国国家卫生健康委、教育部、科技部、国家中医药局联合文件；国卫科教发〔2023〕4号，2023-02-18。
- canonical 官方入口：[湖南省人民政府转载全文](https://www.hunan.gov.cn/zqt/zcsd/202302/t20230228_29258097.html)；页面注明信息来源为国家卫健委网站。它是政府官网转载，不是发文机关的原始页面。
- 本地研究使用：是；正式提交材料前宜再核对国家卫健委现行原文与本校适用范围。
- 本地文件 / SHA：无。

### B6. IRB FAQs

- 类型：Cornell University Research Services 的高校 IRB / HRPP 机构指南。
- 官方入口：[Cornell Research Services](https://researchservices.cornell.edu/resources/irb-faqs)。
- 适用性：其中 pilot、学生研究、不得追溯审批等回答是 Cornell 的机构口径和美国 Common Rule 实务例证，不是对本项目所在中国高校具有直接约束力的规则。
- 本地文件 / SHA：无。

### B7. Do I Need IRB Review?

- 类型：Stanford University Human & Animal Research Compliance 的机构判定指南。
- 官方入口：[Stanford IRB](https://irb.stanford.edu/for-researchers/do-i-need-irb-review)。
- 适用性：机构性流程指导；可作风险建模参考，不可替代本校书面 determination。
- 本地文件 / SHA：无。

### B8. Expedited Review: Categories of Research that may be Reviewed Through an Expedited Review Procedure (1998)

- 类型：HHS OHRP 官方 expedited-review 类别清单 / 指导。
- 官方入口：[HHS OHRP](https://www.hhs.gov/ohrp/regulations-and-policy/guidance/categories-of-research-expedited-review-procedure-1998/index.html)。
- 适用性：美国联邦指导，页面明确其 guidance 性质；不可把“expedited”误解为“不需伦理审查”，也不能直接套用为中国高校免审标准。
- 本地文件 / SHA：无。

### B9. Multimedia Recordings

- 类型：University of Utah Institutional Review Board 的多媒体录制机构指南。
- 官方入口：[University of Utah IRB](https://irb.utah.edu/guidance-series/multimedia-recordings/)。
- 适用性：用于识别录音、录像、照片和可识别性风险；属于该校 IRB 指导，不是通用法律许可。
- 本地文件 / SHA：无。

### B10. 国家互联网信息办公室、公安部联合公布《人脸识别技术应用安全管理办法》

- 类型：中国官方发布说明 / 规则摘要；发布 2025-03-21，说明办法自 2025-06-01 起施行。
- 官方入口：[国家互联网信息办公室 / 中国网信网](https://www.cac.gov.cn/2025-03/21/c_1744174262342111.htm)。
- 来源限制：canonical 链接是负责人说明性质的摘要页，不是《人脸识别技术应用安全管理办法》逐条全文。若项目实际采用 webcam 人脸识别或处理人脸信息，应另将办法正式全文作为直接规范来源，不能只依赖该摘要。
- 本地文件 / SHA：无。

### B11. Get to Know a Review Category: Expedited Category 6

- 类型：Teachers College, Columbia University IRB 官方博客 / 机构解释；2021。
- 官方入口：[Teachers College IRB](https://www.tc.columbia.edu/institutional-review-board/irb-blog/2021/get-to-know-a-review-category-expedited-category-6/)。
- 适用性：对 voice、video、digital/image recording 归类的美国机构实务说明；不是法律文本，也不替代本校审查。
- 本地文件 / SHA：无。

### B12. Informed Consent FAQs

- 类型：HHS OHRP 官方 FAQ / 非约束性指导。
- 官方入口：[HHS OHRP](https://www.hhs.gov/ohrp/regulations-and-policy/guidance/faq/informed-consent/index.html)。
- 适用性：用于理解美国 Common Rule 的 consent 要求与 waiver；本项目应以中国现行规范和本校伦理委员会要求为准。
- 本地文件 / SHA：无。

### B13. 关于办理人体实验伦理审查的相关流程

- 类型：广东工业大学发展规划处 / 校学术委员会秘书处的校级办事流程；发布 2026-06-30。
- 官方入口：[广东工业大学发展规划处](https://fzghc.gdut.edu.cn/info/1045/1304.htm)。
- 来源意义：这是当前 13 项中离本项目高校情境最近的机构流程来源；页面明确列出问卷、访谈、行为实验、眼动等适用场景，并写明实验开始前获得伦理批准、不得事后补办。
- 适用性限制：只有在广东工业大学是本项目责任单位或审查单位时才可作为直接流程依据；否则应向实际所属实验室 / 学校取得对应制度与书面答复。
- 本地文件 / SHA：无。

## C. 文件级公开仓库 gate

| 本地 PDF | 本地研究 | 公开再分发 | 当前 gate |
|---|---:|---:|---|
| `2019_Morris_Using_Simulation_Studies.pdf` | 是 | 是，CC BY | 可提交，补充标准署名 / license notice |
| `2024_Bisbee_Synthetic_Replacements.pdf` | 是 | 是，CC BY 4.0 | 可提交，保留署名与第三方材料 caveat |
| `2024_Shumailov_AI_Models_Collapse.pdf` | 是 | 是，CC BY 4.0 | 可提交，保留署名、许可与改动说明 |
| `2024_Wachinger_Prompts_Pearls_Imperfections.pdf` | 是 | 是，CC BY 4.0 | 可提交，保留署名与许可 |
| `2024_NIST_AI_600-1_Generative_AI_Profile.pdf` | 是 | 是，NIST policy 有条件 | 可提交，增加 NIST courtesy attribution 并检查 credit lines |
| `2014_AERA_APA_NCME_Testing_Standards.pdf` | 是 | 否 | 仅本地；公开仓库排除 |
| `2025_Atreja_Whats_in_a_Prompt.pdf` | 是 | 未获授权 | 仅本地；公开仓库排除 |
| `2025_Pangakis_Keeping_Humans_in_the_Loop.pdf` | 是 | 未获授权 | 仅本地；公开仓库排除 |
| `2023_Ashwin_LLM_Qualitative_Analysis_Bias_WPS10597.pdf` | 是，早期版 | 未验证 | 仅本地；取得 World Bank 明确许可或换成 SAGE CC BY VOR 后再评估 |

这张 gate 表只处理 PDF 版权 / 再分发，不等于论文内容的科学质量背书。任何进入正式研究推理链的作品仍需做版本核对、方法审阅、适用性判断与引用定位。

## D. 自查记录

- 外链覆盖：`AI_RESEARCH_TOOLING_POLICY.md` 12/12；`HUMAN_RESEARCH_GATES.md` 13/13。
- 来源记录：初始 9 个文件来自出版商、作者机构、联合标准官网或 NIST；新增 2 个由用户通过合法渠道提供并经出版商元数据核验。
- 重复控制：未同时保存 arXiv:2306.00176 与 ICWSM 35883；Ashwin 只保存 World Bank WPS，未同时保存 SAGE VOR。
- 文件真实性：11/11 由 `file` 识别为 PDF；`pdfinfo` 可读取页数与元数据；`pdftotext` 可抽取正文；首页渲染无黑页、截断或登录页伪装。
- 完整性：所有文件现由 `sources/catalog.yaml` 和 `sources/checksums.sha256` 锁定；规范元数据以 catalog 为准。
- 待办：公开仓库建立发布 allowlist / denylist 时，应直接复用 C 节和 catalog，而不是按 `sources/library/papers/methods/` 或 `sources/library/standards/` 目录整体上传。
