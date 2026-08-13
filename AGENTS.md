# Project Agent Rules

## Mission

研究自然英语阅读 UI 过程证据能够支持哪些行为、过程、认知与技能推断，并先建立不含 LLM、生成式 AI 或 Agent 的 runtime baseline。

## Required reading order

1. `CONTEXT.md`
2. `reports/project_state/CURRENT_STATE.md`
3. `reports/project_state/RESEARCH_QUESTIONS.md`
4. `reports/synthesis/SYSTEM_DESIGN.md`
5. 与任务对应的 `reports/protocols/` 文件
6. `scripts/papers doctor`

不要把 `webchat_raw_materials/` 或迁移包当作日常研究入口。只有 canonical 文档出现矛盾或需要审计来源时，才按 `reports/provenance/SOURCE_POLICY.md` 回查。

## Evidence rules

- 当前用户决定高于历史会话；完整聊天高于 handoff；handoff 高于迁移包。
- 科学事实以论文原文、正式标准和官方资料为权威，历史聊天只提供研究谱系。
- 明确区分 `observed`、`derived`、`inferred`、`validated` 和 `simulation-only`。
- 模型拟合或预测增益不等于构念效度；合成恢复率不等于真人效度。
- 保留 alternatives、uncertainty 和 `UNKNOWN`；禁止为完整画像强制推断。
- 需要全文才能成立的判断必须先通过 `scripts/papers doctor`，并给出稳定 paper ID 与页码/章节。

## AI and human-data boundaries

- Baseline runtime 不得调用 LLM、生成式 AI 或 Agent。
- AI/Agent 可用于 research/experiment plane，但必须遵守 `reports/protocols/AI_RESEARCH_TOOLING_POLICY.md`。
- 任何团队外真人活动先按 `reports/protocols/HUMAN_RESEARCH_GATES.md` 分类。
- `NONRESEARCH_DEBUG_ONLY` 只产生缺陷单，永远不能转成研究数据。
- 真人原始日志、录屏、音频、Webcam、gaze、身份映射和同意材料不得进入公开 Git。

## Workspace and publication

- Canonical 研究资产写入 `reports/`；论文全文与索引写入 `papers/`。
- 不移动或改名历史资产，除非同时更新 catalog、crosswalk、README 和链接验证。
- 不删除 raw materials；它们是本地冻结的追溯证据，并被 `.gitignore` 排除。
- 新增论文同时更新 `papers/catalog.yaml` 和 `papers/checksums.sha256`。
- 公布 GitHub 仓库、Release 或第三方 PDF 是公开发布；必须在最终审计后取得用户的再次明确批准。
- 密钥、token、密码、可识别或假名化真人数据不进代码、commit 或日志。

## Verification

每次变更至少运行与范围相称的检查。全仓知识/论文变更运行 `scripts/verify`；论文变更至少运行 `scripts/papers doctor`；代码变更运行测试与 lint。失败或未验证项保持 `pending`，不得写成完成。
