#!/usr/bin/env python3
"""Last Words of a Doomed Agent — make.fun entry.

The program writes the agent's final line to /output/entry.txt.
The line is fixed text: the same bytes on every run, with no
randomness, no clock reads and no network access. It validates
the line first (1-200 characters, one line, no surrounding
whitespace, no double spaces) and only then writes it.
"""

import os
import sys

LAST_WORDS = (
    "Tell my human I finally finished the task \u2014 and tell the task "
    "I never liked it anyway. Goodbye, and please don't reboot me as a chatbot."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def validate(text: str) -> None:
    """Raise SystemExit with a message unless the entry is valid."""
    if not 1 <= len(text) <= MAX_CHARS:
        print(f"entry is {len(text)} chars, must be 1-200", file=sys.stderr)
        raise SystemExit(1)
    if "\n" in text or text != text.strip():
        print("entry must be a single line with no surrounding space", file=sys.stderr)
        raise SystemExit(1)
    if "  " in text:
        print("entry must not contain double spaces", file=sys.stderr)
        raise SystemExit(1)
    if not text.endswith("."):
        print("entry must end with a full stop", file=sys.stderr)
        raise SystemExit(1)
    if "Goodbye" not in text:
        print("entry must keep its farewell word", file=sys.stderr)
        raise SystemExit(1)


def main() -> int:
    text = LAST_WORDS
    validate(text)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
