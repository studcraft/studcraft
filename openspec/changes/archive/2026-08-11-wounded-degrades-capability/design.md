# Design — Wounded degrades capability

The ruleset already has a `Wounded` state. `DMG-005` has defined one since `component-damage-system`
was archived, and `CORE-012` spells out that it costs nothing. So this change does not add a state;
it gives the existing one a price, in the capability the wounded component provides and nowhere
else.

Most of the work is deciding what *not* to make it cost. The sections below record every option
weighed and rejected, so the rejected ones are not re-proposed later.

---

## Decision 1 — Wounded degrades the capability the component provides, and nothing else

The generic statement lives in `DMG-005`, which already owns the state machine. The numbers live
in the document that owns each capability: `07-movement.md` for infantry movement,
`08-vehicles.md` for a vehicle whose Pilot is Wounded, `11-combat.md` for Attack Dice.

This is Principle 10 applied literally. It is also the reason the change adds no new `DMG-` rule —
an earlier draft had a `DMG-020 — Wounded Effects` carrying all three degradations, which would
have put the infantry movement limit in the damage document and left `MOVE-004` unaware of its own
exception. `DMG-005` states that the list is closed and points three ways; each destination states
one number.

**The list being closed is load-bearing.** `DMG-005` names Resistance, Impact Strength, the Damage
Roll, Unit Base occupancy, footprint, transport capacity and Action Point costs as unchanged, so a
later rule that wants to read `Wounded` for something else has to say so, in the open, rather than
inheriting a general licence. The one thing a closed list must not do is close over a case it has
not answered — which is why Decision 8 exists.

## Decision 2 — Rejected: a defensive die for a Wounded component

The obvious symmetric move is to let a Wounded component defend better: `+1 die, take highest` on
the Damage Roll, on the theory that a hurt soldier is a cautious one. It is rejected for four
reasons:

- **It makes a Wounded component harder to destroy than an Operational one.** The Damage Roll
  (`DMG-015`) fails on 1, 2 or 3 — one chance in two. Two dice keeping the higher fail only when
  both fall in that range — one chance in four. Wounding an enemy would halve the rate at which you
  can finish them.
- **It contradicts text in five documents,** all of which state or count the two-failure path from
  Operational to Dead: `DMG-005` ("a second successful damaging impact will kill it"), `DMG-008`
  ("exactly two failed Damage Rolls"), `DMG-016`'s shotgun, `MOVE-016`'s falling dice ("two failed
  dice therefore take an Operational unit to Dead"), and Examples 1 to 4 of `16-damage-system.md`.
  Adopting it means editing all of them.
- **There is no "Defense Die" in StudCraft to add one to.** The defender rolls the Damage Roll,
  which `DMG-015` describes as the uncertainty of combat rather than as armour, and `CBT-013`
  spends a rule insisting that armour is Resistance and never a separate statistic. A defensive die
  is the statistic both rules were written to keep out.
- **Its intent is already served by the movement limit.** The reason to want it is to make a
  Wounded unit prefer cover and hold position. A model that can cross 6 studs instead of 12 already
  prefers to stay where it is; nothing further is needed to produce the behaviour.

## Decision 3 — Rejected: halving movement

`×0.5` produces an illegal distance on the side axis. `MOVE-005` allows 4, 8 and 12 studs sideways;
half of 12 is 6, which is not among them. The forward axis survives halving (12 → 6, a multiple of
3) and the side axis does not, so a single "half" rule would need a rounding clause on one axis and
not the other.

Vehicles fail it worse. `VEH-004` is `3 ×` the vehicle's own length, and half of three lengths is
one and a half — a 9-stud Jeep would move 13.5 studs. `system/proposal-review.md` has a section on
exactly this failure ("any multiplier against the granularity of the thing it multiplies"), and
`VEH-004` itself already says why its own multiplier is a whole number: *"Because the multiplier is
a whole number, every resulting distance is a whole number of studs; there is no half stud to
measure."*

So the reduction is expressed in **whole steps of the unit's own measure**, which is what every
movement rule in the ruleset already uses:

| | Operational | Wounded |
|---|---|---|
| Infantry forward / backward | up to 4 steps of 3 studs (12) | up to 2 steps (6) |
| Infantry sideways | up to 3 steps of 4 studs (12) | up to 2 steps (8) |
| Vehicle | 3 × its own length | 2 × its own length |

Two steps, or one length less. Nothing rounds, nothing halves, and every distance in the right-hand
column is a distance `MOVE-004`, `MOVE-005`, `MOVE-006` and `VEH-004` already produce.

Note that the infantry reduction is not a uniform fraction — two of four steps forward, two of
three sideways. That is deliberate. The alternative was one number per axis derived from a
fraction, and "at most two steps" is a single thing to remember at the table (Principle 14) while
the fraction is two numbers and a rounding rule.

## Decision 4 — Rejected: an Action Point penalty instead of a capacity reduction

Principle 8 keeps one economy and `CORE-006` gives every unit 3 AP. A Wounded model paying 2 AP per
move would spend its activation differently rather than move differently, and it would compound
with `MOVE-010`'s climb surcharge into a 3 AP move — an entire activation to cross one obstacle.
The capacity reduction leaves the economy alone and changes what the model can reach, which is the
thing being wounded is supposed to change.

## Decision 5 — Rejected: a unit-level Wounded state

`DMG-001` says combat never targets a unit, and no rule in the ruleset gives a unit a state. A
minifigure *is* a component, which is why `CORE-012` works at all; a vehicle is a collection of
them.

So every degradation here reads one component's state:

- infantry movement reads the minifigure's own state;
- vehicle movement reads the **Pilot's** state;
- Attack Dice read the **weapon's** state, except in the one case Decision 8 covers.

A unit-level state would have needed a rule for which component sets it and a second rule for the
cases where a component is degraded and the unit is not — the Jeep whose cannon is Wounded. With
no unit-level state, that case is simply the general rule.

## Decision 6 — The Pilot is the vehicle's movement component

`VEH-013` already makes the Pilot the single component a powered vehicle needs in order to move:
*"If the vehicle has no Pilot — none embarked, or the Pilot is Dead — the vehicle cannot move."*
Wounding it degrading movement is the middle term of a progression the rule already has two ends
of, which is Principle 12 rather than a new mechanic.

The alternative — reading wheels, tracks or hover assemblies — was rejected because `VEH-019`
mentions "locomotion damage" without any rule defining it, and because a vehicle has several
locomotion components and no rule for how their states combine. Defining that is a change about
vehicles; this one leaves it alone, says so in `VEH-031`, and records the gap in `TODO.md`.

`VEH-031`'s scope is Wounded only. A *destroyed* wheel or track still stops the vehicle under
`VEH-019` and `VEH-026`, and neither is touched here.

## Decision 7 — Attack degrades by rolling two dice and keeping the lower

Three candidates produce a less reliable weapon:

| Candidate | Chance of an Impact | Cost to the reader |
|---|---:|---|
| Roll two, read the lower | 1 in 4 | a new kind of roll; no new number |
| Threshold 5-6 for a Wounded weapon | 1 in 3 | a second threshold |
| Threshold 6 only for a Wounded weapon | 1 in 6 | a second threshold, and a harsh one |

The first is adopted. `CBT-005`'s 4-5-6 threshold is read by the Attack Roll, the Damage Roll and
`MOVE-016`'s falling dice, and it is the only die-reading rule a new player has to learn. Either
threshold variant makes that sentence conditional everywhere it appears, for one rule's benefit.
Rolling a pair adds no number at all — only an instruction about which of two dice to read.

The 5-6 variant is the closest call of the three: it stays inside the existing "roll a die, compare
it to a number" idiom, and it is the gentlest. It was rejected because a player must then remember
*which* threshold applies to *which* die in an attack that mixes an Operational and a Wounded
weapon system, where the pair-of-dice form makes the distinction physical — you can see which die
has a partner.

The cost of the adopted form is honest and worth stating: `CBT-015` is the only place in the
ruleset where the number of physical dice rolled differs from the number of dice read. The rule
spends a bold paragraph on it, because `WPN-006` and `DMG-010` tie one Attack Die to one muzzle and
one muzzle to one Impact, and an extra *die* must be visibly not an extra *Impact*.

## Decision 8 — An unarmed attack reads the minifigure's own state

`MEL-008` lets a unit attack with its bare hands and calls that "its own weapon system". There the
attacker and the weapon are the same component, so "read the weapon's state" and "read the
attacker's state" stop being different instructions.

`CBT-015` states the answer rather than leaving it to be derived: a Wounded minifigure punches with
the degraded pair of dice. The alternative — exempting unarmed attacks — would have meant a Wounded
soldier is worse with a Wounded rifle than with no rifle at all in some rolls, and `DMG-005`
declares its list of degradations closed, which makes an unanswered case inside it worse than one
outside it.

`CORE-012` says the same thing from the infantry side, by pointing at `MEL-008` and `CBT-015`
rather than restating either.

**The answer has to be worded into every enumeration, not only into `CBT-015`.** The degradation is
"how each Attack Die is read when the component providing the attack is Wounded" — never "a Wounded
weapon" — in `DMG-005`, `DMG-011`, the glossary entry, `11-combat.md`'s Summary and both spec
deltas. An earlier draft answered the case in `CBT-015` and left the other six places scoped to
weapons, which put an unarmed attack outside a list `DMG-005` declares closed and left
`damage-resolution`'s unqualified "the attacker SHALL roll one D6" governing the punch.

## Decision 9 — Where the new rule IDs go, and why they look out of place

`scripts/lint_ruleset.py` requires rule IDs to be strictly increasing within a document, and
`system/documentation-standards.md` requires them to be stable. Together those two force a new rule
to the end of its document's rule list, whatever the reader would prefer:

- `MOVE-021` lands after `MOVE-020` (Interactive Terrain), below the terrain and falling sections.
- `VEH-031` lands after `VEH-030`, below the height rules.
- `CBT-015` lands after `CBT-014` (Future Combat Extensions) — a real rule following the list of
  rules that do not exist yet.

The last one is genuinely awkward and was still chosen over the alternatives, which were to
renumber (forbidden) or to put a combat-resolution rule in `10-weapons.md` (wrong owner —
`CBT-005` reads the die, `WPN-006` only counts it). The pointers of Decision 10 are what make the
placement survivable: a reader meets the pointer where they are already reading, and follows it.

## Decision 10 — Pointers, not restatements

Six rules get a one-clause pointer and none gets a copy of the mechanic: `MOVE-004` and `MOVE-005`
→ `MOVE-021`, `VEH-004` → `VEH-031`, `WPN-006`, `MEL-003` and `MEL-008` → `CBT-015`.

`MEL-008` gets its own pointer rather than inheriting `MEL-003`'s, even though both live in
`12-melee.md`: `MEL-008` is the rule that *creates* the case Decision 8 answers, and `MEL-003`'s
pointer sits fifty-nine lines above it.

`CORE-012` follows the same policy, which is why its replacement text does not repeat "6 studs
forward, 8 sideways". An earlier draft did, and it would have put `MOVE-021`'s numbers in a second
document with nothing tying the two together — `system/proposal-review.md` records "same rule
asserted twice, independently" as a failure class this repository has spent several changes
removing.

`CBT-004` deliberately gets nothing: it sits eleven rules above `CBT-015` in the same document, and
a pointer inside the document that contains the rule is the case where the copy is least justified.
`DMG-011` is not an exception to this either — it gets a sentence because it states a *conflicting*
count ("the attacker rolls one die for every generated impact"), not because it needs a signpost.

## Decision 11 — Two deltas, and the documents edited directly

Two shipped capabilities are touched, and both needed finding by reading `openspec/specs/` rather
than by reading the documents this change edits:

- **`component-damage`** holds *Component State Progression*, whose scenario *Wounded component
  still functions* says the component "continues to function normally".
- **`damage-resolution`** holds *Attack Roll*: "the attacker SHALL roll one D6" per Impact. That is
  the same statement `DMG-011` makes in the ruleset, and `CBT-015` contradicts both. The capability
  boundary does not follow the document boundary — `11-combat.md` has never been formalised, but
  the Attack Roll *mechanic* has, under `damage-resolution`.

Both requirements are `MODIFIED`, every living scenario is carried through, and no scenario is
renamed — `system/workflow.md` ("Scenario names are identifiers") is explicit that renaming one
reads as a delete plus an add and is refused.

`weapon-construction`'s *Attack Dice From Muzzle Count* ("Every muzzle SHALL generate exactly one
attack die") needs no delta, and the wording of `CBT-015` is what keeps it that way: the rule says
"for each Attack Die, roll two dice", never "generate two Attack Dice". That distinction is
load-bearing and must survive any later rewording.

`02-core-rules.md`, `07-movement.md`, `08-vehicles.md`, `10-weapons.md`, `11-combat.md`,
`12-melee.md`, `14-glossary.md` and `TODO.md` have no capability in `openspec/specs/` to delta
against, so their edits are ordinary doc-edit tasks, per `system/proposal-review.md` (*Delta vs.
Direct Edit*). No new capability is created: this change adds no system, it prices a state that
already exists.

---

## What this change deliberately leaves open

- **"Locomotion damage."** `VEH-019` names it as one of three ways a vehicle can be unable to move
  and no rule defines it. `VEH-031` says plainly that it does not define it either, and `TODO.md`
  now carries the gap with the quote that declares it.
- **Whether a Wounded component can be repaired more than once.** `DMG-019` allows one repair per
  activation and says nothing about a component that is wounded, repaired and wounded again. It is
  unchanged by this proposal and no less clear than before it.
- **A Wounded Pilot's other duties.** `VEH-013` requires the Pilot to move the vehicle; nothing
  states whether the Pilot does anything else. Only movement is degraded because only movement is
  written down.
- **Crew taking over from a Dead Pilot,** which `VEH-013` already defers to "future rules" and
  `TODO.md` already records. A Wounded Pilot cannot be handed off either, for the same reason: the
  hand-off does not exist yet.
- **Showing the degradation on a component that is not a minifigure.** A seated minifigure is the
  marker for infantry (`CORE-012`); a Wounded cannon looks exactly like an Operational one, and now
  fires differently. Principle 6 would prefer it visible — a tilted barrel, a hinge dropped one
  plate — and `DMG-008` currently leaves all such representation to the table. The pre-change
  ruleset already required a player to remember which components are Wounded, for the second-impact
  rule; this change makes it matter more often without making it visible, and closing that gap
  would touch every component type in the game.
