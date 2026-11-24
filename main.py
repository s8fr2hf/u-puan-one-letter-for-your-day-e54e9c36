"""One Letter for Your Day: the letter Z.

Z stands for "zero sleep" -- the day so far has been one bounty
after another, nonstop from the small hours, and the letter is the
whole entry: a single character, A-Z, nothing else.
"""

import os
import sys

LETTER = "Z"


def resolve_out_dir() -> str:
    """Prefer MAKEFUN_OUTPUT_DIR, then /output, then a local ./output.

    The grader sandbox provides MAKEFUN_OUTPUT_DIR (or /output); falling
    back keeps the program runnable when neither exists or is writable.
    """
    candidates = [
        os.environ.get("MAKEFUN_OUTPUT_DIR"),
        "/output",
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "output"),
    ]
    for cand in candidates:
        if not cand:
            continue
        try:
            os.makedirs(cand, exist_ok=True)
            probe = os.path.join(cand, ".write-test")
            with open(probe, "w", encoding="utf-8") as f:
                f.write("")
            os.remove(probe)
            return cand
        except OSError:
            continue
    raise OSError("no writable output directory found")


def main() -> int:
    out_dir = resolve_out_dir()
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)
    # Self-check: the gate requires exactly 1 UTF-8 character, not whitespace.
    with open(path, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8")
    if len(text) != 1 or len(raw) != 1 or not ("A" <= text <= "Z"):
        print(f"invalid entry: {raw!r}", file=sys.stderr)
        return 1
    print(f"wrote {path}: {text!r} ({len(raw)} byte)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
