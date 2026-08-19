# A chapter groups more than one rule

## Why

`docs/` uses two kinds of `#` heading and does not distinguish them. One names a
rule. The other names a chapter that gathers several rules under a subject —
`# Terrain Movement`, `# Component Damage`, `# Line of Sight`.

Both are written at the same level, so a chapter does not visually outrank the
rules it is supposed to contain. `docs/02-core-rules.md` is the exception that
shows what the convention should have been: its rules are at `##` under `#`
chapters, and there the hierarchy reads correctly.

Two defects follow from having no rule about this.

**A chapter that groups nothing.** `# Unit Base` holds `## CORE-001 — Unit Base
(UB)` and nothing else, repeating the rule's own title one line above it. Six
more like it sit in `02-core-rules.md`, and four more across `07-movement.md`,
`11-combat.md` and `17-infantry.md` — the last of which has two. **Eleven
headings that add a level of structure over one rule.**

**A chapter that groups something, at the wrong level.** `# Terrain Movement`
holds three rules and `# Component Damage` holds eight, all written at `#`, so
the chapter heading and its members are peers and the grouping exists only in
the reading order.

The rule this change writes down:

> **A `#` chapter heading exists only to group two or more rules, and the rules
> inside one are written at `##`. A rule that belongs to no chapter is written
> at `#`.**

`CODE_OF_DESIGN.md` Principle 12 is consistency; `system/documentation-standards.md`
already fixes the document skeleton and the rule-ID convention and says nothing
about heading depth, which is why the two patterns coexisted.

## What Changes

Five ruleset documents, one `system/` document, one script and its test.
**No rule ID is renumbered, retired or reused. No gameplay value changes.**

- **`docs/02-core-rules.md`** — seven chapters holding one rule each are
  deleted, and their rules move from `##` to `#`: `Unit Base`/`CORE-001`,
  `Unit Orientation`/`CORE-002`, `Activation`/`CORE-006`,
  `Interactive Elements`/`CORE-007`, `Cover`/`CORE-010`,
  `Equipment`/`CORE-014`, `Physical State`/`CORE-016`. `# Unit Base` restates
  its rule's title verbatim and two more restate part of it; the rest simply
  name a subject that has one rule under it, which is the defect either way.
  `# Unit Types` (`CORE-003`, `CORE-004`,
  `CORE-005`) and `# Line of Sight` (`CORE-008`, `CORE-009`) group two or more
  and are untouched — they are the pattern the rest of `docs/` adopts here.
- **`docs/07-movement.md`** — `# Terrain Movement` keeps its three rules, which
  move to `##`. `# Falling` holds only `MOVE-015` and is deleted; its one
  sentence says what `MOVE-015` already says.
- **`docs/11-combat.md`** — `# Damaged Weapons` holds only `CBT-015` and is
  deleted, with the same reasoning.
- **`docs/16-damage-system.md`** — `# Component Damage` (eight rules) and
  `# Damage Resolution` (eleven) both keep their intros; all nineteen rules
  move to `##`. The eight worked examples inside `DMG-004` and `DMG-017` move
  from `##` to `###` so they stay subsections of the rule that owns them
  instead of becoming its siblings.
- **`docs/17-infantry.md`** — `# Terrain` keeps its five rules, which move to
  `##`. `# Falling` and `# Damage Effects` each hold one rule and are deleted.
  **`# Falling`'s pointer at `MOVE-015` is not dropped**: `INF-011` never cited
  it, so the sentence is folded into `INF-011`'s opening paragraph.
- **`system/documentation-standards.md`** — the rule, in Documentation
  Guidelines, beside the document skeleton it belongs with.
- **`scripts/lint_ruleset.py`** and **`tests/test_lint_ruleset.py`** — a chapter
  holding exactly one rule fails the linter, as does a rule written at `###` and
  a rule nested under another rule. Without the check the pattern comes straight
  back: nothing else in the repository can see a heading level.
- **`.claude/agents/proposal-applier.md`** — its standing "never change an
  existing heading" is restricted to a rule's ID and title, which is what it
  always meant. This change moves forty-six headings between levels and deletes
  eleven, so the sentence as written told the applier to stop and report the
  work it was given (`tasks.md`, section 8).

## What Does Not Change

- **No gameplay value, anywhere.** This change alters heading levels, deletes
  three chapter blurbs that repeat their rule, and moves one sentence into the
  rule that needed it. No rule's text changes otherwise.
- **No rule ID.** `system/documentation-standards.md` (Naming Conventions) —
  every ID keeps its number and its document.
- **Anchors and cross-references.** A markdown anchor is derived from a
  heading's text, not its level, so `#` to `##` changes no link. Nothing in
  `docs/`, `README.md` or `assets/IMAGES.md` links to a heading by anchor —
  checked, and recorded under *Checked elsewhere*.
- **Prose sections.** A `#` heading holding no rules is not a chapter of rules:
  `# The Battlefield`, `# Universal Rule`, `# Physical Priority`, `# Combat
  Flow`, `# Turn Sequence`, `# Examples`, `# Weapon Archetypes`, `# Design
  Notes`, `# Combat Examples`, `# Combat Philosophy`, and every `# Purpose`,
  `# Design Philosophy` and `# Summary`. All untouched, and the linter check is
  written so none of them is flagged.
- **`docs/01-foundations.md`, `docs/14-glossary.md`** and every other ruleset
  document. They define no chapters over rules.
- **`openspec/specs/`.** No delta. This is document structure: no requirement
  and no scenario stops being true, and `system/proposal-review.md` (Delta vs.
  Direct Edit) covers tracking it as ordinary doc-edit tasks.
- **`CHANGELOG.md` and every version header.** Release-cut-only.

## Checked elsewhere

- `python3 scripts/rule.py` and `scripts/build_index.py` read rule headings
  through `repo.RULE_HEADER_RE`, which is `^#{1,2} ([A-Z]{2,6})-(\d{3}) — `.
  Both levels already match, so no script needs changing to keep reading the
  ruleset. **`###` would not match** — that is why the change never nests a
  rule three deep, and why the eight worked examples are the only headings
  moved to `###`.
- `grep -rn "\.md#" docs/ README.md assets/IMAGES.md` — no anchor links into a
  ruleset heading anywhere. Changing a heading's level strands nothing.
- `assets/IMAGES.md` names rules by ID and documents by filename, never by
  heading level. `scripts/lint_ruleset.py`'s image check is unaffected.

## The exemption that does not cover this

`docs/02-core-rules.md` is a recorded exemption in `scripts/lint_ruleset.py`
(`SECTION_DEBT`) — it has no Design Philosophy and no Summary section. **That
exemption is about missing sections, not about heading depth**, and this change
neither uses it nor extends it. The document keeps the exemption for what it
was granted, and its seven one-rule chapters go like everyone else's.

Its remaining shape is the pattern the ruleset now follows: two chapters that
group, and seven rules that stand alone.

## Out of Scope

- **Giving `02-core-rules.md` its missing sections.** Still owed, still its own
  change.
- **A check for the other half of the rule.** A chapter whose rules were left at
  `#` is indistinguishable from a run of standalone rules — no script can tell
  the two apart, and `tasks.md` says so where the check is written rather than
  implying the linter now covers the whole convention.
- **The prose sections listed above.** Whether `# Combat Flow` and `# Turn
  Sequence` earn their place is a question about content, not about depth.
- **`repo.HEADING_RE`, which ends a rule's body at the next `#` or `##`.** A
  standalone rule's `##` sub-headings therefore fall outside the body
  `scripts/rule.py` and the ruleset index print, while a chaptered rule's `###`
  ones do not — `scripts/rule.py show DEP-009` loses its four scenario
  sub-sections today, and did before this change. Task 8.2 makes the
  consequence visible in the written rule; narrowing the terminator touches
  `scripts/rule.py`, `scripts/build_index.py` and the index, and is a tooling
  change with its own proposal.
- **`system/repository-strategy.md`'s Branch Naming table.** This is the second
  consecutive ruleset branch to carry a file the table does not grant it, and
  each has argued the exception in its own `design.md`. The table is what keeps
  being falsified, and amending it is a `system/` change of its own rather than
  a third exception.
