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

A local hook and a CI gate are not alternatives. The gate is authoritative and
runs for everyone; the hook only moves the same refusal earlier, before a push.
When you change one, check whether the other now disagrees with it.
