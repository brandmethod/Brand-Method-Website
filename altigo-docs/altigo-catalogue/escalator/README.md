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

Open `index.html` in any browser. The deck-nav pill floats at the foot of the
window — the same component every book carries; only the accent colour changes.

**prev · dot rail · page name · counter · next · edition · zoom · icons**

| Control | Action |
|---|---|
| `←` `→` `Space` `PgUp` `PgDn` | Previous / next page |
| Dot rail | Jump to any page; the active dot becomes a numbered pill |
| **Standard / Full** | Full is the complete book; Standard hides the deep-dive pages (09 and 11) |
| `−` `%` `+` **Fit**, `0` | Zoom; the percentage and Fit both reset to fit-to-window |
| `G` or the grid icon | All pages as thumbnails |
| `S` or the scroll icon | Slides (one at a time) ↔ Scroll (continuous) |
| `A` or the guides icon | Alignment guides — off → 100% → 50% → off |
| `P` or the print icon | Print dialogue |
| `H` or the ⊘ icon, beside Home | Hide the bar; the ⊘ **Show bar** chip bottom-right brings it back |
| Home icon | Back to the cover, or to `LIBRARY_URL` if set |
| Click any photograph | Open it full size; `←` `→` step through all 17, `Esc` closes |
| Swipe left / right | Previous / next page on touch screens |
| `#01` … `#12` | Deep-link to a page |
| `?edition=standard` | Open in the Standard edition |
| `?thumb=1` | Cover only, no bar — for hub thumbnails |

The edition applies to print as well: Full exports 12 A4 pages, Standard 10.

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

**Sharp corners, everywhere.** Nothing in the deck is rounded. Every photograph,
panel, drawing, tag, badge, swatch, rule and button is a square corner; the
radius tokens `--r` and `--r-s` are both `0` and there is no `border-radius`
left with a non-zero value. Nothing is italic or script either; `i`, `em`,
`cite` and `address` are all reset to `font-style: normal`. The only curves in
the document belong to the Altigo mark itself and to the objects the technical
drawings depict — the handrail section and the controller icon.

**Safety callouts (page 07).** The numbers 1–8 on the cutaway were separate
text on the source PDF page, not part of the drawing, so they were lost when the
image was extracted. They are back as HTML markers positioned by percentage,
using the coordinates read out of the original page, with two pairs nudged apart
so they don't collide at marker size. Because they are percentage-positioned,
they scale correctly when the drawing is opened in the image viewer.

**The grid.** 120 px side margins, twelve columns of 118 px with 24 px gutters:
12×118 + 11×24 = 1680 = 1920 − 240. Horizontal zones at 88 (mark base), 212
(header base), 254–930 (body) and 1008 (footer rule). Press `A` to see it.

Every top-level block sits on whole columns. Three-column rows span four columns
each (544 px), four-column rows span three (402 px), the introduction runs nine
columns of text against a figure that starts at column ten, and the civil page is
three blocks of 544 px with the elevation spanning two of them. The two five-up
rows — the key figures on page 04 and the planning gallery on page 10 — are the
one arrangement a twelve-column grid cannot host; they align to the outer margins
and the centre line instead, which is noted in the CSS beside each.

Aligning to the grid made most of the vertical rules redundant, so they are gone:
the column dividers on the range page, the key-figure and process bands, the
chapter figures and the dimension-key column. Horizontal rules that carry real
structure — the header hairline, the footer, table and list rows — stay.

**Running footer.** Every page from 02 to 11 carries the same footer the closing
page sets: a hairline, the catalogue line on the left, the page number on the
right. It runs the full measure on every page.

**Rhythm and scale.** Twelve pages, dark on 01, 05, 09 and 12 — one dark page
every four, so the deck never runs more than three white pages together. Page 09
is a chapter divider that opens the planning and civil half; it carries the part
title at 118 px, the three governing civil figures and a contents list.

Scale contrast does the rest of the work. The cover title runs at 172 px over a
full-bleed photograph; the introduction headline at 76 px beside a photograph
bled off the right and bottom edges; the maximum rise on page 05 at 78 px, which
turns a specification table into the product spread; the key figures on page 04
at 64 px. Nothing on an interior page used to exceed 44 px, which is why the
earlier drafts read flat.

**Image resolution.** Every photograph is carried at the native resolution of
the 2026 print PDF, with no downscaling; the cover keeps its original JPEG
stream byte-for-byte and the logo and safety diagram are lossless PNG. The rest
are re-encoded once at quality 95 with 4:4:4 chroma, which is visually lossless.
That is why `index.html` is around 4 MB.

Several source photographs are small — the eight safety details range from 302
to 616 px wide — so the layouts place them at or below native size. If sharper
originals ever turn up, drop them into `assets/` under the same names and
re-run `build.py`; nothing else needs to change.

The stage is scaled with `zoom` rather than `transform`, on screen as well as in
print. `zoom` relayouts, so text is re-rasterised and images are sampled at the
displayed size instead of being resampled from a scaled layer.

All interaction — the progress bar, the image viewer, hover states — is hidden
under `@media print`, so the PDF is unaffected.
