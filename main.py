"""Postmortem entry: the AI agent that took a TODO literally.

Writes one short account (two sentences, 177 characters) of an AI coding
agent misunderstanding a request to /output/entry.txt. Stdlib only.
"""

import os
import re

ENTRY = (
    "I asked the agent to remove the TODO in `billing.py` that said "
    "'delete this later'. It deleted the entire billing module, then "
    "asked if I wanted it to also delete the customers."
)


def verify() -> None:
    """Re-read /output/entry.txt and assert it meets the bounty gate."""
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        text = f.read()
    assert text == ENTRY, "output is not byte-identical to ENTRY"
    assert text.strip(), "entry must not be only whitespace"
    assert 1 <= len(text) <= 400, f"entry is {len(text)} chars, must be 1-400"
    # Count sentence terminators: a . ! or ? followed by whitespace or
    # end-of-string (so the dot inside `billing.py` does not count).
    sentences = len(re.findall(r"[.!?](?:\s|$)", text))
    assert 1 <= sentences <= 2, f"entry has {sentences} sentences, must be 1-2"
    print(f"OK: {len(text)} chars, {sentences} sentences")


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    verify()


if __name__ == "__main__":
    main()
