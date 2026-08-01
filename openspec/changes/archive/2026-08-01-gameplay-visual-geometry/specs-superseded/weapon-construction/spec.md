<!--
SUPERSEDED — retained as a record, not applied at archive time.

This delta modified "Weapon Length Determines Range" on the `weapon-construction` capability. A later merged change
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

### Requirement: Weapon Length Determines Range
Weapon Length SHALL be measured as the longest dimension of the functional Weapon Body, excluding Visual Geometry (per the `geometry-layers` capability). Range SHALL be derived as `Range = 2 × Weapon Length`.

#### Scenario: Range computed from length
- **WHEN** a weapon has a Weapon Length of N
- **THEN** its Range is 2 × N

#### Scenario: Visual Geometry excluded from length
- **WHEN** a Visual Geometry element extends beyond the functional Weapon Body
- **THEN** that element is not counted when measuring Weapon Length
