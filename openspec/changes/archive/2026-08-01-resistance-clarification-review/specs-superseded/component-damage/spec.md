<!--
SUPERSEDED — retained as a record, not applied at archive time.

This delta modified "Geometry Defines Resistance" on the `component-damage` capability. A later merged change
modified the same requirement, so `editorial-reviews-cleanup` now carries the authoritative
version and this one would conflict with it if both were applied.

It is moved out of `specs/` rather than deleted so the archive still shows
what this change proposed. The reasoning that produced it lives in this
change's own proposal.md and design.md, and in git history.

Root cause, recorded once here: these deltas were written against `docs/`
while `openspec/specs/` was already several changes behind, so they never
formed a valid chain. Archiving close to merge, rather than in a batch of
seventeen, is what prevents this.
-->

## MODIFIED Requirements

### Requirement: Geometry Defines Resistance
A component's Resistance SHALL be the smallest structural cross-section, measured in plate layers, that an Impact must cross in its direction of travel. Resistance SHALL NOT be assigned as an arbitrary statistic.

The conversion SHALL be stated once and applied to every component without exception: a plate counts as 1, a brick counts as 3, and any other LEGO element counts as the plate-equivalent of its own thickness in the direction of travel. No component type SHALL be exempt from this measurement, and no component type SHALL be named as a special case — a moulded element is measured by the same conversion as a built one.

Because Impact Strength is expressed in the same unit (`10-weapons.md`, WPN-021), the Geometry Check SHALL compare two counts of plate layers rather than two different units.

#### Scenario: Resistance read from a single-plate cross-section
- **WHEN** a component is built such that an Impact crosses exactly 1 plate layer in its direction of travel
- **THEN** that component's Resistance is 1

#### Scenario: Resistance read from a brick-built cross-section
- **WHEN** a component is built from a single standard brick in its direction of travel
- **THEN** that component's Resistance is 3

#### Scenario: Resistance read from a multi-plate cross-section
- **WHEN** a component is built from four stacked plates in its direction of travel
- **THEN** that component's Resistance is 4

#### Scenario: Resistance read from a multi-brick cross-section
- **WHEN** a component is built two bricks thick in its direction of travel
- **THEN** that component's Resistance is 6

#### Scenario: Visually similar constructed components may have different Resistance
- **WHEN** two components occupy similar external dimensions but are built with different internal construction (e.g. one from a single brick, one from four stacked plates)
- **THEN** their Resistance values may differ according to their actual construction (3 vs. 4) — the count of physical layers, not the external silhouette, is what matters

#### Scenario: A moulded element is measured, not exempted
- **WHEN** a component is a single moulded LEGO element rather than a built assembly (for example a minifig torso, a windscreen, a wheel, or an accessory shield)
- **THEN** its Resistance is the plate-equivalent of its own thickness in the direction of travel, by the same conversion as any built component — a minifig torso is roughly one brick of material and therefore has Resistance 3

#### Scenario: No component carries a fixed or baseline Resistance
- **WHEN** any component's Resistance is determined
- **THEN** it is read from the model by the stated conversion, and no component type has a baseline, exempt, or material-derived value
