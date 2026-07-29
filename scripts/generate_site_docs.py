#!/usr/bin/env python3
"""Generate Jekyll-ready copies of docs/*.md into site/docs/.

The files in docs/ are the canonical rulebook and must never contain
Jekyll front matter. This script injects front matter (title, nav_order)
into generated copies at build time only. site/docs/ is gitignored.
"""

import pathlib
import shutil

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
SOURCE_DIR = REPO_ROOT / "docs"
DEST_DIR = REPO_ROOT / "site" / "docs"

TITLES = {
    "01-foundations.md": "Foundations",
    "02-core-rules.md": "Core Rules",
    "03-game-flow.md": "Game Flow",
    "04-construction-standard.md": "Construction Standard",
    "05-construction-components.md": "Construction Components",
    "06-deployment.md": "Deployment",
    "07-movement.md": "Movement",
    "08-vehicles.md": "Vehicles",
    "09-transport.md": "Transport",
    "10-weapons.md": "Weapons",
    "11-combat.md": "Combat",
    "12-melee.md": "Melee",
    "13-materials.md": "Materials",
    "14-glossary.md": "Glossary",
    "15-geometry-layers.md": "Geometry Layers",
}


def check_titles_match_source() -> None:
    actual = {p.name for p in SOURCE_DIR.glob("[0-9][0-9]-*.md")}
    expected = set(TITLES)

    missing = actual - expected
    stale = expected - actual

    if missing or stale:
        problems = []
        if missing:
            problems.append(f"in docs/ but missing from TITLES: {sorted(missing)}")
        if stale:
            problems.append(f"in TITLES but missing from docs/: {sorted(stale)}")
        raise SystemExit(
            "generate_site_docs.py: TITLES is out of sync with docs/ ("
            + "; ".join(problems)
            + "). Update TITLES in scripts/generate_site_docs.py."
        )


def main() -> None:
    check_titles_match_source()

    if DEST_DIR.exists():
        shutil.rmtree(DEST_DIR)
    DEST_DIR.mkdir(parents=True)

    for filename, title in TITLES.items():
        source_path = SOURCE_DIR / filename
        nav_order = int(filename.split("-", 1)[0])
        original = source_path.read_text(encoding="utf-8")

        front_matter = (
            "---\n"
            f"title: {title}\n"
            f"nav_order: {nav_order}\n"
            "layout: default\n"
            "---\n\n"
        )

        dest_path = DEST_DIR / filename
        dest_path.write_text(front_matter + original, encoding="utf-8")
        print(f"generated {dest_path.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
