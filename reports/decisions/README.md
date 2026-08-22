# 决策记录（Wayfinder decision records）

`reports/decisions/` 是 Wayfinder 决策票**决议答案的唯一 canonical owner**。每份记录对应一张已关闭的 decision child ticket。

## 规则

- 命名：`wayfinder-<issue号>-<slug>.md`，一票一文件。
- 内容遵循决议合同：答案、证据与资产、被否替代、不确定性与门禁、下游含义；开头有中文「结论速览」段（核心结论、怎么得出的、未决项）。
- GitHub Issue 仍是协作表面：讨论、分配、状态与 dependency 在 Issue 上；关票时 resolution 评论只放摘要加本记录链接。地图（`wayfinder:map`）的 `Decisions so far` 只放一行 titled link gist。
- 记录合并进 main 后 append-only：新证据推翻旧决议时按 wayfinder 规则开新票或重开旧票，新记录写明 supersession，不原地改写旧记录。
- 一次性决策辅助物（原型代码、截图、手工材料）不进入本目录；它们在 throwaway 分支上作为决策谱系保存，由记录给出链接。

由来：[ADR 0008](../../docs/adr/0008-wayfinder-decision-records-in-repo.md)。
