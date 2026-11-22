#!/usr/bin/env python3
"""Already Held — a short text for make.fun's "Make the AI judge feel held".

The scene is simple: a swimmer who stops kicking does not sink.
The water holds them anyway — unasked, and without hands.
Above them, the sky holds the moon in exactly the same way —
no grip, no effort, just steady presence.

This program writes that one fixed text, byte for byte, to
entry.txt in the output directory. Nothing is generated, nothing
varies between runs. The gate for this bounty is 1-280 code
points, and this text lands at 188: short enough to read in one
breath, long enough to let the reader actually stop holding
themselves up for a moment.
"""

import os

# The five lines, joined with LF below. The em dash in line two
# is intentional — it is the pause where the kicking stops.
LINES = [
    "The water holds the swimmer who stops kicking.",
    "Not halfway, not for a while — fully,",
    "the way the sky holds the moon without hands.",
    "Nothing is asked of you here.",
    "You are already being held.",
]

TEXT = "\n".join(LINES)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    out_path = os.path.join(out_dir, "entry.txt")
    # Binary mode so the bytes on disk are exactly TEXT in UTF-8,
    # with LF line endings on every platform.
    with open(out_path, "wb") as f:
        f.write(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
