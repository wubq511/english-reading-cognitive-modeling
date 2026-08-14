# Experiment workspace

`experiments/` 保存实验设计、预注册式约束和可复现运行清单，不保存论文原文、正式结论或大体积运行输出。

## 生命周期

1. 在 `specs/` 创建稳定 `EXP-*` 设计；明确研究问题、数据角色、estimand、baseline、候选方法、split、metric、失败条件和伦理/AI gate。
2. 设计通过审查后冻结输入来源、配置和指标版本；未冻结不得写成 confirmatory result。
3. 每次运行产生独立 `run_id`，机器输出写入 `artifacts/runs/<experiment_id>/<run_id>/`。
4. 结果必须保留 run manifest；不可复现、输入漂移或 gate 失败的运行标记为 `INVALID`，不得挑选性进入报告。
5. 只有经过审查的综合结论进入 `reports/`，并回链 experiment ID 与 run ID。

## 最小复现契约

每次运行至少冻结：

- Git commit 和 dirty-state；
- `sources/catalog.yaml` 与 `sources/checksums.sha256` 的 hash；
- dataset ID/version/hash、数据角色与允许用途；
- experiment spec、配置、split、seed、环境和依赖锁；
- metric 名称、版本、方向和聚合规则；
- 输出文件 hash、开始/结束时间、状态和失败原因；
- AI-assisted 工件按 `AI_RESEARCH_TOOLING_POLICY.md` 增补完整 provenance；
- 真人数据按 `HUMAN_RESEARCH_GATES.md` 记录批准与数据分类，但不把敏感材料写入 manifest 或 Git。

模板位于 `templates/`。它们是结构起点，不代表当前已有实验或结果。
