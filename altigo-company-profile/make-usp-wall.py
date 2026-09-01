"""Build the wall strip that sits behind the Brand USP photograph.

The photograph is placed at its own aspect in the bottom corner, which leaves
a band above it. This takes the photograph's own top row and saves it one
pixel tall; stretched vertically behind the photo it continues each wall
panel upward in exactly the colour sitting next to it.

Alpha is carried through unchanged, so the columns where the cut-out is
transparent stay transparent all the way up and the page shows through, the
same way it does beside the escalator.
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
    acc, n, alpha = [0, 0, 0], 0, 0
    for y in range(BAND):
        r, g, b, a = px[x, y]
        alpha += a
        if a > 200:
            acc[0] += r; acc[1] += g; acc[2] += b; n += 1
    # no opaque sample means there is no wall in this column, so it stays clear
    row.append((acc[0] // n, acc[1] // n, acc[2] // n, alpha // BAND) if n
               else (0, 0, 0, 0))

# the cut-out leaves a hairline of matting on the right border. Stretched to
# the width of the page that becomes a visible pale sliver, so square it off
# against the wall beside it. Only a hairline: anything wider is real.
edge = 0
while edge < W and row[-1 - edge][3] < 255:
    edge += 1
if edge and edge <= W // 200:
    for i in range(1, edge + 1):
        row[-i] = row[-edge - 1]

strip = Image.new("RGBA", (W, 1))
strip.putdata(row)
strip.save(A + "photo-usp-wall.png", "PNG", optimize=True)
opaque = [i for i, c in enumerate(row) if c[3] > 200]
print("photo-usp-wall.png", strip.size, os.path.getsize(A + "photo-usp-wall.png"), "bytes")
print("wall begins at column", opaque[0], "of", W, "->", round(100 * opaque[0] / W, 1), "%")
print("first wall colour", row[opaque[0]][:3], "| mid", row[W // 2][:3], "| right", row[-1][:3])
