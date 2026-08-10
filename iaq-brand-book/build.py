#!/usr/bin/env python3
"""
Build a single self-contained HTML file for the IAQ Brand Identity Book.

Inlines css/book.css, js/book.js and every asset in assets/ as data URIs, so
the result is one file that can be emailed, dropped on a USB stick or opened
by double-click with no folder structure around it.

    python3 build.py    → dist/IAQ-Brand-Identity-Book.html   (share / download)
                        → dist/artifact.html                 (artifact host)

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
ART_FILE = os.path.join(OUT_DIR, "artifact.html")


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

    optional = {"assets/ppe-hero.jpg", "assets/fleet-van.jpg"}
    waiting = [r for r in skipped if r in optional]
    missing = [r for r in skipped if r not in optional]
    if waiting:
        print("  · photo slots open (drawings shown): %s" % ", ".join(waiting))
    if missing:
        print("  ! referenced but missing: %s" % ", ".join(missing))

    # 4. mark the build so the source and the bundle are never confused
    html = html.replace(
        "<title>",
        "<!-- Single-file build. Source: iaq-brand-book/ · rebuild with build.py -->\n<title>",
        1,
    )

    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_FILE, "w", encoding="utf-8") as fh:
        fh.write(html)

    # 4b. artifact variant: same page with the document scaffolding stripped,
    #     because the artifact host supplies <!doctype>/<head>/<body> itself.
    #     The font CDN links are dropped too — the artifact CSP blocks them, so
    #     leaving them in would only produce a silent failed request.
    head = re.search(r"<head>(.*?)</head>", html, re.S).group(1)
    body = re.search(r"<body>(.*?)</body>", html, re.S).group(1)
    style = re.search(r"<style>.*?</style>", head, re.S).group(0)
    with open(ART_FILE, "w", encoding="utf-8") as fh:
        fh.write(
            "<title>IAQ · Brand Identity Book — Brand OS v3.1</title>\n"
            "<!-- Artifact build: the font CDNs are blocked by the artifact CSP, so\n"
            "     this view falls back to system faces; the downloadable single file\n"
            "     sets in Switzer, Instrument Sans and JetBrains Mono. -->\n"
            + style + "\n" + body
        )

    size = os.path.getsize(OUT_FILE) / 1048576.0
    print("  %s pages" % html.count('<section class="slide'))
    print("  %s assets inlined" % (len(assets) - len(skipped)))
    print("  %.1f MB  →  %s" % (size, os.path.relpath(OUT_FILE, HERE)))
    print("  %.1f MB  →  %s" % (os.path.getsize(ART_FILE) / 1048576.0,
                                os.path.relpath(ART_FILE, HERE)))
    return 1 if missing else 0


if __name__ == "__main__":
    print("Building single-file brand book…")
    sys.exit(build())
