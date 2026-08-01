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
For a component the player actually builds — a wall, a shield, a hull, a door — Resistance SHALL be the smallest structural cross-section, measured in plate layers (the finest LEGO unit of height), that an Impact must cross in its direction of travel. A standard brick counts as 3 plate layers. Resistance SHALL NOT be assigned as an arbitrary statistic.

A fixed piece that offers no construction choice — most notably a minifig — SHALL NOT be measured this way. It SHALL use a fixed baseline Resistance of 1 instead of a literal plate-layer count. This is not a material-specific exception (every component still resolves Impacts through the same Geometry Check and Damage Roll); it reflects that the piece's form isn't a construction choice to measure.

#### Scenario: Resistance read from a single-plate cross-section
- **WHEN** a constructed component is built such that an Impact crosses exactly 1 plate layer in its direction of travel
- **THEN** that component's Resistance is 1

#### Scenario: Resistance read from a brick-built cross-section
- **WHEN** a constructed component is built from a single standard brick (3 plate layers tall) in its direction of travel
- **THEN** that component's Resistance is 3

#### Scenario: Resistance read from a multi-plate cross-section
- **WHEN** a constructed component is built from four stacked plates in its direction of travel
- **THEN** that component's Resistance is 4

#### Scenario: Visually similar constructed components may have different Resistance
- **WHEN** two constructed components occupy similar external dimensions but are built with different internal construction (e.g. one from a single brick, one from four stacked plates)
- **THEN** their Resistance values may differ according to their actual construction (3 vs. 4, not 1 vs. 4) — the count of physical layers, not the external silhouette, is what matters

#### Scenario: A minifig uses a fixed baseline, not a measurement
- **WHEN** a component is a minifig
- **THEN** its Resistance is 1 by fixed baseline, regardless of the minifig piece's actual molded thickness
