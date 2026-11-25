#!/usr/bin/env python3
"""The Agent's Uh-Oh: write the agent's one-word confession to /output/entry.txt.

The word is "glitch" -- the sound a machine makes when it catches itself
losing the thread mid-task. One word, nothing attached.
"""

import os

WORD = "glitch"


def main() -> None:
    # Validation gate: the entry must be 1-99 chars of real text, never blank.
    if not WORD or not WORD.strip():
        raise ValueError("entry word must not be blank")
    if len(WORD) > 99:
        raise ValueError("entry word must be at most 99 characters")
    if len(WORD.split()) != 1:
        raise ValueError("entry must be exactly one word")

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
