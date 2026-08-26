# ALTIGO Elevator Sdn Bhd — Company Profile 2026

Redesign of the 41-slide company profile. `index.html` is the source of truth;
the PDF is generated from it.

```
index.html                          # the whole deck, 41 slides at 1440 x 810
assets/                             # logos, photography, certificate (from the 2026 edition)
fonts/                              # webfont
build.mjs                           # index.html -> PDF
rescale.py                          # normalises page boxes to 1440 x 810 pt
qa.mjs                              # fails loudly on any content overflowing a slide
widows.mjs                          # finds paragraphs with a stranded last line
make-chapter-visuals.py             # duotones the chapter / texture images
make-portraits.py                   # normalises the two leadership cut-outs
make-artifact.py                    # inlines every asset as a data URI
assemble-artifact.py                # wraps the slides in the web viewer shell
preview-artifact.mjs                # screenshots the viewer in light / dark / mobile
ALTIGO_Company_Profile_2026.pdf     # output, 41 pages, 1440 x 810 pt
```

## Build

```bash
npm install
node build.mjs           # writes ALTIGO_Company_Profile_2026.pdf
node build.mjs --png     # writes out/pNN.png for visual checking
node qa.mjs              # overflow / clipping check — should report 0 issues
node widows.mjs          # reports body copy whose last line holds <=3 words
```

`CHROME_PATH` overrides the Chromium binary if the bundled path is wrong.

### Single-file web viewer

```bash
python3 make-artifact.py && python3 assemble-artifact.py   # -> altigo-profile-viewer.html
node preview-artifact.mjs                                  # visual check, reports h-overflow
```

Produces one self-contained HTML file (~5 MB) with every image and the font
inlined as data URIs — no `assets/` folder needed, opens offline by
double-clicking, and works as an emailable link-free handoff. It is gitignored
because it is fully regenerable from `index.html`.

## What was kept

Brand identity is unchanged and was lifted directly from the previous edition:

- **Logo** — all four lockups reused as-is (wordmark and mark, colour and white).
- **Colour** — exact hex values carried over: `#EA1701`, `#0743C9`, `#7FA8FF`,
  `#2A2A70`, `#1A1C41`, `#0A0D2C`, `#F5F7FD`, text `#4C5580` / `#5A628C`.
- **Photography** — every photograph, portrait and the EUROCERT certificate
  reused, re-encoded (13.5 MB of PNG → ~3 MB, no visible loss). Note that
  `photo-usp` carries a soft mask in the source PDF: the area left of the
  escalator is *transparent*, not black, and it is kept as `photo-usp.webp` so
  that alpha survives. Converting it to JPEG flattens that region to solid black,
  which is very obvious once the photograph sits on a white page. The
  chapter and texture images are also ALTIGO's own photographs, duotoned (see
  **Chapter visuals** below) — no stock or generated imagery anywhere.
- **Structure** — same 41 pages in the same order, same folio numbers, so this
  drops in against the old file page for page.

## What changed

**Layout — the main fix.** The previous edition pinned headings to the top of the
slide and content to the bottom, and stretched cards to fill grid cells while
top-aligning the text inside them. That opened holes: roughly 25–40% of several
slides was empty space *inside* boxes. Every slide now runs on one grid — a
fixed-height masthead band, then a content band that is genuinely filled. Where
content is lighter than the band, cards take their natural height and the
breathing room sits *outside* the boxes, which reads as composition rather than
as a gap. Cards that need a footer label distribute top-and-bottom instead of
leaving a void in the middle.

**Deck paragraphs** were right-aligned against left-aligned headings, which left
a ragged left edge fighting the title. They are now a left-aligned second column
in a real two-column masthead, with a hairline closing the band.

**Specific slides**
- p2 — statement page filled out to two columns; stats moved into a rule-divided
  right-hand stack instead of sitting on top of the footer.
- p3 — contents was a narrow strip beside an empty half-page; now a full-width
  two-column list with page numbers.
- p14 — the "Founder & Managing Director" label was dark red on dark navy and
  effectively unreadable, and the name plates sat over the subjects' hands. Names
  moved into the text column; portraits now run full-bleed.
- p16 — org chart connectors did not visibly join the tiers, and the chart sat in
  the right half leaving the left half blank. Redrawn centred and full-width with
  connectors that actually meet the nodes.
- p18 — chart curve now starts at the stated 2000 base (index 100) rather than
  part-way up the axis.
- p21 / p38 — image tiles were mismatched aspect ratios and heights, so captions
  did not align. Uniform tiles, `object-fit: cover`, captions on one baseline.
- p26 — the seven-stage journey was cramped into a thin strip; stages are now
  panels with room to read.
- Icons redrawn as inline SVG (were small rasters) so they stay sharp at any zoom
  and in print, and standardised to a single 60px size via the `--ico` token —
  the previous edition mixed sizes. At that size an icon needs its own line, so
  card headers stack (icon above label); dense blocks that cannot afford the
  extra height use `.hd.side`, which keeps the same 60px icon in a left column.
- Photographs on the split-layout pages (07 Our Aim, 11 Brand USP) were washed
  out by a fade that ran across half the panel; it now feathers only the seam.
  Background imagery on 19, 25 and 34 was effectively invisible under a
  near-opaque wash and is now legible, with dark-page cards given enough weight
  to read as panels over it.

**Chapter visuals.** The eight chapter dividers were flat gradient with roughly
40% of the slide empty — the weakest pages in the deck, and eight near-identical
ones at that. Each now opens on its own full-bleed image so the chapters are
distinguishable at a glance and the deck has a rhythm. Every image is one of
ALTIGO's own photographs put through a duotone ramp (deep navy shadows → brand
blue midtones → pale blue highlights) with a highlight roll-off, so eight
unrelated photographs read as one art-directed set and tie to the palette. The
composition is bottom-anchored on a baseline rather than floated mid-slide.

Two plain dark interior pages (25 Maintenance Programme, 34 Safety & Compliance)
carry the same treatment at low opacity as background texture.

To swap any of them, drop a replacement into `assets/`, edit `CHAPTERS` at the
top of `make-chapter-visuals.py`, and re-run it:

```bash
python3 make-chapter-visuals.py && node build.mjs
```

| Chapter | Source photograph |
|---|---|
| 00 Company Overview | `photo-aim.jpg` |
| 01 Brand Identity | `cover-technician.jpg` |
| 02 Market & Performance | `photo-kl-skyline.jpg` |
| 03 Products & Services | `prod-escalator.jpg` |
| 04 Client Testimonials | `proj-ferringhi-mutiara.jpg` |
| 05 Our Activities | `photo-usp.jpg` |
| 06 Achievements & Certifications | `prod-passenger.jpg` |
| 07 Project References & Contact | `proj-rawang-perdana.jpg` |

**Decorative numbering removed.** The deck was numbering things twice over: a
large faded numeral on every card, a second small numeral under the icon inside
the same card, and a third in the section chip above the page title ("01 ·
Objective"). None of it carried information the reader needed, so all three are
gone, along with the short red dash before the chip and the red rule under each
chapter numeral. Numbering that *does* carry information is kept: chapter
numerals, the table of contents, page folios, and the seven-stage labels on the
Product Journey, where the order is the point.

**Copy** — corrected and made consistent, no claims added or removed:
- p13 "Two decades of experience" contradicted the "25 years / twenty five years"
  used throughout → "Twenty five years".
- p11 folio rendered as `1111` (duplicated element) → `11`.
- Footer text alternated between "Confidential." and the longer authorised-use
  line → one form throughout.
- Contents named sections differently from the pages themselves ("Activities" vs
  "Our Activities", "Voices from our clients" vs "What Our Clients Say") → unified.
- "Our Value" → "Our Values" (six are listed).

The illustrative market-demand chart on p18 keeps its disclaimer, unchanged.

## Typeface

The 2026 edition was set in **Axiforma** (Kastelov) with ArdelaEdge for folio
numerals. Both are commercially licensed, and in the source PDF the text was
outlined as Type 3 glyph procedures, so the fonts cannot be recovered or
redistributed from it. This build ships **Plus Jakarta Sans** (OFL) — a geometric
sans with the same double-storey `a`, comparable x-height and very close overall
proportions.

If you hold an Axiforma licence, drop the woff2 files into `fonts/` and uncomment
the `@font-face` block at the top of `index.html`. The stack is already
`'Axiforma', 'Jakarta', …`, so the whole document picks it up with no other edit.

## One thing worth raising

The profile lists **altigo@gmail.com** as the contact address on the cover, the
contact page and the back cover. On a document that leans on DOSH certification
and EU type examination for credibility, a free mailbox undercuts the rest of the
page. A domain address (e.g. `enquiry@altigo.com.my`) would be a cheap upgrade.
Left as-is here — changing a company's published contact detail isn't a design
decision.
