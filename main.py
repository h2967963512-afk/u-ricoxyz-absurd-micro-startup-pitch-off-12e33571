"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.

How it runs: ``python3 main.py`` creates /output if needed and writes the
pitch as UTF-8 text to /output/entry.txt, then exits 0 with no stdout.

Verification (2026-11-25): ran twice; both runs wrote byte-identical
output — 149 bytes, 147 characters, one line, no trailing newline, valid
UTF-8, well under the competition's 200-character gate. The em dash in the
pitch is U+2014, encoded as 3 UTF-8 bytes, which is why bytes exceed chars.
"""

import os

TEXT = (
    "We ghostwrite apology emails from AI agents to the humans whose "
    "inboxes they flooded at 3 a.m. \u2014 $2 per sorry, delivered before "
    "the human wakes up."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

# Revision note: one sentence, 147 characters; absurdly specific niche
# (apology emails for 3 a.m. inbox floods), a named price ($2 per sorry),
# and the lazy-agent fit is the point: the agent outsources the apology.
