# External Research Sources

`sources/` 是项目外部证据与输入资产的唯一入口。它同时容纳论文、标准、题目材料和第三方数据集，因此不再使用会误导为“只有论文”的 `papers/` 名称。

项目自身产出的结论进入 `reports/`；实验生成或采集的数据进入 `data/`；外部来源的本地原件与机器索引进入本目录。

## 目录职责

| 路径 | 内容 |
| --- | --- |
| `catalog.yaml` | 稳定来源 ID、类型、版本、获取方式、权利、目标路径与 SHA-256 的唯一机器索引 |
| `checksums.sha256` | `catalog.yaml` 所列本地原件的公开完整性契约 |
| `library/papers/literature/` | A–E 与 UI 交互文献集合 |
| `library/papers/domain/` | 英语阅读、题目、认知诊断等领域论文 |
| `library/papers/methods/` | 模拟、标注、可靠性与研究方法论文 |
| `library/standards/` | 标准、规范和治理文件 |
| `library/study-materials/items/` | passage、item、answer-key 或附件等研究材料；这里的材料不因来自论文附件就自动具有再使用权 |
| `library/datasets/` | 外部数据集及其原始分发包；项目生成的数据不放这里 |

所有报告与旧编号的路径解析集中在 [`../reports/provenance/SOURCE_REPORT_CROSSWALK.md`](../reports/provenance/SOURCE_REPORT_CROSSWALK.md)。不要在其他文档复制完整来源清单。

## 强制预检

克隆仓库后只需执行一次：

```bash
scripts/bootstrap
```

它安装仓库内 Git hooks，并自动执行收件箱归档、合法直下同步和完整性检查。之后 `git checkout`、`git pull` 和 `git push` 会自动触发相应检查；需要直接诊断时运行：

```bash
scripts/sources inbox
scripts/sources sync
scripts/sources doctor
```

`doctor` 未通过时，不得开展依赖缺失全文或材料的研究。`catalog-check` 只验证公共 Git 中的元数据/校验和契约，不代表本地原件齐全。

## 人工下载收件箱

所有需要登录、订阅、图书馆或浏览器人工获取的论文 PDF，统一放入项目根目录：

```text
tmp/pdfs/
```

人不负责改名、猜目录或直接覆盖正式库。Agent 必须：

1. 核实作品、具体版本、DOI/正式来源、许可与获取渠道；
2. 新来源先加入 `catalog.yaml` 和 `checksums.sha256`；已有缺失来源则核对预期 SHA；
3. 运行 `scripts/sources inbox`；工具按 SHA-256 匹配并原子迁移；
4. 只有正式目标再次通过格式与 SHA 校验后，工具才删除 `tmp/pdfs/` 中对应副本；
5. 未知 hash、多个候选、格式异常或目标冲突必须保留在收件箱，并输出 `INBOX_REVIEW_REQUIRED`，不得猜测或删除。

低层 `scripts/sources import ID FILE` 只供 Agent 或维护者在已知稳定 ID 时使用；常规人工协作入口始终是 `tmp/pdfs/`。

## Catalog 规则

- `asset_type` 使用 `PAPER`、`STANDARD`、`STUDY_MATERIAL`、`DATASET` 或 `OTHER`。
- `media_type` 决定额外格式检查；所有文件都必须通过精确 SHA-256。
- `required: true` 表示该来源属于当前完整研究环境；缺失时本地 gate 失败。
- `acquisition_status` 只描述本地获取渠道，不能替代版权判断。
- `redistribution_status` 只描述这个具体文件版本能否再分发；`UNKNOWN` 或 `RESTRICTED` 不得进入公共 Git。
- 作者、DOI、许可或版本证据不足时保留 `null` / `UNKNOWN`，禁止补猜。
- 同一作品的新版本作为新文件登记并建立版本关系，不覆盖旧字节。

公共 Git 默认只跟踪 catalog、checksum、获取说明和权利记录，`sources/library/` 中的第三方原件均被忽略。即使某一文件具有开放许可，也必须经过逐文件发布审计和用户再次批准，不能整目录发布。
