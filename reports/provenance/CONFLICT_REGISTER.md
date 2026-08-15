# 冲突登记册（Conflict Register）

| ID | 冲突 | 证据 | 裁决 / 当前状态 |
| --- | --- | --- | --- |
| `C-001` | Migration package 声称其优先级高于更早的 handoff | package 内 `10_SOURCE_AND_FILE_INDEX.md` | **Resolved**：当前用户规则 + 完整 transcript 优先于 package |
| `C-002` | Package 将 Phase 0/1/2A/3/4 标记为已关闭 | chat3 只明确关闭 Phase 2A 设计；Phase 3/4 只是已开始/已宣布 | **Resolved**：以 `CURRENT_STATE.md` 中的 phase 审计为准 |
| `C-003` | Phase 0 被宣布为“基本收敛”，但承诺的四个资产并未全部交付 | chat3 Turn 4 与后续记录对比 | **Open**：Phase 0 仍然开放 |
| `C-004` | 2022→2026 的 CSE 工作先被描述为待验证的谱系，后来被描述为继承的构念/Q-matrix | handoff2/package 与 2026 J. Intell. 及官方记录对比 | **作为边界解决**：直接继承关系为 J. Intell. ← TSC 2026；2022→J. Intell. 的 same-test/same-matrix 为 `NOT FOUND`，更宽泛的家族关系仅为 `INFERENCE` |
| `C-005` | `L0/L1/L2` 既指采集层级，也指系统层 | chat1/handoff1 与 handoff2 对比 | **Resolved**：区分 `COL-L*` 与 `SYS-L*` |
| `C-006` | `D3` 在一个分类法中表示 Human Pilot，在别处表示 Cognitive Scenario Stress | handoff2/chat3 | **Resolved**：`DATA-D3` 保留给 Human Pilot；压力测试是无编号的 benchmark 场景 |
| `C-007` | E0–E10 与 E0–E6 两套实验编号并存 | handoff2/chat3 | **Resolved**：`BENCH-E0..E6` 为 canonical；更细粒度的历史 ID 只是别名 |
| `C-008` | A–E 报告引用了过时的 `gpt-add-*`/PDF basename | 报告与文件系统对比 | **对当前导航已解决**：通过 canonical 名称与 crosswalk；历史别名仍保留索引 |
| `C-009` | C/D/E 报告依赖项目中不存在的桌面 prompt/反馈文件 | 报告头部与 raw Chat 2 对比 | **Partially resolved**：完整任务 prompt 已通过 `LEGACY_REPORT_PROVENANCE.md` 中的 raw 定位符恢复；不可得的 D/E 反馈原件保持披露状态，未做虚构 |
| `C-010` | Package 的时区写的是 Asia/Tokyo | 当前环境为 Asia/Shanghai | **Resolved**：当前项目采用 Asia/Shanghai；package 中该字段视为错误 |
| `C-011` | “No AI” 可能被解读为禁止所有实验使用 AI | 用户澄清 | **Resolved**：只有 runtime baseline 被排除；政策已记录 |
| `C-012` | 曾提议用一般熟人/学生做早期验证 | 用户偏好与伦理规则冲突 | **Resolved**：H1 仅用于调试；留存/分析的数据需先经 H2 审查 |
| `C-013` | 公开协作需要来源原件，但公开再分发可能缺乏权利 | 协作需求与版权/平台限制冲突 | **在设计层面解决**：类型化 manifest/本地库/法律同步/`tmp/pdfs` 收件箱/自动 hooks/权利已清除的文件发布 |
| `C-014` | `UIB-088` 看起来可能是 `UIB-018` 的笔误 | 仅有当前报告/文件 | **Open**：在外部编号来源明确前保留稳定 ID |
| `C-015` | D5/UIB-005 与 D6/UIB-007 看起来重复 | 标题/DOI 相同，SHA/页码/制作方不同 | **Resolved**：作为同作品的不同版本保留；首选版本仍然开放 |
| `C-016` | Migration package 引入了 ADEMP/DOE/OC-Bench/T0–T18 与工具栈 | 实质性 raw 讨论中不存在 | **Resolved**：仅为 package 来源的提案；ADEMP 后来仅因仿真规划获得独立支持 |
| `C-017` | 历史目录名包含 `interation` 笔误与 migration 来源的 `chatgpt_A-E` | 旧本地路径 | **2026-08-14 已解决**：报告已移至 `reports/literature/*`；源文件在 crosswalk/catalog 中保留旧别名 |
| `C-018` | `papers/` 混放了论文、标准、题目补充材料与未来数据集 | 实际资产类型与目录语义不符 | **2026-08-14 已解决**：外部输入已移至类型化的 `sources/library/` 下；项目生成的数据、run 产物与报告各自有独立生命周期 |

## 关闭规则

`OPEN` 项只有在获得当前用户决定、一手 artifact、论文/官方来源或可复现的本地结果时才能关闭。之后只是复述某一方的摘要不能使其关闭。
