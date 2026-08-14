# Agent Bootstrap Governance

Status: `CURRENT`
Decision date: 2026-08-14
Supersedes: the earlier 2026-08-14 recommendation not to distribute repository skills

## Current design

Every clone has one idempotent initialization operation and one rule owner:

```text
AGENTS.md                         canonical project rules
CLAUDE.md -> @AGENTS.md          cross-platform Claude import shim
scripts/bootstrap(.cmd)          hooks + skills + sources + log identity preflight
.agents/skills/                  one physical project skill set
.claude/skills/<name>            symlink on POSIX; directory junction on Windows
.githooks/                       checkout/merge/commit/push continuity gates
```

Codex and Claude Code Agents are instructed to announce and run bootstrap before project work, so a collaborator does not need to remember the command. Bootstrap is also invoked after checkout/merge once Git hooks are configured.

Repository skills are now required because multiple research members need the same explicit Wayfinder → Spec → Tickets → Implement workflow without installing personal copies. They are not startup hooks and do not replace `AGENTS.md` or `scripts/bootstrap`.

All adapted project skills use the `ercm-` namespace. Bootstrap removes only obsolete generated mappings that point into `.agents/skills/`; it preserves unknown real files and directories.

## First entry

macOS/Linux:

```bash
scripts/bootstrap
```

Windows PowerShell or Command Prompt:

```bat
.\scripts\bootstrap.cmd
```

The operation:

1. verifies the directory is a Git worktree;
2. installs repository-local Git hooks;
3. validates `.agents/skills/` and creates/repairs Claude mappings;
4. processes the source inbox, performs allowed sync, and runs source doctor;
5. reports the local member-log identity requirement;
6. fails closed with the exact skill/source recovery action.

`--check` is read-only. `--hook` performs the idempotent continuity preflight without rewriting Git configuration.

## Cross-platform single source

Root project rules use a physical one-line `CLAUDE.md` containing `@AGENTS.md`. This is preferable to a tracked root symlink because Git for Windows may check a symlink out as a plain text payload when symlink support is disabled. Claude Code officially supports the import form; the repository verifier requires the file to contain nothing else.

Skill directories use bootstrap-generated, Git-ignored platform-native mappings to the same tracked `.agents/skills/<name>` target:

- POSIX: relative directory symlink `../../.agents/skills/<name>`;
- Windows: directory junction created by `.\scripts\skills.cmd install`.

Only `.claude/skills/.gitignore` is tracked below the Claude mapping root. This avoids Git for Windows checking POSIX symlinks out as text files and keeps bootstrap-generated junctions out of commits. Bootstrap refuses to replace an unknown real file/directory; it only repairs known symlinks, legacy Git symlink-placeholder files, or junctions, preventing accidental data loss.

## Invocation boundary

The five public workflow skills are explicit-only on both platforms:

- Claude Code: `disable-model-invocation: true`;
- Codex: `policy.allow_implicit_invocation: false`.

Supporting skills remain available on demand inside an explicitly invoked stage. These fields prevent implicit execution; they should not be described as a guarantee of zero skill-discovery metadata.

## Why no SessionStart hooks now

Root instructions plus idempotent bootstrap remain the current startup mechanism. Project-level Codex and Claude `SessionStart` hooks could run before model choice, but add vendor-specific trust prompts, repeat execution and a second lifecycle surface. No observed bootstrap omission currently justifies them.

If a supported Agent demonstrably begins project work without preflight, use one shared session adapter from both `.codex/hooks.json` and `.claude/settings.json`. Do not put startup logic in skills and do not create `.claude/hooks.json`, which Claude Code does not discover.

## Enforcement and limits

- A newly cloned repository still requires the Agent platform to load root rules; instructions are behavioral, not hostile-client enforcement.
- Windows requires Python and Git; `.\scripts\bootstrap.cmd` avoids requiring a POSIX shell for initialization.
- Local Git hooks can be bypassed, so protected-branch CI remains the remote enforcement layer.
- Public source files, human data and publication boundaries remain governed by `AGENTS.md`; bootstrap does not weaken those gates.

## Acceptance contract

Repository changes to this mechanism are complete only when:

1. `scripts/skills doctor` passes on macOS/Linux;
2. the Windows CI job generates ignored junction mappings and passes doctor with a clean checkout;
3. all five explicit entry skills carry both platform invocation controls;
4. every Claude mapping resolves to the corresponding physical Codex skill;
5. bootstrap is idempotent and `--check` is non-mutating;
6. `scripts/verify` checks rule import, skill sources/mappings, wrappers and knowledge links;
7. failure names a concrete recovery command instead of silently skipping a skill/source gate.

Official mechanism references: [OpenAI repository skills](https://learn.chatgpt.com/docs/build-skills), [OpenAI `AGENTS.md`](https://learn.chatgpt.com/docs/agent-configuration/agents-md), [Claude Code skills](https://code.claude.com/docs/en/slash-commands), and [Claude Code memory/imports](https://code.claude.com/docs/en/memory).
