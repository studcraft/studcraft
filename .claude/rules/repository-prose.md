---
paths:
  - "system/**/*.md"
  - "AGENTS.md"
  - "CLAUDE.md"
  - "README.md"
  - "CONTRIBUTING.md"
  - "CODE_OF_DESIGN.md"
---

# Editing this repository's own prose

`system/` is context for AI agents, not human-facing documentation. Every line
competes with the line that actually decides something.

`system/documentation-standards.md` ("What `system/` Is For") owns that
standard and its consequences: one owner per rule, a pointer instead of a copy
always, and a file whose every line has another home is deleted rather than
kept for its organisational role. Read it before adding a paragraph.

So, before writing: search for whether another document already argues this.
If one does, point at it and write nothing else. A shortened restatement is
never merely redundant — `AGENTS.md` once reprinted eight of fifteen principles
and dropped the two that catch the most defects.

These files need a branch but not an OpenSpec proposal — `system/workflow.md`
(Git Workflow). `CHANGELOG.md` is not in this set: nobody edits it by hand.
