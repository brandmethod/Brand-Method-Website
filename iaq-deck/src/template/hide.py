"""The template pages are in the deck to copy from, not to present, so they
are hidden from the slideshow."""
import re, sys, zipfile
from lxml import etree

P = 'http://schemas.openxmlformats.org/presentationml/2006/main'
R = 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'


def hide(path, first):
    z = zipfile.ZipFile(path)
    pres = etree.fromstring(z.read('ppt/presentation.xml'))
    rels = etree.fromstring(z.read('ppt/_rels/presentation.xml.rels'))
    rmap = {r.get('Id'): r.get('Target') for r in rels}
    order = ['ppt/' + rmap[s.get('{%s}id' % R)]
             for s in pres.find('{%s}sldIdLst' % P)]
    targets = set(order[first - 1:])
    out = path + '.tmp'
    with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED) as w:
        for n in z.namelist():
            d = z.read(n)
            if n in targets:
                s = d.decode('utf-8')
                if 'show=' not in s[:400]:
                    s = re.sub(r'(<p:sld\b[^>]*?)(>)', r'\1 show="0"\2', s, count=1)
                d = s.encode('utf-8')
            w.writestr(n, d)
    z.close()
    import os, shutil
    shutil.move(out, path)
    return len(targets)


if __name__ == '__main__':
    n = hide(sys.argv[1], int(sys.argv[2]))
    print('hid %d pages from the slideshow' % n)
