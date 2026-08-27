# Design — Infantry states its distances in Unit Bases

Eight decisions. Decision 1 records a process defect; Decisions 3 and 6 change
what the rules say.

---

## Decision 1 — The edits came first, and the proposal second

`system/workflow.md` (Git Workflow) is unambiguous: **every change to a
`docs/*.md` file goes through an OpenSpec proposal first.** This one did not.
`17-infantry.md` was edited by hand on branch `fix-infantry`, with the two
citation repairs in `07-movement.md` and `08-vehicles.md` beside it, and this
proposal was written afterwards.

**Recorded rather than hidden.** #130 took the same defect and wrote it down for
the same reason: a proposal in the past tense that reads as if it had been
written first can only be accepted or refused, because the alternative it would
have been argued against no longer exists.

What it cost is countable here. `proposal-auditor` reads a proposal *before* it
is applied; run against the applied text instead, it returned **eleven repairs,
three of them blockers** — the unit spelled `BU`, `UB` used as a distance with no
rule defining that reading, and a Summary contradicting the rules above it. Two
more were rules deleted with the prose around them: `INF-004`'s Action Point
cost, and `INF-009`'s statement that a step too tall to climb stops the climb
there. Every one is in `tasks.md` Part B, and every one would have been a comment
on a draft rather than an edit to the ruleset.

**It took two audit passes.** The first read produced the eleven; the second,
after Part C was added, found a retired rule still cited from
`CODE_OF_DESIGN.md` and a preamble instructing the applier to refuse the section
that retires it. Both are blockers, and both are Part C's, not Part A's — which
is the argument for auditing a proposal each time its scope grows, not once.

**Rejected: rewriting history so the proposal predates the edits.**
`system/repository-strategy.md` forbids it, and it trades a recorded process
defect for an unrecorded one.

---

## Decision 2 — `UB` gains a second reading, and every distance rule names its axis

Two things had to be true together, and the hand edit did neither.

**`UB` had one meaning and it was a volume.** `CORE-001` defines the Unit Base
as `4 × 3 × 13` plate layers; every bare `N UB` in the ruleset counts volumes,
and the only written form for counting them was `W × D UB`, a footprint. "Up to
4 UB forward" is a length along one axis, which is a third reading, and a reader
arriving from `09-transport.md` has no way to know that. **`CORE-001` states the
reading**, because it owns the term (`system/documentation-standards.md`, "What
`system/` Is For"), with the glossary entry and `01-foundations.md`'s list of
uses following it.

**The axes differ, so the numbers invert.** `CORE-001` already requires each rule
to name the dimensions it reads, and infantry is the case that requires it most:
the base is 3 studs deep and 4 studs wide, so **4 UB forward and 3 UB sideways
are both 12 studs**. Without the axis clause the obvious reading of `4 > 3` is
wrong. So `INF-002`, `INF-003`, `INF-004` and `INF-012` each name their axis and
give the stud figure once:

> Forward movement reads the Unit Base's 3-stud depth (`02-core-rules.md`,
> CORE-001), so 4 UB is 12 studs.

That is one clause of reason attached to one imperative sentence, which is what
`system/documentation-standards.md` ("How a Rule Is Written") asks for.

**Rejected: keeping the distances in studs.** The unit-base spec requires every
distance in `UB`, the stud figures are derived from the Unit Base anyway, and
every rule citing them had to restate the derivation.

**Rejected: a single infantry movement unit that is the same in both
directions.** That is a rule change — one of 12 studs sideways or 12 forward
would have to move — and neither the model nor any complaint about play asks for
it. `The Model Is The Rules`: the base has two different edges, and the rules
read them as two.

**The applied text wrote `BU`, and the ruleset's abbreviation is `UB`.** The
transposition is corrected in `tasks.md` Part B rather than adopted. Nothing in
the ruleset is called a `BU`.

**The volume-count reading stays contextual, and is not defined here.**
`CORE-001` will define two written forms — `W × D UB` for a footprint and `N UB`
for a distance along a named axis. A third is in use and older than both:
`09-transport.md`'s "provides **8 UB** of capacity" and "Infantry: 1 UB" count
whole Unit Base *volumes*, disambiguated by the words "capacity" and "occupies"
rather than by `CORE-001`. Defining it is a `09-transport.md` question, this
change does not make it worse, and the new clause is scoped to *"a distance
written `N UB`"* precisely so that it claims nothing about capacity.

---

## Decision 3 — `INF-007` charges per obstacle, and `INF-009` stops restating it

`INF-007` and `INF-009` disagreed once the prose between them was removed.
`INF-007` said a climb costs "1 additional Action Point … for a total cost of
**2 AP**"; `INF-009` said each step of a stepped surface is charged separately.
A staircase of two 4-to-6 plate steps costs 3 AP by one and 2 AP by the other.

**`INF-007` is the rule that was wrong**, and it was wrong before the
compression — "2 AP in total" describes the ordinary case of one obstacle and
states it as if it were the only case. It now charges **1 additional Action Point
for each such obstacle the move crosses**. The single-obstacle move still costs
2 AP.

**The general rule already said this.** `MOVE-013` reads *"Each step is an
obstacle in its own right, read individually."* Charging per obstacle makes
`INF-007` agree with the rule it implements rather than diverge from it, which is
the argument for the change and not merely a consequence of it.

`INF-009`'s "Each step is charged separately" then restates `INF-007` and goes.

**Rejected: restoring `INF-009`'s reconciling paragraph.** It existed to explain
that `INF-007` did not mean what it said. Fixing `INF-007` deletes the need for
the explanation, and leaves a reader able to apply `INF-007` alone.

**Rejected: making `INF-009` cap a climb at 2 AP.** A three-step staircase would
then cost less than the three separate obstacles it is built from, and a player
could split one into three moves to make it cost more.

**Accepted, not overlooked: a move crossing three such obstacles costs 4 AP and
cannot be made.** `CORE-006` gives a unit 3 Action Points, and that is the bound
— no rule caps the climb, because the model already does
(`system/proposal-review.md`, "Do Not Cap What the Model Already Bounds").

---

## Decision 4 — `INF-010` is retired, and `INF-008` is left as it stands

`INF-010` said a vertical face taller than `INF-008`'s threshold cannot be
climbed unless a slope, stair or ramp reaches it. `INF-008` says a face of 7 or
more plate layers cannot be climbed directly, lists slopes, stairs and ramps, and
closes "Without one of these, the obstacle is impassable." The second rule
restates the first four rules later, which is what
`2026-08-18-infantry-is-a-first-class-domain` (Decision 14) recorded and left.

The number is retired, never reissued, and no stub is left
(`system/documentation-standards.md`, Naming Conventions). The two documents
citing `INF-008, INF-010` as a pair now cite `INF-008`.

**`INF-010`'s closing clause — "and no other construction grants access" — is
not moved into `INF-008`.** It would convert `INF-008`'s "Examples:" heading into
a closed set of three, and that is a rule decision about what terrain can be
built, not a consequence of deleting a duplicate. `MOVE-014`, `MOVE-019`,
`CMP-018` and `VEH-026` all reach `INF-008` for this question and all read it as
it now stands, which is how they read it before `INF-010` existed.

**Recorded as still owed**, and unchanged in difficulty by this change: decide
whether slopes, stairs and ramps are examples or the whole list. **It cannot go
in `TODO.md`** — that file takes only gaps the ruleset declares in its own text
and quotes verbatim, and `INF-008`'s "Examples:" declares nothing. It lives here,
and in the issue tracker if someone decides to do it (`TODO.md`, preamble).

**Rejected: keeping `INF-010` until that question is settled.** Two rules stating
one threshold is worse than one rule stating it ambiguously, and the ambiguity
lives in `INF-008`'s heading either way.

---

## Decision 5 — The delta lands as a new `infantry-movement` capability

`openspec/specs/` has seven capabilities and none of them is infantry.

- **`unit-base` owns the measurement, not the domain.** Its living spec already
  says every distance is expressed in Unit Bases; what infantry's distances *are*
  is a domain rule. It also carries an unarchived `MODIFIED` delta from #130
  against its *Unit Base Projections* requirement, and a second delta against the
  same requirement is the case `system/workflow.md` ("When several changes
  modified the same requirement") exists to resolve — one delta is authoritative
  and the other moves to `specs-superseded/`. Avoiding the collision is cheaper
  than resolving it.
- **`action-economy` owns "every unit gets 3 AP" and nothing else.** What a
  movement action costs belongs with the movement rules, and splitting the climb
  cost from the distance it belongs to puts two halves of one rule in two
  capabilities.

`infantry-movement` is therefore `ADDED` in full: the distances and their axes,
the per-obstacle climb, and the Wounded limit.

**No delta is written for `CBT-014`.** No capability covers it — it stated no
rule, which is why it is retired.

---

## Decision 6 — Nothing in `docs/` names a mechanic that does not exist

Deleting `INF-002`'s sprinting note made infantry the only document held to that
standard. Four passages elsewhere did the same thing:
`FLOW-013`'s sprinting bullet, `VEH-011`'s "Future rules may introduce lateral
movement", `CORE-005`'s "Structure-wide effects … are not currently defined", and
**`CBT-014 — Future Combat Extensions`**, a whole rule listing seven mechanics
StudCraft does not have.

All four go. #130 established the precedent when it retired `WPN-017 — Future
Weapon Types` as *"a list of things that do not exist"*; `CBT-014` is the same
rule with a different prefix, and survived that pass only because the pass was
editorial.

**What a scenario may add is not lost.** `FLOW-013` closes with it — *"They may
restrict or extend the ruleset for that game but may not contradict Foundations
or Core Rules"* — and the deleted bullet was an example of that sentence whose
example does not exist.

**`CODE_OF_DESIGN.md` cited `CBT-014`, and no gate could see it.** Principle 9
closed by deferring *"whether that produces a shot outside a unit's own
activation"* to it, and `CBT-014` did answer: *Overwatch* and *Reaction Fire*
were on its list. `scripts/rule.py refs` reports the rule is cited by nothing —
it reads an index built from `docs/` — and `scripts/lint_ruleset.py` reads
`docs/` and `assets/IMAGES.md` only, so preflight was green with a retired ID in
the charter. `system/proposal-review.md` names this failure class first, and a
repository-wide grep is now task 9.4.

**The clause is deleted, not repointed.** Repointing moves the rot to the next
retired ID; `.claude/rules/repository-prose.md` says a deletion is a valid edit
on its own.

**What `CBT-014` answered is not asserted somewhere else — it is recorded as
open.** Three archived changes routed the reaction-fire question to that rule on
purpose: `2026-08-01-full-audit-repairs` rejected building reaction fire because
*"`CBT-014` already correctly flags Reaction Fire as a possible future
extension"*; `2026-08-18-core-states-only-what-it-owns` refused to write an
absolute prohibition into `CORE-009`, because *"an absolute prohibition here
would outrank"* `FLOW-013`'s scenario-extension power; and
`2026-08-19-core-stops-describing-units` decided `CBT-014` should stand uncited
and re-aimed Principle 9 at it in the same commit.

**None of those decisions is reversed here, and none is silently kept either.**
Inferring "an attack happens in the attacker's activation and nowhere else" from
`CBT-001` and `CORE-006` is exactly the absolute form the 2026-08-18 change
declined to write, and a proposal is not the place to state a rule. So the
question goes to `TODO.md` (section 12), quoting `CORE-009` — which survives,
and which is the sentence left reading unqualified once `CBT-014` is gone.

**The entry widens `TODO.md`'s criterion slightly**, and deliberately:
`CORE-009` does not say of itself that something is undefined, it reads
ambiguously without the rule that used to qualify it. Recording that is better
than losing it, and `TODO.md` is repository prose whose criterion is its own to
adjust.

**`TODO.md` loses two entries, gains one and keeps its fourth.** Two quoted
sentences these edits delete; the `CBT-014` entry is replaced by the `CORE-009`
one above; the fourth quotes `VEH-006`, which this change does not touch and
which still reads exactly as quoted.

**The standard this decision sets applies to `docs/` and stops there.**
`system/workflow.md` draws that line already — `docs/*.md` is the ruleset and
goes through a proposal, everything else is the repository. `TODO.md` is
repository prose, its criterion is its own, and whether a scenario power belongs
in a file of declared gaps is a question that predates this change. Reaching
into it would be scope this change has no claim on.

**Rejected: emptying `TODO.md` and deleting it with its gate.** Considered,
because `docs/` will not declare a gap in its own text again and the file's
supply is therefore dry. Two reasons against, and the first is enough:
`scripts/check_todo_quotes.py` **returns 1 on a file with no blockquotes**, so an
emptied `TODO.md` turns a required check red — and removing the check means
`scripts/`, its tests, `.github/workflows/` and three `system/` documents, on a
branch carrying a ruleset proposal. The file keeps one entry and the gate stays
green.

`system/repository-strategy.md` (Branch Naming) allows a ruleset branch to carry
a non-`docs/` file when `design.md` names which and why. **The two are `TODO.md`
and `CODE_OF_DESIGN.md`**, and this is that naming.

**Rejected: moving the four passages into `TODO.md` instead of deleting them.**
`TODO.md` records gaps *the ruleset declares in its own text*. Once the text
stops declaring them there is nothing to quote, and an entry quoting a deleted
sentence is what `check_todo_quotes.py` exists to catch.

**Rejected: retiring `CBT-014` in a separate proposal.** The four passages are
one standard, and applying it to infantry alone is what made this decision
necessary. Splitting it leaves three documents contradicting the fourth.

---

## Decision 7 — Movement and range are now in different units, and that is temporary

`system/proposal-review.md` warns about exactly this pairing — *"especially
movement against range"*. Before this change a player compared an infantry move
to a weapon reaching 12 studs (`10-weapons.md`) or a Bike moving 18 studs
(`08-vehicles.md`) directly. After it, they convert, and the factor differs by
axis: ×3 forward, ×4 sideways.

**Accepted, with the cost paid in two places.** Every changed rule carries its
stud figure in the same clause that names its axis, and the Summary items state
both. So the conversion is never something a player computes; it is printed
beside the rule.

**The end state is that vehicles and weapons convert too**, which the unit-base
spec already requires and neither document does. Named in Out of Scope rather
than attempted here: a vehicle's movement is three times its own length, which
is not a Unit Base axis, and turning it into one is a rule change in a domain
this proposal does not touch.

**Rejected: converting all three documents here.** That is a change to every
distance in the ruleset on a branch named for infantry, and the vehicle
conversion is the hard one.

---

## Decision 8 — The change keeps a name that no longer covers it

`fix-infantry` names the directory, the branch and most of the work. Part C does
not fit it: a rule retired in `11-combat.md`, four passages cut across three more
documents, `TODO.md` emptied and a clause removed from `CODE_OF_DESIGN.md`.

**The name cannot change.** `openspec/config.yaml` requires one dedicated branch
per proposal and `system/repository-strategy.md` (Branch Naming) makes the
matching name the only mechanical check of that — the directory and the branch
are compared exactly. Renaming means a new branch and a new directory, and this
one already carries the work.

**Where a reader will look, and what they will find.** `proposal.md`'s title
covers infantry only, so the `CBT-014` retirement is findable three ways and not
by the change's name: the `**Bump:**`-free commit subject on `main`, the release
`CHANGELOG.md` entry, and `openspec/changes/archive/` once this is archived.
`proposal.md` states the mismatch in its Why so that a reader who arrives at the
directory is not surprised by half its contents.

**Rejected: splitting Part C into its own change.** Considered and decided
against by the maintainer. The four passages are one standard, and the
`INF-002` deletion in Part A is what made the standard uneven — splitting ships
a ruleset where infantry is held to a rule the other four documents are not.

**Rejected: retitling `proposal.md` to something the directory does not say.** A
title that disagreed with its own directory name would be the second name to
check rather than a clearer first one.
