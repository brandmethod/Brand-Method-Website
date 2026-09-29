"""Replay the extracted slide geometry as native PowerPoint shapes.

Every box, picture and line of type on the deck becomes a real object: nothing
is flattened to an image, so the text stays editable and the layout stays where
the design put it.
"""
import io, json, os, re, copy
from pptx import Presentation
from pptx.util import Emu, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR, MSO_AUTO_SIZE
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.dml import MSO_LINE_DASH_STYLE
from pptx.oxml.ns import qn
from PIL import Image

PX = 6350                      # 1920 px across a 13.333 in slide
PT = 0.5                       # 1 css px = 0.5 pt at this slide size
DECK = '/home/user/Brand-Method-Website/iaq-deck/'

def emu(v): return Emu(int(round(v * PX)))
def col(c): return RGBColor(c['r'], c['g'], c['b'])

# Google ships each weight as its own family, which is what PowerPoint matches on
FAMILY = {
    ('poppins', 500): ('Poppins Medium', False), ('poppins', 600): ('Poppins SemiBold', False),
    ('poppins', 700): ('Poppins', True),
    ('urbanist', 400): ('Urbanist', False), ('urbanist', 500): ('Urbanist Medium', False),
    ('urbanist', 600): ('Urbanist SemiBold', False), ('urbanist', 700): ('Urbanist SemiBold', True),
    ('league spartan', 400): ('League Spartan', False),
    ('league spartan', 500): ('League Spartan Medium', False),
    ('league spartan', 600): ('League Spartan SemiBold', False),
}

def font_for(ff, fw):
    fam = ff.split(',')[0].strip().strip('"\'').lower()
    try:
        w = int(fw)
    except ValueError:
        w = 700 if fw == 'bold' else 400
    w = min((k[1] for k in FAMILY if k[0] == fam), key=lambda x: abs(x - w), default=w) \
        if any(k[0] == fam for k in FAMILY) else w
    return FAMILY.get((fam, w), ('Arial', w >= 600))

def noline(sh):
    sh.line.fill.background()
    sh.shadow.inherit = False
    # the theme's style reference would put its own outline, fill and drop shadow
    # back on top of what we set here
    st = sh._element.find(qn('p:style'))
    if st is not None:
        sh._element.remove(st)

def add_rect(sl, x, y, w, h, fill, radius=0):
    # a radius of half the shorter side is a circle, not a rounded box
    if radius >= min(w, h) / 2 - 0.5 and radius > 0.5:
        shape = MSO_SHAPE.OVAL
    elif radius > 0.5:
        shape = MSO_SHAPE.ROUNDED_RECTANGLE
    else:
        shape = MSO_SHAPE.RECTANGLE
    shp = sl.shapes.add_shape(shape, emu(x), emu(y), emu(w), emu(h))
    if fill is None:
        shp.fill.background()
    else:
        shp.fill.solid(); shp.fill.fore_color.rgb = col(fill)
        if fill.get('a', 1) < 0.99:
            a = shp.fill.fore_color._xFill.find(qn('a:srgbClr'))
            el = a.makeelement(qn('a:alpha'), {'val': str(int(fill['a'] * 100000))})
            a.append(el)
    if shape == MSO_SHAPE.ROUNDED_RECTANGLE:
        try:
            shp.adjustments[0] = min(0.5, radius / min(w, h))
        except Exception:
            pass
    noline(shp)
    return shp

def place_picture(sl, path, x, y, w, h, fit='fill', pad=(0, 0, 0, 0)):
    """object-fit: cover crops to the box, contain is letterboxed inside it."""
    pt, pr, pb, pl = [p or 0 for p in pad]
    x, y, w, h = x + pl, y + pt, w - pl - pr, h - pt - pb
    if w <= 0 or h <= 0:
        return None
    try:
        nw, nh = Image.open(path).size
    except Exception:
        return None
    if fit == 'contain':
        s = min(w / nw, h / nh)
        cw, ch = nw * s, nh * s
        return sl.shapes.add_picture(path, emu(x + (w - cw) / 2), emu(y + (h - ch) / 2),
                                     emu(cw), emu(ch))
    pic = sl.shapes.add_picture(path, emu(x), emu(y), emu(w), emu(h))
    if fit == 'cover':
        s = max(w / nw, h / nh)
        rw, rh = nw * s, nh * s
        if rw > w + .5:
            f = (rw - w) / rw / 2; pic.crop_left = f; pic.crop_right = f
        if rh > h + .5:
            f = (rh - h) / rh / 2; pic.crop_top = f; pic.crop_bottom = f
    return pic

def add_text(sl, it):
    pt_, pr, pb, pl = it['pad']
    box = sl.shapes.add_textbox(emu(it['x']), emu(it['y']), emu(it['w']), emu(it['h']))
    tf = box.text_frame
    tf.word_wrap = not it.get('one')   # a line that fits in the browser must not re-wrap here
    tf.auto_size = MSO_AUTO_SIZE.NONE
    tf.margin_left, tf.margin_right = emu(pl), emu(pr)
    tf.margin_top, tf.margin_bottom = emu(pt_), emu(pb)
    # the box is the measured line box, so centring in it lands the type where the
    # browser put it whatever the renderer's own leading works out to
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE if it.get('mid') else MSO_ANCHOR.TOP
    align = {'start': PP_ALIGN.LEFT, 'left': PP_ALIGN.LEFT, 'center': PP_ALIGN.CENTER,
             'end': PP_ALIGN.RIGHT, 'right': PP_ALIGN.RIGHT}.get(it['align'], PP_ALIGN.LEFT)

    paras = [[]]
    for r in it['runs']:
        for i, chunk in enumerate(r['t'].split('\n')):
            if i:
                paras.append([])
            if chunk:
                paras[-1].append({'t': chunk, 's': r['s']})
    first = True
    for pruns in paras:
        p = tf.paragraphs[0] if first else tf.add_paragraph()
        first = False
        p.alignment = align
        # one line needs no exact spacing: centring it in its measured box places it,
        # and an exact value shorter than the face's own leading shifts the glyphs
        if it['lh'] and not (it.get('one') and it.get('mid')):
            lp = p._pPr if p._pPr is not None else p._p.get_or_add_pPr()
            ln = lp.makeelement(qn('a:lnSpc'), {})
            pts = ln.makeelement(qn('a:spcPts'), {'val': str(int(it['lh'] * PT * 100))})
            ln.append(pts); lp.insert(0, ln)
        for rn in pruns:
            s = rn['s']
            txt = rn['t']
            if s.get('tt') == 'uppercase':
                txt = txt.upper()
            run = p.add_run()
            run.text = txt
            fam, bold = font_for(s['ff'], s['fw'])
            f = run.font
            f.name = fam
            f.size = Pt(max(1, round(s['fs'] * PT, 1)))
            f.bold = bold
            f.italic = s.get('it') == 'italic'
            if s['col']:
                f.color.rgb = col(s['col'])
            rPr = run._r.get_or_add_rPr()
            if s['col'] and s['col'].get('a', 1) < 0.99:
                sc = rPr.find(qn('a:solidFill')).find(qn('a:srgbClr'))
                sc.append(sc.makeelement(qn('a:alpha'),
                                         {'val': str(int(s['col']['a'] * 100000))}))
            if s.get('ls'):
                rPr.set('spc', str(int(round(s['ls'] * PT * 100))))
            # name the same face for latin, east-asian and complex scripts.
            # rPr children follow a fixed order in the schema: latin, ea, cs.
            prev = rPr.find(qn('a:latin'))
            if prev is None:
                prev = rPr.makeelement(qn('a:latin'), {}); rPr.append(prev)
            prev.set('typeface', fam)
            for tag in ('a:ea', 'a:cs'):
                e = rPr.find(qn(tag))
                if e is None:
                    e = rPr.makeelement(qn(tag), {}); prev.addnext(e)
                e.set('typeface', fam)
                prev = e
    return box

BIMG = re.compile(r'url\("?file://([^")]+)"?\)')

RLG = re.compile(r'repeating-linear-gradient\(((?:[^()]|\([^()]*\))*)\)')
CSSC = re.compile(r'rgba?\(([^)]*)\)')

def _stop(part):
    m = CSSC.search(part)
    if not m:
        return None, None
    v = [float(n) for n in m.group(1).split(',')]
    c = {'r': int(v[0]), 'g': int(v[1]), 'b': int(v[2]), 'a': v[3] if len(v) > 3 else 1}
    n = re.search(r'(-?[\d.]+)px', part[m.end():])
    return c, (float(n.group(1)) if n else None)

def ruled(bimg, x, y, w, h):
    """The cover's blueprint grid is a repeating gradient: replay it as its lines."""
    out = []
    for m in RLG.finditer(bimg):
        parts = [p.strip() for p in re.split(r',(?![^(]*\))', m.group(1))]
        vertical = False
        if parts and 'deg' in parts[0] and 'rgb' not in parts[0]:
            vertical = abs(float(parts[0].replace('deg', '').strip()) - 90) < 1
            parts = parts[1:]
        if len(parts) < 3:
            continue
        c, _ = _stop(parts[0])
        _, t = _stop(parts[1])
        _, period = _stop(parts[-1])
        if not c or not t or not period or period < 4 or c.get('a', 1) < 0.01:
            continue
        span = w if vertical else h
        k = 0
        while k * period < span - 0.5:
            o = k * period
            out.append((x + o, y, t, h) if vertical else (x, y + o, w, t))
            k += 1
    return out


def build(data, out):
    prs = Presentation()
    prs.slide_width, prs.slide_height = emu(1920), emu(1080)
    blank = prs.slide_layouts[6]
    for s in data:
        sl = prs.slides.add_slide(blank)
        for it in s['items']:
            k = it['k']
            if k == 'rect':
                bimg = it.get('bimg') or ''
                m = BIMG.search(bimg)
                if m:
                    place_picture(sl, m.group(1), it['x'], it['y'], it['w'], it['h'], 'contain')
                    continue
                if 'repeating-linear-gradient' in bimg:
                    for lx, ly, lw, lh in ruled(bimg, it['x'], it['y'], it['w'], it['h']):
                        add_rect(sl, lx, ly, lw, lh, _stop(bimg)[0])
                    continue
                bw, bc, bs = it.get('bw', [0]*4), it.get('bc', [None]*4), it.get('bs', ['none']*4)
                x, y, w, h = it['x'], it['y'], it['w'], it['h']
                rad = it.get('radius', 0)
                drawn = [i for i in range(4) if bw[i] > 0.2 and bs[i] != 'none' and bc[i]]
                # a border on all four sides is the shape's own outline: drawing it as
                # four bars would square off anything round
                box = len(drawn) == 4 and all(abs(bw[i] - bw[0]) < 0.2 for i in drawn) \
                    and all(bc[i] == bc[0] and bs[i] == bs[0] for i in drawn)
                rings = it.get('rings') or []
                halo = next((g for g in rings if not g['inset']), None)
                ring = next((g for g in rings if g['inset']), None)
                if halo:
                    add_rect(sl, x - halo['w'], y - halo['w'], w + 2 * halo['w'],
                             h + 2 * halo['w'], halo['c'],
                             rad + halo['w'] if rad > 0.5 else 0)
                if ring and not box:
                    box, bw, bc, bs = True, [ring['w']] * 4, [ring['c']] * 4, ['solid'] * 4
                if it.get('fill') or box:
                    if box:
                        # CSS draws the border inside the box, PowerPoint centres it on the edge
                        o = bw[0] / 2
                        shp = add_rect(sl, x + o, y + o, w - bw[0], h - bw[0],
                                       it.get('fill'), max(0, rad - o))
                        shp.line.fill.solid()
                        shp.line.fill.fore_color.rgb = col(bc[0])
                        shp.line.width = Pt(bw[0] * PT)
                        if bs[0] in ('dashed', 'dotted'):
                            shp.line.dash_style = MSO_LINE_DASH_STYLE.DASH \
                                if bs[0] == 'dashed' else MSO_LINE_DASH_STYLE.ROUND_DOT
                        if (bc[0] or {}).get('a', 1) < 0.99:
                            sc = shp.line.fill.fore_color._xFill.find(qn('a:srgbClr'))
                            sc.append(sc.makeelement(qn('a:alpha'),
                                                     {'val': str(int(bc[0]['a'] * 100000))}))
                    else:
                        add_rect(sl, x, y, w, h, it['fill'], rad)
                if not box:
                    # PowerPoint has no per-side border, so each drawn edge is its own bar
                    edges = ((0, x, y, w, bw[0]), (1, x + w - bw[1], y, bw[1], h),
                             (2, x, y + h - bw[2], w, bw[2]), (3, x, y, bw[3], h))
                    for i, ex, ey, ew, eh in edges:
                        if i in drawn:
                            add_rect(sl, ex, ey, ew, eh, bc[i])
            elif k == 'img':
                src = it['src']
                path = src if os.path.isabs(src) else os.path.join(DECK, src)
                place_picture(sl, path, it['x'], it['y'], it['w'], it['h'],
                              it.get('fit', 'fill'), it.get('pad'))
            elif k == 'svg':
                if it.get('png') and os.path.exists(it['png']):
                    place_picture(sl, it['png'], it['x'], it['y'], it['w'], it['h'], 'contain')
            elif k == 'text':
                add_text(sl, it)
    prs.save(out)
    return prs

if __name__ == '__main__':
    data = json.load(io.open('slides.json', encoding='utf-8'))
    build(data, 'IAQ-Company-Deck-2026.pptx')
    print('wrote IAQ-Company-Deck-2026.pptx  %.1f MB'
          % (os.path.getsize('IAQ-Company-Deck-2026.pptx') / 1e6))
