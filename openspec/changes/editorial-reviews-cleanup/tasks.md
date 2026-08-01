## 0. Setup

- [x] 0.1 Create and switch to a dedicated branch named `editorial-reviews-cleanup` (`openspec/config.yaml` requires one per proposal; the tree is currently on `resistance-clarification-review`).

Every replacement below is given verbatim. Apply the text exactly as written — do not paraphrase, re-order, or add cross-references beyond those shown. Where a task says *verify only*, make no edit.

### How to read the replacement blocks

Replacement text is shown as a markdown blockquote so it is visually separable from the instructions around it. **The `> ` prefix is not part of the text.** Strip it from every line before writing into the document.

Where a block contains a `## Heading` line, that heading is part of the text and must be written as a real heading, not left inside a quote.

Correct application of a block reading:

```
> ## Example 7 — Vehicle Hull
>
> A vehicle hull with 1-brick front armour...
```

produces exactly this in the document:

```
## Example 7 — Vehicle Hull

A vehicle hull with 1-brick front armour...
```

### What "the body of a rule" means

Several tasks say *replace the entire body of RULE-NNN*. The body is everything between that rule's `#` heading line and the `---` separator that ends it. **Never replace, remove, or renumber the heading itself** — no rule ID changes in this proposal (task 6.2 checks this).

**Expect `openspec/specs/` to look out of date.** Several applied changes have not been archived yet, so the living specs lag `docs/`. That is a known repo state, not something to fix here. Write the two deltas in section 5 and leave the living specs alone.

## 1. `docs/16-damage-system.md`

### 1.1 DMG-003 — hollow components and multi-wall enclosures

- [x] Insert the following as a new paragraph immediately **after** the paragraph beginning "Resistance is the **smallest structural section**..." and **before** the paragraph beginning "Impact Strength (`10-weapons.md`, WPN-021) is expressed in the same unit.":

> Only material the Impact actually crosses contributes. Empty internal space contributes nothing — a component is assumed hollow unless it is physically built solid. Where an Impact would cross more than one wall of an enclosed structure, those walls are separate components (DMG-001), each with its own Resistance, and the outer one protects what lies behind it (DMG-007) — resolved one after another by Penetration (DMG-017). Their thicknesses are never added together into a single Resistance.

### 1.2 DMG-004 — add Example 7

- [x] Insert after Example 6 (Moulded Windscreen) and **before** the closing paragraph beginning "A brick-built shield (Resistance 3)...". Note that closing paragraph carries no `##` heading — it belongs to DMG-004 as a whole, not to Example 6. Keep it last:

> ## Example 7 — Vehicle Hull
>
> A vehicle hull with 1-brick front armour, an empty interior, and 1-brick rear armour. An Impact striking the front crosses `3 plate layers` of structure. Therefore `Resistance = 3`.
>
> The empty interior contributes nothing, and the rear wall is a separate component (DMG-001) — not part of this one's Resistance. If the Impact penetrates the front wall, DMG-017 determines whether it continues toward whatever is inside.

### 1.3 Combat Examples — add Example 5

- [x] Insert after "## Example 4 — Jeep Cannon" and before the `---` preceding "# Combat Philosophy":

> ## Example 5 — Rifle vs Bunker Wall
>
> Bunker wall (two bricks thick, `Resistance 6`). Rifle `Strength 3` (one 1×1 muzzle). Attack Roll: Success. Geometry: `3 < 6`. The Impact ends immediately — no Damage Roll is made and the wall is unaffected (DMG-014).
>
> Cracking it requires a larger muzzle, not more dice: a 2×2 muzzle generates `Strength 6`, which passes at `6 ≥ 6`.

This fixes "Rifle" at a 1×1 muzzle, matching the Pistol already fixed at 1×1 in Combat Example 1. State the muzzle size inline as shown — the previous change's reference table exists precisely because unnamed muzzle sizes caused a naming collision once already.

### 1.4 Verify only — make no edit

- [x] DMG-008: the list "glass, metal, wood, infantry" is retained deliberately. Confirm it is still present and unchanged.
- [x] DMG-014: confirm it still states the `Strength < Resistance` path that Combat Example 5 now illustrates.

## 2. `docs/10-weapons.md`

### 2.1 WPN-003 — name the measurement axis

- [x] Replace the entire body of WPN-003 (currently two lines: "Weapon Length is the longest dimension of the functional Weapon Body." and "Decorative elements are ignored.") with:

> Weapon Length is the longest dimension of the functional Weapon Body, measured along the weapon's firing axis — the axis running perpendicular to the Weapon Front (WPN-019), which is the face the length axis points through.
>
> Measure the Weapon Body only. Mounting hardware (WPN-009) and decorative elements are not part of it and are ignored.

Do **not** restate the definition of Weapon Width here. `WPN-018` owns it ("Weapon Width is the smallest dimension of the Weapon Body"), and repeating it would add a second place to maintain — the duplication this change exists to reduce.

### 2.2 WPN-002 — conceptual definition

This **replaces** WPN-002's existing final line rather than adding a paragraph. `MEL-013` already states the muzzle/striking-end equivalence in full ("both represent the physical contact surface through which a weapon transfers energy into the target; a muzzle and a functional striking end are the same concept, expressed through two different delivery methods"). Restating that here would duplicate it verbatim, and would sit directly beside a line that already points at MEL-013. Add only the ranged-side definition and let MEL-013 keep ownership of the equivalence.

- [x] Replace the existing final line of WPN-002 — "Melee weapons use a functional striking end instead of a muzzle. See `12-melee.md` (MEL-013)." — with:

> A functional muzzle is the physical contact surface through which a ranged weapon transfers energy into an Impact. Melee weapons use a functional striking end in its place, which plays exactly the same role — see `12-melee.md` (MEL-013).

- [x] Confirm the old line is gone. WPN-002 must not end up containing both the old "Melee weapons use a functional striking end instead of a muzzle." line and the new paragraph — the new text replaces it, and two adjacent pointers to MEL-013 is the duplication this task exists to avoid.

### 2.3 Summary — architectural closing line

The Summary ends with three `##` subsections (Length, Muzzle Count, Muzzle Size), then a `---`, then two prose lines: "No hidden statistics are required." and "A player should understand every weapon simply by looking at the LEGO model."

- [x] Insert the following as a new paragraph **after** that `---` and **before** "No hidden statistics are required." — inside the prose block, not between the `---` and the Muzzle Size subsection:

> Weapons define only how an Impact is generated. Every consequence of that Impact is determined by Combat Resolution (`11-combat.md`) and the Component Damage System (`16-damage-system.md`).

### 2.4 Verify only — make no edit

- [x] WPN-021: confirm its closing paragraph already states that each die's Impact Strength depends only on the muzzle that rolled it. No addition needed.
- [x] WPN-013 and WPN-008: confirm both already defer to `11-combat.md`. No boundary statement is being added as a rule.
- [x] WPN-005: confirm `Range = Weapon Length × 2` is unchanged, and that 2.1 changed no measurement.

## 3. `docs/12-melee.md`

### 3.1 MEL-005 — replace the step list with a reference

- [x] Replace the entire body of MEL-005 with:

> Once a melee weapon generates its Attack Die (MEL-003), Combat Resolution (`11-combat.md`) and the Component Damage System determine every remaining step, exactly as for a ranged Impact — the sequence is defined by `16-damage-system.md` (DMG-009), and each step within it by DMG-011 through DMG-017. No melee-specific resolution rules exist.

This citation deliberately names DMG-009 as the owner of the sequence, matching the citation task 3.5 gives the Summary. Both places in this document now credit the same source.

### 3.2 MEL-010 — shorten the placeholder

- [x] Replace the entire body of MEL-010 with:

> Reserved for rule-ID stability. Vehicle component targeting is fully defined by MEL-002 — a vehicle component is targeted like any other: visible and physically reachable.

### 3.3 MEL-012 — correct the scope sentence

- [x] Replace only the final line ("This document only defines how melee weapons generate Attack Dice. Everything after that belongs to the standard combat system.") with:

> This document defines only how a melee attack generates an Impact — physical contact (MEL-001), reach (MEL-014), striking ends (MEL-013), and Attack Dice (MEL-003). All subsequent resolution belongs to Combat Resolution and the Component Damage System.

### 3.4 MEL-013 — unify the terminology

- [x] In the first sentence, change "the physical point of contact through which a melee weapon delivers an Impact" to "the physical contact surface through which a melee weapon delivers an Impact".
- [x] Confirm the rule's final paragraph already uses "physical contact surface"; both now match.

### 3.5 Summary — retighten one citation

- [x] In the final paragraph, change the citation "Penetration (MEL-005)" to "Penetration (`16-damage-system.md`, DMG-009)". The Summary keeps its enumeration; only the source it credits changes, since MEL-005 no longer carries the list.

### 3.6 Verify only — make no edit

- [x] MEL-002: the component example list is retained deliberately. Confirm it is still present and unchanged.
- [x] MEL-002: confirm it still names "Vehicle crew", which MEL-010 depends on after 3.2.
- [x] `docs/11-combat.md` Combat Flow diagram: confirm unchanged. It is one of the two surviving copies of the step sequence (the other being DMG-009) and is intentionally kept.

## 4. `docs/14-glossary.md` — cross-document consistency

Only one glossary entry actually breaks as a result of sections 1–3. The others are deliberately left alone: the glossary's job is to point at the owning rule, not to mirror its prose, and copying the new wording into it would create the third copy this change exists to avoid.

- [x] 4.1 Entry `Functional Striking End`: **required.** It also says "physical point of contact", so it must change with MEL-013 (task 3.4) or grep 6.4 will fail. Change "the physical point of contact through which a melee weapon delivers an Impact" to "the physical contact surface through which a melee weapon delivers an Impact".
- [x] 4.2 Entry `Weapon Body`: **required.** Replace "Defines Weapon Length and Weapon Width." with "Defines Weapon Length (measured along the firing axis) and Weapon Width." Keep it to that qualifier — do not restate WPN-003 in full.
- [x] 4.3 Entry `Muzzle`: verify only — it already defers to `WPN-002` and needs no change. Do **not** copy WPN-002's new contact-surface sentence into it.
- [x] 4.4 Entry `Resistance`: verify only — task 1.1 introduces no new measurement unit, so the entry stays correct.

## 5. Spec deltas

Both are already written in this change directory. Verify each matches the text actually applied; do not rewrite them from scratch.

- [x] 5.1 `specs/component-damage/spec.md`: MODIFIED requirement "Geometry Defines Resistance" — adds the hollow-space and non-summed-walls clauses. Must match task 1.1.
- [x] 5.2 `specs/weapon-construction/spec.md`: MODIFIED requirement "Weapon Length Determines Range" — adds the firing-axis measurement and the mounting-hardware exclusion. Must match task 2.1.

Note which accepted items deliberately get **no** delta: WPN-002's conceptual sentence (2.2) and the Summary line (2.3) restate existing behaviour in prose and introduce no requirement. The same applies to every melee item — MEL-005, MEL-010, MEL-012 and MEL-013 change wording only, and `openspec/specs/` has no melee capability to modify.

## 6. Verify

- [x] 6.1 Run `python3 scripts/lint_ruleset.py`; confirm no structural issues.
- [x] 6.2 Confirm no rule ID was added, removed, or renumbered.
- [x] 6.3 Run `grep -rn "Weapon Length" docs/` and confirm no document contradicts WPN-003's new axis wording.
- [x] 6.4 Run `grep -rn "point of contact" docs/` and confirm zero hits remain (this requires both task 3.4 and task 4.1).
- [x] 6.5 Run `grep -rn "MEL-005" docs/` and confirm the only remaining hit is the rule heading itself — task 3.5 removes the Summary's citation of it.
- [x] 6.6 Confirm no numeric Resistance or Impact Strength value anywhere in `docs/` changed as a result of this change.
- [x] 6.7 Run `grep -rn "transfers energy" docs/` and confirm exactly two hits — `WPN-002` and `MEL-013` — each stating the concept once, with neither restating the other's equivalence sentence, and no third copy in the glossary.
- [x] 6.8 Run `grep -rn "Attack Roll, Select Target Component, Geometry Check" docs/`. Before applying, this returns two hits, both in `docs/12-melee.md` — MEL-005 and the Summary. After applying task 3.1, expect exactly one: the Summary. `DMG-009` writes the same sequence with arrows rather than commas, so it does not match this pattern and is not expected in the output.
- [x] 6.9 Run `grep -rnE "^> (##|A vehicle hull|Bunker wall|Only material|Weapon Length|A functional muzzle|Weapons define|Once a melee|Reserved for|This document defines)" docs/` and confirm zero hits. Any match means a replacement block was pasted with its `> ` prefix still attached. A plain `grep "^> "` is not usable here: every document legitimately ends with a `> **Every Brick Matters.**` epigraph.
- [x] 6.10 Run `git diff --stat` and confirm exactly six files changed: `docs/16-damage-system.md`, `docs/10-weapons.md`, `docs/12-melee.md`, `docs/14-glossary.md`, and the two spec deltas under `openspec/changes/editorial-reviews-cleanup/specs/`. Any other file means something was edited that this proposal does not touch.
