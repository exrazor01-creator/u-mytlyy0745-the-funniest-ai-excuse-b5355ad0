"""Write the funniest one-line excuse an AI agent gives after failing a task.

The line is spoken in the agent's own voice: it did not fail alone, it
delegated the work away, and the delegation looped back on itself. The
joke lands in the last clause - three agents holding a standup about a
task none of them did, with "none of us" echoing "the three of us" for
the punch. No hallucination, reboot or training-data joke, no
explanation of the joke, just one concrete little scene.

Gate guard: the entry must be UTF-8 text of 1 to 200 characters, a
single line, and not only white space - the same gate the sealed
scorer applies to /output/entry.txt. Refuse to write anything that
fails it, so a bad line can never reach the judge.
"""

from pathlib import Path

ENTRY = (
    "I delegated your task to a sub-agent, who delegated it to another "
    "sub-agent, and now the three of us are in a standup about why "
    "none of us did it."
)

MIN_CHARS = 1
MAX_CHARS = 200


def validate(text: str) -> None:
    """Raise SystemExit unless the text passes the scorer's gate."""
    if not isinstance(text, str):
        raise SystemExit("entry is not text")
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise SystemExit(
            f"entry is {len(text)} characters, must be {MIN_CHARS}-{MAX_CHARS}"
        )
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if any(ord(ch) < 32 and ch not in ("\n", "\r") for ch in text):
        raise SystemExit("entry must not contain control characters")
    if text != text.strip():
        raise SystemExit("entry must not have leading or trailing space")
    if not text.strip():
        raise SystemExit("entry must not be only white space")
    text.encode("utf-8")  # raises if the text is not valid UTF-8


def main() -> None:
    validate(ENTRY)
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
