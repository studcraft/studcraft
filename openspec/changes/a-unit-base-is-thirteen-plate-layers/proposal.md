# A Unit Base is thirteen plate layers

## Why

`CORE-001` says a Unit Base is 12 plate layers tall, and derives it like this:

> a Unit Base must contain a standing minifigure — about 4 bricks from its feet to the
> top of its head. Twelve plate layers is the smallest whole-brick height that does

Both halves are wrong about the model.

**A minifigure is not *about* 4 bricks. It is exactly 4 bricks**, feet to the top of
its head. Rendered beside a stack of four bricks it is flush, and beside four bricks
and a plate it is flush again once it stands on the base `SCS-002` requires — stud for
stud, measured off the render at 27 pixels per plate layer: the minifigure 324 pixels,
the base plate 27, the stack 351.

**So 12 does not contain the model.** It contains the minifigure and nothing else,
with the base it is built on left outside. But that base is not scenery: `SCS-002`
requires it, `CORE-002` reads facing off its 4-stud edge, `MOVE-003` measures movement
from its edges, and it travels with the model into every compartment and through every
doorway the ruleset checks. The volume that is supposed to be "the minimum operational
space an object needs" is one plate short of the object.

`CORE-001`'s current answer is to declare the base outside the volume — "that plate is
the model's floor, not part of the space above it". That works on the battlefield,
where the ground is the floor. It fails everywhere the ruleset actually uses the
figure: inside a transport the deck is the floor, the model's own base sits on top of
it, and the passenger needs a plate more than the Unit Base says it does.

The number is 13: **4 bricks of minifigure and the plate it stands on**. Nothing is
rounded, and nothing is chosen — Principle 1 in its plainest form.

Two earlier changes cleared the path. #80 removed fifteen restatements of the figure
so that it now lives only where it is defined, and #81 deleted the two derivations
(`VEH-028`'s height multiplier and the glossary's *Maximum Height*) that computed with
it and stopped dividing at 13. What is left is short.

## What Changes

- **`CORE-001`** states 13 plate layers, derives it from the minifigure and its base,
  and moves the measuring plane: height is counted from the **underside** of the base
  an infantry model stands on, which is part of the volume rather than the floor under
  it. Its two projection rows carry the new figure.
- **The head stud is named as not counted.** A stud is not height — it occupies the
  tube of whatever sits above it, which is why a brick stacks at 3 plate layers with
  its stud already in the count. `CORE-001` says so in its own voice; no other rule is
  cited for it, because none states it.
- **`SCS-002` pins the infantry base at one plate thick.** It constrained the footprint
  and nothing else, which was harmless while the base sat outside the volume. It is
  not harmless now: the height is 4 bricks *plus that plate*, so a base built a brick
  thick would put a legal model 15 plate layers tall inside a 13-plate-layer volume.
- **Three sentences that name a surface** are made explicit about which one — `TRN-019`
  and its glossary entry now measure clearance from the surface a model's **base**
  rests on rather than "the surface a model stands on", which after this change is the
  top of the base and would count it twice. `VEH-028` gains a clause saying a
  half-Unit-Base limit is met by any whole plate count below it, because at 13 a half
  Unit Base is six and a half plate layers.
- **`01-foundations.md`, `README.md` and `CODE_OF_DESIGN.md`** (Principle 7) carry the
  dimension line as an introduction and take the new figure.
- **`14-glossary.md`**'s *Unit Base* entry takes it too.
- **`TRN-013`'s drone, motorbike and walker heights move from 12 to 13.** All three
  were chosen to be exactly one Unit Base tall — it is what makes the drone illustrate
  cargo that fills one, beside a crate that takes part of one — so at 12 they stop
  illustrating anything. Reversed twice before landing here; `design.md`, Decision 3,
  records both turns and what the choice costs. The crate and the pallet keep their
  figures.
- **`assets/IMAGES.md`**'s `CORE-001` brief takes the new figure, moves the base plate
  **inside** the drawn volume, and gains a panel: the minifigure on its base, flush
  with a stack of four bricks and a plate, stud for stud. That panel is the derivation,
  and it is the one thing prose cannot do here.
- **Four spec deltas across two capabilities** — `unit-base`'s three requirements and
  `weapon-capacity`'s Platform Length scenario, which says "the Unit Base's 12 plate
  layers of height are not considered".

## What Does Not Change

Nothing measured in Unit Bases, which after #80 and #81 is nearly everything:

- **Clearance and capacity.** `TRN-003`, `TRN-019`, `TRN-020` and the transport
  Summary all read "one Unit Base of clear height". A compartment that held a
  passenger holds one after this change; it is one plate taller in plastic, and no
  rule sentence moves.
- **Vehicle height.** `VEH-028`'s two bounds are a proportion in Unit Bases and an
  agreed ceiling in Unit Bases. Both scale with the unit and neither is restated here.
- **Deployment.** `DEP-001`'s `W × D × H`, `DEP-003`'s floor charge, `DEP-009`'s
  suggested ceilings — all in Unit Bases.
- **Openings.** `CMP-018` reads the Unit Base's vertical projection and states no
  figure.
- **Resistance and terrain.** `DMG-003`'s plate-counts-1-brick-counts-3, `VEH-021`'s
  vertical distances and `MOVE-009` – `MOVE-011`'s thresholds measure material and
  distance, not occupied volume. Untouched.

**What does change in plastic:** a closed compartment built to exactly 12 plate layers
of clear height stops carrying infantry, and a doorway built to exactly 12 stops
passing it. Both were already one plate short of the model that had to fit; this
change says so. `TRN-019` already tells a builder what to do about it — "raising the
roof by a plate or two, or opening it, is the whole repair".

## Out of Scope

- **Vertical cargo overflow.** Still open, still recorded in
  `deployment-is-a-volume`'s `design.md`: a compartment with two Unit Bases of
  clearance and no intermediate floor offers one position, not two. The figure moving
  does not settle it.
- **Whether the deployment floor is packed or budgeted.** Also open, also recorded
  there.
- **`CHANGELOG.md` and every `**Version:**` header.** Release-cut-only. The commit
  does carry `**Bump:** major`, which is not a version edit — it is the marker
  `scripts/release_cut.py` reads (`system/documentation-standards.md`, Versioning).
  This change makes previously legal models illegal, which is what major means.
