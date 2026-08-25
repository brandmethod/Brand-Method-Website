# -*- coding: utf-8 -*-
import json, io, os, re
B = os.path.dirname(os.path.abspath(__file__))
g = {}
for f in ["gen_part1.py","gen_part2.py","gen_part3.py","gen_part4.py",
          "gen_p01_08.py","gen_p05_08.py","gen_p09_12.py","gen_p13_18.py",
          "gen_p19_23.py","gen_p24_30.py"]:
    exec(compile(open(os.path.join(B,f), encoding="utf-8").read(), f, "exec"), g)

PAGES = g["PAGES"]; CSS = g["CSS"]; CHROME_CSS = g["CHROME_CSS"]
N = len(PAGES)
assert N == 30, f"expected 30 pages, got {N}"

engine = open(os.path.join(B,"engine.js"), encoding="utf-8").read()
engine = engine.replace("<script>\n","",1).replace("</script>","")

FONTS = ("https://fonts.googleapis.com/css2?"
  "family=Archivo:wdth,wght@62..125,400..900&"
  "family=Figtree:wght@300..900&"
  "family=JetBrains+Mono:wght@400..700&"
  "family=Noto+Sans+SC:wght@400..700&"
  "family=Noto+Naskh+Arabic:wght@400..700&display=swap")

NAV = '''
<div class="nav" id="nav">
  <button class="arr" id="prev" title="Previous page" aria-label="Previous page">&#8592;</button>
  <div class="dots" id="dots"></div>
  <div class="nsep"></div>
  <div class="nname" id="nname"></div>
  <div class="nsep"></div>
  <div class="ncount"><b id="ncur">01</b> / <span id="ntot">30</span></div>
  <button class="arr" id="next" title="Next page" aria-label="Next page">&#8594;</button>
  <div class="nsep"></div>
  <div class="zm">
    <button id="zout" title="Zoom out" aria-label="Zoom out">&#8722;</button>
    <button id="zpct" title="Reset to 100 per cent">100%</button>
    <button id="zin" title="Zoom in" aria-label="Zoom in">+</button>
    <button id="zfit" title="Fit to screen">Fit</button>
  </div>
  <div class="nsep"></div>
  <button class="nico" id="btnGrid" title="All pages" aria-label="All pages"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="3" width="7" height="7" rx="1.5"/><rect x="3" y="14" width="7" height="7" rx="1.5"/><rect x="14" y="14" width="7" height="7" rx="1.5"/></svg></button>
  <button class="nico" id="btnPrint" title="Print or export PDF" aria-label="Print"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"><path d="M7 8V3h10v5"/><rect x="3" y="8" width="18" height="8" rx="2"/><path d="M7 14h10v7H7z"/></svg></button>
  <button class="nico" id="btnHome" title="Back to cover" aria-label="Back to cover"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"><path d="M4 11 12 4l8 7"/><path d="M6 10v10h12V10"/></svg></button>
</div>
<div class="hint" id="hint">Arrows page &middot; 0 fits &middot; G all pages &middot; P print &middot; Esc closes</div>
<div class="sheetlist" id="sheetlist">
  <div class="slbar"><h4>All Pages</h4><div class="sub">30 pages &middot; click to jump</div>
  <div class="x" id="slClose">Close</div></div>
  <div class="slscroll"><div class="slgrid" id="slgrid"></div></div>
</div>
<div class="pm" id="pm"><div class="pmbox">
  <h4>Print and export</h4>
  <p>Choose a sheet size then print. In the browser dialog set margins to <b>None</b> and switch on
  <b>Background graphics</b>. Choose <b>Save as PDF</b> for a press ready file.</p>
  <div class="pmlab">Sheet size</div>
  <div class="opts" id="optSize">
    <div class="opt sel" data-w="1920px" data-h="1080px" data-s="1">Native 1920 x 1080 <span>exact design size</span></div>
    <div class="opt" data-w="297mm" data-h="210mm" data-s="0.5837">A4 landscape <span>297 x 210 mm</span></div>
    <div class="opt" data-w="420mm" data-h="297mm" data-s="0.8256">A3 landscape <span>420 x 297 mm</span></div>
    <div class="opt" data-w="11in" data-h="8.5in" data-s="0.5500">US Letter landscape <span>11 x 8.5 in</span></div>
  </div>
  <div class="pmlab">Range</div>
  <div class="opts" id="optRange">
    <div class="opt sel" data-r="all">All pages <span>30 pages</span></div>
    <div class="opt" data-r="one">Current page only <span>single sheet</span></div>
  </div>
  <div class="pmact"><button id="pmCancel">Cancel</button><button class="go" id="pmGo">Print now</button></div>
</div></div>
<div id="printroot"></div>'''

slides = "\n".join(p["html"] for p in PAGES)
names = json.dumps([p["name"] for p in PAGES], ensure_ascii=False)
groups = json.dumps([p["group"] for p in PAGES], ensure_ascii=False)

html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Vit&rsquo;s Brand Book</title>
<meta name="description" content="The Vit's Noodles brand book - brand, verbal identity, visual identity and application. Wireframe draft edition V1.0.">
<style id="psize">@page{{size:1920px 1080px;margin:0}}</style>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}">
<style>{CSS}{CHROME_CSS}</style>
</head>
<body>
<div id="stage"><div id="scaler">
{slides}
</div></div>
{NAV}
<script>window.__NAMES__={names};window.__GROUPS__={groups};</script>
<script>
{engine}
</script>
</body>
</html>
'''
out = os.path.join(B, "vits_brand_book.html")
open(out, "w", encoding="utf-8").write(html)
print(f"pages: {N}   bytes: {len(html):,}   -> {out}")
for i, p in enumerate(PAGES, 1):
    print(f"  {i:02d}  {p['group']:16s} {p['name']}")
