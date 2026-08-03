## 0. Setup

- [ ] 0.1 Work on branch `vehicle-minimum-footprint` (`openspec/config.yaml` requires one branch per proposal).

### How to read the replacement blocks

Replacement text is shown as a markdown blockquote so it is visually separable from the instructions. **The `> ` prefix is not part of the text.** Strip it from every line before writing into the document.

### What "the body of a rule" means

Where a task says *replace the entire body of `RULE-NNN`*, the body is everything between that rule's heading line and the `---` that ends it. `CORE-004` uses a `##` heading; the vehicle and component rules use `#`. **Never change, remove or renumber a heading.** No rule ID changes here; task 5.2 checks that.

### Scope

Three documents change: `docs/02-core-rules.md`, `docs/08-vehicles.md`, `docs/05-construction-components.md`. Nothing else — no glossary entry defines vehicle footprint, and `openspec/specs/` has no vehicles capability, so this change carries no spec delta.

### One idea, stated once

The constraint originates in `VEH-013`: a powered vehicle needs a Pilot, and a Pilot occupies a Unit Base. `VEH-013` carries the reasoning. `CORE-004`, `VEH-001` and `CMP-002` state the consequence and cite it. Do not repeat the derivation in more than one place.

### Coverage

| Item | Task |
|---|---|
| `CORE-004` says two or more | 1.1 |
| `VEH-001` says two or more | 2.1 |
| `VEH-013` carries the derivation | 2.2 |
| `CMP-002` states the consequence | 3.1 |

---

## 1. `docs/02-core-rules.md` — `CORE-004`

- [ ] 1.1 Replace the entire body of `CORE-004` with:

> A powered vehicle occupies **two or more** Unit Bases.
>
> One of those is taken by its Pilot, who occupies a Unit Base like any other crew member (`09-transport.md`, TRN-014) and is required for the vehicle to move at all (`08-vehicles.md`, VEH-013). A single-Unit-Base vehicle would be entirely filled by its own driver, with no vehicle left around them.
>
> Their footprint is defined by the LEGO model itself.
>
> Vehicle movement and transport capacity are described in the Vehicle Rules.

---

## 2. `docs/08-vehicles.md`

### 2.1 `VEH-001` — the same correction

- [ ] 2.1.1 Replace the single line "A vehicle occupies one or more Unit Bases (UB) — see `02-core-rules.md` (CORE-001) for the Unit Base definition (4 × 3 studs)." with:

> A powered vehicle occupies two or more Unit Bases (UB) — see `02-core-rules.md` (CORE-001) for the Unit Base definition (4 × 3 studs), and VEH-013 for why one is not enough.

- [ ] 2.1.2 Leave the footprint example table below it unchanged. Every vehicle in it is already 2 UB or larger — Bike 1 × 2, Buggy 2 × 2, Jeep 2 × 3, Tank 2 × 5, Heavy Transport 3 × 8 — so nothing in the table becomes illegal. Verify this rather than assuming it.

### 2.2 `VEH-013` — carry the derivation

- [ ] 2.2.1 Insert the following as a new paragraph immediately **after** the first paragraph ("Every powered vehicle — wheeled, tracked, walker, or hover (VEH-012) — requires a Pilot to move, a crew member (VEH-015) occupying a visible operating position.") and **before** the paragraph beginning "The Pilot resolves Impacts":

> Because the Pilot occupies a Unit Base of its own (`09-transport.md`, TRN-014), a powered vehicle needs room for its Pilot in addition to its machinery. This is why the minimum footprint is two Unit Bases (`02-core-rules.md`, CORE-004; VEH-001) rather than one: at one, the Pilot is the whole vehicle. The floor is not a chosen number — it is whatever this rule and TRN-014 together imply.

- [ ] 2.2.2 Leave the rest of `VEH-013` unchanged, including the sentence about another crew member taking over (future rules).

---

## 3. `docs/05-construction-components.md` — `CMP-002`

- [ ] 3.1 In `CMP-002`, add one bullet to the existing "Current gameplay:" list, after "Losing the Pilot disables vehicle movement (`08-vehicles.md`, VEH-013).":

> - Because the Pilot occupies a Unit Base, a powered vehicle must be built at least two Unit Bases in footprint (`02-core-rules.md`, CORE-004).

- [ ] 3.2 Change nothing else in `CMP-002`. The construction requirements above the list stay as they are.

---

## 4. Verify only — make no edit

- [ ] 4.1 `TRN-013` still lists "Drone — 1 UB" as cargo. That is the ruleset's category for a one-Unit-Base self-contained object and this change does not touch it.
- [ ] 4.2 `TRN-014` and `CMP-013` still state that crew members occupy their own Unit Bases. This change depends on that and must not alter it.
- [ ] 4.3 `VEH-004` is untouched. Movement still derives from length; this change alters the smallest legal length, not the formula.
- [ ] 4.4 `DEP-003` and `DEP-004` are untouched. Deployment Area cost per Unit Base is unchanged.
- [ ] 4.5 `TRN-001` still reads "Every transported object occupies one or more Unit Bases". That phrase is correct there — it describes cargo and passengers, not vehicle footprints — and must not be swept up by a find-and-replace.

---

## 5. Verify

- [ ] 5.1 Run `python3 scripts/lint_ruleset.py`; confirm no structural issues. This also checks that every `(CORE-NNN)`, `(TRN-NNN)` and `(VEH-NNN)` reference added above resolves.
- [ ] 5.2 Run `grep -rcE '^#{1,2} [A-Z]{3,4}-[0-9]{3} ' docs/ | awk -F: '{s+=$2} END {print s}'` and confirm the total is **218**, unchanged.
- [ ] 5.3 Run `grep -rn "one or more Unit Bases" docs/` and confirm exactly **one** hit remains, in `docs/09-transport.md` (`TRN-001`). That is a different and correct use of the phrase — it is about transported objects, not vehicles, and must not be changed. Before this change there are three hits; `CORE-004` and `VEH-001` are the two that go.
- [ ] 5.4 Run `grep -rn "two or more Unit Bases" docs/` and confirm exactly **two** hits, in `CORE-004` and `VEH-001`.
- [ ] 5.5 Run `grep -rn "Pilot is the whole vehicle\|room for its Pilot" docs/` and confirm the derivation appears **once**, in `VEH-013`. It must not be restated in `CORE-004`, `VEH-001` or `CMP-002` — those cite it.
- [ ] 5.6 Run `git diff --stat main...HEAD` and confirm exactly these paths changed: `docs/02-core-rules.md`, `docs/08-vehicles.md`, `docs/05-construction-components.md`, plus the four files under `openspec/changes/vehicle-minimum-footprint/`.
- [ ] 5.7 Confirm no numeric value changed anywhere. This change alters a minimum footprint, not any distance, cost or threshold.
- [ ] 5.8 Run `python3 scripts/check_delta_coverage.py` and confirm it passes. This change carries no spec delta, so it should report zero MODIFIED requirements checked.
