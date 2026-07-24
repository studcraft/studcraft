# Repository Structure

```
/
├── README.md
├── CODE_OF_DESIGN.md
├── CONTRIBUTING.md
├── CHANGELOG.md
├── LICENSE
├── AGENTS.md
├── system/
│   ├── agent-responsibilities.md
│   ├── design-process.md
│   ├── documentation-standards.md
│   ├── workflow.md
│   ├── communication.md
│   └── vision.md
│
├── openspec/
│   ├── config.yaml
│   ├── changes/
│   └── specs/
│
├── scripts/
│   └── generate_site_docs.py
│
├── site/
│   ├── _config.yml, Gemfile, index.md   (Jekyll site source, hand-maintained)
│   └── docs/   (generated copy of /docs, gitignored — do not hand-edit)
│
└── docs/
    ├── 01-foundations.md
    ├── 02-core-rules.md
    ├── 03-game-flow.md
    ├── 04-construction-standard.md
    ├── 05-construction-components.md
    ├── 06-deployment.md
    ├── 07-movement.md
    ├── 08-vehicles.md
    ├── 09-transport.md
    ├── 10-weapons.md
    ├── 11-combat.md
    ├── 12-melee.md
    ├── 13-materials.md
    └── 14-glossary.md
```

Agents should preserve this modular organization.

---

# Documentation Guidelines

Each document should have one clear responsibility.

Avoid mixing unrelated systems.

Rules should:

- Be deterministic.
- Be concise.
- Be easy to reference.
- Reuse existing terminology.

Every document should include:

- Purpose
- Design Philosophy
- Rule Definitions
- Summary

---

# Naming Conventions

Rule identifiers should remain stable.

Examples:

```
MOV-001
WPN-001
CBT-001
TRN-001
FLOW-001
```

Each document owns its own namespace.

---

# Versioning

StudCraft follows Semantic Versioning.

```
MAJOR.MINOR.PATCH
```

Examples:

- 0.1.0
- 0.2.0
- 1.0.0

Agents should update the changelog whenever behaviour changes.
