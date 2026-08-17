# StudCraft Geometry Layers

**Version:** 0.2.0 Draft

---

# Purpose

This document defines how StudCraft interprets a LEGO model: which parts of it feed the rules, and which parts exist purely for artistic expression.

Every model splits into two layers:

- Gameplay Geometry
- Visual Geometry

Only Gameplay Geometry feeds a measured rule value. Visual Geometry exists exclusively for artistic expression.

This separation lets players build with any level of visual detail while preserving identical measured gameplay values.

---

# Design Philosophy

StudCraft follows one fundamental principle:

> **The Model Is The Rules.**

However, not every LEGO element contributes to gameplay.

Only measurable geometry generates gameplay. Everything else is visual representation.

---

# GEO-001 — Gameplay Geometry

Gameplay Geometry is the minimum physical information required to play the game. It consists only of measurable properties.

Examples include:

- Platform footprint
- Platform dimensions
- Weapon length
- Weapon width
- Muzzle count
- Muzzle sizes
- Transport volume
- Movement geometry
- Component structural thickness (Resistance, `16-damage-system.md` DMG-003) — measured the same way for every component, moulded or built

Derived values (Weapon Front Footprint, Range, Attack Dice, Impact Strength, Weapon Capacity, and similar) are not listed separately — they are always computed from the entries above, per `10-weapons.md`.

"Platform" here means the same thing it means in `10-weapons.md` (WPN-004): a Unit Base or a vehicle.

Gameplay Geometry is objective. Any player should obtain the same measurements from the same model.

---

# GEO-002 — Visual Geometry

Visual Geometry contains every decorative element that does not modify Gameplay Geometry.

Examples include:

- Decorative slope elements
- Pipes
- Technic details
- Decorative armour
- Exhausts
- Antennas
- Greebling
- Printed parts
- Colors
- Cosmetic plates

A plate or panel only counts as Visual Geometry if it is not part of the structural cross-section an Impact must cross (`16-damage-system.md`, DMG-003) — decorative armour bolted on top of, rather than forming part of, a component's structural wall does not add to its Resistance. A plate that *does* sit in that cross-section is Gameplay Geometry, however decorative it looks, the same way a decorative-looking muzzle is still a functional one if it meets WPN-002.

Its purpose is purely aesthetic. Players are free to build with any artistic style.

---

# GEO-003 — Gameplay Geometry Determines Measured Values

Only Gameplay Geometry is used when computing a measured rule value: Range, Attack Dice, Impact Strength, Resistance, Weapon Capacity, Transport Capacity, and Movement distance.

Visual Geometry never contributes to any of these values.

Example: a weapon with a decorative antenna, exhaust, or greebling attached — not part of its Weapon Body, Weapon Front, or muzzles — has exactly the same Range, Attack Dice, and Impact Strength as if the decorative element were absent.

---

# GEO-004 — Visual Geometry and Physical Checks

Some existing rules are not measured values — they are direct physical checks against the whole model as it sits on the table:

- Line of Sight (`02-core-rules.md`, CORE-008, CORE-009): visibility is whatever can physically be seen from the attacker's point of view.
- Cover (`02-core-rules.md`, CORE-010): binary — a component completely hidden cannot be selected as a target; a partially visible component has no separate cover level.
- Access openings (`05-construction-components.md`, CMP-018): the clearance an opening must provide is read from the Unit Base, but whether a given opening provides it is settled against the plastic as built — decorative elements narrowing that opening count exactly as much as structural ones.

These checks are not exceptions to "The Model Is The Rules" — they are the model's rules. Visual Geometry is real plastic on the table, so it physically blocks sight lines exactly like Gameplay Geometry does. It is only ignored when computing a measured value (GEO-003); it is never ignored when a rule asks what can physically be seen right now.

Players should keep this in mind when adding detail: a large decorative element can legitimately block a shot entirely, or complete the concealment that makes a component untargetable, simply because it is physically there. It does not grant a "cover bonus" — cover has none to grant (CORE-010).

---

# GEO-005 — Functional Equivalence

Two models with identical Gameplay Geometry produce identical measured values, regardless of differences in Visual Geometry.

This equivalence does not extend to physical checks (Line of Sight, Cover — see GEO-004), which may still differ based on Visual Geometry.

Example:

Weapon A — Plate 4×2, four 1×1 round plates.

Weapon B — detailed brick-built weapon with tubes, slopes, Technic details.

If both models have Weapon Length 4, Weapon Width 2, and four Size-1 muzzles, every measured value they produce is identical: same Range, same Attack Dice, same Impact Strength. Their Line of Sight and Cover outcomes can still differ if one is visually bulkier than the other.

---

# GEO-006 — Minimum Representation

Every model has a valid minimum representation consisting only of the Gameplay Geometry required by the rules, with no Visual Geometry.

This allows any player to build fully playable models using a small LEGO collection.

---

# GEO-007 — Detailed Representation

A model built with Visual Geometry added on top of a valid Minimum Representation remains valid, provided its Gameplay Geometry is unchanged.

A model does not become invalid, and its measured values do not change, solely as a result of adding Visual Geometry.

---

# Examples

## Weapon

Gameplay Geometry: Length 4, Width 2, four Size-1 muzzles.

Visual Geometry: tubes, slopes, barrel supports, armour plating.

Gameplay remains identical.

---

## Vehicle

Gameplay Geometry: Platform dimensions, Weapon locations, Weapon Capacity, Movement geometry, Transport capacity.

Visual Geometry: tracks, fenders, lights, exhausts, decorative armour.

Gameplay remains identical.

---

## Building

Gameplay Geometry: Footprint, Height, Functional Doors, Functional Windows.

Visual Geometry: roof style, colors, decorative facade, decorative (non-functional) doors and windows.

Gameplay remains identical.

---

# Summary

Every model contains Gameplay Geometry, and may contain Visual Geometry.

- Gameplay Geometry defines the rules; Visual Geometry defines appearance.
- Gameplay Geometry must be measurable; Visual Geometry is unrestricted.
- Only Gameplay Geometry affects any measured rule value (Range, Attack Dice, Impact Strength, Weapon Capacity, Transport Capacity, Movement distance) — GEO-003.
- Visual Geometry still counts for direct physical checks (Line of Sight, Cover, access openings) — GEO-004.
- Visually different models may be functionally identical — GEO-005.
- Every playable model has a minimum valid representation — GEO-006.
- Players may increase visual detail without affecting measured gameplay values — GEO-007.

No hidden statistics are required. A player should understand every model simply by looking at the LEGO model.

---

> **The Model Is The Rules.**
