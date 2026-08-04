## Context

The trigger was a builder's observation: nothing stops someone putting a tiny hinged tile on a hull, calling it a door, and embarking through it. Checking confirmed it — the three rules that govern doors, ramps and access points ask only that the component *move*.

The interesting part is not that the gap exists. It is that the ruleset already had everything needed to close it and had simply never joined the pieces: a category for components that look functional but are not (**decorative**), a category for rules verified against the plastic rather than computed (**physical checks**, `GEO-004`), and a principle against fixed numbers (**Principle 13**).

## Decisions

### Width is derived from the Unit Base; only height is a physical check

The first draft made the whole rule a physical check — "pass the model through, no dimensions stated" — on the grounds that a Unit Base is a floor footprint of 4 × 3 studs and carries no height, so deriving an aperture from it would leave the height undefined.

That reasoning was half right and reached the wrong conclusion. The correct response to "UB gives width but not height" is to take the width from the Unit Base and the height from the model, not to discard the Unit Base for both.

**Width was already defined and the draft was ignoring it.** Infantry is not a loose minifigure. `CORE-001` calls the 4 × 3 plate "the standard base for infantry", `04-construction-standard.md` requires every infantry model to be mounted on one, and `TRN-002` states that gear and posture never change the single Unit Base it occupies. The object crossing a doorway is a minifigure *on a 4-stud-wide plate*, invariably. `CORE-002` then makes the 4-stud edge the front, so it is precisely that edge which enters an opening first.

Leaving width to a physical check invited an argument the game does not otherwise have. The first application of this change measured a bare minifigure's torso in millimetres and concluded the answer was 2 studs — a defensible measurement of the wrong object, and a sign that the rule had wandered out of the ruleset's own unit. Everything else in StudCraft is measured in Unit Bases; an aperture should not be the exception.

**Height genuinely has no Unit Base**, so that half stays physical: take the model and pass it through.

This respects Principle 13 rather than bypassing it. 4 studs is not a magic constant introduced here — it is the Unit Base, and the whole ruleset expresses distances, deployment areas and footprints in it. A rule that refused to use the game's own measuring unit would be inventing arbitrariness, not avoiding it.

The minifigure survives only as an illustration of the height failure: about 4 bricks tall on its base, against a 1 × 2 tile covering an opening under one brick high.

### The check is on the opening, not on the approach

Asked whether a ramp must pass the whole vehicle, the honest answer is that the question is aimed at the wrong object.

A ramp is a surface a model climbs; whether it can be climbed is already the Terrain Threshold's job (`08-vehicles.md`). What a model must fit *through* is the hatch the ramp folds down from. Measuring the opening rather than the approach answers the ramp question, and also catches the case the ramp framing misses entirely: a perfectly drivable ramp leading to a portal too low for the vehicle.

One rule, applied to the aperture, covers doors, hatches and ramps without a special case for any of them.

### The requirement attaches to the declared function, not to the component

`TRN-011` lists roof hatches as firing ports. `TRN-007` lists roof hatches as access points. The same piece of plastic is routinely both.

A rule written against component *names* would either exempt roof hatches from the check — reopening the hole for anyone who calls their tiny door a hatch — or apply it to firing ports and invalidate every observation slit in the game.

Writing it against the claimed function avoids both. A hatch used to embark must pass the embarking models. The same hatch used to shoot from carries no such requirement in that role. An observation slit that is only ever a firing port passes nothing but a line of sight.

This also makes the rule per-model rather than absolute: a hatch that passes a minifigure but not a motorcycle is an access point for one and decorative for the other. That reads odd stated flatly, and it is exactly right — the plastic does not change, the question does.

### The consequence is one that already exists

An opening too small does not trigger a penalty. The component is **decorative**, which `CMP-009`, `CMP-010` and `TRN-007` already define and already handle.

The change therefore adds a *criterion* to an existing category rather than a mechanic. Nothing new has to be learned to apply the outcome, and there is no new state to track.

`TRN-015` covers the worst case without amendment: passengers with no functional access point remaining are trapped. It was written for battle damage; construction reaches the same state by another road and needs no new text.

### `GEO-004` gains the aperture check

`GEO-004` enumerates the rules that are direct physical checks against the model as it sits on the table — currently Line of Sight and Cover. It says "at minimum", so leaving the list alone would not have been wrong.

It is added anyway, because Visual Geometry genuinely participates. Decorative greebling around a hatch narrows the hatch, for the same reason decorative plastic blocks a sight line: it is really there. A builder who has internalised "decoration never affects measured values" (`GEO-003`) can otherwise reasonably conclude that decoration cannot close a door. It can.

That makes the aperture check the third member of a family, not a lone exception, and `GEO-004` is where a reader goes to learn the family exists.

### Where the rule lives

`05-construction-components.md`. The requirement is about how a model is built, and that document owns the door, ramp, window and hatch components themselves.

`09-transport.md` and `07-movement.md` cite it rather than restating it — one idea stated once. `TRN-007` is where a reader asks "what counts as an access point", so it carries the citation most prominently.

## Risks / Trade-offs

- **Marginal fits become a table judgment.** Two players may disagree about whether a model *quite* passes. Mitigated by it being a construction check made once, when the model is built, with the model in hand — not a mid-game measurement under time pressure. The ruleset already accepts judgment of this kind for Line of Sight, which is far more frequent and far more contested.
- **Existing models may lose access points.** Deliberate, and the ruleset is a 0.x draft. The alternative is keeping doors that never functioned.
- **Only the height figure is approximate.** The width is exact and derived (a Unit Base is 4 studs), so the one soft number left is "about 4 bricks tall", which carries no rule weight and only illustrates the failure.
- **Marginal *heights* remain a judgment; marginal widths no longer are.** Splitting the rule this way removes most of the argument surface without pretending the rest away.
- **Per-model results read strangely at first.** "This hatch is an access point for infantry and decorative for the motorcycle" is correct but needs the sentence that explains it, which the rule carries.
- **The rule cannot be linted.** No script can check that a physical opening passes a physical model. It relies on the builder, like every other construction requirement in the document.

## Open Questions

None. Not applied — proposal only.
