# ALTIGO Company Profile 2026 — Refinement Pass

Source: `ALTIGO_Company_Profile_2026.html` · 42 pages (was 43) · 2.35 MB (was 2.96 MB)

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
- **Standard/Full tiering inverted.** Standard (34 pp) now keeps Safety & Compliance,
  Certified Performance Range and EU Type Examination — previously it dropped exactly
  those and kept the generic value grids.

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
