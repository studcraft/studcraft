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

An infantry model is a minifigure occupying one Unit Base — `02-core-rules.md` (CORE-003) is the rule, and this document does not restate it.

Every infantry model is built on the base required by `02-core-rules.md` (CORE-001). Which edge of that base is its front is settled by the universal Facing rule (`02-core-rules.md`, CORE-002).

That orientation is what every direction below is measured relative to — the general rule is `07-movement.md` (MOVE-001).

---

# INF-002 — Forward Movement

Standard infantry movement:

**Up to 12 studs forward, in multiples of 3 studs**

12 is the maximum, not a fixed distance — a unit may move 3, 6, 9 or 12 studs, or stay put.

The step size is the Unit Base's depth (`02-core-rules.md`, CORE-001): moving forward crosses the 3-stud axis, so forward movement counts whole base-depths, exactly as side movement counts whole base-widths of 4 (INF-003). Both numbers come from the base itself, so a player can measure either by laying spare infantry bases end to end.

The distance is measured from the face of the base that leads in the direction of travel — the front face moving forward, the rear face moving backward (INF-004), the corresponding side face moving sideways (INF-003). This is the general measurement rule (`07-movement.md`, MOVE-003) read against an infantry base.

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

Infantry reaches an off-axis position by combining a forward or backward move with a side move, each its own movement action (`07-movement.md`, MOVE-007).

Example — instead of moving diagonally:

- Forward 6 studs (1 AP)
- Left 4 studs (1 AP)

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

A vertical face taller than INF-008's threshold cannot be climbed unless a slope, stair or ramp physically reaches it. Those are the three legal access points INF-008 lists, and no other construction grants access.

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

---

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
