## MODIFIED Requirements

<!--
Authoritative delta for "Geometry Defines Resistance".

Four merged changes modified this requirement: full-audit-repairs (#28),
audit-round2-repairs (#29), resistance-clarification-review (#30) and this
one (#31). Each was written against `docs/` rather than against the living
spec, which had already fallen behind, so their deltas never formed a valid
chain. This change is the last of the four, so it carries the complete,
final wording; the other three have their component-damage deltas retired
under `specs-superseded/` with a note rather than deleted.

Two scenario names are kept exactly as they appear in the living spec —
"single-brick cross-section" and "Visually similar components…" — with their
content corrected. Renaming them would drop them silently at archive time.
Stable identifier, updated content: the same convention MEL-010 and CBT-011
follow in the ruleset itself.
-->

### Requirement: Geometry Defines Resistance
A component's Resistance SHALL be the smallest structural cross-section, measured in plate layers, that an Impact must cross in its direction of travel. Resistance SHALL NOT be assigned as an arbitrary statistic.

The conversion SHALL be stated once and applied to every component without exception: a plate counts as 1, a brick counts as 3, and any other LEGO element counts as the plate-equivalent of its own thickness in the direction of travel. No component type SHALL be exempt from this measurement, and no component type SHALL be named as a special case — a moulded element is measured by the same conversion as a built one.

Only material the Impact actually crosses SHALL contribute to Resistance. Empty internal space SHALL contribute nothing, and a component SHALL be assumed hollow unless it is physically built solid.

Where an Impact would cross more than one wall of an enclosed structure, those walls SHALL be treated as separate components, each with its own Resistance, resolved in sequence by Penetration. Their thicknesses SHALL NOT be summed into a single Resistance value.

Because Impact Strength is expressed in the same unit (`10-weapons.md`, WPN-021), the Geometry Check SHALL compare two counts of plate layers rather than two different units.

#### Scenario: Resistance read from a single-brick cross-section
- **WHEN** a component is built such that an Impact crosses exactly 1 brick in its direction of travel
- **THEN** that component's Resistance is 3, because a brick counts as 3 plate layers

#### Scenario: Resistance read from a single-plate cross-section
- **WHEN** a component is built such that an Impact crosses exactly 1 plate layer in its direction of travel
- **THEN** that component's Resistance is 1

#### Scenario: Resistance read from a multi-plate cross-section
- **WHEN** a component is built from 4 stacked plates such that an Impact must cross all 4 in its direction of travel
- **THEN** that component's Resistance is 4

#### Scenario: Resistance read from a multi-brick cross-section
- **WHEN** a component is built two bricks thick in its direction of travel
- **THEN** that component's Resistance is 6

#### Scenario: Visually similar components may have different Resistance
- **WHEN** two components occupy similar external dimensions but are built with different internal construction (e.g. one from a single brick, one from four stacked plates)
- **THEN** their Resistance values may differ according to their actual construction (3 vs. 4) — the count of physical layers, not the external silhouette, is what matters

#### Scenario: Empty interior contributes no Resistance
- **WHEN** a component encloses empty space behind its structural wall
- **THEN** only the wall's own plate-layer count is its Resistance, and the empty space adds nothing

#### Scenario: Opposing walls of a hollow structure are not summed
- **WHEN** an Impact strikes a hollow structure whose front and rear walls are each one brick thick
- **THEN** the front wall has Resistance 3 and the rear wall has Resistance 3 as a separate component, resolved in sequence by Penetration — the structure does not have a single Resistance of 6

#### Scenario: A moulded element is measured, not exempted
- **WHEN** a component is a single moulded LEGO element rather than a built assembly (for example a minifig torso, a windscreen, a wheel, or an accessory shield)
- **THEN** its Resistance is the plate-equivalent of its own thickness in the direction of travel, by the same conversion as any built component — a minifig torso is roughly one brick of material and therefore has Resistance 3

#### Scenario: No component carries a fixed or baseline Resistance
- **WHEN** any component's Resistance is determined
- **THEN** it is read from the model by the stated conversion, and no component type has a baseline, exempt, or material-derived value
