# 当前研究状态

> 截至：2026-08-14
> 状态类型：canonical 恢复 + 公共协作
> 运行时实现：未开始

## 一句话状态

项目已经完成历史研究的本地恢复、文献资产索引和题目无关的测量设计整理，但尚未完成题目资产、实现、开发数据、benchmark 或真人研究；下一项研究工作不是“继续选最终算法”，而是闭合题目/数据资产并把 measurement 设计实现为可回放的工程基线。

## 现有且可用

| 资产 | 当前证据 | 状态 |
| --- | --- | --- |
| 三份完整网页会话 + 两份 handoff | 本地文件与 SHA-256 已核对 | 已冻结的恢复证据 |
| 公共协作仓库 | `wubq511/english-reading-cognitive-modeling`；首次 CI 通过，`main` 强制 PR + `verify`，管理员不可绕过 | 已上线且受保护 |
| Baseline→H2 Wayfinder 协作地图 | [父地图 #2](https://github.com/wubq511/english-reading-cognitive-modeling/issues/2) + 12 个原生 sub-issues/dependency edges；当前只拆 decision tickets，未生成 execution tickets | **进行中 / 决策开放** |
| A/A+/B/C/D/E 深读 | 44 PDF + 6 份深读报告；均有页码 Evidence Index | 可用，附 provenance 注意事项 |
| UI 行为文献研究 | 18 PDF + 笔记；旧编号 crosswalk 已建立 | 可用 |
| UI 作为测量仪器的研究线 | 已确认需要独立考察 UI 对行为、缺失、可观测性和 estimand 的影响；尚无 variant 实验或结果 | **设计要求 / 实验未开始** |
| 外部来源目录 | 80 PDF/附件，均有稳定 ID、类型、路径与 SHA；论文、标准、题目附件已分层，逐版本权利在已审计范围内记录 | 本地就绪；来源门禁已自动化 |
| 系统概念架构 | 聊天与 handoff 反复收敛，已恢复到 `synthesis/` | 研究设计，非实现 |
| Phase 2A measurement/validation | 原始会话明确标记题目无关设计基本关闭 | 设计已关闭；实现开放 |
| AI 与真人研究治理 | 2026-08-14 经专项研究和用户确认 | 现行政策 |

## 如实阶段审计

| 历史阶段 | 当前证据 | Canonical 状态 |
| --- | --- | --- |
| Phase 0 — 题目与数据来源 | 已落地 2026 J. Intell. 正文+S2、Jin & Liu 作者稿、PELDiaG 2021、Ma & Du 2022、TSC 2026 和 Zhang et al. 2024；2022/TSC 的共享测验/Q 矩阵研发谱系已由逐单元格相同的 `20 × 8` 矩阵确认，但完整题本、独立答案键、逐题权利与响应数据关系未闭合，Candidate Bank V1 和 pilot 规则未冻结 | **OPEN / 核心全文已获取，可用题本缺失** |
| Phase 1 — 认知目标与可观测性 | 目标矩阵、不可识别边界和 `UNKNOWN` 原则在聊天/handoff 中已形成 | **SOURCE-RECOVERED 设计**；未做真人效度实验 |
| Phase 2A — 测量与验证框架 | Raw event、replay、recall、annotation、provenance 等题目无关框架被明确标记 `RESEARCH DESIGN CLOSED` | **设计已关闭**；未实现 |
| Phase 2B — 题目专属实例化 | 明确等待具体题目和 pilot | **未开始 / 受题目 + pilot 阻塞** |
| Phase 3 — 开发数据集 + benchmark | 聊天提出三层开发数据、benchmark、metrics 和 splits；随后只宣布“开始深研” | **草案规范**；没有数据或结果 |
| Phase 4 — 实现 DAG/门禁 | 聊天只宣布下一轮将设计 | **未完成**；迁移包中的完整实现 DAG 是迁移包来源的提案 |
| Phase 5+ — 真人 pilot/主要研究/泛化 | 没有伦理批准、招募、采集或实验 | **未开始** |

## 已锁定的设计边界

- Baseline runtime 不含 LLM、生成式 AI 或 Agent；AI/Agent 只在 research/experiment plane 受控使用。
- 低干扰、paper-native UI：左 passage 独立滚动，右侧一次一道题，可自由跳题、划线、排除/恢复选项和修改答案；不强制解释或 confidence。
- Raw event 不写认知；原始事件 append-only，派生版本可重算。
- `viewport != attention`、`pointer != gaze`、`dwell != difficulty`、`revisit != confusion`。
- 行为、过程、认知和跨题技能分层；每个映射保留证据、替代解释、适用范围和版本。
- Production 只依赖自然 `COL-L0 + COL-L1`；`COL-L2`、replay、recall、人类编码和可选传感器属于 research plane。
- Synthetic 只支持工程与 DGM 条件下的声明，不进入真人构念效度证据。
- Response-only student model baseline 永久保留；process feature 必须先过构念效度门。

## 尚未成真

以下陈述目前都没有证据支持，禁止在文档或论文中写成已完成：

- “系统已经跑通”或“算法已达到最优”；
- “HMM/HSMM/TEM/RLMM 是本项目最佳方法”；
- “pointer 对 focus 有稳定增量”；
- “交互轨迹可以可靠识别 Search/Verification/Confusion”；
- “模型输出已具有构念效度”；
- “已有真人 pilot 或正式样本”；
- “Phase 0/3/4 已关闭”；

## 近期下一步工作

以下工作由 [Wayfinder 父地图 #2](https://github.com/wubq511/english-reading-cognitive-modeling/issues/2) 协调；Phase 状态仍由本文件维护，Issue 不成为第二份状态真相。

1. 闭合 Phase 0：获取或自建权利清晰的 passage/item 资产、建立独立答案键/evidence spans、Candidate Bank V1 与 pilot 选择协议。
2. 向作者核对 2021 PELDiaG、2022 CSE、TSC 2026 与 J. Intell. 2026 的题本、答案键、Q 矩阵版本和响应数据谱系；2022 全文获取项已关闭。
3. 实现 `BENCH-E0`：raw logging、确定性 state reconstruction 与 replay fidelity。
4. 建立 engineering synthetic；它只验证 schema/invariants，不验证 cognition。
5. 在 H2 获批并具备题目后，设计小规模真人 pilot；此前不采研究性真人数据。
6. 在实现 baseline UI 时先冻结 instrument contract 并通过 `BENCH-E0`；UI variant 的优选/确认必须按 RQ0 和 H2 gate 独立设计。

## 未决的外部依赖

- 2022 CSE、PELDiaG 与 TSC 全文均已取得，但其完整题本、响应数据、答案键与再部署权仍需作者/实验室协调。
- 2026 J. Intell. S2 已本地可得，但无独立官方答案键/逐题来源与权利清单；2022/TSC 的共享研发谱系已确认，J. Intell. 的题本文字身份与 2022/J. Intell. 是否复用同一响应矩阵仍未证实。
- 实验室/学校伦理流程、PI 资格、学生招募和敏感模态要求需书面确认。
- 公开分发任何第三方 PDF 前必须逐篇取得再分发依据。
