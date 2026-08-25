# Tasks — Infantry states its distances in Unit Bases

## How to read this file

**Part A is already applied.** It was applied by hand, on this branch, before
this proposal existed (`design.md`, Decision 1). Its boxes are checked because
the work is in the tree, not because a task was followed. Each entry names what
to verify, so a reviewer can check the claim rather than take it.

**Part B is owed**, and so is **Part C**. Both are written as anchor pairs so
`scripts/apply_tasks.py` performs the replacement rather than a model retyping
it. Every anchor is an exact substring occurring **exactly once** in the file
its task names.

If an anchor returns anything other than 1, **stop and report it** rather than
guessing which occurrence was meant. Never edit a document to make a
verification command pass — report the mismatch instead.

### How to read the replacement blocks

The triple-backtick fence marks where the text starts and stops. **The fence is
not part of the text** — do not write the backticks into the document.

### Order matters

Edits apply in the order below, each against the result of the ones above it.
Most of Part B edits `docs/17-infantry.md`; Part C edits six other files.

### What Part B must not do

**Part B repairs; it does not decide.** It fixes what the hand edit broke — an
abbreviation the ruleset does not use, a citation pointing back at the rule that
cited it, a Summary contradicting the rules above it.

**Section 4 is Part B's one rule change.** `INF-007` charges per obstacle
instead of a flat 2 AP; the maintainer decided it and `design.md` (Decision 3)
records the reasoning.

**Four tasks add prose, and each adds a rule rather than its justification.**
Task 2.1 puts back the measurement point `INF-002` stopped stating, task 3.1
puts back `INF-004`'s Action Point cost, task 5.1 puts back the clause saying an
unclimbable step stops the climb there, and section 1b states what a distance
written `N UB` means, in the three documents that own the term.

**Nothing else in Part B may remove a rule, change a distance or a cost, or add
a mechanic.** Numbers on the page do change — "multiples of 3" becomes "4 UB" —
and every one of those is the same distance written in a different unit.
If a Part B replacement block would, it is wrong — stop and report it.

### What Part C does, which Part B may not

**Part C deliberately deletes rules text, and one whole rule.** Sections 8
through 12 remove four passages naming mechanics the ruleset does not define,
retire `CBT-014`, and cut the `TODO.md` entries and the `CODE_OF_DESIGN.md`
clause that read them. `design.md` (Decision 6) decides all of it.

That is the only place in this file where a replacement block may make a rule
disappear. **A Part C task still applies exactly as written and nothing more**
— if a section's anchor does not match, stop and report it rather than
searching for the rule elsewhere.

---

# Part A — Applied

## A1. `docs/17-infantry.md` — prose compressed

- [x] `INF-002`, `INF-003`, `INF-004`, `INF-007` and `INF-009` state their rule
      and stop (`system/documentation-standards.md`, "How a Rule Is Written").
      The derivation paragraphs, the worked example under `INF-003`, the
      sprinting note under `INF-002` and `INF-009`'s reconciling paragraph are
      gone.
- [x] `INF-009`'s three thresholds are a bulleted list rather than a sentence
      naming all three.
- [x] Verify no rule was lost with the words:
      `python3 scripts/rule.py doc 17-infantry.md`.

## A2. `docs/17-infantry.md` — distances restated as a count of Unit Bases

- [x] `INF-002` and `INF-004`: up to 4 across the base's depth. `INF-003`: up to
      3 across its width. Twelve studs in every case, unchanged from `main`.
- [x] `INF-007`'s statement of the limit follows the same count.

**The applied text spells the unit `BU`.** The ruleset's abbreviation is `UB`
(`02-core-rules.md`, CORE-001), and nothing in the ruleset is called a `BU`.
Part B, section 1 corrects it — this A-item records what is in the tree, not
what is right.

## A3. `INF-010` retired

- [x] The rule is deleted from `docs/17-infantry.md`. Its number is retired,
      never reissued, and no stub is left
      (`system/documentation-standards.md`, Naming Conventions).
- [x] `docs/07-movement.md` (`MOVE-014`) and `docs/08-vehicles.md` (`VEH-026`)
      cite `INF-008` alone where they cited the pair.
- [x] Verify no citation survives it: `grep -rn "INF-010" docs/` returns
      nothing.
- [x] Verify the gap is the only one:
      `python3 scripts/rule.py doc 17-infantry.md` lists `INF-001` … `INF-009`,
      `INF-011`, `INF-012`.

## A4. Nothing outside `docs/` changed

- [x] `assets/IMAGES.md` has no `INF-010` row and no row quoting a distance in
      studs. Verify: `grep -n "INF-0" assets/IMAGES.md`.
- [x] `TODO.md` quotes no sentence this change edits. Verify:
      `python3 scripts/check_todo_quotes.py`.

---

# Part B — Owed

Every item came from a read-only audit of the applied text
(`system/proposal-review.md`, "Review the Applied Text, Not Only the Diff").
Sections 1b and 7 are blockers.

## 1. `docs/17-infantry.md` — the unit is `UB`, and each rule states its axis

`BU` appears in seven lines of one document and nowhere else in the repository.
The abbreviation is **`UB`**, defined by `CORE-001`, carried by a glossary
entry, and used by `01-foundations.md`, `06-deployment.md`, `08-vehicles.md`,
`09-transport.md` and `10-weapons.md`.

The axis clause goes back in with it. `CORE-001` requires it — *"Each rule
states which dimensions of the Unit Base it reads"* — and without it `4 UB`
forward and `3 UB` sideways read as different distances when both are twelve
studs (`design.md`, Decision 2).

- [x] 1.1 In `docs/17-infantry.md`, `INF-002`, replace this anchor — the two
      lines stating the limit:

```
**Up to 4 BU forward, in whole BU steps.**

A unit may move 1, 2, 3 or 4 BU, or stay put.
```

with:

```
**Up to 4 UB forward, in whole UB steps.**

A unit may move 1, 2, 3 or 4 UB, or stay put.

Forward movement reads the Unit Base's 3-stud depth (`02-core-rules.md`, CORE-001), so 4 UB is 12 studs.
```

- [x] 1.2 In `docs/17-infantry.md`, `INF-002`, replace this anchor — the
      independence sentence:

```
Each movement action is measured independently: spending two Action Points on movement allows two separate moves of up to 4 BU each, not one move of 8 BU.
```

with:

```
Each movement action is measured independently: spending two Action Points on movement allows two separate moves of up to 4 UB each, not one move of 8 UB.
```

- [x] 1.3 In `docs/17-infantry.md`, `INF-003`, replace this anchor — the two
      lines stating the limit:

```
**Up to 3 BU sideways, in whole BU steps.**

A unit may move 1, 2 or 3 BU sideways, or stay put.
```

with:

```
**Up to 3 UB sideways, in whole UB steps.**

A unit may move 1, 2 or 3 UB sideways, or stay put.

Side movement reads the Unit Base's 4-stud width (`02-core-rules.md`, CORE-001), so 3 UB is 12 studs.
```

- [x] 1.4 In `docs/17-infantry.md`, `INF-007`, replace this anchor — the clause
      naming the limit:

```
the full move still counts against the unit's normal limit of **4 BU** (INF-002)
```

with:

```
the full move still counts against the unit's normal limit of **4 UB** (INF-002)
```

- [x] 1.5 Verify the abbreviation is gone: `grep -rn "\bBU\b" docs/` returns
      nothing.

## 1b. `docs/02-core-rules.md`, `docs/14-glossary.md`, `docs/01-foundations.md` — what a distance written in `UB` means — BLOCKER

**`UB` already means a volume.** `CORE-001` defines the Unit Base as
`4 × 3 × 13` plate layers, and every bare `N UB` in the ruleset today counts
volumes — "Infantry occupies 1 UB" (`01-foundations.md`), "provides **8 UB** of
capacity" (`09-transport.md`), "Infantry: 1 UB" (`09-transport.md`). The one
written form `CORE-001` gives for counting them is two-dimensional: *"A
footprint written `W × D UB` counts 4-stud widths by 3-stud depths."*

Section 1 introduces a third reading — a **length along one named axis**. A
reader arriving from `09-transport.md` reads "up to 4 UB forward" as four
volumes, and nothing in `CORE-001` or the glossary tells them otherwise. The
per-rule axis clauses fix it inside `17-infantry.md` and nowhere else.

**The owner of the term states the reading.** That is `CORE-001`
(`system/documentation-standards.md`, "What `system/` Is For" — one owner, a
pointer everywhere else), with the glossary entry matching it and
`01-foundations.md`'s list of what UB measures gaining the use it now has.

- [x] 1b.1 In `docs/02-core-rules.md`, `CORE-001`, replace this anchor — the
      footprint line:

```
A footprint written `W × D UB` counts 4-stud widths by 3-stud depths, so a `2 × 3 UB` footprint measures `8 × 9` studs.
```

with:

```
A footprint written `W × D UB` counts 4-stud widths by 3-stud depths, so a `2 × 3 UB` footprint measures `8 × 9` studs.

A distance written `N UB` counts N Unit Bases along the single axis its rule names: 4 UB of depth is 12 studs, 3 UB of width is 12 studs (`17-infantry.md`, INF-002, INF-003).
```

- [x] 1b.2 In `docs/14-glossary.md`, replace this anchor — the *UB* entry's
      body:

```
The universal measurement of StudCraft: a volume 4 studs wide, 3 studs deep and 13 plate layers tall. See `02-core-rules.md` (CORE-001).
```

with:

```
The universal measurement of StudCraft: a volume 4 studs wide, 3 studs deep and 13 plate layers tall. A footprint written `W × D UB` counts widths by depths; a distance written `N UB` counts N Unit Bases along the axis its rule names. See `02-core-rules.md` (CORE-001).
```

- [x] 1b.3 In `docs/01-foundations.md`, replace this anchor — the last bullet of
      the *Examples* list:

```
- Cargo occupies UB, and several objects may share one (`09-transport.md`, TRN-013).
```

with:

```
- Cargo occupies UB, and several objects may share one (`09-transport.md`, TRN-013).
- Infantry movement is measured in UB, along a named axis of the base (`17-infantry.md`, INF-002).
```

## 2. `docs/17-infantry.md` — `INF-002` does not own its measurement point

`MOVE-003` names the point and then hands it off — *"Where that point is, is its
own domain's rule — infantry measures from the face of its base that leads in
the direction of travel (`17-infantry.md`, INF-002), a vehicle from its front
along its facing (`08-vehicles.md`, VEH-004)."* The compressed `INF-002` hands
it straight back: "measured according to the general movement measurement rule
(`07-movement.md`, MOVE-003)".

**A reader is not stranded** — `MOVE-003` answers before it delegates — but the
pair reads as a loop, and the domain rule states nothing about its own domain.
`INF-002` takes the answer, and `MOVE-003` keeps only the handoff it was already
making. That leaves the rule stated once, in the document that owns it
(`system/proposal-review.md`, "the same rule asserted twice in two documents").

- [x] 2.1 In `docs/17-infantry.md`, `INF-002`, replace this anchor — the whole
      line:

```
Distance is measured according to the general movement measurement rule (`07-movement.md`, MOVE-003).
```

with:

```
Distance is measured from the face of the base that leads in the direction of travel — the front face moving forward, the rear face moving backward (INF-004), the corresponding side face moving sideways (INF-003). This is the general measurement rule (`07-movement.md`, MOVE-003) read against an infantry base.
```

- [x] 2.2 In `docs/07-movement.md`, `MOVE-003`, replace this anchor — the whole
      handoff line. Both domain rules state their own point after task 2.1:
      `INF-002` states the leading face, and `VEH-004` already read *"Measure
      from the vehicle's front along its facing."* The handoff takes the form
      `MOVE-012`, `MOVE-013` and `MOVE-014` already use:

```
Where that point is, is its own domain's rule — infantry measures from the face of its base that leads in the direction of travel (`17-infantry.md`, INF-002), a vehicle from its front along its facing (`08-vehicles.md`, VEH-004).
```

with:

```
Where that point is, is its own domain's rule — infantry (`17-infantry.md`, INF-002), vehicles (`08-vehicles.md`, VEH-004).
```

- [x] 2.3 Read `MOVE-003`, `INF-002` and `VEH-004` end to end afterwards, in
      that order, and confirm each states its own measurement point exactly once
      (`system/proposal-review.md`).

## 3. `docs/17-infantry.md` — `INF-004` lost its Action Point cost

The compression replaced *"Backward movement is a movement action and costs 1
Action Point"* with a sentence inheriting `INF-002`'s **movement limit and step
size**, which is not its cost. `INF-003` states its own cost; after this edit
`INF-004` states none, and neither does anything it cites.

- [x] 3.1 In `docs/17-infantry.md`, `INF-004`, replace this anchor — the limit
      line and the sentence under it:

```
**Up to 4 BU backward, in whole BU steps.**

Backward movement uses the same movement limit and step size as forward movement (INF-002).
```

with:

```
**Up to 4 UB backward, in whole UB steps.**

Backward movement reads the same 3-stud axis and the same limit as forward movement, and costs **1 Action Point** (INF-002).
```

## 4. `docs/17-infantry.md` — `INF-007` charges per obstacle

**A rule change, not a repair** (`design.md`, Decision 3). `INF-007` states
"a total cost of **2 AP**" absolutely; `INF-009` charges each step of a stepped
surface separately, which makes a two-step staircase 3 AP. The paragraph that
had reconciled them was prose and section A1 removed it.

`INF-007` charges per obstacle crossed. The one-obstacle move still costs 2 AP.

- [x] 4.1 In `docs/17-infantry.md`, `INF-007`, replace this anchor — the whole
      line:

```
Infantry may climb. Climbing costs **1 additional Action Point** on top of the movement action that crosses the obstacle, for a total cost of **2 AP**.
```

with:

```
Infantry may climb. Climbing costs **1 additional Action Point** for each such obstacle the move crosses, on top of the movement action itself — so a move over one such obstacle costs **2 AP**.
```

## 4b. `docs/17-infantry.md` — the three obstacle rules gloss inconsistently

Section A1 removed `INF-007`'s "(more than one brick, up to two)" and left
`INF-006`'s "(one brick or less)" and `INF-008`'s "(taller than two bricks)".
**The two survivors go rather than the third coming back**: `INF-006` states the
conversion outright in its next line — *"a plate counts as 1 and a standard
brick as 3"* — so each gloss restates arithmetic the reader was just given.

- [x] 4b.1 In `docs/17-infantry.md`, `INF-006`, replace this anchor — the whole
      line:

```
Height: **up to 3 plate layers** (one brick or less).
```

with:

```
Height: **up to 3 plate layers**.
```

- [x] 4b.2 In `docs/17-infantry.md`, `INF-008`, replace this anchor — the whole
      line:

```
Height: **7 or more plate layers** (taller than two bricks).
```

with:

```
Height: **7 or more plate layers**.
```

## 5. `docs/17-infantry.md` — `INF-009` lost a rule and gained a restatement

Two defects in one paragraph:

**A rule went with the prose.** `main` read "7 or more not climbable at all
(INF-008), **which stops the climb at that step**". The compressed bullet says
only "cannot be climbed". A player whose staircase has a 7-plate third step now
has no stated outcome — does the move stop below it, or is the whole staircase
impassable? That is a rule, and section A1 claims to have removed justification
only.

**"Each step is charged separately" restates `INF-007`** once task 4.1 lands,
and "Distance traveled up either" points at a slope and a stepped surface named
four lines and a bulleted list away.

- [x] 5.1 In `docs/17-infantry.md`, `INF-009`, replace this anchor — the last
      bullet and the two lines after it:

```
- 7 or more plate layers: cannot be climbed (INF-008).

Each step is charged separately.

Distance traveled up either counts against the normal movement limit (INF-002).
```

with:

```
- 7 or more plate layers: cannot be climbed (INF-008), which stops the climb at that step.

Distance traveled up a slope or a stepped surface counts against the normal movement limit (INF-002).
```

## 6. `docs/17-infantry.md` — `INF-012` is still written in studs

Two unit systems in one document, and `INF-012` is the rule a player reaches for
under pressure. Its third paragraph argues against taking half of a legal
distance, using a stud figure the rules above no longer state.

- [x] 6.1 In `docs/17-infantry.md`, `INF-012`, replace this anchor — the first
      two paragraphs of the rule body:

```
A Wounded infantry model (`16-damage-system.md`, DMG-002) moves **at most two steps** in whichever direction it travels.

The step is the one that direction already uses (`02-core-rules.md`, CORE-001): the Unit Base's 3-stud depth forward and backward (INF-002, INF-004), and its 4-stud width sideways (INF-003). So a Wounded model may move **up to 6 studs forward or backward** and **up to 8 studs sideways** — distances those rules already allow, with the longer ones removed.
```

with:

```
A Wounded infantry model (`16-damage-system.md`, DMG-002) moves **at most 2 UB** in whichever direction it travels.

Each direction reads its own axis of the Unit Base (`02-core-rules.md`, CORE-001), so 2 UB is **6 studs forward or backward** (INF-002, INF-004) and **8 studs sideways** (INF-003) — distances those rules already allow, with the longer ones removed.
```

- [x] 6.2 In `docs/17-infantry.md`, `INF-012`, replace this anchor — the whole
      paragraph:

```
The limit is counted in steps rather than taken as half the normal distance because half of a side move is 6 studs, which INF-003 does not allow. A fraction of a legal distance is not always a legal distance; a count of steps always is.
```

with:

```
The limit is counted in whole Unit Bases rather than taken as half the normal distance, because half of a 3 UB side move is not a whole Unit Base.
```

## 6b. `docs/14-glossary.md` — *Step* points at a rule that no longer uses the word

Task 6.1 leaves `INF-012` reading "at most **2 UB**", with the word "step"
nowhere in it, and task 6.2 removes the fraction argument. The glossary entry
cites `INF-012` for both.

**The term survives** — `INF-002`, `INF-003` and `INF-004` all say "in whole UB
steps" — so the entry is retargeted rather than deleted.
`system/proposal-review.md`: *"Any change touching a rule checks that document's
Summary and its glossary entry in the same pass."*

- [x] 6b.1 In `docs/14-glossary.md`, replace this anchor — the *Step* entry's
      body:

```
An infantry movement increment: one Unit Base depth (3 studs) moving forward or backward, one Unit Base width (4 studs) moving sideways. Used to state a Wounded model's shorter limit as a count rather than a fraction, because half of a legal distance is not always a legal distance. See `17-infantry.md` (INF-012). Not to be confused with a stair's step (INF-009) or with a Component State advancing one step (`16-damage-system.md`, DMG-002).
```

with:

```
An infantry movement increment of one Unit Base: its 3-stud depth moving forward or backward, its 4-stud width moving sideways. See `17-infantry.md` (INF-002, INF-003, INF-004). Not to be confused with a stair's step (INF-009) or with a Component State advancing one step (`16-damage-system.md`, DMG-002).
```

## 7. `docs/17-infantry.md` — the Summary contradicts the rules above it — BLOCKER

Items 2, 3 and 7 still state the distances the way `main` did. A Summary is the
last thing a player reads and the first thing they quote.

- [x] 7.1 In `docs/17-infantry.md`, replace this anchor — Summary items 2 and 3:

```
2. Forward and backward movement is up to 12 studs, in multiples of 3.
3. Side movement is up to 12 studs, in multiples of 4.
```

with:

```
2. Forward and backward movement is up to 4 UB, read across the Unit Base's 3-stud depth — 12 studs.
3. Side movement is up to 3 UB, read across its 4-stud width — 12 studs.
```

- [x] 7.2 In `docs/17-infantry.md`, replace this anchor — Summary item 7:

```
7. A Wounded model moves at most two steps in any direction — 6 studs forward or backward, 8 sideways.
```

with:

```
7. A Wounded model moves at most 2 UB in any direction — 6 studs forward or backward, 8 sideways.
```

- [x] 7.3 In `docs/17-infantry.md`, replace this anchor — Summary item 5, which
      states the climb cost the way `INF-007` did before task 4.1:

```
5. Obstacles up to 3 plate layers are crossed freely, 4 to 6 cost 1 additional Action Point, and 7 or more need a slope, a stair or a ramp — and a stair's own steps are obstacles read the same way.
```

with:

```
5. Obstacles up to 3 plate layers are crossed freely, 4 to 6 cost 1 additional Action Point each, and 7 or more need a slope, a stair or a ramp — and a stair's own steps are obstacles read the same way.
```

- [x] 7.4 Read the Summary against `INF-002`, `INF-003`, `INF-007`, `INF-009`
      and `INF-012` afterwards, not only the changed lines
      (`system/proposal-review.md`, "The Summary Is Part of the Rule").

# Part C — Nothing in `docs/` names a mechanic that does not exist

**Four passages, and they are rule changes rather than repairs.** The maintainer
decided all four; `design.md`, Decision 6 records the reasoning.

`INF-002`'s sprinting note was one of five places where the ruleset described
what it does not contain. Deleting one and leaving four states the standard for
infantry alone. #130 already retired `WPN-017 — Future Weapon Types` for exactly
this — *"a list of things that do not exist"* — and `CBT-014` is the same rule
with a different prefix.

`TODO.md` recorded three of these four passages as declared gaps, and section 12
removes those three entries. `scripts/check_todo_quotes.py` is a required check,
so `TODO.md` travels in the same commit.

## 8. `docs/03-game-flow.md` — `FLOW-013`'s sprinting bullet

`INF-002` said "Future scenarios may allow sprinting or other special
movement"; section A1 deleted it. The bullet in `FLOW-013` outlived it and names
a mechanic no rule defines.

**The scenario power is not lost.** `FLOW-013` closes with it: *"They may
restrict or extend the ruleset for that game but may not contradict Foundations
or Core Rules."* The bullet was an example of that sentence, and its example does
not exist.

**The bullet above it carries the same defect and is repaired in the same
anchor.** It cites `WPN-014` for *"limiting weapons fired in one activation"*,
and `WPN-014` now reads, in full: *"A unit carrying multiple weapons may use them
according to its available Action Points."* Its "Future scenarios may limit the
number of weapons fired during a single activation" was deleted by #130 — the
same pass Decision 6 cites as precedent. `VEH-006` and `CBT-007` both still say
"unless restricted by a scenario" and stay.

- [x] 8.1 In `docs/03-game-flow.md`, `FLOW-013`, replace this anchor — the
      restrictions bullet and the sprinting bullet together, which is how the
      sprinting bullet is deleted without leaving a blank line:

```
* Restrictions on otherwise-legal actions, such as limiting weapons fired in one activation (`10-weapons.md`, WPN-014), restricting reverse movement (`08-vehicles.md`, VEH-006), or restricting how a weapon system's Attack Dice are split (`11-combat.md`, CBT-007).
* Additional movement options such as sprinting (`17-infantry.md`, INF-002).
```

with:

```
* Restrictions on otherwise-legal actions, such as restricting reverse movement (`08-vehicles.md`, VEH-006) or restricting how a weapon system's Attack Dice are split (`11-combat.md`, CBT-007).
```

## 9. `docs/11-combat.md` — `CBT-014` is retired

*Future Combat Extensions* states no rule. It lists seven mechanics StudCraft
does not have and then constrains rules nobody has written.

**No rule in `docs/` cites it.** Two files outside `docs/` do:
`TODO.md` (section 12) and **`CODE_OF_DESIGN.md`**, whose Principle 9 defers a
question to it (task 9.3).

`python3 scripts/rule.py refs CBT-014` reports "cited by nothing" and **cannot
answer this question** — it reads the index, and the index is built from `docs/`.
`scripts/lint_ruleset.py` reads `docs/` and `assets/IMAGES.md` only, so preflight
stays green either way. This is the failure class `system/proposal-review.md`
names first: *"A retired rule ID still cited from outside `docs/` — grep the
whole repository before deleting a rule."* Task 9.4 is that grep.

Its number is retired, never reissued, and no stub is left
(`system/documentation-standards.md`, Naming Conventions). `CBT-015` keeps its
number.

- [x] 9.1 In `docs/11-combat.md`, replace this anchor — the whole rule, its
      trailing rule separator, and the heading of the rule after it. **The next
      heading is part of the anchor and must be written back:**

```
# CBT-014 — Future Combat Extensions

The following are **not currently part of StudCraft**:

* Suppression
* Blast Weapons
* Fire
* Smoke
* Explosions
* Overwatch
* Reaction Fire

Future combat rules must preserve the Impact-based combat system.

---

# CBT-015 — Attacking While Wounded
```

with:

```
# CBT-015 — Attacking While Wounded
```

- [x] 9.2 Verify the numbering: `python3 scripts/rule.py doc 11-combat.md`
      reports **13 rules** — `CBT-001` … `CBT-009`, `CBT-011` … `CBT-013`,
      `CBT-015`. **`CBT-010` was already retired before this change**, so two
      numbers are missing afterwards and that is correct.

### `CODE_OF_DESIGN.md` — Principle 9 defers a question to `CBT-014`

Principle 9 closes by handing one question to the rule this section retires.
`CBT-014` did answer it: *Overwatch* and *Reaction Fire* were on its list of
what StudCraft does not have.

**The answer survives the rule.** `CBT-001` charges an attack 1 Action Point,
and `CORE-006` says Action Points are *"everything a unit can do during its
activation"* — so an attack happens in the attacker's activation and nowhere
else. The clause deferred to a rule for something two live rules already settle.

**The clause is deleted rather than repointed.** Repointing moves the rot to the
next retired ID; `.claude/rules/repository-prose.md` says a deletion is a valid
edit on its own, and `design.md` (Decision 6) names `CODE_OF_DESIGN.md` as a
file this branch carries, which `system/repository-strategy.md` (Branch Naming)
requires.

- [x] 9.3 In `CODE_OF_DESIGN.md`, Principle 9, replace this anchor — the whole
      line:

```
Visibility is symmetric: what can see you can target you. Whether that produces a shot outside a unit's own activation is a rule, not a principle — `docs/11-combat.md` (CBT-014) decides it.
```

with:

```
Visibility is symmetric: what can see you can target you.
```

- [x] 9.4 Verify no tracked file outside this change's own history still names
      the retired rule:
      `git grep -n "CBT-014" -- . ':!openspec/changes/archive'` returns nothing
      until this change is committed, and only `openspec/changes/fix-infantry/`
      afterwards. **`git grep`, not `grep -r`** — a plain recursive grep also
      reads `.studcraft/index.json` and any `delete-me*` handover, both
      gitignored, and both of which name the rule until the index is rebuilt in
      task 13.2.
- [x] 9.5 Verify `docs/11-combat.md` names none of the retired mechanics:
      `grep -nic suppression docs/11-combat.md` returns `0`, and the same for
      `overwatch`, `blast` and `smoke`. **Do not grep `fire`** — "Line of Fire"
      and "firing" are ordinary combat words the document keeps.

## 10. `docs/08-vehicles.md` — `VEH-011`'s lateral movement line

One sentence promising a rule. The two sentences above it state what a hover
vehicle does, which is the rule.

- [x] 10.1 In `docs/08-vehicles.md`, `VEH-011`, replace this anchor — the turn
      sentence and the line after it:

```
They may turn 90° left or right for **1 Action Point**, pivoting around their centre.

Future rules may introduce lateral movement.
```

with:

```
They may turn 90° left or right for **1 Action Point**, pivoting around their centre.
```

## 11. `docs/02-core-rules.md` — `CORE-005`'s structure-wide line

`CORE-005` states what a structure is and whose rules cross it. Its last line
names two effects — collapse and breaching — that no rule resolves.

- [x] 11.1 In `docs/02-core-rules.md`, `CORE-005`, replace this anchor — the
      last bullet of the domain list and the line after it:

```
* Vehicles: `08-vehicles.md`

Structure-wide effects such as building collapse or breaching are not currently defined.
```

with:

```
* Vehicles: `08-vehicles.md`
```

## 12. `TODO.md` — the entries whose quotes are gone, and the one gap that opens

`TODO.md` records **gaps the ruleset declares in its own text**, quotes each one
verbatim, and `scripts/check_todo_quotes.py` enforces the quoting as a required
check. Sections 8 through 11 delete three of the four quoted sentences.

Two entries go outright. **The `CBT-014` entry is replaced rather than deleted**:
retiring that rule opens a real question — whether `CORE-009`'s *"If you can see
it, you can shoot it"* grants a shot outside the attacker's activation — and
`CORE-009` is a live rule this change does not touch, so the entry has something
verbatim to quote. `design.md`, Decision 6.

**`### Reverse movement restrictions` stays.** It quotes `VEH-006`, which this
change does not touch and which still reads exactly as quoted. Whether a
scenario power belongs in a file of declared gaps is a question that predates
this change and is answered by `TODO.md`'s own rules, not the ruleset's —
`system/workflow.md` scopes the standard Decision 6 applies to `docs/*.md`, and
`TODO.md` is repository prose (`.claude/rules/repository-prose.md`).

**Nothing here empties the file, and nothing here touches the gate.** One quote
survives, so `check_todo_quotes.py` has something to verify and stays green.

- [x] 12.1 In `TODO.md`, replace this anchor — the whole *Structures* section
      and the heading after it. **`## Vehicles` is part of the anchor and must
      be written back:**

```
## Structures

### Structure-wide damage

`CORE-005` (`docs/02-core-rules.md`):

> Structure-wide effects such as building collapse or breaching are not currently defined.

What would have to be decided: whether structures can suffer whole-structure effects such as collapse or breaching, and what rules resolve those effects.

---

## Vehicles
```

with:

```
## Vehicles
```

- [x] 12.2 In `TODO.md`, replace this anchor — the *Lateral movement* entry and
      the heading after it. **`### Reverse movement restrictions` is part of the
      anchor and must be written back:**

```
### Lateral movement for hover vehicles

`VEH-011` (`docs/08-vehicles.md`):

> Future rules may introduce lateral movement.

What would have to be decided: whether hover vehicles should gain a side-movement action distinct from their current forward, backward and turning movement, and at what AP cost.

### Reverse movement restrictions
```

with:

```
### Reverse movement restrictions
```

- [x] 12.3 In `TODO.md`, replace this anchor — the whole *Combat* entry. **The
      `## Combat` heading and the separators stay**; only the entry under it
      changes:

```
### Suppression, blast, fire, smoke, explosions, overwatch, reaction fire

`CBT-014` (`docs/11-combat.md`):

> Future combat rules must preserve the Impact-based combat system.

The same rule explicitly lists the following mechanics as not currently part of StudCraft:

* Suppression
* Blast Weapons
* Fire
* Smoke
* Explosions
* Overwatch
* Reaction Fire

What would have to be decided: mechanics for each of these effects that preserve the Impact-based combat system rather than introducing a parallel damage mechanic.
```

with:

```
### Whether visibility grants a shot outside a unit's activation

`CORE-009` (`docs/02-core-rules.md`):

> **If you can see it, you can shoot it.**

What would have to be decided: whether that sentence grants an attack outside the attacker's own activation. `CBT-001` charges an attack 1 Action Point and `CORE-006` spends Action Points inside an activation, but no rule states the consequence, and `FLOW-013` lets a scenario extend the ruleset.
```

- [x] 12.4 Verify: `python3 scripts/check_todo_quotes.py` exits 0, and
      `grep -c "^> " TODO.md` returns `2` — `VEH-006` and `CORE-009`.
- [x] 12.5 Read `TODO.md` end to end and confirm both surviving entries quote a
      rule that still exists.

---

# 13. Verify

- [x] 13.1 `python3 scripts/apply_tasks.py --check fix-infantry` reports every
      anchor matched exactly once before any of them is written.
- [x] 13.2 `python3 scripts/preflight.py` — every check green.
- [x] 13.3 `grep -rn "\bBU\b" docs/` returns nothing.
- [x] 13.4 `grep -rn "INF-010" docs/` returns nothing.
- [x] 13.5 `python3 scripts/rule.py show INF-002 INF-003 INF-004 INF-007 INF-009 INF-012`
      — every distance reads in `UB` and names its axis.
- [x] 13.6 `grep -rni future docs/` returns nothing. Repeat for `not yet`,
      `not currently` and `sprinting`. **One plain pattern per command** —
      `scripts/verify_tasks.py` refuses a command containing `|`
      (`system/delegating-to-agents.md`, "Commands That Do Not Interrupt").
- [ ] 13.7 Read `docs/17-infantry.md` end to end — not only the changed lines
      (`system/proposal-review.md`).
- [ ] 13.8 Read the other nine changed files in place, each around its edit:
      `CORE-001` and `CORE-005` (`docs/02-core-rules.md`), `FLOW-013`
      (`docs/03-game-flow.md`), `MOVE-003` (`docs/07-movement.md`), `VEH-011`
      (`docs/08-vehicles.md`), `CBT-013` through `CBT-015`
      (`docs/11-combat.md`), the *UB* and *Step* entries
      (`docs/14-glossary.md`), the *Unit Base (UB)* section
      (`docs/01-foundations.md`), Principle 9 (`CODE_OF_DESIGN.md`) and
      `TODO.md` end to end.

---

# Part D — What the applied text audited into

`ruleset-auditor` read the ruleset as it stands after Parts B and C
(`system/proposal-review.md`, "Review the Applied Text, Not Only the Diff").
One finding is a contradiction this change introduced; two are consequences of
it that cost one sentence each.

## 14. `docs/17-infantry.md` — `INF-007` names a limit that is wrong sideways — BLOCKER

`INF-007` applies to a climb in any direction and names one limit: **4 UB**.
That is the forward and backward limit. A sideways move is limited to **3 UB**
by `INF-003`, and because a Unit Base counts along the axis its rule names,
`4 UB` read sideways is 16 studs against `INF-003`'s 12.

**The change introduced it.** `main` read "12 studs (INF-002)", which was
correct on both axes because 4 × 3 and 3 × 4 are the same distance. Restating
the limits in `UB` ended that coincidence, and this line was carried over as if
it had not — `system/proposal-review.md`, "Multipliers Set Early Get Falsified
by Numbers Added Later".

- [x] 14.1 In `docs/17-infantry.md`, `INF-007`, replace this anchor — the clause
      naming the limit:

```
the full move still counts against the unit's normal limit of **4 UB** (INF-002), or the Wounded model's shorter limit (INF-012).
```

with:

```
the full move still counts against the limit its own direction sets — **4 UB** forward or backward (INF-002, INF-004), **3 UB** sideways (INF-003) — or the Wounded model's shorter limit (INF-012).
```

## 15. `docs/17-infantry.md` — the Design Philosophy does not say the count differs by axis

It says movement is derived from the Unit Base and names both axes, but never
that the two limits are the same distance written as different counts. A reader
who does not know that reads `4 UB` as the infantry limit — which is exactly the
mistake section 14 repairs.

- [x] 15.1 In `docs/17-infantry.md`, Design Philosophy, replace this anchor —
      the whole line:

```
This makes movement measurable directly from the model. A spare Unit Base can be used instead of a ruler.
```

with:

```
This makes movement measurable directly from the model. A spare Unit Base can be used instead of a ruler.

The count differs by axis because the axes do: 4 UB forward and 3 UB sideways are both 12 studs.
```

## 16. `CODE_OF_DESIGN.md` — Principle 9 quotes a rule and cites none

Task 9.3 removed Principle 9's only citation into `docs/` along with the clause
that carried it. The principle now quotes `CORE-009` word for word and names no
owner, against the convention the document states about itself: *"Where a
principle below mentions a specific value, it cites the rule in `docs/` that
owns it, and that rule is the authority."* Principles 7 and 8 both follow it.

- [x] 16.1 In `CODE_OF_DESIGN.md`, Principle 9, replace this anchor — the line
      introducing the quote:

```
The core rule is simple:
```

with:

```
The core rule is simple — `docs/02-core-rules.md` (CORE-009) states it, and is the authority:
```

## 17. Verify

- [x] 17.1 `python3 scripts/preflight.py` — every check green.
- [x] 17.2 Read `INF-002`, `INF-003`, `INF-004`, `INF-007` and `INF-012` in
      order and confirm no two of them give one move two maxima. Read: forward
      and backward 4 UB, sideways 3 UB, `INF-007` now defers to whichever the
      move's direction sets, `INF-012` halves the count on the axis the
      direction already uses. One maximum per move.
