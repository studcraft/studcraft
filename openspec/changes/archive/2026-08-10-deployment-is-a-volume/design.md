# Design — The Deployment Area is a volume

## Context

`unit-base-is-a-volume` (#73) made the Unit Base a volume with three readings, and
`CORE-001` now carries the vocabulary: the horizontal projection for distances,
footprints and deployment areas; the volume itself for capacity and interior space;
the vertical projection for passing an opening.

Deployment was left reading the horizontal projection. It is the one rule in the
ruleset whose question is *what fits* and whose answer ignores height, and
`VEH-028` — added later, in #75 — exists to fill the gap from the other side.

This change puts deployment in the row it belongs to and deletes the compensation.

---

## Decision 1 — the ceiling is a limit, not a currency

The agreed volume is `W × D × H`. The floor is charged exactly as today
(`DEP-003` per Unit Base covered, `DEP-004` one per infantry model). The ceiling is
not charged at all: it is the height every model must fit under.

**Why not charge volume.** The obvious-looking alternative is to make the budget the
volume itself — a model costs footprint × its own height in Unit Bases. It does not
work, and the reason is physical: a 5 × 5 × 5 UB volume is 125 UB, but an army of
infantry cannot field 125 minifigures in it, because they do not stack. The floor
holds 25 and the other 100 UB of "budget" is unreachable. A volume budget is only
coherent for things that can be stacked into it, and models are not among them.

So the third number does what the players actually want it to do: it says how tall
anything may be. `DEP-002`'s "any combination that physically fits" then means what
it says, in three dimensions.

**Two numbers means a ceiling of one Unit Base**, and that is also the floor of the
whole rule: infantry occupies exactly one Unit Base (`TRN-002`), so a Deployment
Volume shorter than that admits no army at all.

---

## Decision 2 — locomotion counts toward the ceiling

`VEH-029` currently exempts everything below the Base Plane: wheels, legs, hover
assemblies. Its argument is that `VEH-023` and `VEH-024` already price that height in
silhouette, and that "charging it twice here would make the walkers and hover
vehicles they describe illegal".

That argument was correct against a **derived, per-vehicle** ceiling. A footprint
does not become able to support a taller hull because the hull sits on legs, so
charging legs against a footprint-derived allowance really was charging twice.

It is not correct against **agreed space**. A walker two Unit Bases tall on legs
another Unit Base long occupies three Unit Bases of the room; whether the third one
is leg or hull changes nothing about the space it takes. The Deployment Volume is a
box the model has to fit inside, and a box does not care which part of the model
reaches the lid.

What survives unchanged: the Terrain Threshold is still read from the same parts
(`VEH-022` – `VEH-024`), and tall locomotion still costs silhouette
(`CORE-008`). What changes is that reach bought with legs and reach bought with hull
are now paid for out of the same ceiling — which is the more honest of the two,
because on the table they are the same reach.

**This makes models illegal that are legal today**, and `proposal.md` says so under
its own heading rather than burying it here. A long-legged walker needs a game whose
players agreed a tall enough ceiling.

---

## Decision 3 — the ceiling counts Gameplay Geometry, not all plastic

"Physically fits" taken absolutely literally would count a flag, an antenna and a
decorative mast, because they are plastic and they stick up.

Rejected, on a rule the ruleset already settled. `15-geometry-layers.md` (GEO-007):
a model does not become invalid, and its measured values do not change, solely as a
result of adding Visual Geometry. `VEH-030` is built on that and states the
consequence directly — "a height limit that counted decoration would invalidate a
legal vehicle the moment a flag went on it".

So the ceiling counts what `VEH-030` already counts: the vehicle's Gameplay Geometry,
with a movable element measured in the highest position it can physically be placed
in, and an externally carried model included. The change to `VEH-030` is its datum
and its citations, not its test.

The pair of decisions is deliberate and reads oddly at first glance — legs count,
flags do not. It is the same line `15-geometry-layers.md` draws everywhere: a leg
holds the model up and feeds a measured value (`VEH-023`), a flag holds nothing.
Decoration is still never free in play — it is visible, it blocks sight lines and it
is shootable (`GEO-004`) — only in legality.

**And `GEO-004` is not being contradicted, though it looks close.** `GEO-004` says a
physical check is resolved against the plastic as built, "decorative elements
narrowing that opening count exactly as much as structural ones". That is true of an
access opening, where a model is pushed through a real gap and a flag really does
catch. The agreed ceiling is not that kind of check: nobody lowers a lid onto the
army. It is a measured value compared against an agreed number, which is exactly what
`GEO-003` separates from a physical check, and `VEH-030` — the rule that supplies the
measurement — has always measured Gameplay Geometry.

The wording has to carry that distinction rather than leave it to the reader, which is
why two sentences change beyond the rename: `DEP-002` says how a model's height is
read, and `VEH-030`'s "This rule asks how much functional construction one footprint
carries" becomes a sentence about what a model raises into the volume. Without them
the ruleset would say "physically fits" in one document and "Gameplay Geometry" in
another about the same check.

---

## Decision 4 — a vehicle is measured standing on its own locomotion, always

New `VEH-029` counts height "from the surface the vehicle rests on". Read carelessly
that gives a walker deployed inside a transport a datum on the carrier's floor, a
smaller measurement, a pass — and then a disembarked walker standing taller than the
ceiling both players agreed to, permanently legal because `VEH-028` checks once and
never again.

So the datum is the surface the vehicle rests on **when it stands on its own
locomotion**, whether or not the game starts with it embarked. The check belongs to
the model, not to where it happens to begin. This also keeps `VEH-028`'s once-only
promise honest: measured that way, there is no state a vehicle can enter in play that
would change the answer.

---

## Decision 5 — `VEH-028` keeps its ID and changes its content

Deleting the rule would leave a gap at `VEH-028` and break ten citations across five
documents. Keeping the ID and replacing the rule keeps every pointer resolving and
records, in the one place a reader looks, that a vehicle's height is now settled
elsewhere. `system/documentation-standards.md` asks that rule identifiers remain
stable; it does not ask that their content never change, and `MEL-010`, `CBT-011` and
`WPN-021` are the precedent for keeping a superseded thing visible where it was.

`VEH-029` is treated the same way: the ID survives, the Base Plane does not. What the
rule now answers is the question its successor still needs answered — *from where* —
and the answer is the surface the vehicle rests on.

The glossary is the exception. *Maximum Height* and *Base Plane* are retired outright,
because a glossary entry for a term the ruleset no longer uses is a pointer to
nothing. The concepts they named are not superseded by other terms; they are gone.

---

## Decision 6 — what a low ceiling buys, and what one Unit Base costs

Worth stating in `DEP-001` rather than leaving implicit: a low ceiling is a scenario
tool, not a mistake. Tunnels, hangars, cargo holds and bunker fights are agreed at
the same moment as the battlefield (`FLOW-001`), by choosing a smaller `H`. The
ruleset gains a whole category of scenario without adding a rule for it — which is
the same trade `DEP-001` already makes for floor size.

**The floor of that scale is an infantry game, and `DEP-001` says so.** A ceiling of
one Unit Base admits no powered vehicle at all: a Pilot occupies a Unit Base
(`VEH-013`), `TRN-019` requires a Unit Base of clear height above the surface that
Unit Base sits on, and the interior floor and the locomotion under it are height as
well. Since two agreed numbers mean a ceiling of one, that is the **default**, and a
default whose consequence is invisible is a trap. The rule states it, and `DEP-009`'s
three suggested scenarios carry explicit ceilings — `5 × 1 × 2`, `5 × 5 × 4`,
`10 × 10 × 6` — chosen so that each equals what `VEH-028` allows today for the
vehicles that scale is played with (2, 4 and 6 Unit Bases are 24, 48 and 72 plate
layers; `VEH-028` gave 24, 48 and 72). The scenarios stay the games they were.

`DEP-002`'s worked example moves to `5 × 5 × 4 UB` for the same reason: at two numbers
it offered "1 large tank" under a ceiling that cannot hold a pilot, and it shared a
floor with Skirmish while meaning something different.

---

## Rejected

**Keeping `VEH-028` and rounding its multiplier at 13.** "Half a Unit Base per stud,
taken to the whole plate below" keeps every current figure and changes no model's
legality. Rejected because it converts a value that was read off the Unit Base into a
value with a rounding step attached, and leaves the ruleset asserting a coupling
between narrowness and height that nothing physical supports. If the derivation has
to be patched to survive, the derivation is the problem.

**Rescaling `VEH-028` to one Unit Base per two studs (6½ plate layers per stud).**
This is the faithful reading of the same derivation — `(13 ÷ 3) × 1.5` is exactly
`13 ÷ 2` — and it survives the height change cleanly. Rejected because it raises
every vehicle's ceiling by about 8% as a side effect of a wording repair, and because
odd narrowest sides (3, 9, 15 studs) then land on half a plate layer, which no model
can be built to.

**Height as the number of whole Unit Bases across the narrowest side.** Simple, fully
expressed in Unit Bases, and it dissolves the oddity that `2 × 1 UB` (8 × 3 studs)
allows 18 plate layers while `1 × 2 UB` (4 × 6 studs) allows 24. Rejected on
arithmetic: a Jeep (`2 × 3 UB`) would cap at 2 Unit Bases of height, and two interior
levels need two Unit Bases **plus the plate of the floor between them**
(`TRN-020`). Every vehicle narrower than 3 Unit Bases would be permanently
single-deck, and `VEH-028`'s own worked answers would fall from one/three/five levels
to one/one/two. A limit that can never quite fit what the rule beside it costs is the
wrong limit.

**Charging the ceiling as Deployment cost.** Decision 1 — models do not stack, so a
volume budget over-counts by the height of the box.

**Counting all plastic against the ceiling.** Decision 3 — contradicts `GEO-007`.

**Renaming the term to something other than *Deployment Volume*.** *Deployment
Space*, *Deployment Box* and keeping *Deployment Area* were all considered.
*Volume* wins because `CORE-001` already uses exactly this word for exactly this
distinction, and because "Area" naming a volume is the defect #73 and #79 spent two
changes removing from the Unit Base. The rename costs 26 sites across seven
documents and buys the ruleset one vocabulary.

---

## The one spec delta

Neither `06-deployment.md` nor `08-vehicles.md` has ever been formalised as an
OpenSpec capability — `openspec/specs/` holds `action-economy`, `component-damage`,
`damage-resolution`, `geometry-layers`, `unit-base`, `weapon-capacity` and
`weapon-construction`, and none of them owns deployment or vehicle height. Their
wording changes are tracked as ordinary doc-edit tasks
(`system/proposal-review.md`, Delta vs. Direct Edit).

`unit-base` **is** tracked, and it is normative about this. Its *Unit Base
Projections* requirement reads "the horizontal projection (4 × 3 studs) for distances,
movement, deployment areas and footprints", and its `Deployment reads the horizontal
projection` scenario computes "a vehicle's Deployment Area cost". This change writes
a `MODIFIED` delta for that one requirement, at
`openspec/changes/deployment-is-a-volume/specs/unit-base/spec.md`.

Two things about it are deliberate. **Every existing scenario keeps its name**,
including `Deployment reads the horizontal projection` — which stays true, because the
floor is still charged from the horizontal projection; only its body changes to say
the height is charged nothing. `system/workflow.md` ("Scenario names are identifiers")
forbids the rename that would otherwise be tempting. And a fourth scenario is
**added** inside the same block, for the reading that did not exist before: the ceiling
is the volume itself.

`unit-base`'s other two requirements are untouched, and one of them is a debt this
change hands on rather than pays. *Unit Base Measurement* reads "Every distance,
**deployment area**, and vehicle or infantry footprint SHALL be expressed using this
unit" — the sentence `CORE-001` mirrors, and which this change rewrote to "All
distances, Deployment Volumes and vehicle footprints". Deltaing it here as well would
put two changes' `MODIFIED` blocks on one requirement, which is the conflict
`system/workflow.md` ("When several changes modified the same requirement") exists to
prevent: the next change moves the Unit Base's height, stated in that same
requirement's first sentence, so it must modify it regardless. That change owns the
repair, and the Handover below names it so nobody has to rediscover it.

---

## Handover — what the height change inherits

With this applied, moving the Unit Base from 12 plate layers to 13 no longer touches
`VEH-028`, `VEH-029` or the glossary's *Maximum Height*: the two derivations that did
not divide at 13, and the entry that restated one of them, are gone. What is left for
that change is the definitional sites — `CORE-001` and its projections table,
`01-foundations.md`, `README.md`, `CODE_OF_DESIGN.md`, the glossary's *Unit Base*
entry, `assets/IMAGES.md`'s `CORE-001` image brief — plus `TRN-013`'s three
12-plate-layer cargo heights and four spec deltas across two capabilities.

One of those four, `unit-base`'s **Unit Base Measurement**, carries a second repair
that has nothing to do with the height: it still says "deployment area" where
`CORE-001` now says Deployment Volume. This change deliberately left it rather than
put two `MODIFIED` blocks on one requirement — see "The one spec delta" above.

And one thing this change did **not** inherit cleanly: `DEP-001` now fixes `H` in
whole Unit Bases, which reintroduces the granularity the deleted `VEH-028` argued
against ("a hull with plates in it reaches heights no whole brick count expresses").
The argument was answered rather than dropped — a model's own height is still measured
in plate layers, so a 22-plate hull fits a two-Unit-Base ceiling — but if half-Unit-Base
ceilings are ever wanted, `DEP-001` is where that decision goes, and at 13 plate layers
a half Unit Base is not a whole plate.


---

## Decision 8 — both bounds, one measurement (review on PR #81)

The first version of this change made the agreed ceiling the only bound on a vehicle's
height. The review blocked on it, correctly: in a `10 × 10 × 6 UB` game a `2 × 2 UB`
vehicle could then be built six Unit Bases tall. `VEH-028`'s proportion was not a
substitute for the missing third dimension — it was a construction constraint that
happened to be the only height rule there was — and deleting it reopened the
narrow-tower case it existed to close.

Both bounds apply. A vehicle is legal only if its height is under its footprint's
proportion **and** under the agreed ceiling. They answer different questions: the
proportion travels with the model, the ceiling is the size of the game.

**The proportion is stated in Unit Bases, and that is what makes keeping it possible.**
`design.md` originally rejected keeping the bound because at 13 plate layers
`12 ÷ 3 × 1.5` becomes 6½ and the rule would need an arbitrary rounding. Written as
*one Unit Base of height for every two studs of the narrowest side*, it is the same
derivation with the conversion removed — `(UB ÷ 3) × 1.5 = UB ÷ 2` — and it needs no
plate figure at all. It reproduces every limit the old table gave: 2, 3, 4, 4 and 6
Unit Bases are the 24, 36, 48, 48 and 72 plate layers it printed. An odd narrowest
side lands on half a Unit Base, and nothing rounds: a model's height is measured in
plate layers and compared.

That also answers the review's second point without a special case. No rule outside
`CORE-001` now converts a Unit Base into plate layers.

**One height, two comparisons — the Base Plane does not come back.** The obvious
alternative was to keep the ceiling counting locomotion while the footprint bound
measured only from the vehicle's interior floor, which is what the old `VEH-029` did.
Rejected on three grounds:

- **One word, one measurement.** Two datums for one noun is the defect the last three
  changes have been removing. A player would have to know which "height" a check
  means before picking up the ruler.
- **The physics the bound rests on counts the legs.** The proportion asks whether a
  base justifies a height. A hull one and a half Unit Bases up on legs another two
  Unit Bases long is exactly as disproportionate as a hull three and a half Unit Bases
  tall on the same base. The old argument — that a footprint does not support more
  hull for being on legs, so charging legs against it was charging twice — measures
  the hull where the bound measures the model.
- **It would close one loophole and leave its twin open.** The old `VEH-029` said in
  as many words that a vehicle "can gain reach by standing on tall locomotion instead
  of by building upward, and this limit never sees it". Reach bought with legs and
  reach bought with hull are the same reach on the table.

**What it costs:** a long-legged walker on a small base stops existing. A tall walker
is now a wide walker. That is a design statement rather than a casualty — but if
walkers turn out to be squeezed in play, the repair is not to reopen the exclusion.
It is to recognise that a walker's stance *is* wide and give it the footprint it
occupies standing, which would be its own proposal.


---

## Open — is the floor packed or budgeted?

`DEP-002` says an army is "any combination of models that fits inside the agreed
Deployment Volume — on its floor and under its ceiling". Two readings survive that
sentence, and the ruleset has always contained both:

- **Packing**: the floor is a shape, and a `1 × 2 UB` vehicle needs two Unit Bases of
  depth to sit in. `DEP-001`'s `W × D` framing implies this.
- **Budget**: the floor is a count, and a `1 × 2 UB` vehicle costs 2 of the 25 a
  `5 × 5 UB` game holds. `DEP-003`'s "This area is unavailable for any other model"
  implies this.

They differ wherever a footprint is deeper than the floor: under packing, no vehicle
deeper than one Unit Base can be fielded in a `5 × 1 UB` game at all; under a budget,
a Bike fits, and nothing says how a rotated `4 × 6`-stud footprint is counted against
a grid of `4A × 3B`.

This change did not create the ambiguity — `DEP-002`'s wording is unchanged from
before it — but making the agreed thing a `W × D × H` volume sharpens it, and the
audit found it by checking whether `DEP-009`'s Patrol ceiling can ever bind. It
cannot, and `proposal.md`'s scenario table now says so rather than claiming a match
that only holds under the budget reading.

Settling it is a mechanical change to `DEP-002` and `DEP-003`, not a rewording, so it
needs its own proposal. Recorded here so it is proposed rather than rediscovered — the
second such question this change leaves standing, alongside vertical cargo overflow
(Decision 3).
