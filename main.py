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

Verified 2026-11-24T12:43Z: two runs from clean copies produce
byte-identical output, sha256
0ab20ecd535eeb1091cd5951e6f391abf0959029506b37e1b53154d7cccb9855,
file mode 0644, 122 bytes, 122 code points, one line, no trailing
newline, no BOM. A third run with the network namespace disabled
(unshare -rn) writes the same sha256.
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
