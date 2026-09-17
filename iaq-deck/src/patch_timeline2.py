# -*- coding: utf-8 -*-
"""01.3 Milestones, improved from IAQ's own company-profile timeline.

The profile runs one axis with years alternating above and below it and a
national flag wherever an office opened. Reproduced literally that leaves
three columns carrying nothing but a flag, which reads as holes in the
line and squeezes the project names into 108u of width. So the office
openings are lifted into their own strip and the axis carries only the
years that have projects: thirteen columns instead of sixteen, half as
much again per column, and type that can be read.
"""
import io
from flags import FLAGS

OFFICES = [('my','Malaysia','1995'), ('ma','Morocco','2000'), ('cn','China','2006'),
           ('pl','Poland','2007'), ('fr','France','2008'), ('se','Sweden','2020'),
           ('sg','Singapore','2023'), ('de','Germany','2025'),
           ('us','United States','2026'), ('in','India','2026')]

YEARS = [
 ('1995', [('e','Established as a cleanroom specialist')]),
 ('2000', [('e','(EPCC) ST Microelectronics, Class 10K cleanroom')]),
 ('2008', [('e','(PCC) Western Digital PJ, Class 10 cleanroom')]),
 ('2009', [('e','(GC / D&amp;B) MEMC Ipoh, Class 1 cleanroom')]),
 ('2013', [('e','(PCC) MRT Project tunnel station M&amp;E'),
           ('e','(EPC) Infineon MKZ, Class 1K cleanroom'),
           ('e','(EPCC) SilTerra FAB'),
           ('g','(PCC) Rapid Project Siemens powerplant piping works'),
           ('g','(BOT) Pagoh Edu Hub DCS')]),
 ('2016', [('g','(GC) KLCC DCC Plant, largest DCC plant in Malaysia')]),
 ('2017', [('e','(GC) Ain Medicare')]),
 ('2020', [('e','(GC) Vital HC'),
           ('e','(GC / PCC) Robert Bosch'),
           ('e','(GC / PCC) P Project')]),
 ('2021', [('e','(PCC) Microsoft Data Center'),
           ('e','(GC / D&amp;B) SilTerra expansion'),
           ('e','(EPCM / D&amp;B) Soitec PR1A expansion'),
           ('e','(GC / EPCM) Infineon IFKM3 expansion')]),
 ('2022', [('e','(GC / D&amp;B) XFAB 40K expansion')]),
 ('2024', [('e','(GC / D&amp;B) Progressive Build P Project')]),
 ('2025', [('e','(GC / D&amp;B) Hasegawa'),
           ('e','(PCC) 160MW hyperscale data centre'),
           ('e','(EPCC) ESCM Germany'),
           ('g','(EPCC) KLCC DCS chiller upgrading')]),
 ('2026', [('e','(D&amp;B) Tata Dholera DF1'),
           ('t','(EPCM / HU) Micron MSH'),
           ('g','(EPCC) GDC Putrajaya chiller upgrading')]),
]

offices = ''.join(
 '<span class="off"><span class="off-flag">%s</span>'
 '<span class="off-name">%s</span><span class="off-yr">%s</span></span>'
 % (FLAGS[c], name, yr) for c, name, yr in OFFICES)

cols = ''.join(
 '<div class="tl-col %s" style="grid-column:%d"><div class="tl-dot"></div>'
 '<div class="tl-stem"></div><div class="tl-set"><div class="tl-year">%s</div>'
 '<ul class="tl-list">%s</ul></div></div>'
 % ('up' if i % 2 == 0 else 'dn', i + 1, year,
    ''.join('<li class="k-%s">%s</li>' % (k, t) for k, t in items))
 for i, (year, items) in enumerate(YEARS))

LEGEND = ('<div class="tl-key"><span class="k k-e">EPCC projects</span>'
          '<span class="k k-g">Energy projects</span>'
          '<span class="k k-t">Tool utility projects</span></div>')
BLOCK = ('<div class="timeline">'
         '<div class="tl-offices"><span class="label">Offices opened</span>'
         '<div class="offs">%s</div></div>'
         '%s<div class="tl-band">%s</div></div>' % (offices, LEGEND, cols))

p = 'build_deck.py'
s = io.open(p, encoding='utf-8').read()
a = s.index("# ---------------------------------------------------------------- 01.3 MILESTONES")
b = s.index("# ---------------------------------------------------------------- 01.4")
s = s[:a] + ("# ---------------------------------------------------------------- 01.3 MILESTONES\n"
  "slide('''%s''',\n"
  "      part_idx=0, num='01.3', title='Milestones',\n"
  "      note=\"IAQ's own timeline, 1995 to 2026: the offices opened along the way, \"\n"
  "           \"and the projects that marked each year.\", fill=True)\n\n" % BLOCK) + s[b:]
io.open(p, 'w', encoding='utf-8').write(s)
print('rebuilt: %d offices, %d year columns, %d entries'
      % (len(OFFICES), len(YEARS), sum(len(i) for _, i in YEARS)))
