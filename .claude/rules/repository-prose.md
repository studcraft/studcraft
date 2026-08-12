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

Two sections of `system/documentation-standards.md` own this. Read them before
adding a paragraph:

- **"What `system/` Is For"** — one owner per rule, a pointer instead of a copy
  always. Before writing, search for a document that already states this; if
  one does, point at it and write nothing else.
- **"How a Rule Is Written"** — one imperative sentence, reason in one clause.
  No postmortem, no "this used to say X", no section for a case that does not
  exist yet, no snapshot a command can print.

Shorter is the goal, and a deletion is a valid edit on its own.

These files need a branch but not an OpenSpec proposal — `system/workflow.md`
(Git Workflow). `CHANGELOG.md` is not in this set: nobody edits it by hand.
