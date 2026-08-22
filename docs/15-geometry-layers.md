# StudCraft Geometry Layers

**Version:** 0.2.0 Draft

---

# Purpose

This document defines which parts of a LEGO model determine measured gameplay values and which parts are purely decorative.

Every model contains two layers:

* **Gameplay Geometry**
* **Visual Geometry**

The distinction applies to **measured values**. Physical checks use the model as it physically exists on the table.

---

# Design Philosophy

StudCraft follows one fundamental principle:

> **The Model Is The Rules.**

Not every LEGO element, however, contributes to a measured gameplay value.

**Gameplay Geometry** provides the physical measurements used by the rules. **Visual Geometry** provides additional physical detail without changing those measurements.

This separation allows players to build models with different levels of visual detail while preserving the same measured gameplay values.

Visual Geometry is still physically present on the table. It may therefore affect direct physical checks such as Line of Sight, Cover and access, even though it does not modify measured values.

The goal is simple:

> **Build freely without changing the measured rules of the model.**

---

# GEO-001 — Gameplay Geometry

**Gameplay Geometry** is the measurable physical information used by the rules.

Examples include:

* Platform dimensions
* Weapon dimensions
* Muzzle count and size
* Transport volume
* Movement geometry
* Component structural thickness

Derived values such as Range, Attack Dice, Impact Strength, Resistance and Capacity are calculated from Gameplay Geometry by their respective rules.

Gameplay Geometry is objective: the same model produces the same measurements.

---

# GEO-002 — Visual Geometry

**Visual Geometry** is physical LEGO that does not form part of Gameplay Geometry.

Examples include:

* Decorative slopes
* Pipes
* Exhausts
* Antennas
* Greebling
* Printed elements
* Cosmetic armour
* Decorative plates

Visual Geometry does not change a measured gameplay value.

A decorative element becomes Gameplay Geometry if it physically forms part of the structure or functional geometry measured by another rule.

---

# GEO-003 — Measured Values

Only Gameplay Geometry is used when calculating measured rule values.

Examples include:

* Range
* Attack Dice
* Impact Strength
* Resistance
* Weapon Capacity
* Transport Capacity
* Movement distance

Visual Geometry is ignored when calculating these values.

---

# GEO-004 — Physical Checks

Physical checks use the model exactly as it exists on the table, including Visual Geometry.

This applies to checks such as:

* Line of Sight
* Target visibility
* Cover
* Access openings

Therefore, Visual Geometry can physically block sight or access even though it does not modify a measured value.

A partially visible component is simply visible; Visual Geometry does not create an abstract cover bonus.

---

# GEO-005 — Functional Equivalence

Two models with identical Gameplay Geometry have identical measured gameplay values, regardless of their Visual Geometry.

Adding or removing Visual Geometry does not change those values unless the physical construction changes the Gameplay Geometry itself.

Every model may therefore be built as a **Minimum Representation** containing only the Gameplay Geometry required by the rules. Additional Visual Geometry may be added freely without changing its measured values.

---

# Examples

## Weapon

**Gameplay Geometry:** Length 4, Width 2, four Size-1 muzzles.
**Visual Geometry:** tubes, slopes, supports and decorative armour.

The weapon produces the same measured values regardless of its visual detail.

---

## Vehicle

**Gameplay Geometry:** Platform dimensions, weapon locations, movement geometry and transport capacity.
**Visual Geometry:** tracks, fenders, lights, exhausts and decorative armour.

The vehicle's measured values remain unchanged by its visual detail.

---

## Building

**Gameplay Geometry:** Footprint, height and functional doors and windows.
**Visual Geometry:** roof style, colours, facade details and decorative doors or windows.

The building's measured values remain unchanged by its visual detail.

---

# Summary

* **Gameplay Geometry** determines measured values.
* **Visual Geometry** does not modify measured values.
* **Both layers** are physically present for physical checks.
* Different visual designs can produce identical measured gameplay.
* Players may add decorative detail without changing measured values.

No hidden statistics are required. A player should be able to determine a model's gameplay values from its physical construction and the applicable rules.

---

> **The Model Is The Rules.**
