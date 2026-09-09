# Project rules

## IAQ Brand Identity Book (Brand OS v3.1)

Layout rules for the brand book. These are standing requirements — apply them to
every new page and check them after any layout edit.

### 1. Column alignment between stacked rows

**When a page stacks a visual row above a text row, both rows must use the same
column split.** The lower row never introduces its own column count.

A mockup row of two, with a narrative plus a two-part spec beneath it, is built
like this — the spec halves nest *inside* the second top-level column:

```html
<!-- visual row: the split is defined here -->
<div style="display:grid;grid-template-columns:1.4257fr 1.4243fr;gap:var(--gut);max-width:1696px">
  <div data-r="1">…mockup A…</div>
  <div data-r="2">…mockup B…</div>
</div>

<!-- text row: SAME columns, SAME max-width -->
<div style="display:grid;grid-template-columns:1.4257fr 1.4243fr;gap:var(--gut);max-width:1696px">
  <div data-r="3">…narrative…</div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:var(--gut)">
    <div data-r="4">…spec, first half…</div>
    <div data-r="5">…spec, second half…</div>
  </div>
</div>
```

Never leave the lower row as `4fr 4fr 4fr` (or `1fr 1fr 1fr`) under a two-column
visual row. Its edges will not line up with anything above it.

Verify by measuring the rendered column boundaries, not by reading the CSS —
`scratchpad/alledges.py` prints the top and bottom edges per page and reports
ALIGNED / MISMATCH.

### 2. Images are never distorted or cropped

Mockup boxes carry `aspect-ratio` matching the source image exactly, so the photo
fills the box with no letterboxing and no crop. Where two images of different
ratios sit side by side, size the **columns** in proportion to those ratios
(`grid-template-columns:{r1}fr {r2}fr`) so both fill their boxes and the heights
still match.

The wordmark itself is never non-uniformly scaled. A mark applied to a surface
photographed in perspective uses a real 3D transform
(`perspective(...) rotateY(...)`), never `skewY` or `scaleY`.

### 3. Mockups fill the working grid

A visual should reach the full grid width (1696px, or 1656px where a page uses a
narrower measure). Do not cap a mockup at an arbitrary pixel width. Where a
mockup is height-constrained, size it by height and let its column follow.

### 4. Maximum two mockups per page

Three or more mockups get split across pages rather than shrunk.

### 5. Editing the HTML

- `<div>` counts **must** balance per `<section class="slide">`. An extra
  `</div>` still renders acceptably in the browser but nests the following
  slides at print time — the PDF silently loses pages. Always check the balance
  after a structural edit, and confirm the PDF page count.
- Every slide must be exactly 1080px tall (`scratchpad/tallcheck.py`).
- Paragraphs must not end with 1–3 words alone on the last line
  (`scratchpad/audit_orphans2.py` must report 0).
- Nothing crosses into the footer beyond the known baseline
  (`scratchpad/check.py`).
- Nothing crosses the right safe margin except deliberate full-bleed pages —
  cover, close page, section dividers (`scratchpad/overflowx.py`).

### 6. After any change

Rebuild all three deliverables and confirm the PDF reports **99 pages**:
self-contained HTML, the print PDF with fonts embedded, and the published
artifact.
