"""Bind the three typefaces into the file itself.

PowerPoint matches a font by name, so a machine without Poppins, Urbanist and
League Spartan installed would fall back and re-flow every line. Each face goes
in as an embedded font part, which keeps the deck looking the same anywhere
while the text stays text.
"""
import io, re, shutil, zipfile, os

FONTS = '../fonts/'
# (typeface as written on the runs, slot, file)
FACES = [
    ('League Spartan',          'regular', 'LeagueSpartan-400.ttf'),
    ('League Spartan Medium',   'regular', 'LeagueSpartan-500.ttf'),
    ('League Spartan SemiBold', 'regular', 'LeagueSpartan-600.ttf'),
    ('Poppins Medium',          'regular', 'Poppins-500.ttf'),
    ('Poppins SemiBold',        'regular', 'Poppins-600.ttf'),
    ('Poppins',                 'bold',    'Poppins-700.ttf'),
    ('Urbanist',                'regular', 'Urbanist-400.ttf'),
    ('Urbanist Medium',         'regular', 'Urbanist-500.ttf'),
    ('Urbanist SemiBold',       'regular', 'Urbanist-600.ttf'),
]
NS = 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'


def embed(path):
    tmp = path + '.tmp'
    zin = zipfile.ZipFile(path)
    names = zin.namelist()
    ct = zin.read('[Content_Types].xml').decode('utf-8')
    rels = zin.read('ppt/_rels/presentation.xml.rels').decode('utf-8')
    pres = zin.read('ppt/presentation.xml').decode('utf-8')

    if 'fntdata' not in ct:
        ct = ct.replace('<Default Extension="xml"',
                        '<Default Extension="fntdata" ContentType="application/x-fontdata"/>'
                        '<Default Extension="xml"', 1)
    used = set(re.findall(r'Id="(rId\d+)"', rels))
    nxt = max([int(u[3:]) for u in used] or [0]) + 1

    lst, extra, rid = [], [], nxt
    for face, slot, fn in FACES:
        lst.append('<p:embeddedFont><p:font typeface="%s" pitchFamily="34" charset="0"/>'
                   '<p:%s r:id="rId%d"/></p:embeddedFont>' % (face, slot, rid))
        extra.append(('ppt/fonts/font%d.fntdata' % rid,
                      io.open(os.path.join(FONTS, fn), 'rb').read()))
        rels = rels.replace('</Relationships>',
                            '<Relationship Id="rId%d" Type="%s/font" '
                            'Target="fonts/font%d.fntdata"/></Relationships>'
                            % (rid, NS, rid), 1)
        rid += 1

    # the schema fixes where this goes: straight after the notes-slide size
    pres = re.sub(r'(<p:notesSz[^/]*/>)',
                  r'\1<p:embeddedFontLst>' + ''.join(lst) + '</p:embeddedFontLst>', pres, count=1)
    if 'embedTrueTypeFonts' not in pres:
        pres = pres.replace('<p:presentation ', '<p:presentation embedTrueTypeFonts="1" ', 1)

    with zipfile.ZipFile(tmp, 'w', zipfile.ZIP_DEFLATED) as zo:
        for n in names:
            data = zin.read(n)
            if n == '[Content_Types].xml':
                data = ct.encode('utf-8')
            elif n == 'ppt/_rels/presentation.xml.rels':
                data = rels.encode('utf-8')
            elif n == 'ppt/presentation.xml':
                data = pres.encode('utf-8')
            zo.writestr(n, data)
        for n, data in extra:
            zo.writestr(n, data)
    zin.close()
    shutil.move(tmp, path)
    return len(FACES)


if __name__ == '__main__':
    import sys
    f = sys.argv[1] if len(sys.argv) > 1 else 'IAQ-Company-Deck-2026.pptx'
    n = embed(f)
    print('embedded %d faces  %.1f MB' % (n, os.path.getsize(f) / 1e6))
