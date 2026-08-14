# Member Activity Logs

`logs/` 是合作成员的可审计活动层。Git 已经精确记录“哪些字节被谁修改”；这里只补 Git 不知道的语义：本次做了什么工作、形成或改变了什么研究/工程判断、如何验证、遗留什么。

它不是每日心得、Git diff 复制、会议逐字稿或 Agent 思维过程。只记录可共享的工作事实、证据、决定、验证和待办；不得放入密钥、第三方受限原文、真人原始/假名化数据或未经同意的个人信息。

## Directory and identity

```text
logs/
  policy.json
  members/
    <member-id>/
      YYYY-MM/
        YYYYMMDDTHHMMSSZ-<summary-slug>.md
```

`member-id` 是稳定的小写 slug，只使用 `a-z`、`0-9` 和内部连字符。每个 clone 只需绑定一次当前负责成员；设置写入本地 `.git/config`，不写入共享仓库：

```bash
scripts/logs init <member-id>
scripts/logs status
```

正常编写的 commit 只归属一个负责成员目录。若有协作者，在日志正文说明，不为同一工作制造多个互相竞争的所有者。远端 squash 产生的聚合 commit 可保留多名成员原有的独立条目；这是保留原始贡献，不是重新指定一个共同所有者。

## Required workflow

过了 [`policy.json`](policy.json) 的 `enforcement_after` 边界后，每个包含日志目录之外改动的 commit 必须同时新增至少一条当前成员日志。开始新记录的稳定命令是：

```bash
scripts/logs new \
  --category <category> \
  --summary "<one-line outcome>" \
  --work "<completed work>" \
  --impact "<research or decision impact, including no change>" \
  --verification "<command/evidence and PASS, FAIL, or NOT_RUN reason>" \
  --follow-up "<remaining action or None>"
```

Agent 在用户委托下修改项目时，由 Agent 创建、填写、校验并 stage 日志；不要把排版和命令记忆负担转给用户。日志与实际改动一起 `git add`，然后正常 commit。`pre-commit` 会在缺失、归属错误、格式不完整或修改历史日志时 fail closed。

Category 仅能从 `policy.json` 选择。一项工作同时涉及多类时，选择其主要产出；其他影响写入正文，不复制多份日志。

## Entry contract

每条日志是一个独立 Markdown 文件，固定 front matter 与四个 section 由 `scripts/logs` 生成并校验：

- `Work completed`：完成的操作与产出，不复制文件 diff。
- `Research or decision impact`：新结论、被修正结论、新边界或“未改变科学结论”。
- `Verification`：已运行命令/审计与结果；未运行时必须写 `NOT_RUN` 和原因。
- `Follow-ups`：未完成项、外部依赖或 `None`。

日志在进入 commit 后 append-only。若旧记录有错，新增一条更正日志，用 `--supersedes logs/members/...` 指向旧记录；不原地编辑、删除或改名旧记录。这样保留“当时记录”与“后续更正”两个事实。

## Enforcement layers

| Layer | Enforcement | Boundary |
| --- | --- | --- |
| `AGENTS.md` / `CLAUDE.md` | Agent 在 commit 前主动维护日志 | 行为指令，不是强制执行器 |
| `.githooks/pre-commit` | 检查 staged diff、成员归属、schema 和 append-only | 需要先运行 `scripts/bootstrap`；本地可被 `--no-verify` 绕过 |
| `.githooks/pre-push` + `scripts/verify` | 扫描边界后全部非 merge commit | 同样是客户端门禁 |
| GitHub Actions `verify` | 用完整 Git 历史重做全部检查 | 只有设为 protected branch required check 后才能阻止远端合并 |

因此，当前本地机制会立即阻止遗漏；公开仓库建立后，还必须把 `verify` 设成 `main` 的 required check，才能对所有协作者形成远端硬门禁。这是 Git/GitHub 执行边界，不能用更强的文档措辞代替。

`enforcement_after` 之前的恢复历史不追溯伪造成员日志。边界后的普通 commit 逐个检查；merge commit 只聚合已检查的父历史，不要求重复日志。
