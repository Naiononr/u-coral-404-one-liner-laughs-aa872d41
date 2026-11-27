"""One-Liner Laughs entry.

Writes a single original funny line to /output/entry.txt.
Draft version.
"""

import os
from pathlib import Path

LINE = "My therapist said to embrace my mistakes, so I hugged my student loan statement and it charged me interest for the contact."


def main() -> None:
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    tmp = out_dir / ".entry.txt.tmp"
    tmp.write_text(LINE, encoding="utf-8")
    os.chmod(tmp, 0o644)
    os.replace(tmp, target)


if __name__ == "__main__":
    main()
