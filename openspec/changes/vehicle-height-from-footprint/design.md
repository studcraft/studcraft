# Design — vehicle height read from the footprint

## Context

`08-vehicles.md` reads every horizontal dimension of a vehicle off the model:
the footprint sets Deployment Area (`DEP-003`), the longest axis sets movement
(`VEH-003`, `VEH-004`), the locomotion sets terrain capability (`VEH-021`
through `VEH-024`). Height is read nowhere. Nothing in the shipped ruleset
states how tall a vehicle may be, and two rules that landed since — `TRN-019`
(Interior Clearance) and `TRN-020` (Interior Levels) — make vertical
construction precisely countable while bounding none of it.

The change adds one relationship and no new quantity. It is deliberately the
smallest thing that closes the gap.

---

## Decision 1 — the multiplier is read off the Unit Base, not chosen

`CORE-001` defines a Unit Base as a volume: 4 studs wide, 3 deep, 12 plate
layers tall, and what fills it is a standing minifigure. Read on the axis this
rule actually uses — the narrowest side — that is already a proportion:

> A Unit Base is 12 plate layers tall on a narrowest side of 3 studs — **4 plate
> layers for every stud**, which is the proportion of the volume one person
> occupies.

A vehicle is allowed **half as much again: 6**. That is this change's single
design decision, and everything else is arithmetic.

**The ratio belongs to the Unit Base, not to the minifigure standing in it.** A
draft phrased it as "the person who fills it stands 4 plate layers for every stud
of their own narrowest side", which is false of the plastic: a minifigure is
about a stud deep, so its own narrowest side gives 12 plate layers per stud. The
3 studs are the base's depth, not the figure's. Under Principle 1 a reader checks
the model, and the model has to agree.

**The derivation is stated on the narrowest side deliberately**, because that is
the operand the rule reads. An earlier draft derived it from the Unit Base's
4-stud *width* (12 ÷ 4 = 3 plate layers per stud, doubled to 6) and called the
result "twice the slenderness of a person". The number was right and the
sentence was wrong: it compared the vehicle's narrowest side against the Unit
Base's widest, so the factor is 1.5 on a like-for-like reading, not 2. Recorded
because the "twice" phrasing is the one a reader would use to argue the answer
should be 8.

Six is also what makes every other reading whole:

| Narrowest side | Unit Bases of height | Bricks | Plate layers |
|---:|---|---:|---:|
| 3 studs | 1½ | 6 | 18 |
| 4 studs | 2 | 8 | 24 |
| 6 studs | 3 | 12 | 36 |
| 8 studs | 4 | 16 | 48 |
| 12 studs | 6 | 24 | 72 |

Two standard bricks per stud, and one Unit Base of height for every two studs.
No footprint produces a fraction of a plate layer, because 6 is a whole number
and the narrowest side is a whole number of studs.

**Why the narrowest side and not the area.** Area would let a long thin vehicle
buy height by stretching along one axis, which is exactly the mast this rule
exists to stop. Reading the narrowest side means a Tank (8 × 15 studs) and a
Jeep (8 × 9 studs) share a limit, which is correct: neither is any wider than
the other, and width is what holds a tower up.

---

## Decision 2 — plate layers is the operative unit, and nothing is converted

`DMG-003` fixes the ruleset's vertical unit — a plate counts 1, a brick 3 — and
`VEH-021`, `VEH-026`, `MOVE-009`, `MOVE-016`, `TRN-019` and `TRN-020` all
measure vertical distance that way. A build reaches heights no whole brick count
expresses, so "8 bricks" is not a limit a player can check a plate-built hull
against. `VEH-028` states the limit in plate layers and gives the brick and
Unit-Base equivalents alongside, in that order.

`VEH-028` does **not** restate what a plate and a brick count as. `VEH-021`
already says it twenty rules earlier in the same document, and `VEH-028` cites
`VEH-021`.

**Height is plastic, measured above the Base Plane.** Nothing in this change
converts one unit into another, and `VEH-030` says so, because one interaction
invites it: a weapon's Length is measured in studs along its own firing axis
(`WPN-003`) and a raised barrel is a vertical extent in plate layers. The barrel
is measured by how high its plastic actually reaches. There is no stud-to-plate
conversion anywhere in `docs/`, and this change does not introduce one.

`WPN-004` is deliberately not cited beside `WPN-003` there. It is the word
"horizontal" in `WPN-004` that tempts the pairing, and that word belongs to
**Platform** Length, not to Weapon Length — `WPN-003` measures along the firing
axis, which for the elevated barrel this paragraph is about is precisely not
horizontal.

---

## Decision 3 — the datum is the Base Plane, not the table

Height is counted from the vehicle's own lowest interior floor. Three things
follow, and all three are the reason the datum is not the ground:

- **Terrain never changes legality.** A vehicle on a hill, in a depression, or
  part-way up a ramp measures exactly as it does on flat ground.
- **Locomotion is not charged twice.** Everything below the floor is priced by
  `VEH-022` (axle), `VEH-023` (knee) and `VEH-024` (hover assembly), each of
  which already trades reach against silhouette — `VEH-024` says so in those
  words. Measuring from the ground would make the long-legged walker `VEH-023`
  describes illegal, which is a rule inventing a contradiction with its own
  neighbour.
- **A vehicle inside a vehicle needs no extra rule.** The Base Plane is a
  property of the model, so a walker riding inside a transport (`TRN-001`,
  `TRN-003`) is measured against its own floor and the carrier against its own.
  This was left open in the issue this change comes from; defining the datum on
  the model answers it in the same sentence, so `VEH-029` says it explicitly
  rather than leaving a reader to infer it.

It is also the datum `TRN-020` already measures interior levels from, so the two
rules stack without conversion.

**A vehicle with no Pilot still has a Base Plane.** The obvious derivation — a
powered vehicle carries a Pilot occupying a Unit Base (`VEH-013`, `TRN-014`), so
there is always a floor for that Unit Base to rest on — covers only powered
vehicles. `CORE-004` and `VEH-001` both scope the Pilot requirement and the
two-Unit-Base minimum to powered vehicles, so a trailer, a towed gun or an open
flatbed falls outside it. `VEH-029` therefore names the fallback: the lowest
structural floor, the surface the vehicle's load rests on. It is one clause, and
without it an unpowered vehicle has no datum at all.

---

## Decision 4 — only Gameplay Geometry counts, because `GEO-007` requires it

`GEO-007`: "A model does not become invalid, and its measured values do not
change, solely as a result of adding Visual Geometry." A height limit that
counted decoration would invalidate a legal vehicle the moment a flag went on
it. Counting Gameplay Geometry only is not a choice this rule makes — it is the
one reading `GEO-007` permits.

`VEH-030` therefore writes **no list of functional and decorative parts**. A
second list would drift from `GEO-002`'s, which is a failure class this
repository has spent several changes removing. The table in `VEH-030` is worked
examples of `GEO-001`/`GEO-002`'s own test applied to height, and says so.

Two consequences worth stating in the rule rather than leaving to be discovered:

- **A mast is measured to the height of what it carries.** An observation post
  or a weapon mount is Gameplay Geometry, so everything below it is included
  automatically; only plastic continuing *above* the last functional element is
  free. No separate clause about structural support is needed.
- **This is not an exception to `GEO-004`.** `CMP-018` asks whether a model
  physically passes an opening, and decoration obstructs passage, so it counts
  there. This rule asks how much functional construction one footprint carries.
  A flag carries nothing. Decoration is still never free in play — it is
  visible, blocks sight lines and is shootable (`CORE-008`) — only in legality.

**`GEO-003`'s enumerated list is deliberately left alone.** It names the measured
values Gameplay Geometry feeds — Range, Attack Dice, Impact Strength, Resistance,
Weapon Capacity, Transport Capacity, Movement distance — and Maximum Height is
not among them. Neither is Terrain Threshold (`VEH-021`), which is equally a
value computed from Gameplay Geometry and shipped without joining the list. The
argument in this decision rests on `GEO-007`'s unqualified sentence, which does
not depend on the enumeration, and `geometry-layers` **is** a formalised
capability — editing `GEO-003` would mean a `MODIFIED` delta and a claim of
"affected capabilities: none" that is no longer true. Recorded so the question is
not reopened: if the list is ever completed, it should gain Terrain Threshold and
Maximum Height together, in a change that owns the `geometry-layers` capability.

---

## Decision 5 — movable elements are measured at their highest

A turret that rotates, a barrel that elevates, a ramp that lifts. Measured in
the position they occupy when checked, the check is answered by lowering the
barrel first and raising it afterwards. Measured in the highest position they
can physically be placed in during play, there is one answer and it is a
property of the build.

**This is the clause that can invalidate an existing model**, and it is the only
one that does anything the footprint alone would not. `proposal.md` records it as
a migration cost; the arithmetic that says how often it bites is below.

---

## Decision 6 — a model carried on the outside, and which document owns which half

Transport is a physically constructed interior space measured in Unit Bases
(`TRN-001`, `TRN-003`). A minifigure on a roof is not in one and is not embarked.
Nothing forbids placing it there — it is real plastic that physically balances on
a real model — and this change does not forbid it either. It is priced, in two
currencies, and **the two halves live in different documents**:

- **Deployment Area — `DEP-006`.** The waiver is for embarked units only, so a
  model on the outside is deployed individually and costs its own Unit Base
  (`DEP-004`). This is what `DEP-006` already means; the sentence is added there
  because a deployment-cost ruling stated only inside a rule titled "What Counts
  Toward Height", in the vehicle document, is a rule nobody reading
  `06-deployment.md` would ever find (Principle 10).
- **Height — `VEH-030`.** The model can see, be seen and be shot at (`CORE-008`,
  `CORE-009`), so it is Gameplay Geometry, measured in the highest position it
  can be placed in.

Together: the outside of a vehicle is never a cheaper way to carry a model than
the inside.

**An earlier draft cited `DEP-002` for permission to ride outside.** `DEP-002`
says an army "may occupy any combination of models that physically fits inside
the agreed Deployment Area" — it is about army composition against the Deployment
Area, not about whether a minifigure may perch on a hull. The citation existed
and was aimed wrongly, and it is gone. Nothing needs to grant the permission: the
ruleset forbids it nowhere.

**What this deliberately does not settle** is what such a model *does* — whether
it moves with the carrier, may act, or how it gets off. `TRN-005` and `TRN-006`
cover embarking and disembarking only. That gap exists today and this change
neither widens nor closes it; see open question 4.

---

## Decision 7 — the Summary keeps its six characteristics

`08-vehicles.md`'s Summary lists six physical characteristics: Size, Locomotion,
Terrain capability, Crew, Components, Interior volume. Maximum Height is not
added, and "six" is not changed.

The tempting argument — "it is derived, and derived values are not listed" — does
not survive contact with the list, because **Terrain capability is derived too**,
from Locomotion, which is also on the list. `system/proposal-review.md` records
that history explicitly: the Summary "listed five physical characteristics after
terrain capability became a sixth", and the fix was to add the entry and correct
the count.

The distinction that actually holds is *when* the value is read. Every entry on
that list is consulted during play — Size for movement, Terrain capability at
every obstacle, Crew and Components when Impacts resolve, Interior volume when
something embarks. Maximum Height is checked once, before deployment, and never
again; `VEH-028` says so in those words, and says there is no marker and no
in-game state. It is a condition on a legal vehicle, not a characteristic of how
one behaves. The Summary gains a sentence naming the relationship and citing the
new rules, and the count stays true.

---

## Decision 8 — the footprint is the operand, read as Unit Bases

`VEH-028` reads the narrowest side of the **footprint** — the Unit Bases the
vehicle covers, the same ones `DEP-003` charges. A footprint written `A × B` UB
measures `4A × 3B` studs (`CORE-001`), and where an outline is not rectangular,
`VEH-028` reads the smallest rectangle of Unit Bases enclosing it.

**One operand, said once, in the headline sentence.** An earlier draft opened
with "for every stud across its narrowest side", which reads the plastic, and
then defined the narrowest side off the Unit Base grid four paragraphs later. A
hull 6 studs wide sitting on 2 Unit Bases of width is 36 plate layers under the
first reading and 48 under the second, and nothing in `VEH-001` requires a hull
to fill its Unit Bases.

The grid wins for two reasons. It is what `DEP-003` already charges, so the
measurement is one the player has made anyway; and rounding up to the enclosing
rectangle is the reading that is generous rather than punitive, which matters for
a check that can make a built model illegal.

This does leave `08-vehicles.md` measuring its two horizontal axes differently —
`VEH-003` takes the long axis off the plastic for movement, `VEH-028` takes the
short one off the grid. That is not an oversight: movement is a distance the
model travels and must come from the model, while height is a construction
allowance bought with Deployment Area and must come from what was bought.
Its one bad case is recorded as open question 1.

---

## Numbers checked against numbers

`system/proposal-review.md` ("Multipliers Set Early Get Falsified by Numbers
Added Later") requires a new multiplier to be checked against every number it
can be compared with. All of these were computed, not estimated.

**Nothing becomes illegal by footprint alone.** The smallest footprint the
ruleset permits is two Unit Bases (`CORE-004`, `VEH-013`). Arranged side by side
that is 8 × 3 studs, narrowest side 3, so 18 plate layers. A Pilot needs a full
Unit Base of clearance — 12 plate layers (`TRN-019`) — plus a floor it rests on
and a roof over it. 13 ≤ 18, with 5 layers to spare. The tightest legal vehicle
in the game still admits its own Pilot.

**Interior levels become bounded, in a way that reads sensibly.** `TRN-020`
needs `12N + (N − 1)` plate layers above the lowest floor for N levels; a closed
top adds at least one more plate. Both readings give the same answer at every
footprint that matters:

| Narrowest side | Maximum Height | Levels (open top, `13N − 1`) | Levels (closed, `13N`) |
|---:|---:|---:|---:|
| 3 studs | 18 | 1 | 1 |
| 4 studs | 24 | 1 | 1 |
| 6 studs | 36 | 2 | 2 |
| 8 studs | 48 | 3 | 3 |
| 12 studs | 72 | 5 | 5 |

A bike-sized hull gets one deck. A Heavy Transport gets five, which is a tower
and is permitted — see the open questions.

**The one rule this shares an operand with is `WPN-004`, through decision 5.**
`WPN-004` caps `Σ(Weapon Length)` at the platform's **longest** horizontal
dimension; `VEH-028` caps height off the **narrowest**. A barrel that elevates is
measured vertically (decision 5), so a weapon bought against one axis is checked
against the other. The physical conversion is fixed by the parts, not by a rule:
a stud is 8 mm and a plate layer 3.2 mm, so a weapon L studs long stands `2.5L`
plate layers when raised to vertical. Against `6 × narrowest`:

| Vehicle | Longest (`Σ Weapon Length` cap) | Vertical extent | Maximum Height | Spare |
|---|---:|---:|---:|---:|
| Bike | 6 studs | 15 | 24 | 9 |
| Buggy | 8 studs | 20 | 36 | 16 |
| Jeep | 9 studs | 22½ | 48 | 25½ |
| Tank | 15 studs | 37½ | 48 | 10½ |
| Heavy Transport | 24 studs | 60 | 72 | 12 |

Every vehicle in `VEH-001`'s table can raise its entire weapon allowance to
vertical and still fit, with the hull beneath it accounted for in the spare
column. The general condition is `2.5 × longest ≤ 6 × narrowest`, i.e. a vehicle
no more than **2.4 times longer than it is wide**. Beyond that ratio — a 1 × 5 UB
hull, 4 × 15 studs — the full allowance cannot be raised vertical, and the build
lowers the barrel, shortens it, or widens the hull. That is a trade, not a
contradiction: `WPN-004` caps what may be carried and never requires it to point
anywhere.

**Movement, range and terrain are otherwise untouched.** Movement reads the
longest axis (`VEH-004`), Range is `6 × Weapon Length` (`WPN-005`), and the
Terrain Thresholds read the locomotion below the Base Plane. None of them is
computed from anything this change measures.

---

## Rejected

**A flat cap** — "no vehicle may exceed ten bricks", applying to every vehicle
whatever its footprint. It contradicts `VEH-001` one rule away, it is a number
read from nothing, and `system/proposal-review.md` ("Do Not Cap What the Model
Already Bounds") is about exactly this instinct. The footprint is already
measured, already on the table and already paid for.

**A Height Statistic, Vehicle Size Statistic, Vehicle Class or Tower Vehicle
classification.** Principle 1 and Principle 4. A player is never told a vehicle
is "too tall for its category", because there are no categories.

**Three plate layers per stud** — the plain proportion of a person read off the
Unit Base's width, without the factor added in decision 1. It flattens the game:
a Jeep 8 studs across tops out at 24 plate layers, and a second interior level
(25 plate layers, `TRN-020`) would need 9 studs of width, so only the Heavy
Transport in `VEH-001`'s table could ever have one. That makes `TRN-020` a rule
almost nothing can use.

**Counting all plastic, decoration included.** Contradicts `GEO-007` — see
decision 4.

**Measuring from the table rather than the Base Plane.** Makes terrain change
legality and charges locomotion twice — see decision 3.

**Measuring movable elements where they sit.** Answers the check by lowering the
barrel first — see decision 5.

**Measuring the narrowest dimension where the vehicle is tallest**, which would
close the L-shaped-arm case. It costs more wording than the shape is worth, and
it replaces one measurement of the whole model with a per-column one. Recorded
as an open question instead.

**Charging Deployment Area by enclosed volume instead of covered area.** It
would close the multi-deck advantage outright, and it rewrites `DEP-001`,
`DEP-002`, `DEP-003` and `DEP-009` and redefines what a game size means.
`unit-base-is-a-volume` already recorded it as out of scope; it still is.

---

## A linter limitation this change ran into

Recorded because it cost a round trip and will cost the next one too.

`scripts/lint_ruleset.py`'s `CROSS_REF_RE` pairs a backticked filename with the
**first** `(RULE-ID)` appearing within 80 characters after it, regardless of
which document that ID belongs to. A sentence that cites another document and
then uses the bare same-document form — the established convention, already in
`DEP-004`'s own neighbourhood at `06-deployment.md` — is reported as a broken
cross-reference:

```
06-deployment.md: references 09-transport.md (DEP-004), which does not exist
```

The prose is correct and the check is wrong. `DEP-006`'s new paragraph is
therefore worded so no bare same-document ID sits within 80 characters after a
backticked filename, and `tasks.md` task 5.2 records why so nobody "tidies" the
sentence back into the failing order.

**The linter is not fixed here.** `system/repository-strategy.md`'s Branch Naming
table limits a ruleset branch to `docs/*.md` plus its own change directory, so
`scripts/` cannot be touched from this branch. The fix belongs in its own
kebab-case branch: require the ID to be reachable without crossing a second
citation, or anchor the pattern to the comma form the repository actually writes.

---

## Open questions

Left unanswered rather than guessed at.

1. **A narrow arm on a non-rectangular footprint.** Reading the enclosing
   rectangle (decision 8) means an L-shaped vehicle with a wide body and an arm
   one Unit Base across takes its limit from the wide part, and may build the
   tower on the arm. Closing it needs the narrowest side measured where the
   vehicle is tallest rather than across the whole model.
2. **Whether the wide end needs a second constraint.** Six plate layers per stud
   is generous once a footprint is large: a Heavy Transport 12 studs across may
   rise 72 plate layers, taller than it is long. That build is still a tower and
   this rule permits it. A height-against-length check is one possible answer; it
   is a separate question.
3. **The multi-deck advantage.** Bounded by this change, not closed. `TRN-003`
   counts the Unit Base volume "available inside its cargo compartment" without
   saying whether an upper deck's Unit Bases are among them, and `SCS-014`
   defers to "interior volume" without settling it either. Whoever attempts it
   should know `TRN-014` exempts crew space from cargo capacity, so a limit
   phrased around cargo compartments is answered by calling the upper deck a
   crew station.
4. **What a model carried on the outside of a vehicle does.** This change prices
   it (decision 6) and settles nothing else: whether it moves with the carrier,
   may act during its own activation, or spends anything to get off. The gap
   predates this change — `TRN-005` and `TRN-006` define embarking and
   disembarking, and neither covers a model that was never embarked.
5. **The tower displaced below the Base Plane.** Decision 3 excludes everything
   under the lowest floor, so a narrow hull on 60 plate layers of leg reaches the
   altitude a mast would have and this rule never sees it. Bounding it means
   distinguishing a leg from a lattice, which is a classification and therefore
   the wrong instrument (Principles 1 and 4) — and charging it makes `VEH-023`'s
   walker illegal, which decision 3 exists to prevent. What already prices it is
   silhouette (`CORE-008`) and the legs' own destructibility (`VEH-017`,
   `VEH-018`). `VEH-029` states that chain rather than pretending the case does
   not exist. Whether it needs more than that is genuinely open.
6. **The tower displaced onto structures.** A mast that `VEH-028` makes illegal
   as a vehicle can be rebuilt without locomotion (`VEH-012`) and deployed as a
   structure, whose Deployment Area occupation is explicitly undefined
   (`CORE-005`). Closing that needs `CORE-005` finished, not a vehicle rule.
