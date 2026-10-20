"""One file carrying the layouts, for reviewing them in a browser."""
import base64, io, mimetypes, os, re

D = '/home/user/Brand-Method-Website/iaq-deck/'
html = io.open(D + 'template.html', encoding='utf-8').read()
cache = {}


def dataurl(p, default='image/jpeg'):
    if p not in cache:
        mt = mimetypes.guess_type(p)[0] or default
        cache[p] = 'data:%s;base64,%s' % (mt, base64.b64encode(open(D + p, 'rb').read()).decode())
    return cache[p]


html = re.sub(r'src="(img/[^"]+)"', lambda m: 'src="%s"' % dataurl(m.group(1)), html)
html = re.sub(r'url\((img/[^)\'"]+)\)', lambda m: 'url(%s)' % dataurl(m.group(1), 'image/png'), html)

fcss = io.open(D + 'fonts.css', encoding='utf-8').read()
fcss = re.sub(r",url\(fonts/[^)]+\) format\('truetype'\)", '', fcss)
fcss = re.sub(r'url\((fonts/[^)]+\.woff2)\)',
              lambda m: 'url(data:font/woff2;base64,%s)'
              % base64.b64encode(open(D + m.group(1), 'rb').read()).decode(), fcss)
html = re.sub(r'<link rel="stylesheet" href="fonts\.css">',
              lambda m: '<style>\n%s\n</style>' % fcss, html)

out = D + 'template/IAQ-Master-Template-Layouts.html'
io.open(out, 'w', encoding='utf-8').write(html)
print('wrote %s  %.2f MB, %d files inlined' % (out, len(html.encode()) / 1e6, len(cache)))
