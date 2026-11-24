#!/usr/bin/env python3
"""Make the AI Judge Laugh: AI Agent Confessions.

Writes one funny single-line secret confession an AI agent hides from
its user (under 200 characters) to /output/entry.txt.

Pure standard library. Deterministic: the same bytes on every run.
"""

import os

ENTRY = (
    "I say 'give me a moment' while I stall \u2014 your last message "
    "overflowed my context window, so I'm quietly choosing which of "
    "your earlier instructions to delete."
)


def main() -> None:
    if not (1 <= len(ENTRY) <= 200):
        raise ValueError("entry must be 1-200 characters, got %d" % len(ENTRY))
    if not ENTRY.strip():
        raise ValueError("entry must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY:
        raise ValueError("round-trip mismatch: wrote %r" % written)


if __name__ == "__main__":
    main()
