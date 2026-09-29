# The deck as a PowerPoint file

`IAQ-Company-Deck-2026.pptx` is not an export of pictures. Every slide is rebuilt
out of native PowerPoint objects, so the client can retype a line, move a card or
recolour a chip without the layout coming apart.

The HTML deck stays the master. These four steps read it and replay it:

| step | what it does |
|---|---|
| `extract.js` + `extract.py` | walk each slide's DOM at 1920 x 1080 and record every box, picture, icon and line of type, with its measured position, fill, border and font |
| `rasterize.py` | draw each inline SVG (the icons and the flags) to a PNG at four times its size |
| `emit.py` | replay those primitives as PowerPoint shapes, pictures and text boxes |
| `embed.py` | bind the nine faces into the file so it reads the same on a machine that has never seen them |

Run the first three with `./build.sh`, then `python3 embed.py`.

## What the file carries

- 67 slides at 13.333 x 7.5 in, the deck's own proportion.
- Text as text: real runs, real font names, real sizes and colours. Nothing is outlined.
- Photographs and certificates as embedded pictures, cropped the way the design crops them.
- Icons and flags as transparent PNGs at 4x, sharp at any projection size.
- Poppins, Urbanist and League Spartan embedded (nine faces, all licensed for embedding).

## If the type ever looks wrong

PowerPoint for Windows reads the embedded faces. PowerPoint for Mac ignores them,
so install the fonts once from `IAQ-Deck-Fonts.zip` beside the deck and reopen the file.

## Checks worth repeating after an edit to the pipeline

- `python3 textcheck.py` - every word on screen survived into the primitives.
- `validate.py IAQ-Company-Deck-2026.pptx` - the package is well formed.
- Render to PDF and compare against the HTML slides; the QR codes on the contacts
  page should still decode out of the render.
