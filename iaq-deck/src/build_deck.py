#!/usr/bin/env python3
"""Generate the IAQ Group presentation deck (index.html)."""
import html, os

OUT = '/home/user/Brand-Method-Website/iaq-deck/index.html'

# ---------------------------------------------------------------- helpers
def esc(t):
    return html.escape(t, quote=False)

slides = []          # list of html strings
PARTS = ['The Company', 'Project References', 'Safety, Quality & ESG']


def chrome(part_idx, num, foot):
    """Top line + footer shared by every slide. part_idx is 0-2, or None."""
    tab = f'<span class="tab">{num}</span>' if num else ''
    part = f'Part {part_idx+1:02d} · {PARTS[part_idx]}' if part_idx is not None else 'IAQ Group'
    dots = ''.join(
        f'<i class="dot{" on" if part_idx == i else ""}"></i>' for i in range(3)
    ) if part_idx is not None else ''
    return (tab, part, dots, foot)


def slide(body, *, part_idx=None, num='', title='', note='', foot='',
          dark=False, bare=False, cls='', fill=False):
    """Standard content slide: top line, numbered header block, content, footer."""
    i = len(slides) + 1
    tab, part, dots, foot = chrome(part_idx, num, foot or (PARTS[part_idx] if part_idx is not None else 'IAQ Group'))
    head = ''
    if not bare:
        head = f'''
    <header class="shead">
      <h2 class="s-title">{esc(title)}</h2>
      <p class="s-note">{esc(note)}</p>
    </header>'''
    slides.append(f'''<div class="stage"><section class="slide{' dark' if dark else ''} {cls}">
  <div class="topline">
    <div class="tl-l">{tab}<span class="tl-part">{esc(part)}</span></div>
    <div class="tl-r">IAQ Group // Company Deck</div>
  </div>{head}
  <div class="canvas{' fill' if fill else ''}">{body}
  </div>
  <footer class="botline">
    <div class="bl-l"><span class="folio">{i:02d} / TOTAL</span></div>
    <div class="bl-c">{dots}</div>
    <div class="bl-r">{esc(foot)}</div>
  </footer>
</section></div>''')


def raw_slide(inner, dark=True):
    i = len(slides) + 1
    slides.append(f'''<div class="stage"><section class="slide{' dark' if dark else ''}">
{inner}
  <footer class="botline">
    <div class="bl-l"><span class="folio">{i:02d} / TOTAL</span></div>
    <div class="bl-c"></div>
    <div class="bl-r">IAQ Group</div>
  </footer>
</section></div>''')


def specrows(rows):
    out = []
    for label, value, iso in rows:
        out.append(f'''<div class="sr"><dt>{esc(label)}</dt>'''
                   f'''<dd class="{'iso' if iso else ''}">{esc(value)}</dd></div>''')
    return '<dl class="specs">' + ''.join(out) + '</dl>'


def pcard(img, flag, name, rows, alt=None):
    return f'''
      <article class="pcard">
        <img class="shot" src="img/{img}.jpg" alt="{esc(alt or name)}">
        <div class="panel">
          <div class="flag">{esc(flag)}</div>
          <h3 class="pname">{esc(name)}</h3>
          {specrows(rows)}
        </div>
      </article>'''


def hero(img, part_idx, num, section, flag, title, rows, foot):
    i = len(slides) + 1
    tab, part, dots, foot = chrome(part_idx, num, foot)
    slides.append(f'''<div class="stage"><section class="slide dark hero">
  <div class="hero-media"><img src="img/{img}.jpg" alt="{esc(title)}"></div>
  <div class="topline">
    <div class="tl-l">{tab}<span class="tl-part">{esc(section)}</span></div>
    <div class="tl-r">IAQ Group // Company Deck</div>
  </div>
  <div class="hero-panel">
    <div class="flag">{esc(flag)}</div>
    <h2 class="hero-title">{title}</h2>
    {specrows(rows)}
  </div>
  <footer class="botline">
    <div class="bl-l"><span class="folio">{i:02d} / TOTAL</span></div>
    <div class="bl-c">{dots}</div>
    <div class="bl-r">{esc(foot)}</div>
  </footer>
</section></div>''')


# ================================================================ 01 COVER
raw_slide('''  <div class="cover-media"><img src="img/infineon-kulim.jpg" alt="Infineon Kulim Wafer Fab 3"></div>
  <div class="topline">
    <div class="tl-l"><span class="tl-part">Your Total Facility Solutions Provider</span></div>
    <div class="tl-r">Company Deck // Edition 2026</div>
  </div>
  <div class="cover-copy">
    <img class="logo" src="img/iaq-logo.png" alt="IAQ">
    <div class="cover-body">
      <h1 class="cover-title">Engineering the facilities<br>advanced industry<br>runs on.</h1>
      <p class="stand">EPCM, EPCC and Energy Facility Management for cleanroom-critical
      industries: semiconductor, data centre, EV battery, pharmaceutical and energy.
      Established 1994.</p>
    </div>
  </div>''')

# ================================================================ 02 CONTENTS
contents_parts = [
    ('01', 'The Company', 'Who we are, how we are built, and what we deliver.', [
        ('01.1', 'About IAQ'), ('01.2', 'IAQ at a Glance'), ('01.3', 'Milestones'),
        ('01.4', 'Global Footprint'), ('01.5', 'Core Values'), ('01.6', 'Business Units'),
        ('01.7', 'Scope of Services'), ('01.8', 'Industry Focus')]),
    ('02', 'Project References', 'The work itself, grouped by industry and region.', [
        ('02.1', 'Portfolio Overview'), ('02.2', 'Semiconductor · Malaysia'),
        ('02.3', 'Semiconductor · Singapore'), ('02.4', 'Data Centre'),
        ('02.5', 'EV Battery · Europe'), ('02.6', 'Semiconductor · Europe & Morocco'),
        ('02.7', 'Semiconductor & Display · China'), ('02.8', 'Photovoltaics'),
        ('02.9', 'Pharmaceutical & Medical'), ('02.10', 'District Cooling & Energy'),
        ('02.11', 'Reference Index')]),
    ('03', 'Safety, Quality & ESG', 'The standards every project is held to.', [
        ('03.1', 'ESG Commitments'), ('03.2', 'Safety & Recognition'),
        ('03.3', 'Closing'), ('03.4', 'Contacts')]),
]
cols = ''
for pn, pname, pnote, secs in contents_parts:
    items = ''.join(
        f'<li><span class="ci-n">{n}</span><span class="ci-t">{esc(t)}</span></li>'
        for n, t in secs)
    cols += f'''
      <div class="cpart">
        <div class="cp-head">
          <span class="cp-num">{pn}</span>
          <div>
            <h3 class="cp-name">{esc(pname)}</h3>
            <p class="cp-note">{esc(pnote)}</p>
          </div>
        </div>
        <ul class="cp-list">{items}</ul>
      </div>'''
slide(f'<div class="contents">{cols}\n    </div>',
      num='', title='Contents',
      note='Three parts. Every section is numbered, named and opens with a one-line summary.',
      foot='Contents', fill=True)

# ================================================================ PART 01
def divider(part_idx, num, name, note, img, bullets):
    i = len(slides) + 1
    items = ''.join(f'<li>{esc(b)}</li>' for b in bullets)
    dots = ''.join(f'<i class="dot{" on" if part_idx == k else ""}"></i>' for k in range(3))
    slides.append(f'''<div class="stage"><section class="slide dark divider">
  <div class="div-grid">
    <div class="div-copy">
      <span class="div-kicker">Part {num} of 03</span>
      <div class="div-num">{num}</div>
      <h2 class="div-title">{esc(name)}</h2>
      <p class="div-note">{esc(note)}</p>
      <ul class="div-list">{items}</ul>
    </div>
    <div class="div-media"><img src="img/{img}.jpg" alt=""></div>
  </div>
  <div class="topline">
    <div class="tl-l"><span class="tl-part">Part {num} · {esc(name)}</span></div>
    <div class="tl-r">IAQ Group // Company Deck</div>
  </div>
  <footer class="botline">
    <div class="bl-l"><span class="folio">{i:02d} / TOTAL</span></div>
    <div class="bl-c">{dots}</div>
    <div class="bl-r">{esc(name)}</div>
  </footer>
</section></div>''')

divider(0, '01', 'The Company', 'Sections 01.1 to 01.8', 'p-project',
        ['Established 1994 · 32 years in total facility solutions',
         '450 people across 6 global offices',
         'ISO 9001 · ISO 14001 · ISO 45001 certified'])

# ---------------------------------------------------------------- 01.1 ABOUT
slide('''
    <div class="split">
      <div class="lede">
        <h3 class="statement">Established 1994.<br>A trailblazer in total facility solutions.</h3>
        <p class="body">Engineering, procurement, construction and maintenance for the industries
        where contamination, uptime and safety decide the outcome, from semiconductor wafer fabs
        to gigafactories, data centres and pharmaceutical plants.</p>
      </div>
      <div class="lede-side">''' + specrows([
        ('Vision', 'To be a regional facility solutions provider with engineering excellence that facilitates technological innovation and advancement in quality of life.', False),
        ('Mission', 'Providing innovative, sustainable facility and engineering solutions benefitting our clients and stakeholders, driven by our leadership, employees and partners globally.', False),
        ('Delivery Models', 'EPCM · EPCC · Energy Facility Management', True),
      ]) + '''
      </div>
    </div>''',
      part_idx=0, num='01.1', title='About IAQ',
      note='Who we are, what we build, and the models we deliver under.', fill=True)

# ---------------------------------------------------------------- 01.2 GLANCE
stats = [('32', '', 'Years Experience'), ('450', '', 'Employees'),
         ('200', '+', 'Projects Completed'), ('1.5', 'mil m²', 'Cleanroom Built-Up Area'),
         ('6', '', 'Global Offices'), ('20', 't / yr', 'Carbon Footprint Reduced')]
stat_html = ''.join(
    f'<div class="stat"><div class="num">{v}<span>{u}</span></div><div class="label">{esc(l)}</div></div>'
    for v, u, l in stats)
certs = [('Intertek', 'ISO 9001:2015'), ('Intertek', 'ISO 14001:2015'), ('Intertek', 'ISO 45001:2018'),
         ('CIDB', 'Grade G7'), ('PKK', 'Grade G7'), ('Highwire Safety', 'Gold Award'),
         ('MCIEA 2024', 'Builder of the Year')]
cert_html = ''.join(f'<span class="cert">{esc(a)} <strong>{esc(b)}</strong></span>' for a, b in certs)
slide(f'''
    <div class="stats">{stat_html}</div>
    <div class="sub">
      <div class="label">Certification &amp; Recognition</div>
      <div class="certs">{cert_html}</div>
    </div>''',
      part_idx=0, num='01.2', title='IAQ at a Glance',
      note='The company in six numbers, and the certifications that stand behind them.', fill=True)

# ---------------------------------------------------------------- 01.3 MILESTONES
eras = [
    ('1994', '2000', 'Foundation', [
        ('1994', 'Established as cleanroom specialist'),
        ('2000', 'First decade of cleanroom delivery in Malaysia')]),
    ('2006', '2009', 'Regional Expansion', [
        ('2006', '(EPCC) ST Microelectronics, Class 10K cleanroom'),
        ('2008', '(PCC) Western Digital PJ, Class 10 cleanroom'),
        ('2009', '(GC / D&B) MEMC Ipoh, Class 1 cleanroom')]),
    ('2013', '2017', 'Landmark Plants', [
        ('2013', '(GC) KLCC DCC Plant, largest DCC plant in Malaysia'),
        ('2016', '(PCC) MRT tunnel station M&E · (EPC) Infineon MKZ Class 1K · (EPCC) SilTerra FAB · (PCC) Rapid Siemens powerplant piping · (BOT) Pagoh Edu Hub DCS'),
        ('2017', '(GC) Ain Medicare')]),
    ('2020', '2022', 'Global Scale', [
        ('2020', '(GC) Vital Healthcare'),
        ('2021', '(GC / PCC) Robert Bosch · (GC / PCC) P Project'),
        ('2022', '(PCC) Microsoft Data Center · (GC / D&B) SilTerra Expansion · (EPCM / D&B) Soitec PR1A Expansion · (GC / EPCM) Infineon IFKM3 Expansion')]),
    ('2023', '2026', 'Advanced Technology', [
        ('2023', '(GC / D&B) XFAB 40K Expansion'),
        ('2024', '(GC / D&B) Progressive Build P Project'),
        ('2025', '(GC / D&B) Hasegawa · (PCC) 160MW hyperscale data centre · (EPCC) ESCM Germany · (EPCC) KLCC DCS chiller upgrading'),
        ('2026', '(D&B) Tata Dholera DF1 · (EPCM / HU) Micron MSH · (EPCC) GDC Putrajaya chiller upgrading')]),
]
era_html = ''
for k, (a, b, name, items) in enumerate(eras, start=1):
    li = ''.join(f'<li><span class="yr">{y}</span><span class="ev">{esc(t)}</span></li>' for y, t in items)
    era_html += f'''
      <div class="era">
        <div class="era-head">
          <span class="era-span">{a}<span class="to">to</span>{b}</span>
          <h3 class="era-name">{esc(name)}</h3>
        </div>
        <ul class="era-list">{li}</ul>
      </div>'''
slide(f'<div class="eras">{era_html}\n    </div>',
      part_idx=0, num='01.3', title='Milestones',
      note='Landmark projects from 1994 to 2026, grouped into five eras of growth.', fill=True)

# ---------------------------------------------------------------- 01.4 FOOTPRINT
markets = [
    ('1994', 'Malaysia', 'Turnkey design, procurement, construction and commissioning for hi-tech clients. Selangor (HQ), Penang, Johor and Kuching.'),
    ('2020', 'Sweden', "Gigafactory construction for EV battery manufacture, part of Europe's clean and digital transition."),
    ('2023', 'Singapore', 'Design & build EPCM services to global semiconductor clients.'),
    ('2025', 'Germany', 'EPCC services following semiconductor expansion in Europe.'),
    ('2026', 'India · United States', "D&B turnkey for India's first wafer fab, and US entry following localisation of advanced tech facilities."),
]
m_html = ''.join(
    f'<div class="mrow"><div class="myr">{y}</div><div class="mtxt">'
    f'<p class="ghead">{esc(n)}</p><p class="cap">{esc(d)}</p></div></div>'
    for y, n, d in markets)
slide(f'''
    <div class="split">
      <div class="lede">
        <h3 class="statement">From Shah Alam<br>to seven markets.</h3>
        <p class="body">Offices across Asia Pacific and Europe follow our clients as advanced
        manufacturing localises. Additional offices operate in Norway, China, France and Poland.</p>
      </div>
      <div class="mrows">{m_html}</div>
    </div>''',
      part_idx=0, num='01.4', title='Global Footprint',
      note='Where we operate, and the year we arrived in each market.', fill=True)

# ---------------------------------------------------------------- 01.5 CORE VALUES
values = [
    ('Safety First', 'Our services and works are carried out to the highest standard of safety and ethics.'),
    ('Quality Consistency', 'We take pride in the quality of solutions delivered, to achieve maximum client satisfaction.'),
    ('Honesty and Integrity', 'Our core code of conduct, fostering trust, accountability, professionalism and ethical practice.'),
    ('Efficiency & Proficiency', 'Committed to maximising available resources to achieve the best result collectively.'),
    ('Engineering Capabilities', 'Our way of working revolves around engineering principles, developing precise and sustainable solutions.'),
    ('Pursuit of Excellence', 'Devoted to excellence in all our works, providing sustainable solutions to complex challenges.'),
]
v_html = ''.join(
    f'''<article class="value">
        <img src="img/value-{k}.jpg" alt="">
        <div class="v-body"><span class="v-num">{k:02d}</span>
        <h3 class="v-name">{esc(n)}</h3><p class="v-note">{esc(d)}</p></div>
      </article>''' for k, (n, d) in enumerate(values, start=1))
slide(f'<div class="values">{v_html}</div>',
      part_idx=0, num='01.5', title='Core Values',
      note='Six commitments that govern how every project is run. Not words, but working rules.', fill=True)

# ---------------------------------------------------------------- 01.6 BUSINESS UNITS
units = [
    ('IAQ Solutions Sdn Bhd', 'Engineering, Procurement, Construction & Commissioning',
     'EPCC from conception to operation, completion and maintenance. Every stage managed, from initial design through commissioning, so clients in hi-tech industries can bring their visions to life.'),
    ('IAQ Utility Solutions Sdn Bhd', 'Process Critical Utilities & Total Tool Install',
     'EPCM partner for semiconductor manufacturing: engineering, procurement and construction management of process-critical utility infrastructure and total tool installation, bridging facility readiness and manufacturing start-up to accelerate fab ramp-up.'),
    ('IAQ Energy Facility Management Sdn Bhd', 'Energy Management',
     'Energy management solutions that optimise operations and reduce carbon footprint, keeping facilities running at the highest levels of efficiency and sustainability.'),
]
u_html = ''.join(
    f'''<div class="unit"><div class="u-num">{k:02d}</div>
      <div class="u-body"><h3 class="u-name">{esc(n)}</h3>
      <p class="spec">{esc(s)}</p><p class="cap">{esc(d)}</p></div></div>'''
    for k, (n, s, d) in enumerate(units, start=1))
slide(f'<div class="units">{u_html}</div>',
      part_idx=0, num='01.6', title='Business Units',
      note='Three companies under one group, covering the full delivery chain.', fill=True)

# ---------------------------------------------------------------- 01.7 SCOPE
scope = [
    ('Cleanroom System', 'ISO 3 to ISO 8 · Class 1 to Class 100K'),
    ('Air Conditioning System', 'ACMV, make-up air, recirculation'),
    ('Process Utilities', 'CDA, PCW, PV'),
    ('Process Exhaust System', 'Scrubbed, heat and general exhaust'),
    ('Chemical &amp; Gas Delivery', 'Specialty and bulk gases, chemical delivery'),
    ('Ultra Pure Water', 'UPW generation and distribution'),
    ('Waste Water Treatment', 'Industrial effluent and recovery'),
    ('Fire Protection System', 'Detection, suppression, compliance'),
    ('HT &amp; LV Electrical System', 'Up to 33kV substations'),
    ('Civil, Structural &amp; Architectural', 'Greenfield and brownfield CSA'),
    ('Facility Monitoring &amp; Control', 'FMCS, BMS, PA'),
    ('Tools Hookup', 'Progressive tool install and hookup'),
]
s_html = ''.join(
    f'<div class="chip"><span class="c-num">{k:02d}</span>'
    f'<span class="c-name">{n}</span><span class="c-note">{d}</span></div>'
    for k, (n, d) in enumerate(scope, start=1))
slide(f'<div class="chips four">{s_html}</div>',
      part_idx=0, num='01.7', title='Scope of Services',
      note='Twelve packages, self-performed and integrated under one contract.', fill=True)

# ---------------------------------------------------------------- 01.8 INDUSTRY
inds = [
    ('Semiconductor', 'Wafer fab, advanced packaging, test &amp; assembly'),
    ('Data Centre', 'Hyperscale cooling, security, uptime'),
    ('EV Battery', 'Dry rooms, moisture control, explosion proofing'),
    ('District Cooling &amp; Heating', 'Urban energy plant and distribution'),
    ('Photovoltaics', 'Cell and module lines, toxic material handling'),
    ('Pharmaceuticals &amp; Hospitals', 'GMP grades, regulated environments'),
    ('Food &amp; Beverage', 'Hygienic design, quality and safety standards'),
]
i_html = ''.join(
    f'<div class="chip"><span class="c-num">{k:02d}</span>'
    f'<span class="c-name">{n}</span><span class="c-note">{d}</span></div>'
    for k, (n, d) in enumerate(inds, start=1))
i_html += ('<div class="chip solid"><span class="c-num">+</span>'
           '<span class="c-name">Your facility next</span>'
           '<span class="c-note">Total facility solutions, end to end</span></div>')
slide(f'<div class="chips four">{i_html}</div>',
      part_idx=0, num='01.8', title='Industry Focus',
      note='Seven sectors, one discipline: contamination control under code and class.', fill=True)

# ================================================================ PART 02
divider(1, '02', 'Project References', 'Sections 02.1 to 02.11', 'northvolt',
        ['200+ projects completed across three regions',
         'Over 1.5 million m² of cleanroom built',
         'ISO 3 to ISO 8 · Class 1 to Class 100K'])

# ---------------------------------------------------------------- 02.1 PORTFOLIO
regions = [
    ('map-my-sg', 'Malaysia &amp; Singapore', '02.2 to 02.4 · 02.8 to 02.10',
     'Semiconductor, data centre, pharmaceutical, photovoltaics, district cooling and energy.'),
    ('map-europe', 'Europe &amp; Morocco', '02.5 to 02.6',
     'EV battery gigafactories, wafer fabs and advanced semiconductor in Sweden, Norway, France, Poland and Morocco.'),
    ('map-china', 'China', '02.7',
     'Semiconductor, display, pharmaceutical, automotive and R&amp;D facilities.'),
]
r_html = ''.join(
    f'''<article class="maptile">
        <img src="img/{img}.jpg" alt="{esc(name)} project locations">
        <div class="m-body"><span class="flag">{sec}</span>
        <h3 class="m-name">{name}</h3><p class="cap">{note}</p></div>
      </article>''' for img, name, sec, note in regions)
slide(f'''<div class="maps">{r_html}</div>
    <div class="sub">
      <div class="tri">
        <div class="stat sm"><div class="num">200<span>+</span></div><div class="label">Projects Completed</div></div>
        <div class="stat sm"><div class="num">1.5<span>mil m²</span></div><div class="label">Cleanroom Built</div></div>
        <div class="stat sm"><div class="num">5</div><div class="label">Contract Models</div><p class="cap tight">GC · EPCC · EPCM · PCC · Tool Hookup</p></div>
      </div>
    </div>''',
      part_idx=1, num='02.1', title='Portfolio Overview',
      note='How the reference book breaks down by region, and which sections cover what.', fill=True)

# ---------------------------------------------------------------- 02.2 SEMI · MALAYSIA
hero('infineon-kulim', 1, '02.2', 'Semiconductor · Malaysia', 'Kulim, Kedah · Greenfield wafer fab',
     'Infineon Kulim<br>Wafer Fab 3',
     [('Cleanroom', 'ISO 4 · 5 · 6 · 7 (Class 10 · 100 · 1K · 10K)', True),
      ('Scope', 'PCC for cleanroom and mechanical works', False),
      ('Description', 'General contractor for WP06, KLM3 Expansion, 35,000 m² cleanroom area', False)],
     'Semiconductor · Malaysia')

hero('p-project', 1, '02.2', 'Semiconductor · Malaysia', 'Advanced packaging · 75,000 m²',
     'P Project',
     [('Cleanroom', 'ISO 4 to 7 (Class 10 to 10K)', True),
      ('Scope', 'Design & build GC: CSA, MEP, process utilities, chemical & gases system, waste treatment', False),
      ('Description', "Progressive-built EPCM contract model for the client's advanced packaging facility", False)],
     'Semiconductor · Malaysia')

slide('<div class="grid two">' + pcard(
        'xfab-kuching', 'Kuching, Sarawak', 'XFAB Kuching 40K Expansion',
        [('Cleanroom', 'ISO 5 · 6 · 7 (Class 100 · 1K · 10K)', True),
         ('Scope', 'CSA, mechanical, electrical & plumbing, process utilities, UPW, chemical & gases', False),
         ('Description', 'GC design & build for wafer fab extension, CUB and supporting facilities. Capacity 30k to 40k, 40,000 m² built-up', False)]) + pcard(
        'soitec-pr1a', 'Greenfield plant', 'SOITEC PR1A Expansion',
        [('Cleanroom', 'ISO 4 · 5 · 6 · 7 (Class 10 · 100 · 1K · 10K)', True),
         ('Scope', 'EPCM design & build for fab, including all related MEP', False),
         ('Description', 'EPCM consultant for PR1A new greenfield plant, 45,000 m² built-up', False)]) + '\n    </div>',
      part_idx=1, num='02.2', title='Semiconductor · Malaysia',
      note='Wafer fab, advanced packaging, test and assembly, ISO 3 to ISO 7.',
      foot='Semiconductor · Malaysia')

slide('<div class="grid two">' + pcard(
        'bosch-testing', 'Greenfield · test & manufacturing', 'Robert Bosch Testing Manufacturing Plant',
        [('Cleanroom', 'ISO 6 · 7 (Class 1K · 10K)', True),
         ('Scope', 'Main building CSA, MEP, process utilities and cleanroom package', False),
         ('Description', 'General contractor for greenfield testing and manufacturing plant, 25,000 m² built-up', False)]) + pcard(
        'wafer-fab-exp', 'FAB1E A/B · new CUB', 'Wafer Fab Facility & Expansion',
        [('Cleanroom', 'ISO 5 (Class 100)', True),
         ('Scope', 'EPCC new building: CSA, mechanical, electrical, cleanroom, process utilities, specialty and bulk gases, chemical delivery', False),
         ('Description', 'EPCC and design & build for FAB1E A/B expansion. 1,000 m² cleanroom, 5,000 m² new CUB', False)]) + '\n    </div>',
      part_idx=1, num='02.2', title='Semiconductor · Malaysia',
      note='Continued. Greenfield plants and fab expansions delivered as GC and EPCC.',
      foot='Semiconductor · Malaysia')

slide('<div class="grid two">' + pcard(
        'ti-melaka', 'Melaka', 'Texas Instruments, Melaka',
        [('Cleanroom', 'ISO 5 · 6 · 7 (Class 100 · 1K · 10K)', True),
         ('Scope', 'Mechanical, electrical, process utilities, testing & commissioning', False),
         ('Description', 'Facilitation works for residual management, 32,000 m² built-up', False)]) + pcard(
        'infineon-melaka', 'Melaka · Block 8', 'Infineon Technologies (M) Sdn Bhd',
        [('Cleanroom', 'ISO 6 · 7 (Class 1K · 10K)', True),
         ('Scope', 'EPCM-GMP for civil & structural, cleanroom, air-conditioning, process utilities and multi-storey carpark', False),
         ('Description', 'Block 8 testing, probe & assembly plant, 43,000 m² built-up', False)]) + '\n    </div>',
      part_idx=1, num='02.2', title='Semiconductor · Malaysia',
      note='Continued. Test, probe and assembly plants for tier-one device makers.',
      foot='Semiconductor · Malaysia')

slide('<div class="grid two">' + pcard(
        'memc-ipoh', 'Ipoh, Perak · greenfield', 'MEMC Ipoh Sdn Bhd',
        [('Cleanroom', 'ISO 3 · 4 · 5 · 6 · 7 (Class 1 to 10K)', True),
         ('Scope', 'Mechanical, electrical, process utilities, cleanroom, fire fighting, FMCS, CSA and tools hookup', False),
         ('Description', 'Greenfield project. The tightest cleanroom class in the portfolio, ISO 3 (Class 1)', False)]) + pcard(
        'st-johor', 'Johor', 'STMicroelectronics Sdn Bhd',
        [('Cleanroom', 'ISO 7 (Class 10K)', True),
         ('Scope', 'Cleanroom architectural, ACMV, electrical, process utility and cleanroom works', False),
         ('Description', 'Three-storey production factory', False)]) + '\n    </div>',
      part_idx=1, num='02.2', title='Semiconductor · Malaysia',
      note='Continued. Class 1 cleanroom capability and multi-storey production works.',
      foot='Semiconductor · Malaysia')

# ---------------------------------------------------------------- 02.3 SINGAPORE
slide('<div class="grid three">' + pcard(
        'teksend', 'Photomask', 'Teksend Photomask',
        [('Cleanroom', 'Class 1 to Class 10K', True),
         ('Scope', 'EPCC for cleanroom, ACMV, electrical, process utility, BMS, PA, WWT, UPW, tool hookup', False)]) + pcard(
        'micron-msh', 'Tool hookup', 'Micron MSH Tool HU',
        [('Scope', 'Progressive tool hook up', False),
         ('Description', '2,000 progressive tool hookup services for MSH', False)]) + pcard(
        'micron-f10', 'Fit-out', 'Micron F10A & F10NX',
        [('Scope', 'Interior design & mechanical fit-out works', False),
         ('Description', 'F10NX office optimisation', False)]) + '\n    </div>',
      part_idx=1, num='02.3', title='Semiconductor · Singapore',
      note='Design & build EPCM in Singapore since 2023: photomask, tool hookup and fit-out.',
      foot='Semiconductor · Singapore')

# ---------------------------------------------------------------- 02.4 DATA CENTRE
hero('hyperscale-dc', 1, '02.4', 'Data Centre', 'Client confidential · 160 MW',
     'Hyperscale<br>Data Centre',
     [('Scope', 'Construction, completion, testing & commissioning for mechanical packages 1 & 2: office, data halls, mechanical utility building', False),
      ('Also delivered', 'Microsoft DTC-KUL 03. PCC for CHW and CW piping works, 9.6 MW data centre, KUL03 Phase 1', False)],
     'Data Centre')

# ---------------------------------------------------------------- 02.5 EV BATTERY
hero('northvolt', 1, '02.5', 'EV Battery · Europe', 'Skellefteå, Sweden · 62,000 m²',
     'Northvolt AB<br>Gigafactory',
     [('Environment', 'Dry Room', True),
      ('Scope', 'Cleanroom and dry room architecture works', False),
      ('Description', 'Europe gigafactory for lithium-ion battery manufacture', False)],
     'EV Battery · Europe')

slide('<div class="grid three">' + pcard(
        'morrow', 'Norway · Battery Coast', 'Morrow Batteries',
        [('Environment', 'Dry Room', True),
         ('Scope', 'Cleanroom and dry room architectural system, ACMV', False),
         ('Description', '8,600 m² built-up', False)]) + pcard(
        'acc-phase1', 'France · greenfield', 'ACC Phase 1',
        [('Environment', 'Dry Room', True),
         ('Scope', 'Cleanroom, dry room architecture works', False),
         ('Description', '8,000 m² dry room system, 35,000 m² built-up', False)]) + pcard(
        'envision-france', 'France', 'Envision France',
        [('Environment', 'Dry Room', True),
         ('Scope', 'Cleanroom, dry room architecture works', False),
         ('Description', 'Battery manufacturing facility', False)]) + '\n    </div>',
      part_idx=1, num='02.5', title='EV Battery · Europe',
      note='Dry rooms for the gigafactories: moisture control and contamination control at scale.',
      foot='EV Battery · Europe')

# ---------------------------------------------------------------- 02.6 EUROPE SEMI
slide('<div class="grid four">' + pcard(
        'confidential-cmos', 'Client confidential', '28/22nm CMOS · 16/12nm FinFET Plant',
        [('Cleanroom', 'Class 1 to Class 10K', True),
         ('Scope', 'Cleanroom & mechanical general contractor', False)]) + pcard(
        'soitec-paris', 'Paris, France', 'Soitec Semiconductor',
        [('Scope', 'EPCC for cleanroom and MEP', False),
         ('Description', '11,000 m² built-up', False)]) + pcard(
        'st-casablanca', 'Casablanca, Morocco', 'STMicroelectronics',
        [('Cleanroom', 'ISO 5 (Class 100)', True),
         ('Description', 'Cleanroom, MEP and hookup, 60,000 m² built-up', False)]) + pcard(
        'xfab-paris', 'Paris, France', 'Xfab Semiconductor',
        [('Cleanroom', 'ISO 5 (Class 100)', True),
         ('Description', 'Progressive hookup work, 5,000 m² built-up', False)]) + '\n    </div>',
      part_idx=1, num='02.6', title='Semiconductor · Europe & Morocco',
      note='Following the fabs into Europe: advanced-node cleanrooms and progressive hookup.',
      foot='Semiconductor · Europe', fill=True)

# ---------------------------------------------------------------- 02.7 CHINA
slide('<div class="grid four">' + pcard(
        'ferrotec-hangzhou', 'Hangzhou · 23,400 m²', 'Ferrotec Semiconductor',
        [('Cleanroom', 'ISO 4 · 5 (Class 10 & 100)', True),
         ('Scope', 'EPCC for cleanroom, MEP and hookup works', False)]) + pcard(
        'infineon-wuxi', 'Wuxi · 8,000 m²', 'Infineon Technologies',
        [('Cleanroom', 'ISO 5 (Class 100)', True),
         ('Scope', 'EPCC for cleanroom, MEP and hookup works', False)]) + pcard(
        'smic-ningbo', 'Ningbo · 22,000 m²', 'SMIC',
        [('Cleanroom', 'ISO 5 · 6 (Class 100 & 1K)', True),
         ('Scope', 'EPCC for mechanical, electrical and plumbing works', False)]) + pcard(
        'maxtor-suzhou', 'Suzhou · 95,000 m²', 'Maxtor Technology',
        [('Cleanroom', 'ISO 5 · 6 (Class 100 & 1K)', True),
         ('Scope', 'Cleanroom and MEP works', False)]) + '\n    </div>',
      part_idx=1, num='02.7', title='Semiconductor & Display · China',
      note='EPCC across semiconductor, display and precision manufacturing. 23 further projects in section 02.11.',
      foot='China', fill=True)

# ---------------------------------------------------------------- 02.8 PHOTOVOLTAICS
slide('<div class="grid three">' + pcard(
        'first-solar', 'Kulim, Malaysia', 'First Solar Malaysia',
        [('Scope', 'PCC for M&E, KMW building; CSA and M&E for forming gas plant; M&E for SCO1', False)]) + pcard(
        'auo-sunpower', 'Melaka, Malaysia', 'AUO Sunpower',
        [('Scope', 'CSA, utilities, HVAC, electrical, testing & commissioning', False),
         ('Description', 'Fab 3A solar cell manufacturing', False)]) + pcard(
        'chint-solar', 'China · 57,000 m²', 'Chint Solar Technology',
        [('Cleanroom', 'ISO 8 (Class 100K)', True),
         ('Scope', 'Cleanroom, ACMV, process utilities and tools hookup', False)]) + '\n    </div>',
      part_idx=1, num='02.8', title='Photovoltaics',
      note='Solar cell and module manufacturing, including toxic material and waste handling.',
      foot='Photovoltaics')

# ---------------------------------------------------------------- 02.9 PHARMA
slide('<div class="grid four">' + pcard(
        'insulet', 'Greenfield · medical device', 'Insulet',
        [('Cleanroom', 'ISO 8 (Class 100K)', True),
         ('Scope', 'Design and build mechanical, cleanroom & electrical package', False)]) + pcard(
        'vital-healthcare', 'Greenfield · medical device', 'Vital Healthcare',
        [('Cleanroom', 'ISO 8 (Class 100K)', True),
         ('Scope', 'GC for CSA, 33kV substation and MEP', False)]) + pcard(
        'pharmaniaga', 'Puchong, Selangor', 'Pharmaniaga',
        [('Cleanroom', 'ISO 5 · 7 · 8 (Class 100 · 10K · 100K)', True),
         ('Scope', 'Cleanroom system and ACMV for a small volume parenteral facility', False)]) + pcard(
        'ain-medicare', 'Pharmaceutical building', 'Ain Medicare',
        [('Cleanroom', 'ISO 8 (Class 100K)', True),
         ('Scope', 'EPCC CSA, cleanroom system and M&E', False)]) + '\n    </div>',
      part_idx=1, num='02.9', title='Pharmaceutical & Medical',
      note='GMP grades and regulated environments, from parenteral facilities to medical device plants.',
      foot='Pharmaceutical & Medical', fill=True)

# ---------------------------------------------------------------- 02.10 DISTRICT COOLING
hero('klcc-dcp', 1, '02.10', 'District Cooling & Energy', 'Gas District Cooling (M) Sdn Bhd',
     'KLCC District<br>Cooling Plant',
     [('Description', 'Largest district cooling centre in Malaysia', True),
      ('Scope', 'ACMV, electrical & instrumentation, fire protection, process utility, plumbing & sanitary, water treatment, CSA', False),
      ('Also delivered', 'GDC Putrajaya plant electrification & chiller replacement (PICC) · KLCC DCC centrifugal chillers · Rapid Petronas Pengerang Co-gen, first co-gen plant in SEA · Pagoh Education Hub DCS', False)],
     'District Cooling & Energy')

# ---------------------------------------------------------------- 02.11 INDEX
index_cols = [
    ('Malaysia &amp; Singapore', [
        'Western Digital (M) Sdn Bhd, Petaling Jaya', 'WD Media (M) Sdn Bhd, Penang, MA 28 &amp; MA 29',
        'Flextronics Shah Alam Sdn Bhd', 'Caterpillar Asia, 7T office renovation',
        'M Project, greenfield food flavouring plant, 40,000 m²', 'P Project, MEP works, mega lab retrofit',
        'National University of Singapore, tissue culture lab', 'Matrix (M) Sdn Bhd',
        'T Hasegawa, spray dryer &amp; microwave tunnel', 'Elegant Aura (M) Sdn Bhd',
        'Rapid MCD chemical plant']),
    ('Europe &amp; Morocco', [
        'Northvolt AB, Skellefteå, 62,000 m²', 'Morrow Batteries, Norway', 'ACC Phase 1, France',
        'Envision, France', 'Soitec Semiconductor, Paris', 'Xfab Semiconductor, Paris',
        'Nemotek, Rabat, Morocco', 'STMicroelectronics, Casablanca', 'Kimoto, Poland', 'Sumika, Poland']),
    ('China', [
        'All-Cent RF Technology, Wuxi, 25,600 m²', 'Kunshan Visionox Display, 27,000 m²',
        'GS Magicdrive Inc., 68,000 m²', 'Shantou Goworld Display', 'M-Flex (Suzhou), 25,000 m²',
        'MMI Industries (Wuxi)', 'Huawei Technologies Co., Ltd', 'Shanghai Roche Pharmaceuticals',
        'Suzhou Ascentage Pharma, 25,800 m²', 'Jiangsu GenScript Biotech', 'Mindray Group Co., Ltd',
        'Unilever · GE · Dow · Rohm and Haas R&amp;D centres']),
]
w_html = ''.join(
    f'<div class="wcol"><h3>{name}</h3><ul>' + ''.join(f'<li>{x}</li>' for x in items) + '</ul></div>'
    for name, items in index_cols)
slide(f'<div class="wall">{w_html}</div>',
      part_idx=1, num='02.11', title='Reference Index',
      note='A selection from 200+ completed projects. The full reference list is available on request.',
      foot='Project References', fill=True)

# ================================================================ PART 03
divider(2, '03', 'Safety, Quality & ESG', 'Sections 03.1 to 03.4', 'klcc-dcp',
        ['Highwire Gold safety award',
         'ISO 45001:2018 occupational health & safety',
         '20 tons per annum carbon footprint reduction'])

# ---------------------------------------------------------------- 03.1 ESG
esg = [
    ('E', 'Environmental Responsibility',
     'Minimising environmental footprint through sustainable design and construction. Energy-efficient solutions and eco-friendly technologies, prioritised at design stage.'),
    ('S', 'Social Accountability',
     'The well-being and safety of employees and communities first. A diverse, inclusive work environment and ethical labour practices.'),
    ('G', 'Corporate Governance',
     'Transparency, accountability and ethical decision-making, with the highest standards of compliance, building trust with clients, partners and stakeholders.'),
]
e_html = ''.join(
    f'''<div class="unit"><div class="u-num">{k}</div><div class="u-body">
      <h3 class="u-name">{esc(n)}</h3><p class="cap">{esc(d)}</p></div></div>'''
    for k, n, d in esg)
slide(f'<div class="units">{e_html}</div>',
      part_idx=2, num='03.1', title='ESG Commitments',
      note='Three pillars, applied to operations and to every project we take on.', fill=True)

# ---------------------------------------------------------------- 03.2 SAFETY
awards = [
    ('Builder of the Year 2024', 'Malaysian Construction Industry Excellence Awards (MCIEA), awarded by CIDB.'),
    ('Highwire Gold', 'Gold-rated contractor safety performance.'),
    ('ISO 45001:2018', 'Occupational health and safety management, certified by Intertek.'),
]
a_html = ''.join(
    f'<div class="award"><h3 class="a-name">{esc(n)}</h3><p class="cap">{esc(d)}</p></div>'
    for n, d in awards)
slide(f'''
    <div class="split">
      <div class="lede">
        <h3 class="statement">Judged on the things<br>that actually matter.</h3>
        <p class="body">MCIEA award recipients are evaluated across company performance, project
        management, technical expertise, innovation, quality, safety and sustainability. The same
        criteria our clients audit us against.</p>
      </div>
      <div class="awards">{a_html}</div>
    </div>''',
      part_idx=2, num='03.2', title='Safety & Recognition',
      note='How our standards are independently verified and recognised.', fill=True)

# ---------------------------------------------------------------- 03.3 CLOSING
slide('''
    <div class="closing">
      <h3 class="statement big">We infuse safety, quality, efficiency and excellence into every project.</h3>
      <p class="body">From engineering design and project management to construction and maintenance,
      across semiconductor manufacturing, clean energy and every environment in between.
      IAQ is your trusted partner for total facility solutions.</p>
    </div>''',
      part_idx=2, num='03.3', title='Closing', dark=True,
      note='Your Total Facility Solutions Provider.')

# ---------------------------------------------------------------- 03.4 CONTACTS
slide('''
    <img class="signoff" src="img/iaq-logo.png" alt="IAQ">
    <div class="contacts">
      <div class="contact">
        <div class="c-nm">Nelson Tan Wee Keong</div>
        <div class="c-rl">Business Development Director</div>
        <div class="c-dt">nelsontan@iaqtechnology.com.my</div>
        <div class="c-dt">+6012-372 7329</div>
      </div>
      <div class="contact">
        <div class="c-nm">Sunny Lim Qin Xiang</div>
        <div class="c-rl">Senior Engineer, Business Development</div>
        <div class="c-dt">qinxiang.lim@iaqtechnology.com.my</div>
        <div class="c-dt">+6016-442 4578</div>
      </div>
    </div>
    <div class="sub">''' + specrows([
        ('General', 'info@iaqtechnology.com.my', False),
        ('Head Office', '9, Jalan Sungai Jeluh 32/192, Kawasan Perindustrian Kemuning, Seksyen 32, 40460 Shah Alam, Selangor, Malaysia', False),
    ]) + '''
    </div>''',
      part_idx=2, num='03.4', title='Contacts', dark=True,
      note='For inquiry and business opportunity.')

# ================================================================ ASSEMBLE
TOTAL = len(slides)
body = '\n\n'.join(slides).replace('/ TOTAL', f'/ {TOTAL}')

CSS = open(os.path.join(os.path.dirname(__file__), 'deck.css')).read()
JS = open(os.path.join(os.path.dirname(__file__), 'deck.js')).read()

doc = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>IAQ Total Facility Solutions</title>
<meta name="description" content="IAQ Group presentation deck covering company, project references and delivery capability.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@500;600;700&family=Urbanist:wght@400;500;600&family=League+Spartan:wght@400;500;600&display=swap">
<style>
{CSS}
</style>
</head>
<body>

<div class="deck" id="deck">

{body}

</div><!-- /deck -->

<nav class="nav" aria-label="Slide navigation">
  <span class="counter" id="counter">01 / {TOTAL}</span>
  <button type="button" id="prev" aria-label="Previous slide">Prev</button>
  <button type="button" id="next" aria-label="Next slide">Next</button>
</nav>

<script>
{JS}
</script>
</body>
</html>
'''
open(OUT, 'w').write(doc)
print(f'wrote {OUT} — {TOTAL} slides, {len(doc)//1024} KB')
