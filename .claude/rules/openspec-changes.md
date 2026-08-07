---
paths:
  - "openspec/**/*.md"
  - "openspec/config.yaml"
---

# Working on an OpenSpec change

- `system/workflow.md` — OpenSpec Workflow, and Archiving: applying a change
  and archiving it are separate pull requests, and archiving is batched.
- `system/proposal-review.md` — reviewing a proposal before it is applied, the
  common failure classes, and delta vs. direct edit.
- `system/delegating-to-agents.md` — how to write a `tasks.md` that a less
  capable model applies perfectly.
- `openspec/config.yaml` — per-artifact rules. One proposal, one dedicated
  branch, always.

A change directory is complete only with all three of `proposal.md`,
`design.md` and `tasks.md`. The `Docs require OpenSpec proposal` gate rejects a
directory missing any of them.

`openspec/specs/` is shared state written only by the Archive cut. An edit to
it from a branch that is not `archive/*` is refused by the `PreToolUse` hook in
`.claude/settings.json`, the same way the `OpenSpec archive must be separate
from apply` gate rejects it in CI.

Before archiving, re-read every delta against the current `docs/` text. The
tools check structure, not truth — `system/workflow.md` ("Refresh every delta
against `docs/` before archiving") is the standing instruction.
