# Source Authority Policy

## Two independent authority axes

项目状态/决策与科学事实使用不同的权威顺序，不能混成一条“新文件永远赢”的规则。

### A. Project state and intent

1. 当前用户在本地项目中的明确决定；
2. 三份完整聊天 transcript 中较新的明确修正；
3. 两份 handoff，经 transcript 核对后使用；
4. 现有报告对自己生成过程和论文阅读范围的记录；
5. ChatGPT migration package，仅作为查漏和候选建议。

Handoff 是会话边界时由 ChatGPT 生成的派生文档，不是逐字 transcript；用户将它列为主要恢复来源，但出现冲突时完整 transcript 更高。

### B. Scientific claims

1. 论文原文、正式标准、官方数据/规范与本项目可复现实验；
2. 已核对原文页码和研究设计的深读报告；
3. 多来源综合后明确标注的 `PROJECT-INFERENCE`；
4. 聊天或 handoff 中的研究判断；
5. migration package 中无独立来源的新增判断。

历史聊天可以证明“当时讨论或决定过什么”，不能单独证明外部科学事实为真。

## Temporal correction rule

更晚不自动等于更真。后续内容只有在明确修正同一问题、给出更强证据或记录用户新决定时才覆盖旧内容。若后续只是压缩、迁移或宣告完成，不覆盖旧文档的未完成证据。

## Claim states

- `VERIFIED-CURRENT`: 由当前文件、代码、实验或外部一手来源证明。
- `SOURCE-RECOVERED`: 历史主来源明确记录，但尚未在本地重做。
- `PROJECT-INFERENCE`: 项目综合推论，列出输入证据和反例。
- `PACKAGE-ORIGIN PROPOSAL`: 仅在迁移包出现，不能冒充历史已完成结论。
- `OPEN`: 证据不足或资产不可得。
- `CONTRADICTED`: 当前证据直接否定。

## Raw materials policy

- `webchat_raw_materials/` 冻结保留，不移动、不清理、不作为日常研究资产。
- 以 `RAW_SOURCE_MANIFEST.sha256` 检测意外变化。
- Canonical claim 使用 source ID/turn/line locator；发生争议时由授权维护者回查本地 raw。
- 公开 Git 从初始历史就排除 raw materials；以后删除文件不能清除既有 Git 历史，因此不得先提交再删除。
- 计划建立加密异地备份，但备份位置和密钥治理尚未决定。

## Canonical ownership map

同一个事实只能有一个 canonical owner；其他文档可以给受众所需的一句话摘要，但必须链接 owner，不能复制会独立腐坏的完整状态或规则。

| Topic | Canonical owner | Other surfaces may contain |
| --- | --- | --- |
| 当前阶段、完成度、下一工作 | `reports/project_state/CURRENT_STATE.md` | 指针，不重复 phase 状态表 |
| 研究问题 | `reports/project_state/RESEARCH_QUESTIONS.md` | RQ ID 与指针 |
| 阶段依赖与 exit gate | `reports/project_state/ROADMAP.md` | 阶段 ID 与指针，不维护 current status |
| Baseline 架构 | `reports/synthesis/SYSTEM_DESIGN.md` | Module/section ID 与指针 |
| AI 与真人治理 | 对应 `reports/protocols/` | 一句话不可突破边界与指针 |
| 外部来源身份、路径、版本、权利与 hash | `sources/catalog.yaml` + `sources/checksums.sha256` | 稳定 source ID、页码和指针 |
| 来源编号/历史路径到当前路径 | `SOURCE_REPORT_CROSSWALK.md` | 旧 alias，不复制书目真值 |
| 实验设计与 run 复现规则 | `experiments/README.md` + 对应 `EXP-*` spec | experiment/run ID 与结果摘要 |
| 项目术语 | `CONTEXT.md` | 术语引用，不另建竞争定义 |

README 和 Agent 规则只负责导航与不可突破的项目 invariant，不承担动态研究状态。

## Change and supersession protocol

观点、决策、路径、ID、阶段或外部证据变化时，按以下顺序执行：

1. 找到上表 owner；不存在 owner 时先指定一个，不创建多份“临时权威”。
2. 以新证据更新 owner，明确日期、claim state、适用范围、反例和被取代内容。
3. 用 `rg` 全仓搜索旧表述、旧 ID/路径和复制段落；仍需出现的位置改为稳定 ID + owner 指针。
4. 重要架构/治理变更写 ADR；历史矛盾或证据升级更新 conflict register/claim ledger。旧证据不删除，但旧结论必须标明 superseded/contradicted 或离开当前入口。
5. 同步 catalog、checksum、crosswalk、README/Agent 路由和实验锁文件等受影响表面。
6. 运行 `scripts/verify`；未通过不得把变更写成已完成。

“保留历史”不等于让历史判断继续与当前判断并列。追溯证据保留在 provenance/raw 层，日常入口只呈现一个当前答案。

## External source evidence rule

需要全文支持的判断必须绑定 `sources/catalog.yaml` 的稳定 ID，并尽量给 page/section/table/figure。只有摘要时明确标 `ABSTRACT-ONLY`；无法取得全文时，要求用户把合法取得的 PDF 放入 `tmp/pdfs/`，再由 Agent 核验并执行 `scripts/sources inbox`，不能用常识补写原文内容。
