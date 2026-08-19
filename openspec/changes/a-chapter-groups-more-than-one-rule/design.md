# Design — A chapter groups more than one rule

## The problem, stated once

`docs/` has two kinds of `#` heading and no rule telling them apart. A chapter
heading and the rules under it are written at the same level, so the chapter
groups nothing structurally; and a chapter is written even when there is one
rule to group, where it can only repeat that rule's title.

`docs/02-core-rules.md` already writes rules at `##` under `#` chapters and
reads correctly for it — but it also has seven chapters holding a single rule,
so it has one half of the convention and not the other. No document has both.

---

## Decision 1 — The rule is about grouping, not about depth

**Two clauses, and the first is the one that decides:**

> A `#` chapter heading exists only to group two or more rules, and the rules
> inside one are written at `##`. A rule that belongs to no chapter is written
> at `#`.

**The ceiling is what makes this the only workable rule**, and it is worth
stating before the alternatives. `repo.RULE_HEADER_RE` is
`^#{1,2} ([A-Z]{2,6})-(\d{3}) — `, and the document title already occupies `#`.
So a rule has exactly two levels available to it, and every scheme has to fit
inside that.

Two alternatives were considered:

- **"Rules are always `##`"** — every document made to look like
  `02-core-rules.md`. Rejected: it requires inventing a chapter for every rule
  that has no natural subject to sit under, and `08-vehicles.md`'s thirty-one
  rules have no such subjects. A rule that must be nested acquires a parent that
  means nothing, which is the defect this change removes rather than a fix
  for it.
- **A chapter as bold prose rather than a heading**, leaving every rule at `#`.
  Rejected: a chapter that is not a heading is invisible to a table of contents
  and to every script, and the ruleset would have a grouping no tool can read.

**Consequence, accepted deliberately.** Within one document, rules end up at two
levels — `##` inside a chapter, `#` outside one. `02-core-rules.md` after this
change is the clearest instance: two chapters with five rules between them,
seven rules standing alone.

**What that does not achieve, stated plainly.** `#` is still shared by the
document title, the prose sections, the chapters and the standalone rules, so
`# Unit Types` does not outrank `# CORE-002 — Facing` — which is half of the
complaint this change opens with. The fix is partial by construction, because
the two-level ceiling leaves nowhere else to put a chapter. What actually tells
a reader which kind of heading they are looking at is the rule ID in it, which
is also how every script in `scripts/` reads the ruleset. The level is a second
signal, correct where it applies, and not the whole answer.

## Decision 2 — Two is the threshold, and one is the defect

A chapter over one rule can only restate that rule's subject. `# Unit Base`
above `## CORE-001 — Unit Base (UB)` restates the title verbatim; `# Cover`
above `## CORE-010 — Physical Cover` and `# Equipment` above
`## CORE-014 — Visible Equipment` restate part of it; the remaining four name a
subject with one rule under it. **The verbatim cases are the vivid ones, not the
test** — the test is that the chapter groups one thing, which is true of all
seven and of the four outside `02-core-rules.md` as well.

Zero is different, and is not a defect. `# Purpose`, `# Summary`, `# Combat
Flow`, `# Turn Sequence`, `# Weapon Archetypes`, `# Design Notes`, `# The
Battlefield`, `# Universal Rule` hold prose and no rules. They are sections of
a document, not chapters over rules, and the rule does not reach them.

**So the check is exactly one rule, not fewer than two.** That distinction is
the whole reason the linter can be written without a list of exceptions.

## Decision 3 — What happens to a deleted chapter's blurb

Four chapters holding one rule carry an introductory sentence. Three of them say
something the rule already says, and are deleted with the heading:

| Chapter | Blurb | Already in the rule |
|---|---|---|
| `07-movement.md`, `# Falling` | "What the fall costs is its own domain's rule." | `MOVE-015` — "at the risk its own domain's rule describes" |
| `11-combat.md`, `# Damaged Weapons` | "What a weapon's own damage does to the attack it makes." | `CBT-015` — "This rule reads the state of the component that provides the attack." |
| `17-infantry.md`, `# Damage Effects` | "The Component States themselves are `16-damage-system.md` (DMG-005)." | `INF-012`, first line, cites `DMG-005` |

**The fourth is not redundant and is not deleted.** `17-infantry.md`'s
`# Falling` blurb carries the ruleset's only pointer from Infantry's falling
damage to `07-movement.md` (MOVE-015), which states when a unit falls at all
and where it lands. `INF-011` never cited it. Deleting the heading without
moving that sentence would drop a cross-reference, so the sentence is folded
into `INF-011`'s opening paragraph.

This is the failure mode this change had to look for, and the only place it
occurs: a chapter that carries content rather than repeating it.

## Decision 4 — `###` for the worked examples, and nowhere else

`DMG-004` and `DMG-017` carry worked examples as `##` sub-headings. Demoting the
rules to `##` would make those examples the rules' siblings rather than their
subsections, so the eight of them move to `###`.

**Nothing else goes to `###`, and that is a constraint rather than a
preference.** `repo.RULE_HEADER_RE` is `^#{1,2} ([A-Z]{2,6})-(\d{3}) — `, so a
rule written at `###` would stop being visible to `scripts/lint_ruleset.py`,
`scripts/check_id_stability.py`, `scripts/build_index.py`, `scripts/rule.py` and
`scripts/release_cut.py` at once — silently, since each would simply find fewer
rules. Two levels is the ceiling for a rule, so a chapter may not contain a
chapter.

Rejected: widening `RULE_HEADER_RE` to `#{1,3}` to keep the option open. Nothing
needs a third level, and a pattern that permits one invites it.

**The general form, which the rule in `system/` states rather than leaving
implied:** a rule's own sub-headings sit one level below the rule, wherever the
rule sits. That is `###` for `DMG-004`'s examples, because `DMG-004` is inside a
chapter — and `##` for `docs/06-deployment.md`'s `## Patrol`, `## Skirmish`,
`## Battle` and `## Massive Battle`, because `DEP-009` is a standalone rule at
`#`. Both are correct and this change touches only the first. Without the clause
the two documents read as a contradiction.

**They are not equivalent to the tooling, though, and the rule says so after the
audit.** `repo.HEADING_RE` ends a rule's body at the next `#` or `##`, so a
standalone rule's `##` sub-headings fall outside the body `scripts/rule.py` and
the index print, while a chaptered rule's `###` ones do not. `DEP-009` prints
today without its four scenario sub-sections. Repairing the terminator is a
tooling change of its own — `proposal.md`, Out of Scope.

## Decision 5 — `02-core-rules.md` is in scope

Its `SECTION_DEBT` entry in `scripts/lint_ruleset.py` exempts it from having a
Design Philosophy and a Summary. That exemption is about missing sections and
says nothing about heading depth.

Excluding the document was considered, on the grounds that it "predates the
standard". Rejected: it holds seven of the eleven one-rule chapters in `docs/`, so
excluding it would leave the rule true of a minority of the ruleset and would
make the linter check unable to run over the whole of `docs/`. The exemption
stays exactly as wide as it was granted.

## Decision 6 — The linter catches one half, and says so

The check that can be written mechanically: **a `#` chapter containing exactly
one `##` rule.**

The half that cannot: a chapter whose rules were left at `#`. Those rules are
indistinguishable from standalone rules — the same text at the same level — and
no amount of parsing separates them, because the difference is whether the
author meant them as a group.

**The split is measurable, and it is seven to four.** Run against `docs/` as it
stands, the check reports the seven one-rule chapters in `02-core-rules.md`,
whose rules are at `##`. It is silent about the four in `07-movement.md`,
`11-combat.md` and `17-infantry.md`, whose rules are at `#`. Those four are
removed by sections 2, 3 and 5 of `tasks.md` — by a reader, which is the point.

That limitation is written into the function's docstring rather than left for a
reader to discover. A check that silently covers half a rule is worse than one
that states which half.

## Decision 7 — No `openspec/specs/` delta

Nothing in this change alters a requirement or a scenario. Heading levels, three
deleted blurbs that repeated their rule, one sentence moved into the rule that
needed it — no capability behaves differently, and `system/proposal-review.md`
(Delta vs. Direct Edit) is explicit that a change like this is tracked as
ordinary doc-edit tasks in `tasks.md`.

Writing a delta here would mean inventing one, which that document forbids in
as many words.

## Decision 8 — `system/`, `scripts/` and `tests/` ship in this branch

`system/repository-strategy.md` (Branch Naming) gives a ruleset branch
`docs/*.md` plus its one change directory, and would otherwise put
`system/documentation-standards.md`, `scripts/lint_ruleset.py` and
`tests/test_lint_ruleset.py` on a branch of their own.

They ship here, for the reason the change before this one folded
`CODE_OF_DESIGN.md` into the same pull request: **splitting them lands a ruleset
whose convention is written nowhere and checked by nothing**, for however long
the second pull request takes. The rule and the text that obeys it arrive
together or the rule is not yet a rule.

`.claude/rules/tooling.md` requires a script change and the test that pins it to
share a commit, which this does. No CI gate forbids the combination — the
branch-name gate constrains the name, not the file set.

Called out here and in `proposal.md` so the choice is visible rather than
silent.
