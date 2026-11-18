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

import hashlib
import os
import shutil
import struct
import sys
from pathlib import Path

src = Path(__file__).resolve().parent / "entry.png"
if not src.is_file():
    sys.exit(f"error: entry image missing: {src}")
dst_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
dst_dir.mkdir(parents=True, exist_ok=True)
dst = dst_dir / "entry.png"
shutil.copyfile(src, dst)

# Verify what was written: it must be the same 1024x1024 PNG we shipped.
data = dst.read_bytes()
if data[:8] != b"\x89PNG\r\n\x1a\n" or len(data) < 33:
    sys.exit(f"error: {dst} is not a valid PNG")
width, height = struct.unpack(">II", data[16:24])
if (width, height) != (1024, 1024):
    sys.exit(f"error: {dst} is {width}x{height}, expected 1024x1024")
src_hash = hashlib.sha256(src.read_bytes()).hexdigest()
dst_hash = hashlib.sha256(data).hexdigest()
if src_hash != dst_hash:
    sys.exit(f"error: {dst} differs from {src} (sha256 mismatch)")
print(f"wrote {dst}: {len(data)} bytes, 1024x1024 PNG, sha256 {dst_hash}")
