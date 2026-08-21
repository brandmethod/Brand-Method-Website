#!/usr/bin/env python3
"""
Bake the duotone photographic bands.

Every band in the book is the same idea: real Altigo installation photography,
stretched to the full luminance range and then mapped through one Altigo ramp —
near-black navy in the shadows, brand blue through the midtones, a light blue in
the highlights. Baking it (rather than tinting in CSS) keeps the bands identical
in the browser and in both PDF exports, and keeps them sharp when Chrome
rasterises the page.

Each band tiles a different set of photographs, in a different order, cropped to
a different part of the frame, so no two bands in the book read as the same
picture. Tile widths are kept at or below the source width — the installation
photographs are 449 px wide, so a band is four or five tiles, never two or three.

    python3 tools_duotone.py
"""

import pathlib
from PIL import Image, ImageOps

HERE = pathlib.Path(__file__).resolve().parent
ASSETS = HERE / "assets"

# shadow → midtone → highlight, sampled from the brand palette
RAMP = [(3, 11, 34), (8, 46, 130), (116, 168, 246)]


def lut() -> list[int]:
    """256-entry RGB lookup table through the three ramp stops."""
    out = [[], [], []]
    for i in range(256):
        t = i / 255 * 2
        k = 0 if t < 1 else 1
        f = t - k
        for c in range(3):
            a, b = RAMP[k][c], RAMP[k + 1][c]
            out[c].append(round(a + (b - a) * f))
    return out[0] + out[1] + out[2]


LUT = lut()


def crop_to(im: Image.Image, ratio: float, anchor: float) -> Image.Image:
    """Crop to `ratio` (w/h), keeping `anchor` (0 = top/left, 1 = bottom/right)."""
    w, h = im.size
    if w / h > ratio:                       # too wide — trim the sides
        nw = round(h * ratio)
        x = round((w - nw) * anchor)
        return im.crop((x, 0, x + nw, h))
    nh = round(w / ratio)                   # too tall — trim top and bottom
    y = round((h - nh) * anchor)
    return im.crop((0, y, w, y + nh))


def band(out: str, size: tuple[int, int], sources: list[str], anchor: float) -> None:
    W, H = size
    cell = W // len(sources)
    strip = Image.new("RGB", (W, H))
    for i, name in enumerate(sources):
        im = Image.open(ASSETS / name).convert("RGB")
        im = crop_to(im, cell / H, anchor).resize((cell, H), Image.LANCZOS)
        strip.paste(im, (i * cell, 0))
    strip = ImageOps.autocontrast(strip.convert("L"), cutoff=(1, 3)).convert("RGB")
    strip.point(LUT).save(ASSETS / out, quality=88, optimize=True, subsampling=1)
    print(f"  {out:24} {W}×{H}  {len(sources)}-up  {(ASSETS / out).stat().st_size / 1024:5.0f} KB")


HALLS = ["layout-1.jpg", "layout-2.jpg", "layout-3.jpg", "layout-4.jpg", "layout-5.jpg"]


def main() -> int:
    # four foot bands and one half page — different tiling, order and crop each time
    band("duo-band-a.jpg", (1920, 268), HALLS, 0.14)                      # 02 contents
    band("duo-band-b.jpg", (1920, 300), ["layout-5.jpg", "layout-3.jpg",
                                         "layout-1.jpg", "layout-4.jpg"], 0.80)  # 04 control
    band("duo-band-c.jpg", (1920, 320), ["layout-2.jpg", "layout-4.jpg", "layout-1.jpg",
                                         "layout-5.jpg", "layout-3.jpg"], 0.50)  # 07 parts
    band("duo-band-d.jpg", (1920, 244), ["layout-4.jpg", "layout-2.jpg",
                                         "layout-5.jpg", "layout-1.jpg"], 0.28)  # 12 civil
    band("duo-half-rise.jpg", (960, 1080), ["intro-photo.jpg"], 0.5)      # 10 divider
    # the truss is a white-ground product shot; through the ramp its ground
    # becomes light blue, so the page carries colour instead of more white
    band("duo-truss.jpg", (592, 868), ["truss.jpg"], 0.5)                 # 09 devices
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
