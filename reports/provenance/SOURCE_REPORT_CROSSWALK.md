# 外部来源与报告交叉索引

本文件解决现有报告中的来源编号、历史 basename 与当前 `sources/` 路径之间的断链。它是路径解析层，不改写历史结论；目录重构后仍保留旧编号/文件名。作品身份、版本、权利、路径和 SHA-256 以 [`../../sources/catalog.yaml`](../../sources/catalog.yaml) 为准。

## 解析规则

1. 报告中的 `A1`、`B3`、`UIB-005` 等编号先解析为 catalog 的稳定 `id`。
2. 报告中的旧 basename 只作为 `aliases`；实际打开文件时使用 `local_path`。
3. 文件名年份不一定是正式出版年份；引用年份使用 catalog 的 `year`。
4. 标题相同不代表文件重复。`D5`/`UIB-005` 与 `D6`/`UIB-007` 是同一作品的不同本地 PDF 版本。
5. `UIB-088` 保留原编号。在外部编号来源得到核实前，不改为 `UIB-018`。

## A 与 A+：报告编号到当前路径

A 报告没有列出 basename，A+ 报告也没有 PDF Mapping 表；以下以报告中的固定编号和论文标题建立路径。

| 报告编号 | Catalog ID | 当前路径 |
| --- | --- | --- |
| A1 | `A1` | `sources/library/papers/literature/a-e/A/A1_2025_Han_MSRM.pdf` |
| A2 | `A2` | `sources/library/papers/literature/a-e/A/A2_2024_Liu_HMM_NetworkAnalysis.pdf` |
| A3 | `A3` | `sources/library/papers/literature/a-e/A/A3_2025_Xiao_MixtureModeling.pdf` |
| A4 | `A4` | `sources/library/papers/literature/a-e/A/A4_2024_Xiao_StateResponseMM.pdf` |
| A5 | `A5` | `sources/library/papers/literature/a-e/A/A5_2020_Chen_CTDCM.pdf` |
| A+1 | `A_PLUS_1` | `sources/library/papers/literature/a-e/A/A+1_2026_Wang_TEM.pdf` |
| A+2 | `A_PLUS_2` | `sources/library/papers/literature/a-e/A/A+2_2024_Wang_PolytomousEffInd.pdf` |
| A+3 | `A_PLUS_3` | `sources/library/papers/literature/a-e/A/A+3_2024_Fu_ActionSeqTime.pdf` |
| A+4 | `A_PLUS_4` | `sources/library/papers/literature/a-e/A/A+4_2026_Han_SRM_Growth.pdf` |
| A+5 | `A_PLUS_5` | `sources/library/papers/literature/a-e/A/A+5_2026_Xu_RLMM.pdf` |

A+ 报告第 4 行的历史 baseline `gpt-add-group-A-deep-reading.md` 当前解析为 `reports/literature/a-e/A-deep-reading.md`。

## B：旧 basename 到当前路径

| ID | 报告中的旧 basename | 当前路径 |
| --- | --- | --- |
| B1 | `B_2025_Maimaiti_GamifiedSRL.pdf` | `sources/library/papers/literature/a-e/B/B1_2025_Maimaiti_GamifiedSRL.pdf` |
| B2 | `B_2022_He_DTW_Navigation.pdf` | `sources/library/papers/literature/a-e/B/B2_2022_He_DTW_Navigation.pdf` |
| B3 | `B_2015_Naumann_OnlineReadingEngagement.pdf` | `sources/library/papers/literature/a-e/B/B3_2015_Naumann_OnlineReadingEngagement.pdf` |
| B4 | `B_2023_Soyoye_SequenceMining.pdf` | `sources/library/papers/literature/a-e/B/B4_2023_Soyoye_SequenceMining.pdf` |
| B5 | `B_2022_Naumann_StrategyKnowledge.pdf` | `sources/library/papers/literature/a-e/B/B5_2022_Naumann_StrategyKnowledge.pdf` |
| B6 | `B_2025_Naumann_SkilledComprehenders.pdf` | `sources/library/papers/literature/a-e/B/B6_2025_Naumann_SkilledComprehenders.pdf` |
| B7 | `B_2026_Arslan_ResponseFormatsCognitiveProcesses.pdf` | `sources/library/papers/literature/a-e/B/B7_2026_Arslan_ResponseFormatsCognitiveProcesses.pdf` |
| B8 | `B_2023_Tenison_SearchBehaviorsSimulatedEnvironments.pdf` | `sources/library/papers/literature/a-e/B/B8_2023_Tenison_SearchBehaviorsSimulatedEnvironments.pdf` |
| B9 | `B_2023_Arslan_InterpretingPausesProcessData.pdf` | `sources/library/papers/literature/a-e/B/B9_2023_Arslan_InterpretingPausesProcessData.pdf` |
| B10 | `B_2026_Lyu_PurposeInstructionsTaskModels.pdf` | `sources/library/papers/literature/a-e/B/B10_2026_Lyu_PurposeInstructionsTaskModels.pdf` |
| B11 | `B_2025_Wijerathne_RereadBeforeAnswer.pdf` | `sources/library/papers/literature/a-e/B/B11_2025_Wijerathne_RereadBeforeAnswer.pdf` |

## C：旧 basename 到当前路径

| ID | 报告中的旧 basename | 当前路径 |
| --- | --- | --- |
| C1 | `C_2020_Arapakis_MouseAttention.pdf` | `sources/library/papers/literature/a-e/C/C1_2020_Arapakis_MouseAttention.pdf` |
| C2 | `C_2012_Huang_UserSeeUserPoint.pdf` | `sources/library/papers/literature/a-e/C/C2_2012_Huang_UserSeeUserPoint.pdf` |
| C3 | `C_2020_FernandezFontelo_QuestionDifficulty.pdf` | `sources/library/papers/literature/a-e/C/C3_2020_FernandezFontelo_QuestionDifficulty.pdf` |
| C4 | `C_2024_Wilcox_MouseTrackingReading.pdf` | `sources/library/papers/literature/a-e/C/C4_2024_Wilcox_MouseTrackingReading.pdf` |
| C5 | `C_2022_Kirsh_VirtualFingerPointReading.pdf` | `sources/library/papers/literature/a-e/C/C5_2022_Kirsh_VirtualFingerPointReading.pdf` |
| C6 | `C_2025_Latifzadeh_SERPDataset.pdf` | `sources/library/papers/literature/a-e/C/C6_2025_Latifzadeh_SERPDataset.pdf` |
| C7 | `C_2025_Villaizan_AdSight.pdf` | `sources/library/papers/literature/a-e/C/C7_2025_Villaizan_AdSight.pdf` |
| C8 | `C_2022_Meidenbauer_MouseMovementsPersonality.pdf` | `sources/library/papers/literature/a-e/C/C8_2022_Meidenbauer_MouseMovementsPersonality.pdf` |

## D：旧 basename 到当前路径

| ID | 报告中的旧 basename | 当前路径 |
| --- | --- | --- |
| D1 | `D_2025_Wang_MMAD.pdf` | `sources/library/papers/literature/a-e/D/D1_2025_Wang_MMAD.pdf` |
| D2 | `D_2022_Thakur_ChangePointDetection.pdf` | `sources/library/papers/literature/a-e/D/D2_2022_Thakur_ChangePointDetection.pdf` |
| D3 | `D_2017_Aminikhanghahi_ChangePointSurvey.pdf` | `sources/library/papers/literature/a-e/D/D3_2017_Aminikhanghahi_ChangePointSurvey.pdf` |
| D4 | `D_2012_LapuyadeLahorgue_HSMM_Segmentation.pdf` | `sources/library/papers/literature/a-e/D/D4_2012_LapuyadeLahorgue_HSMM_Segmentation.pdf` |
| D5 | `D_2024_Rebmann_TaskLevelEvents.pdf` | `sources/library/papers/literature/a-e/D/D5_2024_Rebmann_TaskLevelEvents.pdf` |
| D6 | `D_2022_Gathani_GrammarVisualizationTaxonomies.pdf` | `sources/library/papers/literature/a-e/D/D6_2022_Gathani_GrammarVisualizationTaxonomies.pdf` |
| D7 | `D_2024_Wang_UnsupervisedSegmentationSurvey.pdf` | `sources/library/papers/literature/a-e/D/D7_2024_Wang_UnsupervisedSegmentationSurvey.pdf` |

## E：旧 basename 到当前路径

| ID | 报告中的旧 basename | 当前路径 |
| --- | --- | --- |
| E1 | `E_2018_Jiao_ProcessData_CognitiveDiagnosis.pdf` | `sources/library/papers/literature/a-e/E/E1_2018_Jiao_ProcessData_CognitiveDiagnosis.pdf` |
| E2 | `E_2025_詹沛达_迷思概念编码.pdf` | `sources/library/papers/literature/a-e/E/E2_2025_詹沛达_迷思概念编码.pdf` |
| E3 | `E_2022_Zhan_ItemExpansionMethod.pdf` | `sources/library/papers/literature/a-e/E/E3_2022_Zhan_ItemExpansionMethod.pdf` |
| E4 | `E_2022_Zhan_ResponseTimesFixationCounts.pdf` | `sources/library/papers/literature/a-e/E/E4_2022_Zhan_ResponseTimesFixationCounts.pdf` |
| E5 | `E_2026_Rajeb_FourComponentJointModeling.pdf` | `sources/library/papers/literature/a-e/E/E5_2026_Rajeb_FourComponentJointModeling.pdf` |
| E6 | `E_2023_Lindner_ProcessDataBlackBox.pdf` | `sources/library/papers/literature/a-e/E/E6_2023_Lindner_ProcessDataBlackBox.pdf` |
| E7 | `E_2023_Fan_SRLTraceThinkAloud.pdf` | `sources/library/papers/literature/a-e/E/E7_2023_Fan_SRLTraceThinkAloud.pdf` |
| E8 | `E_2018_Severino_ReadingComprehensionValidation.pdf` | `sources/library/papers/literature/a-e/E/E8_2018_Severino_ReadingComprehensionValidation.pdf` |

## UI 行为旧编号到 UIB 稳定 ID

`A_tier_notes.md` 中的“一”到“十八”和旧 Notion `[论文 1]` 到 `[论文 18]` 使用的是阅读顺序，不等于 UIB 数字顺序。下面给出一一映射。

| 旧编号 | 稳定 ID | 论文简称 | 当前路径 |
| ---: | --- | --- | --- |
| 论文 1 | `UIB-003` | Process-related User Interaction Logs | `sources/library/papers/literature/ui-interaction/UIB-003-process-related-user-interaction-logs-state-of-the-art-reference-model-and-object.pdf` |
| 论文 2 | `UIB-004` | Screenshot-Based Task Mining | `sources/library/papers/literature/ui-interaction/UIB-004-a-screenshot-based-task-mining-framework-for-disclosing-the-drivers-behind-variabl.pdf` |
| 论文 3 | `UIB-006` | User Behavior Mining | `sources/library/papers/literature/ui-interaction/UIB-006-user-behavior-mining-a-research-agenda.pdf` |
| 论文 4 | `UIB-007` | Grammar-Based Visualization Taxonomies | `sources/library/papers/literature/ui-interaction/UIB-007-a-grammar-based-approach-for-applying-visualization-taxonomies-to-interaction-logs.pdf` |
| 论文 5 | `UIB-008` | Trace Clustering | `sources/library/papers/literature/ui-interaction/UIB-008-trace-clustering-for-user-behavior-mining.pdf` |
| 论文 6 | `UIB-010` | GUI Interaction Logging | `sources/library/papers/literature/ui-interaction/UIB-010-gui-information-based-interaction-logging-and-visualization-for-asynchronous-usabi.pdf` |
| 论文 7 | `UIB-011` | Automated Visual Analysis Classification | `sources/library/papers/literature/ui-interaction/UIB-011-an-analysis-of-automated-visual-analysis-classification-interactive-visualization.pdf` |
| 论文 8 | `UIB-012` | Unsupervised Clickstream Clustering | `sources/library/papers/literature/ui-interaction/UIB-012-unsupervised-clickstream-clustering-for-user-behavior-analysis.pdf` |
| 论文 9 | `UIB-015` | Recovering Reasoning Processes | `sources/library/papers/literature/ui-interaction/UIB-015-recovering-reasoning-processes-from-user-interactions.pdf` |
| 论文 10 | `UIB-016` | Browser Interactions to Predict Task | `sources/library/papers/literature/ui-interaction/UIB-016-using-web-browser-interactions-to-predict-task.pdf` |
| 论文 11 | `UIB-017` | Interaction Traces for Use Case Models | `sources/library/papers/literature/ui-interaction/UIB-017-mining-system-user-interaction-traces-for-use-case-models.pdf` |
| 论文 12 | `UIB-088` | Automatic Macro Mining | `sources/library/papers/literature/ui-interaction/UIB-088-automatic-macro-mining-from-interaction-traces-at-scale.pdf` |
| 论文 13 | `UIB-005` | Recognizing Task-Level Events | `sources/library/papers/literature/ui-interaction/UIB-005-recognizing-task-level-events-from-user-interaction-data.pdf` |
| 论文 14 | `UIB-014` | Mining Problem-Solving Strategies | `sources/library/papers/literature/ui-interaction/UIB-014-mining-problem-solving-strategies-from-hci-data.pdf` |
| 论文 15 | `UIB-009` | Detecting Usability Problems | `sources/library/papers/literature/ui-interaction/UIB-009-detecting-usability-problems-in-mobile-applications-on-the-basis-of-dissimilarity.pdf` |
| 论文 16 | `UIB-013` | Software Operation Data Mining | `sources/library/papers/literature/ui-interaction/UIB-013-understanding-users-behavior-with-software-operation-data-mining.pdf` |
| 论文 17 | `UIB-002` | Shifts in Users' Data Focus | `sources/library/papers/literature/ui-interaction/UIB-002-analyzing-the-shifts-in-users-data-focus-in-exploratory-visual-analysis.pdf` |
| 论文 18 | `UIB-001` | AMUSED | `sources/library/papers/literature/ui-interaction/UIB-001-amused-a-multi-modal-dataset-for-usability-smell-identification.pdf` |

## 新增 Phase 0、方法与标准原文

| Catalog ID | 用途 | 当前路径 | 核验报告 |
| --- | --- | --- | --- |
| `ITEM-001` | 2026 J. Intell. Q-matrix 正文 | `sources/library/papers/domain/Du_Shen_Ma_2026_GenAI_Q_Matrix_EFL_Reading.pdf` | `reports/research/phase-0-item-data-source-audit.md` |
| `ITEM-002` | 上述研究 S1/S2/S3 附件 | `sources/library/study-materials/items/Du_Shen_Ma_2026_GenAI_Q_Matrix_Supplement.pdf` | `reports/research/phase-0-item-data-source-audit.md` |
| `ITEM-003` | Jin & Liu hybrid C-DA 作者稿 | `sources/library/papers/domain/Jin_Liu_2024_Hybrid_CDA_Accepted_Manuscript.pdf` | `reports/research/phase-0-item-data-source-audit.md` |
| `METHOD-001` | simulation study 设计 | `sources/library/papers/methods/2019_Morris_Using_Simulation_Studies.pdf` | `reports/research/methods-and-governance-source-audit.md` |
| `METHOD-002` | LLM qualitative-analysis bias 早期版 | `sources/library/papers/methods/2023_Ashwin_LLM_Qualitative_Analysis_Bias_WPS10597.pdf` | `reports/research/methods-and-governance-source-audit.md` |
| `METHOD-003` | synthetic survey replacements | `sources/library/papers/methods/2024_Bisbee_Synthetic_Replacements.pdf` | `reports/research/methods-and-governance-source-audit.md` |
| `METHOD-004` | recursive synthetic-data model collapse | `sources/library/papers/methods/2024_Shumailov_AI_Models_Collapse.pdf` | `reports/research/methods-and-governance-source-audit.md` |
| `METHOD-005` | ChatGPT vs human qualitative analysis | `sources/library/papers/methods/2024_Wachinger_Prompts_Pearls_Imperfections.pdf` | `reports/research/methods-and-governance-source-audit.md` |
| `METHOD-006` | prompt-design annotation experiment | `sources/library/papers/methods/2025_Atreja_Whats_in_a_Prompt.pdf` | `reports/research/methods-and-governance-source-audit.md` |
| `METHOD-007` | human-centered generative annotation | `sources/library/papers/methods/2025_Pangakis_Keeping_Humans_in_the_Loop.pdf` | `reports/research/methods-and-governance-source-audit.md` |
| `METHOD-008` | human–ChatGPT classroom-dialogue coding comparison | `sources/library/papers/methods/2025_Shin_Co_Coding_Classroom_Dialogue.pdf` | `reports/research/new-user-provided-pdfs-source-audit.md` |
| `METHOD-009` | GRRAS reliability/agreement reporting guideline, IJNS version | `sources/library/papers/methods/2011_Kottner_GRRAS_IJNS.pdf` | `reports/research/new-user-provided-pdfs-source-audit.md` |
| `STANDARD-001` | educational/psychological testing standards | `sources/library/standards/2014_AERA_APA_NCME_Testing_Standards.pdf` | `reports/research/methods-and-governance-source-audit.md` |
| `STANDARD-002` | NIST generative-AI risk profile | `sources/library/standards/2024_NIST_AI_600-1_Generative_AI_Profile.pdf` | `reports/research/methods-and-governance-source-audit.md` |
| `DOMAIN-001` | CSE-based reading cognitive diagnostic model | `sources/library/papers/domain/2024_Zhang_Cognitive_Diagnostic_CSE_Reading.pdf` | `reports/research/new-user-provided-pdfs-source-audit.md` |
| `DOMAIN-002` | TSC 2026 inferential-reading cognitive diagnosis | `sources/library/papers/domain/2026_Du_Ma_From_Coarse_to_Fine.pdf` | `reports/research/phase-0-item-data-source-audit.md` |
| `DOMAIN-003` | PELDiaG multi-CDM reading study | `sources/library/papers/domain/2021_Du_Ma_Multi_CDM_EFL_Reading.pdf` | `reports/research/phase-0-item-data-source-audit.md` |
| `DOMAIN-004` | 2022 CSE 阅读推理认知诊断与成绩报告 | `sources/library/papers/domain/2022_Ma_Du_CSE_Reading_Inference_Cognitive_Diagnosis.pdf` | `reports/research/phase-0-item-data-source-audit.md` |

## 同一作品的不同本地版本

| 作品 | Catalog IDs | 判断边界 |
| --- | --- | --- |
| Recognizing Task-Level Events from User Interaction Data | `D5`, `UIB-005` | DOI 相同，分别服务 D 组和 UIB 组；文件页数、生产信息和 SHA-256 不同 |
| A Grammar-Based Approach for Applying Visualization Taxonomies to Interaction Logs | `D6`, `UIB-007` | DOI 相同，标题和正文对应；PDF 版本与 SHA-256 不同 |

这四个文件均保留。若未来要确定 publisher version、accepted manuscript 或下载来源，应另做版本来源核验，不能由当前文件名推断。

## 尚未闭环的报告 provenance

- C/D/E 的任务书已通过 `LEGACY_REPORT_PROVENANCE.md` 回指到冻结的 Chat 2 原文；D/E 历史反馈原文仍不可得，仅报告内嵌的逐项修订记录存续。该限制不影响可独立回到本地 PDF 核验的科学主张。
- `reports/literature/a-e/README.md` 与 UI 报告 README 只有集合级路径，没有论文级可点击索引；本文件和 catalog 现作为规范解析入口。
- `catalog.yaml` 中 `needs_metadata` 非空的条目表示作者、DOI 等字段尚无足够可靠的本地证据。未知字段没有联网补猜。
