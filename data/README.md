# Project data boundary

`data/` 只存本项目生成、采集或派生的数据。第三方数据集属于 `sources/library/datasets/`。

| 路径 | 角色 | Git 默认 |
| --- | --- | --- |
| `synthetic/` | `DATA-D1/D2` 工程合成与半合成数据 | 生成文件默认忽略；小型、许可清楚的冻结 fixture 可单独审查 |
| `derived/` | 从允许输入可重建的特征、split 和中间表 | 生成文件默认忽略；必须记录输入与代码版本 |
| `human/` | `DATA-D3..D5` 真人研究数据 | 永不进入公共 Git |
| `private/`、`identifiers/` | 受限材料与身份映射 | 永不进入公共 Git，且与分析数据物理隔离 |

数据不得成为无来源的“最终 CSV”。每个可用于实验的数据集必须有稳定 dataset ID、schema、生成/采集协议、许可或伦理依据、版本、hash、split 规则和适用声明。Synthetic truth 永远不能改写为 human truth。
