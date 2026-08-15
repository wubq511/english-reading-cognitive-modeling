# 公开仓库就绪度（Public Repository Readiness）

Status: `PUBLISHED; LIVE VERIFIED; PROTECTED`
Audit date: 2026-08-14
Target: `https://github.com/wubq511/english-reading-cognitive-modeling`

## 决定

本地研究恢复、来源边界迁移与自动化迁移通过了最终审计。项目所有者明确授权公开发布，仓库已在 `https://github.com/wubq511/english-reading-cognitive-modeling` 上线。

经审计的初始快照 `f3a826c7d4e53e4fdb9bad784a16ffe90646f079` 已推送到 `main`。GitHub Actions run `31786325757` 成功完成。受保护分支要求 pull request 和严格的 `verify` 状态检查，规则适用于管理员，并禁止 force-push 与删除分支。

获准的初始快照必须保持元数据优先：它包含 canonical 研究文档、溯源、来源元数据/校验值与恢复工具，但不包含 raw 聊天导出、第三方来源字节或人类参与者数据。

## 已审计的公开边界

| 检查项 | 结果 |
| --- | --- |
| 被跟踪的 raw 恢复材料 | `0`；`webchat_raw_materials/` 被忽略 |
| 发布收尾后被跟踪的文件 | `99` |
| 被跟踪的第三方来源文件 | `0`；在被忽略的本地库之下，只有 `sources/library/README.md` 被跟踪 |
| 被跟踪的真人/私有数据目录 | `0` |
| 常见凭据/token/私钥签名 | 暂存快照中无匹配 |
| 带凭据的 URL | 无匹配 |
| 个人邮箱地址 | 无匹配 |
| 机器本地绝对路径 | 无匹配 |
| 最大的被跟踪 blob | 277,815 字节；未接近 GitHub 大文件边界 |
| 引文元数据 | `CITATION.cff` 解析成功 |
| 工作流供应链固定 | checkout `v7.0.1` 与 setup-python `v7.0.0` 的 commit hash 已对照上游 tag 核验 |
| 成员活动日志 | append-only schema、暂存门禁与边界后历史门禁由仓库测试覆盖；CI 获取完整历史 |
| diff 卫生 | `git diff --cached --check` 通过 |

凭据扫描是有边界的签名扫描，不能证明任意散文都不可能编码敏感信息。更强的结构性保护是：raw、PDF、AI 载荷与真人数据目录树按路径排除，并在发布前核验。

## 来源与权利状态

- 80 个必需的 PDF/附件文件已在本地，并通过精确 SHA-256 与媒体签名检查。
- 11 条 catalog 记录当前有可 hash 复现的 `DIRECT_PUBLIC` 获取渠道；7 条为 `MANUAL_ONLY`；62 条仍是 `UNKNOWN`。`METHOD-003` 在一次全新克隆审计中，官方端点返回的字节与 catalog 锁定不一致，因此被降级。
- 八个特定版本被保守标记为 `REDISTRIBUTION_ALLOWED`，十个为 `RESTRICTED`，62 个为 `UNKNOWN`。
- 尽管有这些许可，**零个来源原件可以进入最初的 Git 历史**。任何后续发布都是独立的文件级审计与公开批准事件。
- 协作者运行一次 `scripts/bootstrap`。人工下载进入 `tmp/pdfs/`；Agent 更新元数据并使用 `scripts/sources inbox`，它只删除已核验的迁移副本。

法律与工程理由记录在 [`../../docs/project-management/SOURCE_DISTRIBUTION.md`](../../docs/project-management/SOURCE_DISTRIBUTION.md)。

## 研究主张边界

- 公开报告恢复并组织先前工作；它们不是同行评审或实证确认。
- 既有文献审计抽样检查主要主张并标记无支持的升级，但并不认证每份遗留报告的每一句话。
- 未来重大主张仍需要稳定来源 ID 加页码/章节证据，并在相关时提供独立实证验证。
- Phase 2A 仅设计关闭。Phase 0 仍然开放，Phase 3 是规范草稿，Phase 4 未完成，且尚不存在系统、benchmark 结果或人类研究。
- 按政策，AI/Agent 在研究平面与实验平面被允许；baseline runtime 本身仍然不含 LLM、生成式 AI 与 Agent。

## 验证证据

```text
39 unit tests (local complete corpus)              PASS
39 unit tests (public clone)                       PASS: local-byte checks skip when originals are absent
scripts/verify (local)                            PASS: 73 Markdown, 80 sources, 25 raw sources
scripts/verify --public                           PASS: 73 Markdown, 80 sources, 25 raw sources
scripts/bootstrap --check                         PASS: core.hooksPath=.githooks
scripts/logs validate                             PASS: 5 member entries; ignored workspace residue excluded
scripts/sources inbox                             PASS: inbox empty
scripts/sources sync                              PASS: no missing direct-public dependency
scripts/sources doctor                            PASS: 80/80 exact local dependencies
CITATION.cff parse                                PASS
publication-closeout Git index                    PASS: 99 files, 0 PDFs, 0 raw files, 0 tmp files
secret/path/credential URL/email signature scan   PASS: no matches
CLAUDE.md in initial snapshot                     PASS: mode 120000 -> AGENTS.md; historical, superseded locally by ADR 0007
git diff --check                                  PASS
initial GitHub Actions run 31786325757            PASS on published commit f3a826c
main branch protection                            PASS: PR + strict verify; admin enforced; no force-push/delete
```

Git 客户端不会克隆或自动启用仓库控制的 hooks。因此每个克隆需要显式执行一次 bootstrap；根级 `AGENTS.md` 要求 Codex 和 Claude（通过 `CLAUDE.md` 的 `@AGENTS.md` 导入）宣告并运行它，这样人类不需要记住命令。POSIX 上的 `scripts/bootstrap` 与 Windows 上的 `.\scripts\bootstrap.cmd` 配置 hooks、校验/修复仓库技能映射、恢复来源并检查日志身份。之后 checkout、merge、commit 与 push hooks 强制执行连续性。重复的工具专属 SessionStart hooks 保持延后，除非出现真实遗漏证据。当前本地分支提议 macOS/Windows 技能映射 CI，但该远端验收证据在得到明确批准的 push/PR 之前仍为待定。参见 [`../../docs/project-management/AGENT_BOOTSTRAP.md`](../../docs/project-management/AGENT_BOOTSTRAP.md)、[`../../docs/agents/SKILL_EVALUATION.md`](../../docs/agents/SKILL_EVALUATION.md) 与 [`../../logs/README.md`](../../logs/README.md)。

## 发布后的遗留动作

1. 在 [`../project_state/MANUAL_ACTIONS.md`](../project_state/MANUAL_ACTIONS.md) 中继续题目/数据权利、实验室与伦理队列。
2. 按 `AGENTS.md`，把每次后续 push、Release 或第三方文件分发都视为新的发布事件；初次批准不授予笼统的发布权限。
3. 切勿推断删除后来公开的产物能撤回已克隆的副本；在 push 之前阻止不安全的发布。

这些后续动作不扩大首次发布的范围。
