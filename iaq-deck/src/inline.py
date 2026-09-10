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
io.open(D+'IAQ-Company-Deck-2026.html','w',encoding='utf-8').write(html)
io.open('iaq-deck-standalone.html','w',encoding='utf-8').write(html)
print('standalone %.2f MB, %d assets inlined' % (len(html.encode())/1e6, len(cache)))
