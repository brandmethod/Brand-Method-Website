# -*- coding: utf-8 -*-
"""Rebuild 01.3 Milestones from IAQ's own company profile timeline (profile p5).

The original is a single flattened graphic: one horizontal axis, years
alternating above and below, entries colour-coded EPCC / Energy / Tool
Utility, and a national flag wherever an office opened. At 16:9 a single
axis of sixteen ticks leaves ~108u per year, which is too narrow for the
project names, so the axis is split into two bands of eight. Every entry
and every flag from the original is carried across.
"""
import io, re
from flags import FLAGS

# (year, [(kind, text)], [office codes])   kind: e=EPCC  g=Energy  t=Tool Utility
ERAS = [
    ('1995', [('e', 'Established as a cleanroom specialist')], ['my']),
    ('2000', [('e', '(EPCC) ST Microelectronics, Class 10K cleanroom')], ['ma']),
    ('2006', [], ['cn']),
    ('2007', [], ['pl']),
    ('2008', [('e', '(PCC) Western Digital PJ, Class 10 cleanroom')], ['fr']),
    ('2009', [('e', '(GC / D&amp;B) MEMC Ipoh, Class 1 cleanroom')], []),
    ('2013', [('e', '(PCC) MRT Project tunnel station M&amp;E'),
              ('e', '(EPC) Infineon MKZ, Class 1K cleanroom'),
              ('e', '(EPCC) SilTerra FAB'),
              ('g', '(PCC) Rapid Project Siemens powerplant piping works'),
              ('g', '(BOT) Pagoh Edu Hub DCS')], []),
    ('2016', [('g', '(GC) KLCC DCC Plant, largest DCC plant in Malaysia')], []),

    ('2017', [('e', '(GC) Ain Medicare')], []),
    ('2020', [('e', '(GC) Vital HC'),
              ('e', '(GC / PCC) Robert Bosch'),
              ('e', '(GC / PCC) P Project')], ['se']),
    ('2021', [('e', '(PCC) Microsoft Data Center'),
              ('e', '(GC / D&amp;B) SilTerra expansion'),
              ('e', '(EPCM / D&amp;B) Soitec PR1A expansion'),
              ('e', '(GC / EPCM) Infineon IFKM3 expansion')], []),
    ('2022', [('e', '(GC / D&amp;B) XFAB 40K expansion')], []),
    ('2023', [], ['sg']),
    ('2024', [('e', '(GC / D&amp;B) Progressive Build P Project')], []),
    ('2025', [('e', '(GC / D&amp;B) Hasegawa'),
              ('e', '(PCC) 160MW hyperscale data centre'),
              ('e', '(EPCC) ESCM Germany'),
              ('g', '(EPCC) KLCC DCS chiller upgrading')], ['de']),
    ('2026', [('e', '(D&amp;B) Tata Dholera DF1'),
              ('t', '(EPCM / HU) Micron MSH'),
              ('g', '(EPCC) GDC Putrajaya chiller upgrading')], ['us', 'in']),
]

def band(rows):
    cols = []
    for year, items, offices in rows:
        flags = ''.join('<span class="tl-flag">%s</span>' % FLAGS[c] for c in offices)
        entries = ''.join(
            '<li class="k-%s">%s</li>' % (k, t) for k, t in items)
        cols.append(
            '<div class="tl-col"><div class="tl-tick"></div>'
            '<div class="tl-year">%s%s</div>'
            '<ul class="tl-list">%s</ul></div>' % (year, flags, entries))
    return '<div class="tl-band">%s</div>' % ''.join(cols)

LEGEND = ('<div class="tl-key">'
          '<span class="k k-e">EPCC projects</span>'
          '<span class="k k-g">Energy projects</span>'
          '<span class="k k-t">Tool utility projects</span>'
          '<span class="k k-o">Office opened</span></div>')

TIMELINE = ('<div class="timeline">%s%s%s</div>'
            % (LEGEND, band(ERAS[:8]), band(ERAS[8:])))

# ---------------------------------------------------------------- splice in
p = 'build_deck.py'
s = io.open(p, encoding='utf-8').read()

start = s.index("# ---------------------------------------------------------------- 01.3 MILESTONES")
end = s.index("# ---------------------------------------------------------------- 01.4")
NEW = ("# ---------------------------------------------------------------- 01.3 MILESTONES\n"
       "slide('''%s''',\n"
       "      part_idx=0, num='01.3', title='Milestones',\n"
       "      note='IAQ&rsquo;s own timeline, 1995 to 2026: the projects that marked each year "
       "and the offices opened along the way.', fill=True)\n\n" % TIMELINE)
s = s[:start] + NEW + s[end:]
io.open(p, 'w', encoding='utf-8').write(s)
print('01.3 rebuilt — %d years, %d entries, %d office openings'
      % (len(ERAS), sum(len(i) for _, i, _ in ERAS), sum(len(o) for _, _, o in ERAS)))
