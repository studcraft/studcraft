## 0. Setup

- [x] 0.1 Work on branch `unit-base-is-a-volume` (`openspec/config.yaml` requires one branch per proposal, and `system/repository-strategy.md` requires the branch to be named for the change).

### How to read the replacement blocks

Replacement text is shown as a markdown blockquote so it is visually separable from the instructions. **The `> ` prefix is not part of the text.** Strip it from every line before writing into the document.

Where a block contains a `#` heading, a `|` table, a fenced code block, a bullet list or bold markers, those are part of the text and must be written as real markdown.

### What "the body of a rule" means

Everything between that rule's `#` (or `##`) heading line and the `---` that ends it. **Never change, remove or renumber an existing heading.** Two rule IDs are added (`TRN-019`, `TRN-020`); none is renumbered. Task 11.2 checks the count.

### Anchors

Every quoted anchor below was checked with `grep -cF` against the pre-change files and returns exactly **1**. Four of them begin with `-` and need `grep -cF -e '<anchor>'` to check. If any anchor returns anything other than 1, stop and report it instead of guessing which occurrence was meant.

### Scope

Ten ruleset documents and two repository documents change, plus the two spec deltas already written in this change directory, which must not be edited:

| Path | What changes |
|---|---|
| `docs/02-core-rules.md` | `CORE-001` body |
| `docs/01-foundations.md` | the `Unit Base (UB)` section |
| `docs/04-construction-standard.md` | `SCS-005` |
| `docs/06-deployment.md` | `DEP-005` |
| `docs/08-vehicles.md` | `VEH-015`, `VEH-016` |
| `docs/05-construction-components.md` | `CMP-018`'s **Height** paragraph, and one sentence in its opening paragraph |
| `docs/15-geometry-layers.md` | `GEO-004` access-openings bullet, and the Summary line that lists the physical checks |
| `docs/10-weapons.md` | `WPN-004` Platform Length sentence |
| `docs/09-transport.md` | Purpose, `TRN-001`, `TRN-002`, `TRN-003`, `TRN-005`, `TRN-013`, new `TRN-019`, new `TRN-020`, Summary |
| `docs/14-glossary.md` | `UB`, `Platform Length`, `Cargo Bay`, new `Interior Clearance`, `Slice`, `Projection` |
| `README.md` | the `Unit Base (UB)` section under Core Concepts |
| `CODE_OF_DESIGN.md` | Principle 7 |

Nothing else. `CHANGELOG.md` and every `**Version:**` header are untouched (`system/documentation-standards.md`, Versioning). `openspec/specs/` is untouched — archiving is a separate PR (`system/workflow.md`).

### One idea, stated once

- The volume, its derivation, the projection principle, the Line-of-Sight boundary and "what must fit is the Unit Base" all live in **`CORE-001`**. Every other rule cites it and adds no reasoning of its own.
- Interior clearance lives in **`TRN-019`**. `TRN-003`, `TRN-005` and the glossary cite it.
- Cargo divisibility lives in **`TRN-013`**. `TRN-001`, `TRN-003` and `TRN-019` cite it.
- The crew consequence (a Pilot needs a Unit Base) is stated **once**, in `TRN-019`. Do not restate it in `VEH-013`, `VEH-015`, `TRN-014` or `CMP-013`.

Task 11.6 checks the first of these.

### Coverage

| Item in `proposal.md` / `design.md` | Task |
|---|---|
| `CORE-001` becomes a volume, with derivation, projections, the physical-check boundary and "what must fit is the Unit Base" | 1.1 |
| `01-foundations.md` tracks the definition | 2.1 |
| `SCS-005` names the Unit Base as the thing that fits (decision 1) | 3.1 |
| `DEP-005` likewise | 3.2 |
| `VEH-015` likewise, for crew | 3.3 |
| `VEH-016` likewise, for passengers | 3.4 |
| `CMP-018` height becomes measured, and names what passes (decision 5) | 4.1, 4.2 |
| `GEO-004` access-openings bullet moves with `CMP-018` | 5.1 |
| The geometry Summary's physical-check list catches up | 5.2 |
| `WPN-004` Platform Length reads the horizontal projection | 6.1 |
| `09-transport.md` Purpose stops counting whole Unit Bases | 7.1 |
| `TRN-001` admits fractional occupancy | 7.2 |
| `TRN-002` names the minifigure carve-out (decision 6) | 7.3 |
| `TRN-003` counts volume, not objects | 7.4 |
| `TRN-005` free Unit Base is free in three dimensions | 7.5 |
| `TRN-013` cargo divides a Unit Base into slices (decision 6) | 7.6 |
| `TRN-019` Interior Clearance, seating, fittings, crew cost (decision 3) | 7.7 |
| `TRN-020` Interior Levels (decision 4) | 7.8 |
| Transport Summary tracks the rules above | 7.9 |
| Glossary `UB` carries the volume | 8.1 |
| Glossary `Platform Length` reads horizontal | 8.2 |
| Glossary `Cargo Bay` points at clearance | 8.3 |
| Glossary gains `Interior Clearance`, `Slice`, `Projection` | 8.4 |
| `README.md` stops restating a 2D definition | 9.1 |
| `CODE_OF_DESIGN.md` Principle 7 likewise | 9.2 |
| Archive-order dependency recorded | 10.1 |

---

## 1. `docs/02-core-rules.md`

### 1.1 `CORE-001` — the Unit Base becomes a volume

- [x] 1.1.1 Replace the entire body of `CORE-001` — everything between the `## CORE-001 — Unit Base (UB)` heading and the `---` that ends the rule — with the following. The heading itself is not touched.

> StudCraft uses a single measuring unit.
>
> One **Unit Base (UB)** is a volume measuring:
>
> **4 studs wide × 3 studs deep × 12 plate layers tall**
>
> This is the standard base for infantry. The 4-stud edge is the front (CORE-002).
>
> Height is counted in plate layers because that is the ruleset's vertical unit — a plate counts as 1 and a standard brick as 3 (`16-damage-system.md`, DMG-003; `08-vehicles.md`, VEH-021). Twelve plate layers is therefore exactly 4 bricks. Height is measured from the top face of the plate an infantry model stands on: that plate is the model's floor, not part of the space above it.
>
> The height is read from the model rather than chosen. Infantry occupies exactly one Unit Base whether standing or seated (`09-transport.md`, TRN-002), so a Unit Base must contain a standing minifigure — about 4 bricks from its feet to the top of its head (`05-construction-components.md`, CMP-018). Twelve plate layers is the smallest whole-brick height that does, and a Unit Base is the minimum operational space an object needs (`09-transport.md`, TRN-001), so it takes exactly that and no more.
>
> **What must fit is the Unit Base.** Wherever a rule asks whether something physically fits — a passenger, a crew member, cargo, a model passing an opening — the volume that must fit is the Unit Base: one for a minifigure, its own volume in Unit Bases for a vehicle (`04-construction-standard.md`, SCS-005). Never the loose model. A minifigure that would slip into a smaller gap than its Unit Base does not fit there.
>
> **Projections.** A rule never reads more of the volume than it needs:
>
> | Reading | Used by |
> |---|---|
> | Horizontal projection — `4 × 3` studs | Distances, movement, deployment areas, footprints |
> | The volume itself — `4 × 3` studs by 12 plate layers | Transport capacity and interior space |
> | Vertical projection — 4 studs by 12 plate layers | Passing through an opening |
>
> The vertical projection is taken across the front, because the 4-stud edge is the front (CORE-002) and it is what enters an opening first.
>
> A projection supplies a measured value and nothing else — the boundary `15-geometry-layers.md` draws (GEO-003).
>
> It never replaces a physical check. Line of Sight (CORE-008) and Cover (CORE-010) are resolved against the plastic actually on the table, never against a Unit Base's silhouette (`15-geometry-layers.md`, GEO-004).
>
> All distances, deployment areas and vehicle footprints are expressed using this unit. When a footprint is written as `W × D` UB (e.g. "Jeep: 2 × 3 UB"), the first number is a count of 4-stud widths and the second a count of 3-stud depths — a `2 × 3 UB` footprint measures `8 × 9` studs, not `6 × 12`. A footprint is a horizontal reading, and says nothing about a model's height.

- [x] 1.1.2 Those last two sentences are **two separate paragraphs, deliberately**. `scripts/lint_ruleset.py` pairs a `` `file.md` `` with the next `(RULE-ID)` appearing on the same line, so putting the `15-geometry-layers.md` citation and `(CORE-008)` in one paragraph makes it read `CORE-008` as a rule of `15-geometry-layers.md` and fail the required check. Do not rejoin them.

- [x] 1.1.3 Change nothing else in `02-core-rules.md`. `CORE-002`, `CORE-003` and `CORE-004` are untouched: facing is unchanged, infantry still occupies one Unit Base, and "occupies two or more Unit Bases" is a horizontal reading settled by the projection table above (`design.md`, Verified unaffected).

---

## 2. `docs/01-foundations.md`

### 2.1 The `Unit Base (UB)` section

- [x] 2.1.1 Anchor: `The Unit Base (UB) is the universal measurement used throughout the game.` Replace everything from that line down to and including the line `- Cargo occupies UB.` with:

> The Unit Base (UB) is the universal measurement used throughout the game.
>
> One Unit Base is a volume measuring:
>
> **4 studs wide × 3 studs deep × 12 plate layers tall**
>
> (see `02-core-rules.md`, CORE-001, for the canonical definition, where the height comes from, and which projection each rule reads)
>
> Everything in StudCraft is ultimately measured using Unit Bases.
>
> Examples:
>
> - Infantry occupies 1 UB, and never shares it.
> - Deployment areas are measured in UB, horizontally.
> - Vehicle footprints are measured in UB, horizontally.
> - Transport capacity is measured in UB, as a volume.
> - Cargo occupies UB, and several objects may share one (`09-transport.md`, TRN-013).

- [x] 2.1.2 Leave the line `Using a single measurement system keeps the rules simple and consistent.` and everything after it unchanged.

---

## 3. What must fit is the Unit Base

Each task in this section adds one sentence and removes none. The reasoning stays in `CORE-001`; these four rules cite it.

### 3.1 `SCS-005` — `docs/04-construction-standard.md`

- [x] 3.1.1 Anchor: `- terrain` (the last bullet of `SCS-005`'s "This applies to:" list). Insert the following as a new paragraph immediately **after** that bullet and **before** the `---` that ends the rule:

> What must fit is measured in Unit Bases (`02-core-rules.md`, CORE-001): a minifigure needs one whole Unit Base, a vehicle its own volume in Unit Bases. A model that would slip into a gap smaller than its Unit Base does not fit there.

### 3.2 `DEP-005` — `docs/06-deployment.md`

- [x] 3.2.1 Anchor: `If a minifigure physically fits inside the vehicle, it may be transported.` Replace that line with:

> If a Unit Base fits inside the vehicle, a minifigure may be transported in it (`02-core-rules.md`, CORE-001; `09-transport.md`, TRN-019).

- [x] 3.2.2 Leave the lines `If it does not fit, it cannot.` and `The LEGO model is the source of truth.` unchanged.

### 3.3 `VEH-015` — `docs/08-vehicles.md`

- [x] 3.3.1 Anchor: `Crew must physically fit inside the vehicle.` Replace that line with:

> Crew must physically fit inside the vehicle. A crew member occupies a Unit Base like any other passenger (`09-transport.md`, TRN-014), so what must fit is that Unit Base (`02-core-rules.md`, CORE-001).

### 3.4 `VEH-016` — `docs/08-vehicles.md`

- [x] 3.4.1 Anchor: `If a passenger physically fits, it may embark.` Replace that line with:

> If a passenger's Unit Base physically fits, it may embark (`02-core-rules.md`, CORE-001).

- [x] 3.4.2 Leave `If it does not fit, it cannot.` and `No transport statistic exists.` unchanged.

---

## 4. `docs/05-construction-components.md`

### 4.1 `CMP-018` — what passes through the opening

- [x] 4.1.1 Anchor: `An access point's opening must physically pass the models that use it. With the component in its open position, if a model cannot be moved through the opening, that component is decorative for that model and has no gameplay effect (CMP-009, CMP-010; `09-transport.md`, TRN-007).` Append the following sentence to the end of that paragraph, in the same paragraph:

> What must pass is the model's Unit Base, not the loose plastic — which is what makes the check a measurement rather than an attempt.

  The sentence carries no `CORE-001` citation on purpose: the paragraph already ends in `` `09-transport.md`, TRN-007 ``, and `scripts/lint_ruleset.py` would pair that filename with the next `(RULE-ID)` on the line. `CORE-001` is cited twice more in the same rule, two paragraphs below.

### 4.2 `CMP-018` — height becomes a measured value

- [x] 4.2.1 Anchor: the paragraph beginning `**Height** has no Unit Base`. Replace that whole paragraph — one paragraph only, from `**Height**` to `...and is still not a door.` — with:

> **Height** is measured the same way. The Unit Base's vertical projection is 4 studs by 12 plate layers (`02-core-rules.md`, CORE-001), so an opening that passes infantry must be at least that clear. A minifigure on its base stands about 4 bricks tall, which is where those 12 plate layers come from. A model taller than one Unit Base is measured by its own height in plate layers.
>
> Measure the *clear* opening rather than the nominal frame: an element hanging in the doorway reduces it exactly as much as the frame does — see `15-geometry-layers.md` (GEO-004). Anything protruding beyond the model's own Unit Base is repositioned; the doorway is measured against the Unit Base either way. A hinged 1 × 2 tile covers an opening less than one brick high, which is why it moves and is still not a door.

  **Two paragraphs, and no "whatever the minifigure carries" clause.** The **Width** paragraph directly above already carries that clause, and the rule already has a paragraph opening "The check is made against the opening, not against the approach" — a second one opening the same way reads as a restatement. The minifigure's 4 bricks stay here because `CORE-001` cites this rule for them.

- [x] 4.2.2 Change nothing else in `CMP-018`. The **Width** paragraph, the opening-versus-approach paragraph, the declared-function paragraph and the closing line all stay exactly as they are.

---

## 5. `docs/15-geometry-layers.md`

### 5.1 `GEO-004` — the access-openings bullet

- [x] 5.1.1 Anchor: the bullet beginning `- Access openings (`05-construction-components.md`, CMP-018)`. Replace that bullet with:

> - Access openings (`05-construction-components.md`, CMP-018): the clearance an opening must provide is read from the Unit Base, but whether a given opening provides it is settled against the plastic as built — decorative elements narrowing that opening count exactly as much as structural ones.

- [x] 5.1.2 Change nothing else in `GEO-004`. The Line of Sight and Cover bullets, and both paragraphs below the list, stay as they are: they are the boundary `CORE-001` now points at, and they were already correct.

### 5.2 The Summary's list of physical checks

- [x] 5.2.1 Anchor: `- Visual Geometry still counts for direct physical checks (Line of Sight, Cover) — GEO-004.` Replace that line with:

> - Visual Geometry still counts for direct physical checks (Line of Sight, Cover, access openings) — GEO-004.

- [x] 5.2.2 Change nothing else in the Summary. `GEO-001`, `GEO-002`, `GEO-003` and `GEO-005` are untouched: interior fittings that reduce a compartment's usable volume are Gameplay Geometry under `GEO-002`'s own test, so `GEO-003`'s list of measured values needs no amendment (`design.md`, decision 3).

---

## 6. `docs/10-weapons.md`

### 6.1 `WPN-004` — Platform Length is horizontal

- [x] 6.1.1 Anchor: `Platform Length is the largest dimension of the Unit Base or vehicle carrying the weapons.` Replace that line with:

> Platform Length is the largest **horizontal** dimension of the Unit Base or vehicle carrying the weapons. A Unit Base is a volume — see `02-core-rules.md` (CORE-001) — and this reads its horizontal projection, so infantry's Platform Length stays 4 studs and the Unit Base's 12 plate layers of height never enter the calculation.

- [x] 6.1.2 Change nothing else in `WPN-004`. Every example and every number in it — Infantry Platform Length 4, Jeep Platform Length 9 — is unchanged, and that is the point of the edit.

---

## 7. `docs/09-transport.md`

### 7.1 Purpose

- [x] 7.1.1 Anchor: `Instead, transport capacity is determined by the number of **Unit Bases (UB)** available inside the vehicle.` Replace that line with:

> Instead, transport capacity is the **Unit Base (UB)** volume available inside the vehicle.

### 7.2 `TRN-001` — the definition pointer, and fractional cargo

- [x] 7.2.1 Anchor: `Every transported object occupies one or more Unit Bases (UB) — see `02-core-rules.md` (CORE-001) for the Unit Base definition (4 × 3 studs).` Replace that line with:

> Every transported object occupies Unit Base volume — one or more whole Unit Bases, or a share of one where the object is cargo shorter than a Unit Base (TRN-013). See `02-core-rules.md` (CORE-001) for the Unit Base definition: a volume of 4 × 3 studs by 12 plate layers.

- [x] 7.2.2 Anchor: `- Supply crate: 1 UB`. Replace that bullet with:

> - Supply crate: up to 1 UB (TRN-013)

- [x] 7.2.3 Leave the line `This represents the minimum operational space required by the object.` unchanged. It is what `CORE-001` cites when it says a Unit Base is no taller than it has to be, and it stays true of a crate occupying a third of one.

### 7.3 `TRN-002` — minifigures never share

- [x] 7.3.1 Anchor: `Changing posture never changes transport capacity.` Insert the following as a new paragraph immediately **after** that line and **before** the closing `---`:

> A Unit Base is a volume, and cargo may divide one (TRN-013) — see `02-core-rules.md` (CORE-001). A minifigure never does: no Unit Base is shared with one, even when a seated model physically leaves room above it. The space was paid for on embarking (TRN-005).

### 7.4 `TRN-003` — capacity is a volume

- [x] 7.4.1 Replace the entire body of `TRN-003` — everything between the `# TRN-003 — Cargo Capacity` heading and the `---` that ends the rule — with:

> A transport vehicle's capacity is the Unit Base volume available inside its cargo compartment — see `02-core-rules.md` (CORE-001).
>
> Count the Unit Bases its floor holds, then check its clearance (TRN-019): a position with less than 12 plate layers above it is a partial Unit Base, not a whole one.
>
> A load is measured against that volume:
>
> - Infantry counts one whole Unit Base apiece, and never shares (TRN-002).
> - Cargo counts its own height, and several objects may share one Unit Base (TRN-013).
>
> Example:
>
> Cargo bay:
>
> 2 × 4 UB, 12 plate layers of clearance
>
> Capacity:
>
> 8 UB
>
> Possible loads:
>
> - 8 infantry
> - 4 infantry + 1 light walker (2 UB) + 2 UB of cargo
> - 6 infantry + six ammo crates of 4 plate layers each — three crates fill one Unit Base, so six fill two
> - Any legal combination occupying no more than 8 UB

### 7.5 `TRN-005` — a free Unit Base is free in three dimensions

- [x] 7.5.1 Anchor: `- A free Unit Base must exist inside the transport.` Replace that bullet with:

> - A free Unit Base must exist inside the transport — free as a volume, so the compartment's clearance must admit it (TRN-019).

- [x] 7.5.2 Change nothing else in `TRN-005`. The Action Point cost is unchanged.

### 7.6 `TRN-013` — cargo divides a Unit Base

- [x] 7.6.1 Replace the entire body of `TRN-013` — everything between the `# TRN-013 — Cargo` heading and the `---` that ends the rule — with:

> Cargo occupies Unit Bases, and unlike infantry it may share one.
>
> A Unit Base divides into **slices**. A slice measures 4 × 3 studs by the height of the object standing in it, and the slices sharing one Unit Base may total no more than 12 plate layers — see `02-core-rules.md` (CORE-001).
>
> - An object **narrower** than 4 × 3 studs still takes a whole slice: the horizontal footprint is already spent, so sharing is only ever vertical.
> - An object **wider or longer** than one Unit Base takes a slice of its own height in every Unit Base its footprint covers.
>
> | Cargo | Footprint | Height | Space |
> |---|---|---|---|
> | Ammo crate | 1 UB | 4 plate layers | ⅓ UB |
> | Fuel drum pallet | 1 UB | 8 plate layers | ⅔ UB |
> | Drone | 1 UB | 12 plate layers | 1 UB |
> | Motorbike | 2 UB | 12 plate layers | 2 UB |
> | Walker | 2 UB or more | 12 plate layers | its footprint |
>
> Footprints and heights are read from the model like every other measured value; the figures above are examples, not assignments.
>
> Three ammo crates of 4 plate layers therefore fill one Unit Base exactly. A crate and a minifigure never share one: the minifigure occupies a whole Unit Base standing or seated (TRN-002), and 4 + 12 plate layers does not fit in 12.
>
> Cargo and passengers compete equally for transport space.

### 7.7 Add `TRN-019` — Interior Clearance

- [x] 7.7.1 Insert the following **after** `TRN-018`'s closing `---` and **before** the `# Summary` heading:

> # TRN-019 — Interior Clearance
>
> A Unit Base is 12 plate layers tall, and what must fit inside a vehicle is the Unit Base itself rather than the loose model (`02-core-rules.md`, CORE-001; `04-construction-standard.md`, SCS-005). A closed compartment offering less than 12 plate layers of clear height therefore holds no whole Unit Base.
>
> Clearance is measured from the surface a model stands or sits on, upward to whatever is above it. That surface is the model's floor, not an obstruction: a bench 3 plate layers high needs 12 clear layers *above the bench*. Seating raises the roof a compartment needs rather than shrinking its occupant — which is what TRN-017 already means by "benches reduce available cargo space".
>
> Everything else physically in the way does count: a roof, a beam, a rack, a pipe. An element that reduces a compartment's usable volume is modifying Gameplay Geometry, not decorating it — see `15-geometry-layers.md` (GEO-002) — whatever it looks like.
>
> - **Infantry and crew need the full 12 plate layers.** An infantry model occupies exactly one Unit Base whether standing or seated (TRN-002), and a crew member occupies one like any other passenger (TRN-014). A compartment shorter than that carries neither.
> - **Cargo needs only its own height.** Cargo divides a Unit Base (TRN-013), so a compartment 9 plate layers high carries cargo up to 9 plate layers — three quarters of a Unit Base per position.
>
> A low closed transport is therefore not an illegal model. It is a freight hull rather than a troop hull.
>
> A position with no roof over it has nothing above to measure against, so no clearance applies there. Where an enclosure is incomplete enough that its occupants stay visible, the transport is open by TRN-009's own test, and its passengers are targetable, able to attack, and without the hull protection TRN-010 gives them. The builder pays in survivability rather than in a legality ruling.
>
> **What this costs an existing model.** A closed compartment built under 12 plate layers stops carrying infantry, and that includes a closed cockpit: a Pilot with no Unit Base is no Pilot, and a vehicle without a Pilot cannot move — see `08-vehicles.md` (VEH-013). Raising the roof by a plate or two, or opening it, is the whole repair.
>
> ---

### 7.8 Add `TRN-020` — Interior Levels

- [x] 7.8.1 Insert the following immediately **after** the `---` that task 7.7.1 wrote at the end of `TRN-019`, and **before** the `# Summary` heading:

> # TRN-020 — Interior Levels
>
> A vehicle may stack interior levels, and each level above the lowest must pay for its own floor.
>
> N levels require:
>
> ```
> 12N + (N − 1) plate layers
> ```
>
> measured above the lowest interior floor.
>
> | Levels | Plate layers | Bricks |
> |---|---|---|
> | 1 | 12 | 4 |
> | 2 | 25 | 8 + 1 plate |
> | 3 | 38 | 12 + 2 plates |
>
> The `(N − 1)` term is the intermediate floors at their thinnest, one plate each; a floor built thicker costs what it actually measures. The lowest level rests on the vehicle's own hull and pays nothing for it — which is why a vehicle exactly 8 bricks tall does not hold two levels. It is one plate short.
>
> Each level is a cargo compartment like any other: its capacity is read from TRN-003 and its clearance from TRN-019.
>
> ---

### 7.9 The transport Summary

- [x] 7.9.1 Anchor: `3. Transport capacity equals the number of available Unit Bases.` Replace the whole numbered list — items 1 to 8 — with:

> 1. Everything occupies Unit Bases.
> 2. Infantry always occupies exactly 1 UB, and never shares it.
> 3. Transport capacity is the Unit Base volume available inside, and cargo may share a Unit Base.
> 4. A closed compartment shorter than 12 plate layers carries cargo but no infantry, crew included.
> 5. Embarking costs 1 AP per occupied Unit Base.
> 6. Disembarking costs 1 AP per occupied Unit Base.
> 7. Open transports expose passengers.
> 8. Closed transports protect passengers.
> 9. Interior design is part of gameplay.

- [x] 7.9.2 Leave the closing `> **Every Brick Matters.**` line and the `---` above it unchanged.

---

## 8. `docs/14-glossary.md`

### 8.1 `UB`

- [x] 8.1.1 Anchor: `4 × 3 studs.` (one occurrence in this file, inside the `## UB` entry). Replace the three lines `Unit Base.`, `The universal measurement of StudCraft.` and `4 × 3 studs.` — leaving the `## UB` heading and the `---` separator in place — with:

> Unit Base.
>
> The universal measurement of StudCraft: a volume 4 studs wide, 3 studs deep and 12 plate layers tall. See `02-core-rules.md` (CORE-001) for the projections a rule reads it through.

### 8.2 `Platform Length`

- [x] 8.2.1 Anchor: `The largest dimension of a platform's Unit Base or vehicle bounding box.` Replace that line with:

> The largest horizontal dimension of a platform's Unit Base or vehicle bounding box. The Unit Base's height is not a candidate. See `10-weapons.md` (WPN-004).

### 8.3 `Cargo Bay`

- [x] 8.3.1 Anchor: `The interior space of a transport vehicle, measured in Unit Bases, used to carry passengers and cargo.` Replace that line with:

> The interior space of a transport vehicle, measured in Unit Bases, used to carry passengers and cargo. A closed bay with less than one Unit Base of clearance carries cargo but no infantry. See `09-transport.md` (TRN-019).

### 8.4 Three new entries

- [x] 8.4.1 Add the following three entries at the **end** of the definitions, immediately after the `## Access Opening` entry and its `---` separator, and **before** the closing `> **Every Brick Matters.**` line. The glossary is in append order, not alphabetical — verify by reading it, then follow it. Match the surrounding style: a `## ` heading, one paragraph, a document-and-ID citation, then a `---` separator.

> ## Interior Clearance
>
> The clear height inside a closed compartment, measured in plate layers from the surface a model stands or sits on. Less than 12 plate layers — one Unit Base — carries cargo but no infantry. See `09-transport.md` (TRN-019).
>
> ---
>
> ## Slice
>
> The share of a Unit Base one cargo object occupies: 4 × 3 studs by that object's own height. Slices sharing a Unit Base may total no more than 12 plate layers, and infantry never occupies a slice — it occupies the whole Unit Base. See `09-transport.md` (TRN-013).
>
> ---
>
> ## Projection
>
> The reading of the Unit Base volume a rule takes: horizontal for distance, deployment and footprints; the whole volume for transport capacity; vertical for passing an opening. A projection is a measured value and never replaces a physical check. See `02-core-rules.md` (CORE-001).

---

## 9. `README.md` and `CODE_OF_DESIGN.md`

Neither file is a ruleset document, and neither may state a rule of its own (`system/documentation-standards.md`). Both currently restate the two-dimensional definition, so both become pointers.

### 9.1 `README.md`

- [x] 9.1.1 Anchor: `One Unit Base measures:` (one occurrence in this file). Replace the three lines `The universal measurement of the game.`, `One Unit Base measures:` and `**4 × 3 studs**` — leaving the `## Unit Base (UB)` heading in place — with:

> The universal measurement of the game.
>
> One Unit Base is a volume:
>
> **4 studs wide × 3 studs deep × 12 plate layers tall**
>
> — defined by `docs/02-core-rules.md` (CORE-001), which is the authority on its dimensions, its orientation and which projection a rule reads.

- [x] 9.1.2 Leave the line `Everything is measured using Unit Bases.` unchanged.

### 9.2 `CODE_OF_DESIGN.md` — Principle 7

- [x] 9.2.1 Anchor: `One Unit Base measures:` (one occurrence in this file). Replace the two lines `One Unit Base measures:` and `**4 × 3 studs**` with:

> One Unit Base is a volume:
>
> **4 studs wide × 3 studs deep × 12 plate layers tall**

- [x] 9.2.2 Leave the line beginning `— defined by `docs/02-core-rules.md` (CORE-001)` unchanged. It already points at the authority, which is why this file needs no other edit.

---

## 10. Archive-order dependency — record it, do not act on it

- [x] 10.1 `openspec/changes/access-openings-must-pass-the-model/specs/geometry-layers/spec.md` is applied to `docs/` but not archived. Its `MODIFIED` requirement describes access openings as "whether an access point's opening **passes the models that use it**" — the framing this change replaces with a measurement against the Unit Base. **That change must be archived before this one**, or its delta reconciled against the new `CMP-018` text first (`system/workflow.md`, "Refresh every delta against `docs/` before archiving"). Do not edit that change directory from this branch — the branch may touch `docs/*.md` and this one change (`system/repository-strategy.md`, Branch Naming). Recording it here is the task.

---

## 11. Verify

Each command below was run against the pre-change files; both the pre- and the post-change values are stated.

- [x] 11.1 Run `python3 scripts/lint_ruleset.py` and confirm no structural issues. It also resolves every `(CORE-NNN)`, `(TRN-NNN)`, `(CMP-NNN)`, `(GEO-NNN)`, `(DMG-NNN)`, `(VEH-NNN)`, `(SCS-NNN)` and `(WPN-NNN)` citation added above.
- [x] 11.2 Run `grep -rcE '^#{1,2} [A-Z]{3,4}-[0-9]{3} ' docs/ | awk -F: '{s+=$2} END {print s}'` and confirm **222** — two more than the 220 before, those two being `TRN-019` and `TRN-020`.
- [x] 11.3 Run `grep -c '^# TRN-' docs/09-transport.md` and confirm **20** (18 before). Then run `grep -n '^# TRN-' docs/09-transport.md` and confirm `TRN-001` through `TRN-020` appear once each, ascending, with no gaps and with both new rules above the `# Summary` heading.
- [x] 11.4 Run `python3 scripts/check_delta_coverage.py` and confirm it passes. The `unit-base` MODIFIED requirement keeps all three of the living spec's scenarios by name (`Unit Base dimensions`, `Infantry occupies one Unit Base`, `Vehicle footprint measured in Unit Bases`) and adds a fourth; the `weapon-capacity` MODIFIED requirement keeps `Platform length from bounding box`.
- [x] 11.5 Run `openspec validate unit-base-is-a-volume` and confirm it passes.
- [x] 11.6 Run `grep -rn 'Projections' docs/` and confirm exactly one hit, in `CORE-001` (0 before). The projection table must not be restated anywhere else; the glossary's `Projection` entry is a definition with a pointer, not a copy of the table.
- [x] 11.7 Run `grep -rn 'never against a Unit Base' docs/` and confirm exactly one hit, in `CORE-001` (0 before). Without it, this change reads as licensing sight lines traced against projected volumes.
- [x] 11.8 Run `grep -rln '12 plate layers' docs/` and confirm exactly six files: `01-foundations.md`, `02-core-rules.md`, `05-construction-components.md`, `09-transport.md`, `10-weapons.md` and `14-glossary.md` (0 files before). `06-deployment.md`, `07-movement.md`, `08-vehicles.md` and `04-construction-standard.md` must not appear — they read the horizontal projection or cite the rule instead of quoting the figure.
- [x] 11.9 Run `grep -rn 'cannot move' docs/09-transport.md docs/08-vehicles.md` and confirm the Pilot consequence is stated in `TRN-019` and in `VEH-013`'s own pre-existing text, and nowhere else — `VEH-015`, `TRN-014` and `CMP-013` must not restate it.
- [x] 11.10 Run `git diff --stat main...HEAD` and confirm exactly these paths changed: the twelve files listed under **Scope**, plus the five files under `openspec/changes/unit-base-is-a-volume/`. `CHANGELOG.md`, every `**Version:**` header and `openspec/specs/` must be absent.
- [x] 11.11 Confirm no Action Point cost and no existing numeric value changed anywhere in `docs/`. `WPN-004`'s Platform Lengths (4, 9), `TRN-005`/`TRN-006`'s 1 AP per Unit Base and `TRN-003`'s 8 UB example are all unchanged; the plate-layer figures are new text, not changed values.

---

## 12. Verify only — make no edit

- [x] 12.1 `MOVE-002`, `MOVE-005` and `MOVE-006` are untouched. Step sizes read the Unit Base's width and depth, and neither moves (`design.md`, Verified unaffected).
- [x] 12.2 `DEP-001`, `DEP-003` and `DEP-009` are untouched. Deployment is planar in its own words and inherits the projection principle from `CORE-001`.
- [x] 12.3 `CORE-004`, `VEH-001` and `VEH-013` are untouched. "Occupies two or more Unit Bases" is a horizontal reading, settled once in `CORE-001`; `VEH-013` already says a vehicle without a Pilot cannot move, and `TRN-019` cites it rather than amending it.
- [x] 12.4 `SCS-014`, `CMP-013` and `TRN-014` are untouched. All three were already the volumetric reading and become literally true without an edit.
- [x] 12.5 `GEO-001`, `GEO-002`, `GEO-003` and `GEO-005` are untouched. `GEO-001`'s pointer to `WPN-004` stays as it is — adding "horizontal" there would make three documents state the same qualification (`design.md`, Rejected).
- [x] 12.6 The `(4 × 3 studs)` pointers in `04-construction-standard.md`, `06-deployment.md`, `07-movement.md` and `08-vehicles.md` are untouched. Each quotes the horizontal figures in a horizontal context.
- [x] 12.7 `TRN-009`, `TRN-010` and `TRN-015` are untouched. `TRN-019` cites the open/closed distinction rather than amending it, and keys its own exemption on the roof rather than on `TRN-009`'s visibility test.
- [x] 12.8 No `geometry-layers` spec delta is written (`design.md`, Rejected; `system/workflow.md`, "When several changes modified the same requirement").
- [x] 12.9 `TODO.md` is not edited. This change closes no gap that `TODO.md` records, and declares none.
