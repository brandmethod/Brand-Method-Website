"""Put the master template inside the deck.

The presentation keeps every page it has. The layouts go into its slide
master, so New Slide offers them by name and a new page comes out as IAQ
without anyone styling it.
"""
import copy, io, json, os, re, zipfile
from lxml import etree
import potx
from potx import q, A, P, R, layout_xml, to_placeholder, slide_number, theme_iaq

DECK = '/home/user/Brand-Method-Website/iaq-deck/IAQ-Company-Deck-2026.pptx'
TPL = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   'IAQ-Master-Template-2026.pptx')
INDEX = '/home/user/Brand-Method-Website/iaq-deck/template/layouts.json'
CT_LAYOUT = ('application/vnd.openxmlformats-officedocument.presentationml'
             '.slideLayout+xml')


def slide_paths(z):
    pres = etree.fromstring(z.read('ppt/presentation.xml'))
    rels = etree.fromstring(z.read('ppt/_rels/presentation.xml.rels'))
    rmap = {r.get('Id'): r.get('Target') for r in rels}
    return ['ppt/' + rmap[s.get(q('r:id'))] for s in pres.find(q('p:sldIdLst'))]


def layouts_from(tpl, names, media_at):
    """Each template page becomes a layout; its pictures are renumbered so they
    can live beside the deck's own media."""
    z = zipfile.ZipFile(tpl)
    pages = slide_paths(z)[1:]          # page one is the contents, not a layout
    assert len(pages) == len(names), (len(pages), len(names))
    out, media = [], {}
    nextimg = media_at
    for path, name in zip(pages, names):
        slide = etree.fromstring(z.read(path))
        rels = etree.fromstring(z.read(path.replace('slides/', 'slides/_rels/') + '.rels'))
        rmap = {r.get('Id'): r.get('Target') for r in rels}
        tree = slide.find(q('p:cSld')).find(q('p:spTree'))
        kids = [k for k in tree if k.tag in (q('p:sp'), q('p:pic'))]

        texts = []
        for k in kids:
            if k.tag != q('p:sp'):
                continue
            t = ''.join(e.text or '' for e in k.iter(q('a:t'))).strip()
            sz = max([int(e.get('sz', 0)) for e in k.iter() if e.get('sz')] or [0])
            if t:
                texts.append((k, t, sz))
        title_sp = next((k for k, t, _ in texts if t == 'Page title'), None)
        if title_sp is None and texts:
            title_sp = max(texts, key=lambda x: x[2])[0]

        shapes, idx, sid, rid = [], 20, 2, 2
        newrels = ['<Relationship Id="rId1" Type="%s/slideMaster" '
                   'Target="../slideMasters/slideMaster1.xml"/>' % R]
        for k in kids:
            sid += 1
            if k.tag == q('p:pic'):
                blip = k.find('.//' + q('a:blip'))
                if blip is not None:
                    src = os.path.normpath(os.path.join('ppt/slides',
                                                        rmap[blip.get(q('r:embed'))]))
                    ext = os.path.splitext(src)[1]
                    tgt = 'image%d%s' % (nextimg, ext)
                    media.setdefault(tgt, z.read(src.replace('\\', '/')))
                    nextimg += 1
                    blip.set(q('r:embed'), 'rId%d' % rid)
                    newrels.append('<Relationship Id="rId%d" Type="%s/image" '
                                   'Target="../media/%s"/>' % (rid, R, tgt))
                    rid += 1
                k.find(q('p:nvPicPr')).find(q('p:cNvPr')).set('id', str(sid))
                shapes.append(k)
                continue
            t = ''.join(e.text or '' for e in k.iter(q('a:t'))).strip()
            if not t:
                k.find(q('p:nvSpPr')).find(q('p:cNvPr')).set('id', str(sid))
                shapes.append(k)
                continue
            box = k.find(q('p:spPr')).find(q('a:xfrm'))
            off = box.find(q('a:off')) if box is not None else None
            x = int(off.get('x')) if off is not None else 0
            y = int(off.get('y')) if off is not None else 0
            if t.isdigit() and y > 6000000 and x < 2000000:
                potx.FOLIO.append(slide_number(copy.deepcopy(k), 9))
                continue
            if k is title_sp:
                shapes.append(to_placeholder(k, 0, 'title', sid, 'Title'))
            else:
                shapes.append(to_placeholder(k, idx, 'body', sid, 'Text %d' % (idx - 19)))
                idx += 1
        out.append((name, layout_xml(shapes, 'IAQ · ' + name), newrels))
    return out, media


def combine(out_path):
    names = [x['name'] for x in json.load(io.open(INDEX, encoding='utf-8'))]
    zd = zipfile.ZipFile(DECK)
    have = [n for n in zd.namelist() if n.startswith('ppt/media/')]
    nextimg = max([int(m.group(1)) for m in
                   (re.search(r'image(\d+)', n) for n in have) if m] or [0]) + 1
    layouts, media = layouts_from(TPL, names, nextimg)

    # PowerPoint's own eleven starter layouts would sit in the same menu and
    # give an off-brand page, so only the one the deck's pages are built on stays
    used = set()
    for sp in slide_paths(zd):
        rels = etree.fromstring(zd.read(sp.replace('slides/', 'slides/_rels/') + '.rels'))
        for r in rels:
            if r.get('Type').endswith('/slideLayout'):
                used.add(os.path.basename(r.get('Target')))
    allv = sorted(n for n in zd.namelist()
                  if re.match(r'ppt/slideLayouts/slideLayout\d+\.xml$', n))
    drop = {os.path.basename(n) for n in allv} - used
    first = len(allv) + 1

    master = etree.fromstring(zd.read('ppt/slideMasters/slideMaster1.xml'))
    tree = master.find(q('p:cSld')).find(q('p:spTree'))
    for sp in list(tree.findall(q('p:sp'))):
        ph = sp.find('.//' + q('p:ph'))
        if ph is not None and ph.get('type') in ('dt', 'ftr', 'sldNum'):
            tree.remove(sp)
    if potx.FOLIO:
        tree.append(copy.deepcopy(potx.FOLIO[0]))
    mrels = etree.fromstring(zd.read('ppt/slideMasters/_rels/slideMaster1.xml.rels'))
    rid = max(int(r.get('Id')[3:]) for r in mrels) + 1
    gone = {r.get('Id') for r in mrels
            if r.get('Type').endswith('/slideLayout')
            and os.path.basename(r.get('Target')) in drop}
    lst = master.find(q('p:sldLayoutIdLst'))
    for e in list(lst):
        if e.get(q('r:id')) in gone:
            lst.remove(e)
    base = max(int(e.get('id')) for e in lst) + 1
    rel_add = []
    for i, (name, _, _) in enumerate(layouts):
        e = etree.SubElement(lst, q('p:sldLayoutId'))
        e.set('id', str(base + i))
        e.set(q('r:id'), 'rId%d' % (rid + i))
        rel_add.append('<Relationship Id="rId%d" Type="%s/slideLayout" '
                       'Target="../slideLayouts/slideLayout%d.xml"/>'
                       % (rid + i, R, first + i))

    mrels_xml = zd.read('ppt/slideMasters/_rels/slideMaster1.xml.rels').decode('utf-8')
    for rid_gone in gone:
        mrels_xml = re.sub(r'<Relationship Id="%s"[^>]*/>' % rid_gone, '', mrels_xml)
    mrels_xml = mrels_xml.replace('</Relationships>', ''.join(rel_add) + '</Relationships>')

    ct = zd.read('[Content_Types].xml').decode('utf-8')
    for name in drop:
        ct = re.sub(r'<Override PartName="/ppt/slideLayouts/%s"[^>]*/>' % name, '', ct)
    adds = ''.join('<Override PartName="/ppt/slideLayouts/slideLayout%d.xml" '
                   'ContentType="%s"/>' % (first + i, CT_LAYOUT)
                   for i in range(len(layouts)))
    for ext, mime in (('png', 'image/png'), ('jpeg', 'image/jpeg'), ('jpg', 'image/jpeg')):
        if 'Extension="%s"' % ext not in ct:
            adds += '<Default Extension="%s" ContentType="%s"/>' % (ext, mime)
    ct = ct.replace('</Types>', adds + '</Types>')

    with zipfile.ZipFile(out_path, 'w', zipfile.ZIP_DEFLATED) as z:
        for n in zd.namelist():
            if os.path.basename(n).replace('.rels', '') in drop and 'slideLayout' in n:
                continue
            if n == '[Content_Types].xml':
                z.writestr(n, ct)
            elif n == 'ppt/slideMasters/slideMaster1.xml':
                z.writestr(n, etree.tostring(master, xml_declaration=True,
                                             encoding='UTF-8', standalone=True))
            elif n == 'ppt/slideMasters/_rels/slideMaster1.xml.rels':
                z.writestr(n, mrels_xml)
            elif os.path.basename(n) in used and 'slideLayouts/' in n:
                lay = etree.fromstring(zd.read(n))
                lay.find(q('p:cSld')).set('name', 'IAQ \u00b7 Blank page')
                z.writestr(n, etree.tostring(lay, xml_declaration=True,
                                             encoding='UTF-8', standalone=True))
            elif n.startswith('ppt/theme/theme1.xml'):
                z.writestr(n, theme_iaq(zd.read(n)))
            else:
                z.writestr(n, zd.read(n))
        for i, (name, xml, rels) in enumerate(layouts):
            z.writestr('ppt/slideLayouts/slideLayout%d.xml' % (first + i),
                       etree.tostring(xml, xml_declaration=True, encoding='UTF-8',
                                      standalone=True))
            z.writestr('ppt/slideLayouts/_rels/slideLayout%d.xml.rels' % (first + i),
                       '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                       '<Relationships xmlns="http://schemas.openxmlformats.org/package'
                       '/2006/relationships">' + ''.join(rels) + '</Relationships>')
        for name, data in media.items():
            z.writestr('ppt/media/' + name, data)
    return out_path


if __name__ == '__main__':
    out = combine('IAQ-Company-Deck-2026-Template.pptx')
    print('wrote %s  %.1f MB' % (out, os.path.getsize(out) / 1e6))
