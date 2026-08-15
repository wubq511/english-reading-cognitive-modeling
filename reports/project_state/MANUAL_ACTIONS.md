# 人工行动队列

状态：`ACTIVE`
默认负责人：项目负责人 + 实验室/机构联系人
规则：这些行动需要凭据、机构权限、作者联系或人工判断；Agent 不得模拟完成。

## 现在：改进 Phase 0 的来源获取

目前没有待处理的全文获取行动。Phase 0 剩余的人工工作涉及作者提供的题目/数据资产及其允许用途，而不是再找一篇论文 PDF。

## 2026-08-14 完成的来源获取

TSC 2026、PELDiaG 2021、Ma & Du 2022、GRRAS 2011 和 Shin 2025 已由用户提供并分别登记为 `DOMAIN-002`、`DOMAIN-003`、`DOMAIN-004`、`METHOD-009`、`METHOD-008`；另新增 Zhang et al. 2024 `DOMAIN-001`。规范路径、SHA、版本和权利只以 `sources/catalog.yaml` 为准；五文件批次的证据见 [`../research/new-user-provided-pdfs-source-audit.md`](../research/new-user-provided-pdfs-source-audit.md)，2022 的当前结论见 [`../research/phase-0-item-data-source-audit.md`](../research/phase-0-item-data-source-audit.md)。这些完成项不再留在行动队列中。

arXiv 预印本 `2306.00176` 有意**不**作为缺失需求：catalog 保留正式的 ICWSM 后继版本（`METHOD-007`）以避免重复版本。仅在出现版本比较问题时才补充该预印本。

## Candidate Bank V1 之前

1. 请 Wenbo Du / Xiaomei Ma 提供一张紧凑谱系表，覆盖 2022 CSE 论文、TSC 2026 与 J. Intell. 2026：

   - `instrument_version_id` 和题目映射（item mapping）；
   - 采集批次、原始 N、排除规则与最终 N；
   - 是否复用了任何参与者-响应矩阵；
   - 各版本的 Q 矩阵/构念变化；
   - 答案键权威性与题目/文章 provenance；
   - 数据字典、去标识化与允许的研究/共享用途。

2. 若向通讯作者索取 J. Intell. 实证数据，先取得实验室的数据治理批准。未经批准的传输与存储途径，不得通过个人邮箱/云盘发送或接收个人级数据。
3. 对于 `ITEM-002` S2，至少请两名合格的英语阅读/内容专家独立作答每题并标注证据区间；解决分歧时不得展示 S3 模型输出。记录逐题来源/权利状态。S3 的 Doubao 答案永远不是标准答案键。
4. 若现有材料无法完成权利清理，则构建原创的文章/题目包。从创建时起记录作者身份、来源灵感、作答依据、证据区间、候选技能映射、允许用途与版本。

Phase 0 保持开放，直到至少一个包满足全部条件：可用权利、文章/题目/选项、独立答案键、证据区间、候选标签、可观测性梯度与版本化的 pilot 选题规则。

## 邀请任何团队外人员之前

用户目前没有已确认的正式招募/伦理渠道。将其作为明确的依赖项，而不是想当然的未来能力。

书面询问负责的实验室/学校：

1. 哪个委员会审查这项非医学的教育/HCI/认知研究，谁必须担任 PI/负责研究者？
2. 机构能否为仅排 bug 的 smoke test 出具书面的 H1 非研究/调试认定？
3. H2 可行性 pilot 与 H3 正式研究适用哪条审查路径，已批准的 pilot 能否进入正式分析？
4. 招募熟人、同学或学生的规则是什么，尤其是从属/成绩关系与未成年人？
5. event logs、屏幕/音频录制、刺激回忆（stimulated recall）、Webcam 与眼动追踪（eye tracking）适用哪些同意、存储、保留、共享与修订规则？
6. 机构批准了哪些存储与数据传输渠道用于协作者和 AI/LLM 处理？

在获得书面答复之前：

- H0 合成数据/团队工程可以继续；
- H1 团队外人员 smoke test 在 `HUMAN_RESEARCH_GATES.md` 的狭窄规则下，只能产生 `NONRESEARCH_DEBUG_ONLY` 缺陷 ticket；
- H2/H3 的系统化日志、绩效、访谈、认知标签或可发布数据不得开始；
- Webcam/眼动追踪仍是可选的 M1 修订项，而不是 baseline 依赖。

## 2026-08-14 完成的公共 GitHub 发布

所有者已授权发布并刷新 GitHub 认证，Agent 已在 `https://github.com/wubq511/english-reading-cognitive-modeling` 完成经审计的发布。初始 `main` 快照通过 GitHub Actions run `31786325757`；分支保护现在要求 pull request 和严格的 `verify` 检查，适用于仓库管理员，并禁止 force-push 与分支删除。

初始发布不再有遗留行动。未来的 GitHub push、Release 或第三方文件分发属于新的发布事件，仍须通过 `AGENTS.md` 与 `SOURCE_DISTRIBUTION.md` 中的项目批准与文件级权利门禁。

## 完成记录

对于每项已完成的人工行动，更新相关审计/catalog 并添加：

```yaml
action_id: stable-id
completed_at: YYYY-MM-DD
actor_role: project-lead | lab | library | author | ethics-office
evidence_path_or_url: string
artifact_sha256: string-or-null
result: completed | denied | unavailable | superseded
constraints: []
```

不得仅凭邮件承诺或搜索摘要就把行动标记为完成；完成需要实际文件、机构认定、数据使用协议或其他可查验的证据。
