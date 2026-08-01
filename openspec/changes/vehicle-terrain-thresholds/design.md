## Context

Infantry have four terrain rules (`MOVE-009` … `MOVE-014`). Vehicles have none, and both `07-movement.md` and `MOVE-016` say so in writing. Every vehicle-versus-terrain question is currently settled by table consensus under the Physical Priority principle, which is a reasonable fallback but not a rule.

The design constraint is Principle 1: whatever fills the gap must be readable off the model, not assigned as a statistic. That rules out a table of clearance values per vehicle class and rules in reading a threshold from the locomotion the builder actually built.

## Decisions

### One threshold per vehicle, read from its locomotion

Each locomotion type carries a natural physical limit that a builder has already decided by building it:

- **Wheels and tracks — the axle.** A wheel cannot climb an obstacle taller than its own centre; push a wheel at a step above its axle and it drives into the step rather than over it. On a LEGO model, axle height is the wheel's radius, so the rule reads as "half the wheel's diameter" and needs no measuring beyond looking.
- **Walkers — the knee.** A leg lifts its foot as high as the joint allows. The knee is a visible, built component on any walker that satisfies `CMP-006`.
- **Hover — the ground clearance.** How high the hull floats is the single most visible property of a hover build, and it is exactly what determines what fits underneath.

None of these is a number the rules assign. All three are measurements the model already contains.

### Hover sits between the other two by being good at the opposite thing

The brief was that hover should be "something between" wheels and walkers. The interesting reading is not a middling threshold but a different shape of capability.

Hover vehicles typically have the **lowest** obstacle threshold in the game — a skirt one or two plates off the ground is stopped by a wall a jeep drives straight over. In exchange they are the only locomotion that cannot be stranded: a depression is something to pass over, not fall into.

That produces a real trade-off rather than a ranking. Hover is the worst at walls and the best at ground, wheels are the reverse, and walkers scale with how tall the builder made the legs. A player picks locomotion for terrain, and the choice is visible on the table.

The immunity is bounded so it does not become strictly dominant: a hover vehicle still cannot cross a gap wider than its own footprint, because there has to be something under it to hover above.

### Stranded reuses `VEH-019` rather than inventing a state

A vehicle that drops into a depression deeper than its threshold is Immobilized — the state `VEH-019` already defines, including that it stays on the battlefield and keeps operating its remaining systems. No new state, no new marker, no new recovery mechanic.

Recovery is deliberately left undefined, in the same style as `VEH-013`'s "unless another crew member takes over (future rules)". Inventing a self-recovery action here would mean inventing an AP cost and a success condition, neither of which the brief asked for and both of which deserve their own design pass.

### Falling reuses infantry's dice but not infantry's target

`MOVE-016` cannot be copied across. A minifig is one component, so "the faller's Component State advances one step" has an obvious subject; `DMG-001` says a vehicle is not one component, so the same sentence has no subject at all. That single difference is the whole design problem.

The dice stay identical — one D6 per complete brick, each an independent Damage Roll, no Geometry Check and no Resistance. Skipping the Geometry Check is not a new exception: `MOVE-016` already skips it because a fall has no attacker and therefore no Impact Strength, and that reasoning applies to a tank exactly as it does to a minifig. Resolving vehicle falls through `DMG-014` instead would give the game two different falling rules, against Principle 12.

What changes is where each failure lands: on a component that physically touches the ground when the vehicle comes down. That is model-readable — look underneath — and it needs no list of which components qualify, because the build answers it.

An agreeable property emerges rather than being designed: falls wreck locomotion, and destroyed locomotion means Immobilized (`VEH-019`). A vehicle that survives a fall is usually stuck where it landed anyway, which converges with `VEH-025`. Drops and falls turn out to be the same idea seen from two heights, not two mechanics competing.

The free height is the vehicle's own Terrain Threshold rather than infantry's fixed first brick. A jeep dropping less than its axle height has driven off a kerb; the same drop is a genuine fall for a hover skirt. Deriving it keeps the rule model-driven and ties `VEH-026` to `VEH-021` instead of introducing a second constant.

### Crew are never harmed, and that is a choice

A closed transport can fall fifteen bricks and its eight passengers walk out unhurt.

The alternative — passengers roll once the hull reaches Dead — is more realistic and was considered. It was rejected on frequency: nobody drives their own transport off a cliff deliberately, so the rule would add a condition to the rare case of an already-rare case. Principle 11 settles it.

The rule says "this is a deliberate simplification" in so many words, so it reads as a decision rather than as something the next reviewer should close.

### The real cost needed no rule

A vehicle at the bottom of a ravine is a trap. Its passengers disembark normally under `TRN-006`, and then meet the ravine's walls as ordinary terrain — `MOVE-011` already demands a slope, stair or ramp for anything 7 plate layers or higher.

So driving into a pit can strand a squad as effectively as it strands the vehicle, and none of that required writing anything. It falls out of infantry rules that already exist. `VEH-026` only points at it, because a player who does not notice will misjudge the risk.

### Hover takes no falling damage either

Hover vehicles descend under power rather than falling. This extends their `VEH-024` immunity from drops to falls, which is consistent — their whole identity is ignoring the ground — and it is paid for by having the lowest obstacle threshold in the game.

### Slopes, stairs and vertical access stay open

Three of the four gaps `07-movement.md` names remain. The deferral note is rewritten to say exactly which one closed, rather than deleted, so nobody reads this change as having solved vehicle terrain entirely.

### Five rules rather than two

The content could compress into one rule with three cases plus one for stranding. It is split into five to mirror `VEH-008` … `VEH-011`, which already devote a rule each to wheeled, tracked, walker and hover behaviour.

Consistency with the surrounding document (Principle 12) is judged worth more here than the smaller rule count (Principle 11), because a reader looking up "how do walkers handle terrain" should find it in the same shape as "how do walkers turn".

## Risks / Trade-offs

- **Threshold measurement depends on build quality.** A vehicle with half-buried wheels or an ambiguous knee makes the threshold arguable. Mitigated by fallbacks in each rule — half the track run, half the leg height — and ultimately by Physical Priority, which already governs disputes of this kind.
- **Hover may prove too strong or too weak.** Its profile is deliberately extreme in both directions. Whether the trade lands correctly is a playtesting question, and the dial is the ground clearance a builder chooses, not a number in the rules.
- **Tall-legged walkers dominate terrain.** A walker on very long legs beats both other types. The intended counterweight is that the same legs raise its silhouette, and `CORE-008` makes visibility purely physical — a taller model is easier to see and therefore to shoot. That counterweight is real but indirect, and worth watching.
- **Five new rule IDs in one change**, all additive. Nothing is renumbered.

## Open Questions

None. Not applied — proposal only.
