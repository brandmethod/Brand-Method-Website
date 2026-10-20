"""One file: the company deck, then the master template behind it.

The layouts are wired into the slide master so New Slide offers them, but a
menu nobody finds is a menu that does not exist. The template pages are also
appended as real pages, hidden from the slideshow, so they are there in the
panel to copy from.
"""
import io, re

D = '/home/user/Brand-Method-Website/iaq-deck/'
OUT = D + 'deck-with-template.html'
STAGE = re.compile(r'<div class="stage">.*?</section></div>', re.S)


def stages(path):
    return STAGE.findall(io.open(path, encoding='utf-8').read())


deck = stages(D + 'index.html')
tpl = stages(D + 'template-empty.html')
print('deck %d pages, template %d pages' % (len(deck), len(tpl)))

# the appended pages carry on the deck's own numbering
out = []
for i, s in enumerate(tpl, len(deck) + 1):
    out.append(re.sub(r'(<span class="folio">)\d+(</span>)', r'\g<1>%02d\g<2>' % i, s, count=1))

CSS = (io.open(D + 'deck.css', encoding='utf-8').read() + '\n'
       + io.open(D + 'src/tpl.css', encoding='utf-8').read())
JS = io.open(D + 'deck.js', encoding='utf-8').read()

doc = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>IAQ Total Facility Solutions</title>
<meta name="description" content="IAQ Technology International Sdn Bhd presentation deck, with the master template behind it.">
<link rel="stylesheet" href="fonts.css">
<style>
{CSS}
</style>
</head>
<body>
<div class="deck">
{chr(10).join(deck + out)}
</div>
<script>
{JS}
</script>
</body>
</html>'''
io.open(OUT, 'w', encoding='utf-8').write(doc)
print('wrote %s - %d pages, %d KB' % (OUT, len(deck) + len(out), len(doc.encode()) // 1024))
print('template pages are %d to %d' % (len(deck) + 1, len(deck) + len(out)))
