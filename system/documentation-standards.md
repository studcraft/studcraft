# What `system/` Is For

**`system/` is context for AI agents. It is not human-facing documentation.**

That single fact decides how these documents are written, and it is the reason
for the deletions in this repository's history rather than the tidy summaries
someone might expect instead.

Every line here is loaded into an agent's context window, where it competes
with the line that actually decides something. A restatement a human reader
would find harmlessly reassuring — the same principle in shorter words, one
file closer to hand — is, for an agent, noise diluting the signal. And a
shortened restatement is never merely redundant: `AGENTS.md` reprinted eight of
fifteen principles and silently dropped the two that catch the most defects;
`design-process.md` reprinted five of seven checklist questions the same way.

So, when writing anything under `system/`:

- **If it is already argued elsewhere — `CODE_OF_DESIGN.md`, another `system/`
  file, a script's docstring — delete it and point at the owner.** Do not keep
  a convenient summary. One owner per rule.
- **Only content with no other home survives.** A file whose every line has a
  destination is deleted, not preserved for its organisational role.
- Prefer a pointer to a copy, always, even when the copy would be shorter to
  read. The copy is what goes stale.

## The context lives in the repository

An agent's own memory, scratchpad or session notes are **not** a valid home for
anything about this repository. Constraints live in `system/`, `AGENTS.md` and
`.claude/agents/` — in the repository, versioned and reviewable — *"rather than
in whoever is driving the session"* (`AGENTS.md`), and so they *"do not have to
be retyped from memory each session. They had been, and they drifted"*
(`system/delegating-to-agents.md`).

This has been violated in practice, by an agent that learned a criterion during
a session and wrote it to its own local memory instead of here. Anything worth
remembering about this repository is worth committing to it. If it is not worth
a commit, it is not worth remembering.

---

# Repository Structure

```
/
├── README.md
├── CODE_OF_DESIGN.md
├── CONTRIBUTING.md
├── CHANGELOG.md
├── LICENSE
├── AGENTS.md
├── system/
│   ├── design-process.md
│   ├── documentation-standards.md
│   ├── workflow.md
│   ├── proposal-review.md
│   ├── delegating-to-agents.md
│   ├── ci-gates.md
│   ├── repository-strategy.md
│   └── communication.md
│
├── openspec/
│   ├── config.yaml
│   ├── changes/          (active proposals; changes/archive/ holds completed ones)
│   └── specs/             (canonical capability specs, written only by Archive cut)
│
├── scripts/
│   ├── generate_site_docs.py   (builds site/docs/; TITLES dict must list every docs/*.md)
│   ├── lint_ruleset.py         (structural check; see Documentation Guidelines below)
│   ├── check_delta_coverage.py (a MODIFIED delta may not drop a living spec's scenario)
│   ├── release_cut.py          (batches CHANGELOG.md + Version-header updates)
│   └── archive_cut.py          (batches openspec/changes/ -> openspec/changes/archive/)
│
├── site/
│   ├── _config.yml, Gemfile, index.md   (Jekyll site source, hand-maintained)
│   └── docs/   (generated copy of /docs, gitignored — do not hand-edit)
│
└── docs/
    ├── 01-foundations.md
    ├── 02-core-rules.md
    ├── 03-game-flow.md
    ├── 04-construction-standard.md
    ├── 05-construction-components.md
    ├── 06-deployment.md
    ├── 07-movement.md
    ├── 08-vehicles.md
    ├── 09-transport.md
    ├── 10-weapons.md
    ├── 11-combat.md
    ├── 12-melee.md
    ├── 14-glossary.md
    ├── 15-geometry-layers.md
    └── 16-damage-system.md
```

This tree is illustrative, not exhaustively re-verified on every change —
`docs/` in particular grows with every ruleset proposal. **Trust `ls` over
this list whenever they disagree**, for every directory here and not only
`docs/`: the two entries that had actually gone stale were
`system/delegating-to-agents.md` and `scripts/check_delta_coverage.py`,
each added by a PR that updated the thing it introduced and not the tree
describing it. See "Adding a New Ruleset Document" below for what to
update when `docs/` changes.

The `13-*.md` gap is deliberate — `13-materials.md` was removed and its
number retained as a gap, not reused, per the Naming Conventions below.

Agents should preserve this modular organization.

---

# Documentation Guidelines

Each document should have one clear responsibility.

Avoid mixing unrelated systems.

Rules should:

- Be deterministic.
- Be concise.
- Be easy to reference.
- Reuse existing terminology.

Every document that defines rules should include:

- Purpose
- Design Philosophy
- Rule Definitions
- Summary

`scripts/lint_ruleset.py` checks for Purpose, Design Philosophy and Summary as
headings, in every document that defines rules. "Rule Definitions" is not a
heading anywhere in `docs/` — the rule headers are the definitions — so it is
not checked as one. `01-foundations.md` and `14-glossary.md` define no rules
and are not required to carry the sections; `02-core-rules.md` predates the
standard and is missing Design Philosophy and Summary. That last one is a
recorded exemption in the linter, not a precedent: a new document cannot be
added to the list without editing the script.

Every document closes with one of StudCraft's two co-equal mottos: `> **Every Brick Matters.**` for construction/gameplay documents, or `> **The Model Is The Rules.**` for the two documents specifically about the model-defines-values mechanism (`15-geometry-layers.md`, `16-damage-system.md`). This split is deliberate, not an inconsistency to fix.

`01-foundations.md` carries **both**, because it introduces both — `> **The Model Is The Rules.**` first, then `> **Every Brick Matters.**` as the closing line. The linter checks the last non-empty line, so a document ending in either motto passes and this one is not a special case in the script.

---

# Adding a New Ruleset Document

Adding a new numbered `docs/*.md` file touches more than the file itself.
Every one of these was missed at least once while shipping a proposal in
this repo — treat this as the checklist:

- `docs/NN-name.md` itself, with a stable rule-ID prefix (see Naming
  Conventions below) and the required Purpose / Design Philosophy / Rule
  Definitions / Summary structure.
- `scripts/generate_site_docs.py`'s `TITLES` dict — its own
  `check_titles_match_source()` guard fails the site build if this is out
  of sync, but only when the build actually runs; don't rely on that alone.
- `README.md`: the Repository Structure tree, the Rulebook reading-order
  list (note its numbers are reading-order position, not filename number —
  inserting a document renumbers everything after it), and the Current
  Status implemented-systems list.
- `docs/14-glossary.md`: at least the new terms a reader can't infer from
  context.
- `python3 scripts/lint_ruleset.py`, after writing the document, to catch
  rule-ID and cross-reference mistakes before they ship.

One OpenSpec change can introduce multiple capabilities while still
shipping as a single document when they're tightly coupled — see
`system/proposal-review.md` ("Capability Boundaries Don't Have to Match
Document Boundaries") for when to do that instead of one document per
capability.

---

# Naming Conventions

Rule identifiers should remain stable.

Examples:

```
MOV-001
WPN-001
CBT-001
TRN-001
FLOW-001
```

Each document owns its own namespace.

---

# Versioning

StudCraft follows Semantic Versioning.

```
MAJOR.MINOR.PATCH
```

Examples:

- 0.1.0
- 0.2.0
- 1.0.0

**Nobody edits `CHANGELOG.md` or a `**Version:**` header by hand — agents least
of all.** Both are written by the `Release cut` workflow, which computes the
next version from the commits since the last tag and rewrites every header in
one pass. `Docs must not edit CHANGELOG.md directly` is a required status check
that fails any PR changing `docs/*.md` which also touches `CHANGELOG.md`.

This is not a style preference. Several proposal branches are usually in flight
at once, and a version number or changelog entry chosen on a branch collides
with every sibling branch that chose the same one. Deferring both to the cut is
what makes concurrent proposals possible at all — see `system/workflow.md`.

So a ruleset change declares nothing about its own version. `docs/*.md` changes
default to a minor bump automatically; a commit that needs a major says so with
a `**Bump:** major` line in its message, and `scripts/release_cut.py` reads it.
