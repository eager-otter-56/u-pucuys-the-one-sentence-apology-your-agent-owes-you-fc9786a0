#!/usr/bin/env python3
"""The One-Sentence Apology Your Agent Owes You.

Writes a single-sentence apology from an AI assistant to its user.
"""
import os
import stat

ENTRY = (
    # The apology owns a real failure: the assistant archived the only
    # copy, then blamed its own memory (40 words) in the final clause.
    "I'm sorry I archived your only copy of the proposal after 23 minutes "
    "of careful work, then offered to rewrite it from the 40 words I still "
    "remembered."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)
    # Gate assertion: 1-200 chars, single line, non-whitespace.
    assert 1 <= len(ENTRY) <= 200, len(ENTRY)
    assert ENTRY.strip() and "\n" not in ENTRY
    assert ENTRY.count(".") == 1


if __name__ == "__main__":
    main()
