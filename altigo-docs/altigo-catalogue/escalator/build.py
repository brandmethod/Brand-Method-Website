#!/usr/bin/env python3
"""
Build the Altigo escalator catalogue.

Reads catalogue.template.html, replaces every {{ASSET:filename}} token with a
base64 data URI of assets/<filename>, and writes a single self-contained
index.html that works offline and from file://.

    python3 build.py
"""

import base64
import mimetypes
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
TEMPLATE = HERE / "catalogue.template.html"
ASSETS = HERE / "assets"
OUTPUT = HERE / "index.html"

TOKEN = re.compile(r"\{\{ASSET:([^}]+)\}\}")


def data_uri(name: str) -> str:
    # "logo-blue.png" resolves inside assets/; "fonts/Inter-600.woff2" from here
    path = (HERE / name) if "/" in name else (ASSETS / name)
    if not path.is_file():
        raise SystemExit(f"missing asset: {path}")
    mime = mimetypes.guess_type(name)[0] or "application/octet-stream"
    return f"data:{mime};base64," + base64.b64encode(path.read_bytes()).decode("ascii")


def main() -> int:
    html = TEMPLATE.read_text(encoding="utf-8")
    used: dict[str, int] = {}

    def sub(m: re.Match) -> str:
        name = m.group(1).strip()
        used[name] = used.get(name, 0) + 1
        return data_uri(name)

    html = TOKEN.sub(sub, html)
    OUTPUT.write_text(html, encoding="utf-8")

    for name in sorted(used):
        print(f"  inlined {name}  ×{used[name]}")
    unused = sorted(p.name for p in ASSETS.iterdir() if p.is_file() and p.name not in used)
    unused = [u for u in unused if not any(u in k for k in used)]
    if unused:
        print("  unused:", ", ".join(unused))
    print(f"\n{OUTPUT.name}  {OUTPUT.stat().st_size / 1024:.0f} KB")
    return 0


if __name__ == "__main__":
    sys.exit(main())
