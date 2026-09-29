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

# CSS backgrounds too: the running mark lives in a rule, not in the markup
def csssub(m):
    p = m.group(1)
    if p not in cache:
        mt = mimetypes.guess_type(p)[0] or 'image/png'
        cache[p] = 'data:%s;base64,%s' % (mt, base64.b64encode(open(D + p, 'rb').read()).decode())
    return 'url(%s)' % cache[p]
html = re.sub(r'url\((img/[^)\'"]+)\)', csssub, html)

# The three typefaces travel with the file. This deck is handed over as one
# document that has to open offline, so the latin faces beside it are carried
# inline rather than fetched.
fcss = io.open(D + 'fonts.css', encoding='utf-8').read()
def fsub(m):
    p = m.group(1)
    if p not in cache:
        cache[p] = ('data:font/woff2;base64,'
                    + base64.b64encode(open(D + p, 'rb').read()).decode())
    return 'url(%s)' % cache[p]
# only the woff2 source is inlined; the ttf fallback beside it would double the file
fcss = re.sub(r",url\(fonts/[^)]+\) format\('truetype'\)", '', fcss)
fonts = re.sub(r'url\((fonts/[^)]+\.woff2)\)', fsub, fcss)
html = re.sub(r'<link rel="stylesheet" href="fonts\.css">',
              lambda m: '<style>\n%s\n</style>' % fonts, html)

io.open(D+'IAQ-Company-Deck-2026.html','w',encoding='utf-8').write(html)
io.open('iaq-deck-standalone.html','w',encoding='utf-8').write(html)
print('standalone %.2f MB, %d files inlined' % (len(html.encode())/1e6, len(cache)))
