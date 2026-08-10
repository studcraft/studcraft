---
paths:
  - "scripts/*.py"
  - ".github/workflows/*.yml"
  - ".claude/**/*.md"
  - ".claude/*.json"
---

# Scripts, CI gates, hooks and agent definitions

- `system/ci-gates.md` — required-check design pitfalls: a required check must
  trigger on every pull request unconditionally, a branch-name exemption must
  additionally be constrained by content, and shared state needs a concurrency
  guard. Read it before adding or editing a workflow.
- `system/delegating-to-agents.md` — what belongs in a `.claude/agents/`
  definition, and what the reviewer still has to do afterwards.
- `system/documentation-standards.md` — the Repository Structure tree records
  what each script owns; update it when you add one, and note that
  `scripts/generate_site_docs.py` carries a `TITLES` dict that must list every
  `docs/*.md`.

`.claude/settings.json` also carries the `permissions` block. Its `deny` list is
the git commands `system/repository-strategy.md` forbids and
`.claude/agents/git-operator.md` lists verbatim — it adds no policy of its own,
and anything added to it that those two documents do not already forbid is a
policy change wearing a configuration disguise. `.claude/settings.local.json` is
per-machine and gitignored; nothing another checkout must have belongs there.

A local hook and a CI gate are not alternatives. The gate is authoritative and
runs for everyone; the hook only moves the same refusal earlier, before a push.
When you change one, check whether the other now disagrees with it.

`scripts/preflight.py` is the same bargain in script form: it mirrors four of
the workflows plus both checker scripts so a push is not the first thing to
report a red gate. **Editing a workflow means checking the mirror against it.**

`.claude/hooks/lint_after_edit.py` watches `Bash` as well as `Write` and `Edit`,
because a shell command that writes carries no `file_path` for a hook to read.
It decides by modification time rather than by reading the command — deciding
intent from a shell string is a losing game, and the attempt matched a commit
message quoting a path. Anything that adds a generated file under `.studcraft/`
should keep that split in mind: the directory is a cache, gitignored, and never
a source of truth.
