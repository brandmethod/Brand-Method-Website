---
name: no-orphan-lines
description: Stop paragraphs ending on a one-to-three-word line (orphans/widows) in HTML decks, documents and page layouts. Use whenever writing or editing body copy, leads, card descriptions, bullets or labels that will wrap - and always before shipping a layout for client review.
---

# No orphan lines

A block of copy must never end with a line carrying only one to three words.
A stranded "partner." or "specification." under a full paragraph reads as a
mistake and is the single most common thing clients flag in a layout.

## The rule

**Every wrapped block's last line carries four or more words.**

Applies to paragraphs, leads, card descriptions, bullets, captions, table
cells and labels - anything that wraps. A block that fits on one line is
fine; the rule only bites once it wraps.

## How to fix it

Preferred, in order:

1. **Bind the trailing words** with non-breaking spaces so they cannot be
   split off:
   `...delivered as&nbsp;one&nbsp;accountable&nbsp;partner.`
   Bind the last four words. This pulls extra words down onto the last line
   rather than pushing text around.

2. **Edit the copy** - cut or add a word or two so it wraps cleanly. Often
   the best answer for headings and short labels.

3. **`text-wrap: balance`** for short label-type blocks of three to four
   words in a narrow cell, where four words on the last line is impossible.
   It splits the lines evenly (2 + 2) instead of orphaning one word.

4. **`text-wrap: pretty`** on prose as a general safety net. It only
   prevents single-word orphans, so it supplements binding - it does not
   replace it.

## Watch the width

A bound run cannot break, so it will overflow a container narrower than the
run. Scale how much you bind to the column width:

| Block | Bind up to |
|---|---|
| Full-measure prose (leads, body, callouts) | ~46 characters |
| Half-measure cards, bullets, list rows | ~34-40 characters |
| Narrow stat and label cells | ~26-30 characters |

If four words exceed the cap, bind three, then two. If even two exceed it,
leave the block alone and fix the copy or use `text-wrap: balance`.

Never bind a whole block end to end unless the entire block fits inside the
cap - otherwise it becomes one unbreakable run and overflows.

## Verify, don't eyeball

Measure the rendered result rather than trusting the markup. Walk each text
node, wrap every word in a `Range`, read `getBoundingClientRect().top`,
group words by that top to get lines, and check the last group's length:

```js
const walker = document.createTreeWalker(el, NodeFilter.SHOW_TEXT);
const words = []; let n;
while ((n = walker.nextNode())) {
  for (const m of n.textContent.matchAll(/\S+/g)) {
    const r = document.createRange();
    r.setStart(n, m.index); r.setEnd(n, m.index + m[0].length);
    const box = r.getBoundingClientRect();
    if (box.width || box.height) words.push({ w: m[0], top: Math.round(box.top) });
  }
}
const lastTop = words.at(-1).top;
const lastLine = words.filter(w => w.top === lastTop);   // want >= 4
```

Also check for horizontal overflow afterwards (`scrollWidth > clientWidth`)
- that is how an over-long bound run shows up.

## Entities and inline markup

- Count an HTML entity (`&amp;`, `&middot;`) as **one** glyph when measuring
  a run, not as its five or eight source characters.
- Bind **across** inline tags. `...into a <b>Total Facility Solutions
  Provider</b>.` needs the non-breaking spaces placed inside the `<b>`, or
  the trailing text run is just `.` and nothing binds.
