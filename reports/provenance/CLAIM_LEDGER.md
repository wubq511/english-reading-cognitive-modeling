# Canonical Claim 台账

来源 ID：

- `CHAT-1/2/3`：完整 transcript 与 turn 编号；
- `HO-1/2`：handoff 文件；
- `USER-LOCAL-2026-08-14`：本地恢复期间做出的决定；
- 外部来源 ID 通过 `sources/catalog.yaml` 解析。

行号指向冻结的本地恢复文件，并受 `RAW_SOURCE_MANIFEST.sha256` 保护。

| 主张（claim） | 状态 | 恢复定位符 | 科学证据要求 |
| --- | --- | --- | --- |
| 项目寻求最终正确性之外的过程/认知/技能证据 | `SOURCE-RECOVERED` | `CHAT-1/T1/L40+`; `HO-1/L9-L34` | 研究问题，而非外部事实 |
| 先构建不含 LLM/Agent 的 runtime baseline；之后再做纵向/横向 AI 扩展 | `SOURCE-RECOVERED + CURRENT-DECISION` | `CHAT-1/T16/L6768+`; `CHAT-2/T2/L60-L74`; `HO-2/L39-L72`; 用户本地澄清 | AI 政策约束实验 |
| AI 在研究、实验与合成辅助中被允许且重要 | `CURRENT-DECISION` | `USER-LOCAL-2026-08-14` | `AI_RESEARCH_TOOLING_POLICY.md` |
| 低干扰 UI：左侧文章、右侧单题、自由导航、underline/eliminate/change（下划线/消除/改答） | `SOURCE-RECOVERED` | `CHAT-1/T14/L4251+`; `HO-1/L81-L113`; `HO-2/L190-L226` | 可用性仍需测试 |
| raw 事件不得包含认知内容，且应为 append-only/以对象为中心（object-centric） | `SOURCE-RECOVERED + PROJECT-INFERENCE` | `CHAT-1/T12/L3181+`; `HO-1/L155-L218`; `HO-2/L259-L316` | 需要埋点 benchmark |
| Viewport/pointer/dwell/revisit 不能直接等同于注意/难度/困惑（attention/difficulty/confusion） | `SOURCE-RECOVERED + PAPER-SUPPORTED` | `CHAT-1/T8/L1753+`; `HO-2/L118-L188` | B/C 报告 Evidence Index |
| 最终架构是分层的部分观测证据系统 | `PROJECT-INFERENCE` | `HO-2/L318-L421` | A–E/UIB 的综合，而非单篇论文的主张 |
| 未知与相互竞争的假设是强制要求的 | `SOURCE-RECOVERED + MEASUREMENT-LOGIC` | `CHAT-2/T23/L10443+`; `CHAT-3/T7/L725-L1857`; `HO-2/L118-L188` | 验证弃权/校准（abstention/calibration） |
| Phase 2A 的与题目无关设计已关闭，Phase 2B 等待题目/试测 | `SOURCE-RECOVERED` | `CHAT-3/T7/L725-L1857` | 仅设计状态 |
| Phase 3 有草稿，没有完成的 benchmark | `VERIFIED-CURRENT` | `CHAT-3/T8/L1863-L2305`; `T9/L2306-L2318` | 本地仓库没有 runs/结果 |
| Phase 4 在 raw chat 中只是被宣布，未交付 | `VERIFIED-CURRENT` | `CHAT-3/T10/L2319-L2331` | package 新增内容不能升级状态 |
| 多个算法候选必须由本地实验裁决 | `SOURCE-RECOVERED` | `CHAT-2/T21/L10413-L10439`; `HO-2/L74-L116` | 同数据 benchmark |
| 合成数据不能确立真实行为→认知效度 | `SOURCE-RECOVERED + PAPER-SUPPORTED` | `HO-2/L902-L1011`; `CHAT-3/T8/L1869+` | AI 政策来源 + 人类锚点数据 |
| 摄像头与眼动追踪（eye tracking）是可选的子研究，不是 baseline 依赖 | `CURRENT-DECISION` | `USER-LOCAL-2026-08-14` | 使用前需过 M1 伦理门禁 |
| H1 随意测试仅用于调试；研究数据从 H2 开始 | `CURRENT-DECISION + OFFICIAL-RULE` | `USER-LOCAL-2026-08-14` | `HUMAN_RESEARCH_GATES.md` |
| raw 聊天仍是本地冻结证据，不是日常资产或公开 Git 内容 | `CURRENT-DECISION` | `USER-LOCAL-2026-08-14` | 来源政策 + 校验值 |
| PDF 使用 manifest/本地缓存与权利感知（rights-aware）同步，而不是一律放进公开 Git | `CURRENT-DECISION` | `USER-LOCAL-2026-08-14` | 逐篇权利审计仍然开放 |
| 公开下载端点与公开再分发许可是两个独立状态 | `OFFICIAL-RULE + CURRENT-DESIGN` | `USER-LOCAL-2026-08-14`; 版权/GitHub 审计 | catalog 中 `acquisition_status` 与 `redistribution_status` 保持分离 |
| 2026 J. Intell. 研究直接继承 TSC 2026 的属性/Q-matrix，而不是显式声明的 2022 数据谱系 | `PRIMARY-SOURCE-SUPPORTED` | `ITEM-001`; Phase 0 来源审计 | 2022→2026 的 same test/matrix 为 `NOT FOUND`；家族关系仅为 `INFERENCE` |
| J. Intell. S2 包含一个 20 题测试，但不是可部署的金标准题库 | `PRIMARY-SOURCE-SUPPORTED` | `ITEM-002`; Phase 0 来源审计 | 需要独立 answer key、证据范围与题目级权利 |
