# ALTIGO · Passenger Elevator — Product Catalogue 2026

An interactive HTML catalogue rebuilt from the original PDF. 17 pages, each one an
exact **1920 × 1080** landscape canvas, with slide navigation, an alignment-grid
overlay, a hide-bar review mode and an **A4 landscape** print/PDF export.

```
altigo/passenger-elevator/
├─ index.html                                  ← the catalogue (open this)
├─ altigo-passenger-elevator-catalogue.html    ← single-file copy, everything inlined
├─ build-standalone.py                         ← regenerates the single-file copy
├─ README.md
└─ assets/
   ├─ fonts/   Altigo Edge, Altigo Display, IBM Plex Sans, Inter
   └─ img/     all catalogue imagery (94 files)
```

Open `index.html` in Chrome or Edge. Nothing to install, no internet needed —
fonts and images are local.

---

## The navigation bar

A single fixed bar across the top: the Altigo mark and catalogue line on the
left, the pager and controls on the right.

| Control | What it does | Key |
| --- | --- | --- |
| `‹` `01 / 17` `›` | Page back / forward, live page counter | `←` `→` `Space` `Home` `End` |
| **Slides** | One page at a time, centred and scaled to the window | `1` |
| **Scroll** | Every page stacked for continuous reading; the counter follows the scroll | `2` |
| **Pages** | Live thumbnail overview of all 17 pages — click one to jump to it | `3` |
| **Guides** | Alignment-grid overlay with its layer / opacity controls | `G` |
| **Hide bar** | Clears the bar for a clean review; a chip brings it back | `H` |
| **Print · PDF** | Opens the A4 landscape export checklist, then the print dialog | `P` |

Fullscreen is `F`, `Esc` closes the overview or the print dialog. Swipe
left/right works on touch screens in Slides view. A thin red progress line
across the top of the bar tracks how far through the catalogue you are, and
every page has a deep link — `index.html#p07` opens page 7 directly.

### Alignment grid

Press **Grid** to overlay the layout system the catalogue is built on:

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

Press **Print A4** and follow the on-screen checklist:

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
repeated diagonal corner stripe on interior pages were removed. What remains:
one hairline under each page header with a short red tab, one 2 px rule under
each card title, and the red/blue diagonal only on the cover and the back page
where it belongs.

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

**Contact details are unchanged** and now appear consistently on the cover and
the back page:

> ALTIGO SDN. BHD. · REG. 562238-H
> NO. 54-3-3, WISMA SRI MATA, JALAN VAN PRAAGH, 11600 PENANG, MALAYSIA
> +604-283 7005 / +604-283 6772 · ENQUIRY@ALTIGO.COM · WWW.ALTIGO.COM

The cover in the source PDF carried placeholder contacts
(`+60 1234-56-7890`, `ALTIGO@EMAIL.COM`, empty address); those were replaced with
the real details from the back page.

---

## Editing

`index.html` is one plain file — no build step, no framework. Page content sits
in `<section class="slide">` blocks in document order; the contents page and the
navigation drawer build themselves from each section's `data-title`, `data-sub`
and `data-folio`.

To reorder pages, move the `<section>` blocks. To add one, copy an existing
section and update its `data-*` attributes and folio.

After changing anything, regenerate the single-file copy:

```bash
python3 build-standalone.py
```
