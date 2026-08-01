## ADDED Requirements

### Requirement: Unit Base Measurement
The Unit Base (UB) SHALL be StudCraft's universal measurement, equal to a LEGO Plate measuring 4×3 studs. Every distance, deployment area, and vehicle or infantry footprint SHALL be expressed using this unit.

#### Scenario: Unit Base dimensions
- **WHEN** a Unit Base is measured
- **THEN** it measures 4×3 studs

#### Scenario: Infantry occupies one Unit Base
- **WHEN** an infantry model is placed on its standard base
- **THEN** it occupies exactly one Unit Base

#### Scenario: Vehicle footprint measured in Unit Bases
- **WHEN** a vehicle's footprint is measured
- **THEN** it is expressed as a number of Unit Bases, not an independent unit of measure
