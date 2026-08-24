# The ruleset states its rules and stops

## Why

**The ruleset had become too verbose and too complicated to read for a general
audience.** That is the motive, and everything below follows from it.

It had grown a second voice. Beside each rule sat the argument for it, the case
it was chosen over, the reader it was written to reassure. Each addition was
defensible on its own and none was where it went wrong — but the result is a
rulebook that answers a designer's questions in the space where a player is
looking for the rule.

`system/documentation-standards.md` ("How a Rule Is Written") already describes
what that reader needs: **one imperative sentence, the reason in one clause, no
over-explanation.** The standard was not the reason for this pass; it is the
existing statement of the same concern, which is why it is worth matching.

**This is the editorial pass that brings the fifteen documents back to it.** It
is the largest single change to the ruleset so far — fifteen documents, 194 rules
before and 182 after — and almost all of it is deletion.

The reasoning that was deleted is not lost: it is in the git history and in the
archived proposals that put it there, which is where `system/workflow.md` says
design rationale lives. `docs/` holds the current accepted rules.

**This proposal was written after the edits were made.** That is not the
workflow (`system/workflow.md`, Git Workflow) and the change does not pretend
otherwise — `design.md`, Decision 1, records why the sequence was inverted and
what it costs.

## What Changes

### Every document: prose compressed

Justification, worked-out reasoning and defensive qualification are removed from
every rule that carried them. Lists move to a single bullet marker, tables gain
headers, and the boxed statement (`> **If it fits, it deploys.**`) is used where
a rule benefits from a line a player can quote.

**No mechanic changes as a result of this compression.** Where a mechanic *does*
change, it is named below.

### Twelve rule IDs retired

| ID | Document | What happened to it |
|---|---|---|
| `CBT-010` | `11-combat.md` | Simultaneous Resolution — described a case no rule produces |
| `MEL-004` | `12-melee.md` | Its melee half of the same case |
| `MEL-010` | `12-melee.md` | The stub kept for ID stability; the five files naming it are amended instead — `design.md` Decision 10 |
| `GEO-006` | `15-geometry-layers.md` | Minimum Representation — folded into `GEO-005` |
| `GEO-007` | `15-geometry-layers.md` | Detailed Representation — folded into `GEO-005` |
| `WPN-013` | `10-weapons.md` | Attack Procedure — restated `CBT-001` |
| `WPN-017` | `10-weapons.md` | Future Weapon Types — a list of things that do not exist |
| `VEH-028` | `08-vehicles.md` | Maximum Height — **a mechanic is removed, see below** |
| `DMG-009` | `16-damage-system.md` | Combat Resolution Overview — replaced by `DMG-008` |
| `DMG-010` | `16-damage-system.md` | Generate Impacts — `WPN-006` already says it |
| `DMG-011` | `16-damage-system.md` | Attack Roll — moved to `11-combat.md`, `CBT-005` |
| `DMG-018` | `16-damage-system.md` | Weapon Distribution — moved to `11-combat.md`, `CBT-007` |

All twelve stay retired. `MEL-010` was the ruleset's one sanctioned stub, named
as such by five files outside `docs/`; those five are amended rather than the
rule restored (`design.md`, Decision 10).

### `16-damage-system.md`: the `DMG-*` numbers move

Deleting four rules from the middle of the document closed the gaps rather than
leaving them. Every number from `DMG-002` to `DMG-018` now names a different
rule than it did:

| Rule | Was | Is now |
|---|---|---|
| Component State Progression | `DMG-005` | `DMG-002` |
| Universal Destruction | `DMG-006` | `DMG-005` |
| Internal Components | `DMG-007` | `DMG-006` |
| No Material-Specific Mechanics | `DMG-008` | `DMG-007` |
| Select Target Component | `DMG-012` | `DMG-011` |
| Composite Vehicle Targeting | `DMG-013` | `DMG-012` |
| Geometry Check | `DMG-014` | `DMG-013` |
| Damage Roll | `DMG-015` | `DMG-014` |
| Multiple Impacts | `DMG-016` | `DMG-015` |
| Penetration | `DMG-017` | `DMG-016` |
| Repairs | `DMG-019` | `DMG-018` |

**`system/documentation-standards.md` (Naming Conventions) forbids exactly
this**: "Rule identifiers are never renumbered and never reused." The
renumbering is a knowing exception, taken by the maintainer, and `design.md`
(Decision 3) states the reasoning and the price. **The price is paid in this
change**: every citation aiming at a moved number is repaired here, and
`tasks.md` lists them one by one.

### `08-vehicles.md`: footprint no longer bounds height

`VEH-028` derived a vehicle's maximum height from its own footprint — one Unit
Base of height for every two studs of its narrowest side. That rule is gone. A
vehicle's height is now bounded by one thing only: the ceiling the players
agreed in the Deployment Volume (`06-deployment.md`, DEP-001).

`VEH-029` (where height is counted from) and `VEH-030` (what counts toward it)
are unchanged and now feed that single bound.

### `06-deployment.md`: `DEP-002` reads the floor as a placement

`DEP-002` had stated the floor as arithmetic — each model spends the Unit Bases
of its footprint, and the total may not exceed the floor. It now states it as a
placement: an army is legal if every model can be physically placed inside the
Deployment Volume at the same time, with no overlaps.

This reverses the decision `a-deployment-volume-is-floor-and-ceiling` (#129)
made two changes ago. `DEP-001` still carries one clause from that change —
"The floor is counted rather than treated as a shape" — and **that clause and
`DEP-002` disagree**. `design.md` (Decision 5) records the choice this proposal
makes and `tasks.md` (section 1) carries the repair.

### `03-game-flow.md`: the Turn Sequence diagram is removed

The fenced flow diagram restated `FLOW-002` and `FLOW-003` in ASCII. The
document's own Summary now carries the sequence as a numbered list.

### Outside `docs/`

- **`assets/IMAGES.md`** — the `VEH-028` image row is removed with its rule, and
  the penetration row is renumbered `DMG-017` → `DMG-016`. `system/repository-strategy.md`
  (Branch Naming) allows a ruleset branch to carry a non-`docs/` file when
  `design.md` names it; Decision 7 does.
- **`TODO.md`** — the quoted-ruleset section is cut to match. `Docs must not
  edit CHANGELOG.md directly` and `TODO.md quotes the ruleset verbatim` are both
  required checks and both pass.
- **`cspell.json`** — two words added (`rulebook`, `wargame`).
- **`system/documentation-standards.md`, `system/workflow.md`,
  `system/proposal-review.md`, `scripts/check_delta_coverage.py`,
  `.claude/agents/ruleset-auditor.md`** — all five cite `MEL-010` as the one
  retired-but-kept number. Amended, not the rule restored. Decision 10.
- **`tests/test_ruleset_ast.py`, `tests/test_build_index.py`** — two tests
  pinned rule bodies against named rules in `docs/` and broke when a rule gained
  a sub-heading. They now pin the behaviour and check the invariant across all
  fifteen documents. Decision 8.
- **Nine files in `scripts/`, plus `.claude/rules/tooling.md`** — see below.

### `scripts/` stops naming rules that exist

**No script's behaviour ever depended on a rule**, and this change checked that
rather than assuming it: every match of `[A-Z]{2,6}-[0-9]{3}` in `scripts/` was
in a comment, a docstring or a `--help` line, and the only rule-shaped thing in
the code is `repo.RULE_ID_RE`, which is generic.

**The illustrations were the dependency, and three had already rotted** —
`lint_ruleset.py` named `DMG-019` as the example its regex must not swallow, and
`DMG-019` no longer exists; `check_todo_quotes.py` quoted a sentence of
`WPN-016` this change deleted; `lint_ruleset.py`'s docstring quoted a
`06-deployment.md` citation no longer written that way.

Every one now uses an invented prefix (`AAA-`, `BBB-`) or a placeholder, none of
which can rot. The constraint is written into
`system/documentation-standards.md` beside rule-ID stability, and
`.claude/rules/tooling.md` — the file an agent loads when it edits a script —
points at it. `design.md`, Decision 11.

### The constraint becomes a gate

Writing a rule into `system/` and leaving nothing to enforce it is the shape
`.claude/rules/tooling.md` warns about: *"Context can be read and ignored; a
hook cannot."* `scripts/lint_ruleset.py` already holds the set of live rule IDs,
so **no file in `scripts/` may name a rule that exists in `docs/`** is now a
required check, with tests, and verified by making it fail on purpose and
reverting — a check nobody has seen fail is a check nobody has tested.

`SECTION_DEBT`, the linter's per-document exemption, shrank in the same pass.
It exempted `02-core-rules.md` from a Design Philosophy section and a Summary;
this change gave that document a Design Philosophy, and **nobody noticed for
several commits**, because an exemption's function is to stop the check from
asking. Only the Summary is still owed. `design.md`, Decision 12.

**One check is scheduled rather than shipped.** `check_id_stability.py` should
report an ID that kept its number while its rule changed underneath — the defect
this change committed eleven times, and the source of every broken citation it
then had to repair. It cannot land here: `preflight.py` compares against
`origin/main`, and this branch *is* eleven of them, so the check's first act
would be to fail the change that adds it. Once this merges, `main` carries the
new numbering and it lands green in the next pull request.

## What Does Not Change

- **Every mechanic not named above.** Attack Roll thresholds, the Geometry
  Check, the Damage Roll, Impact Strength, Weapon Capacity, Action Points,
  Terrain Thresholds, transport capacity and interior levels all resolve exactly
  as they did. The words are shorter; the numbers are identical.
- **The `Wounded` degradations.** Still exactly three, still owned by
  `INF-012`, `VEH-031` and `CBT-015`.
- **Every rule prefix, and every document number.** No document is added,
  removed or renumbered.
- **`CHANGELOG.md` and every `**Version:**` header.** Release-cut only
  (`system/documentation-standards.md`, Versioning).

## What the Audit Found, and Where It Went

The applied text was audited read-only before this proposal was finished
(`system/proposal-review.md`, "Review the Applied Text, Not Only the Diff").
It found eleven repairs, **two of them blockers**, and all of them are applied
— `tasks.md` Part B carries them as anchor pairs and every box but one is
ticked.

- **One clause of `DEP-001` contradicted `DEP-002`.** "The floor is counted
  rather than treated as a shape" against a rule that makes physical placement
  the final check: a Buggy (`2 × 2 UB`) deployed in `DEP-009`'s `5 × 1 × 2 UB`
  Patrol volume under one and not the other. The two rules' jobs were fine; one
  sentence was not. Task 1.1.
- **Twenty-eight citations aimed at the wrong rule**, all consequences of the
  renumbering. Two inverted a rule's meaning rather than mislabelling it:
  `02-core-rules.md` and `11-combat.md` both sent a reader asking "can I target
  this?" to Composite Vehicle Targeting, which grants the opposite. **The linter
  cannot see any of it** — it checks that a cited ID exists, and all of these
  did. Section 2.

Two of the audit's own claims were wrong, and the verification greps in
`tasks.md` are what caught them: `MEL-010` was cited from five files rather than
three, and one `DMG-018` mention survived in `assets/IMAGES.md` prose. Both are
repaired.

**One box is deliberately unticked**: task 12.1 moves #129's superseded delta to
`specs-superseded/`, and `Docs require OpenSpec proposal` fails a pull request
touching two change directories. It is a separate PR, and it is why
`scripts/archive_cut.py` will skip this change until then.

## Out of Scope

- **Restoring the deleted rationale to `docs/`.** It belongs in the archived
  proposals, and this pass is the argument that it does.
- **Re-deciding the floor question.** Decision 5 picks the reading that makes
  the chapter agree with itself; whether packing or budget is the better game is
  the question #129 already answered and this change does not reopen on its
  merits.
- **`DEP-007`, `DEP-008` and `DEP-009`'s overlap**, which #129 also left
  standing.
