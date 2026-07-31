## Context

An external review (`delete-me-comments.md`) asked for one clarification: state that Resistance is measured in plates, never bricks. Verification against shipped text found five of its six points already implemented, and the sixth — the un-exceptioned wording — impossible to apply as written, because `DMG-003` carries a deliberate fixed-piece exception for the minifig.

Tracing why that exception exists led to the real problem: `DMG-014` compares Impact Strength (studs of muzzle width) against Resistance (plate layers of material). Two units, one comparison. The exception is a patch over that mismatch, applied at the single point where the mismatch produced a visibly absurd result.

## Decisions

### Fix the unit mismatch rather than add more exceptions

The alternative — extending the fixed-piece exception to cover moulded wheels, accessory shields, windscreens and door pieces — would close the documentation hole while leaving the mismatch intact. Infantry would still be unable to damage a brick wall, and the ruleset would carry a growing list of components exempt from its own measurement rule.

Aligning the units instead removes the mismatch, the exception, and the moulded-piece hole in one move, and leaves the system with fewer rules than it has now. This is the direction Principle 11 (Simplicity Before Complexity) and Principle 15 (reuse existing systems rather than introducing parallel ones) both point.

### Why `× 3` specifically

One stud of muzzle width is chosen to represent one brick of penetrating power, and `DMG-003` already fixes a brick at 3 plate layers. The multiplier is therefore not a balance dial — it is the conversion factor already present in the ruleset, applied to the side that was missing it.

This also means the scale stays readable from the model, per "The Model Is The Rules": a 1-stud muzzle defeats 1 brick of material, a 2-stud muzzle defeats 2 bricks, a 4-stud muzzle defeats 4. A player can reason about a matchup by comparing muzzle width in studs against wall thickness in bricks, with no arithmetic at all.

### Delete the minifig exception rather than keep it as a shortcut

With the scale aligned, a minifig measured normally lands at Resistance 3 (roughly one brick of material), and the smallest legal muzzle generates exactly Strength 3. The exception's entire purpose — keeping minifigs killable — is satisfied by the general rule, so keeping it would mean maintaining a special case that no longer does anything.

Removing it also restores a property the ruleset otherwise has everywhere: every component is measured by one method, and `DMG-008`'s claim that only *how a component is built* matters becomes literally true again rather than true-with-an-asterisk.

### Moulded pieces are covered by stating the conversion, not by naming them

Rather than enumerate which pieces are "fixed", `DMG-003` states the conversion generally: a plate counts 1, a brick counts 3, and any other element counts as the plate-equivalent of its own thickness in the direction of travel. A windscreen shell measures thin and resolves low; a minifig torso measures about a brick and resolves to 3; a wheel measures thick and resolves higher.

This is a measurement instruction, not a category. No component type is named, so `DMG-008` is not weakened and `13-materials.md` is not reintroduced by the back door — which was the specific risk in the reviewer's REVIEW-004 framing of "transparent components" as a class needing their own treatment.

### Unarmed attacks inherit the scale instead of hardcoding a number

`MEL-008` currently states `Impact Strength 1` as a literal. Under the new scale that number would make bare hands unable to affect anything, including a minifig. Rather than replace it with a different literal (3), the rule is restated as "counts as a size-1 striking end", so it derives from `WPN-021` like every other Impact Strength and cannot drift out of sync if the scale is ever revisited.

### Fix the "Heavy Cannon" name collision while applying

`WPN-020` defines a Heavy Cannon as a 2×2 muzzle. `DMG-017` and Combat Example 3 use "Heavy Cannon" at `Strength 4`, which under the old scale implies a 4×4 muzzle. Two different weapons have been sharing one name since before this change.

Rescaling forces the issue, because an applier has to pick a muzzle size to derive the new value from. Unify on `WPN-020`'s definition (2×2, Impact Strength 6) — it is the one stated in a rule rather than implied by an example, and it keeps the worked examples at a scale infantry can actually reach.

### Every numeric value is tabulated in `tasks.md` rather than derived

The shipped documents never state what muzzle size a "Pistol", "Shotgun" or "Enemy Cannon" has; those sizes were only ever implied by the old Impact Strength values. An applier rescaling the examples would have to infer each one backwards, and would hit the Heavy Cannon collision above with no way to resolve it.

`tasks.md` section 3 therefore fixes every muzzle size and lists every before/after value explicitly, including the three locations that must *not* change. This is deliberately more prescriptive than this repo's usual task style, because the work is arithmetic across many small sites where a single wrong inference propagates silently.

### Two examples are rebuilt rather than rescaled

`DMG-017`'s example currently teaches "just barely enough strength to continue" (remaining 1 against a Resistance-1 minifig). A 4×4 muzzle would leave remaining 9 against Resistance 3 and lose that point entirely; the chosen 2×2 muzzle leaves remaining 3 against Resistance 3 and preserves it exactly.

Combat Example 4 changes meaning under the new scale: a tripled Enemy Cannon would punch through the Mounted Cannon with strength to spare, so the example's tidy "only the weapon is affected" conclusion would no longer hold. Setting the Enemy Cannon at a 1×1 muzzle (Strength 3 vs Resistance 2) leaves remaining 1, which then stops against the Jeep's one-brick hull (Resistance 3). The original conclusion survives, and the example gains a demonstration of penetration terminating — which no other example in the ruleset currently shows.

## Risks / Trade-offs

- **This is a rebalance.** Unlike the preceding audit changes, this one changes outcomes at the table. Playtesting after applying it is worthwhile in a way it was not for the documentation fixes.
- **Deeper penetration.** Tripled Strength means `DMG-017` carries impacts through more layers. Judged acceptable: each layer still rolls its own `DMG-015`, so added depth increases the number of independent 50% checks rather than guaranteeing anything. If playtesting shows it dominates, the lever is `DMG-017`'s subtraction, not the scale.
- **Exact ties are now load-bearing.** Pistol vs minifig (`3 ≥ 3`) and infantry-max vs bunker (`6 ≥ 6`) both resolve on equality. `DMG-014` already specifies `≥`, so this is defined behaviour, but it means the scale has little slack at the low end — a minifig built one plate thicker than assumed would become immune to pistols again. Mitigated by `DMG-004` Example 1 stating the minifig measurement explicitly.
- **Larger numbers on the page.** Cosmetic. No rule other than `DMG-014` (comparison) and `DMG-017` (subtraction) reads Impact Strength.

### `WPN-021`'s table states the final value only; the brick step is prose

The alternative considered was an intermediate column (`Size 2 → 2 bricks → Strength 6`), making the physical reasoning visible at the point of use. Rejected: it puts a second unit back on the page, which is the defect this change exists to remove.

The specific failure it would invite is that Resistance cannot be expressed in bricks without loss — a four-plate shield is Resistance 4, or 1.33 bricks, which is why plate layers won as the unit in the first place. A table stating "muzzle 2×2 → 2 bricks" next to a component stating Resistance 6 sets up exactly the mixed-unit comparison (`2 < 6`, wrongly concluding failure) that the alignment is meant to eliminate.

The brick relationship is still the intuition worth carrying, so it is kept as prose and as an explicitly labelled shortcut — "a muzzle N studs wide defeats a component N bricks thick" — stated together with its limit, that it stops dividing evenly once a component is built from plates. Labelled as a shortcut it aids reasoning; presented as a table column it would read as the operative magnitude.

## Open Questions

- None. Not yet applied — proposal only this round.
