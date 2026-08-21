# ALTIGO Company Profile 2026 — Refinement Pass

Source: `ALTIGO_Company_Profile_2026.html` · 41 pages, single edition (was 43) · 2.39 MB (was 2.96 MB)

## Applied

### Consistency
- Company age standardised to **25 years / Since 2001** (was stated four ways: "20+",
  "twenty five years", "over two decades", "two and a half decades").
- Registration number now `562238-H` throughout (was `562238 H`).
- Cover pills: `Service` → `25 Years`, `Escalator & Lift` → `Lifts & Escalators`.

### Copy
- Positioning headline rewritten in the deck's own sharper voice (was "Your premier
  partner… where cutting edge innovation meets uncompromising safety").
- **Our Objective** reframed as five outward ambitions. It previously repeated
  Our Value almost item for item.
- Products page now ties the range to the EU type examined **TIGO-R** platform,
  which was orphaned on two certification pages.
- Market chart relabelled honestly as illustrative and unsourced.
- Track Record carries a source line for the 200+ / 98% / 25 figures.

### Structure
- **Removed "Our Success"** — it duplicated ~70% of Our Achievements. TOC and the
  Chapter 02 divider updated to match.
- **Standard/Full edition toggle removed** at the client's request; the deck ships as one
  41-page book. Nav control, CSS, the `setEdition` switcher and all 41 `data-tier`
  attributes are gone, and the grid overview no longer reads the toggle for its label.

### Design
- **Organisation chart built.** Was a "to be confirmed" placeholder. Directors named;
  everything below is by position, per brief. Safety & Compliance sits on a dashed
  line off the board spine to show independence.
- **Product Journey** rebuilt as a horizontal 7-stage process flow with a connector
  rail. It was a static 4x2 grid that hid the sequence.
- Each of the 8 chapter dividers now has its own glow geometry instead of one repeated.
- Signal red on dark surfaces lifted to `--red-d:#FF5A47` (~4.1:1 → ~6.1:1). Footer and
  certificate-note opacity raised.

### Production
- Images recompressed (WebP q82; the Target Market backdrop harder, since it renders at
  30% opacity under a veil). **614 KB saved**, no visible quality loss.
- Removed dead CSS (`.tile`, `.band`, `.fcard`, `.cover-img`, `.emblem`, empty spec-table
  comment). Scrubbed two "ported from OWND" comments referencing another client.
- Table-of-contents entries are now real `<button>`s — previously click-only `<div>`s.

### Iconography (client-directed)
- Custom inline-SVG icon set drawn in the deck's line style (1.6 stroke, round caps),
  inheriting the red/blue alternation through `currentColor` so no colour rules changed.
- Numerals replaced by icons on Target Market (8), The ALTIGO Difference (4), Our Value (6),
  Our Products (5), Service Scope (4), Maintenance Programme (4), Our Activities (6) and
  Product Journey (7). Certified Performance Range gained 6 spec icons.
- Heading marks beside Our Objective (burst), Our Aim (bullseye) and Our Value (diamond).
- Numerals kept where they carry real sequence and the client asked for them: Our Objective,
  Our Achievements, and the chapter dividers.
- Every icon now sits **beside** its title on one line rather than floating above it, at a
  single 44px across the whole book (38px only in the seven-up Product Journey columns).
- **All numbering is gone.** 36 remaining numerals across Our Objective, Our Achievements,
  Operating Footprint, Company Culture, Product Range I & II, Safety & Compliance,
  EU Type Examination, Our Aim and Brand USP were replaced with icons from a shared
  library, so the same concept always draws the same mark.
- Cards top-align, so every icon row in a grid shares a line.

### Later client edits
- Our Objective restored to the client's source wording (my earlier reframing reverted).
- Product Journey stages now carry a phase-of-life tag, pre construction through later life,
  so the row reads as a timeline rather than a list.
- ALTIGO x STADE page removed; chapter 05 is now "Activities". Its one remaining page was
  moved from the Full-only tier to Standard, otherwise chapter 05 would have been a divider
  with nothing behind it in the short edition.
- Our Products columns rebuilt on a shared grid. They were independent flex stacks, so a
  longer caption shrank that column's image and the row lost its baseline.

## Needs client input before this ships

1. **Duplicate testimonial.** Mr. Siew (Citra Embun) and Mr. Ong (Flamingo Hotel) are
   near word-for-word. Flagged in-source; needs the real wording. Not rewritten — putting
   invented words in a named client's mouth is not ours to do.
2. **Email.** Now shows the live `altigo@gmail.com`; `support@altigo.com` did not resolve.
   See the swap instructions in the HTML comment at the top of `<body>`.
3. **Website URL** — absent from all 42 pages.
4. **Response-time SLA** for the maintenance pages (e.g. 4h response / 1h entrapment).
5. **CIDB grade, SPKK, MOF registration** — needed for the government and developer
   sectors the deck targets first.
6. **Team size**, **safety record**, **ISO 9001/45001** if held.
7. **Project reference scope** — units, product type, year per project.
8. **A case study** — the single highest-value page still missing.
9. **KL and Negeri Sembilan addresses**; NS currently has no phone number.
10. **Client name spellings.** "Kwong Waai Siew" matches its public listing, so it is
    probably right as-is, but worth a confirm alongside "Komplek Adorna Gold".

## Corrections to the earlier review
Two findings in my first pass were wrong — they were artefacts of a truncated working copy:
- All 46 images **do** have `alt` attributes.
- `.prj-tag` **is** used (5 sector labels on the project references page).

### Round 14 — right-aligned leads, lift against the wall
- All 21 top-right description blocks now carry `.lead-r` (`text-align:right`), so every
  one of them ends flush on the right alignment guide at x=1800 (verified 0px short).
- Brand USP: the lift moved right to `right:36px` and up to `bottom:118px` at `height:516px`
  so it sits against the wall panel instead of floating in the middle of the shaft space.
- Open judgement point for the client: right-aligned body copy reads cleanly at 2–3 lines.
  The two 5-line blocks (Our Objective, Our Track Record) are the only ones where the ragged
  left edge is noticeable — say the word and those two revert to left-aligned.

### Round 15 — no short tail lines, bigger stat icons, tighter lists, tidier cards
- `.lead-r` now balances as well as right-aligns. Every one of the 21 top-right
  description blocks ends with at least 5 words on its last line (was as few as 2).
  `text-wrap:balance` also replaces `pretty` on every other paragraph in the deck.
- Standalone stat icons (`.tr-i`, `.cp-i`, `.gl-i`) go from 34px to 51px. Icons that
  sit beside a title stay at the standardised 34px.
- Maintenance Programme list gaps 98px → 78px; Safety & Compliance 66px → 53px.
- Six-up card grids (Our Value, Our Activities, Our Achievements): rows cut from 254px
  to 200px so the accent bars stop running past empty space, content stays top-aligned
  so titles and copy line up across the row.
- Tall card grids (Our Objective, Service Scope): rows capped at 300px / 400px so the
  caption is no longer stranded at the bottom of a void.
- Project references: `min-height` of two lines on `.prj h3`, so all five thumbnails
  end at the same height and the number/title/location rows line up.
- Brand USP lift moved right and up to sit against the wall panel.
- `TIGO-R` now uses a non-breaking hyphen so the model name never splits across lines.

Known and accepted: 13 body paragraphs in narrow card columns still end on a 2–3 word
line. Those columns are ~230px wide; at that measure it is a normal break and the lines
are already balanced. Fixing them further would mean rewriting client copy.

### Round 16 — Brand USP artwork and title mark
- Replaced the three separate images (blue panel, escalator cutout, lift cutout) with the
  single composite scene supplied by the client. It fills the right 980px of the slide,
  bleeding off the top and right, anchored to the bottom so the tiled floor stays whole.
- Text column pulled in (`frame right:1010px`) so the copy and page number stay clear of
  the escalator.
- Added a rising-arrow mark beside the Brand USP title, matching the treatment on
  Our Objective (46px `hd-mark`, blue frame with a red arrow breaking out of it).
- Cropped the supplied scene: the ragged tile apron and the white corner below the lift
  are gone (source trimmed to 1105x990 from 1189x1112), so the floor now meets the
  bottom edge of the slide on a clean straight line. Scene area widened to 1060px and
  the text column pulled to `right:1086px` to keep a gutter beside the page number.
- Brand USP scene widened to 1060 -> 1100px and anchored flush left (`object-position:0%`),
  so nothing is cropped off the escalator's tile apron; the trim now falls on the right,
  which is plain wall. Text column pulled to `right:1120px` to clear it.
- Page number moved out of the narrow footer to the slide's true bottom-right corner
  (right:120px, bottom:62px), matching every other page's guide position, in white with
  a soft shadow so it reads over the tiled floor.

## Round 17 — design uplift (client feedback: "quite normal", "backgrounds too simple")

Direction confirmed with the agency: rhythm rebuild, existing photography only, supporting
tints added. Client declined the three dark flips (p2, p8, p40) — those stay light.

**System**
- Palette gains `--ice #EDF2FF` (the middle surface), `--steel #C8D2E8` (hairlines, motif)
  and `--hair` / `--sh-card`. Brand red, blue and navy untouched.
- `--mist` deepened #F5F7FD → #E8EEFC. The old value sat ~4% off white, so cards never
  registered as objects. This was the single biggest cause of the "too simple" read.
- New `.t-ice` surface. It redefines `--mist`/`--paper` to white on itself, so every
  existing panel component keeps a real tonal step with no per-component rewrite.
- `.card` gains a steel hairline and a soft shadow on light surfaces; a hairline on dark.
- Two background devices, both behind all content (z-index 0, frame is 4):
  `.bg-shaft` — vertical rules on the deck's own 142px column guide, masked top and bottom.
  `.bg-field` — a soft corner tint, four positions (`f-tl/tr/bl/br`) plus an `f-red` variant,
  rotated page to page so neighbours never resolve the same way.

**Rhythm** — 22 pages reassigned. Ice: 3, 6, 8, 12, 15, 22, 24, 28, 33, 39.
Shaft: 3, 9, 16, 26. Field: 2, 4, 7, 13, 18, 23, 30, 32, 35.
No two adjacent pages now share a surface, except where a content page is followed by a
section divider (19/20 and 36/37), which is intentional.

**Per page**
- Testimonials: quote mark 52px → 78px, now a real design element.
- Product Journey: rail 2px → 3px and opacity .38 → .62 so it carries the eye.
- Market Statistics: the chart panel picks up the deepened mist automatically.

Not yet done from the plan: enlarging the lobby photo on Our Aim, scaling the product
photographs on Our Products, the certificate frame on EU Type Examination, and the steel
rule on Company Info & History.
