## Context

Three reviews arrived together, each declaring itself purely editorial. Verifying them against shipped text found that judgement was mostly right — but not entirely. One item is a real ambiguity in a load-bearing rule, one proposes a fix that would silently change every weapon's Range, and two would remove text that is doing useful work.

The reviews were also written against a ruleset that already moved: `ae09710` aligned Impact Strength and Resistance onto plate layers and deleted the minifig exception. Every accepted item was re-checked against post-`ae09710` text.

## Decisions

### `DMG-003`'s hollow clarification is extended past what the review asked for

The review's suggested wording covers empty space: "Empty internal space contributes no Resistance." That is correct but incomplete. The likelier misreading is not that a player counts air — it is that they count *both walls* of an enclosure as one component and arrive at Resistance 6 for a hull that is two independent Resistance-3 components.

`DMG-001` (a vehicle is a collection of independent components) and `DMG-017` (Penetration resolves them in sequence) already settle this, but neither is where a reader looks when computing Resistance. The accepted wording states both halves — air contributes nothing, and separate walls are separate components, never summed — at `DMG-003` itself.

### The Weapon Length fix names the axis without changing the measurement

`WPN-003` says "the longest dimension of the functional Weapon Body" and stops. Which axis that runs along is only inferable by chaining `WPN-018` (Width is the smallest dimension) and `WPN-019` (the Weapon Front Footprint is Width × Width, so the Front is perpendicular to the length). The review is right that this is under-specified.

Its proposed replacement — "from its rear mounting or grip to the outer face of the functional muzzle" — is not a clarification but a different measurement. It pulls mounting hardware into the Weapon Body, which `WPN-009` treats as separate, and `WPN-003` already excludes non-functional elements. Because `WPN-005` derives Range as `Weapon Length × 2` and `WPN-004` caps total mounted length at Platform Length, adopting it would change every Range and every legality check in the game — in a change whose stated premise is "no mechanical changes."

The accepted wording states the axis explicitly and reaffirms the exclusion, leaving every existing measurement identical.

### Keep the material list in `DMG-008`

The review reads "glass, metal, wood, infantry" as residue of the deleted material system. It is the opposite: it is the rule naming the exact temptation it forbids. A reader who wonders whether glass should behave differently finds glass named and answered. Stripped to "regardless of what it represents", the rule becomes true but no longer useful — and the material system's removal is precisely why that answer needs to stay findable.

### Keep the component list in `MEL-002`

Removing it would leave `MEL-010` — retained purely as an ID-stability placeholder pointing at `MEL-002` for vehicle component targeting — pointing at a rule that no longer mentions vehicle components at all. The list is also the only place the melee document enumerates what is reachable. The review's stated benefit ("keeps the rule universal") is already satisfied by the rule's own first sentence, which the examples follow rather than qualify.

### `MEL-005` loses its step list but the Melee Summary keeps one

The step sequence currently appears four times: `DMG-009` (arrow form), `11-combat.md`'s Combat Flow diagram, `MEL-005`, and the Melee Summary. Cutting `MEL-005`'s copy leaves three, and only one of those is a rule.

The Melee Summary keeps its enumeration. A summary restating a sequence for a reader who has just finished the document is a different act from a rule restating it as if it owned it — the first is a recap, the second is a second source of truth. Its citation is retightened from `MEL-005` to `DMG-009`, so the recap credits the rule that actually owns the sequence rather than the one that used to repeat it.

## Risks / Trade-offs

- **`DMG-003` grows.** It is already the longest rule in the damage system, and this adds a paragraph. Judged worth it: it is also the most consulted, and the alternative is a correct answer that lives in two other rules a reader has no reason to visit.
- **Ten changes across three documents in one pass**, plus two required glossary follow-ons. Each is independent and small, but the volume raises the chance of a stale cross-reference — both follow-ons were caught while drafting (the glossary's `Functional Striking End` also says "point of contact", and `Weapon Body` also omits the axis). Section 6's greps exist to catch any that remain.
- **Rejecting five of fifteen items** may read as dismissive of the reviews. The ten accepted include the only substantive find across all three, and the rejections are recorded with reasons so the next review round does not re-raise them.

## Open Questions

None. Not applied — proposal only.
