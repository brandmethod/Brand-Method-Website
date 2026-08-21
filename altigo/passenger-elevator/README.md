# ALTIGO · Passenger Elevator — Product Catalogue 2026

An interactive HTML catalogue rebuilt from the original PDF. 17 pages, each one an
exact **1920 × 1080** landscape canvas, with slide navigation, an alignment-grid
overlay, a hide-bar review mode and an **A4 landscape** print/PDF export.

```
altigo/passenger-elevator/
├─ index.html                                  ← the catalogue (open this)
├─ altigo-passenger-elevator-catalogue.html    ← single-file copy, everything inlined
├─ build-standalone.py                         ← regenerates the single-file copy
├─ export-deck-pdf.py                          ← exports the 1920×1080 PDF
├─ README.md
└─ assets/
   ├─ fonts/   Altigo Edge, Altigo Display, IBM Plex Sans, Inter
   └─ img/     all catalogue imagery (94 files)
```

Open `index.html` in Chrome or Edge. Nothing to install, no internet needed —
fonts and images are local.

---

## Deck-nav

A floating pill along the bottom of the window. Structure is fixed — the same
bar every book gets — and only the accent colour follows the brand.

| Control | What it does | Key |
| --- | --- | --- |
| `←` `→` | Page back / forward | `←` `→` `Space` `Home` `End` |
| dot rail | One 6 px dot per page; the current one becomes a numbered pill in the accent. Hover a dot to enlarge it, click to jump. Scrolls itself when the book is long | — |
| slide name | `05 · Core Safety & Performance` — position and title of the page you are on | — |
| counter | Position within the **current edition**, not the file | — |
| **Standard / Full** | Full is the complete 17-page catalogue. Standard drops the three technical deep dives — Man Machine Series, Fixture Design, Construction Parameters — leaving 14 client-facing pages. Folios, the contents page, the counter, the rail and both overlays all renumber, and the A4 export prints the edition you are in | — |
| `−` `100%` `+` | Zoom in steps 50 / 65 / 80 / 100 / 125 / 150 / 200 %. Past fit the page pans. Clicking the percentage resets to 100 % | `+` `-` |
| **Fit** | Back to fit-the-window; the readout shows the fit percentage | `0` |
| grid | Full-screen thumbnail overview, current page ringed | `3` |
| filmstrip | Thumbnail strip above the bar for scrubbing without leaving the page | `4` |
| scroll | Continuous vertical reading; the counter follows the scroll | `2` (`1` for slides) |
| guides | Alignment-grid overlay with its layer / opacity controls | `G` |
| print | A4 landscape export checklist, then the print dialog | `P` |
| hide | Clears the bar; a chip brings it back | `H` |
| home | Back to the cover | — |

`Esc` closes an overlay, `F` is fullscreen, and swipe works on touch screens.
Every page has a deep link — `index.html#p07` opens page 7 — and
`index.html?thumb=1` renders the cover alone with no bar, for hub thumbnails.

### Alignment grid

Press **Guides** to overlay the layout system the catalogue is built on:

- **Margins** — 88 px side, 72 px top/bottom safe box
- **Columns** — 12 columns · 116 px wide · 32 px gutter
- **Rows** — 8 rows · 96 px tall · 24 px gutter
- **Baseline** — 24 px sub-grid
- **Centre** — vertical and horizontal centre lines
- **Safe area** — 48 px outer trim guide

Each layer toggles independently, and the whole overlay runs at **100 % / 50 % /
25 % opacity** so you can check alignment over dark pages and photography.

Every page is built on this grid: page margins, headers, card columns, image
bands and the folio all snap to it.

### Printing / exporting to PDF

Press **Print · PDF** and follow the on-screen checklist:

1. Destination — **Save as PDF**
2. Layout — **Landscape** · Paper — **A4**
3. Margins — **None**
4. **Background graphics** — ticked (under *More settings*)
5. Scale — **Default / 100 %**

Each 16:9 page is centred on the A4 sheet and the leftover strip becomes a
letterbox band carrying a printed footer (catalogue line + page number). On the
cover and the dark pages the band is deep navy so it reads as a deliberate
cinema bar rather than a gap. The screen folio is hidden when printing so the
page number never appears twice.

### The presentation-size PDF

For a PDF at the catalogue's own page size — **1920 × 1080 px (1440 × 810 pt)**,
full bleed, no letterbox bands and no printed footer:

```bash
python3 export-deck-pdf.py
```

A browser print dialog cannot be set to a custom 16:9 sheet, which is why this
one runs headless rather than sitting behind the Print button.

---

## Design system

**Type** — the original typefaces are embedded as subsets taken from the source
catalogue, so the wordmark, headings and spec figures are unchanged:

| Role | Family |
| --- | --- |
| Kickers, cover display, spec values, contact values | Altigo Edge *(Ardela Edge X01 ExtraBold)* |
| Page headings, folios | Altigo Display *(Axiforma Black / Bold / Regular)* |
| Body copy, tables, labels | IBM Plex Sans |
| Small caps labels, cover meta | Inter |

Poppins is loaded as a metric-compatible fallback so nothing breaks if a glyph
falls outside the embedded subsets.

**Colour** — unchanged from the source: `#0242CA` Altigo blue, `#F61800` Altigo
red, `#0B0D12` ink, plus grey steps for hairlines and secondary text.

**Edges** — every corner in the catalogue is square. `border-radius` is reset to
`0` globally, so cards, chips, swatches, buttons and image frames all keep sharp
edges.

**Lines** — the original's stacked rules, boxed-in-boxed card borders and the
repeated diagonal corner stripe on interior pages were removed, and so was every
white rule and grid overlay on the dark pages. What remains: short blue rules
that open a spec block or a section label, and nothing else. Pills on the dark
pages are filled rather than outlined. The red/blue diagonal appears only on the
cover and the back page.

**Page grounds** — the book no longer runs a row of plain white pages. Every
page sits on one of three grounds:

| Ground | Where | What it is |
| --- | --- | --- |
| `deep` | 04 Design · 05 Core Safety · 09 Sightseeing · 14 Man Machine · 17 Contact | Deep navy with a blue bloom — the chapter pages |
| `tint` | 02 Contents · 03 Company · 06 Configurations · 12 Platform · 13 Freight · 15 Fixture · 16 Construction | A cool paper tint with a soft top-right light and a ghosted wordmark |
| white | 07 · 08 · 10 · 11 — the cabin pages | Photography carries the page, so the ground stays out of the way |

**Layout** — every interior page is built the same way: a masthead in the top
zone (kicker · headline · Altigo Edge qualifier · wordmark right), then imagery,
then content. Headlines are set in Altigo Display Black at 72–92 px with the
second word in red, and **type never sits on photography** — images run
full-bleed or in cards, captions and specs sit beside or below them.

---

## Content

All facts, model codes, finishes and dimensions come from the source catalogue.
Editorial changes were limited to correcting typography and obvious errors:

- `ELAVATOR` → `ELEVATOR`, `Mirrior` → `Mirror`, `harline` → `hairline`,
  `contiguration` → `configuration`, `titonium` → `titanium`, `coner` → `corner`,
  `glasss` → `glass`, `wal` → `wall`
- hyphenation fixed — *cutting-edge, fast-paced, mid- and high-rise,
  machine-room-less, low-traffic, multi-layer, purpose-designed, anti-interference*
- the Platform page kicker read `PROTECT EVERY HEALTH JOURNEY` (copied from the
  Medical page) → `ACCESSIBILITY · PLATFORM LIFTS`
- `Your Wellness, Your Way` → `Your journey, your way` (the original line came
  from a different sector)
- page numbers were duplicated in the source (two pages numbered `03`) → now
  sequential 02–17
- a **Contents** page was added as page 02 so a 17-page deck can be navigated
- **Construction Parameters** keeps its three schematic drawings, but every
  dimension line, arrow and figure was stripped out of them (they were drawn in
  blue over black line art, so the annotations could be separated by colour).
  The measurements live only in the wording beside the drawings; dimensioned
  drawings are issued per project as separate documents

**Contact details are unchanged** and now appear consistently on the cover and
the back page:

> ALTIGO SDN. BHD. · REG. 562238-H
> NO. 54-3-3, WISMA SRI MATA, JALAN VAN PRAAGH, 11600 PENANG, MALAYSIA
> +604-283 7005 / +604-283 6772 · ALTIGOELEVATOR@GMAIL.COM · WWW.AKKALLIANCE.COM

The cover in the source PDF carried placeholder contacts
(`+60 1234-56-7890`, `ALTIGO@EMAIL.COM`, empty address); those were replaced with
the real details from the back page.

The source also printed `WWW.ALTIGO.COM` and `ENQUIRY@ALTIGO.COM` — a domain the
company does not hold. Altigo trades under AKK, so the website line is now
`WWW.AKKALLIANCE.COM`, and the enquiry address is the working
`ALTIGOELEVATOR@GMAIL.COM`.

---

## Editing

`index.html` is one plain file — no build step, no framework. Page content sits
in `<section class="slide">` blocks in document order; the contents page and the
Pages overview build themselves from each section's `data-title`, `data-sub`
and `data-folio`.

To reorder pages, move the `<section>` blocks. To add one, copy an existing
section and update its `data-*` attributes and folio.

After changing anything, regenerate the single-file copy:

```bash
python3 build-standalone.py
```
