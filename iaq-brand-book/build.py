#!/usr/bin/env python3
"""
Build a single self-contained HTML file for the IAQ Brand Identity Book.

Inlines css/book.css, js/book.js and every asset in assets/ as data URIs, so
the result is one file that can be emailed, dropped on a USB stick or opened
by double-click with no folder structure around it.

    python3 build.py                → dist/IAQ-Brand-Identity-Book.html

Everything still works in the single file: page turns, the index overlay,
section rail, deep links and print/PDF export. Fonts still come from their
CDNs, so the machine opening it needs a connection to set in the brand faces
(see css/fonts-local.css to make those local too).
"""

import base64
import mimetypes
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(HERE, "dist")
OUT_FILE = os.path.join(OUT_DIR, "IAQ-Brand-Identity-Book.html")


def read(path):
    with open(os.path.join(HERE, path), "r", encoding="utf-8") as fh:
        return fh.read()


def data_uri(rel_path):
    full = os.path.join(HERE, rel_path)
    mime = mimetypes.guess_type(full)[0] or "application/octet-stream"
    with open(full, "rb") as fh:
        return "data:%s;base64,%s" % (mime, base64.b64encode(fh.read()).decode("ascii"))


def build():
    html = read("index.html")
    css = read("css/book.css")
    js = read("js/book.js")

    # 1. inline the stylesheet
    html = html.replace(
        '<link rel="stylesheet" href="css/book.css">',
        "<style>\n%s\n</style>" % css,
    )

    # 2. inline the deck engine
    html = html.replace(
        '<script src="js/book.js"></script>',
        "<script>\n%s\n</script>" % js,
    )

    # 3. inline every asset reference (src="assets/..." and href="assets/...")
    assets = sorted(set(re.findall(r'assets/[A-Za-z0-9._-]+', html)))
    skipped = []
    for rel in assets:
        if not os.path.isfile(os.path.join(HERE, rel)):
            skipped.append(rel)
            continue
        html = html.replace(rel, data_uri(rel))

    if skipped:
        print("  ! referenced but missing: %s" % ", ".join(skipped))

    # 4. mark the build so the source and the bundle are never confused
    html = html.replace(
        "<title>",
        "<!-- Single-file build. Source: iaq-brand-book/ · rebuild with build.py -->\n<title>",
        1,
    )

    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_FILE, "w", encoding="utf-8") as fh:
        fh.write(html)

    size = os.path.getsize(OUT_FILE) / 1048576.0
    print("  %s pages" % html.count('<section class="slide'))
    print("  %s assets inlined" % (len(assets) - len(skipped)))
    print("  %.1f MB  →  %s" % (size, os.path.relpath(OUT_FILE, HERE)))
    return 1 if skipped else 0


if __name__ == "__main__":
    print("Building single-file brand book…")
    sys.exit(build())
