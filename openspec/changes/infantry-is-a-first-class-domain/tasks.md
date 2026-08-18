# Tasks — Infantry is a first-class domain

## How to apply this change

Every anchor below was checked with exact-substring matching against the pre-change files and occurs **exactly once in the file its task names**. Replace the whole anchor.

If an anchor returns anything other than 1, **stop and report it** rather than guessing which occurrence was meant. Never edit a document to make a verification command pass — report the mismatch instead.

### How to read the replacement blocks

The triple-backtick fence marks where the text starts and stops. **The fence is not part of the text** — do not write the backticks into the document.

A `#` heading or a `---` horizontal rule inside a fence is real markdown that must land in the file as markdown, not as quoted text. Section 2 is full of both: several anchors run from one `#` heading to the next, and the second heading is repeated in the replacement as a **landmark** — a line that must stay in the file, not an edit.

### Vocabulary

- **The body of `RULE-NNN`** is everything between its `# RULE-NNN — Name` heading and the `---` that ends it, heading and `---` untouched.
- **A landmark** is a line reproduced unchanged in a replacement so that a deletion has a unique anchor. Copy it exactly; do not treat it as new text.

### The three things this change must not do

**No rule ID is renumbered or reused.** Ten `MOVE-` IDs are deleted outright — `MOVE-002`, `MOVE-004`, `MOVE-005`, `MOVE-006`, `MOVE-008`, `MOVE-009`, `MOVE-010`, `MOVE-011`, `MOVE-016`, `MOVE-021`. Do not renumber `MOVE-003` into the `MOVE-002` gap, do not renumber anything else, and do not leave a stub saying a rule used to be there.

**`docs/17-infantry.md` is created without a `**Version:**` header.** Every other document in `docs/` has one; this one must not. Writing that line is refused by `.claude/hooks/guard_repo_edits.py` and forbidden by `system/documentation-standards.md` (Versioning). If you find yourself adding it, stop — the task is wrong, not the file (`design.md`, Decision 11).

**Files outside `docs/` are part of this change.** `assets/IMAGES.md`, `README.md`, `TODO.md`, `scripts/lint_ruleset.py`, `scripts/release_cut.py`, `system/documentation-standards.md` and two test files all move with the ruleset, because the ruleset breaks them. Section 13 lists them.

This departs from `system/repository-strategy.md` (Branch Naming), which confines a `<change-name>` branch to `docs/*.md` plus that one change. The maintainer decided it, and `design.md` Decision 12 records what the split cost and why one branch is the better shape here. **No gate enforces the table** — `branch-naming.yml` checks only that the branch is kebab-case and names one change directory.

- [x] 0.1 The branch is `infantry-is-a-first-class-domain`, named for this change directory, and it is branched from an up-to-date `main`.

- [x] 0.2 **This change ships as one branch and one pull request**, including the four files outside `docs/` that it breaks. Sections 9, 10 and 11 were written when it was going to be four, so several of their expected figures describe an intermediate state that no longer exists; each such task carries a note saying so, and section 13 records the final state (`design.md`, Decision 12).

  What was going to be a prerequisite is now part of the change: `scripts/lint_ruleset.py` stops requiring a version header a new document cannot have, and `scripts/release_cut.py` learns to insert that line. `assets/IMAGES.md`, `README.md` and `TODO.md` are repaired here rather than left stale across three merges.

### Scope and coverage

Eight ruleset documents, no spec delta: **one file creation, forty-seven anchor pairs and twenty-seven verification tasks** (9.1 – 9.15, 10.2 – 10.3, 11.16 – 11.25), plus the two non-edit tasks 0.1 and 0.2. Sections 1 – 9 are the change as proposed and audited — thirty-two pairs, listed in the table below. Section 10 is one repair the applier's run found. Section 11 is fifteen repairs from the audit of the applied text; both carry their own coverage notes, and section 11 brings `VEH-002`, `VEH-004` and `VEH-026`'s opening into the change.

| `proposal.md` item | Task | Path |
|---|---|---|
| `docs/17-infantry.md` — the new document | 1.1 | `docs/17-infantry.md` |
| `07-movement.md` — Purpose | 2.1 | `docs/07-movement.md` |
| `MOVE-001` — the four directions, and the duplicated ban | 2.2 | `docs/07-movement.md` |
| `MOVE-002` retired | 2.3 | `docs/07-movement.md` |
| `MOVE-004`, `MOVE-005`, `MOVE-006` retired | 2.4 | `docs/07-movement.md` |
| `MOVE-008` retired | 2.5 | `docs/07-movement.md` |
| `MOVE-009`, `MOVE-010`, `MOVE-011` retired | 2.6 | `docs/07-movement.md` |
| `MOVE-012` — split to its generic half | 2.7 | `docs/07-movement.md` |
| `MOVE-013` — split to its generic half | 2.8 | `docs/07-movement.md` |
| `MOVE-014` — split to its generic half | 2.9 | `docs/07-movement.md` |
| `MOVE-015` — the falling-risk citation | 2.10 | `docs/07-movement.md` |
| `MOVE-016` retired, section renamed | 2.11 | `docs/07-movement.md` |
| The `Unit Movement` section body | 2.12 | `docs/07-movement.md` |
| `MOVE-019` — the access-point citation | 2.13 | `docs/07-movement.md` |
| `MOVE-021` retired with its section | 2.14 | `docs/07-movement.md` |
| `07-movement.md` — Summary | 2.15 | `docs/07-movement.md` |
| `MOVE-003` — measuring from an infantry base | 2.16 | `docs/07-movement.md` |
| `MOVE-007` — the infantry mechanism and example | 2.17 | `docs/07-movement.md` |
| `CORE-005` — the terrain citation | 3.1 | `docs/02-core-rules.md` |
| `CORE-006` — the obstacle citation | 3.2 | `docs/02-core-rules.md` |
| `CORE-003` — a signpost at the infantry document | 3.3 | `docs/02-core-rules.md` |
| `FLOW-013` — the sprinting citation | 4.1 | `docs/03-game-flow.md` |
| `CMP-018` — the approach citation | 5.1 | `docs/05-construction-components.md` |
| `VEH-007` — the restated no-diagonal ban | 6.1 | `docs/08-vehicles.md` |
| `VEH-008` — the borrowed Action Point cost | 6.2 | `docs/08-vehicles.md` |
| `VEH-021` — the borrowed access-point list | 6.3 | `docs/08-vehicles.md` |
| `VEH-026` — the borrowed dice procedure | 6.4 | `docs/08-vehicles.md` |
| `VEH-026` — the disembarked-infantry citation | 6.5 | `docs/08-vehicles.md` |
| `VEH-027` — the stairs contrast | 6.6 | `docs/08-vehicles.md` |
| `VEH-005` — the restated no-diagonal ban | 6.7 | `docs/08-vehicles.md` |
| `DMG-005` — the Wounded-movement citation | 7.1 | `docs/16-damage-system.md` |
| Glossary ***Wounded*** entry | 8.1 | `docs/14-glossary.md` |
| `VEH-007` — the two citations on one line | 10.1 | `docs/08-vehicles.md` |

**Untouched, deliberately:** `MOVE-017`, `MOVE-018` and `MOVE-020`, the three surviving rules that state nothing infantry-only and cite nothing that retires. The `# Design Philosophy`, `# Falling` and `# Physical Priority` sections of `docs/07-movement.md`. `VEH-027`'s citation of `MOVE-012` at "LEGO slope elements", because `MOVE-012` keeps its number and the half `VEH-027` reads it for. `CORE-003`, which owns infantry identity and keeps it — `INF-001` cites it rather than restating it. Every rule in `docs/01-foundations.md`, `docs/06-deployment.md`, `docs/09-transport.md`, `docs/10-weapons.md`, `docs/11-combat.md`, `docs/12-melee.md` and `docs/15-geometry-layers.md`; `docs/06-deployment.md` cites no `MOVE-` ID and needs nothing. `openspec/specs/` — this change ships no delta (`design.md`, Decision 10). `CHANGELOG.md` and every `**Version:**` header. `README.md`, `TODO.md` and `assets/IMAGES.md`, which are companion changes.

---

## 1. `docs/17-infantry.md` — the new document

**This is a file creation, not an anchor pair.** `scripts/apply_tasks.py` does not create files; write this one by hand, exactly as fenced, and create no other file.

The text below is `docs/07-movement.md`'s infantry rules with their citations re-aimed and nothing else changed. **No number, distance, cost or threshold differs from the rule it came from** — `design.md`, Decision 9 tabulates all eleven. Where the source rule cited a `MOVE-` ID that this change retires, the citation names the `INF-` rule that now carries the text; where it cited a rule that survives, the citation names the document as well, because it is now a cross-document reference.

- [x] 1.1 Create `docs/17-infantry.md` containing exactly:

```
# StudCraft Infantry Rules

---

# Purpose

This document defines what an infantry model is and what it can do.

Infantry is a unit domain, as Vehicles is. The mechanics every unit shares are `07-movement.md`; the rules below are the infantry implementation of them.

---

# Design Philosophy

Every distance infantry moves is a count of its own base, so a player measures with a spare base rather than with a ruler.

Infantry has no statistics. What a model can do follows from the base it stands on and from the Action Points every unit receives.

---

# INF-001 — Infantry Unit

What an infantry model is, is `02-core-rules.md` (CORE-003).

Every infantry model is built on the base required by `02-core-rules.md` (CORE-001).

Which edge of that base is its front is settled by the universal Facing rule (`02-core-rules.md`, CORE-002).

The base's orientation defines movement and line of advance.

---

# INF-002 — Forward Movement

Standard infantry movement:

**Up to 12 studs forward, in multiples of 3 studs**

12 is the maximum, not a fixed distance — a unit may move 3, 6, 9 or 12 studs, or stay put.

The step size is the Unit Base's depth (`02-core-rules.md`, CORE-001): moving forward crosses the 3-stud axis, so forward movement counts whole base-depths, exactly as side movement counts whole base-widths of 4 (INF-003). Both numbers come from the base itself, so a player can measure either by laying spare infantry bases end to end.

One movement action costs **1 Action Point** (`02-core-rules.md`, CORE-006) and moves the unit in a single direction. Changing direction requires a second movement action (`07-movement.md`, MOVE-007).

Each movement action is measured independently: a unit spending two Action Points on movement makes two separate moves of up to 12 studs each, not one move of 24.

A Wounded model's limit is lower — see INF-012.

Future scenarios may allow sprinting or other special movement.

---

# INF-003 — Side Movement

Infantry may move sideways, left or right.

**Up to 12 studs, in multiples of 4 studs**

The step size is the Unit Base's width (`02-core-rules.md`, CORE-001) — moving sideways crosses the 4-stud axis. Legal distances are therefore 4, 8 and 12 studs. Partial side movement is not allowed.

Side movement is a movement action and costs **1 Action Point**, the same as moving forward (INF-002).

Infantry reaches an off-axis position by combining a forward or backward move with a side move, each its own movement action (`07-movement.md`, MOVE-007). Instead of moving diagonally: forward 6 studs (1 AP), then left 4 studs (1 AP).

A Wounded model's limit is lower — see INF-012.

---

# INF-004 — Backward Movement

Infantry may move backwards.

**Up to 12 studs, in multiples of 3 studs** — the same limit and step size as forward movement (INF-002), because backward movement crosses the same 3-stud axis of the base.

The unit keeps its facing. No rotation is required.

Backward movement is a movement action and costs **1 Action Point**.

A Wounded model's limit is lower — see INF-012.

---

# INF-005 — Rotation

Infantry may rotate to any facing.

Rotation does not require measuring.

Rotating costs:

**1 Action Point**

The new facing becomes immediately active.

---

# Terrain

Terrain physically affects infantry movement. What a slope and a stepped surface are built from is `07-movement.md` (MOVE-012, MOVE-013), and what physically supports a unit at all is MOVE-014; what infantry can do with them is below.

---

# INF-006 — One Brick Obstacles

Height: **up to 3 plate layers** (one brick or less).

Obstacle height is measured in plate layers, the same unit `16-damage-system.md` (DMG-003) uses: a plate counts as 1 and a standard brick as 3.

Infantry may cross freely. No additional movement cost.

---

# INF-007 — Two Brick Obstacles

Height: **4 to 6 plate layers** (more than one brick, up to two).

Infantry may climb. Climbing costs **1 additional Action Point** on top of the movement action that crosses the obstacle, so a move over such an obstacle costs 2 AP in total.

The climb is part of that movement action and does not increase the distance the unit may travel: the limit on that move still applies as a whole — 12 studs (INF-002), or a Wounded model's shorter limit (INF-012).

---

# INF-008 — Three Brick Obstacles

Height: **7 or more plate layers** (taller than two bricks).

Cannot be climbed directly.

A legal access point is required.

Examples:

- Slopes
- Stairs
- Ramps

Without one of these, the obstacle is impassable.

---

# INF-009 — Slopes and Stairs

Infantry may move normally over connected slopes and up stepped surfaces (`07-movement.md`, MOVE-012, MOVE-013), at no additional Action Point cost — they are ordinary terrain, not obstacles to climb. Distance travelled up either counts against the normal movement limit (INF-002).

A stepped surface carries infantry only where no single step is taller than an obstacle infantry crosses freely (INF-006).

---

# INF-010 — Vertical Access

If no slope, stair or ramp exists, the wall cannot be climbed. These are the three legal access points listed in INF-008, and no other construction grants access.

---

# Falling

When a unit falls at all, and where it lands, is `07-movement.md` (MOVE-015). What the fall costs an infantry model is below.

---

# INF-011 — Falling Damage

Falling damage depends on the height fallen, measured in plate layers — the same unit obstacles use (INF-006).

Roll **one D6 for every complete brick (3 plate layers) fallen beyond the first**. A remainder of one or two plate layers adds no die.

The first brick is free, which is why a fall of 3 plate layers or less needs no roll at all: INF-006 already treats that height as trivial to cross, and stepping down it is no more dangerous than stepping over it.

Each die is treated as a Damage Roll (`16-damage-system.md`, DMG-015): a result of 4, 5, or 6 means no damage. A result of 1, 2, or 3 advances the faller's Component State one step (`Operational → Wounded`, or `Wounded → Dead`).

The dice are independent and are never pooled, resolved exactly as multiple Impacts are (DMG-016). Two failed dice therefore take an Operational unit to Dead — the higher the fall, the more dice, and the more likely both a wound and a death.

This is a declared exception to the normal sequence: falling has no Impact Strength and no attacker, so there is no Geometry Check (DMG-014) to pass first. The Damage Rolls apply directly, and Resistance plays no part in falling damage.

No height is certainly fatal. A unit that survives a very tall fall has simply passed every Damage Roll, which `16-damage-system.md` (DMG-015) already describes as a fortunate landing rather than an oversight. This is intentional: in StudCraft, geometry can rule an outcome out — the first brick of a fall, like an Impact below a component's Resistance (DMG-014) — but geometry never rules an outcome in. A minifig can survive two cannon Impacts for the same reason it can survive a fall from a tower.

Vehicle falling is defined separately in `08-vehicles.md` (VEH-026), which scales from each vehicle's own Terrain Threshold rather than from a fixed first brick.

Example:

- Fall of 1 brick (3 plate layers) → no dice, no damage.
- Fall of 2 bricks → Roll 1D6. A failure wounds; a fall this short cannot kill an Operational unit.
- Fall of 3 bricks → Roll 2D6, resolved independently. Two failures kill.
- Fall of 5 bricks → Roll 4D6, resolved independently.
- Fall of 10 bricks → Roll 9D6. Survival is very unlikely.

---

# Damage Effects

What a damaged infantry model can still do. The Component States themselves are `16-damage-system.md` (DMG-005).

# INF-012 — Wounded Movement

A Wounded infantry model (`16-damage-system.md`, DMG-005) moves **at most two steps** in whichever direction it travels.

The step is the one that direction already uses (`02-core-rules.md`, CORE-001): the Unit Base's 3-stud depth forward and backward (INF-002, INF-004), and its 4-stud width sideways (INF-003). So a Wounded model may move **up to 6 studs forward or backward** and **up to 8 studs sideways** — distances those rules already allow, with the longer ones removed.

Nothing else about the move changes. It still costs **1 Action Point**, it still travels in a single direction (`07-movement.md`, MOVE-007), and rotation (INF-005), slopes and stairs (INF-009) and falling (`07-movement.md`, MOVE-015; INF-011) are untouched. Climbing a two-brick obstacle still costs the 1 additional Action Point INF-007 charges — what changes there is the length of the move the climb belongs to, not the climb.

The limit is counted in steps rather than taken as half the normal distance because half of a side move is 6 studs, which INF-003 does not allow. A fraction of a legal distance is not always a legal distance; a count of steps always is.

---

# Summary

Infantry in StudCraft follows seven simple principles:

1. An infantry model is a minifigure on the base `02-core-rules.md` defines.
2. Forward and backward movement is up to 12 studs, in multiples of 3.
3. Side movement is up to 12 studs, in multiples of 4.
4. Each movement action costs 1 Action Point, and so does a rotation.
5. Obstacles up to 3 plate layers are crossed freely, 4 to 6 cost 1 additional Action Point, and 7 or more need a slope, a stair or a ramp.
6. A fall rolls one D6 per complete brick beyond the first, each die a Damage Roll.
7. A Wounded model moves at most two steps in any direction — 6 studs forward or backward, 8 sideways.

---

> **Every Brick Matters.**
```

  **The file must end with `---`, a blank line, and then `> **Every Brick Matters.**`** — `scripts/lint_ruleset.py` checks the last non-empty line, and it requires the `# Purpose`, `# Design Philosophy` and `# Summary` headings above.

---

## 2. `docs/07-movement.md`

### 2.1 Purpose

- [x] 2.1 Replace this anchor — the first line of the `# Purpose` section and the three lines below it. The `# Purpose` heading is **not** part of the anchor:

```
This document defines how units move across the battlefield.

Movement in StudCraft is entirely based on the physical LEGO model.

Distances are measured using LEGO studs.

No diagonal movement exists.
```

with:

```
This document defines the movement mechanics every unit shares.

Movement in StudCraft is entirely based on the physical LEGO model.

Distances are measured using LEGO studs.

No diagonal movement exists.

How far a particular unit moves, and what terrain it can cross, is stated by its own domain — `17-infantry.md` for infantry, `08-vehicles.md` for vehicles.
```

### 2.2 `MOVE-001`

- [x] 2.2 In `MOVE-001`, replace this anchor — the whole rule body. The heading is **not** part of the anchor:

```
Every unit has four possible movement directions:

- Forward
- Backward
- Left
- Right

Movement is always performed relative to the current facing of the unit.

Diagonal movement is never allowed.
```

with:

```
Movement is always performed relative to the current facing of the unit (`02-core-rules.md`, CORE-002).

Which directions a unit may move in is its own domain's rule: infantry moves forward, backward, left and right (`17-infantry.md`, INF-002 through INF-004), while a vehicle moves forward and in reverse and changes direction by turning (`08-vehicles.md`, VEH-005, VEH-006, VEH-008 through VEH-011).
```

  **The four directions are infantry's, not every unit's.** No vehicle moves left or right without turning — `VEH-005` and `VEH-006` give a vehicle two directions, and `VEH-008` through `VEH-011` give it turns instead of the other two. Stating four as universal is the same defect this change removes from `VEH-021`, in the document that is supposed to be the generic one. The no-diagonal line goes because `MOVE-007` states the ban in full and `# Purpose` states it a third time.

### 2.3 `MOVE-002` retired

- [x] 2.3 Replace this anchor — the whole `MOVE-002` rule, from its heading through the `MOVE-003` heading that follows it. The `---` above `# MOVE-002` stays where it is and becomes the separator before `MOVE-003`:

```
# MOVE-002 — Infantry Base

Every infantry model is built on the base required by `02-core-rules.md` (CORE-001).

Which edge of that base is its front is settled by the universal Facing rule (`02-core-rules.md`, CORE-002).

The base's orientation defines movement and line of advance.

---

# MOVE-003 — Measuring Movement
```

with:

```
# MOVE-003 — Measuring Movement
```

  `MOVE-003`'s heading is a landmark. `INF-001` states the deleted text. **Do not renumber `MOVE-003` into the gap.**

### 2.4 `MOVE-004`, `MOVE-005`, `MOVE-006` retired

- [x] 2.4 Replace this anchor — three whole rules, from the `MOVE-004` heading through the `MOVE-007` heading that follows them:

```
# MOVE-004 — Infantry Movement

Standard infantry movement:

**Up to 12 studs forward, in multiples of 3 studs**

12 is the maximum, not a fixed distance — a unit may move 3, 6, 9 or 12 studs, or stay put.

The step size is the Unit Base's depth (`02-core-rules.md`, CORE-001): moving forward crosses the 3-stud axis, so forward movement counts whole base-depths, exactly as side movement counts whole base-widths of 4 (MOVE-005). Both numbers come from the base itself, so a player can measure either by laying spare infantry bases end to end.

One movement action costs **1 Action Point** (`02-core-rules.md`, CORE-006) and moves the unit in a single direction. Changing direction requires a second movement action (MOVE-007).

Each movement action is measured independently: a unit spending two Action Points on movement makes two separate moves of up to 12 studs each, not one move of 24.

A Wounded model's limit is lower — see MOVE-021.

Future scenarios may allow sprinting or other special movement.

---

# MOVE-005 — Side Movement

Infantry may move sideways, left or right.

**Up to 12 studs, in multiples of 4 studs**

The step size is the Unit Base's width (`02-core-rules.md`, CORE-001) — moving sideways crosses the 4-stud axis. Legal distances are therefore 4, 8 and 12 studs. Partial side movement is not allowed.

Side movement is a movement action and costs **1 Action Point**, the same as moving forward (MOVE-004).

A Wounded model's limit is lower — see MOVE-021.

---

# MOVE-006 — Backward Movement

Infantry may move backwards.

**Up to 12 studs, in multiples of 3 studs** — the same limit and step size as forward movement (MOVE-004), because backward movement crosses the same 3-stud axis of the base.

The unit keeps its facing. No rotation is required.

Backward movement is a movement action and costs **1 Action Point**.

A Wounded model's limit is lower — see MOVE-021.

---

# MOVE-007 — No Diagonal Movement
```

with:

```
# MOVE-007 — No Diagonal Movement
```

  `INF-002`, `INF-003` and `INF-004` state the deleted text.

### 2.5 `MOVE-008` retired

- [x] 2.5 Replace this anchor — the whole `MOVE-008` rule, through the `# Terrain Movement` section heading that follows it:

```
# MOVE-008 — Rotation

Infantry may rotate to any facing.

Rotation does not require measuring.

Rotating costs:

**1 Action Point**

The new facing becomes immediately active.

---

# Terrain Movement
```

with:

```
# Terrain Movement
```

  `INF-005` states the deleted text. The `# Terrain Movement` heading is a landmark and still heads `MOVE-012` through `MOVE-014`.

### 2.6 `MOVE-009`, `MOVE-010`, `MOVE-011` retired

- [x] 2.6 Replace this anchor — three whole rules, from the `MOVE-009` heading through the `MOVE-012` heading that follows them:

```
# MOVE-009 — One Brick Obstacles

Height: **up to 3 plate layers** (one brick or less).

Obstacle height is measured in plate layers, the same unit `16-damage-system.md` (DMG-003) uses: a plate counts as 1 and a standard brick as 3.

Infantry may cross freely. No additional movement cost.

---

# MOVE-010 — Two Brick Obstacles

Height: **4 to 6 plate layers** (more than one brick, up to two).

Infantry may climb. Climbing costs **1 additional Action Point** on top of the movement action that crosses the obstacle, so a move over such an obstacle costs 2 AP in total.

The climb is part of that movement action and does not increase the distance the unit may travel: the limit on that move still applies as a whole — 12 studs (MOVE-004), or a Wounded model's shorter limit (MOVE-021).

---

# MOVE-011 — Three Brick Obstacles

Height: **7 or more plate layers** (taller than two bricks).

Cannot be climbed directly.

A legal access point is required.

Examples:

- Slopes
- Stairs
- Ramps

Without one of these, the obstacle is impassable.

---

# MOVE-012 — Slopes
```

with:

```
# MOVE-012 — Slopes
```

  `INF-006`, `INF-007` and `INF-008` state the deleted text.

### 2.7 `MOVE-012` keeps its number and its generic half

- [x] 2.7 Replace this anchor — the body of `MOVE-012`. The heading is **not** part of the anchor:

```
A slope is built from LEGO slope elements, and is a valid climbing surface.

Units may move normally over connected slopes, at no additional Action Point cost — a slope is ordinary terrain, not an obstacle to climb. Distance travelled up a slope counts against the normal movement limit (MOVE-004).

That paragraph is the infantry rule. A vehicle reads this rule for what a slope is built from and nothing else; whether it can ascend one is its own question (`08-vehicles.md`, VEH-027).
```

with:

```
A slope is built from LEGO slope elements, and is a valid climbing surface.

Whether a given unit may ascend one is its own domain's question — infantry (`17-infantry.md`, INF-009), vehicles (`08-vehicles.md`, VEH-027).
```

  The first line is a landmark: `VEH-027` cites `MOVE-012` for exactly that sentence, which is why this rule keeps its number instead of retiring with the others. The disclaimer goes because there is no longer an infantry paragraph to disclaim.

### 2.8 `MOVE-013` keeps its number and its generic half

- [x] 2.8 Replace this anchor — the body of `MOVE-013`. The heading is **not** part of the anchor:

```
Stepped surfaces are valid movement paths, whatever they are built from, as long as no single step is taller than an obstacle a unit crosses freely (MOVE-009).

Units may climb them normally, at no additional Action Point cost, and the distance climbed counts against the normal movement limit (MOVE-004) — the same as slopes (MOVE-012).
```

with:

```
A stepped surface is a valid movement path, whatever it is built from.

Whether a given unit may climb one is its own domain's question — infantry (`17-infantry.md`, INF-009), vehicles never (`08-vehicles.md`, VEH-027).
```

  **The step-height qualification leaves this rule deliberately.** It was stated against `MOVE-009`, an infantry threshold, which would leave the generic document depending on the infantry one — the defect this change removes. `INF-009` carries it (`design.md`, Decision 3).

### 2.9 `MOVE-014` keeps its number and its generic half

- [x] 2.9 Replace this anchor — the body of `MOVE-014`. The heading is **not** part of the anchor:

```
If no slope, stair or ramp exists, the wall cannot be climbed. These are the three legal access points listed in MOVE-011, and no other construction grants access.

Any stable LEGO surface may support a unit, and physical construction determines accessibility.
```

with:

```
Any stable LEGO surface may support a unit, and physical construction determines accessibility.

Which constructions grant a given unit access is its own domain's question — infantry (`17-infantry.md`, INF-008, INF-010), vehicles (`08-vehicles.md`, VEH-021, VEH-027).
```

  The two paragraphs swap order: what survives is the generic one, and it now opens the rule. `INF-010` states the deleted paragraph.

### 2.10 `MOVE-015`

- [x] 2.10 In `MOVE-015`, replace this anchor — the rule's first paragraph:

```
A unit that leaves a higher position without support falls. A unit may do this deliberately — stepping off a ledge is a legal way to descend, at the risk described in MOVE-016.
```

with:

```
A unit that leaves a higher position without support falls. A unit may do this deliberately — stepping off a ledge is a legal way to descend, at the risk its own domain's rule describes — infantry (`17-infantry.md`, INF-011), vehicles (`08-vehicles.md`, VEH-026).
```

  `MOVE-015` keeps its number and its whole rule: when a unit falls and where it lands are generic. Only what the fall costs is a unit rule.

### 2.11 `MOVE-016` retired, and the section renamed

- [x] 2.11 Replace this anchor — the whole `MOVE-016` rule, from its heading through the `# Vehicle Movement` section heading that follows it. The `---` above `# MOVE-016` stays where it is and becomes the separator before the renamed section:

```
# MOVE-016 — Falling Damage

Falling damage depends on the height fallen, measured in plate layers — the same unit obstacles use (MOVE-009).

Roll **one D6 for every complete brick (3 plate layers) fallen beyond the first**. A remainder of one or two plate layers adds no die.

The first brick is free, which is why a fall of 3 plate layers or less needs no roll at all: MOVE-009 already treats that height as trivial to cross, and stepping down it is no more dangerous than stepping over it.

Each die is treated as a Damage Roll (`16-damage-system.md`, DMG-015): a result of 4, 5, or 6 means no damage. A result of 1, 2, or 3 advances the faller's Component State one step (`Operational → Wounded`, or `Wounded → Dead`).

The dice are independent and are never pooled, resolved exactly as multiple Impacts are (DMG-016). Two failed dice therefore take an Operational unit to Dead — the higher the fall, the more dice, and the more likely both a wound and a death.

This is a declared exception to the normal sequence: falling has no Impact Strength and no attacker, so there is no Geometry Check (DMG-014) to pass first. The Damage Rolls apply directly, and Resistance plays no part in falling damage.

No height is certainly fatal. A unit that survives a very tall fall has simply passed every Damage Roll, which `16-damage-system.md` (DMG-015) already describes as a fortunate landing rather than an oversight. This is intentional: in StudCraft, geometry can rule an outcome out — the first brick of a fall, like an Impact below a component's Resistance (DMG-014) — but geometry never rules an outcome in. A minifig can survive two cannon Impacts for the same reason it can survive a fall from a tower.

This rule covers infantry only. Vehicle falling is defined separately in `08-vehicles.md` (VEH-026), which scales from each vehicle's own Terrain Threshold rather than from a fixed first brick.

Example:

- Fall of 1 brick (3 plate layers) → no dice, no damage.
- Fall of 2 bricks → Roll 1D6. A failure wounds; a fall this short cannot kill an Operational unit.
- Fall of 3 bricks → Roll 2D6, resolved independently. Two failures kill.
- Fall of 5 bricks → Roll 4D6, resolved independently.
- Fall of 10 bricks → Roll 9D6. Survival is very unlikely.

---

# Vehicle Movement
```

with:

```
# Unit Movement
```

  `INF-011` states the deleted rule, without the "This rule covers infantry only" sentence, which a document called Infantry does not need. The section heading is renamed in the same edit because the section stops being about vehicles alone — task 2.12 replaces its body.

### 2.12 The `Unit Movement` section body

- [x] 2.12 Replace this anchor — the body of the section task 2.11 renamed. The `# Unit Movement` heading is **not** part of the anchor:

```
Vehicle movement depends on:

- Physical dimensions.
- Locomotion type.

Vehicle-specific rules are described in `08-vehicles.md`, including terrain. The Terrain Threshold rules (VEH-021 through VEH-024) give each locomotion type its own limit, read from the model; VEH-025 covers being stranded, VEH-026 falling, and VEH-027 ascent.

Vehicles and infantry differ most at stairs: infantry climb them (MOVE-013), vehicles never do (VEH-027).
```

with:

```
How far a unit moves, what terrain it crosses and what a fall costs it are stated by its own domain:

- **Infantry** — `17-infantry.md`. The three distances (INF-002 through INF-004), rotation (INF-005), the obstacle thresholds (INF-006 through INF-008), slopes and stairs (INF-009), vertical access (INF-010), falling damage (INF-011) and the Wounded limit (INF-012).
- **Vehicles** — `08-vehicles.md`. Movement and locomotion (VEH-004 through VEH-012), the Terrain Threshold rules (VEH-021 through VEH-024) that give each locomotion type its own limit, read from the model, VEH-025 for being stranded, VEH-026 for falling and VEH-027 for ascent.

Vehicles and infantry differ most at stairs: infantry climb them (`17-infantry.md`, INF-009), vehicles never do (`08-vehicles.md`, VEH-027).
```

  **This must be applied after 2.11**, which supplies the heading it sits under. `scripts/apply_tasks.py` applies pairs in file order, which is this order.

### 2.13 `MOVE-019`

- [x] 2.13 In `MOVE-019`, replace this anchor — the rule's first paragraph:

```
A lowered ramp immediately becomes usable terrain and is a legal access point (MOVE-011, MOVE-014). Where the ramp leads to an opening, that opening must physically pass the model as well (`05-construction-components.md`, CMP-018).
```

with:

```
A lowered ramp immediately becomes usable terrain (MOVE-014). Whether it grants a given unit access is its own domain's question — infantry (`17-infantry.md`, INF-008), vehicles (`08-vehicles.md`, VEH-027). Where the ramp leads to an opening, that opening must physically pass the model as well (`05-construction-components.md`, CMP-018).
```

  "Is a legal access point" was `MOVE-011`'s infantry list, and `INF-008` names ramps in it.

### 2.14 `MOVE-021` retired with its section

- [x] 2.14 Replace this anchor — the whole `# Infantry Damage Effects` section, from its heading through the `# Physical Priority` heading that follows it. The `---` above `# Infantry Damage Effects` stays where it is and becomes the separator before `# Physical Priority`:

```
# Infantry Damage Effects

What a damaged infantry model can still do. Unlike the rules above this heading, these are infantry-only.

# MOVE-021 — Wounded Movement

A Wounded infantry model (`16-damage-system.md`, DMG-005) moves **at most two steps** in whichever direction it travels.

The step is the one that direction already uses (`02-core-rules.md`, CORE-001): the Unit Base's 3-stud depth forward and backward (MOVE-004, MOVE-006), and its 4-stud width sideways (MOVE-005). So a Wounded model may move **up to 6 studs forward or backward** and **up to 8 studs sideways** — distances those rules already allow, with the longer ones removed.

Nothing else about the move changes. It still costs **1 Action Point**, it still travels in a single direction (MOVE-007), and rotation (MOVE-008), slopes (MOVE-012), stairs (MOVE-013) and falling (MOVE-015, MOVE-016) are untouched. Climbing a two-brick obstacle still costs the 1 additional Action Point MOVE-010 charges — what changes there is the length of the move the climb belongs to, not the climb.

The limit is counted in steps rather than taken as half the normal distance because half of a side move is 6 studs, which MOVE-005 does not allow. A fraction of a legal distance is not always a legal distance; a count of steps always is.

---

# Physical Priority
```

with:

```
# Physical Priority
```

  `INF-012` states the deleted rule. **This section heading exists only because the document held infantry rules it had to fence off; both go together.**

### 2.15 Summary

- [x] 2.15 Replace this anchor — the body of the `# Summary` section. The `# Summary` heading is **not** part of the anchor, and neither is the `---` and closing motto below it:

```
Movement in StudCraft is based on seven simple principles:

1. No diagonal movement.
2. Infantry move up to 12 studs forward or backward, in multiples of 3.
3. Side movement is up to 12 studs, in multiples of 4.
4. Each movement action costs 1 Action Point and moves in one direction.
5. Walls require physical access — a slope, a stair or a ramp.
6. Physical construction always defines legal movement.
7. A Wounded model moves at most two steps in any direction — 6 studs forward or backward, 8 sideways.
```

with:

```
Movement in StudCraft is based on five simple principles:

1. No diagonal movement.
2. Movement is measured along the direction of travel, from the leading edge of the model.
3. Each movement action costs 1 Action Point and moves in one direction.
4. Physical construction always defines legal movement, and models may not overlap.
5. How far a unit moves, and what terrain it can cross, is its own domain's rule — `17-infantry.md`, `08-vehicles.md`.
```

  **The count is recomputed, not carried over**: seven principles become five, and the list below states five. `system/proposal-review.md` ("The Summary Is Part of the Rule", "Verify the Number, Not Just the Direction"). Every principle dropped was an infantry value that `17-infantry.md`'s own Summary now states.

### 2.16 `MOVE-003`

- [x] 2.16 In `MOVE-003`, replace this anchor — the rule's first paragraph:

```
Movement is measured along the direction of travel, from the edge of the base that leads in that direction: the front edge moving forward, the rear edge moving backward, and the corresponding side edge moving left or right.
```

with:

```
Movement is measured along the direction of travel, from the face of the model that leads in it: the front face moving forward, the rear face moving backward, and the corresponding side face moving sideways. Which of them a unit may lead with is its own domain's rule — infantry has all four (`17-infantry.md`, INF-002 through INF-004), a vehicle the front and the rear (`08-vehicles.md`, VEH-004, VEH-006).
```

  "the edge of the base" is `CORE-001`'s Unit Base, which only infantry stands on; a vehicle measures from its own model. The rule now states the measurement — from whichever face leads — and defers which faces a unit may lead with, rather than enumerating four as though every unit had them. `VEH-004` is cited for forward measurement and `VEH-006` for reverse, because `VEH-004`'s "Measure from the vehicle's front, along its facing" is its forward instruction and does not govern reverse.

  The rule's second paragraph — "When movement ends, the unit occupies its new position completely." — is **not** part of the anchor and is not touched.

### 2.17 `MOVE-007`

- [x] 2.17 In `MOVE-007`, replace this anchor — everything below the rule's first line. The first line, "StudCraft does not use diagonal movement.", is **not** part of the anchor and is not touched:

```
Players combine forward and lateral movement instead. Each leg is its own movement action, costing 1 Action Point each.

Example — instead of moving diagonally:

- Forward 6 studs (1 AP)
- Left 4 studs (1 AP)

This maintains compatibility with the LEGO grid, and means a unit with 3 AP can make at most three movement legs in an activation.
```

with:

```
A unit reaches an off-axis position by combining the moves and turns its own domain gives it — infantry combines forward or backward with sideways (`17-infantry.md`, INF-003), a vehicle combines forward movement with turns (`08-vehicles.md`, VEH-007). Each leg is its own movement action, costing 1 Action Point.

This maintains compatibility with the LEGO grid, and means a unit with 3 AP can make at most three movement legs in an activation.
```

  **`MOVE-007` is the rule task 6.1 sends every vehicle to, so it cannot prescribe an infantry remedy.** "Forward and lateral movement" is what `VEH-007` says vehicles do *not* do, and the worked example counts the infantry base's 3-stud and 4-stud axes. The example is transposed into `INF-003` by task 1.1, unchanged: forward 6 studs (1 AP), then left 4 studs (1 AP). The ban, the one-action-per-leg rule and the 3-AP consequence are universal and stay.

---

## 3. `docs/02-core-rules.md`

- [x] 3.1 In `CORE-005`, replace this anchor — the opening clause of the rule's closing paragraph:

```
its walls, slopes, stairs and platforms are terrain, and how a unit crosses or stands on them is `07-movement.md` (MOVE-009 through MOVE-014).
```

with:

```
its walls, slopes, stairs and platforms are terrain — `07-movement.md` (MOVE-012 through MOVE-014) states what those constructions are — and how a unit crosses or stands on them is its own domain's rule: `17-infantry.md` (INF-006 through INF-010) for infantry, `08-vehicles.md` (VEH-021 through VEH-024, VEH-027) for vehicles.
```

  The old citation pointed every unit at the infantry rules. **`TODO.md` quotes this paragraph verbatim** and its quote goes stale here; that repair belongs to the follow-up change and is expected to fail `scripts/check_todo_quotes.py` in section 9 (`design.md`, Decision 12).

- [x] 3.2 In `CORE-006`, replace this anchor — the closing clause of the rule's last paragraph:

```
an obstacle of 3 plate layers is crossed freely and one of 4 is climbed (`07-movement.md`, MOVE-009, MOVE-010).
```

with:

```
an obstacle of 3 plate layers is crossed freely and one of 4 is climbed (`17-infantry.md`, INF-006, INF-007).
```

- [x] 3.3 In `CORE-003`, replace this anchor — the whole rule body. The heading is **not** part of the anchor:

```
Infantry are represented by LEGO minifigures.

Infantry occupy one Unit Base.
```

with:

```
Infantry are represented by LEGO minifigures.

Infantry occupy one Unit Base.

What an infantry model can do is an infantry rule — `17-infantry.md`.
```

  Both existing lines are landmarks and neither changes: `CORE-003` stays the owner of infantry identity, and `INF-001` defers to it. What it gains is the signpost `CORE-004` already has for vehicles ("How small a vehicle may be built is a vehicle-construction rule — `08-vehicles.md`"). Without it, the one universal rule that names infantry names no infantry document, which is the asymmetry this change exists to remove.

---

## 4. `docs/03-game-flow.md`

- [x] 4.1 In `FLOW-013`, replace this anchor — one bullet:

```
- Additional movement options such as sprinting (`07-movement.md`, MOVE-004).
```

with:

```
- Additional movement options such as sprinting (`17-infantry.md`, INF-002).
```

---

## 5. `docs/05-construction-components.md`

- [x] 5.1 In `CMP-018`, replace this anchor — one line:

```
The check is made against the opening, not against the approach. Whether a model can reach the opening is the terrain's question — `07-movement.md` (MOVE-011) for infantry, `08-vehicles.md` (VEH-021) for vehicles — and what must pass through the opening is this rule's.
```

with:

```
The check is made against the opening, not against the approach. Whether a model can reach the opening is the terrain's question — `17-infantry.md` (INF-008) for infantry, `08-vehicles.md` (VEH-021) for vehicles — and what must pass through the opening is this rule's.
```

---

## 6. `docs/08-vehicles.md`

- [x] 6.1 In `VEH-007`, replace this anchor — the whole rule body. The heading is **not** part of the anchor:

```
StudCraft does not use diagonal movement.

Vehicles combine forward movement with turns.
```

with:

```
Vehicles combine forward movement with turns, where infantry combines forward movement with lateral movement (`17-infantry.md`, INF-003). Neither moves diagonally — `07-movement.md` (MOVE-007) states the ban for every unit.
```

  `VEH-007` keeps its number and its own statement: how a vehicle achieves lateral displacement is a vehicle rule. What it stops doing is restating the universal ban `MOVE-007` owns.

- [x] 6.2 In `VEH-008`, replace this anchor — one line:

```
Wheel vehicles may perform, each costing **1 Action Point** (matching MOVE-008's infantry rotation cost):
```

with:

```
Wheel vehicles may perform, each costing **1 Action Point**:
```

  Nothing replaces the parenthetical. The cost is stated in the sentence, and `02-core-rules.md` (CORE-006) already says an action's cost is set by the rule that governs it — a vehicle does not need an infantry rule to corroborate its own price (`design.md`, Decision 6).

- [x] 6.3 In `VEH-021`, replace this anchor — one bullet:

```
- An obstacle **taller** than the threshold blocks movement. The vehicle cannot cross it and must go around, or ascend by a slope or ramp (VEH-027). Do not use MOVE-011's access-point list here: it is the infantry rule and includes stairs, which are never a legal vehicle ascent.
```

with:

```
- An obstacle **taller** than the threshold blocks movement. The vehicle cannot cross it and must go around, or ascend by a slope or ramp (VEH-027). Do not use the infantry access-point list (`17-infantry.md`, INF-008): it includes stairs, which are never a legal vehicle ascent.
```

- [x] 6.4 In `VEH-026`, replace this anchor — one line:

```
Beyond that, roll one D6 for every complete brick (3 plate layers) fallen **past the threshold**. Each die is an independent Damage Roll (`16-damage-system.md`, DMG-015), resolved exactly as infantry falling is (`07-movement.md`, MOVE-016): a result of 4, 5 or 6 means nothing happens, and a result of 1, 2 or 3 advances one component by one state.
```

with:

```
Beyond that, roll one D6 for every complete brick (3 plate layers) fallen **past the threshold**. Each die is an independent Damage Roll (`16-damage-system.md`, DMG-015): a result of 4, 5 or 6 means nothing happens, and a result of 1, 2 or 3 advances one component by one state.
```

  **This is the dependency the change exists to remove.** `DMG-015` owns the dice procedure and is cited in the same sentence; the second citation added nothing but a sibling dependency (`design.md`, Decision 5). No number changes: a vehicle's free height is still its own Terrain Threshold.

- [x] 6.5 In `VEH-026`, replace this anchor — one line:

```
A vehicle at the bottom of a drop may be a trap. Infantry inside it disembark normally (`09-transport.md`, TRN-006), but then face the drop's walls as ordinary terrain: 7 or more plate layers requires a slope, stair or ramp (`07-movement.md`, MOVE-011, MOVE-014). Driving into a ravine can strand a squad as effectively as it strands the vehicle.
```

with:

```
A vehicle at the bottom of a drop may be a trap. Infantry inside it disembark normally (`09-transport.md`, TRN-006), but then face the drop's walls as ordinary terrain: 7 or more plate layers requires a slope, stair or ramp (`17-infantry.md`, INF-008, INF-010). Driving into a ravine can strand a squad as effectively as it strands the vehicle.
```

  **This citation is legitimate and stays.** The sentence is about infantry, so pointing at the infantry rules is correct — what was wrong is that they lived in a document named for the generic mechanic.

- [x] 6.6 In `VEH-027`, replace this anchor — one line:

```
**Stairs are never a legal ascent for a vehicle**, however shallow each step is. Infantry climb stairs (`07-movement.md`, MOVE-013); vehicles do not. What matters is the total rise, not the individual steps — a staircase is one obstacle, not a series of small ones.
```

with:

```
**Stairs are never a legal ascent for a vehicle**, however shallow each step is. Infantry climb stairs (`17-infantry.md`, INF-009); vehicles do not. What matters is the total rise, not the individual steps — a staircase is one obstacle, not a series of small ones.
```

  `VEH-027`'s other citation, of `MOVE-012` for what a LEGO slope element is, is **not** touched: `MOVE-012` keeps its number and that half of its text (task 2.7).

- [x] 6.7 In `VEH-005`, replace this anchor — the rule's last two lines:

```
Movement follows the vehicle's current facing.

Diagonal movement does not exist.
```

with:

```
Movement follows the vehicle's current facing.
```

  The first line is a landmark. Four rules state this ban — `MOVE-001`, `MOVE-007`, `VEH-005` and `VEH-007` — and this is the third of them and the first of the two inside `docs/08-vehicles.md`. `MOVE-007` owns it; tasks 2.2 and 6.1 remove the other two restatements, and `VEH-007` becomes the one vehicle rule that points at the owner.

---

## 7. `docs/16-damage-system.md`

- [x] 7.1 In `DMG-005`, replace this anchor — the opening of the `Wounded` bullet's list of degradations:

```
Exactly three degradations exist, each owned by the document that owns the capability: a Wounded infantry model's movement (`07-movement.md`, MOVE-021), the movement of a vehicle whose Pilot is Wounded (`08-vehicles.md`, VEH-031), and how each Attack Die is read when the component providing the attack is Wounded (`11-combat.md`, CBT-015).
```

with:

```
Exactly three degradations exist, each owned by the document that owns the capability: a Wounded infantry model's movement (`17-infantry.md`, INF-012), the movement of a vehicle whose Pilot is Wounded (`08-vehicles.md`, VEH-031), and how each Attack Die is read when the component providing the attack is Wounded (`11-combat.md`, CBT-015).
```

  The sentence says each degradation is owned by the document that owns the capability, and after this change that is finally true of the first one.

---

## 8. `docs/14-glossary.md`

- [x] 8.1 In the `## Wounded` entry, replace this anchor — the opening of the entry:

```
The middle Component State: the component still functions, and where the capability it provides is one of the three the ruleset degrades, it functions worse — a Wounded infantry model's movement (`07-movement.md`, MOVE-021), the movement of a vehicle whose Pilot is Wounded (`08-vehicles.md`, VEH-031), and how each Attack Die is read when the component providing the attack is Wounded, whether that is the weapon or an unarmed attacker (`11-combat.md`, CBT-015).
```

with:

```
The middle Component State: the component still functions, and where the capability it provides is one of the three the ruleset degrades, it functions worse — a Wounded infantry model's movement (`17-infantry.md`, INF-012), the movement of a vehicle whose Pilot is Wounded (`08-vehicles.md`, VEH-031), and how each Attack Die is read when the component providing the attack is Wounded, whether that is the weapon or an unarmed attacker (`11-combat.md`, CBT-015).
```

  `system/proposal-review.md` ("The Summary Is Part of the Rule") — the glossary entry is checked in the same pass as the rule it restates. This is the only glossary entry citing a retired ID; no entry is added (`design.md`, Decision 8).

---

## 9. Verification

Run each command and write down what it actually returned. If a figure differs from the one stated here, **stop and report it** — do not edit a document to make it match. Every "before" figure below was produced by running the command against the pre-change files.

- [x] 9.1 `grep -c "^# MOVE-" docs/07-movement.md` — before: **21**, after: **11**. The eleven that survive are `MOVE-001`, `MOVE-003`, `MOVE-007`, `MOVE-012`, `MOVE-013`, `MOVE-014`, `MOVE-015`, `MOVE-017`, `MOVE-018`, `MOVE-019`, `MOVE-020`.

- [x] 9.2 `grep -rn "^# INF-" docs/` — before: **no output at all**, after: **twelve lines**, `INF-001` through `INF-012`, all in `docs/17-infantry.md`. Task 1.1. The command is written against the directory rather than the file so that it runs before the file exists.

- [x] 9.3 `grep -rn "MOVE-002" docs/` — before: one hit, the heading in `docs/07-movement.md`. After: **no output at all**. Run the same command for `MOVE-004`, `MOVE-005`, `MOVE-006`, `MOVE-008`, `MOVE-009`, `MOVE-010`, `MOVE-011`, `MOVE-016` and `MOVE-021` — each must also return no output. A surviving hit is a citation this change failed to re-aim.

- [x] 9.4 `grep -rln "07-movement.md" docs/` — before: six files, `02-core-rules.md`, `03-game-flow.md`, `05-construction-components.md`, `08-vehicles.md`, `14-glossary.md` and `16-damage-system.md`. After: **three**, `02-core-rules.md`, `08-vehicles.md` and `17-infantry.md`. All three point back at the generic rules they consume: `CORE-005` keeps a clause naming `MOVE-012` through `MOVE-014` for what a slope, a stepped surface and a supporting surface are (task 3.1), and 9.5 pins how many times the vehicle document does. A **two** here means task 3.1's terrain clause was dropped.

- [x] 9.5 `grep -c -F "07-movement.md" docs/08-vehicles.md` — before: **4**, after: **2**. Tasks 6.4, 6.5 and 6.6 remove three of the four; the survivor is `VEH-027`'s "LEGO slope elements (`07-movement.md`, MOVE-012)", and task 6.1 **adds** one, `VEH-007`'s new pointer at `MOVE-007`. A **1** here means task 6.1 was not applied.

  **Superseded by 11.26.** Section 11 adds three more: `VEH-002` cites `MOVE-001` (11.11), `VEH-004` cites `MOVE-003` (11.3) and `VEH-026` cites `MOVE-015` (11.5). The figure after the whole change is **5**, and that is the point of section 11 — the vehicle document was not reading the shared layer at all.

- [x] 9.6 `grep -rln "^\*\*Version" docs/` — before: **14 files**, after: **the same 14**. `docs/17-infantry.md` must **not** appear: the release-cut-only header line is never written by hand, and the new document is created without it (`design.md`, Decision 11). If it does appear, delete that line and report it.

- [x] 9.7 `grep -c "^# Infantry Damage Effects" docs/07-movement.md` — before: **1**, after: **0**. Task 2.14.

- [x] 9.8 `grep -c -F "five simple principles" docs/07-movement.md` — before: **0**, after: **1**. Task 2.15. A **0** here with `grep -c -F "seven simple principles"` returning **1** means the Summary was left stale.

  **Superseded by 11.18.** Task 11.8 rewrote the Summary again, to **six** principles, adding falling and correcting "leading edge" to a point on the model. Run today this command returns **0**, and so does the `seven simple principles` fallback above — the live string is "six simple principles", which 11.18 pins. Nothing is wrong with the document; this task's figure belongs to an intermediate state.

- [x] 9.9 `python3 scripts/lint_ruleset.py` — before: `Checked 14 docs, no structural issues found.` After: `Checked 15 docs, no structural issues found.` **Read task 0.2 before acting on a failure here.** Until both prerequisites have merged, exactly four errors are expected and none is this change's defect: one reporting that `17-infantry.md` has no release-cut version line, and three naming `MOVE-009`, `MOVE-011` and `MOVE-016` in `assets/IMAGES.md`. Any other error is.

- [x] 9.10 `python3 scripts/check_task_anchors.py infantry-is-a-first-class-domain` — must **exit 0**. Report the line it printed.

- [x] 9.11 `python3 scripts/preflight.py` — **read this before running it.** Two checks may FAIL for reasons this change cannot repair from its own branch, and neither is a defect. `Docs ruleset linter` fails while either prerequisite in task 0.2 is outstanding — 9.9 says which four errors. The other is **`TODO.md quotes the ruleset verbatim`**, which fails until the follow-up change `infantry-references-outside-docs` has merged. `TODO.md` quotes `MOVE-004`'s sprint sentence against `docs/07-movement.md`, and quotes `CORE-005`'s paragraph including its old citation — both go stale here and neither file may be edited from this branch (`design.md`, Decision 12). That checker is not a CI gate and blocks nothing. **Write down what it printed, tick this box, and carry on.** Do not restore a rule and do not edit `TODO.md`. Every other check must PASS, except `Docs ruleset linter` while either prerequisite in task 0.2 is outstanding; if any *other* check fails, that is the halt-and-report case.

- [x] 9.12 `git status --short` — seven modified files — `docs/02-core-rules.md`, `docs/03-game-flow.md`, `docs/05-construction-components.md`, `docs/07-movement.md`, `docs/08-vehicles.md`, `docs/14-glossary.md`, `docs/16-damage-system.md` — plus `docs/17-infantry.md` and the change directory `openspec/changes/infantry-is-a-first-class-domain/` as untracked `??` entries. **`README.md`, `TODO.md` and `assets/IMAGES.md` must NOT appear.** Anything else in the list is a mismatch: report it and stage nothing.

The last three pin the edits that generalise a surviving rule. Each removes an infantry-only phrasing from a document that is supposed to be generic after this change, and none of them is visible in any other check.

- [x] 9.13 `grep -rn -F "Players combine forward and lateral movement" docs/` — before: one hit in `docs/07-movement.md`, after: **no output at all**. Task 2.17. A surviving hit means `MOVE-007` still prescribes an infantry remedy to the vehicles task 6.1 sends there.

- [x] 9.14 `grep -rn -F "from the edge of the base that leads" docs/` — before: one hit in `docs/07-movement.md`, after: **no output at all**. Task 2.16. A surviving hit means `MOVE-003` still measures from a Unit Base only infantry has.

- [x] 9.15 `grep -rn -F "Diagonal movement does not exist" docs/` — before: one hit in `docs/08-vehicles.md`, after: **no output at all**. Task 6.7. `docs/07-movement.md`'s `# Purpose` says "No diagonal movement exists", which is a different string and is not touched.

---

## 10. Repair after applying — `VEH-007`'s two citations on one line

The applier ran section 9 and reported a **fifth** linter error that task 0.2 does not account for:

```
::error::08-vehicles.md: references 17-infantry.md (MOVE-007), which does not exist
```

It is a false positive, and it is this change's defect. `scripts/lint_ruleset.py:41` pairs a filename with the first parenthesised rule ID within eighty characters of it:

```
CROSS_REF_RE = re.compile(r"`([\w.-]+\.md)`[^\n]{0,80}?\(([A-Z]{2,6}-\d{3})\)")
```

Task 6.1's replacement put two citations on one line — `` `17-infantry.md`, INF-003 `` in the comma form, then `` `07-movement.md` (MOVE-007) `` in the parenthesised form about fifty characters later. The scanner reaches past the first citation, finds `(MOVE-007)`, and pairs it with `17-infantry.md`. **Nothing is wrong with the rule as a reader reads it; it is wrong for the checker, and the checker is the required gate.**

The fix is ordering, not content: put the parenthesised citation first, so the only `(ID)` on the line sits immediately after the document that owns it, and leave the comma-form citation with nothing after it to swallow.

**The anchor below was checked against the applied file, not the pre-change one.**

- [x] 10.1 In `docs/08-vehicles.md`, `VEH-007`, replace this anchor — the whole rule body as task 6.1 left it:

```
Vehicles combine forward movement with turns, where infantry combines forward movement with lateral movement (`17-infantry.md`, INF-003). Neither moves diagonally — `07-movement.md` (MOVE-007) states the ban for every unit.
```

with:

```
Neither vehicles nor infantry move diagonally — `07-movement.md` (MOVE-007) states the ban for every unit.

Vehicles combine forward movement with turns, where infantry combines forward movement with lateral movement (`17-infantry.md`, INF-003).
```

  Same two statements, same two citations, two lines instead of one. No rule changes.

### Verification after section 10

- [x] 10.2 `python3 scripts/lint_ruleset.py` — **four** errors, not five: one saying `17-infantry.md` has no release-cut version line, and three naming `MOVE-009`, `MOVE-011` and `MOVE-016` in `assets/IMAGES.md`. The `references 17-infantry.md (MOVE-007)` error must be gone. This supersedes 9.9, which was written before the defect was known.

- [x] 10.3 `grep -c -F "07-movement.md" docs/08-vehicles.md` — still **2**, unchanged from 9.5. The repair moves a citation; it does not add or remove one. **Superseded by 11.26**, which is the same command after section 11 raises it to 5.

10.2 is the sweep for the same trap elsewhere: the linter scans every citation in `docs/`, so a clean run is what confirms no other line this change wrote pairs a filename with another document's rule ID.

---

## 11. Repairs after the audit of the applied text

The applied text was audited and returned fourteen findings. Thirteen are repaired here; the fourteenth is a pre-existing ambiguity this change did not create and does not fix (see the note closing this section).

**Four of them are this change's own defects, and they share one cause: generalising a rule extended it over vehicles that no vehicle rule was adjusted to meet.** The other repairs are wording the split left behind.

**Every anchor in this section was checked against the applied files, not the pre-change ones**, and occurs exactly once. `docs/08-vehicles.md` gains three rules the change had not touched — `VEH-002`, `VEH-004` and `VEH-026`'s opening — and `docs/14-glossary.md` gains an entry, so the coverage table above gains those rows here rather than being rewritten.

Each task names its own file path, because `scripts/check_task_anchors.py` resolves a target from the nearest preceding path and this section has no per-document sub-sections.

### The measurement contradiction — 11.1 through 11.3, apply all three

Task 2.16 rewrote `MOVE-003` to measure "from the face of the model that leads in it: the front face moving forward, **the rear face moving backward**", and cited `VEH-004` and `VEH-006` as the vehicle authority. `VEH-004` says "Measure from the vehicle's front, along its facing", unconditionally, and `VEH-006` says only that reverse uses the same distance. **A tank reversing 45 studs therefore ends 15 studs apart depending on which rule is read.**

Before the change `MOVE-003` said "the edge of the base", which scoped it to infantry and left `VEH-004` the only rule measuring a vehicle. The generalisation is what created the contradiction, so the repair is to stop the shared rule deciding where the measurement starts, and to state it once on each side.

- [x] 11.1 In `docs/07-movement.md`, `MOVE-003`, replace this anchor — the rule's first paragraph as task 2.16 left it:

```
Movement is measured along the direction of travel, from the face of the model that leads in it: the front face moving forward, the rear face moving backward, and the corresponding side face moving sideways. Which of them a unit may lead with is its own domain's rule — infantry has all four (`17-infantry.md`, INF-002 through INF-004), a vehicle the front and the rear (`08-vehicles.md`, VEH-004, VEH-006).
```

with:

```
Movement is measured along the direction of travel, and the whole distance is measured from one point on the model, not from wherever the model happens to be widest.

Where that point is, is its own domain's rule — infantry measures from the face of its base that leads in the direction of travel (`17-infantry.md`, INF-002), a vehicle from its front along its facing (`08-vehicles.md`, VEH-004).
```

  **The enumeration of faces goes.** It was true of an infantry base and false of a vehicle, which is the whole defect. What the shared rule keeps is the part that is genuinely shared: a distance is measured from one point, and that point does not move with the model's silhouette.

- [x] 11.2 In `docs/17-infantry.md`, `INF-002`, replace this anchor — the rule's third paragraph:

```
The step size is the Unit Base's depth (`02-core-rules.md`, CORE-001): moving forward crosses the 3-stud axis, so forward movement counts whole base-depths, exactly as side movement counts whole base-widths of 4 (INF-003). Both numbers come from the base itself, so a player can measure either by laying spare infantry bases end to end.
```

with:

```
The step size is the Unit Base's depth (`02-core-rules.md`, CORE-001): moving forward crosses the 3-stud axis, so forward movement counts whole base-depths, exactly as side movement counts whole base-widths of 4 (INF-003). Both numbers come from the base itself, so a player can measure either by laying spare infantry bases end to end.

The distance is measured from the face of the base that leads in the direction of travel — the front face moving forward, the rear face moving backward (INF-004), the corresponding side face moving sideways (INF-003). This is the general measurement rule (`07-movement.md`, MOVE-003) read against an infantry base.
```

  The first paragraph is a landmark. The new one is the convention `MOVE-003` used to state for infantry and now defers; without it, `17-infantry.md` states four distances and never says where they are measured from.

- [x] 11.3 In `docs/08-vehicles.md`, `VEH-004`, replace this anchor — one line:

```
Measure from the vehicle's front, along its facing.
```

with:

```
Measure from the vehicle's front, along its facing — including in reverse (VEH-006), where the front is still the point measured from even though it is not the leading face. This is the general measurement rule (`07-movement.md`, MOVE-003) read against a vehicle.
```

  **This settles the reversing tank, and settles it the way `VEH-004` already read.** No distance changes: a vehicle still moves three times its own length, forward or backward. What is added is which point the three lengths are counted from when reversing, which no rule stated.

### The remaining repairs

- [x] 11.4 In `docs/07-movement.md`, `MOVE-013`, replace this anchor — the rule's first line:

```
A stepped surface is a valid movement path, whatever it is built from.
```

with:

```
A stepped surface is terrain built from discrete steps, whatever the steps are built from, and each step has a measurable height.
```

  The old line asserted validity unconditionally and the line below it then said half of all units may never use one. `MOVE-012` and `MOVE-014` both state a construction fact and defer the capability; `MOVE-013` alone stated a capability. Now all three match.

- [x] 11.5 In `docs/08-vehicles.md`, `VEH-026`, replace this anchor — the rule's first line:

```
A vehicle that leaves a height and comes down under gravity — rather than descending a slope or ramp (VEH-027) — falls. Measure the fall in plate layers, from the surface it left to the surface it lands on.
```

with:

```
A vehicle that leaves a height and comes down under gravity — rather than descending a slope or ramp (VEH-027) — falls. When a fall happens and where the vehicle is placed is the general rule (`07-movement.md`, MOVE-015); this rule states what it costs. Measure the fall in plate layers, from the surface it left to the surface it lands on.
```

  `MOVE-015` names `VEH-026` as the vehicle side, and `VEH-026` named nothing back. `17-infantry.md`'s Falling section already defers this way, so the change had reproduced its own asymmetry with the domains swapped.

- [x] 11.6 In `docs/08-vehicles.md`, `VEH-007`, replace this anchor — the second line of the rule body as task 10.1 left it:

```
Vehicles combine forward movement with turns, where infantry combines forward movement with lateral movement (`17-infantry.md`, INF-003).
```

with:

```
Vehicles combine forward movement with turns.
```

  The infantry clause goes. `MOVE-007` already draws the contrast and draws it correctly — it says infantry combines forward **or backward** with sideways, where this sentence said only forward. Two statements of one derivation had already disagreed within a single change, which is the argument for not having two.

- [x] 11.7 In `docs/07-movement.md`, replace this anchor — the whole `# Unit Movement` section, from its heading through the `MOVE-017` heading that follows it. The `---` above `# Unit Movement` stays where it is and becomes the separator before `MOVE-017`:

```
# Unit Movement

How far a unit moves, what terrain it crosses and what a fall costs it are stated by its own domain:

- **Infantry** — `17-infantry.md`. The three distances (INF-002 through INF-004), rotation (INF-005), the obstacle thresholds (INF-006 through INF-008), slopes and stairs (INF-009), vertical access (INF-010), falling damage (INF-011) and the Wounded limit (INF-012).
- **Vehicles** — `08-vehicles.md`. Movement and locomotion (VEH-004 through VEH-012), the Terrain Threshold rules (VEH-021 through VEH-024) that give each locomotion type its own limit, read from the model, VEH-025 for being stranded, VEH-026 for falling and VEH-027 for ascent.

Vehicles and infantry differ most at stairs: infantry climb them (`17-infantry.md`, INF-009), vehicles never do (`08-vehicles.md`, VEH-027).

---

# MOVE-017 — Collision
```

with:

```
# MOVE-017 — Collision
```

  **This section was mine, and it should not have been written.** It is an index of another document's rule IDs — "no snapshot a command can print" (`system/documentation-standards.md`, How a Rule Is Written) — and adding `INF-013` would leave it stale exactly as `assets/IMAGES.md` is stale now. Everything in it is already stated: `# Purpose` points at both documents, `MOVE-001`, `MOVE-012`, `MOVE-013`, `MOVE-014` and `MOVE-015` each point at the rule a reader of that rule needs, and `MOVE-013`'s second line already says infantry climb stairs and vehicles never do. It also headed `MOVE-017` through `MOVE-020`, none of which is a domain rule.

- [x] 11.8 In `docs/07-movement.md`, replace this anchor — the body of the `# Summary` section. The heading, the `---` and the closing motto are **not** part of the anchor:

```
Movement in StudCraft is based on five simple principles:

1. No diagonal movement.
2. Movement is measured along the direction of travel, from the leading edge of the model.
3. Each movement action costs 1 Action Point and moves in one direction.
4. Physical construction always defines legal movement, and models may not overlap.
5. How far a unit moves, and what terrain it can cross, is its own domain's rule — `17-infantry.md`, `08-vehicles.md`.
```

with:

```
Movement in StudCraft is based on six simple principles:

1. No diagonal movement.
2. A distance is measured along the direction of travel, from one point on the model.
3. Each movement action costs 1 Action Point and moves in one direction.
4. A unit that leaves a height without support falls, and lands on the first surface that supports it.
5. Physical construction always defines legal movement, and models may not overlap.
6. How far a unit moves, and what terrain it can cross, is its own domain's rule — `17-infantry.md`, `08-vehicles.md`.
```

  Two defects. Falling was missing: `MOVE-015` is one of only two mechanics this document now owns outright, and it had no line. And item 2 said "leading edge", the word task 2.16 replaced — an edge is a property of the infantry base. **The count is recomputed: six items, and six are listed.**

- [x] 11.9 In `docs/07-movement.md`, replace this anchor — the `# Falling` section heading and the `---` below it:

```
# Falling

---
```

with:

```
# Falling

When a unit falls and where it lands are stated here. What the fall costs is its own domain's rule — infantry (`17-infantry.md`, INF-011), vehicles (`08-vehicles.md`, VEH-026).

---
```

  The heading had no body. Its counterpart in `17-infantry.md` carries the same split from the other side, and `# Terrain Movement` in this document carries an orienting line.

- [x] 11.10 In `docs/17-infantry.md`, `INF-001`, replace this anchor — the whole rule body. The heading is **not** part of the anchor:

```
What an infantry model is, is `02-core-rules.md` (CORE-003).

Every infantry model is built on the base required by `02-core-rules.md` (CORE-001).

Which edge of that base is its front is settled by the universal Facing rule (`02-core-rules.md`, CORE-002).

The base's orientation defines movement and line of advance.
```

with:

```
An infantry model is a minifigure occupying one Unit Base — `02-core-rules.md` (CORE-003) is the rule, and this document does not restate it.

Every infantry model is built on the base required by `02-core-rules.md` (CORE-001). Which edge of that base is its front is settled by the universal Facing rule (`02-core-rules.md`, CORE-002).

That orientation is what every direction below is measured relative to — the general rule is `07-movement.md` (MOVE-001).
```

  Three repairs in one body. "What an infantry model is, is" was clumsy and asserted nothing. **"Line of advance" appears nowhere else in the ruleset**, is defined by no rule and no glossary entry, and was inherited from the retired `MOVE-002`; a standalone infantry document is where a reader meets it first, with nothing to infer it from, so it goes. And the rule now cites `MOVE-001`, which after this change is read by no rule at all.

- [x] 11.11 In `docs/08-vehicles.md`, `VEH-002`, replace this anchor — the rule's first line:

```
Every vehicle must have an obvious front — the universal Facing rule (`02-core-rules.md`, CORE-002) applies to vehicles exactly like any other unit.
```

with:

```
Every vehicle must have an obvious front — the universal Facing rule (`02-core-rules.md`, CORE-002) applies to vehicles exactly like any other unit, and movement is performed relative to it (`07-movement.md`, MOVE-001).
```

  The other half of 11.10. `MOVE-001` was generalised to be the rule both domains read for orientation and then read by neither; an interface with traffic in one direction is not one.

- [x] 11.12 In `docs/17-infantry.md`, `INF-010`, replace this anchor — the whole rule body. The heading is **not** part of the anchor:

```
If no slope, stair or ramp exists, the wall cannot be climbed. These are the three legal access points listed in INF-008, and no other construction grants access.
```

with:

```
A vertical face taller than INF-008's threshold cannot be climbed unless a slope, stair or ramp physically reaches it. Those are the three legal access points INF-008 lists, and no other construction grants access.
```

  "The wall" had no antecedent: the word appears nowhere else in this document, and the paragraph that used to precede it stayed behind in `MOVE-014`. A rule whose subject is undefined is not deterministic.

- [x] 11.13 In `docs/17-infantry.md`, `INF-003`, replace this anchor — the rule's fourth paragraph:

```
Infantry reaches an off-axis position by combining a forward or backward move with a side move, each its own movement action (`07-movement.md`, MOVE-007). Instead of moving diagonally: forward 6 studs (1 AP), then left 4 studs (1 AP).
```

with:

```
Infantry reaches an off-axis position by combining a forward or backward move with a side move, each its own movement action (`07-movement.md`, MOVE-007).

Example — instead of moving diagonally:

- Forward 6 studs (1 AP)
- Left 4 studs (1 AP)
```

  The example is restored to the form it had in `MOVE-007` and the form `INF-011` uses. Compressed into a sentence it read as a rules clause; it is an illustration, and it is the only one in the document not marked as one.

- [x] 11.14 In `docs/17-infantry.md`, replace this anchor — the `# Damage Effects` section heading, its line, and the `INF-012` heading below it:

```
# Damage Effects

What a damaged infantry model can still do. The Component States themselves are `16-damage-system.md` (DMG-005).

# INF-012 — Wounded Movement
```

with:

```
# Damage Effects

What a damaged infantry model can still do. The Component States themselves are `16-damage-system.md` (DMG-005).

---

# INF-012 — Wounded Movement
```

  The document's other two section headings, `# Terrain` and `# Falling`, both close with `---` before the rule that follows. This one did not, so `INF-012` rendered without the break every other rule gets.

- [x] 11.15 In `docs/14-glossary.md`, replace this anchor — the end of the `## Wounded` entry, the `---` below it and the closing motto:

```
---

> **Every Brick Matters.**
```

with:

```
---

## Step

An infantry movement increment: one Unit Base depth (3 studs) moving forward or backward, one Unit Base width (4 studs) moving sideways. Used to state a Wounded model's shorter limit as a count rather than a fraction, because half of a legal distance is not always a legal distance. See `17-infantry.md` (INF-012). Not to be confused with a stair's step (INF-009) or with a Component State advancing one step (`16-damage-system.md`, DMG-005).

---

> **Every Brick Matters.**
```

  The entry goes last, which is where this glossary appends. *Step* carries three senses within fifty lines of `17-infantry.md`, and the load-bearing one is stated only inside `INF-012` while the Summary uses it at a distance. `Terrain Threshold`, the vehicle-side counterpart, has had an entry all along.

### Not repaired here — closed later by section 15

**A stepped surface whose steps are 4 to 6 plate layers tall is undecided.** `INF-009` says a stepped surface carries infantry only where no step is taller than one infantry crosses freely — 3 plate layers (`INF-006`) — and `INF-007` says an obstacle of 4 to 6 plate layers may be climbed for 1 additional Action Point. A staircase with 5-plate steps is therefore either not a movement path at all or a series of climbable obstacles, and no rule chooses. The vehicle side does choose, in `VEH-027`: "a staircase is one obstacle, not a series of small ones."

The ambiguity predates this change — `MOVE-013` and `MOVE-010` had it in the same words — and settling it decides how a unit moves, which is a rule change and not a transposition.

**The maintainer settled it on review of pull request #112: a step is an obstacle, read like any other.** Section 15 applies it. This note stays as written because it is the reasoning that reached the maintainer, and a decision reads better beside the question than in place of it.

### Verification after section 11

- [x] 11.16 `python3 scripts/lint_ruleset.py` — still **four** errors, the same four as 10.2. Section 11 adds citations of `MOVE-001`, `MOVE-003` and `MOVE-015` and one glossary entry; a fifth error means one of them does not resolve.

- [x] 11.17 `grep -c "^# " docs/07-movement.md` — before: **19**, after: **18**. Task 11.7 removes `# Unit Movement`; every other heading survives, including `# MOVE-017`, which 11.7's replacement puts back. The 18 are the document title, five section headings — `Purpose`, `Design Philosophy`, `Terrain Movement`, `Falling`, `Physical Priority`, `Summary`, which is six — and eleven `MOVE-` rules; title + 6 + 11 = 18.

  **This task first stated 16 and 15, which were never run against the file.** `system/delegating-to-agents.md` ("Test the verification commands against the pre-change state") is the standing instruction, and the applier reported the mismatch instead of editing the document to satisfy it, which is the standard. The figures above are what the command prints.

- [x] 11.18 `grep -c -F "six simple principles" docs/07-movement.md` — before: **0**, after: **1**. Task 11.8.

- [x] 11.19 `grep -rn -F "line of advance" docs/` — before: one hit in `docs/17-infantry.md`, after: **no output at all**. Task 11.10.

- [x] 11.20 `grep -rn -F "the rear face moving backward" docs/` — before: one hit in `docs/07-movement.md`, after: **one hit, in `docs/17-infantry.md`**. Tasks 11.1 and 11.2 — the clause moves from the shared rule to the infantry rule. Two hits means 11.1 was not applied; none means 11.2 was not.

- [x] 11.21 `python3 scripts/rule.py orphans` — before: `MOVE-001`, `MOVE-003` and `INF-001` are all listed. After: **`MOVE-001` and `MOVE-003` are gone; `INF-001` is still listed, and that is correct.**

  `python3 scripts/rule.py refs MOVE-001 MOVE-003` confirms the two now have readers — `VEH-002` and `INF-001` cite `MOVE-001`, `VEH-004` and `INF-002` cite `MOVE-003`. That was the finding: two rules generalised to be the shared layer and read by neither domain.

  **`INF-001` staying is not the same defect, and this task first claimed it was.** The audit finding was about `MOVE-001` and `MOVE-003` having no inbound citation; `INF-001` is a document's anchor rule, and no rule needs to cite it — `CORE-003` owns infantry identity and `INF-001` defers to it. `VEH-002`, the vehicle document's equivalent anchor, has been uncited since it was written and is not a defect either. The script says so itself: "Standalone is legitimate; disconnected is a defect. This is a shortlist, not a verdict." Fifty-two rules are on that list. `MOVE-017` through `MOVE-020` also stay listed, also legitimately.

- [x] 11.22 `grep -c "^## Step" docs/14-glossary.md` — before: **0**, after: **1**. Task 11.15.

- [x] 11.23 `python3 scripts/check_task_anchors.py infantry-is-a-first-class-domain` — must **exit 0**.

- [x] 11.24 `python3 scripts/preflight.py` — as in 9.11: `Docs ruleset linter` and `TODO.md quotes the ruleset verbatim` FAIL for the companion-change reasons, every other check PASSes.

- [x] 11.25 `git status --short` — unchanged from 9.12: the same seven modified files, `docs/17-infantry.md` and the change directory untracked. Section 11 edits no file the change had not already touched.

- [x] 11.26 `grep -c -F "07-movement.md" docs/08-vehicles.md` — **5**, superseding 9.5 and 10.3, which both fixed it at 2 before section 11 existed. The five are `VEH-002` → `MOVE-001` (11.11), `VEH-004` → `MOVE-003` (11.3), `VEH-007` → `MOVE-007` (6.1), `VEH-026` → `MOVE-015` (11.5) and `VEH-027` → `MOVE-012`, which was there before this change and is untouched.

  **This is the measure of what section 11 was for.** Before it, `08-vehicles.md` named the shared movement document on two lines; the infantry document named it on nine. One domain read the generic layer and the other did not, which is the asymmetry the change set out to remove and had reproduced.

- [x] 11.27 `grep -c -F "07-movement.md" docs/17-infantry.md` — **9**. Counted as lines carrying the filename, not as citations: several lines name it more than once, and both bridging section headings do. The figure is recorded so a later change that thins these pointers has a number to compare against.

---

## 12. One repair from reading the applied text

Found by reading `docs/07-movement.md` end to end after section 11, which is the step `system/proposal-review.md` ("Review the Applied Text, Not Only the Diff") reserves for the reviewer.

Task 11.9 gave the `# Falling` section an orienting line, and it repeats the pointer `MOVE-015` makes four lines below it. Both name `INF-011` and `VEH-026` for what a fall costs. One owner per statement, a pointer instead of a copy: the rule keeps its clause, because a reader of `MOVE-015` needs it there, and the section heading stops restating it.

- [x] 12.1 In `docs/07-movement.md`, replace this anchor — the line task 11.9 added below the `# Falling` heading:

```
When a unit falls and where it lands are stated here. What the fall costs is its own domain's rule — infantry (`17-infantry.md`, INF-011), vehicles (`08-vehicles.md`, VEH-026).
```

with:

```
When a unit falls and where it lands are stated here. What the fall costs is its own domain's rule.
```

  The citations stay where they are load-bearing, in `MOVE-015` itself. The heading keeps the split it announces and drops the duplicate.

### Verification after section 12

- [x] 12.2 `grep -c -F "INF-011" docs/07-movement.md` — before: **2**, after: **1**. The survivor is `MOVE-015`. The same command for `VEH-026` gives the same pair of figures.

- [x] 12.3 `python3 scripts/lint_ruleset.py` — still **four** errors, the same four as 11.16. **Superseded by 13.1**: those four were the price of shipping in four pull requests, and the change now ships in one, so the linter is clean.

---

## 13. Consolidated into one pull request

The change was designed to ship as four pull requests: two prerequisites, the ruleset, and a follow-up. **The maintainer decided it ships as one**, and that is the better shape — the split existed only to work around `scripts/lint_ruleset.py` failing on every intermediate state, and one pull request has no intermediate state.

Three things got simpler, not just fewer:

- **`assets/IMAGES.md` no longer makes a round trip.** The plan was to delete two entries, land the ruleset, then restore them renamed. They now move straight to `## docs/17-infantry.md`, and `MOVE-003`'s entry moves with them — it illustrates a base measured from its leading face, which is `INF-002`'s claim now and not `MOVE-003`'s.
- **`TODO.md` is never stale.** Its two quotes were going to be wrong for the length of one merge.
- **No exemption list has to name a file that does not exist.** The prerequisite was going to list `17-infantry.md` a merge before the document arrived; the requirement it was exempting has since been removed outright (`design.md`, Decision 11).

What was verified after consolidating:

- [x] 13.1 `python3 scripts/lint_ruleset.py` — `Checked 15 docs, no structural issues found.` **No errors at all.** Every figure in sections 9 through 12 that expected four is superseded here.

- [x] 13.2 `python3 scripts/preflight.py` — **all 12 checks PASS**, including `TODO.md quotes the ruleset verbatim` and `Tests`. Sections 9.11 and 11.24 expected two failures; both are gone.

- [x] 13.3 The image index, counted mechanically with `lint_ruleset.parse_image_entries` — **23 entries across 8 documents**, matching the totals the file states in prose. `07-movement.md` leaves that list and `17-infantry.md` joins it.

- [x] 13.4 `git status --short` — clean, after committing. The change touches sixteen paths: eight `docs/*.md`, `assets/IMAGES.md`, `README.md`, `TODO.md`, `scripts/lint_ruleset.py`, `scripts/release_cut.py`, `system/documentation-standards.md`, two files under `tests/`, and its own change directory.

### The four expectations that sections 9 – 12 still state

Left as written, each with a note at the task, because a task's figure records what was true when it ran and the diff is not a place to look things up:

| Task | Said | Now | Why |
|---|---|---|---|
| 9.5, 10.3 | 2 | 5 | Section 11 added three vehicle citations of the shared layer |
| 9.8 | "five simple principles" | "six" | Task 11.8 rewrote the Summary again |
| 9.9, 10.2, 11.16, 12.3 | four linter errors | none | 13.1 |
| 9.11, 11.24 | two preflight failures | none | 13.2 |

---

## 14. Review of pull request #112 — `INF-001` explains itself instead of stating a rule

One review comment, accepted in full.

`INF-001` opened: *"An infantry model is a minifigure occupying one Unit Base — `02-core-rules.md` (CORE-003) is the rule, and this document does not restate it."*

**The second clause is commentary about the document, not a rule.** `system/documentation-standards.md` ("How a Rule Is Written") asks for one imperative sentence with its reason in one clause at most, and no narration. A reader who wants to know what an infantry model is gets told where the answer lives and then told that this document is not the place — after the sentence has already said it.

It is also the exact defect `proposal.md` indicts three times in its opening argument: `MOVE-012`'s *"That paragraph is the infantry rule"*, `MOVE-016`'s *"This rule covers infantry only"*, and the `# Infantry Damage Effects` heading that existed to fence off rules that did not belong. A document apologising for its own shape. This change removed all three and then wrote a fourth into the new document, while repairing something else.

The fix is to state the fact and cite the owner, which is what every other rule here does.

**The anchor below was checked against the applied file**, and occurs exactly once.

- [x] 14.1 In `docs/17-infantry.md`, `INF-001`, replace this anchor — the rule's first line:

```
An infantry model is a minifigure occupying one Unit Base — `02-core-rules.md` (CORE-003) is the rule, and this document does not restate it.
```

with:

```
An infantry model is a minifigure occupying one Unit Base (`02-core-rules.md`, CORE-003).
```

  The citation moves to the comma form so the sentence ends on the reference rather than on a clause about itself. `CORE-003` remains the owner: it is what `DEP-001`, `DEP-004` and `TRN-002` cite, and this rule is one of its readers.

### Verification after section 14

- [x] 14.2 `grep -c -F "does not restate it" docs/17-infantry.md` — before: **1**, after: **0**.

- [x] 14.3 `python3 scripts/lint_ruleset.py` — `Checked 15 docs, no structural issues found.` The comma-form citation must still resolve; a new error means it does not.

- [x] 14.4 `python3 scripts/preflight.py` — all 12 checks PASS, unchanged from 13.2.

---

## 15. Review of pull request #112 — the stair ambiguity is closed

**This section changes a rule.** Everything before it transposes; this decides something the ruleset left undecided, at the maintainer's instruction. `proposal.md` and `design.md` are corrected in the same commit so that neither goes on claiming the change alters no gameplay.

Section 11 recorded the gap and declined to close it: `INF-009` said a stepped surface carries infantry only where no step is taller than one infantry crosses freely — 3 plate layers (`INF-006`) — while `INF-007` says an obstacle of 4 to 6 plate layers is climbed for 1 additional Action Point. A staircase with 5-plate steps was therefore either no path at all or a series of climbable obstacles, and no rule chose.

**The decision: a step is an obstacle, read exactly like any other.** There is no stair rule, because there was never a stair mechanic — `INF-006`, `INF-007` and `INF-008` already answer the question for any height, and applying them per step is simpler than the exception `INF-009` carried. `CODE_OF_DESIGN.md` Principle 11 and Principle 12.

**What actually changes in play:** a staircase with a step of 4 to 6 plate layers was impassable and now costs 1 additional Action Point. A step of 7 or more still stops the climb. Ordinary stairs, built from steps of a plate or two, cost nothing exactly as before — the common case is untouched, and the case that changes is the one no rule decided.

The asymmetry with `VEH-027` is deliberate and now said out loud: a vehicle reads a staircase as one obstacle of its total rise, infantry reads it step by step. That is not two answers to one question — it is the difference between taking the steps and not being able to.

**Both anchors were checked against the applied file**, and each occurs exactly once.

- [x] 15.1 In `docs/17-infantry.md`, `INF-009`, replace this anchor — the whole rule body. The heading is **not** part of the anchor:

```
Infantry may move normally over connected slopes and up stepped surfaces (`07-movement.md`, MOVE-012, MOVE-013), at no additional Action Point cost — they are ordinary terrain, not obstacles to climb. Distance travelled up either counts against the normal movement limit (INF-002).

A stepped surface carries infantry only where no single step is taller than an obstacle infantry crosses freely (INF-006).
```

with:

```
Infantry may move normally over connected slopes (`07-movement.md`, MOVE-012) at no additional Action Point cost: a slope is ordinary terrain, not an obstacle to climb.

A stepped surface (`07-movement.md`, MOVE-013) is climbed one step at a time, and each step is an obstacle read exactly like any other — 3 plate layers or fewer crossed freely (INF-006), 4 to 6 for 1 additional Action Point (INF-007), 7 or more not climbable at all (INF-008), which stops the climb at that step. Stairs built from steps of a plate or two therefore cost nothing.

Distance travelled up either counts against the normal movement limit (INF-002).

A vehicle reads the same staircase as one obstacle of its total rise rather than a series of small ones (`08-vehicles.md`, VEH-027): infantry takes the steps and a vehicle cannot.
```

  The rule keeps its name and its number. What it loses is the clause that made a stepped surface a special case, and with it the contradiction against `INF-007`.

- [x] 15.2 In `docs/17-infantry.md`, the `# Summary` section, replace this anchor — the fifth item:

```
5. Obstacles up to 3 plate layers are crossed freely, 4 to 6 cost 1 additional Action Point, and 7 or more need a slope, a stair or a ramp.
```

with:

```
5. Obstacles up to 3 plate layers are crossed freely, 4 to 6 cost 1 additional Action Point, and 7 or more need a slope, a stair or a ramp — and a stair's own steps are obstacles read the same way.
```

  `system/proposal-review.md` ("The Summary Is Part of the Rule"). The count is unchanged: still seven principles, still seven items.

### Verification after section 15

- [x] 15.3 `grep -c -F "carries infantry only where no single step" docs/17-infantry.md` — before: **1**, after: **0**. Task 15.1.

- [x] 15.4 `grep -c -F "each step is an obstacle read exactly like any other" docs/17-infantry.md` — before: **0**, after: **1**. Task 15.1.

- [x] 15.5 `grep -c "^[0-9]\. " docs/17-infantry.md` — **7**, before and after. The Summary still lists seven items, and 15.2 rewrites one rather than adding one.

- [x] 15.6 `python3 scripts/lint_ruleset.py` — `Checked 15 docs, no structural issues found.` Task 15.1 adds a citation of `VEH-027`, which must resolve.

- [x] 15.7 `python3 scripts/preflight.py` — all 12 checks PASS.

---

## 16. Design re-review of pull request #112 — two ruleset edits

Two of the three required items touch `docs/`; the third is prose in this change's own artifacts and carries no task.

**`CORE-006` illustrates a universal principle with an infantry-only example.** It closes: "A measurement may still decide **which** rule applies: an obstacle of 3 plate layers is crossed freely and one of 4 is climbed (`17-infantry.md`, INF-006, INF-007)." Those bands are infantry's. A vehicle reads its own Terrain Threshold (`VEH-021` – `VEH-024`) and never the 3/4 split. It is the same defect this change fixed in `CORE-005`, left standing one rule below it.

**Decision 16 left the multi-step case undecided.** `INF-007` charges 1 additional Action Point and says "a move over such an obstacle costs 2 AP in total" — written when one obstacle was the only case. `INF-009` now says every step is an obstacle. A staircase with three 5-plate steps in one move therefore has no stated cost. **The resolution is per step**, because that is what "each step is an obstacle read exactly like any other" already means; charging once would make the rule say each step is an obstacle and then treat several as one.

**No band, threshold or value is invented by either edit.**

**Both anchors were checked against the applied files**, and each occurs exactly once.

- [x] 16.1 In `docs/02-core-rules.md`, `CORE-006`, replace this anchor — the closing sentence of the rule's last paragraph:

```
A measurement may still decide **which** rule applies: an obstacle of 3 plate layers is crossed freely and one of 4 is climbed (`17-infantry.md`, INF-006, INF-007).
```

with:

```
A measurement may still decide **which** rule applies, and which measurement is read is the unit's own domain's rule — an obstacle's height for infantry (`17-infantry.md`, INF-006 through INF-008), a Terrain Threshold for a vehicle (`08-vehicles.md`, VEH-021).
```

  The concrete 3-and-4 example goes. It was true only of infantry, and `CORE-006` is the universal action-economy rule. What the sentence still says is the thing that is universal: a measurement selects the rule, and it never sets the price.

- [x] 16.2 In `docs/17-infantry.md`, `INF-009`, replace this anchor — the rule's second paragraph:

```
A stepped surface (`07-movement.md`, MOVE-013) is climbed one step at a time, and each step is an obstacle read exactly like any other — 3 plate layers or fewer crossed freely (INF-006), 4 to 6 for 1 additional Action Point (INF-007), 7 or more not climbable at all (INF-008), which stops the climb at that step. Stairs built from steps of a plate or two therefore cost nothing.
```

with:

```
A stepped surface (`07-movement.md`, MOVE-013) is climbed one step at a time, and each step is an obstacle read exactly like any other — 3 plate layers or fewer crossed freely (INF-006), 4 to 6 for 1 additional Action Point (INF-007), 7 or more not climbable at all (INF-008), which stops the climb at that step. Stairs built from steps of a plate or two therefore cost nothing.

**Each such step is charged.** A move crossing two steps of 4 to 6 plate layers spends the movement action's Action Point and 2 more, because it climbed two obstacles and not one — INF-007's "2 AP in total" counts one climb, which is the ordinary case rather than the only one. A staircase steep enough to charge for twice is one a unit may not finish in a single activation, which the 3 Action Points of `02-core-rules.md` (CORE-006) bound on their own.
```

  The first paragraph is a landmark and does not change. What is added is the answer to a question `INF-007` never had to face while one obstacle per move was the only shape available.

### Verification after section 16

- [x] 16.3 `grep -c -F "is crossed freely and one of 4 is climbed" docs/02-core-rules.md` — before: **1**, after: **0**. Task 16.1.

- [x] 16.4 `grep -c -F "Each such step is charged" docs/17-infantry.md` — before: **0**, after: **1**. Task 16.2.

- [x] 16.5 `grep -rn -F "INF-006, INF-007" docs/` — before: one hit, in `docs/02-core-rules.md`. After: **no output at all**. The range `INF-006 through INF-008` replaces it, and no other rule cited that pair.

- [x] 16.6 `python3 scripts/lint_ruleset.py` — `Checked 15 docs, no structural issues found.` Task 16.1 adds a citation of `VEH-021` from `02-core-rules.md`, which must resolve.

- [x] 16.7 `python3 scripts/preflight.py` — all 12 checks PASS.
