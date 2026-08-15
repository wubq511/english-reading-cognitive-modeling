# 恢复目标完成审计（Recovery Goal Completion Audit）

Status: `COMPLETE; LIVE VERIFIED`
Audit date: 2026-08-14
Published base snapshot: `f3a826c7d4e53e4fdb9bad784a16ffe90646f079`; publication-closeout changes proceed through the protected pull-request workflow

## 审计方法

本审计从用户的恢复目标与后续决定导出需求，然后核验当前文件、Git 状态、本地 PDF 字节、manifest、测试与实时远端状态。通过的 verifier 只用于它实际测试的属性；未解决的访问、研究或发布依赖仍然明确列出。

## 需求到证据矩阵

| ID | 需求 | 权威证据 | 结论 |
| --- | --- | --- | --- |
| `R-01` | 把三份完整聊天与两份 handoff 作为主要恢复证据；migration package 仅作参考 | `SOURCE_POLICY.md`、`RAW_SOURCE_MANIFEST.sha256`、`chatgpt_chathistory/` 下 3 个文件、`handoff/` 下 2 个 | **已证明** — 优先级为用户决定 → 完整聊天 → handoff → migration package；科学事实需要一手文献/官方来源 |
| `R-02` | 无损保留 raw 材料以供日后争议追溯，同时不使其成为日常资产 | raw SHA manifest、`.gitignore`、`AGENTS.md`、`scripts/verify` 本地模式 | **已证明** — 25 个冻结来源文件按 hash 校验通过；raw 目录树保持本地且不被跟踪；日常阅读顺序将其排除 |
| `R-03` | 解决矛盾，避免盲目继承 ChatGPT 结论 | `CONFLICT_REGISTER.md`、`CLAIM_LEDGER.md`、`RECOVERY_LOG.md`、`CURRENT_STATE.md` | **已证明** — package 的 phase 膨胀与来源升级被明确降级；替代方案与 `UNKNOWN` 得到保留 |
| `R-04` | 把当前结果、计划与先前方案恢复为持久的项目资产 | `reports/project_state/`、`reports/synthesis/`、`reports/protocols/`、`reports/literature/` | **已证明** — 当前状态、问题、路线图、架构、测量设计、benchmark 草稿与文献资产都有 canonical 归属位置与 README |
| `R-05` | 让研究人员与 Agent 能理解项目 | 根目录 `README.md`、`AGENTS.md`、`CONTEXT.md`、`CONTRIBUTING.md`、各目录 README | **已证明** — 必读顺序、术语、证据规则、验证命令、人工门禁与发布边界都是明确的 |
| `R-06` | 组织外部来源，把主张连接到原件，并保留旧编号/路径溯源 | `sources/catalog.yaml`、`sources/checksums.sha256`、`SOURCE_REPORT_CROSSWALK.md`、`LEGACY_REPORT_PROVENANCE.md` | **已证明** — 80 条类型化稳定记录与 80 个本地 PDF/附件文件匹配；论文、标准与研究材料有独立路径；遗留 ID 与同作品版本得到保留 |
| `R-07` | 在本地下载所需科学来源，或及时报告访问障碍 | 80 个本地文件；`phase-0-item-data-source-audit.md`；`methods-and-governance-source-audit.md`；`MANUAL_ACTIONS.md` | **已证明，但存在开放研究依赖** — TSC、PELDiaG、Ma & Du 2022、Shin 与 GRRAS 全文已在本地并完成审计；已无剩余的论文全文获取动作，而不可得的题目/数据/权利资产不会被提升为已核验资产 |
| `R-08` | 让协作者及其 Agent 在不把语料放进公开 Git 的前提下恢复精确来源 | `AGENTS.md`、`CLAUDE.md`、`scripts/bootstrap`、`scripts/sources`、`.githooks/`、CLI 测试、`docs/project-management/AGENT_BOOTSTRAP.md` | **已证明** — 两个受支持的 Agent 都会加载根规则，且必须运行并宣告一次 bootstrap；已安装的 Git hooks 自动化 checkout/merge/push 门禁；`doctor`/`sync` 失败即关闭（fail closed）；`tmp/pdfs` 按 hash 导入，只删除核验后的副本 |
| `R-09` | 让 baseline 系统架构不含 AI/Agent，同时允许研究/实验中重要的 AI 使用 | ADR 0002、`AI_RESEARCH_TOOLING_POLICY.md`、`SYSTEM_DESIGN.md` | **已证明** — runtime 平面与研究平面分离；合成/LLM 输出不能确立人类真值或构念效度（construct validity） |
| `R-10` | 把 AI 纵向深化与横向扩展保留为后续研究方向 | `ROADMAP.md`、`RESEARCH_QUESTIONS.md`、`AI_RESEARCH_TOOLING_POLICY.md` | **已证明** — 后续 AI 比较/扩展仍是受门禁约束的研究方向，不是 baseline 实现假设 |
| `R-11` | 科学处理初期的熟人/学生测试与后来的正式研究 | ADR 0004、`HUMAN_RESEARCH_GATES.md`、`MANUAL_ACTIONS.md` | **作为治理机制证明** — H1 仅调试用途与 H2/H3 研究在物理/语义上分离；机构与招募问题保留到后续阶段 |
| `R-12` | 准备一个公开协作仓库，不泄露 raw 证据、来源原件、密钥或真人数据 | `PUBLICATION_READINESS.md`、公开目录树、`.gitignore`、公开验证模式 | **已证明** — 98 个文件的初始快照与 99 个文件的发布收尾包含零个 PDF、raw 恢复文件、收件箱文件或第三方来源原件；来源、密钥、路径、引文与公开模式检查全部通过 |
| `R-13` | 实际创建并发布公开 GitHub 仓库 | `https://github.com/wubq511/english-reading-cognitive-modeling`、GitHub Actions run `31786325757`、实时 `main` 保护 API | **已证明** — 仓库已公开；初始快照通过 `verify`；`main` 要求 PR + 严格 `verify`，保护适用于管理员，并拒绝 force-push/删除 |

## 恢复确立的科学状态

- `Phase 2A` 仅设计关闭；实现仍然开放。
- `Phase 0` 开放，因为没有已完成权利清除、配备独立 answer key 的候选题库（candidate item bank）。
- `Phase 3` 是 benchmark 规范草稿；`Phase 4` 只是被宣布，尚未完成。
- 没有可运行的 runtime、benchmark 结果、人类试测、正式实验或经过验证的认知推断模型。
- 下一个可执行的工程里程碑是 `BENCH-E0`：在可用题包关闭或选定刻意合成的工程夹具之后，实现 raw 日志、确定性状态重建与回放保真。

## 验证覆盖

以下证据从已提交的工作区重新运行：

```text
39 unit tests                                      PASS locally; public clone skips only absent-byte checks
scripts/verify (local)                            PASS: 73 Markdown, 80 sources, 25 raw sources
scripts/verify --public                           PASS: public snapshot boundary
scripts/sources doctor                             PASS: 80/80 exact local dependencies
scripts/sources sync                               PASS: no missing direct-public dependency
git diff --cached --check (before commit)         PASS
prospective forbidden-path and secret signatures  no matches
```

verifier 并不声称六份遗留文献报告中的每一句话都已对照其 PDF 独立重读。那样更宽泛的主张会超出已执行的审计范围。主要结论类别在 `existing-literature-validation-audit.md` 中做了抽样，未来重大用途必须引用稳定来源 ID 及页码/章节证据。

## 目标结论

需求 `R-01` 至 `R-13` 在其声明范围内均已证明。恢复目标已完成：canonical 研究资产、溯源、来源恢复门禁、协作者/Agent 引导、公开仓库边界、实时 CI 与受保护的协作都已建立。开放的题目/数据权利、实现、伦理与实证验证工作是未来研究，不是未完成的恢复。
