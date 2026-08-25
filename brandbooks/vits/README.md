# Vit's Noodles — Brand Book

Edition **V1.0 · Wireframe draft**. Thirty pages, 1920 × 1080, built on the same page
system as the Agensia Brand Book: mono topbar, hairline rule, title/lead head, body,
footer, plus the shared deck shell (paging, zoom, all-pages grid, print/export).

## Files

| File | What it is |
|---|---|
| `vits-brand-book.html` | The deck. Open in any browser — no build step, no server. |
| `Vits_Brand_Book_V1.0_Draft.pdf` | 30 pages, 16:9 (1440 × 810 pt), fonts embedded. |
| `src/` | The generator the HTML is built from. |

## Viewing

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

**Mark** — a phoenix rising as steam from a bowl. The phoenix carries the name
(Mandarin *Wei Yi*, 唯一, "the only one"); the bowl carries the category. Drawn
original for this edition as a placeholder for whatever vector master Vit's holds.

**Palette** — Vit's Red `#D8232A`, Golden Wheat `#F0A81E`, Soy Ink `#191410`,
Steam `#FAF4E9`, Broth `#8A7360`. Contrast ratios on page 3.8 are measured, not
estimated.

**Type** — Archivo (display, 800 expanded), Figtree (text), JetBrains Mono (data),
Arial (documents and email). Noto Sans SC and Noto Naskh Arabic carry the Chinese
and Arabic variants on page 3.11. All are SIL Open Font Licence, so packaging
artwork and partner co-branding carry no per-seat cost.

## Status — read before using anything here

This edition is a **wireframe draft**. Structure, hierarchy and copy are proposed
for review.

- The mark, palette and typeface selection are a **design proposal**. They have not
  been reconciled against the artwork Vit's currently holds. No file here is a
  production master.
- Every dashed frame is a **placeholder** — photography and art direction pending.
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
