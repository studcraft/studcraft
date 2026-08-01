## 0. Setup

- [ ] 0.1 Work on branch `rescale-movement-and-range` (`openspec/config.yaml` requires one branch per proposal).

### How to read the replacement blocks

Replacement text is shown as a markdown blockquote so it is visually separable from the instructions. **The `> ` prefix is not part of the text.** Strip it from every line before writing into the document.

Where a block contains a `#` heading or a `|` table, those are part of the text and must be written as real markdown, not left inside a quote.

### What "the body of a rule" means

Where a task says *replace the entire body of `RULE-NNN`*, the body is everything between that rule's `#` heading line and the `---` separator that ends it. **Never change, remove or renumber a rule heading.** No rule ID changes in this proposal; task 6.2 checks that.

### Scope

Four documents change: `docs/08-vehicles.md`, `docs/10-weapons.md`, `docs/11-combat.md`, `docs/14-glossary.md`, plus one spec delta already written in this change directory. Nothing else. Every anchor quoted below was confirmed unique at the time of writing.

### The two numbers

Everything in this change comes from exactly two substitutions. If you find yourself computing a third multiplier, stop and re-read.

| | Before | After |
|---|---|---|
| Vehicle movement | `1.5 × length` | **`3 × length`** |
| Weapon Range | `Weapon Length × 2` | **`Weapon Length × 6`** |

### Coverage

| Item | Task |
|---|---|
| `VEH-004` movement multiplier and examples | 1.1 |
| `VEH-004` clear-lane note | 1.1 |
| `WPN-005` Range multiplier and table | 2.1 |
| `WPN-005` bounds paragraph (no cap, and why) | 2.1 |
| `CBT-003` restated formula | 3.1 |
| Glossary `Weapon Range` entry | 4.1 |
| Spec delta | 5.1 |

---

## 1. `docs/08-vehicles.md` — `VEH-004`

The current body states `1.5×`, gives three worked examples, and ends with "This rule scales naturally for all vehicle sizes."

- [ ] 1.1 Replace the entire body of `VEH-004` with:

> A vehicle moves:
>
> **Three (3×) times its own length**
>
> Costing **1 Action Point** (`02-core-rules.md`, CORE-006), the same as any other Move action.
>
> Measure from the vehicle's front, along its facing.
>
> Every vehicle therefore covers three of its own lengths per action, whatever its size. A small vehicle is not slow — it is small. Because the multiplier is a whole number, every resulting distance is a whole number of studs; there is no half stud to measure.
>
> Examples
>
> | Vehicle | Longest dimension | Movement |
> |---|---:|---:|
> | Bike (1 × 2 UB) | 6 studs | 18 studs |
> | Buggy (2 × 2 UB) | 8 studs | 24 studs |
> | Jeep (2 × 3 UB) | 9 studs | 27 studs |
> | Tank (2 × 5 UB) | 15 studs | 45 studs |
> | Heavy Transport (3 × 8 UB) | 24 studs | 72 studs |
>
> Large vehicles rarely realise these figures. A 24-stud transport moving 72 studs needs a clear lane of nearly a hundred studs, and terrain seldom offers one — the limit in play is the battlefield, not the rule.
>
> This rule scales naturally for all vehicle sizes.

- [ ] 1.2 Confirm the phrases "One and a half" and "1.5" no longer appear anywhere in `docs/08-vehicles.md`.
- [ ] 1.3 Confirm the sentence beginning "After moving, the rear of the vehicle will approximately occupy..." is gone. It described the geometry of a 1.5× move specifically and is false at 3×.

---

## 2. `docs/10-weapons.md` — `WPN-005`

- [ ] 2.1 Replace the entire body of `WPN-005` with:

> Weapon range is determined by construction.
>
> Range equals:
>
> **Weapon Length × 6**
>
> Examples
>
> | Weapon Length | Maximum Range |
> |---------------|--------------:|
> | 2 studs | 12 studs |
> | 4 studs | 24 studs |
> | 6 studs | 36 studs |
> | 8 studs | 48 studs |
> | 12 studs | 72 studs |
>
> No additional range values exist.
>
> There is no maximum Range, for the same reason there is no maximum Impact Strength (WPN-021): the limit is what the attacker's platform can carry. That limit is real, it is simply not written as a number. Weapon Length is bounded by Platform Length (WPN-004), platform size by the agreed Deployment Area (`04-construction-standard.md`, SCS-003; `06-deployment.md`, DEP-003), and the Deployment Area by the battlefield the players agree on before it (`03-game-flow.md`, FLOW-001). Range therefore scales with the size of the game on its own.
>
> Maximum Range is rarely the practical limit in any case. Line of Sight is a physical check (`02-core-rules.md`, CORE-008), so a weapon reaching 90 studs only matters where 90 studs of clear sight exist. On a battlefield with terrain, that is uncommon.

- [ ] 2.2 Confirm every row of the new table is `length × 6`, and that the table replaced the old one rather than being added beside it.

---

## 3. `docs/11-combat.md` — `CBT-003`

- [ ] 3.1 Replace the single sentence that is `CBT-003`'s body — "A target must be inside the weapon's maximum range: `Range = Weapon Length × 2` — see `10-weapons.md` (WPN-005) for the full definition." — with:

> A target must be inside the weapon's maximum range: `Range = Weapon Length × 6` — see `10-weapons.md` (WPN-005) for the full definition, and for why that figure has no written maximum.

---

## 4. `docs/14-glossary.md` — `Weapon Range`

- [ ] 4.1 Replace the body of the `## Weapon Range` entry — "The maximum distance a ranged weapon may attack, equal to Weapon Length × 2. See `10-weapons.md` (WPN-005)." — with:

> The maximum distance a ranged weapon may attack, equal to Weapon Length × 6. Bounded in practice by Line of Sight and by what the attacker's platform can carry, rather than by a written maximum. See `10-weapons.md` (WPN-005).

- [ ] 4.2 Verify only — the `Weapon Reach` entry immediately below is about melee and has no multiplier. It must not change.

---

## 5. Spec delta

- [ ] 5.1 `specs/weapon-construction/spec.md` is already written in this change directory. Verify it matches the text applied in task 2.1, and do not rewrite it from scratch.

Note what deliberately gets **no** delta: `VEH-004`. `openspec/specs/` has no vehicles capability, so vehicle movement is not covered by any living spec. Creating one would mean capturing all 27 VEH rules, which is its own piece of work — not something to half-do inside a rescale.

---

## 6. Verify

- [ ] 6.1 Run `python3 scripts/lint_ruleset.py`; confirm no structural issues. This also checks every `(WPN-NNN)`-style cross-reference added above resolves.
- [ ] 6.2 Run `grep -rn "^# [A-Z]\{3,4\}-" docs/ | wc -l` before and after; confirm the count is identical — no rule ID added, removed or renumbered.
- [ ] 6.3 Run `grep -rn "Length × 2\|× 2 \|1\.5\|One and a half" docs/` and confirm **zero** hits relating to Range or vehicle movement. A hit inside `WPN-018` (`Length ≥ 2 × Width`) is expected and correct — that is the weapon proportion rule, not a multiplier this change touches.
- [ ] 6.4 Run `grep -rn "Weapon Length × 6" docs/` and confirm exactly **three** hits: `WPN-005`, `CBT-003` and the glossary. All three must agree.
- [ ] 6.5 Run `grep -rn "Three (3×)\|3 × length\|three of its own lengths" docs/08-vehicles.md` and confirm `VEH-004` states the new multiplier.
- [ ] 6.6 Confirm no numeric example anywhere in `docs/` still shows a half stud. Run `grep -rn "\.5 studs\|13\.5\|22\.5" docs/` and expect zero hits.
- [ ] 6.7 Run `git diff --stat main...HEAD` and confirm exactly these paths changed: `docs/08-vehicles.md`, `docs/10-weapons.md`, `docs/11-combat.md`, `docs/14-glossary.md`, and the four files under `openspec/changes/rescale-movement-and-range/`.
- [ ] 6.8 Confirm `MOVE-004` is untouched — infantry movement stays 12 studs. It is the reference every figure in this change was measured against.
- [ ] 6.9 Confirm `WPN-021` (Impact Strength) is untouched. This change rescales reach, not power.
- [ ] 6.10 Confirm `WPN-004` (Weapon Capacity) is untouched. Only the value derived from Weapon Length changes, not the cap on Weapon Length itself.
