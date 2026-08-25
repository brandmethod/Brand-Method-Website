"""Normalise the two leadership cut-outs so they read as one photograph.

They were shot separately, so matching them by raw pixel height makes one
person look smaller than the other. Head width is the reliable cue for
camera distance, so both are scaled to the same head width, their heads are
aligned to the same line, and both are cropped at the same depth — which is
how a real two-shot reads.
"""
from PIL import Image
import os

A = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets") + os.sep
SRC = [("leader-founder.png", "portrait-founder.png"),
       ("leader-executive.png", "portrait-executive.png")]

HEAD   = 400    # target head width, px
CANVAS = (1080, 1180)   # shared frame; both figures cropped at the same depth

def head_width(im, box):
    l, t, r, b = box
    a = im.getchannel("A")
    best = 0
    for y in range(t, t + int((b - t) * 0.12), 3):
        xs = [x for x in range(l, r, 3) if a.getpixel((x, y)) > 24]
        if xs:
            best = max(best, xs[-1] - xs[0] + 3)
    return best

for dest, src in SRC:
    im = Image.open(A + src).convert("RGBA")
    box = im.getchannel("A").point(lambda v: 255 if v > 24 else 0).getbbox()
    s = HEAD / head_width(im, box)
    fig = im.crop(box)
    fig = fig.resize((round(fig.width * s), round(fig.height * s)), Image.LANCZOS)
    out = Image.new("RGBA", CANVAS, (0, 0, 0, 0))
    out.paste(fig, ((CANVAS[0] - fig.width) // 2, 0), fig)   # heads on the same line
    out.save(A + dest, "PNG", optimize=True)
    print(f"{dest:<24} scale {s:.3f}  figure {fig.width}x{fig.height}  {os.path.getsize(A+dest)//1024} KB")
