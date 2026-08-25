# Agensia Brand Creation

Source for `Agensia_Brand_Creation.html` at the repository root. The deck follows the
MyHero Brand Creation format exactly: 1920 x 1080 slides, a blue Method divider section
of Brand Method reference pages, then black client dividers for Brand Foundation,
Reference, Stylescape and Logo Ideation. 58 slides, same page numbering as the reference.

## Build

    python3 src/agensia-brand-creation/build.py

Fragments are concatenated in the order listed in `build.py`. The build fails rather
than shipping a glyph the subsetted brand fonts cannot render.

## Assets

`assets/fonts.css` and `assets/symbol-path.txt` are lifted from Agensia Brand Book V3.0,
so the deck reproduces the confirmed identity rather than approximating it:

- **Fonts** Ardela (display and wordmark), Axiforma (text), Inter (interface),
  JetBrains Mono (technical). All subsetted to basic Latin, which is why the build
  rejects em and en dashes.
- **AgDot** is JetBrains Mono restricted to `U+00B7` and placed first in the text stack.
  Axiforma and Inter sit their middle dot on the baseline, where it reads as a full stop;
  serving that one codepoint from Mono centres it.
- **Symbol** one path, `fill="currentColor"` so `color:` recolours it, used via
  `<use href="#i-ag">` so the 28 KB of contour geometry is paid for once.

## Brand rules the deck holds itself to

- Agensia Green is a signal: the mark and one call to action per surface. It never
  carries text on a light ground (1.7:1) and never indicates a status. Green text uses
  Green Deep `#6FA800`.
- Depth in the mark comes from line density alone, never a gradient or a shadow.
- Ardela Edge is a display face and is never set as a paragraph.

## Checking a change

`build.py` warns if page numbers fall out of document order. To catch layout overflow,
render with Playwright against `#export` and compare each `.canvas` scrollHeight to 1080.
