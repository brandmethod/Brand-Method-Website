# MyHero — Brand Creation (v0.1)

Brand creation deck for the MyHero / "My Health Record" app (Dr Amira · Elite Care Clinic).

- **Canvas:** 1920 × 1080 per page, 20 pages
- **Source:** `index.html` — open in a browser; pages scale to fit the window
- **Exports:** `exports/01.png` … `exports/20.png` (full-resolution 1920 × 1080)

## Cover format
Follows the house cover layout: master lockup → 3-line process headline with the brand
name in accent → category pill → deliverables line → golden-ratio spiral → twin footers.

## Status
The **logo system is marked IN PROGRESS** throughout. Sections 09–12 present three
temporary concept routes (Guardian / The Kept Record / Pulse); the shield mark used on
the cover is a placeholder drawn from Route A and has **not** been approved.

## Sourced from the 15 Aug 2026 kickstart notes
- Original colour scheme retained — sky blue primary, blush pink secondary
- Doctor hero icon must read professional, never cartoonish or gaming-style
- Positioned as a medical records app; AI is a secondary supporting technology
- Branding leads with the app's USP rather than personal branding
- Audience narrowed to young parents and mothers tracking a pregnancy at the clinic

## Regenerating the PNG exports
Requires Node with `playwright-core` and a Chromium build. Screenshot each `.canvas`
element at `index.html#export` (the `#export` hash disables the fit-to-window scaling).
