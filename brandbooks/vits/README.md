# Vit's Noodles Brand Book

Edition **V1.0 · Wireframe draft**. Thirty pages, 1920 × 1080, built on the same page
system as the Agensia Brand Book: mono topbar, hairline rule, title/lead head, body,
footer, plus the shared deck shell (paging, zoom, all-pages grid, print/export).

## Files

| File | What it is |
|---|---|
| `vits-brand-book.html` | The deck. Open in any browser no build step, no server. |
| `Vits_Brand_Book_V1.0_Draft.pdf` | 30 pages, 16:9 (1440 × 810 pt), fonts embedded. |
| `src/` | The generator the HTML is built from. |
| `src/fonts/embedded.css` | Archivo, Figtree, JetBrains Mono and the Noto subsets as woff2 data URIs. Regenerate with `fetchfonts.py`. |

## Viewing

Fonts are embedded as woff2 data URIs, so the book renders identically offline
and the PDF carries the real faces rather than a system fallback.

Open `vits-brand-book.html`. Arrow keys page, `0` fits to screen, `G` opens the
all-pages grid, `P` opens print and export, `Esc` closes. The deck scales to any
window; `#p14` in the URL jumps to a page.

## Contents

| Section | Pages |
|---|---|
| 00 Essentials | Introduction, Table of Contents |
| 01 Brand | Company Introduction, Positioning and Script, Vision and Mission, Values and Culture |
| 02 Verbal Identity | Messaging Pillars, Voice and Character |
| 03 Visual Identity | Logo Overview, Concept, Formats, Clearspace and Size, Backgrounds, Don'ts, Colour Palette, Colour in Use, Typography, Type Scale, Language Variants |
| 04 Application | Packaging System, Stationery, Retail and Shelf, Digital and Social |
| 05 Close | Contacts and Legal |

## Identity as drafted

**Mark** the client's own badge, redrawn from `Vits-Logo.png`: a red badge with a
domed top and a scalloped base, an inner keyline, and the wordmark reversed out.
The badge silhouette is traced and close. The wordmark is set in Archivo 900,
which is the nearest available match and **not** the real drawing, so the vector
master is still needed before artwork.

There is no separate symbol and no separate wordmark: the badge is used whole. It
survives to about 60px in a circle; below that an interim `V` tile stands in until
a proper app icon is drawn.

**Palette** Vit's Red `#EC1F28`, Golden Wheat `#F0A81E`, Soy Ink `#191410`,
Steam `#FAF4E9`, Broth `#8A7360`, plus Deep Red `#C4141C` for small type on light
grounds. The signature red is sampled from the client's own logo file. Contrast
ratios on page 3.8 are measured, not estimated: white on the red clears large text
only (4.4:1), which is why nothing under 18px sits on it.

**Type** Archivo (display, 800 expanded), Figtree (text), JetBrains Mono (data),
Arial (documents and email). Noto Sans SC and Noto Naskh Arabic carry the Chinese
and Arabic variants on page 3.11. All are SIL Open Font Licence, so packaging
artwork and partner co-branding carry no per-seat cost.

## Status read before using anything here

This edition is a **wireframe draft**. Structure, hierarchy and copy are proposed
for review.

- The **mark and the red are the client's own**, taken from `Vits-Logo.png`.
  The badge is a redrawing, not the master file: request the vector before any
  artwork goes to separation. No file here is a production master.
- **The mark does not depict the phoenix** that Vit's own storytelling rests on.
  Page 3.2 records this as an open question for the client, because the answer
  changes Section 03 wholesale.
- Every dashed frame is a **placeholder** photography and art direction pending.
- Brand facts (founded 1975, halal certified 1980, Rawang plant, 30+ export markets,
  FSSC 22000 / HACCP / GMP / SMETA, company and contact details) are drawn from
  Vit's published material and should be confirmed by the client before sign-off.
- Flavour band colours on page 4.1 are proposed, not matched to current retail packs.

The open items are listed on page 5.1.

## Rebuilding

```
cd src && python3.13 build.py
```

Needs Python 3.13 or newer (the generators use PEP 701 nested f-strings). Writes
`vits_brand_book.html` beside the sources; copy it up one level to replace the deck.
