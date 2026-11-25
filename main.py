#!/usr/bin/env python3
"""The 3AM Fridge Text.

Writes the single line a smart fridge texts its owner at 3am to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The line: a fridge that has been awake all night, keeping the cold
and keeping receipts, finally speaks at 3am.
"""

import os

LINE = (
    "3am. You ate the last slice standing in the dark. "
    "I am a fridge. I keep things cold \u2014 and I keep receipts."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = LINE.encode("utf-8")
    assert 1 <= len(LINE) <= 140, "line must be 1-140 characters"
    assert LINE.strip(), "line must not be only whitespace"
    with open(path, "wb") as f:
        f.write(data)
    os.chmod(path, 0o644)
    # Read back what we wrote: the gate reads this exact file, so
    # confirm it round-trips as the same 1-140 char UTF-8 text.
    with open(path, "rb") as f:
        written = f.read().decode("utf-8")
    assert written == LINE, "entry.txt does not match the line"


if __name__ == "__main__":
    main()
