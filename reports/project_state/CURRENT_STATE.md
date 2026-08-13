# Current Research State

> As of: 2026-08-14
> Status type: canonical local recovery
> Runtime implementation: not started

## One-sentence state

项目已经完成历史研究的本地恢复、文献资产索引和题目无关的测量设计整理，但尚未完成题目资产、实现、开发数据、benchmark 或真人研究；下一项研究工作不是“继续选最终算法”，而是闭合题目/数据资产并把 measurement 设计实现为可回放的工程基线。

## What exists and is usable

| Asset | Current evidence | Status |
| --- | --- | --- |
| 三份完整网页会话 + 两份 handoff | 本地文件与 SHA-256 已核对 | Frozen recovery evidence |
| A/A+/B/C/D/E 深读 | 44 PDF + 6 份深读报告；均有页码 Evidence Index | Usable with provenance caveats |
| UI 行为文献研究 | 18 PDF + 笔记；旧编号 crosswalk 已建立 | Usable |
| 论文目录 | 74 PDF/附件，均可解析、未加密、SHA 已记录；新增 3 份 Phase 0、7 份方法、2 份标准原文 | Locally ready; per-version rights recorded where audited |
| 系统概念架构 | 聊天与 handoff 反复收敛，已恢复到 `synthesis/` | Research design, not implementation |
| Phase 2A measurement/validation | 原始会话明确标记题目无关设计基本关闭 | Design closed; implementation open |
| AI 与真人研究治理 | 2026-08-14 经专项研究和用户确认 | Active policy |

## Honest phase audit

| Historical phase | What the raw record proves | Canonical status |
| --- | --- | --- |
| Phase 0 — Item & data sources | 已完成一手来源专项，落地 2026 J. Intell. 正文+S2 附件及 Jin & Liu 作者稿；但 S2 无独立官方答案键/逐题权利，PELDiaG/2022 CSE/TSC 全文与数据未取得，Candidate Bank V1 和 pilot 规则未冻结 | **OPEN / source audit completed, usable item bank absent** |
| Phase 1 — Cognitive target & observability | 目标矩阵、不可识别边界和 `UNKNOWN` 原则在聊天/handoff 中已形成 | **SOURCE-RECOVERED DESIGN**；未做真人效度实验 |
| Phase 2A — Measurement & validation framework | Raw event、replay、recall、annotation、provenance 等题目无关框架被明确标记 `RESEARCH DESIGN CLOSED` | **DESIGN CLOSED**；未实现 |
| Phase 2B — Item-specific instantiation | 明确等待具体题目和 pilot | **NOT STARTED / BLOCKED BY ITEMS + PILOT** |
| Phase 3 — Development dataset + benchmark | 聊天提出三层开发数据、benchmark、metrics 和 splits；随后只宣布“开始深研” | **DRAFT SPECIFICATION**；没有数据或结果 |
| Phase 4 — Implementation DAG/gates | 聊天只宣布下一轮将设计 | **NOT COMPLETED**；迁移包中的完整实现 DAG 是 package-origin proposal |
| Phase 5+ — Human pilot/main/generalization | 没有伦理批准、招募、采集或实验 | **NOT STARTED** |

## Locked design boundaries

- Baseline runtime 不含 LLM、生成式 AI 或 Agent；AI/Agent 只在 research/experiment plane 受控使用。
- 低干扰、paper-native UI：左 passage 独立滚动，右侧一次一道题，可自由跳题、划线、排除/恢复选项和修改答案；不强制解释或 confidence。
- Raw event 不写认知；原始事件 append-only，派生版本可重算。
- `viewport != attention`、`pointer != gaze`、`dwell != difficulty`、`revisit != confusion`。
- 行为、过程、认知和跨题技能分层；每个映射保留证据、替代解释、适用范围和版本。
- Production 只依赖自然 `COL-L0 + COL-L1`；`COL-L2`、replay、recall、人类编码和可选传感器属于 research plane。
- Synthetic 只支持工程与 DGM 条件下的声明，不进入真人构念效度证据。
- Response-only student model baseline 永久保留；process feature 必须先过构念效度门。

## Not yet true

以下陈述目前都没有证据支持，禁止在文档或论文中写成已完成：

- “系统已经跑通”或“算法已达到最优”；
- “HMM/HSMM/TEM/RLMM 是本项目最佳方法”；
- “pointer 对 focus 有稳定增量”；
- “交互轨迹可以可靠识别 Search/Verification/Confusion”；
- “模型输出已具有构念效度”；
- “已有真人 pilot 或正式样本”；
- “Phase 0/3/4 已关闭”；
- “公开 GitHub 仓库已经建立”。

## Immediate next work

1. 闭合 Phase 0：获取或自建权利清晰的 passage/item 资产、建立独立答案键/evidence spans、Candidate Bank V1 与 pilot 选择协议。
2. 通过实验室/机构渠道获取 2022 CSE、TSC 2026、PELDiaG 三份受限全文，并向作者询问三者题本/数据谱系。
3. 实现 `BENCH-E0`：raw logging、确定性 state reconstruction 与 replay fidelity。
4. 建立 engineering synthetic；它只验证 schema/invariants，不验证 cognition。
5. 在 H2 获批并具备题目后，设计小规模真人 pilot；此前不采研究性真人数据。

## Open external dependencies

- PELDiaG、2022 CSE 与 TSC 2026 的全文、item/data 资产和权利状态仍需实验室订阅或作者协调。
- 2026 J. Intell. S2 已本地可得，但无独立官方 answer key/逐题来源与权利清单；2022→2026 “同题本/同响应矩阵”未被证实，只能标为研发谱系推论。
- 实验室/学校伦理流程、PI 资格、学生招募和敏感模态要求需书面确认。
- 公开分发任何第三方 PDF 前必须逐篇取得再分发依据。
