# MyHero — Brand Creation (v0.1)

Brand creation deck for the MyHero / "My Health Record" app (Dr Amira · Elite Care Clinic).

- **Canvas:** 1920 × 1080 per page, 44 pages
- **Source:** `index.html` — open in a browser; pages scale to fit the window
- **Exports:** `exports/01.png` … `exports/44.png` (full-resolution 1920 × 1080)

## Structure
Follows the Brand Method brand-creation format:

1. **Cover** — brand name + tagline, large "BRAND CREATION", golden-ratio spiral, description, twin footers
2. **Name Guide** *(blue divider — reference)* — name funnel, naming routes, real-world examples
3. **Logo Guide** *(blue divider — reference)* — logo creation, brand architecture, brand family,
   logo types, features & meaning, development, exploration, art style, detailing, concept
   direction, logo refinement, logo system & colour, system, brandscape, modules & family
4. **Stylescape Guide** *(blue divider — reference)* — the three-tier method
5. **Brand Foundation** *(black divider — client)* — name, why the name, positioning,
   brand architecture, hierarchy tree, tagline test, competitor analysis
6. **Reference** *(black divider — client)* — competitor, content and design reference
7. **Stylescape** *(black divider — client)* — MID tier, recommended direction
8. **Logo Ideation** *(black divider — client)* — concept/element, combo/build, sketch/shape,
   founder concept, logo system drafts, next steps

Blue dividers mark generic reference sections; black dividers mark MyHero-specific work.
The guide sections are deliberately kept generic — they are standing reference material
shown to inform the client, and carry no MyHero-specific commentary.

## Viewing and refining
Open `index.html` in any browser. Pages scale to fit the window.
**Contents** (bottom right) opens a jump-to-page index; arrow keys page through.
Append `#export` to the URL to disable scaling and hide the viewer chrome.

## Status
The **logo system is in progress**. All marks shown are placeholder geometry from the
Guardian route; no route has been selected. Third-party brands are cited by name as
written examples only — no third-party logos are reproduced.

## Sourced from the 15 Aug 2026 kickstart notes
- Original colour scheme retained — sky blue primary, blush pink secondary
- Doctor hero icon must read professional, never cartoonish or gaming-style
- Positioned as a medical records app; AI is a secondary supporting technology
- Branding leads with the app's USP rather than personal branding
- Audience narrowed to young parents and mothers tracking a pregnancy at the clinic

## Regenerating the PNG exports
Requires Node with `playwright-core` and a Chromium build. Screenshot each `.canvas`
element at `index.html#export` (the `#export` hash disables the fit-to-window scaling).
