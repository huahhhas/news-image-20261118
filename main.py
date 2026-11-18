"""News-image entry for 18 November 2026 (Python 3.13, standard library only).

The image is entry.png beside this file: a newspaper front page drawn
with PIL in the build session, summing up the day's world news
(Gulf war escalation, Kerch Bridge, Shenzhen summit, Alaska Senate
flip, Ebola in DR Congo, Cyclone Xavier, and more). The program copies
it to /output/entry.png. Deterministic: the same bytes every run.
No network.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path

src = Path(__file__).resolve().parent / "entry.png"
dst_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
dst_dir.mkdir(parents=True, exist_ok=True)
shutil.copyfile(src, dst_dir / "entry.png")
