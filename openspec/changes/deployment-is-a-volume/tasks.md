# Tasks — The Deployment Area is a volume

## 0. Setup

- [x] 0.1 Work on branch `deployment-is-a-volume` (`openspec/config.yaml` requires one branch per proposal, and `system/repository-strategy.md` requires the branch to be named for the change). The branch already exists and is checked out; do not create another and do not leave it.

### How to read the replacement blocks

Every anchor and every replacement is given inside a fenced block. **The fence is not
part of the text.** Inline backticks, em dashes (`—`), `×` and the bold `**` markers
are part of the text — write them exactly.

Task 2.2 and task 2.3 use a **four-backtick** fence because their content contains a
markdown table or a heading; the four-backtick lines are not part of the text either.
A `#` heading or a `|` table inside a block is real markdown, not quoted text.

Unless a task says otherwise, it replaces one paragraph with one paragraph and adds no
blank line.

### Headings

**Three rule headings change their title in this change** — `DEP-001`, `VEH-028` and
`VEH-029`. Their **rule IDs do not change**, and no rule is added, removed or
renumbered anywhere. Those three are the only headings any task touches; every other
heading in every file stays exactly as it is.

Two glossary entries are **deleted outright**, heading and body: *Maximum Height* and
*Base Plane*. Glossary headings are `##` and are not rule IDs.

### The term

`Deployment Area` becomes **`Deployment Volume`** everywhere it appears, in seven
documents and the image index — and four further sites say *deployment* is read
horizontally, in lower case, which tasks 3.3, 3.4, 5.4 and 9.1 repair. Do not shorten it, do not write "Deployment volume", and do not leave a
plural "Deployment Areas" behind. Every site is given its own task below with its own
anchor — do not run a global find-and-replace, because three sites also change their
surrounding sentence.

### Anchors

Every anchor below was checked with exact-substring matching against the pre-change
file and occurs exactly **once** in it. Several sites in `docs/06-deployment.md`
repeat the same short phrase, so their anchors carry surrounding lines to be unique —
replace the whole anchor, including those lines.

If an anchor returns anything other than 1, **stop and report it** rather than
guessing which occurrence was meant.

### Citation form

`scripts/lint_ruleset.py` pairs a backticked filename with any **parenthesised** rule
ID that follows it within 80 characters and resolves that ID against that file. Every
citation added below is the comma form (`` `06-deployment.md`, DEP-001 ``) or a
parenthesised ID that resolves in its own file. Do not convert one form to the other.

### Scope and coverage

Nine ruleset documents, the image index and one spec delta: **46 edits**. Twenty-two
of them change nothing but the term; the other twenty-four change what a rule says,
so read each one's replacement rather than assuming it is mechanical.

| `proposal.md` item | Task | Path |
|---|---|---|
| `DEP-001` agrees a volume | 1.2, 1.3 | `docs/06-deployment.md` |
| `DEP-002` fits an army in three dimensions | 1.4, 1.5 | `docs/06-deployment.md` |
| `DEP-003`'s footprint no longer bounds height | 1.6 | `docs/06-deployment.md` |
| The term, everywhere else in `06-deployment.md` | 1.1, 1.7, 1.8, 1.9, 1.10, 1.11, 1.12, 1.13, 1.14, 1.15, 1.16 | `docs/06-deployment.md` |
| `VEH-028` keeps its ID and loses its content | 2.2 | `docs/08-vehicles.md` |
| `VEH-029` stops being the Base Plane | 2.3 | `docs/08-vehicles.md` |
| `VEH-030` keeps its test, changes its datum | 2.4, 2.5, 2.6 | `docs/08-vehicles.md` |
| `VEH-001` and the vehicles Summary | 2.1, 2.7 | `docs/08-vehicles.md` |
| `CORE-001` stops pointing at a height bound | 3.1 | `docs/02-core-rules.md` |
| `CORE-005`'s structure caveat takes the new term | 3.2 | `docs/02-core-rules.md` |
| `TRN-020` reads the ceiling | 4.1 | `docs/09-transport.md` |
| Glossary: *Deployment Volume*, minus two retired entries | 5.1, 5.2, 5.3 | `docs/14-glossary.md` |
| The term in the remaining documents | 6.1, 7.1, 8.1, 8.2 | `04`, `10`, `03` |
| Deployment stops being a horizontal reading | 3.3, 5.4, 9.1 | `02`, `14`, `01` |
| `DEP-009`'s scenarios gain their ceilings | 1.12, 1.13, 1.14 | `docs/06-deployment.md` |
| `06-deployment.md` stops calling occupied space the cost | 1.17, 1.18 | `docs/06-deployment.md` |
| `VEH-030`'s orphaned footprint sentence | 2.8 | `docs/08-vehicles.md` |
| The image index follows the rules it briefs | 10.1 – 10.7 | `assets/IMAGES.md` |
| The `unit-base` capability's projections requirement | delta | `openspec/changes/deployment-is-a-volume/specs/unit-base/spec.md` |

**Untouched, deliberately.** `DEP-003`'s charge (Unit Bases covered) and `DEP-004`'s
(one per infantry model) are unchanged — only their wording of the term and
`DEP-003`'s closing paragraph change. `VEH-022`, `VEH-023` and `VEH-024` keep every
word: Terrain Thresholds are still read from locomotion, and this change alters what
locomotion costs, not how it is measured. `CHANGELOG.md`, every `**Version:**` header
and `openspec/specs/` are untouched — the spec **delta** lives inside this change
directory, at `specs/unit-base/spec.md`, and is already written; no task edits it.

---

## 1. `docs/06-deployment.md`

- [x] 1.1 In the Design Philosophy, replace this anchor:

```
Every vehicle and infantry model occupies space; a scenario-placed structure's Deployment Area occupation is not yet defined (`02-core-rules.md`, CORE-005).
```

with:

```
Every vehicle and infantry model occupies space; a scenario-placed structure's Deployment Volume occupation is not yet defined (`02-core-rules.md`, CORE-005).
```

- [x] 1.2 Replace this heading — **the rule ID `DEP-001` does not change**, only the title after the em dash:

```
# DEP-001 — Deployment Area
```

with:

```
# DEP-001 — Deployment Volume
```

- [x] 1.3 Replace `DEP-001`'s entire body — everything between that heading and the `---` that ends the rule. Six paragraphs and a list become seven paragraphs and a list:

```
Before the game begins, players agree on a Deployment Area.

A Deployment Area is measured in **Unit Bases (UB)** — see `02-core-rules.md` (CORE-001) for the Unit Base definition (4 × 3 studs).

Deployment Areas may have any dimensions agreed upon by the players.

Examples:

- 5 × 1 UB
- 5 × 5 UB
- 10 × 10 UB
- Scenario-defined areas
```

with:

```
Before the game begins, players agree on a Deployment Volume.

A Deployment Volume is measured in **Unit Bases (UB)** — see `02-core-rules.md` (CORE-001) for the Unit Base definition — and is written `W × D × H`: a floor `W × D`, and the height `H` every model in a player's army must fit under.

Where only two numbers are agreed, the ceiling is one Unit Base. That is also the lowest a Deployment Volume can be: infantry occupies exactly one Unit Base (`09-transport.md`, TRN-002), so a shorter one admits no army at all.

A one-Unit-Base ceiling is an infantry game, and deliberately so. A powered vehicle carries a Pilot occupying a Unit Base of its own (`08-vehicles.md`, VEH-013), that Unit Base needs a Unit Base of clear height above the surface it sits on (`09-transport.md`, TRN-019), and the floor and the locomotion beneath it are height as well — so no powered vehicle fits under a ceiling of one. Players who want vehicles agree a taller volume.

Deployment Volumes may have any dimensions agreed upon by the players.

Examples:

- 5 × 1 UB — two numbers, so one Unit Base tall: infantry only
- 5 × 5 × 4 UB
- 10 × 10 × 6 UB
- Scenario-defined volumes

A low ceiling is a scenario choice rather than an oversight. Tunnels, hangars, cargo holds and fights inside a hull are agreed here, by choosing a smaller `H`, and need no rule of their own.
```

- [x] 1.4 In `DEP-002`, replace this anchor:

```
A player's army may occupy any combination of models that physically fits inside the agreed Deployment Area.
```

with:

```
A player's army may occupy any combination of models that physically fits inside the agreed Deployment Volume — on its floor and under its ceiling. A model's height is read the way `08-vehicles.md` (VEH-028) reads a vehicle's: from the surface it rests on to the top of its Gameplay Geometry.
```

- [x] 1.5 In `DEP-002`'s example, replace this anchor:

```
A 5 × 5 UB Deployment Area could contain:
```

with:

```
A 5 × 5 × 4 UB Deployment Volume could contain:
```

- [x] 1.6 In `DEP-003`, replace this anchor — the rule's closing paragraph:

```
That same footprint bounds the vehicle's height: 6 plate layers for every stud of its narrowest side (`08-vehicles.md`, VEH-028). Where an outline is not rectangular the height is read from the smallest rectangle of Unit Bases enclosing it, which never changes what is charged here.
```

with:

```
The footprint is what this rule charges, and it bounds nothing else. How tall a vehicle may build is settled by the ceiling of the agreed Deployment Volume (DEP-001; `08-vehicles.md`, VEH-028), not by the space it covers.
```

- [x] 1.7 In `DEP-004`, replace this anchor — **two occurrences of the term in one paragraph**:

```
Each infantry model occupies 1 Unit Base (`02-core-rules.md`, CORE-003). Deployed individually, this UB counts against the Deployment Area; already embarked inside a transport, it counts only against the transport's own interior UB (DEP-006) — not as additional Deployment Area.
```

with:

```
Each infantry model occupies 1 Unit Base (`02-core-rules.md`, CORE-003). Deployed individually, this UB counts against the Deployment Volume; already embarked inside a transport, it counts only against the transport's own interior UB (DEP-006) — not as additional Deployment Volume.
```

- [x] 1.8 In `DEP-006`, replace this anchor:

```
Their occupied space is the transport interior, not additional Deployment Area.
```

with:

```
Their occupied space is the transport interior, not additional Deployment Volume.
```

- [x] 1.9 In `DEP-006`'s example, replace this anchor:

```
The infantry do not consume additional Deployment Area while embarked.
```

with:

```
The infantry do not consume additional Deployment Volume while embarked.
```

- [x] 1.10 In `DEP-006`, replace this anchor:

```
The waiver is for **embarked** units. A model carried on the outside — on a roof, a bonnet, a hull top or the outside of a turret — is not embarked, so it is deployed individually and costs Deployment Area of its own: one Unit Base for an infantry model (DEP-004), its own footprint for a vehicle (DEP-003).
```

with:

```
The waiver is for **embarked** units. A model carried on the outside — on a roof, a bonnet, a hull top or the outside of a turret — is not embarked, so it is deployed individually and costs Deployment Volume of its own: one Unit Base for an infantry model (DEP-004), its own footprint for a vehicle (DEP-003).
```

This anchor is the first two sentences of that paragraph only. The rest of the
paragraph, which ends "counts toward the carrier's height as well
(`08-vehicles.md`, VEH-030)", is unchanged and stays where it is.

- [x] 1.11 Replace this anchor:

```
As long as the Deployment Area is respected, all armies are legal.
```

with:

```
As long as the Deployment Volume is respected, all armies are legal.
```

- [x] 1.12 In `DEP-009`, replace this anchor — **the Patrol entry, three lines with their blank lines**:

```
## Patrol

Deployment Area:

5 × 1 UB
```

with:

```
## Patrol

Deployment Volume:

5 × 1 × 2 UB
```

- [x] 1.13 In `DEP-009`, replace this anchor:

```
## Skirmish

Deployment Area:

5 × 5 UB
```

with:

```
## Skirmish

Deployment Volume:

5 × 5 × 4 UB
```

- [x] 1.14 In `DEP-009`, replace this anchor:

```
## Battle

Deployment Area:

10 × 10 UB
```

with:

```
## Battle

Deployment Volume:

10 × 10 × 6 UB
```

- [x] 1.15 In `DEP-009`'s Massive Battle entry, replace this anchor:

```
Any agreed Deployment Area.
```

with:

```
Any agreed Deployment Volume.
```

- [x] 1.16 In the Summary, replace this anchor — **two of the four numbered items**:

```
2. Vehicles consume space according to their footprint.
3. Transport capacity depends on physical interior volume.
4. Embarked units do not consume additional Deployment Area.
```

with:

```
2. Vehicles consume floor space according to their footprint, and must fit under the agreed ceiling.
3. Transport capacity depends on physical interior volume.
4. Embarked units do not consume additional Deployment Volume.
```

Item 3 is unchanged and is included only to make the anchor unambiguous. The list
still has four items and the sentence introducing it still says four.

- [x] 1.17 In the Design Philosophy, replace this anchor:

```
That occupied space becomes the cost of including the model.
```

with:

```
The floor that space covers becomes the cost of including the model. Its height is not charged: how tall a model may be is a ceiling both players agreed to (DEP-001), not a price one of them pays.
```

- [x] 1.18 In the Design Notes, replace this anchor:

```
Players pay for larger units by sacrificing deployment capacity.
```

with:

```
Players pay for wider units by sacrificing floor space, and for taller ones by having to agree a Deployment Volume that admits them.
```

---

## 2. `docs/08-vehicles.md`

- [x] 2.1 In `VEH-001`, replace this anchor:

```
No maximum vehicle size exists. The footprint does bound how high the vehicle may build on it — 6 plate layers for every stud of its narrowest side (VEH-028) — but no dimension of the footprint itself is capped.
```

with:

```
No maximum vehicle size exists, and the footprint bounds no dimension of its own. How tall a vehicle may build is settled by the ceiling of the agreed Deployment Volume (`06-deployment.md`, DEP-001; VEH-028).
```

- [x] 2.2 Replace `VEH-028` — **its heading title and its entire body**, from the heading to the `---` that ends the rule. The rule ID does not change. Four-backtick fences; the `#` heading and the `|` table inside are real markdown:

````
# VEH-028 — Maximum Height

A vehicle's footprint (VEH-001) governs how high it may build, as well as how much Deployment Area it costs (`06-deployment.md`, DEP-003).

**For every stud across the narrowest side of its footprint, a vehicle may rise 6 plate layers.**

The footprint is the Unit Bases the vehicle covers — the ones DEP-003 charges. Written `A × B` UB it measures `4A × 3B` studs (`02-core-rules.md`, CORE-001), so its narrowest side is the smaller of those two numbers. Where an outline is not rectangular, read `A × B` as the smallest rectangle of Unit Bases enclosing it. That rectangle serves this measurement only and changes no vehicle's Deployment Area, which DEP-003 still charges per Unit Base actually covered.

Six plate layers is two standard bricks, and one Unit Base of height for every two studs (CORE-001). The limit is stated in plate layers because that is the unit VEH-021 already uses for vertical distance, and because a hull with plates in it reaches heights no whole brick count expresses: a vehicle 22 plate layers tall is legal where the limit is 24, and no count of bricks says so.

The multiplier is read off the Unit Base rather than chosen. A Unit Base is 12 plate layers tall on a narrowest side of 3 studs — 4 plate layers for every stud, which is the proportion of the volume one person occupies (CORE-001). A vehicle is allowed half as much again. That is this rule's only design decision.

Footprints below are VEH-001's; only the two right-hand columns belong to this rule.

| Vehicle | Footprint | Studs | Narrowest side | Maximum Height |
|---|---|---|---:|---:|
| Bike | 1 × 2 UB | 4 × 6 | 4 | 24 plate layers (8 bricks) |
| Buggy | 2 × 2 UB | 8 × 6 | 6 | 36 plate layers (12 bricks) |
| Jeep | 2 × 3 UB | 8 × 9 | 8 | 48 plate layers (16 bricks) |
| Tank | 2 × 5 UB | 8 × 15 | 8 | 48 plate layers (16 bricks) |
| Heavy Transport | 3 × 8 UB | 12 × 24 | 12 | 72 plate layers (24 bricks) |

Tank and Jeep share a limit because they share a narrowest side. Stretching a vehicle along its long axis buys it nothing: a long thin vehicle is still a thin vehicle.

The same two Unit Bases give different limits depending on how they are arranged — side by side (2 × 1 UB, 8 × 3 studs) they allow 18 plate layers, front to back (1 × 2 UB, 4 × 6 studs) 24. That is not an exploit to close. The arrangement is built into the model, chosen once at the bench and paid for in the shape of the vehicle. Turning the finished model on the table changes nothing, because the narrowest side is a property of the rectangle and not of which way it points.

A vehicle taller than its Maximum Height is not a legal vehicle. It cannot be deployed until it is rebuilt, either by lowering the construction or by widening the footprint, which raises the limit. There is no penalty, no marker and no in-game state: this is a construction check made once before the game, exactly like the two-Unit-Base minimum (`02-core-rules.md`, CORE-004; VEH-013). Legality is settled before deployment and never revisited, so a vehicle whose construction is altered in play (VEH-018) is not measured again.

This caps no dimension of its own. VEH-001's "No maximum vehicle size exists" stays true as written — a footprint may be any size, and the height allowed grows with it. What this rule fixes is the relationship between the two, and it introduces no height statistic, vehicle class or size category to do it.

It also bounds how many interior levels a footprint carries, while saying nothing about capacity. Each level needs one Unit Base of clear height and each floor above the lowest a plate of its own (`09-transport.md`, TRN-020), so a vehicle 4 studs across has room for one level, 8 studs for three, and 12 studs for five. A wide vehicle may still stack decks; a narrow one cannot.
````

with:

````
# VEH-028 — Height

A vehicle may be built to any height that fits under the ceiling of the agreed Deployment Volume (`06-deployment.md`, DEP-001).

The footprint bounds nothing here. A narrow vehicle may be as tall as a wide one, and turning or stretching a footprint changes no height: what a vehicle may reach is the height both players agreed to before the game, and it is the same height for every model on the table.

Height is counted from the surface the vehicle rests on (VEH-029) to the top of its Gameplay Geometry (VEH-030) — **locomotion included**. A walker's legs, a wheel's diameter and a hover assembly occupy the ceiling exactly as a hull does: they are what holds the rest of the model up there.

A vehicle taller than the ceiling is not a legal vehicle. It cannot be deployed until it is rebuilt, or until the players agree a taller volume. There is no penalty, no marker and no in-game state: this is a construction check made once before the game, exactly like the two-Unit-Base minimum (`02-core-rules.md`, CORE-004; VEH-013). Legality is settled before deployment and never revisited, so a vehicle whose construction is altered in play (VEH-018) is not measured again.

This rule caps nothing of its own. VEH-001's "No maximum vehicle size exists" stays true as written, and no height statistic, vehicle class or size category is introduced: the size of the game is agreed by the players, and every model is measured against that agreement rather than against a figure this ruleset invents.

How many interior levels a vehicle carries follows from the same ceiling rather than from its footprint — each level needs one Unit Base of clear height, and each floor above the lowest a plate of its own (`09-transport.md`, TRN-020).
````

- [x] 2.3 Replace `VEH-029` — **its heading title and its entire body**, from the heading to the `---` that ends the rule. The rule ID does not change. Four-backtick fences; the `#` heading inside is real markdown:

````
# VEH-029 — Base Plane

Maximum Height (VEH-028) is counted from the vehicle's own **Base Plane**: the lowest surface on which one of its Unit Bases rests — its interior floor. Where a vehicle has floors at several heights, the lowest governs. It is the same surface interior levels are measured from (`09-transport.md`, TRN-020).

A powered vehicle always has one, because it carries a Pilot occupying a Unit Base of its own (VEH-013; `09-transport.md`, TRN-014), and that Unit Base rests on something. A vehicle with no Pilot and no interior — a trailer, a towed gun, an open flatbed — takes its lowest structural floor instead: the surface its load rests on.

The Base Plane is a property of the model, not of the table. A vehicle on a hill, in a depression or part-way up a ramp measures exactly as it does on flat ground, so terrain elevation never changes what is legal. A vehicle carried inside another vehicle (`09-transport.md`, TRN-001, TRN-003) is read the same way: each vehicle is measured against its own Base Plane, and the carrier's floor is the carried vehicle's ground.

**Ground clearance is not height.** Everything below the Base Plane is locomotion, measured by its own rules: a wheel by its axle (VEH-022), a leg by its knee (VEH-023), a hover assembly by its full height (VEH-024). Those rules already price height in silhouette — VEH-024 calls it "the same trade a walker makes with long legs" — and charging it twice here would make the walkers and hover vehicles they describe illegal. A long-legged walker stays legal however tall its legs. What it may not do is build a tower on top of them.

A vehicle can therefore gain reach by standing on tall locomotion instead of by building upward, and this limit never sees it. That is deliberate rather than overlooked: it is the walker VEH-023 describes, and it is paid for in silhouette (`02-core-rules.md`, CORE-008) and in legs that are components like any other, destroyed like any other (VEH-017, VEH-018). It is not paid for here.

Height is counted straight up from the Base Plane, never along a leaning element. A mast raked backwards is measured by how high it reaches, not by how long it is.
````

with:

````
# VEH-029 — Where Height Is Counted From

Height (VEH-028) is counted from **the surface the vehicle rests on when it stands on its own locomotion**. A vehicle that begins the game inside another (`09-transport.md`, TRN-001, TRN-003) is measured the same way and against the same ceiling, never from the carrier's floor: it disembarks into the agreed volume like anything else, and the check belongs to the model rather than to where it starts.

**Locomotion counts.** Everything between that surface and the top of the vehicle's Gameplay Geometry occupies the ceiling: a walker two Unit Bases tall on legs another Unit Base long takes three Unit Bases of the room, and which part of it reaches the lid changes nothing about the space it takes.

Terrain capability is still read from those same parts — a wheel by its axle (VEH-022), a leg by its knee (VEH-023), a hover assembly by its full height (VEH-024) — and tall locomotion still costs silhouette (`02-core-rules.md`, CORE-008). What it no longer buys is reach the ceiling cannot see. Reach gained by standing on long legs and reach gained by building upward are the same reach on the table, and they are paid for out of the same agreed height.

This is a check made at the bench, not on the table. A vehicle on a hill, in a depression or part-way up a ramp is not measured again: legality was settled before deployment (VEH-028), so terrain elevation never enters it.

Height is counted straight up, never along a leaning element. A mast raked backwards is measured by how high it reaches, not by how long it is.
````

- [x] 2.4 In `VEH-030`, replace this anchor:

```
Maximum Height (VEH-028) is counted to the highest point of the vehicle's **Gameplay Geometry** (`15-geometry-layers.md`, GEO-001). Visual Geometry above that point is unrestricted and never makes a vehicle illegal.
```

with:

```
A vehicle's height (VEH-028) is counted to the highest point of its **Gameplay Geometry** (`15-geometry-layers.md`, GEO-001). Visual Geometry above that point is unrestricted and never makes a vehicle illegal.
```

- [x] 2.5 In `VEH-030`, replace this anchor:

```
Height is plastic, measured above the Base Plane (VEH-029) in plate layers.
```

with:

```
Height is plastic, measured from the surface the vehicle rests on (VEH-029) in plate layers.
```

- [x] 2.6 In `VEH-030`, replace this anchor:

```
It counts toward this height, measured in the highest position it can be placed in, because it can see, be seen and be shot at (`02-core-rules.md`, CORE-008, CORE-009) — and it costs Deployment Area of its own, which `06-deployment.md` (DEP-006) owns.
```

with:

```
It counts toward this height, measured in the highest position it can be placed in, because it can see, be seen and be shot at (`02-core-rules.md`, CORE-008, CORE-009) — and it costs Deployment Volume of its own, which `06-deployment.md` (DEP-006) owns.
```

- [x] 2.7 In the Summary, replace this anchor:

```
Height is read from the footprint the same way: a vehicle may rise 6 plate layers for every stud of its footprint's narrowest side, counted from its own Base Plane and measured to the top of its Gameplay Geometry (VEH-028 through VEH-030).
```

with:

```
Height is read from the agreed Deployment Volume instead: a vehicle may be built to any height that fits under its ceiling, counted from the surface the vehicle rests on and measured to the top of its Gameplay Geometry (VEH-028 through VEH-030).
```

- [x] 2.8 In `VEH-030`, replace this anchor:

```
Access openings ask a different question, whether a model physically passes through (`05-construction-components.md`, CMP-018), and decoration obstructs passage, so it counts there. This rule asks how much functional construction one footprint carries, and a flag carries nothing.
```

with:

```
Access openings ask a different question, whether a model physically passes through (`05-construction-components.md`, CMP-018), and decoration obstructs passage, so it counts there. The agreed ceiling asks how much functional construction a model raises into the volume, and a flag raises none.
```

The old sentence said this rule "asks how much functional construction one footprint
carries". After task 2.2 the rule asks nothing about a footprint, and the sentence
would be the last place in `docs/` still claiming it does.

---

## 3. `docs/02-core-rules.md`

- [x] 3.1 In `CORE-001`, replace this anchor — the final sentence of the paragraph only:

```
A footprint is a horizontal reading, and says nothing about how tall a model actually is — though for a vehicle it does bound how tall the model may be (`08-vehicles.md`, VEH-028).
```

with:

```
A footprint is a horizontal reading, and says nothing about how tall a model actually is.
```

- [x] 3.2 In `CORE-005`, replace this anchor — the term only, in a sentence about scenario-placed structures:

```
Structures follow the Construction Standard. Structure-specific damage (collapse, breaching walls) and Deployment Area occupation for scenario-placed structures are not yet defined
```

with:

```
Structures follow the Construction Standard. Structure-specific damage (collapse, breaching walls) and Deployment Volume occupation for scenario-placed structures are not yet defined
```

This anchor is the opening of a longer sentence; everything after "are not yet
defined" is unchanged and stays as it is. `docs/06-deployment.md`'s Design Philosophy
carries the same caveat and is task 1.1 — the two must not disagree.

- [x] 3.3 In `CORE-001`'s projections table, replace this anchor — **two rows of a markdown table**:

```
| Horizontal projection — `4 × 3` studs | Distances, movement, deployment areas, footprints |
| The volume itself — `4 × 3` studs by 12 plate layers | Transport capacity and interior space |
```

with:

```
| Horizontal projection — `4 × 3` studs | Distances, movement, deployment floors, footprints |
| The volume itself — `4 × 3` studs by 12 plate layers | Transport capacity, interior space, and the Deployment Volume a model must fit inside |
```

The third row, the vertical projection, is unchanged. This table is the reason the
change exists: deployment was listed as a horizontal reading, and after this change it
is not one.

- [x] 3.4 In `CORE-001`, replace this anchor — the opening sentence of the footprint paragraph, whose closing sentence task 3.1 edits separately:

```
All distances, deployment areas and vehicle footprints are expressed using this unit.
```

with:

```
All distances, Deployment Volumes and vehicle footprints are expressed using this unit.
```

---

## 4. `docs/09-transport.md`

- [x] 4.1 In `TRN-020`, replace this anchor — the rule's closing paragraph:

```
How many levels a vehicle has room for is bounded by its footprint rather than by this rule: a vehicle may rise 6 plate layers for every stud of its footprint's narrowest side (`08-vehicles.md`, VEH-028).
```

with:

```
How many levels a vehicle has room for is bounded by the ceiling of the agreed Deployment Volume rather than by this rule (`06-deployment.md`, DEP-001; `08-vehicles.md`, VEH-028).
```

---

## 5. `docs/14-glossary.md`

- [x] 5.1 Replace this entry — **heading and body**:

```
## Deployment Area

The battlefield space, measured in Unit Bases, that a player's army may occupy before the game begins.
```

with:

```
## Deployment Volume

The battlefield space a player's army must fit inside, agreed before the game and measured in Unit Bases: a floor `W × D` and a ceiling `H`. See `06-deployment.md` (DEP-001).
```

- [x] 5.2 **Delete** this entry entirely — heading, body and the `---` separator that follows it, plus the blank lines that belonged to it, so that the entry before it is followed directly by the entry after it:

```
## Maximum Height

The greatest height a vehicle's Gameplay Geometry may reach above its Base Plane: 6 plate layers — two bricks, half a Unit Base — for every stud of its narrowest footprint side. A construction check made before deployment, never an in-game state. See `08-vehicles.md` (VEH-028).

---
```

Nothing replaces it. There is no longer a per-vehicle maximum height to define
(`design.md`, Decision 4).

- [x] 5.3 **Delete** this entry entirely, the same way:

```
## Base Plane

A vehicle's lowest floor — the surface its own Unit Bases rest on — and the datum its Maximum Height is counted from. A property of the model rather than of the ground beneath it; everything below it is locomotion. See `08-vehicles.md` (VEH-029).

---
```

Nothing replaces it. Height is counted from the surface the vehicle rests on, which
`VEH-029` states in place and no longer names.

- [x] 5.4 In the *Projection* entry, replace this anchor:

```
The reading of the Unit Base volume a rule takes: horizontal for distance, deployment and footprints; the whole volume for transport capacity; vertical for passing an opening.
```

with:

```
The reading of the Unit Base volume a rule takes: horizontal for distance, deployment floors and footprints; the whole volume for transport capacity and for the Deployment Volume a model must fit inside; vertical for passing an opening.
```

The rest of the entry — "A projection is a measured value and never replaces a
physical check. See `02-core-rules.md` (CORE-001)." — is unchanged.

---

## 6. `docs/04-construction-standard.md`

- [x] 6.1 In `SCS-003`, replace this anchor:

```
Vehicles are measured using Unit Bases — see `08-vehicles.md` (VEH-001) for the canonical footprint examples and the size ceiling (none — the agreed Deployment Area naturally limits model size).
```

with:

```
Vehicles are measured using Unit Bases — see `08-vehicles.md` (VEH-001) for the canonical footprint examples and the size ceiling (none — the agreed Deployment Volume naturally limits model size).
```

---

## 7. `docs/10-weapons.md`

- [x] 7.1 In `WPN-005`, replace this anchor — **two occurrences of the term in one sentence**:

```
Weapon Length is bounded by Platform Length (WPN-004), platform size by the agreed Deployment Area (`04-construction-standard.md`, SCS-003; `06-deployment.md`, DEP-003), and the Deployment Area by the battlefield the players agree on before it (`03-game-flow.md`, FLOW-001).
```

with:

```
Weapon Length is bounded by Platform Length (WPN-004), platform size by the agreed Deployment Volume (`04-construction-standard.md`, SCS-003; `06-deployment.md`, DEP-003), and the Deployment Volume by the battlefield the players agree on before it (`03-game-flow.md`, FLOW-001).
```

---

## 8. `docs/03-game-flow.md`

- [x] 8.1 Replace this anchor:

```
- The battlefield size (FLOW-001) and the Deployment Area (`06-deployment.md`, DEP-001).
```

with:

```
- The battlefield size (FLOW-001) and the Deployment Volume (`06-deployment.md`, DEP-001).
```

- [x] 8.2 Replace this anchor:

```
This ruleset defines no objectives of its own. It states what a scenario must declare, not what it may declare — the same way DEP-001 requires a Deployment Area to be agreed without dictating its size.
```

with:

```
This ruleset defines no objectives of its own. It states what a scenario must declare, not what it may declare — the same way DEP-001 requires a Deployment Volume to be agreed without dictating its size.
```

---

## 9. `docs/01-foundations.md`

- [x] 9.1 In the Unit Base overview's example list, replace this anchor:

```
- Deployment areas are measured in UB, horizontally.
```

with:

```
- Deployment Volumes are measured in UB, as a volume — a floor and a ceiling (`06-deployment.md`, DEP-001).
```

The three bullets around it — infantry, vehicle footprints, transport capacity — are
unchanged. This is the fourth and last place that called deployment a horizontal
reading.

---

## 10. `assets/IMAGES.md`

The image index specifies images the ruleset needs, and three of its entries brief an
illustrator on rules this change rewrites. Commit `a837ec9` is the precedent: the
index is refreshed in the change that invalidates it, not later.

- [x] 10.1 In the `VEH-028` entry, replace this anchor — the whole "What it must show" and "Why text alone is not enough" cells are being replaced together, as one row's two cells. Do not reflow the row:

```
| VEH-028 | `assets/images/veh-028-enclosing-rectangle.png` | A vehicle with a non-rectangular outline — an L-shaped or stepped footprint — drawn over a stud grid. Shade the Unit Bases the outline actually covers. Around them, draw the smallest rectangle of whole Unit Bases that encloses the outline, dimensioned on both sides in studs. Label the shaded cells and the enclosing rectangle distinctly, and mark the cells inside the rectangle that no part of the vehicle covers. | One footprint is read two ways here, and for an outline that is not a rectangle the two readings cover different cells. Which cells belong to which reading is the whole difficulty: the rule states the construction in a sentence, and a reader who conflates the two applies one cell set to both rules — the covered cells give the right cost and the wrong height, the enclosing rectangle the reverse. |
```

with:

```
| VEH-028 | `assets/images/veh-028-agreed-ceiling.png` | A Deployment Volume drawn as an open box, its floor dimensioned in Unit Bases and its ceiling marked at a height in Unit Bases. Inside it, three vehicles measured from the surface they rest on to the top of their Gameplay Geometry: a wide low hull well under the ceiling, a narrow tall one reaching it exactly, and a walker whose legs alone carry its hull past it, drawn as failing. Mark each measurement's start at the resting surface, and show a flag on the failing walker excluded from the measurement. | The rule replaced a limit derived from the footprint with one agreed by the players, and two things a reader gets wrong follow from that: that a narrow vehicle is still short, and that locomotion is still free. The third panel carries the one exclusion that survives — decoration is not measured — which is only legible beside the leg that is. |
```

- [x] 10.2 In the `VEH-029` entry, replace this anchor, the same way:

```
| VEH-029 | `assets/images/veh-029-base-plane-datum.png` | A long-legged walker with its Base Plane marked at its interior floor, the height counted straight up from that plane, and the entire leg assembly below it shaded as excluded. The same walker repeated on a slope, and again standing on a carrier vehicle's floor — each time with its Base Plane marked on the walker itself and the measurement unchanged. | The datum sits on the model rather than on the table, so where the count begins is the whole rule, and prose cannot point at it. A shaded exclusion also shows in one look what the rule needs several paragraphs to argue: that locomotion below the plane is not height at all. |
```

with:

```
| VEH-029 | `assets/images/veh-029-resting-surface-datum.png` | A long-legged walker measured from the surface it rests on to the top of its Gameplay Geometry, with the leg assembly shaded as included. The same walker repeated on a slope, and again standing inside a carrier vehicle — each time measured against the same total, with the slope and the carrier's floor marked as changing nothing. | Where the count begins is the whole rule, and the answer moved: everything the model stands up on is now part of its height. The repeated panels carry the half prose argues hardest, that terrain and being carried never re-measure a model whose legality was settled at the bench. |
```

- [x] 10.3 In the `TRN-019` entry, replace this anchor — one clause inside its long "Why text alone is not enough" cell:

```
Neither neighbouring image carries a datum that moves: CMP-018's doorway measures a fixed aperture, and VEH-029's Base Plane is the floor itself, which a bench standing on it does not raise.
```

with:

```
Neither neighbouring image carries a datum that moves: CMP-018's doorway measures a fixed aperture, and VEH-029 measures from the surface a vehicle rests on, which a bench inside it does not raise.
```

- [x] 10.4 In the rejected-candidates list, replace this anchor:

```
- **TRN-020 (Interior Levels)** — The stacking is arithmetic on a height the CORE-001 image already dimensions: one Unit Base of clear height per level, plus a plate for each floor above the lowest. VEH-028 works the answer out in its own text for footprints 4, 8 and 12 studs across, so nothing is left for a picture to settle.
```

with:

```
- **TRN-020 (Interior Levels)** — The stacking is arithmetic on a height the CORE-001 image already dimensions: one Unit Base of clear height per level, plus a plate for each floor above the lowest. How many levels fit is then a comparison against the agreed ceiling, which the VEH-028 image draws, so nothing is left for a picture to settle.
```

- [x] 10.5 In the rejected-candidates list, replace this anchor:

```
- **DEP-003, DEP-004 (Vehicle Footprint, Infantry)** — Both are direct multiplication/counting applications of the Unit Base's horizontal projection, already covered by the CORE-001 image. The contrast between what DEP-003 charges and what VEH-028 encloses is drawn in VEH-028's image, not in a second one here.
```

with:

```
- **DEP-003, DEP-004 (Vehicle Footprint, Infantry)** — Both are direct multiplication/counting applications of the Unit Base's horizontal projection, already covered by the CORE-001 image. What DEP-003 charges is that floor and nothing above it; the ceiling it no longer bounds is drawn in VEH-028's image, not in a second one here.
```

- [x] 10.6 In the rejected-candidates list, replace this anchor:

```
- **DEP-006 (Embarked Units)** — The waiver and its limit are counting rules: an embarked model costs no Deployment Area, an externally carried one costs its own. Nothing about where such a model sits is hard to picture.
```

with:

```
- **DEP-006 (Embarked Units)** — The waiver and its limit are counting rules: an embarked model costs no Deployment Volume, an externally carried one costs its own. Nothing about where such a model sits is hard to picture.
```

- [x] 10.7 **Verify only, change nothing.** `scripts/lint_ruleset.py` checks every filename in this file against the naming convention, that it names a document which exists, and that the rule it illustrates exists in that document. Tasks 10.1 and 10.2 rename two files — `veh-028-agreed-ceiling.png` and `veh-029-resting-surface-datum.png`. Confirm the linter passes (verification 11.9) and that no other entry in the file names either old filename.

---

## 11. Verification

Each command below was run against the pre-change tree and the "before" figure is what
it actually returned. Run each one after applying, and report any figure that differs
from "after" **without editing a document to make a check pass**.

- [x] 11.1 `grep -rni "deployment area" docs/ assets/ | wc -l` — before: **30**, after: **0**. Case-insensitive on purpose: three of the sites are lower-case prose calling deployment a horizontal reading, and a case-sensitive check passes while they survive.

- [x] 11.2 `grep -rn "Deployment Volume" docs/ | wc -l` — before: **0**, after: **35**. `grep -c "Deployment Volume" docs/06-deployment.md` — before: **0**, after: **20**.

- [x] 11.3 `grep -rn "Base Plane" docs/ assets/ | wc -l` — before: **11**, after: **0**.

- [x] 11.4 `grep -rn "Maximum Height" docs/ | wc -l` — before: **7**, after: **0**.

- [x] 11.5 `grep -c "6 plate layers" docs/08-vehicles.md docs/06-deployment.md docs/09-transport.md` — before: `4`, `1`, `1`. After: `0`, `0`, `0`. The derived multiplier is gone from every document.

- [x] 11.6 `grep -c "^# VEH-0" docs/08-vehicles.md` and `grep -c "^# DEP-0" docs/06-deployment.md` — before: **30** and **9**. After: **30** and **9**. No rule is added, removed or renumbered; `VEH-028`, `VEH-029` and `DEP-001` change titles only.

- [x] 11.7 `grep -c "^## " docs/14-glossary.md` — before: **48**, after: **46**. Exactly two entries are deleted, and no other entry is lost.

- [x] 11.8 `python3 scripts/lint_ruleset.py` — exits 0, no findings. It resolves every cross-document rule ID and every filename in `assets/IMAGES.md`, so tasks 10.1 and 10.2's two renamed image files are checked here.

- [x] 11.9 `python3 scripts/check_delta_coverage.py` — before: `Checked 1 MODIFIED requirement(s) across all changes. No dropped scenarios.`, after: the same. The delta is already written and no task changes it; this confirms it still covers every scenario the living spec has.

- [x] 11.10 `git status --porcelain` — exactly eleven paths: the nine `docs/*.md` files, `assets/IMAGES.md`, and this change's own directory. Nothing under `openspec/specs/`, no `CHANGELOG.md`, no `**Version:**` header, and no `README.md`.

- [x] 11.11 `grep -rn "Version:" docs/*.md | grep -c "0.2.0 Draft"` — before: **15**, after: **15**.

- [x] 11.12 Report anything that had to be interpreted. Every interpretation is a place this proposal was unclear (`system/delegating-to-agents.md`).


---

## 12. Post-audit repairs

The audit of the **applied** text returned sixteen findings, thirteen of them defects
in this proposal's own replacement wording rather than in its transcription — the
pattern `system/delegating-to-agents.md` predicts. Every anchor below was checked
against the **applied** tree and occurs exactly once.

Three findings are answered in `design.md` rather than in `docs/`: the stale site
counts in `proposal.md` and `design.md`, the `unit-base` capability's *Unit Base
Measurement* requirement (handed to the next change explicitly rather than deltaed
twice), and the change-relative phrasing in two `assets/IMAGES.md` rationales, which
task 12.13 does repair.

- [x] 12.1 In `docs/03-game-flow.md`, `FLOW-001`, replace this anchor:

```
4. Select the deployment size (measured in Unit Bases).
```

with:

```
4. Agree the Deployment Volume — `W × D × H` in Unit Bases (`06-deployment.md`, DEP-001).
```

`FLOW-001` is the list a player follows to start a game, and it asked for a size
without a ceiling. `DEP-001` argues that a two-number agreement defaults to one Unit
Base and that a default whose consequence is invisible is a trap; this is the step
where it was sprung.

- [x] 12.2 In `DEP-002`, replace this anchor:

```
A player's army may occupy any combination of models that physically fits inside the agreed Deployment Volume — on its floor and under its ceiling. A model's height is read the way `08-vehicles.md` (VEH-028) reads a vehicle's: from the surface it rests on to the top of its Gameplay Geometry.
```

with:

```
A player's army may occupy any combination of models that fits inside the agreed Deployment Volume — on its floor and under its ceiling. An infantry model's height is its Unit Base, weapons and equipment included (`02-core-rules.md`, CORE-001; `09-transport.md`, TRN-002). A vehicle's is what `08-vehicles.md` (VEH-028) measures: from the surface it rests on to the top of its Gameplay Geometry.
```

The old sentence measured every model as loose plastic, which `CORE-001` forbids —
"what must fit is the Unit Base … never the loose model" — and which would have put a
minifigure holding an upright rifle over a one-Unit-Base ceiling, in the game
`DEP-001` calls an infantry game. It also sent infantry to a rule whose subject is
vehicles.

- [x] 12.3 In `DEP-002`, replace this anchor:

```
Any legal combination is allowed provided it physically fits.
```

with:

```
Any legal combination is allowed provided it fits, read that way.
```

"Physically fits" re-opened the question the paragraph above it settles: a tank whose
flag rises through the ceiling does not physically fit, and `VEH-030` keeps it legal.

- [x] 12.4 In `DEP-001`, replace this anchor — **two paragraphs and the example list**, reordered so the rule states the minimum after it has said dimensions are free, and adding the granularity of `H`:

```
Deployment Volumes may have any dimensions agreed upon by the players.

Examples:

- 5 × 1 UB — two numbers, so one Unit Base tall: infantry only
- 5 × 5 × 4 UB
- 10 × 10 × 6 UB
- Scenario-defined volumes
```

with:

```
Deployment Volumes may have any dimensions agreed upon by the players, subject only to the one Unit Base of height an army needs to exist in.

`H` is agreed in whole Unit Bases. A model's own height is measured as its rule measures it — a vehicle's in plate layers (`08-vehicles.md`, VEH-030) — so a hull 22 plate layers tall fits a ceiling of two Unit Bases with room to spare.

Examples:

- 4 × 4 UB — two numbers, so one Unit Base tall: infantry only
- 5 × 5 × 4 UB
- 10 × 10 × 6 UB
- Scenario-defined volumes
```

Three repairs in one block. The old "any dimensions" denied the minimum stated two
paragraphs above it; nothing said whether `H` could be fractional, which the deleted
`VEH-028` had argued about explicitly; and the old first example used `5 × 1`, the
floor `DEP-009` gives Patrol, so one document showed the same floor as two different
games.

- [x] 12.5 In `DEP-001`, replace this anchor:

```
A one-Unit-Base ceiling is an infantry game, and deliberately so. A powered vehicle carries a Pilot occupying a Unit Base of its own (`08-vehicles.md`, VEH-013), that Unit Base needs a Unit Base of clear height above the surface it sits on (`09-transport.md`, TRN-019), and the floor and the locomotion beneath it are height as well — so no powered vehicle fits under a ceiling of one. Players who want vehicles agree a taller volume.
```

with:

```
A one-Unit-Base ceiling is an infantry game, and deliberately so. A powered vehicle carries a Pilot occupying a Unit Base of its own (`02-core-rules.md`, CORE-003; `08-vehicles.md`, VEH-013), and that Unit Base rests on a floor which rests on the vehicle's locomotion — all of it height, before any hull exists. A closed cockpit needs the clearance above it as well (`09-transport.md`, TRN-019). Players who want vehicles agree a taller volume.
```

The derivation failed on the case it was written for: `TRN-019` imposes no clearance on
a position with no roof over it, so an open-topped bike escaped the argument. The
Pilot's Unit Base, the floor under it and the locomotion under that are enough on
their own, and `TRN-019` now covers the closed case it actually governs.

- [x] 12.6 In `DEP-001`, replace this anchor:

```
Where only two numbers are agreed, the ceiling is one Unit Base. That is also the lowest a Deployment Volume can be: infantry occupies exactly one Unit Base (`09-transport.md`, TRN-002), so a shorter one admits no army at all.
```

with:

```
Where only two numbers are agreed, the ceiling is one Unit Base. That is also the lowest a Deployment Volume can be: infantry occupies exactly one Unit Base (`02-core-rules.md`, CORE-003), so a shorter one admits no army at all.
```

One citation. `DEP-004`, sixty-seven lines below, already cites `CORE-003` for the same
fact; the Core Rule owns it and `TRN-002` itself defers to it.

- [x] 12.7 In the Design Philosophy, replace this anchor:

```
Larger models provide greater capabilities but consume more deployment capacity.
```

with:

```
Wider models provide greater capabilities but consume more deployment capacity.
```

One word. Three lines above, the same section now says height is not charged, so
"larger" was false in one of its two dimensions.

- [x] 12.8 In `VEH-029`, replace this anchor:

```
Height (VEH-028) is counted from **the surface the vehicle rests on when it stands on its own locomotion**. A vehicle that begins the game inside another (`09-transport.md`, TRN-001, TRN-003) is measured the same way and against the same ceiling, never from the carrier's floor: it disembarks into the agreed volume like anything else, and the check belongs to the model rather than to where it starts.
```

with:

```
Height (VEH-028) is counted from **the surface the vehicle rests on when it stands on its own locomotion**. A vehicle that begins the game inside another (`09-transport.md`, TRN-001, TRN-003) is measured the same way and against the same ceiling: its own height is what is checked, never its height plus the carrier's, and a vehicle stowed lying down or in a cradle is measured as it would stand.
```

"Never from the carrier's floor" forbade the correct datum. A walker standing inside a
transport rests on that floor, and measuring from it gives exactly the number the rule
wants. What must not happen is adding the carrier's own height to it.

- [x] 12.9 In `VEH-028`, replace this anchor:

```
How many interior levels a vehicle carries follows from the same ceiling rather than from its footprint — each level needs one Unit Base of clear height, and each floor above the lowest a plate of its own (`09-transport.md`, TRN-020).
```

with:

```
How many interior levels a vehicle carries follows from the same ceiling rather than from its footprint, at the cost `09-transport.md` (TRN-020) sets.
```

The restated arithmetic buys nothing here — the old rule at least computed an answer
from it — and #80 spent a whole change removing copies of exactly this kind.

- [x] 12.10 In `VEH-024`, replace this anchor:

```
A taller assembly clears more terrain at the cost of a taller silhouette, which is easier to see and therefore to shoot (`02-core-rules.md`, CORE-008) — the same trade a walker makes with long legs.
```

with:

```
A taller assembly clears more terrain at the cost of a taller silhouette, which is easier to see and therefore to shoot (`02-core-rules.md`, CORE-008), and of the height it takes under the agreed ceiling (VEH-029) — the same trade a walker makes with long legs.
```

This sentence is what a builder reads when sizing an assembly, and it stated the cost
of tall locomotion in full. After this change it is no longer full.

- [x] 12.11 In `docs/04-construction-standard.md`, `SCS-003`, replace this anchor:

```
Vehicles are measured using Unit Bases — see `08-vehicles.md` (VEH-001) for the canonical footprint examples and the size ceiling (none — the agreed Deployment Volume naturally limits model size).
```

with:

```
Vehicles are measured using Unit Bases — see `08-vehicles.md` (VEH-001) for the canonical footprint examples and the maximum size (none — the agreed Deployment Volume naturally limits model size).
```

"Ceiling" now names a defined part of the Deployment Volume that does limit height, so
a clause saying the ceiling is none reads as a contradiction.

- [x] 12.12 In `system/proposal-review.md`, replace this anchor:

```
      ≤ what fits the Deployment Area (SCS-003, DEP-003)
```

with:

```
      ≤ what fits the Deployment Volume (SCS-003, DEP-003)
```

`system/` needs a branch but not a proposal (`system/workflow.md`, Git Workflow). This
is the repository's canonical worked Range chain, taught to reviewers, and
`10-weapons.md` carries the same chain and was updated by task 7.1.

- [x] 12.13 In `assets/IMAGES.md`, three rationales are written relative to this change rather than to the rule as it stands. Replace each anchor with the text given.

First, in the `VEH-028` entry:

```
| The rule replaced a limit derived from the footprint with one agreed by the players, and two things a reader gets wrong follow from that: that a narrow vehicle is still short, and that locomotion is still free. The third panel carries the one exclusion that survives — decoration is not measured — which is only legible beside the leg that is. |
```

with:

```
| Two things a reader gets wrong about a ceiling that is agreed rather than derived: that a narrow vehicle must be a short one, and that locomotion is free. The third panel carries the one exclusion — decoration is not measured — which is only legible beside the leg that is. |
```

Then, in the `VEH-029` entry:

```
| Where the count begins is the whole rule, and the answer moved: everything the model stands up on is now part of its height. The repeated panels carry the half prose argues hardest, that terrain and being carried never re-measure a model whose legality was settled at the bench. |
```

with:

```
| Where the count begins is the whole rule, and everything the model stands up on is part of its height. The repeated panels carry the half prose argues hardest, that terrain and being carried never re-measure a model whose legality was settled at the bench. |
```

Then, in the rejected-candidates list:

```
What DEP-003 charges is that floor and nothing above it; the ceiling it no longer bounds is drawn in VEH-028's image, not in a second one here.
```

with:

```
What DEP-003 charges is that floor and nothing above it; the ceiling, which it does not bound, is drawn in VEH-028's image, not in a second one here.
```

`assets/IMAGES.md`'s Entry format section bars bookkeeping from these columns: a
rationale that turns on what a rule "no longer" says cannot be evaluated by anyone who
never read the old one.

### Verification after section 12

- [x] 12.14 `grep -rn "physically fits" docs/06-deployment.md` — before: **2**, after: **0**. Both sentences now say how a model is read.

- [x] 12.15 `grep -rni "deployment area" docs/ assets/ system/ | wc -l` — before: **1** (`system/proposal-review.md`), after: **0**.

- [x] 12.16 `grep -c "5 × 1" docs/06-deployment.md` — before: **2** (`DEP-001`'s example and `DEP-009`'s Patrol), after: **1**, the Patrol entry.

- [x] 12.17 `python3 scripts/lint_ruleset.py` and `python3 scripts/check_delta_coverage.py` — both exit 0, the second still reporting one MODIFIED requirement and no dropped scenarios.

- [x] 12.18 `git status --porcelain` — twelve paths: the nine `docs/*.md`, `assets/IMAGES.md`, `system/proposal-review.md`, and this change's directory.


---

## 13. Linter repair — a citation this proposal packed too tightly

Task 12.2's replacement put three backticked filenames and a parenthesised rule ID in
one sentence. `scripts/lint_ruleset.py` pairs a filename with any parenthesised ID
within 80 characters **on the same line**, and does not stop at an intervening
filename, so it read `` `02-core-rules.md` `` … `(VEH-028)` as a reference into
`02-core-rules.md` and failed the build:

```
::error::06-deployment.md: references 02-core-rules.md (VEH-028), which does not exist
```

The citation is correct and the linter's window is the known false-positive class its
own comments describe. The repair is on this proposal's side — the tasks preamble
already warns against exactly this shape, and task 12.2 broke its own rule. The
executing agent reported the failure instead of editing a document to silence it,
which is the standard.

- [x] 13.1 In `DEP-002`, replace this anchor:

```
A vehicle's is what `08-vehicles.md` (VEH-028) measures: from the surface it rests on to the top of its Gameplay Geometry.
```

with:

```
A vehicle's is what `08-vehicles.md`, VEH-028 measures: from the surface it rests on to the top of its Gameplay Geometry.
```

One character pair. The comma form carries the same citation and the linter resolves
it against the right file; no parenthesised ID is left in the sentence for the
80-character window to mis-pair.

- [x] 13.2 `python3 scripts/lint_ruleset.py` — before: exit 1, one issue. After: **exit 0**, `Checked 15 docs, no structural issues found.` Then re-run `python3 scripts/check_delta_coverage.py` — still exit 0, one MODIFIED requirement, no dropped scenarios.

- [x] 13.3 Tick task 12.17 once 13.2 passes: it was left unticked deliberately, because the check it names genuinely failed.
