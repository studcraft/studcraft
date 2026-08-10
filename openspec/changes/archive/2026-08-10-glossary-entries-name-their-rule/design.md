# Design — Every glossary entry names the rule that owns it

## The decision that needed making

Eleven of the twelve entries were attribution, not design: each names a term that exactly
one rule defines, and the only work was reading the ruleset to find which. `Priority` is
`FLOW-003`, whose title is *Priority*. `Open Transport` is `TRN-009`, whose title is *Open
Transport*. Those are not judgement calls.

The twelfth was. `Functional Component` had two candidate owners with the same title and
different meanings, and no citation could have been correct while both existed.

## Resolving the collision

### What was found

`python3 scripts/rule.py refs SCS-006` and the same for `CMP-001`: **neither is cited by
anything.** Both are orphans, which is how two rules kept one title without a single
reference ever having to choose between them.

A grep for the phrase across `docs/` settles which rule owns it in practice:

```
docs/05-construction-components.md:29:# CMP-001 — Functional Components
docs/05-construction-components.md:31:A functional component is a physical part of a model that affects gameplay.
docs/05-construction-components.md:252:Removing a functional component immediately changes the model's capabilities.
docs/05-construction-components.md:274:Functional components should be easy to identify.
docs/04-construction-standard.md:87:# SCS-006 — Functional Components
docs/14-glossary.md:87:## Functional Component
```

Every use of the term in running prose in `docs/` is in `CMP-001`'s own document, with
`CMP-001`'s meaning. `SCS-006` holds the title and never uses it.

Outside `docs/`, `README.md`, `CONTRIBUTING.md` and `CHANGELOG.md` each mention functional
components once, all three in `CMP-001`'s sense. None is touched by this change and none is
made wrong by it.

## The duplication the retitle exposes

`SCS-006` and `CORE-007` are near-duplicates, and nothing in the ruleset says so. They list
the same six examples — doors, hatches, ramps, drawbridges, elevators, gates — and both
assert that an interactive element must physically exist and that decoration has no effect.
`CORE-007` adds what operating one costs and is cited by nine rules. `SCS-006` is cited by
none.

The retitle makes this impossible to leave alone: `SCS-006`'s new title is
character-identical to the section heading in `02-core-rules.md` that houses `CORE-007`.
Two rules with the same name and the same examples, in different documents, neither citing
the other, is the collision this change set out to fix — moved rather than resolved.

So `SCS-006` gains one sentence pointing at `CORE-007`. Its immediate neighbours `SCS-007`
and `SCS-008` already cite `CORE-007`; `SCS-006` was the gap in a pattern its own section
otherwise keeps.

**Consolidating them outright was considered and rejected for this change.** Deleting
`SCS-006` in favour of `CORE-007`, or vice versa, removes a rule from the construction
standard that a builder reading only that document would then not find. Which document
should carry a construction requirement that is also an action-economy rule is a real
question, and it is not this change's question. The pointer records the relationship
without pre-empting the answer.

### Chosen: retitle `SCS-006` to `Interactive Elements`

`SCS-006`'s body opens *"Interactive elements must physically exist."* The title
contradicts the sentence directly beneath it, and every example it lists — doors, hatches,
ramps, drawbridges, elevators, gates — is an interactive element rather than a functional
component in `CMP-001`'s sense.

The term is already the ruleset's own. `docs/02-core-rules.md:153` carries a section
headed `Interactive Elements`; `CORE-007` governs operating one; `MOVE-018`, `MOVE-019`
and `MOVE-020` each describe their subject as an interactive element action. Nothing is
being coined.

So this is not a rename that picks a winner between two claims. It corrects a title that
was already wrong about its own contents, and the collision disappears as a consequence.

### Rejected: retitle `CMP-001` instead

`CMP-001` is the rule that actually defines the term, uses it, and is used by two further
paragraphs in its own document. Renaming the rule that owns a term, to preserve the title
of a rule that never uses it, inverts the problem rather than fixing it.

### Rejected: two glossary entries, one per rule

`Functional Component (construction standard)` and `Functional Component (components)`
would record the collision in the glossary instead of resolving it, and leave a reader to
work out which one a given rule meant. The glossary is where a term is disambiguated, not
where an ambiguity is filed.

### Rejected: cite both rules from one entry

Also considered, also wrong: the entry's text — *"A LEGO element that has gameplay
effects"* — is `CMP-001`'s definition and not `SCS-006`'s. Citing both would attach
`SCS-006` to a definition it does not make.

### Rejected: leave the collision and fix only eleven entries

This was the original plan, and splitting it into two changes was offered. It was rejected
because the twelfth entry is not deferrable in the way the other eleven are: leaving it
means leaving the one entry that a reader most needs disambiguated, and a second change
would have to reopen the same file. One change, one file, one reading.

## Why the citations are appended rather than rewritten

`system/communication.md` warns against rewriting text that was already correct: it hides
the real change inside a large diff, and on this repository it also causes artificial merge
conflicts with every concurrent branch. So ten of the eleven entries keep every word they
had and gain a `See …` sentence at the end of the last paragraph, which is the form the 35
already-cited entries use.

`Impact` is the one exception, and an earlier draft of this design claimed no exception
existed — in three separate places, while its own task made one. The entry's last paragraph
already carried a citation to `16-damage-system.md` with no rule ID, so the choice was
between adding `DMG-009` inside that existing parenthetical or leaving a citation half
made. The parenthetical is edited. The absolute claim has been corrected rather than the
task, because the task was right and the claim was not.

## Owner, not echo

Several terms are stated in one rule and restated in another that cites it. The citation
goes to the rule that *makes* the statement, never to the one that repeats it.

This is not a stylistic preference — it decided four of the eleven, and an earlier draft
got all four wrong in the same direction:

- **`Weapon Front`** was pointed at `SCS-018`, whose body defers to `WPN-019` in its own
  first sentence. `WPN-019` is where "every weapon has exactly one Weapon Front" is stated.
- **`Weapon Body`**'s second sentence is about Weapon Length and Weapon Width. `SCS-017`
  mentions neither; `WPN-003` defines Length and `WPN-018` defines Width.
- **`AP`** and **`Activation`** were both pointed at `FLOW-005`, whose first line reads
  "The 3 AP **defined in CORE-006**". `FLOW-005` names its own source, and it is not
  `FLOW-005`.

The rule of thumb that catches these: if the candidate's body cites another rule *for the
thing the glossary entry is defining*, the citation belongs to that other rule.

## Why the comma citation form

Both forms are legal and both are checked by `scripts/lint_ruleset.py`:
`` `10-weapons.md` (WPN-021) `` and `` `08-vehicles.md`, VEH-013 ``.

The comma form is used throughout this change. The parenthesised form is matched by a
pattern that pairs a backticked filename with the next `(RULE-ID)` **within 80
characters**, whichever document that ID actually belongs to — a window that has produced
false failures in this repository before, recorded in
`openspec/changes/archive/2026-08-07-vehicle-height-from-footprint/tasks.md`. The comma
form has no such window.

## What is deliberately not done

- **No entry's definition is corrected.** If one is wrong, that is a separate finding
  against a rule, not something to fold into a citation change.
- **The rules that nothing cites are untouched.** `python3 scripts/rule.py orphans` lists
  them; most are legitimately standalone. It is a reading list, not a defect list. Six of
  them — `FLOW-003`, `FLOW-005`, `SCS-004`, `SCS-017`, `SCS-018`, `CMP-001` — leave that
  list as a side effect of gaining a glossary citation here, which is why the count written
  into `.claude/agents/ruleset-auditor.md` is removed rather than corrected.
- **`rule.py glossary` is not promoted to a gate.** It could be, once this lands and the
  count is 0. That is a tooling change and belongs in a tooling branch, not in a ruleset
  proposal.
