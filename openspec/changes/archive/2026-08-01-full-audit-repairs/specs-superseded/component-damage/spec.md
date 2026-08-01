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
A component's Resistance SHALL be the smallest structural cross-section, measured in plate layers (the finest LEGO unit of height), that an Impact must cross in its direction of travel. A standard brick counts as 3 plate layers. Resistance SHALL NOT be assigned as an arbitrary statistic.

#### Scenario: Resistance read from a single-plate cross-section
- **WHEN** a component is built such that an Impact crosses exactly 1 plate layer in its direction of travel
- **THEN** that component's Resistance is 1

#### Scenario: Resistance read from a brick-built cross-section
- **WHEN** a component is built from a single standard brick (3 plate layers tall) in its direction of travel
- **THEN** that component's Resistance is 3

#### Scenario: Resistance read from a multi-plate cross-section
- **WHEN** a component is built from four stacked plates in its direction of travel
- **THEN** that component's Resistance is 4

#### Scenario: Visually similar components may have different Resistance
- **WHEN** two components occupy similar external dimensions but are built with different internal construction (e.g. one from a single brick, one from four stacked plates)
- **THEN** their Resistance values may differ according to their actual construction (3 vs. 4, not 1 vs. 4) — the count of physical layers, not the external silhouette, is what matters
