# 遗留文献报告溯源（Legacy Literature Report Provenance）

Status: `CURRENT`
Purpose: replace inaccessible historical desktop paths with stable recovery locators

## 可恢复的内容

用于生成 C、D、E 深读报告的完整任务说明保存在冻结的 Chat 2 transcript 中：

| 报告 | Raw 恢复定位符 | 来源内容 |
| --- | --- | --- |
| C 组 | `CHAT-2 / Turn 10 / lines 2025–4181` | 锁定的 C1–C8 映射、继承的假设、要求的分析模板、证据矩阵、迁移限制与输出要求 |
| D 组 | `CHAT-2 / Turn 14 / lines 4214–6676` | 锁定的 D1–D7 映射、去噪/边界/分割/识别（denoising/boundary/segmentation/recognition）的分离、方法比较、评估要求与推断禁令 |
| E 组 | `CHAT-2 / Turn 18 / lines 6890–10379` | 锁定的 E1–E8 映射、诊断效用与构念效度（construct validity）两条路线、响应过程验证要求与推断禁令 |

紧接 E 组任务简报之前的换论文决定位于 `CHAT-2 / Turn 17 / lines 6714–6880`。

这些定位符指向 `webchat_raw_materials/chatgpt_chathistory/chat2.md`，其身份已冻结在 `RAW_SOURCE_MANIFEST.sha256` 中。raw transcript 仍是争议裁决来源，不是日常研究依赖。

## 无法作为独立文件恢复的内容

D 和 E 报告提到一个名为 `反馈.md` 的历史桌面文件。恢复出的工作区或三份导出的 transcript 中都不存在该文件的独立副本。因此该原件必须按 `UNAVAILABLE` 处理，不得静默重构。其机器本地绝对路径有意不保留在公开项目记录中。

存留的证据是嵌在各最终报告顶部附近的详细修订记录。这些记录标明了每一项已应用的更正及其目标章节。它们证明最终报告声称改动的内容，但并不是审阅者原始措辞的独立副本。

## Canonical 解读

- 最终报告文件是持久的文献资产，须经本地 PDF 复核。
- raw Chat 2 任务说明确立的是生成意图与范围，不是科学事实。
- 内嵌的修订记录确立最终报告自身的变更历史。
- 缺失的历史反馈文件是溯源（provenance）限制；它并不使能够对照本地 PDF 独立核验的主张（claim）失效。
- 任何未来报告都不得把外部个人桌面路径当作当前依赖来引用。
