# 论文原文库

本目录保存项目研究中实际使用的论文 PDF。PDF 是论证来源，不是聊天材料的附件缓存；引用研究结论时，应通过 [`catalog.yaml`](catalog.yaml) 的稳定 ID 找到原文，并在报告中保留页码、章节、公式或表格定位。

## 当前范围

| 集合 | 路径 | 数量 | 用途 |
| --- | --- | ---: | --- |
| A/A+/B/C/D/E | `library/a-e/` | 44 | 过程测量、数字阅读、鼠标/注意、行为分割、认知诊断与构念效度 |
| UIB | `library/ui-interaction/` | 18 | UI 交互日志、任务识别、轨迹聚类、行为挖掘 |
| 题目/数据源 | `library/item-and-data-sources/` | 3 | Phase 0 题目谱系、Q-matrix 附件与难度 pilot 方法 |
| 方法 | `library/methods/` | 7 | simulation 设计、LLM 合成/标注风险与验证 |
| 标准/治理 | `library/standards/` | 2 | 测量标准与 NIST 生成式 AI 风险 profile |
| 合计 | `papers/` | 74 | 当前本地全文/附件全集 |

历史目录的 `interation` 拼写与 `chatgpt_A-E` 来源名已完成物理重构；旧路径和 basename 只作为 provenance aliases 保留。`UIB-088` 仍是稳定 ID；在来源关系核实前，不擅自改成 `UIB-018`。

## Pull 后预检

每次拉取或接收项目副本后，先在项目根目录运行：

```bash
scripts/papers doctor
```

它会 fail closed 地检查 catalog schema、稳定 ID 和路径唯一性、74 份 required 文件、SHA-256 与 PDF magic。缺失或损坏时会逐项打印 `id`、DOI、来源、目标路径和人工操作命令；未通过前，不应开始依赖这些论文的研究、评审或实验。

如果存在缺失论文：

```bash
scripts/papers sync
scripts/papers import ID /path/to/lawfully-obtained-paper.pdf
scripts/papers doctor
```

`sync` 只有在 catalog 同时提供 HTTPS `download_url`，且 `acquisition_status` 明确为 `DIRECT_PUBLIC` 时才会自动下载。它不携带登录凭据、不绕过认证；其余条目输出人工清单并以非零状态退出。`acquisition_status` 只回答“协作者能否从记录的官方公开端点获取本地副本”；`redistribution_status` 独立回答“项目能否再向公众分发这个具体版本”。免费可下载不等于可公开再分发。

## 权威索引

- [`catalog.yaml`](catalog.yaml)：论文级元数据、稳定 ID、旧文件别名、报告引用、解析状态和同一作品的本地版本关系。
- [`checksums.sha256`](checksums.sha256)：74 个 PDF/附件的 SHA-256，用于完整性校验。
- [`../reports/provenance/PAPER_REPORT_CROSSWALK.md`](../reports/provenance/PAPER_REPORT_CROSSWALK.md)：报告编号、旧 basename 与当前文件路径的映射。

文件名中的年份不一定等于正式出版年。例如部分文件使用预印本年、获取年或旧任务中的年份。规范引用以 `catalog.yaml` 的 `year`、论文首页和报告中的年份说明为准。

Catalog 的 acquisition 字段含义：

- `required`：该论文是否是当前仓库完整状态的一部分；当前 74 份均为 `true`。
- `acquisition_status`：本地获取通道；`DIRECT_PUBLIC` 可从记录的 HTTPS 端点自动获取，`MANUAL_ONLY` 需订阅/作者/人工操作，`UNKNOWN` 尚未核验。
- `source_url`：可供人工核验的来源页；未知时为 `null`。
- `download_url`：允许无认证直接下载的 PDF URL；未知时为 `null`。
- `redistribution_status`：本地已核验的再分发许可状态；未知时为 `UNKNOWN`，禁止据此公开再分发。它不控制本地 `sync`。

## 解析与完整性状态

本轮对全部 PDF 执行了 `pdfinfo` 和首页 `pdftotext` 检查：

- 74/74 可由 `pdfinfo` 解析；
- 74/74 可提取正文/首页文本；
- 0 份加密；
- 0 份 SHA-256 完全重复。

六个文件可正常读取，但 `pypdf` 容错解析报告了结构警告；具体警告记录在 `catalog.yaml`。这不等于论文内容损坏，但涉及自动化全文处理时应保留 QA 标记。

另有两组同一学术作品的不同本地 PDF 版本：

- `D5` 与 `UIB-005`；
- `D6` 与 `UIB-007`。

它们不是字节重复件，不能只凭标题相同删除。版本关系已在 `catalog.yaml` 中显式记录。

## 使用规则

1. 用稳定 ID 引用论文，不从目录顺序推断编号。
2. 新增论文时同时更新 `catalog.yaml`、`checksums.sha256` 和报告 crosswalk。
3. DOI、作者、venue、access 或 license 无可靠本地证据时保持 `null` / `UNKNOWN`，不要补猜。
4. `redistribution_status: UNKNOWN` 表示本仓库尚未记录再分发许可，不表示论文一定禁止研究使用。
5. 不要覆盖原 PDF。若获得正式版、作者稿或勘误版，作为新文件加入并用 `same_work` 建立关系。

## 独立校验命令

在项目根目录运行：

```bash
shasum -a 256 -c papers/checksums.sha256
```

通过标准是 74 项全部显示 `OK`。
