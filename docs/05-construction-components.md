# StudCraft Construction Components

**Version:** 0.2.0 Draft

---

# Purpose

This document defines the functional construction components used in StudCraft.

Components are physical LEGO elements that provide gameplay functionality.

What a component does once it exists is defined by the system that owns that capability.

---

# Design Philosophy

StudCraft uses construction instead of hidden statistics.

Players should be able to identify the purpose of every important component simply by looking at the model.

Components define capabilities.

They do not define abstract statistics.

---

# CMP-001 — Functional Components

A functional component is a physical part of a model that affects gameplay.

Decorative elements have no gameplay effect unless another rule gives them one.

---

# CMP-003 — Wheels

A functional wheel must physically touch the ground and rotate freely.

Decorative wheels are ignored.

---

# CMP-004 — Tracks

Tracks must be physically represented, and both sides of the vehicle should contain them.

Decorative track details have no effect.

---

# CMP-005 — Hover System

Hover vehicles replace wheels or tracks with hover emitters.

Hover components must be visually distinguishable.

---

# CMP-006 — Walkers

Walkers use articulated legs instead of wheels or tracks, and those legs must visibly support the vehicle.

Decorative legs have no gameplay effect.

---

# CMP-008 — Turrets

A turret is a weapon mount (`10-weapons.md`, WPN-009) that must physically rotate, and the weapons mounted on it rotate with it.

---

# CMP-014 — Shields

A Shield is defensive equipment physically attached to an infantry model, visible on it, and occupying one hand (`02-core-rules.md`, CORE-015).

A shield protects only what it physically stands between: one interposed between the attacker and a component protects it (`16-damage-system.md`, DMG-007), one facing away blocks nothing. Orientation matters for that reason, not for any separate defensive bonus.

---

# CMP-016 — Functional Integrity

Removing a functional component immediately changes what the model can do.

Gameplay always reflects the current physical model.

---

# CMP-018 — Access Openings

An access opening, with the component in its open position, must physically pass every model that uses it. What must pass is the Unit Bases that model occupies (`02-core-rules.md`, CORE-001) rather than its loose plastic, which is what makes the check a measurement rather than an attempt: the opening must be at least as wide as the model's front edge (`02-core-rules.md`, CORE-002) and as tall as the model stands. An opening that does not pass a model is decorative for that model and has no gameplay effect (CMP-001).

Measure the *clear* opening rather than the nominal frame: an element hanging in the doorway reduces it exactly as much as the frame does — see `15-geometry-layers.md` (GEO-004).

The check is made against the opening, not against the approach. Whether a model can reach the opening is the terrain's question — `17-infantry.md` (INF-008) for infantry, `08-vehicles.md` (VEH-021) for vehicles — and what must pass through the opening is this rule's.

A component may therefore be an access point for one model and decorative for another — a hatch that passes a minifigure but not a motorcycle. The plastic has not changed; the question has.

An opening is checked against the plastic as it stands: at the bench, like every other construction requirement in this document, and again whenever the model changes (CMP-016).

---

# CMP-019 — Interactive Elements

Interactive elements must physically exist. What operating one costs is defined in `02-core-rules.md`, CORE-007.

---

# CMP-020 — Doors

Functional doors:

- must open physically
- may close physically

The opening must physically pass the models that use the door (CMP-018).

---

# CMP-021 — Ramps

A ramp must physically rotate or lower. Where it leads to an opening, that opening must physically pass the models that use it (CMP-018).

---

# CMP-022 — Windows

Transparent LEGO elements represent windows.

---

# Summary

StudCraft components provide gameplay through physical construction.

Components define what a model can do.

If a component is removed, damaged or destroyed, the model immediately behaves differently.

StudCraft therefore treats every important brick as a meaningful part of the game.

---

> **Every Brick Matters.**