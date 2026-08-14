# Repository skill set

`.agents/skills/` is the only tracked physical source for project skills. Codex discovers it directly; after bootstrap, Claude Code consumes generated, Git-ignored mappings under `.claude/skills/`.

The five public workflow entry points are user-invoked only:

- `research-workflow`
- `wayfinder`
- `to-spec`
- `to-tickets`
- `implement`

Their supporting skills retain model invocation so an explicitly started stage can use them when needed. Workflow and tracker semantics are owned by `docs/agents/`; skill files contain stage procedures, not a second project policy.

Several supporting skills and the original stage designs are adapted from Matt Pocock's skills under the MIT License. See `LICENSES/MATT-POCOCK-SKILLS-MIT.txt`.
