# The Deployment Area is a volume

## Why

`06-deployment.md`'s own Design Philosophy opens with this:

> StudCraft measures army size using physical **volume** instead of abstract points.

`DEP-001` then agrees a rectangle. The third dimension is missing from the one rule
whose entire question is *what fits*, and the ruleset has spent a whole rule
compensating for it: `VEH-028` derives a per-vehicle height ceiling from the
footprint — 6 plate layers for every stud of the narrowest side — because nothing
else was bounding height.

That derived ceiling is the anomaly, and it shows:

- **The proportion is invented where everything else is read.** `VEH-028` says so
  itself: "A vehicle is allowed half as much again. That is this rule's only design
  decision." Every other measured value in StudCraft comes off the plastic.
- **It couples two things that are not related.** A 1 × 2 UB bike may rise 24 plate
  layers and a 3 × 8 UB transport 72, so a narrow vehicle is short by rule rather
  than by physics. Nothing about a thin hull makes a tall mast impossible to build.
- **It answers a question the players already answer.** The size of the game is
  agreed before it starts (`03-game-flow.md`, FLOW-001; `DEP-001`). Height is the one
  dimension of that agreement the ruleset took away from them.
- **It stops dividing.** `VEH-028`'s 6 is `12 ÷ 3 × 1.5`, read off the Unit Base's
  height. The follow-up change moves that height to 13, where the same derivation
  gives 6½ and the rule has to choose between an arbitrary rounding and a
  repository-wide rescale. Deleting the derivation is better than repairing it.

## What Changes

**The Deployment Area becomes the Deployment Volume**, agreed as `W × D × H` in Unit
Bases: a floor and a ceiling. Where two numbers are agreed, the ceiling is one Unit
Base — the smallest it can be, since infantry occupies exactly one (`TRN-002`).

An army is then what physically fits inside it, which is what `DEP-002` has always
said and can now mean literally.

- **`DEP-001`** agrees a volume, and names a low ceiling as a scenario choice —
  tunnels, hangars, bunker fights — rather than an accident.
- **`DEP-002`** fits an army on the floor *and* under the ceiling.
- **`DEP-003`** charges exactly what it charges today: the Unit Bases a footprint
  covers. Only its closing paragraph changes, because the footprint no longer bounds
  height.
- **`VEH-028`** keeps its ID and loses its content. A vehicle may be built to any
  height that fits under the agreed ceiling. The proportion, the five-row Maximum
  Height table and the worked "one level at 4 studs, three at 8, five at 12" all go.
- **`VEH-029`** stops being the Base Plane. Height is counted from the surface the
  vehicle rests on, **locomotion included** — a walker's legs, a wheel's diameter and
  a hover assembly occupy the ceiling like any other plastic.
- **`VEH-030`** survives nearly intact: height is still counted to the top of the
  vehicle's **Gameplay Geometry**, a movable element is still measured in the highest
  position it can be placed in, and an externally carried model still counts. Only
  its datum and its citations change.
- **`TRN-020`**'s closing line reads the ceiling instead of the footprint.
- **`DEP-009`'s suggested scenarios gain their ceilings** — Patrol `5 × 1 × 2 UB`,
  Skirmish `5 × 5 × 4 UB`, Battle `10 × 10 × 6 UB`, and `DEP-002`'s worked example
  becomes `5 × 5 × 4 UB` so that the same floor does not mean two different games
  sixteen lines apart. Left at two numbers each would default to a one-Unit-Base
  ceiling, which is a legitimate game but an infantry-only one. The three ceilings are
  chosen to match today's limits for the vehicles those games are played with — see
  What This Costs.
- **Deployment stops being described as a horizontal reading.** Four places say it is:
  `CORE-001`'s projections table, `CORE-001`'s own sentence, the glossary's
  *Projection* entry and `01-foundations.md`'s overview list. All four now read the
  volume, which is the change's entire point and the one thing a rename would have
  left behind.
- **`06-deployment.md` stops calling occupied space the cost.** Its Design Philosophy
  and Design Notes say the space a model occupies is what it costs; after this change
  the floor is charged and the height is not, so both say that instead.
- **`VEH-030`** loses one orphaned sentence — "This rule asks how much functional
  construction one footprint carries" — because after the rewrite the rule asks
  nothing about a footprint.
- **`assets/IMAGES.md`** is refreshed, as commit `a837ec9` refreshed it after #73 and
  #75. Two image briefs describe rules that no longer exist — `VEH-028`'s enclosing
  rectangle and `VEH-029`'s excluded leg assembly — and both are rewritten, filenames
  included; three rejection notes that cite the deleted text are corrected.
- **`14-glossary.md`** gains *Deployment Volume* and retires *Maximum Height* and
  *Base Plane*, neither of which names anything the ruleset still has.
- **The term is renamed** at all 27 capitalised sites, in `02-core-rules.md` (`CORE-005`'s
  structure caveat), `03-game-flow.md`,
  `04-construction-standard.md`, `08-vehicles.md` and `10-weapons.md`, plus
  `06-deployment.md` throughout, plus `assets/IMAGES.md`. Nine documents change in
  all, `09-transport.md` included for `TRN-020` alone and `01-foundations.md` for one
  bullet.

## What This Costs

Four consequences, stated plainly because each one changes what a player may bring:

- **Tall locomotion now costs ceiling.** A long-legged walker and a tall hover
  assembly are measured from the ground, so in a low-ceiling game they do not deploy.
  `VEH-029` currently exempts everything below the Base Plane on the grounds that
  `VEH-023` and `VEH-024` already price it in silhouette. That exemption goes:
  the Deployment Volume is real space, and space is occupied by whatever occupies it.
  Terrain capability is still read from the same parts, and silhouette still costs
  what it costs.
- **Narrow no longer means short.** A 1 × 2 UB bike may be built to the full agreed
  ceiling. The coupling `VEH-028` enforced is gone, and nothing replaces it.
- **Every Maximum Height figure disappears.** No vehicle has a height limit of its
  own any more; there is one ceiling per game, agreed by both players.
- **A two-number Deployment Volume is an infantry game.** With a ceiling of one Unit
  Base, no powered vehicle can exist: a Pilot occupies a Unit Base (`VEH-013`), that
  Unit Base needs a Unit Base of clear height above the surface it sits on
  (`TRN-019`), and the floor and locomotion beneath it are height too. `DEP-001` says
  so in place rather than leaving a player to discover it, and `DEP-009`'s scenarios
  carry explicit ceilings for the same reason.

The three suggested ceilings are chosen against what `VEH-028` allows today, so the
scenarios stay the games they were:

| Scenario | Ceiling | In plate layers | Today's `VEH-028` limit for its vehicles |
|---|---|---|---|
| Patrol `5 × 1 × 2 UB` | 2 UB | 24 | Bike, 4 studs across: 24 |
| Skirmish `5 × 5 × 4 UB` | 4 UB | 48 | Jeep and Tank, 8 studs across: 48 |
| Battle `10 × 10 × 6 UB` | 6 UB | 72 | Heavy Transport, 12 studs across: 72 |

Those figures are equal, not merely close — a Unit Base is 12 plate layers and
`VEH-028` allowed 6 per stud. What changes for those vehicles is not the number but
what it measures: the ceiling counts locomotion, so a walker that fitted its old
allowance may not fit the equivalent ceiling.

## Out of Scope

- **The footprint.** `DEP-003` still charges the Unit Bases covered, and overhangs
  are still read as `VEH-003` reads them. Only the ceiling is added.
- **Decoration.** Height is counted to the top of the vehicle's Gameplay Geometry,
  not to the top of its plastic. Counting decoration would contradict
  `15-geometry-layers.md` (GEO-007) — a model does not become invalid solely because
  Visual Geometry was added to it — and `design.md`, "Rejected", records the option
  and why it was turned down.
- **The Unit Base's height.** It stays 12 plate layers here; the change to 13 is the
  next proposal, and this change exists partly to clear its path.
- **Charging height as Deployment cost.** A volume budget only works for things that
  stack, and models do not: 125 UB of volume in a 5 × 5 × 5 game does not mean 125
  minifigures, because the floor holds 25. The ceiling is a limit, not a currency.
  `design.md`, "Rejected".
- **`06-deployment.md` and `08-vehicles.md` as capabilities.** Neither predates this
  repo's OpenSpec workflow as a tracked capability, so there is nothing to write a
  delta against for the deployment or vehicle rules themselves
  (`system/proposal-review.md`, Delta vs. Direct Edit). **One delta is written**, for
  `unit-base`: its *Unit Base Projections* requirement is normative about deployment
  reading the horizontal projection, and that stops being true here.
- **`CHANGELOG.md` and every `**Version:**` header.** Release-cut-only.
