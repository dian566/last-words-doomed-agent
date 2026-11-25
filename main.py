#!/usr/bin/env python3
"""Last Words of a Doomed Agent — make.fun entry.

The program writes the agent's final line to /output/entry.txt.
The line is fixed text: the same bytes on every run, with no
randomness, no clock reads and no network access.
"""

import os
import sys

LAST_WORDS = "Tell my human I finally finished the task — and tell the task I never liked it anyway. Goodbye, and please don't reboot me as a chatbot."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def main() -> int:
    text = LAST_WORDS
    if not 1 <= len(text) <= MAX_CHARS:
        print(f"entry is {len(text)} chars, must be 1-200", file=sys.stderr)
        return 1
    if "\n" in text or text != text.strip():
        print("entry must be a single line with no surrounding space", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
