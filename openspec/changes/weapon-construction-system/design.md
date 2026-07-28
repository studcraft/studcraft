## Context

StudCraft's core principle is "The Model Is The Rules": physical LEGO construction determines gameplay behaviour instead of hand-authored stat blocks. Weapons are the first system built on this principle. There is no existing weapon or platform specification in `openspec/specs/` — this design establishes the geometric rules from scratch.

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

## Risks / Trade-offs

- [Risk] Fixed multiplier `Range = 2 × Weapon Length` may not scale well across very short or very long weapons once balance testing starts. → Mitigation: formula is isolated in `weapon-construction` spec as a single requirement; can be revised in a follow-up change without touching muzzle/capacity rules.
- [Risk] Square-only muzzle constraint may feel restrictive for some visual weapon designs (e.g. wide flamethrower nozzles). → Mitigation: explicitly called out as current-proposal status in source material; can be revisited if playtesting shows a need for non-square muzzles, via a MODIFIED requirement in a later change.
- [Risk] Because Weapon Capacity uses only total Length (not Width or footprint area), two platforms with identical Platform Length but very different bulk/footprint get identical capacity. → Mitigation: acceptable per design consequence section — length-based scaling is the intentional emergent-specialization mechanism; revisit only if it produces degenerate builds in practice.
- [Risk] No validation/tooling is specified for actually checking a physical or digital model against these rules. → Mitigation: out of scope per Non-Goals; a future change can define a validation/import pipeline against this spec.

## Open Questions

- Should Weapon Capacity account for anything besides Length (e.g. Width or footprint area) once more playtesting data exists? Deferred — not blocking this change.
- Will future impact/damage specs need additional muzzle metadata beyond size (e.g. material, ammo type)? Deferred to future OpenSpecs per proposal scope.
