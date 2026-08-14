# Project Agent Rules

## Mission and phases

研究自然英语阅读 UI 过程证据能够支持哪些行为、过程、认知与技能推断。

1. 当前阶段先实现并尽量优化不含 LLM、生成式 AI 或 Agent 的 runtime baseline，得到可复现的能力上限与失败边界。
2. Baseline 对应 Module 的 Interface、数据、split、metric 和结果冻结后，再研究两类 AI 扩展：纵向提升既有环节，或横向增加 baseline 无法完成的新能力。
3. AI/Agent 在当前 research/experiment plane 已经允许且重要，可辅助文献、编码、合成数据、实验编排、候选标注和 QA；其输出始终是待验证工件，不能自造真值。

当前阶段和完成度只以 `reports/project_state/CURRENT_STATE.md` 为准，不在本文件维护动态状态。

## Start every task

1. 运行 `scripts/bootstrap`；若 sources gate 未通过，停止依赖缺失原件的工作并输出精确人工获取项。
2. 依次阅读 `CONTEXT.md`、`reports/project_state/CURRENT_STATE.md`、`reports/project_state/RESEARCH_QUESTIONS.md`。
3. 系统设计读 `reports/synthesis/SYSTEM_DESIGN.md`；来源/结论冲突读 `reports/provenance/SOURCE_POLICY.md`。
4. 涉及 AI、真人、实验或数据时，分别读取对应 `reports/protocols/`、`experiments/README.md` 或 `data/README.md`。

不要把 `webchat_raw_materials/` 或 migration package 当作日常入口。只有 canonical 资产矛盾或需要审计谱系时，才按 `SOURCE_POLICY.md` 回查。

## Evidence invariants

- 当前用户决定高于历史项目状态；科学事实以原文、正式标准、官方资料和可复现实验为权威。
- 区分 `observed`、`derived`、`inferred`、`validated` 与 `simulation-only`；模型拟合、预测增益和 synthetic recovery 都不自动构成构念效度。
- 保留 alternatives、uncertainty、negative/null result 与 `UNKNOWN`；禁止为了完整画像强制推断。
- 依赖全文的判断必须先通过 `scripts/sources doctor`，引用稳定 source ID 与页码/章节。
- Raw event append-only；派生资产必须可回到输入、代码、配置和版本。

## Single-source knowledge maintenance

- 每个事实只指定一个 owner 文档；其他文件只给受众所需摘要并链接 owner，不复制整段规则、清单或当前状态。
- 修改观点、决策、ID、路径或阶段状态时：先更新 owner；全仓搜索旧表述；更新或改为指针；重要变更记录 supersession/ADR；最后运行 `scripts/verify`。
- 不静默覆盖旧实验或原始证据。保留可审计版本关系，但不要让已被取代的结论继续以“当前事实”出现。
- 主题 owner 与变更流程由 `reports/provenance/SOURCE_POLICY.md` 唯一维护。

## Sources and workspace

- `reports/`：项目产出的 canonical 研究资产；`sources/`：外部论文、标准、题目和第三方数据；`data/`：项目生成/采集数据；`artifacts/`：可重建运行输出。
- 所有人工下载论文统一放 `tmp/pdfs/`。Agent 核实身份、版本、权利和 SHA 后更新 catalog，再运行 `scripts/sources inbox`；只有迁移后复验通过才删除 inbox 副本。
- 新增来源必须同步更新 `sources/catalog.yaml`、`sources/checksums.sha256` 和必要 crosswalk/报告；不猜 DOI、许可或版本。
- 不移动或改名已有来源，除非同一变更更新 catalog、checksum、crosswalk、链接和验证。
- `webchat_raw_materials/` 本地冻结且不删除；它是追溯证据，不是研究资产。

## AI, human data, and publication

- Baseline runtime 不调用 AI/Agent；研究外环遵守 `AI_RESEARCH_TOOLING_POLICY.md`。
- 团队外真人活动先按 `HUMAN_RESEARCH_GATES.md` 分类；`NONRESEARCH_DEBUG_ONLY` 永不转研究数据。
- 真人原始/假名化数据、录屏、音视频、gaze、身份映射、同意材料、密钥和 token 不进公开 Git、日志或未经批准的外部 AI。
- Git 默认只发布外部来源的 metadata/checksum，不发布第三方原件。创建公开仓库、push、Release 或分发第三方文件都需最终审计后再次获得用户明确批准。

## Implementation and experiment skeleton

- 本轮实现前代码边界见 `src/README.md`；不要在 benchmark 前把候选算法写成既定架构或创建假想 Adapter。
- 实验规范、状态和 run manifest 见 `experiments/README.md`；大体积输出写 `artifacts/runs/`，审查后的结论才进入 `reports/`。
- 代码变更增加对应测试；不得靠注释报错、跳过 gate 或修改指标定义来制造通过。

## Completion contract

- 文档/来源/知识变更：运行 `scripts/verify`。
- 来源变更：另运行 `scripts/sources inbox`、`scripts/sources doctor` 和 catalog/checksum 检查。
- 代码变更：运行相关测试与 lint；实验变更验证 manifest、split、metric 与 source lock。
- 失败、未运行或缺证据的项目保持 `pending/open`，不得报告完成。
- `AGENTS.md` 是唯一规则正文；根级 `CLAUDE.md` 必须保持为指向它的相对软链，禁止复制成第二份规则。
