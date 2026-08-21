#!/usr/bin/env python3
"""
Export the catalogue as a PDF at its native page size — 1920 x 1080 px
(1440 x 810 pt), full bleed, no navigation bar, no letterbox bands and no
printed footer.

This is the presentation-size export. The A4 landscape version is the one the
Print button in the catalogue produces; a browser print dialog cannot be set to
a custom 16:9 sheet, which is why this runs headless instead.

    pip install playwright
    python3 export-deck-pdf.py

Output: Altigo-Passenger-Elevator-Catalogue-1920x1080.pdf (in this folder)
"""

import asyncio
import os
from pathlib import Path

from playwright.async_api import async_playwright

HERE = Path(__file__).parent
SRC = HERE / "index.html"
OUT = HERE / "Altigo-Passenger-Elevator-Catalogue-1920x1080.pdf"

# 1920 x 1080 css px at 96dpi = 20in x 11.25in.
#
# The page stylesheet scales the 1920x1080 canvas to the sheet width, so on a
# 16:9 sheet the letterbox bands collapse to nothing by themselves. Two things
# still need saying: the @page rule has to match the paper we ask for (otherwise
# the browser lays the document out for A4 and shrinks it onto the sheet), and
# the printed footer belongs to the A4 version only.
EXPORT_CSS = """
@page{size:20in 11.25in;margin:0}
@media print{
  .printfoot{display:none !important}
  .canvas{top:0 !important}
}
"""

# Set this if Chromium lives somewhere Playwright does not look by default;
# leave it None and Playwright will use its own download.
CHROME = os.environ.get("CHROME_PATH") or None


async def main() -> None:
    async with async_playwright() as p:
        launch = {"args": ["--no-sandbox"]}
        if CHROME:
            launch["executable_path"] = CHROME
        browser = await p.chromium.launch(**launch)
        page = await browser.new_page(viewport={"width": 1920, "height": 1080})

        await page.goto(SRC.resolve().as_uri())
        await page.wait_for_timeout(2500)          # fonts and imagery settle
        await page.add_style_tag(content=EXPORT_CSS)

        await page.pdf(
            path=str(OUT),
            width="20in",
            height="11.25in",
            print_background=True,
            margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
            prefer_css_page_size=True,
        )
        await browser.close()

    print(f"{OUT.name}  ({OUT.stat().st_size / 1_048_576:.1f} MB)")


if __name__ == "__main__":
    asyncio.run(main())
