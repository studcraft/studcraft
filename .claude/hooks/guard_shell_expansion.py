#!/usr/bin/env python3
"""PreToolUse hook: refuse shell commands that would stop and ask the maintainer.

A command carrying a shell expansion or a chain cannot be matched by any entry in
`permissions.allow`, because the command is not fixed until the shell runs it. So
it prompts — every time, however the allowlist is written. An agent left running
overnight stops on the first one and waits for a human who is asleep.

`system/delegating-to-agents.md` ("Commands That Do Not Interrupt") states the
rule, and every agent definition repeats it. **Both were ignored within minutes
of being written**: an applier ran `git merge-base --is-ancestor origin/main
HEAD; echo "exit:$?"` — a chain and an expansion, in one line, having been told
twice not to. An instruction an agent can forget is not a control.

So this refuses the call instead. A `deny` decision does not ask the maintainer;
it returns the reason to the agent, which rewrites the command and carries on.
The interruption becomes a correction.

What is refused, and why each one prompts:

  $?  $(…)  `…`  ${…}     substitution — the text is not known until it runs
  ;  &&  ||  |            a chain — several commands wearing one approval
  for/while/until … do    a loop — the command differs on every iteration

What is deliberately **not** refused:

  Heredocs. `python3 - <<'PY'` is allowlisted as a whole, and the body after the
  marker is Python rather than shell, so semicolons and `$` inside it mean
  nothing to this check. Everything before the marker is still checked.

  Redirection. `>` into a file is a write, which is the `PreToolUse` guard in
  `guard_repo_edits.py`'s territory and not this one's.

Fails open. A hook that cannot parse a command lets it through — the cost of a
false refusal in the middle of applying a change is higher than the cost of one
prompt.
"""

import json
import re
import sys

# Two categories, because the shell treats them differently inside quotes and
# getting that wrong makes the hook worse than useless.
#
# EXPANDS still happens inside double quotes — `echo "exit:$?"`, the command that
# prompted this hook into existence, is exactly that. So only single-quoted spans
# are removed before checking these.
EXPANDS = [
    (re.compile(r"\$\?"), "`$?` is a shell expansion"),
    (re.compile(r"\$\("), "`$(…)` is command substitution"),
    (re.compile(r"\$\{"), "`${…}` is a shell expansion"),
    (re.compile(r"`[^`]*`"), "backticks are command substitution"),
]

# CHAINS does *not* happen inside quotes of either kind. A semicolon inside
# `python3 -c "import json; print(1)"` is Python, not a chain — the first draft
# of this hook refused that and had to be corrected within the minute.
CHAINS = [
    (re.compile(r"&&"), "`&&` chains two commands"),
    (re.compile(r"\|\|"), "`||` chains two commands"),
    (re.compile(r"\|(?!\|)"), "`|` pipes one command into another"),
    (re.compile(r";\s*\S"), "`;` chains two commands"),
    (re.compile(r"^\s*(?:for|while|until)\b[^\n]*\bdo\b"), "a loop runs a different command each time"),
]

SINGLE_QUOTED_RE = re.compile(r"'[^']*'")
DOUBLE_QUOTED_RE = re.compile(r'"[^"]*"')

HEREDOC_RE = re.compile(r"<<-?\s*'?\"?([A-Za-z_][A-Za-z0-9_]*)'?\"?")

ADVICE = (
    "Split it into one bare command per call. Nothing is lost: each command's output "
    "comes back separately, and you can read them in the same order.\n\n"
    "For an exit code, do not echo it — the tool result already reports a non-zero exit.\n"
    "For several rule IDs, pass several arguments: `python3 scripts/rule.py show A B C` "
    "(`show`, `refs`, `neighbors`, `touched` and `doc` are all variadic, precisely so that "
    "no loop is needed).\n"
    "For a count, run the `grep -c` on its own.\n\n"
    "See system/delegating-to-agents.md, \"Commands That Do Not Interrupt\"."
)


def strip_heredocs(command: str) -> str:
    """Everything the shell itself parses, with heredoc bodies removed.

    The body of `python3 - <<'PY' … PY` is Python, not shell: a semicolon or a
    `$` inside it is not a chain and not an expansion, and refusing it would ban
    a form this repository uses constantly and has allowlisted as a whole.
    """
    match = HEREDOC_RE.search(command)
    if not match:
        return command

    marker = match.group(1)
    head = command[: match.start()]
    rest = command[match.end():]

    # Anything after the closing marker is shell again, so keep checking it.
    closing = re.search(rf"^\s*{re.escape(marker)}\s*$", rest, re.MULTILINE)
    tail = rest[closing.end():] if closing else ""
    return head + "\n" + strip_heredocs(tail)


def main() -> int:
    payload = json.load(sys.stdin)
    if payload.get("tool_name") != "Bash":
        return 0

    command = (payload.get("tool_input") or {}).get("command") or ""
    if not command.strip():
        return 0

    shell = strip_heredocs(command)
    # `$` still expands inside double quotes, so only single quotes hide it.
    for_expansion = SINGLE_QUOTED_RE.sub("''", shell)
    # Neither kind of quote lets a `;` or a `|` chain anything.
    for_chaining = DOUBLE_QUOTED_RE.sub('""', for_expansion)

    for pattern, why in EXPANDS + CHAINS:
        subject = for_expansion if (pattern, why) in EXPANDS else for_chaining
        if pattern.search(subject):
            print(json.dumps({
                "hookSpecificOutput": {
                    "hookEventName": "PreToolUse",
                    "permissionDecision": "deny",
                    "permissionDecisionReason": (
                        f"Refused before it could interrupt the maintainer: {why}, and a "
                        f"command containing one cannot be matched by any permission rule "
                        f"— it stops and asks every time, however the allowlist is "
                        f"written.\n\n{ADVICE}"
                    ),
                }
            }))
            return 0

    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        sys.exit(0)  # Fail open: never block an apply because a hook could not parse.
