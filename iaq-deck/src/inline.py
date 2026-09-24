import base64, io, os, re, mimetypes
D='/home/user/Brand-Method-Website/iaq-deck/'
html=io.open(D+'index.html',encoding='utf-8').read()
css=io.open(D+'deck.css',encoding='utf-8').read()
js=io.open(D+'deck.js',encoding='utf-8').read()
# lambda replacements: the CSS/JS may contain backslashes that re would
# otherwise read as template escapes
html=re.sub(r'<link[^>]+href="deck\.css"[^>]*>', lambda m: '<style>\n%s\n</style>'%css, html)
html=re.sub(r'<script[^>]+src="deck\.js"[^>]*></script>', lambda m: '<script>\n%s\n</script>'%js, html)
cache={}
def sub(m):
    p=m.group(1)
    if p not in cache:
        mt=mimetypes.guess_type(p)[0] or 'image/jpeg'
        cache[p]='data:%s;base64,%s'%(mt, base64.b64encode(open(D+p,'rb').read()).decode())
    return 'src="%s"'%cache[p]
html=re.sub(r'src="(img/[^"]+)"', sub, html)

# The three typefaces travel with the file. Google Fonts is a network call,
# and this deck is handed over as one document that has to open offline, so
# the latin and latin-ext faces are fetched once and carried inline. The
# other subsets (cyrillic, greek, vietnamese) are not used by the deck.
FONT_CSS = 'fonts.css'
KEEP = ('/* latin */',)
faces, fcache = [], {}
block = None
for chunk in io.open(FONT_CSS, encoding='utf-8').read().split('@font-face'):
    head = chunk.strip().splitlines()[-1].strip() if chunk.strip() else ''
    if block is not None and block in KEEP:
        faces.append('@font-face' + chunk[:chunk.rindex('}') + 1])
    block = head if head.startswith('/*') else None
def wsub(m):
    u = m.group(1)
    if u not in fcache:
        import urllib.request
        fcache[u] = ('data:font/woff2;base64,'
                     + base64.b64encode(urllib.request.urlopen(u).read()).decode())
    return 'url(%s)' % fcache[u]
fonts = re.sub(r'url\((https://fonts\.gstatic\.com/[^)]+)\)', wsub, ''.join(faces))
html = re.sub(r'<link rel="preconnect"[^>]*>\s*', '', html)
html = re.sub(r'<link rel="stylesheet" href="https://fonts\.googleapis\.com[^"]*"[^>]*>',
              lambda m: '<style>\n%s\n</style>' % fonts, html)

io.open(D+'IAQ-Company-Deck-2026.html','w',encoding='utf-8').write(html)
io.open('iaq-deck-standalone.html','w',encoding='utf-8').write(html)
print('standalone %.2f MB, %d images + %d font files inlined'
      % (len(html.encode())/1e6, len(cache), len(fcache)))
