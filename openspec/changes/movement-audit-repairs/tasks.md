## 0. Setup

- [ ] 0.1 Work on branch `movement-audit-repairs` (`openspec/config.yaml` requires one branch per proposal).

### How to read the replacement blocks

Replacement text is shown as a markdown blockquote so it is visually separable from the instructions. **The `> ` prefix is not part of the text.** Strip it from every line before writing into the document.

Where a block contains a `#` or `##` heading, that heading is part of the text and must be written as a real heading, not left inside a quote.

### What "the body of a rule" means

Where a task says *replace the entire body of `MOVE-NNN`*, the body is everything between that rule's `#` heading line and the `---` separator that ends it. **Never change, remove, or renumber an existing heading.**

### New rule headings must match the linter's format

`scripts/lint_ruleset.py` parses rule headings with `^#{1,2} ([A-Z]{2,6})-(\d{3}) — `. The four new headings in section 8 must therefore use a level-1 `#`, a three-digit number, and a real **em dash** (`—`, U+2014) surrounded by single spaces — not a hyphen and not an en dash. Copy the punctuation from an existing heading such as `# MOVE-016 — Falling Damage` if in doubt.

The linter also requires rule IDs to be strictly increasing within a document. `MOVE-017` … `MOVE-020` are assigned in the order those sections already appear in the file (Collision, Doors, Ramps, Interactive Terrain), so do not reorder the sections.

### Scope

Only `docs/07-movement.md` changes. No other document is touched. Every anchor quoted below was confirmed unique in the file at the time of writing.

### Defect coverage

Each of the twenty-one defects in `proposal.md` maps to at least one task here. Use this to check nothing was skipped.

| Defect | Task |
|---|---|
| 1 — `MOVE-004` fixed vs. maximum | 2.1 |
| 2 — `MOVE-007`'s "Forward 8 studs" is illegal | 2.1, 5.1 |
| 3 — `MOVE-014` drops ramps | 7.3 |
| 4 — side movement uncapped | 3.1 |
| 5 — side movement has no AP cost | 3.1 |
| 6 — "movement allowance" undefined | 4.1 |
| 7 — backward movement has no limit or granularity | 4.1 |
| 8 — backward movement has no AP cost | 4.1 |
| 9 — `MOVE-003` measures forward only | 1.1 |
| 10 — forward granularity undefined | 2.1 |
| 11 — plate-built obstacle heights unresolvable | 6.1, 6.2, 6.3 |
| 12 — climbing vs. movement action undefined | 6.2 |
| 13 — slope and stair traversal cost undefined | 7.1, 7.2 |
| 14 — deliberate falls and landing position undefined | 8.1 |
| 15 — overlap rule duplicated | 1.1, 1.2, 8.2 |
| 16 — CORE-007's cost restated three times | 8.3, 8.4, 8.5, 8.6 |
| 17 — four normative sections have no rule ID | 8.2, 8.3, 8.4, 8.5 |
| 18 — Summary omits AP costs | 9.3 |
| 19 — `MOVE-016` cites its own file | 9.1 |
| 20 — fall height still measured in bricks | 9.2.1, 9.2.2 |
| 21 — a 1-brick drop wounds, a 1-brick obstacle is free | 9.2.1, 9.2.2 |

---

## 1. `MOVE-003` — measure along the direction of travel

Currently written for forward movement only ("from the front edge"), which is wrong for backward and sideways movement. It also duplicates the Collision section's overlap rule, which moves to `MOVE-017` in task 8.

- [ ] 1.1 Replace the entire body of `MOVE-003` with:

> Movement is measured along the direction of travel, from the edge of the base that leads in that direction: the front edge moving forward, the rear edge moving backward, and the corresponding side edge moving left or right.
>
> When movement ends, the unit occupies its new position completely.

- [ ] 1.2 Confirm the line "Models may not overlap." no longer appears in `MOVE-003`. Model-on-model overlap becomes `MOVE-017`'s rule (task 8.2); `MOVE-003` keeps only how distance is measured and that the unit ends fully in its new position.

---

## 2. `MOVE-004` — 12 studs is a maximum, in multiples of 3

- [ ] 2.1 Replace the entire body of `MOVE-004` with:

> Standard infantry movement:
>
> **Up to 12 studs forward, in multiples of 3 studs**
>
> 12 is the maximum, not a fixed distance — a unit may move 3, 6, 9 or 12 studs, or stay put.
>
> The step size is the Unit Base's depth (`02-core-rules.md`, CORE-001): moving forward crosses the 3-stud axis, so forward movement counts whole base-depths, exactly as side movement counts whole base-widths of 4 (MOVE-005). Both numbers come from the base itself, so a player can measure either by laying spare Unit Bases end to end.
>
> One movement action costs **1 Action Point** (`02-core-rules.md`, CORE-006) and moves the unit in a single direction. Changing direction requires a second movement action (MOVE-007).
>
> Each movement action is measured independently: a unit spending two Action Points on movement makes two separate moves of up to 12 studs each, not one move of 24.
>
> Future scenarios may allow sprinting or other special movement.

---

## 3. `MOVE-005` — add the maximum and the AP cost

The rule currently states granularity but no upper limit and no cost, so a unit may sidestep an unlimited distance for free.

- [ ] 3.1 Replace the entire body of `MOVE-005` with:

> Infantry may move sideways, left or right.
>
> **Up to 12 studs, in multiples of 4 studs**
>
> The step size is the Unit Base's width (`02-core-rules.md`, CORE-001) — moving sideways crosses the 4-stud axis. Legal distances are therefore 4, 8 and 12 studs. Partial side movement is not allowed.
>
> Side movement is a movement action and costs **1 Action Point**, the same as moving forward (MOVE-004).

---

## 4. `MOVE-006` — replace the undefined "movement allowance"

"The same movement allowance" names nothing defined elsewhere in the ruleset, and leaves the limit, granularity and cost all unstated.

- [ ] 4.1 Replace the entire body of `MOVE-006` with:

> Infantry may move backwards.
>
> **Up to 12 studs, in multiples of 3 studs** — the same limit and step size as forward movement (MOVE-004), because backward movement crosses the same 3-stud axis of the base.
>
> The unit keeps its facing. No rotation is required.
>
> Backward movement is a movement action and costs **1 Action Point**.

---

## 5. `MOVE-007` — correct the illegal example

The current example moves "Forward 8 studs". 8 is not a multiple of 3, so it is illegal under `MOVE-004`. It also costs two movement actions, which the example does not say.

- [ ] 5.1 Replace the entire body of `MOVE-007` with:

> StudCraft does not use diagonal movement.
>
> Players combine forward and lateral movement instead. Each leg is its own movement action, costing 1 Action Point each.
>
> Example — instead of moving diagonally:
>
> - Forward 6 studs (1 AP)
> - Left 4 studs (1 AP)
>
> This maintains compatibility with the LEGO grid, and means a unit with 3 AP can make at most three movement legs in an activation.

---

## 6. `MOVE-009`, `MOVE-010`, `MOVE-011` — express heights in plate layers

Thresholds are currently given in whole bricks, leaving any plate-built obstacle unresolvable — a 4-plate wall is taller than `MOVE-009`'s 1 brick and shorter than `MOVE-010`'s 2 bricks. `16-damage-system.md` (DMG-003) already standardised on plate layers, with a brick counting as 3.

Thresholds are unchanged in effect. Do not alter the AP costs.

- [ ] 6.1 Replace the entire body of `MOVE-009` with:

> Height: **up to 3 plate layers** (one brick or less).
>
> Obstacle height is measured in plate layers, the same unit `16-damage-system.md` (DMG-003) uses: a plate counts as 1 and a standard brick as 3.
>
> Infantry may cross freely. No additional movement cost.

- [ ] 6.2 Replace the entire body of `MOVE-010` with:

> Height: **4 to 6 plate layers** (more than one brick, up to two).
>
> Infantry may climb. Climbing costs **1 additional Action Point** on top of the movement action that crosses the obstacle, so a move over such an obstacle costs 2 AP in total.
>
> The climb is part of that movement action and does not increase the distance the unit may travel: the 12-stud limit (MOVE-004) still applies to the move as a whole.

- [ ] 6.3 In `MOVE-011`, replace the three lines "Height:", the blank line after it, and "3 Bricks or more" — that is, everything between the `# MOVE-011 — Three Brick Obstacles` heading and the line "Cannot be climbed directly." — with this single line:

> Height: **7 or more plate layers** (taller than two bricks).

- [ ] 6.4 Leave the rest of `MOVE-011` unchanged: "Cannot be climbed directly.", "A legal access point is required.", the "Examples:" list (Slopes, Plate stairs, Ramps) and "Without one of these, the obstacle is impassable." all stay exactly as they are.
- [ ] 6.5 Leave all three rule headings unchanged, including the words "One Brick", "Two Brick" and "Three Brick" in them. Renaming a heading is out of scope; only the height thresholds in the bodies change.

---

## 7. `MOVE-012`, `MOVE-013`, `MOVE-014` — state costs, restore ramps

`MOVE-011` lists three legal access points; `MOVE-014` recognises only slopes and stairs, silently dropping ramps. Neither `MOVE-012` nor `MOVE-013` says what traversal costs.

- [ ] 7.1 Replace the entire body of `MOVE-012` with:

> Slopes are valid climbing surfaces.
>
> Units may move normally over connected slopes, at no additional Action Point cost — a slope is ordinary terrain, not an obstacle to climb. Distance travelled up a slope counts against the normal movement limit (MOVE-004).

- [ ] 7.2 Replace the entire body of `MOVE-013` with:

> Plate-built stairs are valid movement paths.
>
> Units may climb them normally, at no additional Action Point cost, and the distance climbed counts against the normal movement limit (MOVE-004) — the same as slopes (MOVE-012).

- [ ] 7.3 Replace the entire body of `MOVE-014` with:

> If no slope, stair or ramp exists, the wall cannot be climbed. These are the three legal access points listed in MOVE-011, and no other construction grants access.
>
> Physical construction determines accessibility.

---

## 8. `MOVE-015`, and four new rule IDs

`MOVE-015` does not say whether a unit may fall deliberately or where it lands. The Collision, Doors, Ramps and Interactive Terrain sections are normative but carry no rule ID, so nothing can cite them.

- [ ] 8.1 Replace the entire body of `MOVE-015` with:

> A unit that leaves a higher position without support falls. A unit may do this deliberately — stepping off a ledge is a legal way to descend, at the risk described in MOVE-016.
>
> The unit is placed directly below the point it left, at the first surface that physically supports it. Falling immediately ends the movement action; any unspent movement from that action is lost.

- [ ] 8.2 Convert the `# Collision` section heading to `# MOVE-017 — Collision` and replace its body with:

> Units may not finish movement occupying the same physical space. Models may not overlap.
>
> Friendly units may move around each other if enough space physically exists. Enemy units block movement unless another rule allows otherwise.

- [ ] 8.3 Convert the `# Doors` section heading to `# MOVE-018 — Doors` and replace its body with:

> Closed doors block movement. Once opened, the doorway becomes a valid movement path.
>
> Opening or closing a door is an interactive element action (`02-core-rules.md`, CORE-007).

- [ ] 8.4 Convert the `# Ramps` section heading to `# MOVE-019 — Ramps` and replace its body with:

> A lowered ramp immediately becomes usable terrain and is a legal access point (MOVE-011, MOVE-014).
>
> Lowering or raising a ramp is an interactive element action (`02-core-rules.md`, CORE-007).

- [ ] 8.5 Convert the `# Interactive Terrain` section heading to `# MOVE-020 — Interactive Terrain` and replace its body with:

> Any movable LEGO element may become part of a movement path.
>
> Examples:
>
> - Drawbridges
> - Elevators
> - Gates
> - Hinged platforms
>
> Operating one is an interactive element action (`02-core-rules.md`, CORE-007).

- [ ] 8.6 Confirm the AP cost was removed from all three of `MOVE-018`, `MOVE-019` and `MOVE-020` — CORE-007 is now the single source for it. The phrase "1 Action Point" must not appear in any of them.
- [ ] 8.7 Leave every other unnumbered heading exactly as it is — `# StudCraft Movement Rules`, `# Purpose`, `# Design Philosophy`, `# Terrain Movement`, `# Falling`, `# Vehicle Movement`, `# Physical Priority` and `# Summary`. These are section dividers, framing prose, or a documented deferral, not rules. Only the four named in 8.2–8.5 become rules.

---

## 9. `MOVE-016` and the Summary

- [ ] 9.1 In `MOVE-016`, replace the self-citation "vehicle falling is not yet defined (`07-movement.md`, Vehicle Movement)" with "vehicle falling is not yet defined — see the Vehicle Movement section below". A document should not cite itself by filename.

### 9.2 `MOVE-016` — plate layers and a minimum fall height

Two problems. `MOVE-016` measures in whole bricks, which would leave it the only place in the document still doing so after section 6; and a one-brick drop currently costs a 50% wound roll while `MOVE-009` treats the same height as trivial terrain a unit crosses for free.

Replace everything from the line "Falling damage depends on the height fallen." down to and including "The greater the fall, the greater the chance of suffering damage." with:

> Falling damage depends on the height fallen, measured in plate layers — the same unit obstacles use (MOVE-009).
>
> A fall of **3 plate layers or less causes no damage** and no roll is made. This is the height MOVE-009 already treats as trivial to cross; stepping down it is no more dangerous than stepping over it.
>
> For a greater fall, roll **one D6 per complete brick (3 plate layers) fallen**, and keep only the **lowest result**. A remainder of one or two plate layers adds no die.
>
> The greater the fall, the greater the chance of suffering damage.

- [ ] 9.2.1 Apply that replacement.
- [ ] 9.2.2 Replace the three example lines with:

> - Fall of 3 plate layers (1 brick) → no roll, no damage.
> - Fall of 4 to 6 plate layers → Roll 1D6.
> - Fall of 7 to 9 plate layers → Roll 2D6, keep the lowest.
> - Fall of 15 plate layers (5 bricks) → Roll 5D6, keep the lowest.

- [ ] 9.2.3 Leave `MOVE-016`'s Geometry Check exception paragraph untouched — the one beginning "The kept die is treated as a Damage Roll". It is still correct: falling has no Impact Strength, so Resistance still plays no part.
- [ ] 9.2.4 Leave the infantry-only line untouched apart from the citation fix in 9.1.
- [ ] 9.3 Replace the entire body of the `# Summary` section (everything between the `# Summary` heading and the `---` before the epigraph) with:

> Movement in StudCraft is based on six simple principles:
>
> 1. No diagonal movement.
> 2. Infantry move up to 12 studs forward or backward, in multiples of 3.
> 3. Side movement is up to 12 studs, in multiples of 4.
> 4. Each movement action costs 1 Action Point and moves in one direction.
> 5. Walls require physical access — a slope, a stair or a ramp.
> 6. Physical construction always defines legal movement.

- [ ] 9.4 Confirm the Summary now says "six simple principles" and lists exactly six.

---

## 10. Verify

- [ ] 10.1 Run `python3 scripts/lint_ruleset.py`; confirm no structural issues.
- [ ] 10.2 Run `git diff --stat main...HEAD` and confirm exactly two paths changed: `docs/07-movement.md` and the four new files under `openspec/changes/movement-audit-repairs/`.
- [ ] 10.3 Run `grep -n "^# MOVE-" docs/07-movement.md` and confirm `MOVE-001` through `MOVE-020` appear once each, in ascending order, with no gaps.
- [ ] 10.4 Run `grep -c "movement allowance" docs/07-movement.md` and confirm **0** — the undefined term is gone.
- [ ] 10.5 Run `grep -c "Forward 8 studs" docs/07-movement.md` and confirm **0**.
- [ ] 10.6 Run `grep -n "Models may not overlap" docs/07-movement.md` and confirm exactly **one** hit, inside `MOVE-017`. The sentence moved out of `MOVE-003`; it was not deleted, and it must not appear in both.
- [ ] 10.7 Run `grep -n "1 Action Point" docs/07-movement.md` and confirm exactly five hits, in `MOVE-004`, `MOVE-005`, `MOVE-006`, `MOVE-007` and `MOVE-008` — never in `MOVE-018`, `MOVE-019` or `MOVE-020`. `MOVE-010` will not appear: it reads "1 **additional** Action Point", which this pattern does not match. That is expected, not a miss.
- [ ] 10.8 Run `grep -n "Brick\|brick" docs/07-movement.md` and confirm every hit is one of: the three rule headings (`One Brick Obstacles`, `Two Brick Obstacles`, `Three Brick Obstacles`, left unchanged by 6.5), a parenthetical equivalent added in section 6, the `a standard brick as 3` conversion in `MOVE-009`, or `MOVE-016`'s falling text. No threshold may still be stated in bricks alone.
- [ ] 10.9 Run `grep -rn "MOVE-0" docs/ --include="*.md" | grep -v 07-movement` and confirm the only external citation is `08-vehicles.md`'s reference to `MOVE-008`, which this change does not touch.
- [ ] 10.10 Confirm no existing rule ID (`MOVE-001` … `MOVE-016`) was renumbered, and that `MOVE-017` … `MOVE-020` are new.
