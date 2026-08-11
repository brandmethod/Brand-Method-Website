#!/usr/bin/env python3
"""
Build a single, self-contained copy of the Altigo Passenger Elevator catalogue.

Every image and font referenced by index.html is inlined as a data: URI, so the
result is one .html file that can be emailed, dropped on a USB stick or opened
offline with no assets/ folder next to it.

    python3 build-standalone.py

Output: altigo-passenger-elevator-catalogue.html  (in this folder)
"""

import base64
import mimetypes
import re
from pathlib import Path

HERE = Path(__file__).parent
SRC = HERE / "index.html"
OUT = HERE / "altigo-passenger-elevator-catalogue.html"

MIME = {
    ".png": "image/png",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".svg": "image/svg+xml",
    ".woff2": "font/woff2",
}


def data_uri(path: Path) -> str:
    mime = MIME.get(path.suffix.lower()) or mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    return "data:%s;base64,%s" % (mime, base64.b64encode(path.read_bytes()).decode("ascii"))


def main() -> None:
    html = SRC.read_text(encoding="utf-8")
    cache: dict[str, str] = {}
    missing: list[str] = []

    def replace(match: re.Match) -> str:
        rel = match.group("path")
        if rel.startswith("data:"):
            return match.group(0)
        if rel not in cache:
            asset = (HERE / rel).resolve()
            if not asset.is_file():
                missing.append(rel)
                return match.group(0)
            cache[rel] = data_uri(asset)
        return match.group(0).replace(rel, cache[rel])

    # src="assets/..."  and  url("assets/...")
    html = re.sub(r'src="(?P<path>assets/[^"]+)"', replace, html)
    html = re.sub(r'url\("(?P<path>assets/[^"]+)"\)', replace, html)

    OUT.write_text(html, encoding="utf-8")
    size = OUT.stat().st_size / 1_048_576
    print(f"inlined {len(cache)} assets -> {OUT.name} ({size:.1f} MB)")
    if missing:
        print("MISSING (left as-is):")
        for m in sorted(set(missing)):
            print("  ", m)


if __name__ == "__main__":
    main()
