# What `system/` Is For

**`system/` is context for AI agents. It is not human-facing documentation.**

Every line here is loaded into a context window, where it competes with the
line that actually decides something. So, when writing anything under
`system/`:

- **If it is already stated elsewhere, delete it and point at the owner.** One
  owner per rule. A convenient summary is what goes stale, and a shortened
  restatement silently drops what it left out.
- **Only content with no other home survives.** A file whose every line has a
  destination is deleted, not kept for its organisational role.

---

# How a Rule Is Written

Rules here and in `docs/` are read under load, by agents and by people with a
task in hand. Length is a cost paid on every read.

- **A rule is one imperative sentence.** Its reason is one clause at most.
- **No postmortem narration.** Name a past defect only where a reader needs it
  to recognise the case — that is what `system/proposal-review.md` is. Never
  narrate the cost of fixing it: "this cost two PRs" changes nothing a reader
  does.
- **No "this used to say X".** The diff records that. A correction left in the
  text reads later like a rule.
- **No section for a case that does not exist yet.** Write it when it exists.
- **No snapshot a command can print.** Give the command.
- **If the rule is clear in two lines, three lines is a defect.**

Prose that argues, rather than states, belongs in a proposal's `design.md`.

---

# The context lives in the repository

An agent's own memory, scratchpad or session notes are **not** a valid home for
anything about this repository. Constraints live in `system/`, `AGENTS.md` and
`.claude/agents/` — versioned and reviewable. If it is not worth a commit, it
is not worth remembering.

Two settings enforce it: `autoMemoryEnabled: false` removes the motive, and a
`PreToolUse` hook denying `/.claude/projects/*/memory/` removes the capability.
The second is not redundant — `Write` never consults the setting, and that is
the path the one real violation took.

Committing a constraint is necessary and not sufficient; something has to load
it. Three mechanisms do, and they are not interchangeable:

- **`CLAUDE.md`** — one `@AGENTS.md` import. Claude Code loads this name, not
  `AGENTS.md`. It carries no rules of its own.
- **`.claude/rules/*.md`** — `paths:` frontmatter, so each loads only for the
  files it governs. They route to an owner; they do not summarise one.
- **The `PreToolUse` hook** in `.claude/settings.json` — refuses edits that
  break the branch, proposal and version rules. Context can be read and
  ignored; a hook cannot.

---

# Repository Structure

| Path | Holds |
|---|---|
| `docs/` | the ruleset — numbered documents, the only accepted rules |
| `system/` | this directory: agent context, one owner per rule |
| `openspec/` | `changes/` (active proposals, `archive/` for completed) and `specs/` (capability specs, written only by Archive cut) |
| `scripts/` | the checkers and the cut/PR automation; each states its job in its own docstring |
| `tests/` | the pytest suite over `scripts/`; pytest is a development dependency and `scripts/` stays stdlib-only |
| `.claude/` | `settings.json` (hooks, permissions), `agents/`, `rules/`, `hooks/` |
| `assets/` | `IMAGES.md` owns the example-image spec; `images/` holds the files |

`ls` is the authority on contents. The `04-*.md` and `13-*.md` gaps in `docs/`
are deliberate: `04-construction-standard.md` and `13-materials.md` were
removed and their numbers retained, per Naming Conventions below.

---

# Documentation Guidelines

Each document has one responsibility. Rules are deterministic, concise, easy to
reference, and reuse existing terminology. Write them per **How a Rule Is
Written** above.

Every document that defines rules carries: Purpose, Design Philosophy, Rule
Definitions, Summary. `scripts/lint_ruleset.py` checks the first, second and
fourth as headings — the rule headers are the definitions, so "Rule
Definitions" is not one. `01-foundations.md` and `14-glossary.md` define no
rules; `02-core-rules.md` predates the standard and is a recorded exemption in
the linter, not a precedent.

A `#` chapter heading exists only to group two or more rules, and the rules
inside one are written at `##`; a rule belonging to no chapter is written at
`#`, because a chapter over one rule says nothing that rule's own heading does
not. A `#` section holding no rules is prose, not a chapter, and this does not
reach it.

A rule's own sub-headings — worked examples, tables of cases — sit one level
below the rule wherever the rule sits: `##` under a standalone rule, `###`
under one inside a chapter. **No rule is itself written at `###`**: a chapter
groups rules and never another chapter, so a rule has two levels open to it
and no third, and `scripts/lint_ruleset.py` reports one written deeper. A
rule's body runs to the next heading that is not its own descendant, so a
sub-heading at either level stays inside the rule that owns it — `scripts/rule.py`
and the ruleset index both read that span from `scripts/ruleset_ast.py`.

Every document closes with a motto: `> **Every Brick Matters.**` for
construction and gameplay documents, `> **The Model Is The Rules.**` for the
two about the model-defines-values mechanism (`15-geometry-layers.md`,
`16-damage-system.md`). `01-foundations.md` carries both, closing with the
first. The linter checks the last non-empty line.

---

# Adding a New Ruleset Document

Adding a numbered `docs/NN-name.md` touches more than the file. Each of these
has been missed at least once:

- The document itself, with a stable rule-ID prefix and the required skeleton.
- **No `**Version:**` header** — write none, and change nothing to allow that.
  The Release cut inserts it, and it is the only code permitted to.
- `README.md` — structure list, Rulebook reading order (its numbers are
  positions, so inserting renumbers everything after), Current Status.
- `docs/14-glossary.md` — the new terms a reader cannot infer.
- `python3 scripts/lint_ruleset.py`, after writing it.

One change may introduce several capabilities and still ship as one document —
`system/proposal-review.md` ("Capability Boundaries Don't Have to Match
Document Boundaries").

---

# Naming Conventions

Rule identifiers are never renumbered and never reused: `MOVE-001`, `WPN-001`,
`CBT-001`, `FLOW-001`. Each document owns its own prefix. A removed document's
number is never reused either.

A rule may be deleted. Its number is retired, never reissued, and no stub is
left in its place — the diff records that the rule was there. Where the rule
stays and only its design was superseded, the note goes inside that rule.

Image filenames are a separate namespace owned by `assets/IMAGES.md`.
`scripts/lint_ruleset.py` checks them against that convention and against the
rule IDs in `docs/`.

**A script never names a rule that exists**, in code, comment, docstring or
`--help` text. No script's behaviour depends on one — the only rule-shaped
thing in `scripts/` is `repo.RULE_ID_RE` — and an illustration that names a
live ID is a dependency on a rule that can be retired or renumbered. Illustrate
with an invented prefix (`AAA-001`, `BBB-002`), a placeholder, or an invented
number under a real prefix (`VEH-099`): none of the three can rot.

`tests/` is not held to this. A test fixture defines its own document, so an ID
inside one is local by construction and names nothing in `docs/`. What a test
must not do is reach into `docs/` for a *real* rule — that is the dependency,
and it is what `tests/test_ruleset_ast.py` and `tests/test_build_index.py` were
repaired for.

---

# Versioning

StudCraft follows Semantic Versioning (`MAJOR.MINOR.PATCH`).

**Nobody edits `CHANGELOG.md` or a `**Version:**` header by hand.** Both are
written by the `Release cut` workflow in one pass. Several proposal branches
are usually in flight, and a version chosen on one collides with every sibling
that chose the same one — deferring to the cut is what makes concurrent
proposals possible. `Docs must not edit CHANGELOG.md directly` fails the PR
that tries.

A ruleset change declares nothing about its own version. `docs/*.md` changes
default to a minor bump; a commit needing a major says `**Bump:** major` in its
message. `system/workflow.md` (Versioning) has the mechanism.
