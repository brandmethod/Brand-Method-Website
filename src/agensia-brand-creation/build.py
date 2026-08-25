#!/usr/bin/env python3
"""Assemble Agensia_Brand_Creation.html from the slide fragments in this folder.

Fonts and the Agensia symbol path are lifted from the confirmed Brand Book V3.0
artwork, so the deck reproduces the identity rather than approximating it.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
ASSETS = os.path.join(HERE, "assets")
OUT = os.path.join(ROOT, "Agensia_Brand_Creation.html")

# Fragments in deck order. 00-head and 99-tail wrap the slides.
ORDER = [
    "00-head.html",
    "01-cover.html",
    "02-guide-name.html",
    "03-guide-logo-a.html",
    "04-guide-logo-b.html",
    "05-guide-logo-c.html",
    "06-guide-stylescape.html",
    "07-foundation.html",
    "08-reference.html",
    "09-stylescape.html",
    "10-ideation.html",
    "11-system.html",
    "12-mockups.html",
    "99-tail.html",
]

# Characters the subsetted brand fonts do not carry. Using them would silently
# fall back to a system face mid-sentence, so the build refuses them.
FORBIDDEN = {
    "—": "em dash (use a middle dot or a comma)",
    "–": "en dash (use a middle dot or a comma)",
    "−": "minus sign",
    "‑": "non-breaking hyphen",
}


def read(name):
    with open(os.path.join(HERE, name), encoding="utf-8") as fh:
        return fh.read()


def main():
    fonts = open(os.path.join(ASSETS, "fonts.css"), encoding="utf-8").read().strip()
    sympath = open(os.path.join(ASSETS, "symbol-path.txt"), encoding="utf-8").read().strip()

    missing = [n for n in ORDER if not os.path.exists(os.path.join(HERE, n))]
    if missing:
        sys.exit("missing fragments: " + ", ".join(missing))

    doc = "\n".join(read(n) for n in ORDER)
    doc = doc.replace("/*{{FONTS}}*/", fonts).replace("{{SYMPATH}}", sympath)

    bad = []
    for ch, why in FORBIDDEN.items():
        if ch in doc:
            line = doc[: doc.index(ch)].count("\n") + 1
            bad.append("line %d: %s %s" % (line, repr(ch), why))
    # Anything outside the subsetted fonts' coverage would fall back mid-sentence.
    for i, ch in enumerate(doc):
        if ord(ch) > 0x2192 and ch not in "\u2500\u2502\u2514\u251c":
            line = doc[:i].count("\n") + 1
            bad.append("line %d: %s outside brand font coverage" % (line, repr(ch)))
            break
    if bad:
        sys.exit("unsupported glyphs in output:\n  " + "\n  ".join(bad))

    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write(doc)

    slides = doc.count('<div class="slide">')
    print("wrote %s" % OUT)
    print("  %d slides, %.2f MB" % (slides, len(doc.encode("utf-8")) / 1048576))

    # Page numbers must run in document order and match the slide count.
    nums = [int(m) for m in re.findall(r'class="pnum">(\d+)<', doc)]
    out_of_order = [n for a, n in zip(nums, nums[1:]) if n <= a]
    if out_of_order:
        print("  WARNING page numbers out of order at: %s" % out_of_order)


if __name__ == "__main__":
    main()
