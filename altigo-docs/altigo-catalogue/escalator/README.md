# Altigo · Product Catalogue · Escalator 2026

Interactive rebuild of the Altigo escalator catalogue. Thirteen pages at exactly
**1920 × 1080**, with slide navigation on screen and a clean **A4 landscape**
export when printed to PDF.

The book is set to the **Altigo house standard** — the same grid, type scale,
cover, contents and closing page as the *Passenger Elevator* catalogue, so the
two sit together as one series. The standard is documented under *House
standard* below.

## Files

| File | What it is |
|---|---|
| `index.html` | **The deliverable.** Single self-contained file — images and fonts inlined. Works offline, from `file://`, or hosted. |
| `catalogue.template.html` | Source. Same file with `{{ASSET:name}}` tokens instead of base64 blobs. **Edit this one.** |
| `build.py` | Inlines `assets/` + `fonts/` into `index.html`. |
| `assets/` | Photography, logo and the safety diagram, extracted from the 2026 print PDF and optimised. |
| `fonts/` | Self-hosted Latin `woff2` subsets, so the catalogue renders identically without a network connection. |
| `pdf/` | Exports: A4 landscape and native 1920 × 1080, each in a Full and a Standard edition. |

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
| **Standard / Full** | Full is the complete book; Standard hides the deep-dive pages (10 and 12) |
| `−` `%` `+` **Fit**, `0` | Zoom; the percentage and Fit both reset to fit-to-window |
| `G` or the grid icon | All pages as thumbnails |
| `S` or the scroll icon | Slides (one at a time) ↔ Scroll (continuous) |
| `A` or the guides icon | Alignment guides — off → 100% → 50% → off |
| `P` or the print icon | Print dialogue |
| `H` or the ⊘ icon, beside Home | Hide the bar; the ⊘ **Show bar** chip bottom-right brings it back |
| Home icon | Back to the cover, or to `LIBRARY_URL` if set |
| Click any photograph | Open it full size; `←` `→` step through all 17, `Esc` closes |
| Swipe left / right | Previous / next page on touch screens |
| `#01` … `#13` | Deep-link to a page |
| `?edition=standard` | Open in the Standard edition |
| `?thumb=1` | Cover only, no bar — for hub thumbnails |
| `?paper=slide` | Print at the native 1920×1080 page instead of A4 |

The edition applies to print as well: Full exports 13 pages, Standard 11.

Two paper sizes. By default the deck prints A4 landscape, with each 16:9 page
scaled to the full 297 mm width and centred. Add `?paper=slide` to print at the
native page instead — 1920 × 1080 px, which is 1440 × 810 pt or 508 × 285.75 mm,
the same page the 2026 source PDF used. Nothing is scaled and nothing letterboxes;
the pages come out edge to edge.

## Exporting the A4 PDF

Click **Print · PDF**, then in the browser dialogue set:

- **Destination** — Save as PDF
- **Paper** — A4
- **Layout** — Landscape
- **Margins** — None / Default
- **Background graphics** — **on** (Chrome hides it under *More settings*)

Each page becomes one A4 landscape page.

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

Colours, logo, the corner stripe and all photography follow the 2026 print
edition; the typography follows the house standard. `Ardela Edge X01` sets the
kickers, the small letterspaced labels and the cover title; `Axiforma` sets
everything else — page titles, body, figures and captions. Both are named first
in the font stacks, so a machine with the licensed brand fonts installed uses
them; everyone else gets Outfit, which is metrically close.

**Original technical drawings.** The book carries eleven of them, and they are what
give each page its picture. All are inline SVG on one system — `.st` is the
object outline, `.fill` / `.fill2` are solid faces, `.thin` is secondary
structure, `.dim` is a dimension line, `.dash` a hidden or centre line, and the
`.on-dark` variant swaps the palette to white line on navy so the same system
works on either ground. Being vector, they stay sharp at any zoom and in both
PDF exports, and they cost almost nothing in file size.

| Page | Drawing |
|---|---|
| 02 Contents | Crisscross bank, four levels — section |
| 04 Intelligent Control | Signal flow: mains → converter → machine → step band, with the VLR return and the RS485 / BAS report |
| 05 Technical Advantages | Drive train through the truss — machine space, step band, handrail loop, tension carriage, lettered A–G |
| 06 Four Platforms | Four incline profiles, one per duty class, each drawn to its own angle |
| 07 Standard & Optional Parts | Section through balustrade, step and truss, lettered A–F |
| 09 Safety & Detection Devices | Elevation showing where each of the ten standard devices sits |
| 10 Planning & Civil | Well opening — plan, with B, C and D dimensioned |
| 11 Logical Positioning | Five arrangement diagrams — single, continuous, interrupted, parallel, crisscross |
| 12 Construction Parameters | Elevation, cross-section and landing plan |

Each drawing is specific to its page; none is reused. The lettered keys (A–G on
page 05, A–F on page 07) are deliberately letters, not numbers, so they never
collide with the numbered copy running beside them. Page 09 is the exception and
uses numbers on purpose: its pins are 01–10 precisely because they map to the
numbered device list sitting directly above them.

**Photography: once each, never twice.** Every photograph in `assets/` appears
on exactly one page — the cover shot on 01, the interior on 03, the truss on 09,
the five installations on 11, the eight safety details on 08. Nothing is tiled,
tinted or repeated to fill space; where a page needs a picture and has no
photograph of its own, it gets a drawing.

**Page types.** One header and one grid on every page is what made the earlier
draft read flat, so the book now runs four architectures over the same brand
system — same colours, same fonts, same type scale, same 88 px margins, same
sharp corners:

- **Statement** — full-bleed dark, oversized display type: 01, 10, 13.
- **Split** — the header band is dropped and the page is cut vertically instead,
  a full-bleed navy panel carrying a drawing against content on the other side: 02.
- **Reference** — the standard header over a content grid: 03, 08.
- **Diagram** — a large drawing carries the page and the copy runs beside it as a
  key: 05, 07, 09, 11, 12. Pages 04 and 06 are the dark variant of the same idea.

**Sharp corners, everywhere.** Nothing in the book is rounded. Every photograph,
panel, drawing, label, badge, swatch and rule is a square corner; the radius
tokens `--r` and `--r-s` are both `0`, and the icons' `rect` elements carry no
`rx`. The only rounded thing in the file is the floating navigation pill, which
is screen chrome rather than part of the catalogue and follows the supplied
deck-nav component. Nothing is italic or script either; `i`, `em`,
`cite` and `address` are all reset to `font-style: normal`. The only curves in
the document belong to the Altigo mark itself and to the objects the technical
drawings depict — the handrail section and the controller icon.

**Safety callouts (page 08).** The numbers 1–8 on the cutaway were separate
text on the source PDF page, not part of the drawing, so they were lost when the
image was extracted. They are back as HTML markers positioned by percentage,
using the coordinates read out of the original page, with two pairs nudged apart
so they don't collide at marker size. Because they are percentage-positioned,
they scale correctly when the drawing is opened in the image viewer.

**The grid.** 88 px side margins and 32 px gutters, as the house standard sets
them: two columns of 856, three of 560, four of 410. Horizontal zones at 71
(kicker), 108 (title), 180 (header hairline), 212 (body top) and 984 (body
bottom). Press `A` to see it.

Every top-level block sits on whole columns. The introduction is two 856 columns,
the range page is four of 410, the parts table is three of 560, and the civil page
is three blocks with the elevation spanning two of them. The two five-up rows —
the key figures on page 05 and the planning gallery on page 11 — are the one
arrangement the column set cannot host; they align to the outer margins and the
centre line instead, which is noted in the CSS beside each.

Aligning to the grid made most of the vertical rules redundant, so they are gone:
the column dividers on the range page, the key-figure and process bands, the
chapter figures and the dimension-key column. Horizontal rules that carry real
structure — the header hairline, the contents rows, table and list rows — stay.

**Pale rules: covers only.** Pages 02–12 keep their pale rules — the header
hairline, the contents rows, table, list and dimension-key rows, the grid texture
on pages 06 and 10, and the outlines on icon frames. The cover and the closing
page carry none: no grid texture, no rule above the contact block and none
between the contact fields. The exceptions are scoped by the section's
`data-bg`, so the two covers can change without touching the rest.

Small labels are plain letterspaced type, not outlined chips — the house books
never box a label, and boxing one reintroduces exactly the container shapes the
rebuild set out to remove.

**No running footer.** As in the house standard, interior pages carry neither a
footer nor a page number; the body simply runs to `y 984`. The closing page is
the exception — the catalogue line on the left, the year on the right, at
`y 987`.

**Rhythm and scale.** Thirteen pages, dark on 01, 04, 06, 10 and 13. Page 10 is
a chapter divider that opens the planning and civil half; it carries the part
title, the three governing civil figures, a contents list, and a well-opening
plan drawn white on navy across its right half.

Scale contrast is carried by the two dark display pages, where the house
standard allows it: the cover title at 172 px over a full-bleed photograph and
the closing head at 76 px. Interior pages hold to the standard — 44 px for the
page title and for the largest figure, nothing above it.

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

## House standard

Measured off the *Passenger Elevator* 1920 × 1080 edition and matched here to
within a couple of pixels. Coordinates are from the top-left of the page.

| Element | Position | Type |
|---|---|---|
| Side margin | 88 px, both sides | — |
| Gutter | 32 px; two columns of 856 px | — |
| Logo | `x 88, y 72`, 262 × 55 on the cover, 250 × 53 elsewhere | — |
| Kicker | `x 88, y 71` | Ardela Edge X01 ExtraBold 16, red, letterspaced |
| Page title | `x 88, y 108`, second line at 155 | Axiforma SemiBold 44, blue |
| Red rule | `x 88, y 179`, 96 × 3 | — |
| Header hairline | `x 88 → 1832, y 180` | — |
| Body top | `y 212` | — |
| Body bottom | `y 984` | — |
| Lead paragraph | 19–22 | Axiforma Regular |
| Body | 17, line pitch 28 | Axiforma Regular |
| Small body | 16, line pitch 24 | Axiforma Regular |
| Section label | 12–13, letterspaced | Ardela Edge X01 |
| Caption | 14 | Axiforma Regular |
| Figure | 21 | Axiforma SemiBold |

Three things are cover-only, and are deliberately absent from every light
interior page: the diagonal red-and-blue corner stripe, the grid texture (which
the dark pages also carry), and display type above 44 px. Interior pages carry no footer and no page number — the
contents page is the only place page numbers appear.

**The cover.** Year at `y 75` right-aligned; eyebrow at `y 341`; the title at
`y 387` in Ardela 172 with a 151 px line pitch; the product line at `y 781` in
Axiforma SemiBold 30; a three-column footer at `y 901` on 444 px centres, labels
at 11 and values at 15 with a 23 px pitch.

**The closing page.** Head at `y 171` in Axiforma SemiBold 76; red rule at
`y 282`, 96 × 4; a two-column field grid at `x 88` and `x 680` starting at
`y 399`, labels at 12 and values at 23; the running line and the year at `y 987`.

**The contents page.** Two 856 px columns, one rule above each row on a 99 px
pitch starting at `y 212`. Item number at the column edge in red, title 76 px in
at 20, its tag inline 12 px after the title at 14, and the page number
right-aligned at 18 in blue.
