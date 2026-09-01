"""Build the wall strip that sits behind the Brand USP photograph.

The photograph is placed at its own aspect in the bottom corner, which leaves
white above it, and its cut-out is transparent to the left of the escalator.
Rather than pick a flat blue, this takes the photograph's own top row, fills
the transparent part of that row from its nearest opaque neighbour, and saves
it one pixel tall. Stretched vertically behind the photo it continues each
wall panel upward in exactly the colour sitting next to it.
"""
from PIL import Image
import os

A = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets") + os.sep
src = Image.open(A + "photo-usp.webp").convert("RGBA")
W, H = src.size
px = src.load()

BAND = 6                      # average a few rows so JPEG noise doesn't band
row = []
for x in range(W):
    acc, n = [0, 0, 0], 0
    for y in range(BAND):
        r, g, b, a = px[x, y]
        if a > 200:
            acc[0] += r; acc[1] += g; acc[2] += b; n += 1
    row.append(tuple(c // n for c in acc) if n else None)

# carry the nearest opaque colour across the transparent part of the row
last = next(c for c in row if c)
for i, c in enumerate(row):
    if c is None:
        row[i] = last
    else:
        last = c

strip = Image.new("RGB", (W, 1))
strip.putdata(row)
strip.save(A + "photo-usp-wall.png", "PNG", optimize=True)
print("photo-usp-wall.png", strip.size, os.path.getsize(A + "photo-usp-wall.png"), "bytes")
print("left edge", row[0], "| mid", row[W // 2], "| right", row[-1])
