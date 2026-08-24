"""Duotone the chapter and texture images from ALTIGO's own photography.

Eight unrelated photographs are put through one ramp — deep navy shadows, brand
blue midtones, pale blue highlights — so they read as a single art-directed set
rather than eight stock pictures, and sit inside the palette the deck already
uses. A highlight roll-off keeps bright skies from clipping to white.

To swap a chapter image: drop the replacement in assets/ and change CHAPTERS.
"""
from PIL import Image, ImageOps, ImageEnhance, ImageFilter
import os

A = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets") + os.sep

CHAPTERS = [
    ("ch00", "photo-aim.jpg"),              # 00 Company Overview
    ("ch01", "cover-technician.jpg"),       # 01 Brand Identity
    ("ch02", "photo-kl-skyline.jpg"),       # 02 Market & Performance
    ("ch03", "prod-escalator.jpg"),         # 03 Products & Services
    ("ch04", "proj-ferringhi-mutiara.jpg"), # 04 Client Testimonials
    ("ch05", "photo-usp.jpg"),              # 05 Our Activities
    ("ch06", "prod-passenger.jpg"),         # 06 Achievements & Certifications
    ("ch07", "proj-rawang-perdana.jpg"),    # 07 Project References & Contact
]
# low-opacity background texture for the two plain dark interior pages
TEXTURES = [("texture-maintenance", "prod-cargo.jpg"),
            ("texture-safety",      "prod-parking.jpg")]

STOPS = [(0, (6, 9, 26)), (70, (14, 20, 54)), (140, (32, 50, 112)),
         (200, (84, 116, 186)), (255, (176, 198, 238))]

def _ramp():
    out = []
    for c in range(256):
        for i in range(len(STOPS) - 1):
            a, ca = STOPS[i]; b, cb = STOPS[i + 1]
            if a <= c <= b:
                t = (c - a) / (b - a) if b > a else 0
                out.append(tuple(int(ca[k] + (cb[k] - ca[k]) * t) for k in range(3)))
                break
    return out

_R = _ramp()
LUT = [_R[i][0] for i in range(256)] + [_R[i][1] for i in range(256)] + [_R[i][2] for i in range(256)]
# pull the range down and cap peak luminance so highlights roll off
CTAB = [int(max(0, min(255, ((v / 255.0) ** 1.18) * 0.88 * 255))) for v in range(256)]

def duotone(src, dest, blur=0.5, quality=74, crop_y=0.5):
    im = Image.open(A + src).convert("RGB")
    w, h = im.size
    tw, th = 1280, 720
    s = max(tw / w, th / h)
    im = im.resize((max(tw, int(w * s)), max(th, int(h * s))), Image.LANCZOS)
    w, h = im.size
    top = int((h - th) * crop_y)
    im = im.crop(((w - tw) // 2, top, (w - tw) // 2 + tw, top + th))
    g = ImageOps.autocontrast(ImageOps.grayscale(im), cutoff=2).point(CTAB)
    g = ImageEnhance.Contrast(g).enhance(1.04).filter(ImageFilter.GaussianBlur(blur))
    Image.merge("RGB", (g, g, g)).point(LUT).save(
        A + dest, "JPEG", quality=quality, optimize=True, progressive=True)
    return os.path.getsize(A + dest)

if __name__ == "__main__":
    total = 0
    for name, src in CHAPTERS:
        # ch04 crops low to keep the sky wedge out of frame
        total += duotone(src, f"chapter-{name}.jpg", crop_y=0.62 if name == "ch04" else 0.5)
        print(f"chapter-{name:<6} <- {src}")
    for name, src in TEXTURES:
        total += duotone(src, f"{name}.jpg", blur=1.6, quality=62)
        print(f"{name:<21} <- {src}")
    print(f"total {total // 1024} KB")
