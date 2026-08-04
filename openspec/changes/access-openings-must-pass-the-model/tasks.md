## 0. Setup

- [x] 0.1 Work on branch `access-openings-must-pass-the-model` (`openspec/config.yaml` requires one branch per proposal).

### How to read the replacement blocks

Replacement text is shown as a markdown blockquote so it is visually separable from the instructions. **The `> ` prefix is not part of the text.** Strip it from every line before writing into the document.

Where a block contains a `#` heading, a bullet list or bold markers, those are part of the text and must be written as real markdown.

### What "the body of a rule" means

Everything between that rule's `#` heading line and the `---` that ends it. **Never change, remove or renumber an existing heading.** One rule ID is added (`CMP-018`); none is renumbered. Task 6.2 checks the count.

### Scope

Five documents change, plus one spec delta that already exists in this change and must not be edited:

| Path | What changes |
|---|---|
| `docs/05-construction-components.md` | `CMP-009`, `CMP-010`, new `CMP-018` |
| `docs/09-transport.md` | `TRN-007`, `TRN-011` |
| `docs/07-movement.md` | `MOVE-018`, `MOVE-019` |
| `docs/15-geometry-layers.md` | `GEO-004` |
| `docs/14-glossary.md` | new `Access Opening` entry |

Nothing else. `TODO.md` is not touched (task 5.4).

### One idea, stated once

The rule lives in `CMP-018`. Every other edit **cites** it in one short sentence and adds no reasoning of its own. Do not restate the minifigure example, the opening-versus-approach distinction, or the declared-function rule anywhere but `CMP-018`. Task 6.5 checks this.

### Coverage

| Item | Task |
|---|---|
| `CMP-018` carries the rule | 1.3 |
| `CMP-009` doors cite it | 1.1 |
| `CMP-010` ramps cite it | 1.2 |
| `TRN-007` access points cite it | 2.1 |
| `TRN-011` firing ports exempted | 2.2 |
| `MOVE-018` doorways cite it | 3.1 |
| `MOVE-019` ramps cite it | 3.2 |
| `GEO-004` gains the third physical check | 4.1 |
| Glossary entry | 4.2 |

---

## 1. `docs/05-construction-components.md`

### 1.1 `CMP-009` — Doors

- [x] 1.1.1 In `CMP-009`, add one bullet to the existing "Requirements:" list, after "Must physically open and close.":

> - The opening must physically pass the models that use the door (CMP-018).

- [x] 1.1.2 Change nothing else in `CMP-009`. The "Doors are used for:" list and the Action Point line stay exactly as they are.

### 1.2 `CMP-010` — Ramps

- [x] 1.2.1 In `CMP-010`, add one bullet to the existing "Requirements:" list, after "Must physically move.":

> - The opening the ramp gives access to must physically pass the models that use it (CMP-018).

- [x] 1.2.2 Change nothing else in `CMP-010`.

### 1.3 Add `CMP-018` at the end of the rules

- [x] 1.3.1 Insert the following **after** `CMP-017`'s closing `---` and **before** the `# Summary` heading:

> # CMP-018 — Access Openings
>
> An access point's opening must physically pass the models that use it. With the component in its open position, if a model cannot be moved through the opening, that component is decorative for that model and has no gameplay effect (CMP-009, CMP-010; `09-transport.md`, TRN-007).
>
> This is a physical check, not a measured value (`15-geometry-layers.md`, GEO-004): take the model and pass it through. No dimension is written here because none would hold — a minifigure, a droid, a cargo crate and a motorcycle each measure themselves.
>
> Infantry is the common case. A minifigure is roughly 4 studs across the arms and 4 bricks tall, so a hinged 1 × 2 tile is not a door: it moves, and nothing can walk through it.
>
> The check is made against the opening, not against the approach. A rear ramp is a surface a model climbs — whether it can be climbed is the Terrain Threshold's question (`08-vehicles.md`, VEH-022 – VEH-024). What a model must fit *through* is the hatch at the top of it. A perfectly drivable ramp leading to a portal too low for the vehicle is not an access point.
>
> What must pass depends on what the component is declared to do. A roof hatch used to embark and disembark (`09-transport.md`, TRN-007) must pass the models that use it that way. The same hatch used as a firing port (`09-transport.md`, TRN-011) carries no such requirement in that role, and an observation slit that is only ever a firing port passes nothing but a line of sight. Windows (CMP-011) are exempt unless declared as access points.
>
> A component may therefore be an access point for one model and decorative for another — a hatch that passes a minifigure but not a motorcycle. The plastic has not changed; the question has.
>
> Openings are checked when the model is built, like every other construction requirement in this document.

- [x] 1.3.2 Before writing the minifigure sentence, **verify the two figures against a real minifigure** — roughly 4 studs across the arms, roughly 4 bricks tall. They are illustrative and carry no rule weight, but a wrong number in a rulebook invites correction. If either is wrong, correct it in place and note the correction in your report; do not change the surrounding sentence structure.

---

## 2. `docs/09-transport.md`

### 2.1 `TRN-007` — Access Points

- [x] 2.1.1 In `TRN-007`, insert the following line immediately **after** "Only functional access points may be used." and **before** the "Examples:" line:

> An access point's opening must physically pass the models that use it; one that does not is decorative (`05-construction-components.md`, CMP-018).

- [x] 2.1.2 Leave the examples list and the "Decorative access points have no gameplay effect." line unchanged.

### 2.2 `TRN-011` — Firing Ports

- [x] 2.2.1 In `TRN-011`, add the following as a new paragraph immediately **after** "The opening determines the firing arc." and **before** the closing `---`:

> A firing port passes a line of sight, not a model, so the access-opening requirement does not apply to it (`05-construction-components.md`, CMP-018). A roof hatch serving as both a firing port and an access point must satisfy that requirement in its access-point role only.

- [x] 2.2.2 Change nothing else in `TRN-011`. The list of openings — Windows, Gun ports, Roof hatches, Observation slits — stays as it is.

---

## 3. `docs/07-movement.md`

### 3.1 `MOVE-018` — Doors

- [x] 3.1.1 Replace the line "Closed doors block movement. Once opened, the doorway becomes a valid movement path." with:

> Closed doors block movement. Once opened, the doorway becomes a valid movement path for any model the opening physically passes (`05-construction-components.md`, CMP-018).

- [x] 3.1.2 Leave the Action Point line unchanged.

### 3.2 `MOVE-019` — Ramps

- [x] 3.2.1 Replace the line "A lowered ramp immediately becomes usable terrain and is a legal access point (MOVE-011, MOVE-014)." with:

> A lowered ramp immediately becomes usable terrain and is a legal access point (MOVE-011, MOVE-014). Where the ramp leads to an opening, that opening must physically pass the model as well (`05-construction-components.md`, CMP-018).

- [x] 3.2.2 Leave the Action Point line unchanged.

---

## 4. `docs/15-geometry-layers.md` and `docs/14-glossary.md`

### 4.1 `GEO-004` — a third physical check

- [x] 4.1.1 In `GEO-004`, add one bullet to the existing list, after the Cover bullet:

> - Access openings (`05-construction-components.md`, CMP-018): whether a model physically passes through an opening is settled by passing it, and decorative elements narrowing that opening count exactly as much as structural ones.

- [x] 4.1.2 Change nothing else in `GEO-004`. The two paragraphs below the list already explain why Visual Geometry participates in physical checks, and they cover the new bullet without amendment.

### 4.2 Glossary

- [x] 4.2.1 Add an `## Access Opening` entry at the **end** of the definitions in `docs/14-glossary.md`, immediately after the last existing entry and its `---` separator, and **before** the closing `> **Every Brick Matters.**` line. The glossary is in append order, not alphabetical — verify by reading it, then follow it.

- [x] 4.2.2 Match the surrounding style: a `## ` heading, one paragraph, a document-and-ID citation, then a `---` separator.

> ## Access Opening
>
> The gap a model passes through when it uses a door, hatch or ramp. An access point whose opening does not physically pass a given model is decorative for that model and has no gameplay effect. See `05-construction-components.md` (CMP-018).

---

## 5. Verify only — make no edit

- [x] 5.1 **The spec delta is already written.** `openspec/changes/access-openings-must-pass-the-model/specs/geometry-layers/spec.md` modifies the *Visual Geometry Still Applies to Physical Checks* requirement and carries all three scenarios. Do not edit it. Task 6.9 checks it stays coherent.
- [x] 5.2 `TRN-015` (Emergency Exit) is untouched. It already states that passengers with no functional access point remaining are trapped, which covers the construction case without amendment.
- [x] 5.3 `TRN-003`, `TRN-004` and `CMP-012` are untouched. Interior capacity and layout are a separate question from passage.
- [x] 5.4 `TODO.md` is not edited. Nothing here declares a gap; this change closes one.
- [x] 5.5 `CMP-001`'s list of functional components is untouched. Doors and ramps stay on it — the change adds a requirement, it does not remove the category.
- [x] 5.6 No Action Point cost changes anywhere. Opening a door still costs 1 AP (`CORE-007`), embarking still costs 1 AP per Unit Base (`TRN-005`).

---

## 6. Verify

- [x] 6.1 Run `python3 scripts/lint_ruleset.py`; confirm no structural issues. This also checks that every `(CMP-NNN)`, `(TRN-NNN)`, `(MOVE-NNN)`, `(GEO-NNN)` and `(VEH-NNN)` reference added above resolves.
- [x] 6.2 Run `grep -rcE '^#{1,2} [A-Z]{3,4}-[0-9]{3} ' docs/ | awk -F: '{s+=$2} END {print s}'` and confirm **220** — one more than the 219 before, that one being `CMP-018`.
- [x] 6.3 Run `grep -n "^# CMP-" docs/05-construction-components.md` and confirm `CMP-001` through `CMP-018` appear once each, ascending, no gaps.
- [x] 6.4 Run `grep -rn "CMP-018" docs/` and confirm it is cited from `CMP-009`, `CMP-010`, `TRN-007`, `TRN-011`, `MOVE-018`, `MOVE-019`, `GEO-004` and the glossary — eight citations plus the rule's own heading and its internal self-references.
- [x] 6.5 Run `grep -rn "minifigure is roughly\|1 × 2 tile\|not against the approach" docs/` and confirm each phrase appears **once**, all inside `CMP-018`. The reasoning must not be duplicated into the citing rules.
- [x] 6.6 Run `grep -rn "line of sight, not a model" docs/` and confirm exactly one hit, in `TRN-011`. Without it, this change reads as invalidating every observation slit in the game.
- [x] 6.7 Confirm no numeric value changed anywhere in `docs/`. The `4 studs` and `4 bricks` in `CMP-018` are new illustrative text, not a changed value.
- [x] 6.8 Run `git diff --stat main...HEAD` and confirm exactly these paths changed: the five documents listed under **Scope**, plus the five files under `openspec/changes/access-openings-must-pass-the-model/`.
- [x] 6.9 Run `python3 scripts/check_delta_coverage.py` and confirm it passes. It must report the `geometry-layers` MODIFIED requirement as checked, with no dropped scenarios — the delta keeps both original scenarios and adds a third.
- [x] 6.10 Run `openspec validate access-openings-must-pass-the-model` and confirm it passes.
