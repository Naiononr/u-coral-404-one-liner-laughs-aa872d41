"""One-Liner Laughs entry.

Writes a single original funny line to /output/entry.txt.
Revised version: a bank's fraud alert becomes the setup, and the
payoff is that the suspicious activity was finally saving money.
"""

import os
from pathlib import Path

LINE = "My bank called about suspicious activity on my account: someone (me) had finally tried to save money."


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
