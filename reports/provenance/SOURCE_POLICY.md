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

## Paper evidence rule

需要全文支持的判断必须绑定 `papers/catalog.yaml` 的稳定 ID，并尽量给 PDF page/section/table/figure。只有摘要时明确标 `ABSTRACT-ONLY`；无法取得全文时及时生成用户人工下载请求，不能用常识补写论文内容。
