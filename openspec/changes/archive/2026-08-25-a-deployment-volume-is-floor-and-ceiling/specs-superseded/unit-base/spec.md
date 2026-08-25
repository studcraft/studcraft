<!--
SUPERSEDED — retained as a record, not applied at archive time.

This delta modified "Unit Base Projections" on the `unit-base` capability.
`general-review` (#130) modified the same requirement afterwards and is the
later change, so it now carries the authoritative version
(`system/workflow.md`, "When several changes modified the same requirement").

Applying both would conflict, and `scripts/archive_cut.py` processes a batch in
directory order with no dependency resolution — it would abort on the first.

`general-review`'s delta is written against `openspec/specs/unit-base/spec.md`
as it stands, which is the pre-#129 text, so it is complete on its own and does
not need this one applied first.

It is moved out of `specs/` rather than deleted so the archive still shows what
this change proposed. The reasoning that produced it lives in this change's own
proposal.md and design.md, and in git history.
-->

# unit-base Specification Delta

## MODIFIED Requirements

### Requirement: Unit Base Projections
A rule SHALL read whichever projection of the Unit Base volume it requires: the horizontal projection (4 × 3 studs) for distances, movement, deployment floors and footprints; the volume itself for transport capacity, interior space, and the model height checked against the agreed ceiling; and the vertical projection across the front (4 studs × 13 plate layers) for whether something passes through an opening. A projection SHALL supply a measured value only. A projection SHALL NOT replace a physical check: Line of Sight and Cover SHALL be resolved against the physical model on the table, never against a Unit Base silhouette.

#### Scenario: Deployment reads the horizontal projection
- **WHEN** a vehicle's Deployment Volume cost is computed
- **THEN** it is read from the horizontal projection of the Unit Bases it covers, and its height is charged nothing

#### Scenario: An opening is measured against the vertical projection
- **WHEN** an access opening is checked against an infantry model
- **THEN** the clear opening must measure at least 4 studs wide and 13 plate layers high

#### Scenario: Line of Sight is not traced against a projection
- **WHEN** visibility between an attacker and a target is resolved
- **THEN** it is resolved against the physical models on the table, and the Unit Base volume or any of its projections plays no part

#### Scenario: The agreed ceiling reads the volume
- **WHEN** a model is checked against the height agreed for the Deployment Volume
- **THEN** the reading is the volume itself rather than a projection of it, and the model's own height is measured from the surface it rests on to the top of its Gameplay Geometry
