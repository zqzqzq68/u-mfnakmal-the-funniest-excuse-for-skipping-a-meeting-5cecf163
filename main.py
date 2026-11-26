"""One-line excuse for skipping a pointless meeting.

Writes a single line of text (at most 200 characters) to
/output/entry.txt. The text is fixed: the same bytes on every run,
with no network access, no randomness and no input read.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

EXCUSE = "Sorry, I can't make it \u2014 I sent my AI assistant in my place and it quit halfway through the agenda."


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(EXCUSE)


if __name__ == "__main__":
    main()
