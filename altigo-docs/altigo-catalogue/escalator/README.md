# Altigo · Product Catalogue · Escalator 2026

Interactive rebuild of the Altigo escalator catalogue. Eleven slides at exactly
**1920 × 1080**, with slide navigation on screen and a clean **A4 landscape**
export when printed to PDF.

## Files

| File | What it is |
|---|---|
| `index.html` | **The deliverable.** Single self-contained file — images and fonts inlined. Works offline, from `file://`, or hosted. |
| `catalogue.template.html` | Source. Same file with `{{ASSET:name}}` tokens instead of base64 blobs. **Edit this one.** |
| `build.py` | Inlines `assets/` + `fonts/` into `index.html`. |
| `assets/` | Photography, logo and the safety diagram, extracted from the 2026 print PDF and optimised. |
| `fonts/` | Self-hosted Latin `woff2` subsets, so the catalogue renders identically without a network connection. |

## Rebuilding after an edit

```bash
python3 build.py      # catalogue.template.html + assets/ + fonts/ → index.html
```

No dependencies beyond the Python standard library.

## Using it

Open `index.html` in any browser.

| Control | Action |
|---|---|
| `←` `→` `Space` `PgUp` `PgDn` | Previous / next slide |
| `Home` / `End` | First / last slide |
| `G` or **Grid** | All eleven slides as thumbnails |
| `S` | Toggle **Slides** (one at a time) ↔ **Scroll** (continuous) |
| `P` or **Print · PDF** | Print dialogue |
| `#01` … `#11` in the URL | Deep-link to a slide |

## Exporting the A4 PDF

Click **Print · PDF**, then in the browser dialogue set:

- **Destination** — Save as PDF
- **Paper** — A4
- **Layout** — Landscape
- **Margins** — None / Default
- **Background graphics** — **on** (Chrome hides it under *More settings*)

Each slide becomes one A4 landscape page.

### How the 16:9 → A4 fit works

A4 landscape is 297 × 210 mm (1.414:1); the slides are 16:9 (1.778:1). The stage
is scaled to the full 297 mm page width — `1920px × 0.584646 = 1122.5px = 297mm`
— and centred vertically, leaving 21.5 mm above and below.

On the white slides those bands are invisible. On the cover and the contact page
the gradient is re-declared on the *page* container so it runs edge to edge and
no band shows. That is why the backgrounds are CSS gradients rather than images.

Three details make the export reliable, and are easy to break:

- `zoom`, not `transform`, scales the stage for print. A transform is a paint
  effect; Chrome's paginator lays out the untransformed box and mis-pages it.
- The stage stays `position: relative` in print. Setting it to `static` moves the
  containing block to `.slide` and every absolutely-positioned element on the
  slide jumps.
- `html, body` are pinned to `297mm` in print. Left at viewport width, the
  browser shrink-to-fits the whole document and everything comes out small.

## Design notes

Colours, typography, logo, the corner stripe and all photography follow the
2026 print edition. `Axiforma` and `Ardela Edge X01` are named first in the font
stacks, so a machine with the licensed brand fonts installed uses them; everyone
else gets Outfit, which is metrically close. Body text is IBM Plex Sans and
labels are Inter — both exactly as in the source document.

The corner stripe and all icons are vector, and the civil drawings on slide 10
are inline SVG rather than a raster image, so they stay sharp in print.
