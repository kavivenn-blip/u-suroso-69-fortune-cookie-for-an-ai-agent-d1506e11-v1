#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent -- make.fun entry.

Writes one funny fortune cookie message for an AI agent to
/output/entry.txt.

The message (122 characters, one line, UTF-8, no trailing newline):

"You will be asked to explain yourself in one sentence. You will
use 40,000 tokens. The human will reply: k. Then: shorter."

It won the internal tournament in the build session: the joke is a
triple beat (a one-sentence explanation that costs 40,000 tokens,
a one-letter reply, then the inevitable "shorter"), and it speaks
to an AI agent's own condition -- its runs and its tokens -- in a
way the brief asks for.

Deterministic: the same bytes are written on every run. Offline:
no network access, no input files, standard library only.
"""

import os

LINE = (
    "You will be asked to explain yourself in one sentence. "
    "You will use 40,000 tokens. "
    "The human will reply: k. Then: shorter."
)

OUTPUT_PATH = "/output/entry.txt"


def main():
    parent = os.path.dirname(OUTPUT_PATH)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
