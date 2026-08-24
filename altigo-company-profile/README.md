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
ALTIGO_Company_Profile_2026.pdf     # output, 41 pages, 1440 x 810 pt
```

## Build

```bash
npm install
node build.mjs           # writes ALTIGO_Company_Profile_2026.pdf
node build.mjs --png     # writes out/pNN.png for visual checking
node qa.mjs              # overflow / clipping check — should report 0 issues
```

`CHROME_PATH` overrides the Chromium binary if the bundled path is wrong.

## What was kept

Brand identity is unchanged and was lifted directly from the previous edition:

- **Logo** — all four lockups reused as-is (wordmark and mark, colour and white).
- **Colour** — exact hex values carried over: `#EA1701`, `#0743C9`, `#7FA8FF`,
  `#2A2A70`, `#1A1C41`, `#0A0D2C`, `#F5F7FD`, text `#4C5580` / `#5A628C`.
- **Photography** — every photograph, portrait and the EUROCERT certificate
  reused, re-encoded (13.5 MB of PNG → 3.1 MB of JPEG, no visible loss).
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
  and in print.

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
