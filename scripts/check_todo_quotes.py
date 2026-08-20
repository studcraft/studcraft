#!/usr/bin/env python3
"""Every blockquote in TODO.md must still appear verbatim in the document it cites.

`TODO.md` registers the gaps the ruleset declares **in its own text**, and says
of itself that every entry "cites the rule or section that declares the gap and
quotes it". That claim is what makes the file worth keeping: it is derivable
from `docs/`, so a reader can trust it without re-reading the ruleset, and an
entry has to disappear when the rule closes the gap.

The claim also rots silently. When `Deployment Area` became `Deployment Volume`,
two blockquotes went on quoting a sentence `docs/` no longer contained, and
nothing noticed — the file is not referenced by any gate and reads perfectly
well while being wrong.

This is the deterministic half of that problem, and only that half:

  - It answers "does TODO.md misquote the ruleset?" — pure substring matching,
    no judgement, no false positives.
  - It does **not** answer "is TODO.md complete?". Sweeping `docs/` for
    `future` / `not yet defined` finds passages that declare no gap at all
    (`WPN-016`'s "allowing future expansion" is a closing remark that
    declares nothing). Telling those apart means
    reading the sentence, which belongs to `ruleset-auditor`, not to a regex.

How an entry is matched to its source: the last `docs/*.md` path named on a
non-quoted line before the blockquote. That covers all three shapes the file
uses — a rule ID with a path, a path with no rule ID, and a rule ID mid-sentence
— without parsing the sentence itself. Paths named *inside* a quote are ignored,
since several quoted rules cite other documents.

Exit code 0 when every quote matches, 1 otherwise. Each failure names the
TODO.md line the quote starts on, the document it claims to quote, and the first
quoted line missing from it.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
TODO = REPO_ROOT / "TODO.md"

DOC_PATH_RE = re.compile(r"`(docs/[\w.-]+\.md)`")


def strip_quote(line: str) -> str:
    """`> text` -> `text`, and a bare `>` -> the empty line it stands for."""
    body = line[1:]
    return body[1:] if body.startswith(" ") else body


def collect_quotes(text: str) -> list[tuple[int, str | None, str]]:
    """Every blockquote in TODO.md, as (first line number, source path, body)."""
    quotes: list[tuple[int, str | None, str]] = []
    source: str | None = None
    block: list[str] = []
    start = 0

    def flush() -> None:
        nonlocal block
        if block:
            body = "\n".join(block).strip("\n")
            if body:
                quotes.append((start, source, body))
            block = []

    for number, line in enumerate(text.splitlines(), start=1):
        if line.startswith(">"):
            if not block:
                start = number
            block.append(strip_quote(line))
            continue

        flush()
        found = DOC_PATH_RE.findall(line)
        if found:
            source = found[-1]

    flush()
    return quotes


def main() -> int:
    if not TODO.is_file():
        print(f"{TODO.name} does not exist.")
        return 1

    quotes = collect_quotes(TODO.read_text(encoding="utf-8"))
    if not quotes:
        print("TODO.md contains no blockquotes to verify.")
        return 1

    cache: dict[str, str | None] = {}
    failures: list[str] = []

    for line_number, source, body in quotes:
        if source is None:
            failures.append(
                f"TODO.md:{line_number} quotes something, but no docs/*.md path is "
                f"named before it. Every entry cites the document it quotes."
            )
            continue

        if source not in cache:
            path = REPO_ROOT / source
            cache[source] = path.read_text(encoding="utf-8") if path.is_file() else None

        document = cache[source]
        if document is None:
            failures.append(f"TODO.md:{line_number} cites {source}, which does not exist.")
            continue

        if body in document:
            continue

        missing = next(
            (ln for ln in body.splitlines() if ln.strip() and ln not in document),
            None,
        )
        detail = f" First line not found: {missing!r}." if missing else (
            " Every line appears on its own; the surrounding formatting has moved."
        )
        failures.append(f"TODO.md:{line_number} no longer matches {source}.{detail}")

    if failures:
        for failure in failures:
            print(failure)
        print(
            f"{len(failures)} of {len(quotes)} TODO.md quote(s) do not match the "
            f"ruleset. Re-read the rule and update the entry, or drop it if the "
            f"gap has closed."
        )
        return 1

    print(f"All {len(quotes)} TODO.md quote(s) match the document they cite.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
