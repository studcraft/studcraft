---
paths:
  - "docs/**/*.md"
---

# Editing `docs/`

`docs/` holds only the accepted ruleset. Four documents own the rules for
changing it — read the one that governs this edit before making it:

- `system/workflow.md` — OpenSpec Workflow and Git Workflow: a ruleset change
  is proposed first, on its own branch, named for the change it carries.
- `system/documentation-standards.md` — required document skeleton, rule-ID
  stability, image naming, and Versioning.
- `CODE_OF_DESIGN.md` — the fifteen principles every rule must reinforce.
- `system/proposal-review.md` — what to check before applying a change and
  after applying it.

Adding a new numbered document touches more files than the document itself.
`system/documentation-standards.md` ("Adding a New Ruleset Document") is the
checklist.

After editing, run both required checks:

```bash
python3 scripts/lint_ruleset.py
python3 scripts/check_delta_coverage.py
```

An edit that breaks the branch, proposal or version rules is refused by the
`PreToolUse` hook in `.claude/settings.json` rather than left to be caught in
CI after a push.
