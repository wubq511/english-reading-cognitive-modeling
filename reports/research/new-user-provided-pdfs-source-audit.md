# 用户提供的五份 PDF 来源、版本与权利审计

> Follow-up: this report preserves the five-file batch audit. Later on 2026-08-14, the user separately provided Ma & Du 2022, now registered as `DOMAIN-004`; its current findings and 2022/TSC/J. Intell. lineage ruling are owned by [`phase-0-item-data-source-audit.md`](phase-0-item-data-source-audit.md). Therefore statements below that the *five-file batch itself* did not contain Ma & Du 2022 remain historically correct, but no current full-text acquisition gap remains.

- 审计日期：2026-08-14
- 输入：tmp/pdfs 中用户提供的 5 份 PDF
- 范围：书目身份、版本、官方来源、直接获取与再分发权利
- 审计阶段未执行：先不移动原件，避免身份/权利判断尚未完成时误归档
- 审计后处置：5 份文件已按 SHA 导入 `sources/` 并登记；`tmp/pdfs/` 对应副本在目标复验成功后清理

## 当前登记

| 临时 ID | Stable source ID | Canonical path |
| --- | --- | --- |
| USERPDF-01 | `DOMAIN-001` | `sources/library/papers/domain/2024_Zhang_Cognitive_Diagnostic_CSE_Reading.pdf` |
| USERPDF-02 | `METHOD-008` | `sources/library/papers/methods/2025_Shin_Co_Coding_Classroom_Dialogue.pdf` |
| USERPDF-03 | `DOMAIN-002` | `sources/library/papers/domain/2026_Du_Ma_From_Coarse_to_Fine.pdf` |
| USERPDF-04 | `METHOD-009` | `sources/library/papers/methods/2011_Kottner_GRRAS_IJNS.pdf` |
| USERPDF-05 | `DOMAIN-003` | `sources/library/papers/domain/2021_Du_Ma_Multi_CDM_EFL_Reading.pdf` |

规范元数据、许可、SHA 与路径以 `sources/catalog.yaml` 为唯一机器权威；本报告保留审计推理与一手来源证据。

## 判定口径

acquisition_status 与 redistribution_status 独立：

- DIRECT_PUBLIC：出版商或正式机构的 HTTPS PDF 端点可在无账号、cookie、订阅凭据或绕过的条件下返回 PDF。
- MANUAL_ONLY：需要机构访问、购买、正常浏览器人工流程或作者提供；HTTP 403 不冒充为可自动同步。
- REDISTRIBUTION_ALLOWED：该具体版本载有明确开放许可，仍须遵守署名、非商业、禁止演绎和第三方材料例外。
- RESTRICTED：未核验到适用于该文件的开放再分发许可；合法本地阅读不等于可上传公共 Git。

本轮核验 SHA-256、页数、PDF 元数据、首页和版权栏文本，并渲染首屏目检。官方 PDF 端点于 2026-08-14 以无凭据 HTTPS 请求实测。

## 结论

| ID | 具体版本 | acquisition_status | redistribution_status |
| --- | --- | --- | --- |
| USERPDF-01 | Zhang, Hamzah & Jamaludin 2024 出版商 VOR；与官方 PDF 字节相同 | DIRECT_PUBLIC | REDISTRIBUTION_ALLOWED，CC BY-NC 4.0 条件 |
| USERPDF-02 | Shin 2025 Wiley VOR 内容；本地容器有 iText 后处理记录 | MANUAL_ONLY | REDISTRIBUTION_ALLOWED，CC BY-NC-ND 条件 |
| USERPDF-03 | Du & Ma 2026 Elsevier VOR | MANUAL_ONLY | RESTRICTED |
| USERPDF-04 | Kottner et al. 2011 IJNS 再发表 VOR | MANUAL_ONLY | RESTRICTED |
| USERPDF-05 | Du & Ma 2021 Springer VOR | MANUAL_ONLY | RESTRICTED |

USERPDF-02/03/04/05 分别补齐原人工获取队列中的 Shin、TSC、GRRAS 和 PELDiaG 全文。USERPDF-01 是 Zhang 等人 2024 的另一篇研究，**不是** Ma & Du 2022《中国考试》论文；DOI [10.19360/j.cnki.11-3303/g4.2022.12.001](https://doi.org/10.19360/j.cnki.11-3303/g4.2022.12.001) 对应的 2022 全文仍未由这批文件补齐。

## USERPDF-01

- Local input filename: A Cognitive Diagnostic Model of Reading Ability based on China’s Standards of English Language Ability.pdf
- SHA-256: 4598cbaacef18759b37986c1cfcc8ec9e923bd3aa7c6a090d82322f3f9f4fd55
- Pages: 16
- 正式题名：A Cognitive Diagnostic Model of Reading Ability Based on China’s Standards of English Language Ability
- 作者：Zhe Zhang, Mohd Isa Hamzah, Khairul Azhar Jamaludin
- 出版：Forum for Linguistic Studies 6(6), 800-815 (2024)；online 2024-12-11
- DOI：[10.30564/fls.v6i6.7551](https://doi.org/10.30564/fls.v6i6.7551)
- 版本：出版商 VOR。本轮从官方端点取得的 756,572-byte 文件与本地输入 SHA-256 完全相同。
- 官方 landing：[article page](https://journals.bilpubgroup.com/index.php/fls/article/view/7551)
- 官方 PDF：[publisher PDF](https://journals.bilpubgroup.com/index.php/fls/article/download/7551/5664/36220)
- 获取：DIRECT_PUBLIC；官方端点无认证返回 HTTP 200、application/pdf。
- 许可与再分发：PDF 首页和作品页均标记 CC BY-NC 4.0。判为 REDISTRIBUTION_ALLOWED，但仅限非商业用途，须署名、保留 DOI/许可、标明改动并另审第三方材料。作品页 License 区错误列出无关版权人；作者身份以 PDF 首页和页面 Authors 区为准。
- 精确定位：本地 PDF p.1 / 印刷页 800；出版商页面 Authors、DOI、Downloads、Issue、License 区。

## USERPDF-02

- Local input filename: Computer Assisted Learning - 2025 - Shin - Co‐Coding Classroom Dialogue  A Single Researcher Case Study of ChatGPT‐Assisted.pdf
- SHA-256: 60a83dda506a0491baa33a8be8bcd1f9b1524c5367d7518174887c6c1b0fa62b
- Pages: 16
- 正式题名：Co-Coding Classroom Dialogue: A Single Researcher Case Study of ChatGPT-Assisted Analysis in Science Education
- 作者：Eunhye Shin
- 出版：Journal of Computer Assisted Learning 41(4), e70089 (2025)；first published 2025-07-02
- DOI：[10.1111/jcal.70089](https://doi.org/10.1111/jcal.70089)
- 版本：Wiley VOR 内容和版式。pdfinfo 同时显示 modified using iText 4.2.0 与 2026-08-14 ModDate，因此不能声称本地 bitstream 与出版商原始字节相同。
- 官方 landing：[Wiley article](https://onlinelibrary.wiley.com/doi/10.1111/jcal.70089)
- 官方 PDF 候选：[pdf](https://onlinelibrary.wiley.com/doi/pdf/10.1111/jcal.70089)、[pdfdirect](https://onlinelibrary.wiley.com/doi/pdfdirect/10.1111/jcal.70089)
- 获取：MANUAL_ONLY；两个官方端点对本轮无凭据请求均返回 HTTP 403 和 HTML，不能作为稳定自动 sync 源。
- 许可与再分发：PDF 首页明确为 CC BY-NC-ND，允许正确引用、非商业、无修改/改编的分发。判为 REDISTRIBUTION_ALLOWED，但应原样保存；公开前最好用正常浏览器重取官方副本并比较 SHA，避免把未知内容改动当作未改编原件。
- 精确定位：本地 PDF p.1；Wiley 页面作者、First published、引用和 DOI 区。

## USERPDF-03

- Local input filename: From coarse to fine.pdf
- SHA-256: d62d4273c249e294e93d09224a21baa77bb26d1c7d0d8e568b6ea29f1e7565fe
- Pages: 13
- 正式题名：From Coarse to Fine: A Cognitive Diagnosis of EFL Learners’ Inferential Ability in EFL Reading
- 作者：Wenbo Du, Xiaomei Ma
- 出版：Thinking Skills and Creativity 59, 102022 (March 2026)；available online 2025-09-26
- DOI：[10.1016/j.tsc.2025.102022](https://doi.org/10.1016/j.tsc.2025.102022)
- 版本：Elsevier VOR。规范引用年为卷期年 2026；DOI 和首页版权年为 2025，这不是版本冲突。
- 官方 landing：[ScienceDirect](https://www.sciencedirect.com/science/article/pii/S1871187125002706)
- 官方 PDF 候选：[ScienceDirect PDF](https://www.sciencedirect.com/science/article/pii/S1871187125002706/pdfft?isDTMRedir=true&download=true)
- 获取：MANUAL_ONLY；无凭据 PDF 请求返回 HTTP 403 和 HTML。
- 许可与再分发：首页标记 © 2025 Elsevier Ltd., all rights reserved，并单列 TDM/AI training 权利保留。判为 RESTRICTED；可作为用户合法取得的本地研究副本，不上传公共 Git/Release。
- 精确定位：本地 PDF p.1；ScienceDirect 的卷期、题名、DOI 和摘要区。

## USERPDF-04

- Local input filename: Guidelines for Reporting Reliability and Agreement Studies (GRRAS) were proposed.pdf
- SHA-256: a8dbb6a808e510aa534f1e583eda90ec04e2677b252f19bbe3bda1045a762cfc
- Pages: 11
- 正式题名：Guidelines for Reporting Reliability and Agreement Studies (GRRAS) Were Proposed
- 作者：Jan Kottner, Laurent Audigé, Stig Brorson, Allan Donner, Byron J. Gajewski, Asbjørn Hróbjartsson, Chris Roberts, Mohamed Shoukri, David L. Streiner
- 出版：International Journal of Nursing Studies 48, 661-671 (2011)
- DOI：[10.1016/j.ijnurstu.2011.01.016](https://doi.org/10.1016/j.ijnurstu.2011.01.016)
- 版本：Elsevier IJNS 再发表 VOR。首页说明其经许可再发表自 Journal of Clinical Epidemiology 64, 96-106；原 JCE 版 DOI 为 [10.1016/j.jclinepi.2010.03.002](https://doi.org/10.1016/j.jclinepi.2010.03.002)。两者是同一作品的不同期刊版本，本地文件必须按 IJNS DOI 登记。
- 官方 landing：[ScienceDirect IJNS](https://www.sciencedirect.com/science/article/pii/S0020748911000368)
- 官方 PDF 候选：[ScienceDirect PDF](https://www.sciencedirect.com/science/article/pii/S0020748911000368/pdfft?isDTMRedir=true&download=true)
- 辅助正式来源：[EQUATOR record](https://www.equator-network.org/reporting-guidelines-study-design/reliability-and-agreement-studies/)；[EQUATOR checklist](https://www.equator-network.org/wp-content/uploads/2012/12/GRRAS-checklist-for-reporting-of-studies-of-reliability-and-agreement.pdf)。checklist 不是本地 11 页论文的替代版本。
- 获取：MANUAL_ONLY；无凭据 PDF 请求返回 HTTP 403 和 HTML，未找到这个 IJNS 版本的官方公开直下端点。
- 许可与再分发：PDF 标记 © 2011 Published by Elsevier Ltd.，未提供面向读者的开放许可。期刊间再发表许可不转化为读者再分发权。判为 RESTRICTED。
- 精确定位：本地 PDF p.1 / 印刷页 661；ScienceDirect IJNS 页面；EQUATOR checklist 首页引文。

## USERPDF-05

- Local input filename: Probing_whats_behind_the_test_score_application_o.pdf
- SHA-256: e0df9daf7f73e2381403d88102bb89b5a2c95f0ee7d02b2693f97c4b008ae7bc
- Pages: 27
- 正式题名：Probing What’s Behind the Test Score: Application of Multi-CDM to Diagnose EFL Learners’ Reading Performance
- 作者：Wenbo Du, Xiaomei Ma
- 出版：Reading and Writing 34, 1441-1466 (2021)；online 2021-01-22
- DOI：[10.1007/s11145-021-10124-x](https://doi.org/10.1007/s11145-021-10124-x)
- 版本：Springer VOR；官方页面明确登记 Version of record: 22 January 2021，本地期刊版式、页码、DOI 和版权栏一致。
- 官方 landing：[Springer Nature](https://link.springer.com/article/10.1007/s11145-021-10124-x)
- 官方 PDF 候选：[Springer PDF route](https://link.springer.com/content/pdf/10.1007/s11145-021-10124-x.pdf)
- 获取：MANUAL_ONLY；官方页明确为 subscription content；无凭据 PDF URL 重定向到 HTML 页面。
- 许可与再分发：首页标记作者向 Springer Nature B.V. 授予 exclusive licence，页脚标记 rights reserved；页面只有 Reprints and permissions，无开放许可。判为 RESTRICTED。
- 精确定位：本地 PDF p.1 / 印刷页 1441；Springer 页 Published、Access this article、Rights and permissions、About this article 区。

## 后续导入约束

1. 导入时以上述 SHA-256 识别文件，不从文件名猜测身份。
2. USERPDF-01 不得用于关闭 Ma & Du 2022 获取项。
3. USERPDF-04 按 IJNS 再发表版本登记，并以 same_work 等版本关系关联 JCE 原版；不得把两个 DOI 合并。
4. 公共 Git 默认继续排除全部 PDF。即使 USERPDF-01/02 有条件开放许可，也只能经单文件审批、署名和第三方材料复核后发布。
5. 全文到手只关闭“全文缺失”；题本、answer key、Q-matrix、响应数据、伦理与再部署权仍是独立 gate。

## 一手来源

以下来源访问日期均为 2026-08-14：

- [Forum for Linguistic Studies - Zhang et al.](https://journals.bilpubgroup.com/index.php/fls/article/view/7551)
- [Wiley Online Library - Shin](https://onlinelibrary.wiley.com/doi/10.1111/jcal.70089)
- [ScienceDirect - Du & Ma TSC](https://www.sciencedirect.com/science/article/pii/S1871187125002706)
- [ScienceDirect - Kottner et al. IJNS](https://www.sciencedirect.com/science/article/pii/S0020748911000368)
- [Springer Nature - Du & Ma](https://link.springer.com/article/10.1007/s11145-021-10124-x)
- [EQUATOR Network - reliability and agreement studies](https://www.equator-network.org/reporting-guidelines-study-design/reliability-and-agreement-studies/)
