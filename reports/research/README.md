# 研究审计

`reports/research/` 保存范围明确、以一手来源为主的研究审计，用来更新或约束项目的规范性综合结论。这里保存的是可长期维护的研究资产，不是原始检索笔记。

- [Phase 0 题目与数据来源审计](phase-0-item-data-source-audit.md)：梳理 CSE/PELDiaG/TSC/J. Intell. 的谱系、题目资产、外部过程数据集、权利情况和精确获取队列。
- [方法与治理来源审计](methods-and-governance-source-audit.md)：审计 AI 与真人研究协议使用的全部 25 份外部来源，包括按具体版本核对的 PDF 权利门禁。
- [既有文献验证审计](existing-literature-validation-audit.md)：基于本地 PDF 重新核对 7 条高影响 A/A+/B/C/D/E/UIB 声明及其迁移边界。
- [UI 仪器效应证据审计](ui-instrument-effects-evidence-audit.md)：审查答题 UI 的布局、导航、反馈、可访问性和交互功能是否影响行为、缺失、仪器可靠性或估计目标（Wayfinder #5）。
- [回放保真度指标与工程 Oracle](replay-fidelity-metrics-and-engineering-oracles.md)：议题 #7 的一手来源方案审查，包含 `replay-fidelity-oracles/v1` 指标登记表、分层 `BENCH-E0` Oracle，以及三个 `simulation-only` 反例。

只能由成员完成的工作（环境配置、受限数据库检索、付费来源获取）统一登记在 [human-tasks/](human-tasks/README.md)：每个议题使用一个中文文件，并共用跨议题的 `setup.md`。`ercm-research` 会在人工事项出现时立即登记，并在聊天中指出具体文件和章节。

研究审计可以收窄先前声明，但不能静默取代 `reports/project_state/` 或 `reports/synthesis/`。如果审计改变了当前项目状态，必须在同一变更中更新对应的规范性状态/综合文件，以及冲突或声明登记表。
