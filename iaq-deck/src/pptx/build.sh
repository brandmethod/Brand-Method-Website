#!/bin/sh
# one command so the SVG rasterisation is never skipped: it writes the PNG paths
# back into slides.json, and emitting without it silently drops every icon
set -e
cd "$(dirname "$0")"
python3 extract.py
python3 rasterize.py
python3 emit.py
