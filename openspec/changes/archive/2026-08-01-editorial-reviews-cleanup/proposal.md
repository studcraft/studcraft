## Why

Three external reviews (`delete-me-1.md` Damage, `delete-me-2.md` Weapons, `delete-me-3.md` Melee) propose fifteen editorial items across the three documents. All three declare "no mechanical changes recommended."

Each item was checked against the shipped text at `ae09710` (after `Align Impact Strength and Resistance units`). Of the fifteen: **ten are valid and worth applying, five are rejected** — one is already implemented, two are redundant with existing text, and two would make the ruleset worse if applied.

One accepted item is more than editorial. `DMG-003` defines Resistance as "the smallest structural section that an impact must cross in its direction of travel" but never says that empty space contributes nothing, nor that the two walls of an enclosed structure are separate components rather than one summed thickness. A reader can currently conclude that a hollow tank hull with 1-brick front and 1-brick rear armour has Resistance 6. It has Resistance 3, twice, resolved in sequence by Penetration. This is a genuine ambiguity in the most-consulted rule of the damage system.

## What Changes

### Accepted — `docs/16-damage-system.md`

- **DMG-003**: state that only material the Impact crosses contributes; components are assumed hollow unless built solid; and where an Impact would cross more than one wall, each wall is a separate component (DMG-001) whose outer layer protects what lies behind it (DMG-007), resolved in sequence by Penetration (DMG-017) and never summed into one Resistance. *(delete-me-1 REVIEW-001, extended — the reviewer did not identify the summing case, which is the more likely misreading.)*
- **DMG-004**: add Example 7, a vehicle hull, demonstrating the hollow case. *(delete-me-1 REVIEW-002)*
- **Combat Examples**: add Example 5, an attack stopped by the Geometry Check alone. All four current examples pass the Geometry Check, so the ruleset never shows the `Strength < Resistance` path it explicitly defines. *(delete-me-1 REVIEW-004)*

### Accepted — `docs/10-weapons.md`

- **WPN-003**: state which axis Weapon Length is measured along — the firing axis, perpendicular to the Weapon Front (WPN-019) — and that mounting hardware is excluded. *(delete-me-2 REVIEW-001, wording rejected; see Impact.)*
- **WPN-002**: add the ranged-side conceptual definition — a muzzle is the contact surface through which a weapon transfers energy into an Impact — by *replacing* the existing final line rather than adding one. `MEL-013` already owns the muzzle/striking-end equivalence in full; restating it here would duplicate it verbatim, so WPN-002 states only its own half and points at MEL-013 for the rest. *(delete-me-2 REVIEW-002, scoped down)*
- **Summary**: add the closing architectural line already mirrored by `CBT-011`. *(delete-me-2 REVIEW-005)*

### Accepted — `docs/12-melee.md`

- **MEL-005**: replace the enumerated step list with a reference. The sequence currently appears four times — MEL-005, the Melee Summary, `DMG-009` (arrow form), and `11-combat.md`'s Combat Flow diagram. Cutting MEL-005's copy leaves the canonical statement, one diagram, and one end-of-document recap, which is the intended shape. *(delete-me-3 REVIEW-001)*
- **MEL-010**: shorten to a two-line placeholder. *(delete-me-3 REVIEW-003)*
- **MEL-012**: correct the scope sentence — the document defines physical contact, reach, and striking ends, not only Attack Dice generation. *(delete-me-3 REVIEW-005)*
- **MEL-013**: fix an internal inconsistency — the rule opens with "physical point of contact" and closes with "physical contact surface" for the same thing. Unify on "contact surface", matching muzzle terminology. *(delete-me-3 REVIEW-004)*

### Accepted — `docs/14-glossary.md` (consequential, not from the reviews)

Two entries break as a side effect of the above and must move with them: `Functional Striking End` also uses "point of contact" (changes with MEL-013), and `Weapon Body` omits the measurement axis (changes with WPN-003). The remaining glossary entries are deliberately left alone — the glossary points at owning rules rather than mirroring their prose.

### Rejected

| Item | Reason |
|---|---|
| delete-me-1 REVIEW-003 — delete "glass, metal, wood, infantry" from `DMG-008` | The rule is titled *No Material-Specific Mechanics*. Naming the materials is the rule doing its work: it pre-empts "but glass should shatter." Removing the list leaves an abstract sentence that no longer answers the question it exists to answer. |
| delete-me-2 REVIEW-003 — state Strength belongs to each muzzle | Already shipped. `WPN-021` closes with "each die's Impact Strength depends only on the muzzle or striking end that rolled it." |
| delete-me-2 REVIEW-004 — add a Weapons/Combat boundary statement **as a rule** | Rejected as a rule, absorbed as framing. `WPN-013` already defers the entire attack sequence to `CBT-001`, and `WPN-008` defers targeting to `CBT-006`/`CBT-007`, so a new rule would restate existing deferrals. The content survives in the accepted Summary line (REVIEW-005), where it frames without creating a second place to maintain. |
| delete-me-3 REVIEW-002 — delete the component list from `MEL-002` | Net loss. It is the only place melee names reachable component types, and "Vehicle crew" is the content `MEL-010` points at. Removing it makes `MEL-010`'s pointer emptier, not cleaner. |
| delete-me-3 REVIEW-006 — add an architectural line to the Melee Summary | Redundant. The Summary's opening sentence already says it: "Ranged and melee differ only in how an Impact is generated." |

## Impact

No mechanical change. No rule ID added, removed, or renumbered. No numeric value changes.

`DMG-003`'s addition is a clarification, not a new rule — it states the reading `DMG-001` and `DMG-017` already imply, at the point where readers actually go looking.

**One reviewer wording explicitly not adopted.** delete-me-2 REVIEW-001 proposes measuring Weapon Length "from its rear mounting or grip to the outer face of the functional muzzle." That would include mounting hardware in the measurement, contradicting `WPN-003`'s existing "decorative elements are ignored" and `WPN-009`'s treatment of mounts as separate from the weapon. It would also silently change every Range in the game, since Range is `Weapon Length × 2` (`WPN-005`). The ambiguity the reviewer identified is real; only the proposed fix is wrong. The accepted version names the axis without changing what is measured.

**Requires its own branch** per `openspec/config.yaml`. The working tree is currently on `resistance-clarification-review`.

Not applied — proposal only.
