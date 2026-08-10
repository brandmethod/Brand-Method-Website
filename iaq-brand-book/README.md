# IAQ · Brand Identity Book — Brand OS v3.1

An interactive, presentation-grade brand book built as a single self-contained
web deck. **1920 × 1080 landscape, 53 pages**, designed to be presented live,
shared as a link, or exported to PDF.

This is also the **reference template** for future BrandMethod brand books: the
CSS is a documented brand-book engine, and the page structure is a repeatable
component system. To start a new book, copy this folder, swap the tokens and
assets, and keep the shell.

---

## Run it

Two ways, both interactive:

**A. The single file** — `dist/IAQ-Brand-Identity-Book.html` (3 MB). One file,
everything inlined. Double-click it, email it, drop it on a USB stick. This is
the copy to hand to the client.

**B. The source folder** — open `index.html`. Same book, split into
`css/`, `js/` and `assets/` for editing.

After editing the source, rebuild the single file:

```bash
cd iaq-brand-book
python3 build.py        # → dist/IAQ-Brand-Identity-Book.html
```

## Navigate

| Action | Control |
|---|---|
| Next / previous page | the large **PREV / NEXT** buttons either side of the book, the arrows in the dock, `→` `←`, `Space`, scroll, swipe, or click the right/left half of the page |
| Page index (all 53 thumbnails) | `G`, or the **INDEX** button |
| Fullscreen presentation | `F` |
| First / last page | `Home` / `End` |
| Jump to a section | The rail on the left edge |
| Deep-link to a page | `index.html#26` |

## Export to PDF (1920 × 1080)

Click **PDF** in the dock, or `Ctrl/Cmd + P`. In the print dialog:

- **Destination:** Save as PDF
- **Paper size:** Default (the page CSS declares `1920px × 1080px` landscape)
- **Margins:** None
- **Background graphics:** On

Each page exports as one landscape sheet at exact book dimensions. Note the
export is image-heavy (~15 MB) because of the photography; share it by link or
file transfer rather than email attachment.

---

## Structure

```
iaq-brand-book/
├── index.html          all 53 pages, one <section class="slide"> each
├── build.py            packs everything into dist/ as one self-contained file
├── dist/
│   └── IAQ-Brand-Identity-Book.html   the shareable single file
├── css/book.css        the brand-book engine (tokens → primitives → pages)
├── css/fonts-local.css optional self-hosted @font-face rules
├── js/book.js          deck engine: fit, page turns, index, rail, deep-links
└── assets/
    ├── iaq-wordmark.png        primary registered wordmark (transparent)
    ├── iaq-wordmark-3d.png     dimensional render · digital hero only
    ├── photo-campus.jpg        delivered facility, Malaysia
    ├── photo-team-cleanroom.jpg  the team on site
    └── photo-drawings.jpg      design & consultation
```

### The 53 pages

| Section | Pages | Contents |
|---|---|---|
| Cover | 01 | Brand Identity — The IAQ Book |
| **0.0 Navigation** | 02–04 | Divider, contents & map, Brand OS alignment |
| **1.0 Foundation** | 05–13 | Divider, brand at a glance, vision/mission/principles, three pillars, audience, client journey, positioning map, story arc, the pitch |
| **2.0 Verbal** | 14–19 | Divider, the voice, vocabulary, channels, messaging framework, governed proof |
| **3.0 Visual** | 20–35 | Divider, logo system, logo concept, anatomy, placement, misuse, colour, colour in use, typography, type in use, the element kit, the grid, blueprint system, iconography, photography, system don'ts |
| **4.0 Applications** | 36–43 | Divider, digital flagship, digital surfaces, stationery, tender & investor, site/fleet/wearables, LinkedIn, touchpoint priority |
| **5.0 Governance** | 44–53 | Divider, assets & naming, trademark & legal, subsidiary architecture, per-subsidiary template, three reserved company pages, governance, close |

---

## The engine (css/book.css)

Nine numbered layers, in order:

1. **Tokens** — the locked palette, three type families, base-8 spacing, motion curves
2. **Reset / stage** — the fixed 1920 × 1080 stage, scaled to any viewport by JS
3. **Chrome** — progress, dock, section rail, index overlay
4. **Slide shell** — header / body / footer, the 12-column grid, page transitions
5. **Primitives** — the six-element kit (rule, chip, leader line, drafting grid, scale bar, stat block) plus panels, key/value rows, do/don't lists, swatches
6. **Dimension** — the 3D layer: isometric construction planes, extruded slabs, depth surfaces, glow fields
7. **Specials** — cover, dividers, device mockups, colour, type specimens, close
8. **Motion** — entrance choreography, the page turn, leader-line tracing
9. **Print** — exact 1920 × 1080 landscape export

### Design system, locked

| Token | Value | Role |
|---|---|---|
| IAQ Red | `#EC2027` | single accent — logo, key lines, focus |
| Signal Deep | `#B5121B` | text-safe red — eyebrows, links, emphasis |
| Ink | `#0C1220` | headlines and body |
| Deep Navy | `#0A101F` | dark bands, dividers, showpieces |
| Cloud | `#F7F9FC` | the light base |
| Steel / Mist | `#48536A` / `#828B9E` | support greys |

Type: **Switzer** (display) · **Instrument Sans** (body) · **JetBrains Mono**
(technical). Ratio in use: 62% light / 22% navy-ink / 10% grey / 6% red.

### Fonts

Loaded from Google Fonts (Instrument Sans, JetBrains Mono) and Fontshare
(Switzer), with a system fallback stack so the book still lays out correctly
without a connection — though it will not be in the brand faces.

**To make it fully offline**, `css/fonts-local.css` is ready to go: drop the
three variable `.woff2` files into `assets/fonts/` (sources listed in
`assets/fonts/README.md`), then in `index.html` replace the two CDN `<link>`
tags with:

```html
<link rel="stylesheet" href="css/fonts-local.css">
```

Nothing else changes.

---

## Reusing this as a template

1. Copy the folder and rename it.
2. Replace the tokens in `css/book.css` §1 — that alone re-skins the whole book.
3. Swap `assets/` and the cover.
4. Keep the slide shell: every page is
   `.slide → .ticks + .s-head + .s-body + .s-foot`, and every page declares
   `data-sec`, `data-secname` and `data-title` so the rail and index build
   themselves. Nothing else needs wiring.
5. Add or remove `<section class="slide">` blocks freely — the counter,
   progress bar, index and section rail are all generated from the DOM.

Useful body layouts: `.g-2 .g-3 .g-4 .g-5 .g-6 .g-12 .g-58 .g-64 .g-75`, and
`.s-body.spread` for pages whose rows should sit as one centred block.

---

**Custodian:** BrandMethod Sdn. Bhd. · admin@brandmethod.co
**Edition:** 1.0 · Brand OS v3.1 · © 2026. Internal and authorised partner use only.
