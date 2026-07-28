## Context

StudCraft's core principle is "The Model Is The Rules": physical LEGO construction determines gameplay behaviour instead of hand-authored stat blocks. A weapon ruleset already exists in `docs/10-weapons.md` (WPN-001 through WPN-017), but it under-uses the principle: muzzles are locked to a single fixed part, and nothing about muzzle size affects gameplay. This design formalizes muzzle geometry (size, footprint partitioning) as the missing piece, refining rather than replacing that ruleset. There is no existing OpenSpec artifact for weapons in `openspec/specs/` (this is the first formal spec for the capability), which is why this reads as a from-scratch design even though it lands on top of an existing ruleset document.

Two capabilities are introduced together because they share the same measurement unit (stud-length) and are tightly coupled: a weapon's Length determines both its Range and its Weapon Capacity cost, and Weapon Capacity is what constrains how many/which weapons a platform can mount.

## Goals / Non-Goals

**Goals:**
- Define a fully deterministic mapping from weapon geometry to three gameplay properties: Range, Attack Dice, Impact Strength.
- Define validity rules for weapon construction (body continuity, single firing face, square muzzles, proportion constraints) that can be checked by inspecting a model/bounding-box representation.
- Define a platform-level capacity constraint so weapon load-out scales naturally with platform size, without unit classes or weapon slots.

**Non-Goals:**
- Impact/damage resolution, armor interaction, penetration, area effects — deferred to future specs.
- Any concrete numeric balancing (e.g. is Range = 2× Length the "right" multiplier) — this spec fixes the formula shape, not final game balance, which can be tuned later without changing the structural rules.
- Physical LEGO-model parsing/detection implementation (e.g. computer vision or CAD import) — this spec defines the abstract geometric model (Length, Width, Footprint, muzzle grid) that any such implementation must conform to.

## Decisions

**Weapon geometry represented as: Length, Width, and a Width×Width Front Footprint grid of square muzzle cells.**
Alternative considered: representing weapons as arbitrary 3D voxel models. Rejected for this spec because it adds implementation complexity without changing derived stats — only the Front Footprint (a 2D square grid) and the two scalar body dimensions (Length, Width) actually affect gameplay properties. Full 3D modeling is a rendering/asset concern, not a rules concern.

**Muzzles must be square; rectangular muzzles are invalid.**
This keeps Impact Strength a single scalar per muzzle (muzzle size) rather than requiring a width/height pair, and matches the stated real-world analogy (barrels have circular/square cross-sections, not rectangular ones).

**Weapon Capacity is a single linear constraint (`Σ(Weapon Length) ≤ Platform Length`), not a slot system.**
Alternative considered: fixed weapon hardpoints/slots per platform (common in other tabletop systems). Rejected because it reintroduces "hidden" platform stats (number of slots, slot sizes) that aren't derivable from the model — contradicts "The Model Is The Rules." A single length-sum constraint is fully derivable from the platform's own bounding box.

**Platform Length is defined as the largest dimension of the platform's base/bounding box.**
Keeps the same measurement approach (bounding-box dimension) used for weapons, so the same "measure the model" logic applies uniformly to both weapons and platforms.

**Muzzles may be placed directly adjacent, with no mandatory body separation between them — superseding WPN-007.**
Alternative considered: keep WPN-007's existing 1-stud-separation rule alongside the new footprint model. Rejected because the source design's own canonical examples (Twin Barrel, Quad Barrel — muzzles packed edge-to-edge in a 2×2 block) require adjacency to work, and a fixed "1 stud of gap" constant is itself an arbitrary rule not derivable from the model, which sits awkwardly next to "The Model Is The Rules." The footprint's own non-overlap requirement is sufficient physical validation — two square muzzles either occupy distinct cells or they don't.

**Weapon Length is the longest dimension of the functional (non-decorative) Weapon Body — superseding WPN-003's "rear of body to foremost functional muzzle" measurement.**
Alternative considered: keep WPN-003's method unchanged and layer the new footprint/muzzle rules on top of it. Rejected because it would leave two different, subtly incompatible definitions of "Weapon Length" active at once (one stops at the muzzle and explicitly ignores trailing decoration; the other is a raw bounding-box span) once the same term is reused across both documents. The bounding-box definition is kept because it matches the same "measure the model" approach used for Width, the Footprint, and Platform Length — one measurement method, applied consistently. Decorative elements are still excluded, consistent with the existing principle that decoration has no gameplay effect (WPN-015).

## Design Consequences

Because Range, Attack Dice, Impact Strength, and Weapon Capacity are all derived directly from geometry, weapon specialization emerges without any unit classes or weapon slots:

- A larger Weapon Front Footprint allows more muzzles, larger muzzles, and more combinations.
- A wider weapon requires a longer body (`Length ≥ 2 × Width`), and a longer weapon consumes more Weapon Capacity.
- A platform with more Weapon Capacity must itself be longer (`Platform Length` is the capacity ceiling).
- As a result: small platforms naturally carry light weapons, medium platforms carry medium weapons, and large platforms carry heavy weapons — purely as a consequence of geometry, not an authored rule.

## Risks / Trade-offs

- [Risk] Fixed multiplier `Range = 2 × Weapon Length` may not scale well across very short or very long weapons once balance testing starts. → Mitigation: formula is isolated in `weapon-construction` spec as a single requirement; can be revised in a follow-up change without touching muzzle/capacity rules.
- [Risk] Square-only muzzle constraint may feel restrictive for some visual weapon designs (e.g. wide flamethrower nozzles). → Mitigation: explicitly called out as current-proposal status in source material; can be revisited if playtesting shows a need for non-square muzzles, via a MODIFIED requirement in a later change.
- [Risk] Because Weapon Capacity uses only total Length (not Width or footprint area), two platforms with identical Platform Length but very different bulk/footprint get identical capacity. → Mitigation: acceptable per Design Consequences above — length-based scaling is the intentional emergent-specialization mechanism; revisit only if it produces degenerate builds in practice.
- [Risk] Removing WPN-007 (muzzle separation) and redefining Weapon Length (WPN-003) both invalidate existing constructions built under the current `docs/10-weapons.md`. → Mitigation: flagged **BREAKING** in the proposal; CHANGELOG entry should use `**Bump:** major`.
- [Risk] No validation/tooling is specified for actually checking a physical or digital model against these rules. → Mitigation: out of scope per Non-Goals; a future change can define a validation/import pipeline against this spec.

## Open Questions

- Should Weapon Capacity account for anything besides Length (e.g. Width or footprint area) once more playtesting data exists? Deferred — not blocking this change.
- Will future impact/damage specs need additional muzzle metadata beyond size (e.g. material, ammo type)? Deferred to future OpenSpecs per proposal scope.
