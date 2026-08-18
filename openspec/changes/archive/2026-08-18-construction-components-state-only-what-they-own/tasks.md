# Tasks — Construction Components state only what they own

## How to apply this change

Every anchor below is pre-change text, checked with exact-substring matching and occurring **exactly once in the file its task names**. Replace the whole anchor.

If an anchor returns anything other than 1, **stop and report it** rather than guessing which occurrence was meant. Never edit a document to make a verification command pass — report the mismatch instead.

### How to read the replacement blocks

The triple-backtick fence marks where the text starts and stops. **The fence is not part of the text** — do not write the backticks into the document.

A `#` heading or a `---` horizontal rule inside a fence is real markdown that must land in the file as markdown, not as quoted text. Tasks 3.1, 8.1, 10.1, 12.1 and 13.1 all contain real `# ` headings, and 13.1 contains a real `---` rule.

**This change is mostly deletion.** Fourteen of the sixteen replacement blocks are shorter than their anchor, and four of those consist of a single heading line that already appears at the end of the anchor — tasks 3.1, 8.1, 10.1 and 12.1. **That repeated heading is a landmark, not an edit** — it stays in the file exactly once, where it already is. Copy each block exactly.

**Two blocks are longer than their anchor: tasks 15.1 and 16.1.** Each adds text, and neither is a mistake.

**Nine rule IDs are deleted and nothing is renumbered.** `CMP-002`, `CMP-007`, `CMP-009`, `CMP-010`, `CMP-011`, `CMP-012`, `CMP-013`, `CMP-015` and `CMP-017` are removed outright. Do not renumber the rules that remain, do not close the gaps, and do not leave a stub saying a rule used to be there.

**Task 3.1 is a deletion and task 15.1 is the move that goes with it.** `CMP-002`'s minifigure sentence lands in `VEH-013` (`docs/08-vehicles.md`). Task 3.1 without task 15.1 is a deletion rather than a move.

**`TODO.md` is edited by exactly one task, 21.3, and by no other.** It quotes no text from `docs/05-construction-components.md`, so sections 1–20 leave it alone; it does quote `CORE-005`, which task 21.2 edits, and `scripts/check_todo_quotes.py` compares that blockquote character for character on every `preflight` run. Applying 21.2 without 21.3 turns the pull request red. A `TODO.md` edit demanded by any other task is a defect in this file — stop and report it.

- [x] 0.1 The branch is `construction-components-state-only-what-they-own`, named for this change directory, and it is branched from an up-to-date `main`.

### Scope and coverage

Seven ruleset documents, `assets/IMAGES.md`, `TODO.md` and one script comment, no spec delta: **forty-one edits and forty-two non-edit tasks** (0.1, 17.1 – 17.9, 18.6 – 18.10, 20.5 – 20.17, 21.5 – 21.10, 22.6 – 22.10 and 22.12 – 22.14).

- **Sections 1–17** are the change as proposed: sixteen edits, mapped in the table below.
- **Section 18** adds five repairs from the audit of the applied text, and brings in `assets/IMAGES.md`.
- **Sections 19 and 20** move six rules out of `docs/04-construction-standard.md` at the maintainer's decision — four into `docs/05-construction-components.md`, two absorbed by `WPN-001` — and bring in `docs/10-weapons.md`.
- **Section 21** repairs the four places outside those documents that pointed at `04-construction-standard.md` for something it no longer holds, and brings in `docs/02-core-rules.md`, `TODO.md` and `scripts/lint_ruleset.py`.
- **Sections 22 and 22b** are the audit of the moved text: five statements left describing rules their document no longer holds, and one sentence that had to be reordered to survive the ruleset linter.

**Anchors in sections 18 – 21 are post-change text wherever an earlier task touched the same line**, and each such task says so.

**Sections 19, 20 and 21 are one edit set: apply all fourteen edits, then run both verification blocks.** Their verification tasks are not independent — 20.8 greps `scripts/` and only passes once task 21.4 has landed, and the `PostToolUse` linter reports a dangling citation between a rule leaving one document and its citer being retargeted. Neither is a defect; both resolve when the companion task lands, and neither is ever a reason to edit a document to make a command pass.

| `proposal.md` item | Task | Path |
|---|---|---|
| `# Purpose` states the split | 1.1 | `docs/05-construction-components.md` |
| `CMP-001` trimmed, gains the qualifier | 2.1 | `docs/05-construction-components.md` |
| `CMP-002` retired | 3.1 | `docs/05-construction-components.md` |
| `CMP-003` trimmed | 4.1 | `docs/05-construction-components.md` |
| `CMP-004` trimmed | 5.1 | `docs/05-construction-components.md` |
| `CMP-005` trimmed | 6.1 | `docs/05-construction-components.md` |
| `CMP-006` trimmed | 7.1 | `docs/05-construction-components.md` |
| `CMP-007` retired | 8.1 | `docs/05-construction-components.md` |
| `CMP-008` trimmed | 9.1 | `docs/05-construction-components.md` |
| `CMP-009` – `CMP-013` retired | 10.1 | `docs/05-construction-components.md` |
| `CMP-014` trimmed | 11.1 | `docs/05-construction-components.md` |
| `CMP-015` retired | 12.1 | `docs/05-construction-components.md` |
| `CMP-016` trimmed, `CMP-017` retired | 13.1 | `docs/05-construction-components.md` |
| `CMP-018` trimmed | 14.1 | `docs/05-construction-components.md` |
| `CMP-002`'s minifigure sentence lands in `VEH-013` | 15.1 | `docs/08-vehicles.md` |
| Glossary ***Functional Component*** gains the qualifier | 16.1 | `docs/14-glossary.md` |
| `CMP-018` scales to multi-Unit-Base models | 18.1 | `docs/05-construction-components.md` |
| `CMP-018` labels its two terrain citations | 18.2 | `docs/05-construction-components.md` |
| `CMP-018` states when the check is made | 18.3 | `docs/05-construction-components.md` |
| Image candidates retargeted off `CMP-002` | 18.4, 18.5 | `assets/IMAGES.md` |
| `SCS-006` – `SCS-009` leave the Standard | 19.1 | `docs/04-construction-standard.md` |
| They land as `CMP-019` – `CMP-022` | 19.2 | `docs/05-construction-components.md` |
| `VEH-027` retargeted from `SCS-008` to `CMP-021` | 19.3 | `docs/08-vehicles.md` |
| `TRN-012` retargeted from `SCS-009` to `CMP-022` | 19.4 | `docs/09-transport.md` |
| Glossary ***Interactive Element*** retargeted to `CMP-019` | 19.5 | `docs/14-glossary.md` |
| `# Purpose` states the boundary | 19.6 | `docs/04-construction-standard.md` |
| `SCS-016`, `SCS-017` leave the Standard | 20.1 | `docs/04-construction-standard.md` |
| `WPN-001` absorbs both | 20.2, 20.3 | `docs/10-weapons.md` |
| Glossary ***Weapon Body*** retargeted to `WPN-001` | 20.4 | `docs/14-glossary.md` |
| `# Construction Principles` deleted | 21.1 | `docs/04-construction-standard.md` |
| `CORE-005` routes structures to both documents | 21.2 | `docs/02-core-rules.md` |
| `TODO.md`'s `CORE-005` quote follows it | 21.3 | `TODO.md` |
| The linter's comment stops citing `SCS-008` | 21.4 | `scripts/lint_ruleset.py` |
| `WPN-001`'s body definition admits a striking end | 22.1 | `docs/10-weapons.md` |
| `CMP-021`'s opening clause matches `MOVE-019`'s scope | 22.2 | `docs/05-construction-components.md` |
| `# Purpose` names the infantry base and settles structures | 22.3, 22.11 | `docs/04-construction-standard.md` |
| `# Design Philosophy` drops its orphaned line | 22.4 | `docs/04-construction-standard.md` |
| `# Summary` describes the five rules above it | 22.5 | `docs/04-construction-standard.md` |

**Untouched, deliberately:** the `# Design Philosophy` and `# Summary` sections of `docs/05-construction-components.md` (`design.md`, Decision 7), and the `# Design Philosophy` and `# Summary` sections of `docs/04-construction-standard.md` — of that document, sections 19–21 edit the `# Purpose` first line, delete four rules, delete two rules and delete `# Construction Principles`, and nothing else. `docs/16-damage-system.md` — every owner this change points at already states its rule in full. `SCS-002` and `SCS-010` – `SCS-013`, which are the battlefield and the base (`design.md`, Decision 13). `openspec/specs/` — this change ships no delta (`design.md`, Decision 8). `CHANGELOG.md` and every `**Version:**` header. Every archived change under `openspec/changes/archive/`.

---

## 1. `docs/05-construction-components.md` — `# Purpose`

- [x] 1.1 Replace this anchor — one line of the `# Purpose` section:

```
A component only has a game effect if it complies with the construction rules defined in this document.
```

with:

```
What a component does once it exists is defined by the system that owns that capability.
```

  The two lines above the anchor stay as they are. The replaced line became false when `04-construction-standard.md` took back the door, ramp and window construction requirements (`SCS-006` – `SCS-009`).

---

## 2. `docs/05-construction-components.md` — `CMP-001`

- [x] 2.1 In `CMP-001`, replace this anchor — the whole rule body below its heading:

```
A functional component is a physical part of a model that affects gameplay.

Examples include:

- Pilot
- Wheels
- Tracks
- Hover systems
- Weapons
- Doors
- Windows
- Ramps
- Turrets
- Cargo Bays

Decorative elements have no gameplay effect.
```

with:

```
A functional component is a physical part of a model that affects gameplay.

Decorative elements have no gameplay effect unless another rule gives them one.
```

  The `# CMP-001 — Functional Components` heading above the anchor is not part of it and does not change. **The first line is unchanged and is a landmark** — only the example list goes and only the qualifier is added. The definition stays word for word so that `docs/14-glossary.md`'s ***Functional Component*** entry, which restates it, stays true (`design.md`, Decision 6). The added qualifier is `CMP-015`'s, which task 12.1 retires.

---

## 3. `docs/05-construction-components.md` — `CMP-002`

- [x] 3.1 Replace this anchor — the whole `CMP-002` rule, its trailing `---`, and the heading of the rule below it:

```
# CMP-002 — Pilot

Every powered vehicle must include a visible Pilot position, occupied by a crew minifigure (`08-vehicles.md`, VEH-015).

Requirements:

- The Pilot must be a distinct, visible minifigure in an operating position.
- A decorative "empty seat" does not count as a Pilot.

Current gameplay:

- Required for all powered vehicles.
- Losing the Pilot disables vehicle movement (`08-vehicles.md`, VEH-013).
- Because the Pilot occupies a Unit Base, a powered vehicle must be built at least two Unit Bases in footprint (`08-vehicles.md`, VEH-001).

---

# CMP-003 — Wheels
```

with:

```
# CMP-003 — Wheels
```

  `CMP-003`'s heading is the landmark that ends the anchor; it stays in the file. **Task 15.1 must be applied with this one** — it is where the minifigure sentence goes. `VEH-013` owns the Pilot requirement, the movement consequence and the two-Unit-Base minimum.

---

## 4. `docs/05-construction-components.md` — `CMP-003`

- [x] 4.1 In `CMP-003`, replace this anchor — the whole rule body below its heading:

```
Wheels define wheeled locomotion.

Requirements:

- Must physically touch the ground.
- Must rotate freely.
- Decorative wheels are ignored.

Movement is resolved using the Vehicle Movement Rules. Terrain behaviour follows `08-vehicles.md` (VEH-022) — a wheel's axle height is its Terrain Threshold.
```

with:

```
A functional wheel must physically touch the ground and rotate freely.

Decorative wheels are ignored.
```

  `VEH-022` owns the Terrain Threshold, and `VEH-008` the steering.

---

## 5. `docs/05-construction-components.md` — `CMP-004`

- [x] 5.1 In `CMP-004`, replace this anchor — the whole rule body below its heading:

```
Tracks define tracked locomotion.

Requirements:

- Must be physically represented.
- Both sides should contain tracks.
- Decorative track details have no effect.

Pivot behavior follows `08-vehicles.md` (VEH-009), and terrain behaviour (VEH-022).
```

with:

```
Tracks must be physically represented, and both sides of the vehicle should contain them.

Decorative track details have no effect.
```

  **"should" stays "should".** Rewriting it to "must" would be a new construction requirement, not a trim.

---

## 6. `docs/05-construction-components.md` — `CMP-005`

- [x] 6.1 In `CMP-005`, replace this anchor. The two lines at the top are landmarks and are **not** an edit:

```
Hover vehicles replace wheels or tracks with hover emitters.

Hover components must be visually distinguishable.

Hover vehicles ignore wheel requirements. Pivot and movement behavior follows `08-vehicles.md` (VEH-011), and terrain behaviour (VEH-024) — the height of the hover assembly is the vehicle's Terrain Threshold, which is why these components must be visible.
```

with:

```
Hover vehicles replace wheels or tracks with hover emitters.

Hover components must be visually distinguishable.
```

  Both surviving lines are what `VEH-024` cites `CMP-005` for. `VEH-024` also states the deleted reason in full — "`CMP-005` already requires hover components to be visually distinguishable, and this is why" — so nothing about it is lost.

---

## 7. `docs/05-construction-components.md` — `CMP-006`

- [x] 7.1 In `CMP-006`, replace this anchor — the whole rule body below its heading:

```
Walkers use articulated legs instead of wheels or tracks.

Requirements:

- Legs must visibly support the vehicle.
- Decorative legs have no gameplay effect.

Pivot behavior follows `08-vehicles.md` (VEH-010), and terrain behaviour (VEH-023) — a walker's knee height is its Terrain Threshold.
```

with:

```
Walkers use articulated legs instead of wheels or tracks, and those legs must visibly support the vehicle.

Decorative legs have no gameplay effect.
```

  `VEH-023` cites `CMP-006` for the leg as built and owns knee height as the Terrain Threshold.

---

## 8. `docs/05-construction-components.md` — `CMP-007`

- [x] 8.1 Replace this anchor — the whole `CMP-007` rule, its trailing `---`, and the heading of the rule below it:

```
# CMP-007 — Weapons

Weapons are defined separately in:

`10-weapons.md`

Construction determines:

- Weapon length
- Range
- Attack Dice
- Firing direction

Only physically represented weapons may attack.

---

# CMP-008 — Turrets
```

with:

```
# CMP-008 — Turrets
```

  `CMP-008`'s heading is the landmark; it stays in the file. The owners: `WPN-003` (length), `WPN-005` (range), `WPN-006` (Attack Dice), `WPN-019` (firing direction), `WPN-001` and `CORE-014` (a weapon that is not physically represented is decorative).

---

## 9. `docs/05-construction-components.md` — `CMP-008`

- [x] 9.1 In `CMP-008`, replace this anchor — the whole rule body below its heading:

```
A turret is any rotating weapon mount.

Requirements:

- Must physically rotate.
- Rotation should be visible.
- Weapons mounted on the turret rotate with it.

Turrets follow the normal rotation rules.
```

with:

```
A turret is a weapon mount (`10-weapons.md`, WPN-009) that must physically rotate, and the weapons mounted on it rotate with it.
```

  The deleted last line named no rule. Vehicle rotation is `VEH-008` – `VEH-011`; re-aiming a rotating mount between shots is `DMG-018`.

---

## 10. `docs/05-construction-components.md` — `CMP-009` through `CMP-013`

- [x] 10.1 Replace this anchor — five whole rules with their `---` rules, and the heading of the rule below them. It is long; copy it whole:

```
# CMP-009 — Doors

Doors are interactive components.

Requirements:

- Must physically open and close.
- The opening must physically pass the models that use the door (CMP-018).
- Decorative doors have no gameplay effect.

Doors are used for:

- Embarking
- Disembarking
- Entering buildings
- Line of Sight

---

# CMP-010 — Ramps

Ramps function like doors.

Requirements:

- Must physically move.
- The opening the ramp gives access to must physically pass the models that use it (CMP-018).
- Decorative ramps have no effect.

Ramps may serve as vehicle access points.

---

# CMP-011 — Windows

Transparent LEGO elements represent windows, per the Construction Standard (`04-construction-standard.md`, SCS-009).

Windows:

- Allow visibility.
- May provide firing positions.
- Resolve Impacts like any other component (`16-damage-system.md`).

---

# CMP-012 — Cargo Bays

Cargo Bays transport Unit Bases.

Capacity is determined entirely by the available internal space, counted in Unit Bases (`09-transport.md`, TRN-003) and bounded by the compartment's clearance (TRN-019).

Cargo Bays never have an abstract transport value.

---

# CMP-013 — Crew Compartments

Driver positions are separate from Cargo Bays.

Crew compartments:

- Occupy Unit Bases.
- Are not counted as cargo capacity.
- Must be physically represented.

---

# CMP-014 — Shields
```

with:

```
# CMP-014 — Shields
```

  **This is one edit, not five.** `# CMP-014 — Shields` is the landmark that ends the anchor; it stays in the file. The owners: `SCS-007` and `SCS-006` (`CMP-009`), `SCS-008`, `SCS-006` and `MOVE-019` (`CMP-010`), `SCS-009`, `CORE-008`, `TRN-011` and `DMG-008` (`CMP-011`), `TRN-003`, `TRN-019` and `DEP-005` (`CMP-012`), `TRN-014` and `VEH-015` (`CMP-013`). **Task 14.1 must be applied with this one** — it removes `CMP-018`'s citations of the three rules deleted here.

---

## 11. `docs/05-construction-components.md` — `CMP-014`

- [x] 11.1 In `CMP-014`, replace this anchor — the whole rule body below its heading:

```
A Shield is defensive equipment carried by infantry — a physical component that may be targeted or may interpose to protect a component behind it, exactly like any other component (`16-damage-system.md`, DMG-007, DMG-012).

Requirements:

- Must be physically attached to the model.
- Must remain visible.
- Must occupy one hand.

A shield provides no bonus beyond being a component in the way — its own Resistance (DMG-003) determines what it takes to get through it.

A shield protects only what it physically stands between: one interposed between the attacker and a component protects it, one facing away blocks nothing. Orientation matters for that reason, not for any separate defensive bonus.
```

with:

```
A Shield is defensive equipment physically attached to an infantry model, visible on it, and occupying one hand (`02-core-rules.md`, CORE-015).

A shield protects only what it physically stands between: one interposed between the attacker and a component protects it (`16-damage-system.md`, DMG-007), one facing away blocks nothing. Orientation matters for that reason, not for any separate defensive bonus.
```

  The second paragraph is the one #104 put here, unchanged except for the `DMG-007` citation moving into it from the deleted first paragraph. **Do not delete it** — the glossary's ***Facing*** entry routes shield orientation to `CMP-014` (`design.md`, Decision 4). `DMG-001` and `DMG-012` own targeting, `DMG-003` owns Resistance, `CORE-015` owns the hand.

---

## 12. `docs/05-construction-components.md` — `CMP-015`

- [x] 12.1 Replace this anchor — the whole `CMP-015` rule, its trailing `---`, and the heading of the rule below it:

```
# CMP-015 — Accessories

Accessories are decorative unless another rule specifically defines them.

Examples:

- Antennas
- Lights
- Exhausts
- Mirrors
- Decorative panels

These components have no gameplay effect by default.

---

# CMP-016 — Functional Integrity
```

with:

```
# CMP-016 — Functional Integrity
```

  `CMP-016`'s heading is the landmark; it stays in the file. **Task 2.1 must be applied with this one** — it is where the "unless another rule" qualifier goes. `GEO-002` lists antennas, exhausts and decorative panels among its own examples of Visual Geometry.

---

## 13. `docs/05-construction-components.md` — `CMP-016` and `CMP-017`

- [x] 13.1 Replace this anchor — `CMP-016`'s whole body, the `---` below it, the whole `CMP-017` rule, its `---`, and the heading of the rule below it:

```
Removing a functional component immediately changes the model's capabilities.

Examples:

Pilot lost

→ Vehicle cannot move.

Remove Weapon

→ Weapon cannot attack.

Destroy Door

→ Door can no longer function normally.

Gameplay always reflects the current physical model.

---

# CMP-017 — Component Visibility

Functional components should be easy to identify.

Players should not need to ask whether a component exists.

Good construction communicates functionality clearly.

---

# CMP-018 — Access Openings
```

with:

```
Removing a functional component immediately changes what the model can do.

Gameplay always reflects the current physical model.

---

# CMP-018 — Access Openings
```

  **The `---` and the `# CMP-018 — Access Openings` heading are real markdown and must land in the file** — they are the ones that already separate `CMP-017` from `CMP-018`, and after this edit they separate `CMP-016` from `CMP-018`. `CMP-016`'s heading above the anchor is untouched. `CMP-017` is deleted whole (`design.md`, Decision 7): its aspiration is already in this document's `# Design Philosophy`, and every rule needing visibility states its own objective requirement.

---

## 14. `docs/05-construction-components.md` — `CMP-018`

- [x] 14.1 In `CMP-018`, replace this anchor — the whole rule body below its heading. It is long; copy it whole:

```
An access point's opening must physically pass the models that use it. With the component in its open position, if a model cannot be moved through the opening, that component is decorative for that model and has no gameplay effect (CMP-009, CMP-010; `09-transport.md`, TRN-007). What must pass is the model's Unit Base, not the loose plastic — which is what makes the check a measurement rather than an attempt.

**Width** is not a judgment call. Every model on the table stands on Unit Bases (`02-core-rules.md`, CORE-001), and a model's 4-stud edge is its front (`02-core-rules.md`, CORE-002) — so the opening must be at least as wide as the front edge of whatever passes through it. Infantry is invariably 1 Unit Base, 4 studs, whatever the minifigure carries and whether it stands or sits (`09-transport.md`, TRN-002). A vehicle W Unit Bases wide needs `W × 4` studs.

**Height** is measured the same way. An opening that passes infantry must be at least 13 plate layers clear — one Unit Base tall (`02-core-rules.md`, CORE-001). A model taller than one Unit Base is measured by its own height in plate layers.

Measure the *clear* opening rather than the nominal frame: an element hanging in the doorway reduces it exactly as much as the frame does — see `15-geometry-layers.md` (GEO-004). Anything protruding beyond the model's own Unit Base is repositioned; the doorway is measured against the Unit Base either way. A hinged 1 × 2 tile covers an opening less than one brick high, which is why it moves and is still not a door.

The check is made against the opening, not against the approach. A rear ramp is a surface a model climbs — whether it can be climbed is the Terrain Threshold's question (`08-vehicles.md`, VEH-022 – VEH-024). What a model must fit *through* is the hatch at the top of it. A perfectly drivable ramp leading to a portal too low for the vehicle is not an access point.

What must pass depends on what the component is declared to do. A roof hatch used to embark and disembark (`09-transport.md`, TRN-007) must pass the models that use it that way. The same hatch used as a firing port (`09-transport.md`, TRN-011) carries no such requirement in that role, and an observation slit that is only ever a firing port passes nothing but a line of sight. Windows (CMP-011) are exempt unless declared as access points.

A component may therefore be an access point for one model and decorative for another — a hatch that passes a minifigure but not a motorcycle. The plastic has not changed; the question has.

Openings are checked when the model is built, like every other construction requirement in this document.
```

with:

```
An access opening, with the component in its open position, must physically pass the Unit Base of each model that uses it (`02-core-rules.md`, CORE-001), measured against the front edge that model leads with (`02-core-rules.md`, CORE-002). An opening that does not pass a model is decorative for that model and has no gameplay effect (CMP-001). What must pass is the Unit Base, not the loose plastic, which is what makes the check a measurement rather than an attempt.

Measure the *clear* opening rather than the nominal frame: an element hanging in the doorway reduces it exactly as much as the frame does — see `15-geometry-layers.md` (GEO-004).

The check is made against the opening, not against the approach. Whether a model can reach the opening is the terrain's question (`07-movement.md`, MOVE-011; `08-vehicles.md`, VEH-021); what must pass through it is this rule's.

A component may therefore be an access point for one model and decorative for another — a hatch that passes a minifigure but not a motorcycle. The plastic has not changed; the question has.

Openings are checked when the model is built, like every other construction requirement in this document.
```

  Five paragraphs replace eight. What goes is arithmetic `CORE-001`, `CORE-003` and `TRN-002` own, and two paragraphs restating `VEH-021` – `VEH-024`, `MOVE-019`, `TRN-007` and `TRN-011` (`design.md`, Decision 5). What survives from the deleted **Width** paragraph is its conclusion — the opening is measured against the front edge the model leads with — because no other rule states which face of a Unit Base an opening is checked against, and `MOVE-003` lets a model travel sideways (`design.md`, Decision 5). The citations of `CMP-009`, `CMP-010` and `CMP-011` go with the rules task 10.1 retires. `CORE-001` is still cited, for the Unit Base it defines.

---

## 15. `docs/08-vehicles.md` — `VEH-013`

- [x] 15.1 In `VEH-013`, replace this anchor — the rule's first sentence:

```
Every powered vehicle — wheeled, tracked, walker, or hover (VEH-012) — requires a Pilot to move, a crew member (VEH-015) occupying a visible operating position.
```

with:

```
Every powered vehicle — wheeled, tracked, walker, or hover (VEH-012) — requires a Pilot to move, a crew member (VEH-015) occupying a visible operating position. The Pilot is a minifigure physically placed in that position; a decorative empty seat is not a Pilot.
```

  **This is an addition, not a deletion**, and the rest of `VEH-013` is untouched. The added sentence is the one thing `CMP-002` stated that no other rule does: `VEH-015` says vehicles carry crew members without saying what a crew member is made of (`design.md`, Decision 3). Task 3.1 removes it from `05-construction-components.md`.

---

## 16. `docs/14-glossary.md` — ***Functional Component***

- [x] 16.1 In the ***Functional Component*** entry, replace this anchor:

```
Decorative elements have none. See `05-construction-components.md`, CMP-001.
```

with:

```
Decorative elements have none unless another rule gives them one. See `05-construction-components.md`, CMP-001.
```

  The entry restates `CMP-001`, which task 2.1 qualifies. The ***Facing*** and ***Access Opening*** entries were checked and need no edit.

---

## 17. Verification

Run these after every edit above. Each is a bare command; none of them edits anything. Where a count is given, it is the count observed on the pre-change tree, so a mismatch means the edit did not land.

- [x] 17.1 `python3 scripts/preflight.py` passes.

- [x] 17.2 `grep -n "^# CMP-" docs/05-construction-components.md` lists exactly nine headings, in this order: `CMP-001`, `CMP-003`, `CMP-004`, `CMP-005`, `CMP-006`, `CMP-008`, `CMP-014`, `CMP-016`, `CMP-018`. Any other count, or any heading renumbered to close a gap, is a defect. Before this change the same command listed eighteen.

- [x] 17.3 `grep -rn "CMP-0" docs/` returns **no line naming a retired ID** — `CMP-002`, `CMP-007`, `CMP-009`, `CMP-010`, `CMP-011`, `CMP-012`, `CMP-013`, `CMP-015` or `CMP-017`. Read the output rather than counting it. Expected: the nine surviving headings, `CMP-018`'s own reference to `CMP-001`, and citations from `docs/07-movement.md` (`MOVE-018`, `MOVE-019`), `docs/08-vehicles.md` (`VEH-023`, `VEH-024` twice, `VEH-030`), `docs/09-transport.md` (`TRN-007`, `TRN-011`), `docs/15-geometry-layers.md` (`GEO-004`) and `docs/14-glossary.md` (three entries). A line naming a retired ID is an edit that did not land; stop and report it.

- [x] 17.4 `python3 scripts/rule.py refs CMP-001 CMP-005 CMP-006 CMP-014 CMP-018` — every citer printed must name a rule that still exists. `CMP-014` prints "is cited by nothing"; **that is correct**, since its only citer is the glossary's ***Facing*** entry and `rule.py` reads the rule graph rather than the glossary. `CMP-001` prints one citer, `CMP-018` — the `(CMP-001)` reference task 14.1 puts in its first paragraph. Task 17.3 is what covers the glossary.

  **This task was written wrong and is corrected here.** It claimed `CMP-001` would print "is cited by nothing", which contradicted task 14.1's own replacement text. The applier ran the command, reported the mismatch and edited nothing, which is the required behaviour and worked.

- [x] 17.5 `python3 scripts/check_id_stability.py` reports no renumbered and no reused ID. Nine retirements are expected and are not reported.

- [x] 17.6 `grep -c -F "Terrain Threshold" docs/05-construction-components.md` returns `0`. It returned `4` before tasks 4.1, 6.1, 7.1 and 14.1.

- [x] 17.7 `grep -rn "CMP-0" system/ README.md CODE_OF_DESIGN.md CONTRIBUTING.md AGENTS.md TODO.md` returns **nothing**, exactly as it did before this change. A hit means a task edited a file this change does not touch; stop and report it.

The two checks below each confirm one addition landed. Deletions are visible in the diff; an addition that was skipped looks exactly like a change applied correctly, which is what these catch.

- [x] 17.8 `grep -c -F "The Pilot is a minifigure physically placed in that position" docs/08-vehicles.md` returns `1`. It returned `0` before task 15.1.

- [x] 17.9 `grep -c -F "have none unless another rule gives them one" docs/14-glossary.md` returns `1`. It returned `0` before task 16.1.

---

## 18. Repairs from the audit of the applied text

Sections 1–17 are the change as proposed. These five edits come from the audit of the result, and **their anchors are post-change text** — three of them name sentences task 14.1 put there. Apply them after section 17, not before.

**One new file joins the change: `assets/IMAGES.md`.** It cites `CMP-002`, which task 3.1 retired, and nothing checks it: `scripts/lint_ruleset.py` validates only the rule named beside a filename in the image table, and task 17.7's grep does not reach `assets/`.

- [x] 18.1 In `docs/05-construction-components.md`, `CMP-018`, replace this anchor — the rule's whole first paragraph, as task 14.1 left it:

```
An access opening, with the component in its open position, must physically pass the Unit Base of each model that uses it (`02-core-rules.md`, CORE-001), measured against the front edge that model leads with (`02-core-rules.md`, CORE-002). An opening that does not pass a model is decorative for that model and has no gameplay effect (CMP-001). What must pass is the Unit Base, not the loose plastic, which is what makes the check a measurement rather than an attempt.
```

with:

```
An access opening, with the component in its open position, must physically pass every model that uses it. What must pass is the Unit Bases that model occupies (`02-core-rules.md`, CORE-001) rather than its loose plastic, which is what makes the check a measurement rather than an attempt: the opening must be at least as wide as the model's front edge (`02-core-rules.md`, CORE-002) and as tall as the model stands. An opening that does not pass a model is decorative for that model and has no gameplay effect (CMP-001).
```

  Two defects in one paragraph. **"the Unit Base of each model" fits only infantry** — a vehicle occupies `W × D` Unit Bases (`VEH-001`) and stands several tall (`VEH-028`), so the rule decided nothing for the models `MOVE-018`, `TRN-007` and `VEH-030` read it for. **"the front edge that model leads with" contradicts `MOVE-003`**, which lets a model lead with its side edge; read the other way it reopens the sideways loophole the clause exists to close. The replacement states the edge unconditionally, which is what `CMP-018` said before this change, and adds height without restating a number — `CORE-001` still owns the conversion.

- [x] 18.2 In `docs/05-construction-components.md`, `CMP-018`, replace this anchor — the rule's third paragraph:

```
The check is made against the opening, not against the approach. Whether a model can reach the opening is the terrain's question (`07-movement.md`, MOVE-011; `08-vehicles.md`, VEH-021); what must pass through it is this rule's.
```

with:

```
The check is made against the opening, not against the approach. Whether a model can reach the opening is the terrain's question — `07-movement.md` (MOVE-011) for infantry, `08-vehicles.md` (VEH-021) for vehicles — and what must pass through the opening is this rule's.
```

  The two citations sat side by side with nothing to choose between them. `VEH-021` exists partly to say `MOVE-011` is the infantry rule and must not be used for a vehicle, and `system/proposal-review.md` records a vehicle rule pointed at that same infantry rule as a shipped defect.

- [x] 18.3 In `docs/05-construction-components.md`, `CMP-018`, replace this anchor — the rule's last line:

```
Openings are checked when the model is built, like every other construction requirement in this document.
```

with:

```
An opening is checked against the plastic as it stands: at the bench, like every other construction requirement in this document, and again whenever the model changes (CMP-016).
```

  With `CMP-017` gone from between them, `CMP-016` ("Gameplay always reflects the current physical model") is now the rule immediately above this line, and a build-time-only check reads as its contradiction. Nothing new is decided — `CMP-016` already governs a model that changes in play, and this says so where the collision is visible.

- [x] 18.4 In `assets/IMAGES.md`, under the `VEH-030` bullet, replace this anchor:

```
This list already declines DMG-018 as "a binary construction check made directly on the model" and CMP-002 and CMP-008 as verified by looking at the build.
```

with:

```
This list already declines DMG-018 as "a binary construction check made directly on the model" and VEH-013 and CMP-008 as verified by looking at the build.
```

- [x] 18.5 In `assets/IMAGES.md`, replace this anchor — one whole bullet:

```
- **CMP-002 (Pilot), CMP-008 (Turrets)** — "A visible minifigure in an operating position" and "a mount that physically rotates" are easily verified by looking at the model; nothing in the text is hard to picture.
```

with:

```
- **VEH-013 (Pilot), CMP-008 (Turrets)** — "A visible minifigure in an operating position" and "a mount that physically rotates" are easily verified by looking at the model; nothing in the text is hard to picture.
```

  Only the rule ID changes; the quoted phrase is still what the Pilot rule says, because task 15.1 moved it to `VEH-013`. **Do not move the bullet** — the declined list is not sorted by document.

### Verification

- [x] 18.6 `grep -rn "CMP-002" assets/ docs/ system/ README.md TODO.md` returns **nothing**. Before tasks 18.4 and 18.5 it returned two lines, both in `assets/IMAGES.md`.

- [x] 18.7 `grep -c -F "as tall as the model stands" docs/05-construction-components.md` returns `1`, and `grep -c -F "the front edge that model leads with" docs/05-construction-components.md` returns `0`.

- [x] 18.8 `grep -c -F "(MOVE-011) for infantry" docs/05-construction-components.md` returns `1`.

- [x] 18.9 `grep -c -F "and again whenever the model changes" docs/05-construction-components.md` returns `1`.

- [x] 18.10 `python3 scripts/preflight.py` passes, all 12 checks.

---

## 19. The interactive elements move to Construction Components

Sections 1–18 removed the mirror by retiring the copy in `05-construction-components.md`. This section moves the survivor, at the maintainer's decision, so that one criterion decides which document a construction rule lives in:

> **`04-construction-standard.md` is the battlefield and the base every model stands on. `05-construction-components.md` is every functional part of a model.**

A door is a part of a model — `DMG-001` targets it, `CMP-016` removes it — so `SCS-006` – `SCS-009` move to `05-construction-components.md` under **new** rule IDs. The old IDs are retired, never reissued (`system/documentation-standards.md`, Naming Conventions), and the new ones append after `CMP-018` because rule IDs ascend within a document and are never renumbered to read better.

**Each moved rule is trimmed on arrival, exactly as every rule already in `05-construction-components.md` was.** A move is not a licence to import text this change removed twelve lines above: `CMP-019` arrives without `SCS-006`'s example list (an index of `CMP-018`, `CMP-020` and `CMP-021`, and the glossary's ***Interactive Element*** entry lists the same six elements) and without its "Decoration alone has no gameplay effect", which `CMP-001` now states **qualified**. `CMP-020` and `CMP-021` gain the `CMP-018` pointer the retired `CMP-009` and `CMP-010` carried, which is a pointer rather than the copy those rules were. Three citations are retargeted and one `# Purpose` line is rewritten.

- [x] 19.1 In `docs/04-construction-standard.md`, replace this anchor — four whole rules with their `---` rules, and the heading of the rule below them. It is long; copy it whole:

```
# SCS-006 — Interactive Elements

Interactive elements must physically exist. What operating one costs is defined in `02-core-rules.md`, CORE-007.

Examples:

- Doors
- Hatches
- Ramps
- Drawbridges
- Elevators
- Gates

Decoration alone has no gameplay effect.

---

# SCS-007 — Doors

Functional doors:

- must open physically
- may close physically

---

# SCS-008 — Ramps

A ramp must physically rotate or lower.

---

# SCS-009 — Windows

Transparent LEGO elements represent windows.

---

# SCS-010 — Walls
```

with:

```
# SCS-010 — Walls
```

  **This is one edit, not four.** `# SCS-010 — Walls` is the landmark that ends the anchor; it stays in the file. **Task 19.2 must be applied with this one** — it is where all four rules land. Section 19 without 19.2 deletes them.

- [x] 19.2 In `docs/05-construction-components.md`, replace this anchor — `CMP-018`'s last line, the `---` below it, and the `# Summary` heading:

```
An opening is checked against the plastic as it stands: at the bench, like every other construction requirement in this document, and again whenever the model changes (CMP-016).

---

# Summary
```

with:

```
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

A ramp must physically rotate or lower, and the opening it gives access to must physically pass the models that use it (CMP-018).

---

# CMP-022 — Windows

Transparent LEGO elements represent windows.

---

# Summary
```

  **The first line and the `# Summary` heading are landmarks and stay in the file exactly once**, where they already are. Everything between them is new. Do not renumber `CMP-019` – `CMP-022` to sit nearer the rules they resemble.

  **Three differences from task 19.1's anchor, all deliberate.** `CMP-019` drops `SCS-006`'s six-item example list and its unqualified "Decoration alone has no gameplay effect" — `CMP-001` states that rule qualified, twelve lines above, and importing the absolute form would reinstate what task 2.1 removed. `CMP-020` and `CMP-021` each gain a `CMP-018` clause, which is the pointer the retired `CMP-009` and `CMP-010` carried; `CMP-018` is now in the same document, so it is a pointer and not the copy those rules were. `CMP-022` is `SCS-009` word for word.

- [x] 19.3 In `docs/08-vehicles.md`, `VEH-027`, replace this anchor:

```
The angle does not matter and is never measured: LEGO slope elements (`04-construction-standard.md`, SCS-011) and a lowered ramp (SCS-008) bound it by their own construction.
```

with:

```
The angle does not matter and is never measured: LEGO slope elements (`04-construction-standard.md`, SCS-011) and a lowered ramp (`05-construction-components.md`, CMP-021) bound it by their own construction.
```

  One citation moves document. `SCS-011` stays where it is — a slope is terrain.

- [x] 19.4 In `docs/09-transport.md`, `TRN-012`, replace this anchor:

```
Transparent LEGO elements represent windows or viewports (`04-construction-standard.md`, SCS-009).
```

with:

```
Transparent LEGO elements represent windows or viewports (`05-construction-components.md`, CMP-022).
```

- [x] 19.5 In `docs/14-glossary.md`, the ***Interactive Element*** entry, replace this anchor:

```
See `02-core-rules.md`, CORE-007 and `04-construction-standard.md`, SCS-006.
```

with:

```
See `02-core-rules.md`, CORE-007 and `05-construction-components.md`, CMP-019.
```

- [x] 19.6 In `docs/04-construction-standard.md`, `# Purpose`, replace this anchor — its first line:

```
The StudCraft Construction Standard (SCS) defines the building conventions used throughout the game.
```

with:

```
The StudCraft Construction Standard (SCS) defines how the battlefield is built, and the base every model stands on. What a model's own functional parts must be is `05-construction-components.md`; how a weapon is built is `10-weapons.md`.
```

  **This is the one place the criterion is written down.** It is not repeated in `05-construction-components.md`, whose own `# Purpose` already states what that document holds. The three lines below the anchor are untouched.

---

## 20. The weapon-construction rules move to Weapons

Same criterion, applied to the two rules the Construction Standard held about weapons. `10-weapons.md` owns weapons; `WPN-001` already requires a body, a muzzle and a mounting point.

- [x] 20.1 In `docs/04-construction-standard.md`, replace this anchor — two whole rules with their `---` rules, and the section heading below them:

```
# SCS-016 — Functional Weapons

Every weapon must include at least one visible functional muzzle.

Valid muzzle pieces are defined in `10-weapons.md` (WPN-002).

---

# SCS-017 — Weapon Body

Every muzzle must connect to a weapon body.

The body represents:

- barrel
- mechanism
- support

Decoration does not count.

---

# Construction Principles
```

with:

```
# Construction Principles
```

  `# Construction Principles` is the landmark; it stays in the file. **Tasks 20.2, 20.3 and 20.4 must be applied with this one.** Both rules are absorbed by `WPN-001`, which already lists a weapon body, a muzzle and a mounting point as a weapon's three requirements. **No new rule ID is created** — `SCS-017` does not become `WPN-022`.

- [x] 20.2 In `docs/10-weapons.md`, `WPN-001`, replace this anchor — three bullets:

```
- A weapon body.
- At least one functional muzzle.
- A physical mounting point.
```

with:

```
- A weapon body — the structure carrying the muzzle: barrel, mechanism, support. Decoration does not count.
- At least one visible functional muzzle (WPN-002).
- A physical mounting point.
```

  This is what `SCS-016` and `SCS-017` said, in the rule that already said the rest of both. `visible` is `SCS-016`'s only word `WPN-001` lacked; the body clause is `SCS-017`'s definition, with its three-item list written inline. The third bullet is a landmark and is not an edit.

- [x] 20.3 In `docs/10-weapons.md`, `WPN-001`, replace this anchor — the sentence below the bullets:

```
Melee weapons replace the functional muzzle with a functional striking end, as defined in `12-melee.md` (MEL-013).
```

with:

```
Melee weapons replace the functional muzzle with a functional striking end, visible in the same way, as defined in `12-melee.md` (MEL-013).
```

  `SCS-016` required a visible muzzle of **every** weapon; `WPN-001`'s bullet list governs ranged weapons only, so without this clause the melee striking end would lose a requirement it had. `MEL-013` states none of its own.

- [x] 20.4 In `docs/14-glossary.md`, the ***Weapon Body*** entry, replace this anchor:

```
See `04-construction-standard.md`, SCS-017 and `10-weapons.md`, WPN-003, WPN-018.
```

with:

```
See `10-weapons.md`, WPN-001, WPN-003, WPN-018.
```

  The entry's own definition — "barrel, mechanism and support" — is `SCS-017`'s, and after task 20.2 `WPN-001` states it. The citation follows it there.

### Verification

- [x] 20.5 `grep -n "^# SCS-" docs/04-construction-standard.md` lists exactly five headings: `SCS-002`, `SCS-010`, `SCS-011`, `SCS-012`, `SCS-013`. Before section 19 it listed eleven.

- [x] 20.6 `grep -n "^# CMP-" docs/05-construction-components.md` lists exactly thirteen headings, in this order: `CMP-001`, `CMP-003` – `CMP-006`, `CMP-008`, `CMP-014`, `CMP-016`, `CMP-018`, `CMP-019`, `CMP-020`, `CMP-021`, `CMP-022`.

- [x] 20.7 `grep -rn "SCS-0" docs/` names only `SCS-002`, `SCS-010`, `SCS-011`, `SCS-012` and `SCS-013`. A line naming `SCS-006` – `SCS-009`, `SCS-016` or `SCS-017` is a retarget that did not land; stop and report it.

- [x] 20.8 `grep -rn "SCS-0" system/ README.md CODE_OF_DESIGN.md CONTRIBUTING.md AGENTS.md TODO.md assets/ scripts/` returns **nothing**. `scripts/` is in the list because `scripts/lint_ruleset.py` cited `SCS-008` and `SCS-011` in a code comment until task 21.4; it is the same omission that made section 18 necessary, one directory further on. `tests/` is deliberately not in the list: `tests/test_build_index.py` uses `SCS-001` as a synthetic fixture string that never reads `docs/`.

- [x] 20.9 `grep -c -F "CMP-021" docs/08-vehicles.md` returns `1`, `grep -c -F "CMP-022" docs/09-transport.md` returns `1`, and `grep -c -F "CMP-019" docs/14-glossary.md` returns `1`. Each returned `0` before tasks 19.3, 19.4 and 19.5.

- [x] 20.10 `python3 scripts/check_id_stability.py` reports **no moved and no reused ID**. Six retirements (`SCS-006` – `SCS-009`, `SCS-016`, `SCS-017`) and four additions (`CMP-019` – `CMP-022`) are expected: a retirement is not reported, and an addition above its document's highest existing number is not a reuse.

The six checks below confirm the moved text landed. Sections 19 and 20 delete six rules and write four; a block transcribed with a line dropped passes every count above, which is what these catch.

- [x] 20.11 `grep -c -F "Interactive elements must physically exist" docs/05-construction-components.md` returns `1`, and `grep -c -F "Interactive elements must physically exist" docs/04-construction-standard.md` returns `0`.

- [x] 20.12 `grep -c -F "must open physically" docs/05-construction-components.md` returns `1`, `grep -c -F "A ramp must physically rotate or lower" docs/05-construction-components.md` returns `1`, and `grep -c -F "Transparent LEGO elements represent windows" docs/05-construction-components.md` returns `1`.

- [x] 20.13 `grep -c -F "(CMP-018)" docs/05-construction-components.md` returns `2` — one in `CMP-020`, one in `CMP-021`. It returned `0` after task 10.1.

- [x] 20.14 `grep -c -F "Drawbridges" docs/05-construction-components.md` returns `0`, and `grep -c -F "Decoration alone has no gameplay effect" docs/05-construction-components.md` returns `0`. **Both are `0` on purpose** — `CMP-019` is trimmed on arrival, and a `1` means `SCS-006`'s example list or its unqualified decoration line was imported.

- [x] 20.15 `grep -c -F "barrel, mechanism, support" docs/10-weapons.md` returns `1`, `grep -c -F "At least one visible functional muzzle" docs/10-weapons.md` returns `1`, and `grep -c -F "visible in the same way" docs/10-weapons.md` returns `1`. Each returned `0` before tasks 20.2 and 20.3.

- [x] 20.16 `grep -c -F "defines how the battlefield is built" docs/04-construction-standard.md` returns `1`. It returned `0` before task 19.6 — the only check that task 19.6 landed.

- [x] 20.17 `python3 scripts/preflight.py` passes, all 12 checks.

---

## 21. What the move falsified elsewhere

Four edits outside the two documents that swapped rules. Each is a sentence that pointed at `04-construction-standard.md` for something it no longer holds.

**`TODO.md` is edited by this section**, which the preamble at the top of this file forbids. That instruction was written before sections 19–21 existed and is corrected here: `TODO.md` quotes `CORE-005` verbatim, `scripts/check_todo_quotes.py` compares it character for character on every `preflight` run, and task 21.2 edits the sentence it quotes. Applying 21.2 without 21.3 turns the pull request red.

- [x] 21.1 In `docs/04-construction-standard.md`, replace this anchor — the whole `# Construction Principles` section and the heading below it:

```
# Construction Principles

Every functional game element should satisfy three conditions.

## Visible

Players can immediately identify it.

---

## Physical

It exists on the LEGO model.

---

## Interactive

It affects gameplay.

---

# Summary
```

with:

```
# Summary
```

  `# Summary` is the landmark; it stays in the file. The section governs "every functional game element", and after tasks 19.1 and 20.1 this document holds no rule about one. **Its `Visible` condition is the adjudication this change retires `CMP-017` for** — "Players can immediately identify it" and "Functional components should be easy to identify" are the same sentence, and keeping one while deleting the other for being subjective is the inconsistency (`design.md`, Decision 14). `05-construction-components.md`'s `# Design Philosophy` states the aspiration; `CORE-014` and `CORE-008` own the two enforceable halves.

- [x] 21.2 In `docs/02-core-rules.md`, `CORE-005`, replace this anchor — the rule's first sentence:

```
Structures follow the Construction Standard.
```

with:

```
A structure's walls, slopes, stairs and platforms follow `04-construction-standard.md`; its doors, windows and other functional parts follow `05-construction-components.md`.
```

  The rest of `CORE-005` — the sentence about structure-specific damage and Deployment Volume — is untouched. **Task 21.3 must be applied with this one.**

- [x] 21.3 In `./TODO.md`, under the ***Structure-wide damage and Deployment Volume occupation*** heading, replace this anchor — the blockquote that quotes `CORE-005`. The `> ` prefix is real markdown, `TODO.md`'s own format, and must land in the file:

```
> Structures follow the Construction Standard. Structure-specific damage (collapse, breaching walls) and Deployment Volume occupation for scenario-placed structures are not yet defined — a structure's individual components (doors, windows, walls) already resolve Impacts through the standard Component Damage System (`16-damage-system.md`) like any other component; only structure-wide consequences (e.g. a building collapsing) remain future work.
```

with:

```
> A structure's walls, slopes, stairs and platforms follow `04-construction-standard.md`; its doors, windows and other functional parts follow `05-construction-components.md`. Structure-specific damage (collapse, breaching walls) and Deployment Volume occupation for scenario-placed structures are not yet defined — a structure's individual components (doors, windows, walls) already resolve Impacts through the standard Component Damage System (`16-damage-system.md`) like any other component; only structure-wide consequences (e.g. a building collapsing) remain future work.
```

  **The path is `TODO.md` at the repository root — not under `docs/`.** The quote must match `CORE-005` as task 21.2 leaves it. The gap itself does not close, so the entry stays; only the quoted first sentence changes.

- [x] 21.4 In `scripts/lint_ruleset.py`, replace this anchor — four lines of a code comment. Their leading `            # ` is part of the text:

```
            # The parenthesised form leaves up to 80 characters between the
            # filename and the ID, which is what lets "see `10-weapons.md`
            # (WPN-002)" and the continuation form "(`04-construction-standard.md`,
            # SCS-011) and a lowered ramp (SCS-008)" both match. That window also
```

with:

```
            # The parenthesised form leaves up to 80 characters between the
            # filename and the ID, which is what lets "see `10-weapons.md`
            # (WPN-002)" and a continuation form, where a second bare ID follows
            # the cited one after a few words of prose, both match. That window also
```

  **No code changes — this is a comment.** Its worked example was `VEH-027`'s sentence, which task 19.3 rewrites, and it named `SCS-008`, which task 19.1 retires. The mechanism it explains is unchanged, so the example is replaced by a description of the same shape rather than by another live sentence that would go stale the same way.

### Verification

- [x] 21.5 `grep -c -F "Every functional game element should satisfy three conditions" docs/04-construction-standard.md` returns `0`. It returned `1` before task 21.1.

- [x] 21.6 `grep -c -F "Structures follow the Construction Standard" docs/02-core-rules.md` returns `0`, and the same command against `TODO.md` returns `0`. Each returned `1` before tasks 21.2 and 21.3.

- [x] 21.7 `python3 scripts/check_todo_quotes.py` passes. It fails if task 21.2 or task 21.3 was applied without the other.

- [x] 21.8 `python3 scripts/lint_ruleset.py` passes — `docs/04-construction-standard.md` still carries `# Purpose`, `# Design Philosophy` and `# Summary`, which are the three sections the linter checks.

- [x] 21.9 `python3 -m pytest tests/ -q` passes, unchanged by task 21.4.

- [x] 21.10 `python3 scripts/preflight.py` passes, all 12 checks.

  **Task 21.9's command needs the project's virtualenv:** `python3 -m pytest` finds no pytest under the system interpreter. Run `.venv/bin/pytest tests/ -q`, or rely on `preflight.py`, which runs the suite itself and reports it as `Tests`.

---

## 22. Repairs from the audit of the moved text

Sections 19–21 moved six rules and left six statements that no longer match what their document holds. **Their anchors are post-change text** — three name lines sections 19–21 wrote. Apply after section 21.

Four of the six are in `docs/04-construction-standard.md`, and they are the same defect the change is about, committed against the document it emptied: prose describing rules that are no longer there.

- [x] 22.1 In `docs/10-weapons.md`, `WPN-001`, replace this anchor — one bullet, as task 20.2 left it:

```
- A weapon body — the structure carrying the muzzle: barrel, mechanism, support. Decoration does not count.
```

with:

```
- A weapon body — the structure carrying the muzzle or striking end: barrel, mechanism, support. Decoration does not count.
```

  Two lines below, `WPN-001` states that melee weapons have a striking end **instead of** a muzzle — so as task 20.2 left it, the ruleset's only definition of a weapon body was one no melee weapon could satisfy, while `MEL-014` reads melee reach from Weapon Length and `WPN-003` measures Weapon Length on the Weapon Body. `WPN-002` and `MEL-013` both state that a striking end plays exactly the muzzle's role; this makes the definition agree with them.

- [x] 22.2 In `docs/05-construction-components.md`, `CMP-021`, replace this anchor — the whole rule body, as task 19.2 wrote it:

```
A ramp must physically rotate or lower, and the opening it gives access to must physically pass the models that use it (CMP-018).
```

with:

```
A ramp must physically rotate or lower. Where it leads to an opening, that opening must physically pass the models that use it (CMP-018).
```

  `MOVE-019` states the same requirement conditionally — "**Where the ramp leads to an opening**" — and not every ramp leads to one: `VEH-027` cites `CMP-021` for a ramp a vehicle climbs to reach a height. The unconditional form was inherited from the retired `CMP-010`, which predates `MOVE-019`'s hedge.

- [x] 22.3 In `docs/04-construction-standard.md`, `# Purpose`, replace this anchor — its first line, as task 19.6 wrote it:

```
The StudCraft Construction Standard (SCS) defines how the battlefield is built, and the base every model stands on. What a model's own functional parts must be is `05-construction-components.md`; how a weapon is built is `10-weapons.md`.
```

with:

```
The StudCraft Construction Standard (SCS) defines how the battlefield is built, and the infantry base every minifigure stands on (SCS-002). What a model's own functional parts must be is `05-construction-components.md`; how a weapon is built is `10-weapons.md`. A structure is both at once, and `02-core-rules.md` (CORE-005) splits it: its walls, slopes, stairs and platforms are built here, its doors, windows and other functional parts are components.
```

  Two repairs to the boundary. **"the base every model stands on" was false** — `SCS-002` is infantry-only, and no rule requires a vehicle to be built on a base. **The criterion returned two answers for a building**, which is battlefield and model at once, and that is precisely the case that produced the `SCS`/`CMP` mirror this change removes; `CORE-005` already settles it, so the boundary now points there instead of leaving the reader to guess.

- [x] 22.4 In `docs/04-construction-standard.md`, `# Design Philosophy`, replace this anchor. The first line is a landmark and is **not** an edit:

```
Construction choices directly affect gameplay.

Every functional element should be physically represented.
```

with:

```
Construction choices directly affect gameplay.
```

  This is the deleted `# Construction Principles`' `Physical` condition in one sentence, and task 21.1's stated reason for deleting that section applies to it word for word: the document holds no rule about a functional element. `CORE-014` owns the checkable half.

- [x] 22.5 In `docs/04-construction-standard.md`, replace this anchor — the whole body of `# Summary`:

```
StudCraft models are not miniatures.

They are game systems built from LEGO.

Construction defines gameplay.

Gameplay rewards good construction.

The battlefield itself communicates the game state.
```

with:

```
Terrain is built, not declared: a wall, a slope, a stair or a platform affects play because the plastic is there.

Every infantry model stands on the same base, which is where every measurement starts.

The battlefield itself communicates the game state.
```

  The `# Summary` heading above the anchor is not part of it. The four deleted lines summarise the ruleset's construction ethos rather than this document — and after the move, "models" is `05-construction-components.md`'s subject. `01-foundations.md` states the same claim for the whole game. The replacement summarises the five rules that are actually above it; the last line is a landmark and is unchanged.

### Verification

- [x] 22.6 `grep -c -F "A weapon body — the structure carrying the muzzle or striking end" docs/10-weapons.md` returns `1`, and `grep -c -F "the structure carrying the muzzle:" docs/10-weapons.md` returns `0`.

  **This task was written wrong and is corrected here.** It first grepped the bare phrase "the muzzle or striking end" and expected `1`; `WPN-016` and `WPN-021` have used that phrase since before this change, so the correct answer was `3`. The applier ran it, reported the mismatch and edited nothing, which is the required behaviour. The grep above names the whole bullet, which occurs once.

- [x] 22.7 `grep -c -F "Where it leads to an opening" docs/05-construction-components.md` returns `1`.

- [x] 22.8 `grep -c -F "the infantry base every minifigure stands on" docs/04-construction-standard.md` returns `1`, `grep -c -F "CORE-005" docs/04-construction-standard.md` returns `1`, and `grep -c -F "Every functional element should be physically represented" docs/04-construction-standard.md` returns `0`.

- [x] 22.9 `grep -c -F "StudCraft models are not miniatures" docs/04-construction-standard.md` returns `0`, and `grep -c -F "The battlefield itself communicates the game state" docs/04-construction-standard.md` returns `1` — the one line of the old Summary that stays.

- [x] 22.10 `python3 scripts/preflight.py` passes, all 12 checks. `docs/04-construction-standard.md` still carries `# Purpose`, `# Design Philosophy` and `# Summary`. **Task 22.11 must be applied first** — task 22.3's sentence fails the ruleset linter as written.

---

## 22b. The `# Purpose` sentence has to survive the linter

Task 22.3's replacement text is valid English and invalid to `scripts/lint_ruleset.py`. Its `CROSS_REF_RE` binds a parenthesised rule ID to a filename in backticks up to 80 characters earlier, non-greedily, and the sentence puts `` `10-weapons.md` `` 52 characters before `(CORE-005)` — so the linter reads the line as claiming `10-weapons.md` states `CORE-005`, and fails with `04-construction-standard.md: references 10-weapons.md (CORE-005), which does not exist`. (That message is quoted inline rather than fenced: `scripts/check_task_anchors.py` reads any fenced block in this file as an anchor to look for, and a fenced error message is one it will never find.)

The rule is right and the sentence is wrong. Reordering it so no other filename sits between `` `02-core-rules.md` `` and `(CORE-005)` fixes it without changing what it says. **This is why task 22.10 could not pass, and it is not the applier's defect.**

- [x] 22.11 In `docs/04-construction-standard.md`, `# Purpose`, replace this anchor — its first line, as task 22.3 left it:

```
The StudCraft Construction Standard (SCS) defines how the battlefield is built, and the infantry base every minifigure stands on (SCS-002). What a model's own functional parts must be is `05-construction-components.md`; how a weapon is built is `10-weapons.md`. A structure is both at once, and `02-core-rules.md` (CORE-005) splits it: its walls, slopes, stairs and platforms are built here, its doors, windows and other functional parts are components.
```

with:

```
The StudCraft Construction Standard (SCS) defines how the battlefield is built, and the infantry base every minifigure stands on (SCS-002). A structure is both battlefield and model at once, and `02-core-rules.md` (CORE-005) splits it: its walls, slopes, stairs and platforms are built here, its doors, windows and other functional parts are components (`05-construction-components.md`). How a weapon is built is `10-weapons.md`.
```

  Same three claims, reordered. `(CORE-005)` now follows `` `02-core-rules.md` `` with nothing between them, `` `05-construction-components.md` `` carries no ID, and `` `10-weapons.md` `` ends the line with no parenthesis after it.

### Verification

- [x] 22.12 `python3 scripts/lint_ruleset.py` passes. It reported one issue before this task.

- [x] 22.13 `grep -c -F "A structure is both battlefield and model at once" docs/04-construction-standard.md` returns `1`, and `grep -c -F "how a weapon is built is" docs/04-construction-standard.md` returns `0` — the clause moved to the end of the line and changed case.

- [x] 22.14 `python3 scripts/preflight.py` passes, all 12 checks.
