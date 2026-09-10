#!/usr/bin/env python3
"""Generate the IAQ Group presentation deck (index.html)."""
import html, os

OUT = '/home/user/Brand-Method-Website/iaq-deck/index.html'

SERVICE_ICONS = ['<svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="4" rx="1"/><path d="M7 11v7M12 11v7M17 11v7"/><path d="M5.5 16.5L7 18l1.5-1.5M10.5 16.5L12 18l1.5-1.5M15.5 16.5L17 18l1.5-1.5"/></svg>', '<svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="8" rx="1.5"/><path d="M6 9h12"/><path d="M5 18c1.4-1.6 2.8-1.6 4.2 0s2.8 1.6 4.2 0 2.8-1.6 4.2 0"/></svg>', '<svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M3 8h18M3 16h18"/><circle cx="9" cy="8" r="2.2"/><circle cx="15" cy="16" r="2.2"/></svg>', '<svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><rect x="6" y="10" width="12" height="10" rx="1"/><path d="M12 7V2M9.5 4.5L12 2l2.5 2.5"/></svg>', '<svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><rect x="7" y="6" width="10" height="15" rx="2.5"/><path d="M10 6V4h4v2M7 11h10"/></svg>', '<svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3c4 5.2 6 7.7 6 10.2A6 6 0 016 13.2C6 10.7 8 8.2 12 3z"/></svg>', '<svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="8" width="16" height="12" rx="1"/><path d="M4 13c2-1.5 4-1.5 6 0s4 1.5 6 0 2-1 4 0"/><path d="M9 5h6"/></svg>', '<svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21a5 5 0 005-5c0-4-5-8-5-8s-5 4-5 8a5 5 0 005 5z"/><path d="M4 4h16M12 4v3"/></svg>', '<svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2L5 14h6l-1 8 8-12h-6z"/></svg>', '<svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M3 21h18M6 21V8l6-5 6 5v13"/><path d="M10 21v-6h4v6"/></svg>', '<svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="13" rx="1"/><path d="M8 21h8M12 17v4"/><path d="M7 12l3-3 2.5 2.5L17 7"/></svg>', '<svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><circle cx="7" cy="7" r="3"/><circle cx="17" cy="17" r="3"/><path d="M9.2 9.2l5.6 5.6"/></svg>']
INDUSTRY_ICONS = ['<svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><rect x="7" y="7" width="10" height="10" rx="1"/><path d="M10 3v4M14 3v4M10 17v4M14 17v4M3 10h4M3 14h4M17 10h4M17 14h4"/></svg>', '<svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="4" width="16" height="5" rx="1"/><rect x="4" y="11" width="16" height="5" rx="1"/><rect x="4" y="18" width="16" height="3" rx="1"/><path d="M7 6.5h.01M7 13.5h.01"/></svg>', '<svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="7" width="15" height="10" rx="2"/><path d="M18 11h3v2h-3"/><path d="M11 9.5l-2 3h3l-2 3"/></svg>', '<svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v18M4.5 7.5l15 9M19.5 7.5l-15 9"/></svg>', '<svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M4.5 17h15l-2-9h-11z"/><path d="M8 8l-1.2 9M16 8l1.2 9M5.6 12.5h12.8"/><path d="M12 4V2"/></svg>', '<svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="9" width="16" height="11" rx="2"/><path d="M9 9V6.5a3 3 0 016 0V9"/><path d="M12 12.5v4M10 14.5h4"/></svg>', '<svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M6.5 8h11l-1.4 12h-8.2z"/><path d="M17.5 10h2a2 2 0 010 4h-1.6"/><path d="M9 5V3M13 5V3"/></svg>', '<svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M12 8v8M8 12h8"/></svg>']

# ---------------------------------------------------------------- helpers
def esc(t):
    return html.escape(t, quote=False)

slides = []          # list of html strings
STAT_ICONS = [
 '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M12 6.6v5.7l3.6 2.1"/></svg>',
 '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="9.2" cy="8" r="3.2"/><path d="M3.4 20c0-3.3 2.6-5.6 5.8-5.6s5.8 2.3 5.8 5.6"/><path d="M16.2 5.4a3.2 3.2 0 010 5.6M17.6 14.8c1.9.9 3 2.7 3 5.2"/></svg>',
 '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="4.5" y="4" width="15" height="17" rx="2"/><path d="M9 4V2.6h6V4"/><path d="M8.4 12.6l2.6 2.6 4.6-5.2"/></svg>',
 '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="3.2" y="3.2" width="17.6" height="17.6" rx="2"/><path d="M8 12V8h4M16 12v4h-4"/><path d="M8 8l8 8"/></svg>',
 '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M3.2 12h17.6"/><path d="M12 3c2.6 2.7 3.9 5.7 3.9 9s-1.3 6.3-3.9 9c-2.6-2.7-3.9-5.7-3.9-9S9.4 5.7 12 3z"/></svg>',
 '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20.2 3.8c0 9.1-4.9 13.7-11.1 13.7H5.4C5.4 9.4 11 3.8 20.2 3.8z"/><path d="M3.8 21c1.5-4.6 4.1-7.5 7.7-9.6"/></svg>',
]

PH_ICON = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" '
           'stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="2"/>'
           '<circle cx="8.6" cy="10" r="1.7"/><path d="M3.4 17.6l5.2-5.2 4 4 3.1-2.6 4.9 4.6"/></svg>')

def ph(note, dark=False, cap='Visual Placeholder'):
    """A holding block that states which photograph belongs in this frame."""
    return ('<figure class="ph%s"><span class="ph-frame">%s</span>'
            '<span class="ph-cap">%s</span><span class="ph-note">%s</span></figure>'
            % (' dark' if dark else '', PH_ICON, esc(cap), esc(note)))

MAIL_ICON = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" '
             'stroke-linecap="round" stroke-linejoin="round"><rect x="2.6" y="5" width="18.8" height="14" rx="2"/>'
             '<path d="M3.4 6.6l8.6 6 8.6-6"/></svg>')

PHONE_ICON = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" '
              'stroke-linecap="round" stroke-linejoin="round"><path d="M7.4 3.2H4.8a2 2 0 00-2 2.2c.5 8.2 6.6 '
              '14.3 14.8 14.8a2 2 0 002.2-2v-2.6a1.4 1.4 0 00-1.2-1.4l-2.9-.4a1.4 1.4 0 00-1.4.7l-.9 1.6a13 13 '
              '0 01-5.8-5.8l1.6-.9a1.4 1.4 0 00.7-1.4l-.4-2.9a1.4 1.4 0 00-1.4-1.2z"/></svg>')

def person(name, role, mail, tel):
    return ('<article class="ccard"><span class="cc-role">%s</span>'
            '<h3 class="cc-person">%s</h3>'
            '<span class="cc-line">%s<span>%s</span></span>'
            '<span class="cc-line">%s<span>%s</span></span></article>'
            % (esc(role), esc(name), MAIL_ICON, esc(mail), PHONE_ICON, esc(tel)))

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
          dark=False, bare=False, cls='', fill=False, rows=False):
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
    <div class="tl-r"><img class="mark" src="img/iaq-logo.png" alt="IAQ"></div>
  </div>{head}
  <div class="canvas{' fill' if fill else ''}{' rows' if rows else ''}">{body}
  </div>
  <footer class="botline">
    <div class="bl-l"><span class="folio">{i:02d} / TOTAL</span></div>
    <div class="bl-c">{dots}</div>
    <div class="bl-r">{esc(foot)}</div>
  </footer>
</section></div>''')


def raw_slide(inner, dark=True):
    i = len(slides) + 1
    slides.append(f'''<div class="stage"><section class="slide cover{' dark' if dark else ''}">
{inner}
  <footer class="botline">
    <div class="bl-l"><span class="folio">{i:02d} / TOTAL<span class="edition">· Edition 2026</span></span></div>
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
    <div class="tl-r"><img class="mark" src="img/iaq-logo.png" alt="IAQ"></div>
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
raw_slide('''  <div class="cover-media"><img src="img/iaq-hq.jpg" alt="IAQ Solutions headquarters"></div>
  <div class="topline">
    <div class="tl-l"><span class="tl-part">Your Total Facility Solutions Provider</span></div>
    <div class="tl-r">Company Deck</div>
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
      foot='Contents', fill=True, rows=True)

# ================================================================ PART 01
def divider(part_idx, num, name, note, img, bullets, ph_note=None):
    i = len(slides) + 1
    if ph_note:
        media, ph_cls = ph(ph_note, dark=True), ' is-ph'
    else:
        media, ph_cls = f'<img src="img/{img}.jpg" alt="">', ''
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
    <div class="div-media{ph_cls}">{media}</div>
  </div>
  <div class="topline">
    <div class="tl-l"><span class="tl-part">Part {num} · {esc(name)}</span></div>
    <div class="tl-r"><img class="mark" src="img/iaq-logo.png" alt="IAQ"></div>
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
      <div class="colcards c1">
        <article class="colcard flat"><div class="cc-body"><h3 class="cc-name">Vision</h3><p class="cc-note">To be a regional facility solutions provider with engineering excellence that facilitates technological innovation and advancement in quality of life.</p></div></article><article class="colcard flat"><div class="cc-body"><h3 class="cc-name">Mission</h3><p class="cc-note">Providing innovative, sustainable facility and engineering solutions benefitting our clients and stakeholders, driven by our leadership, employees and partners globally.</p></div></article><article class="colcard flat"><div class="cc-body"><h3 class="cc-name">Delivery Models</h3><p class="cc-spec">EPCM · EPCC · Energy Facility Management</p><p class="cc-note">Engineering and construction management, full EPCC from design through commissioning, and ongoing energy and facility management.</p></div></article>
      </div>
    </div>''',
      part_idx=0, num='01.1', title='About IAQ',
      note='Who we are, what we build, and the models we deliver under.', fill=True)

# ---------------------------------------------------------------- 01.2 GLANCE
stats = [('32', '', 'Years Experience'), ('450', '', 'Employees'),
         ('200', '+', 'Projects Completed'), ('1.5', 'mil m²', 'Cleanroom Built-Up Area'),
         ('6', '', 'Global Offices'), ('20', 't / yr', 'Carbon Footprint Reduced')]
stat_html = ''.join(
    f'<div class="stat"><span class="st-ico">{STAT_ICONS[k]}</span>'
    f'<div class="st-body"><div class="num">{v}<span>{u}</span></div>'
    f'<div class="label">{esc(l)}</div></div></div>'
    for k, (v, u, l) in enumerate(stats))
certs = [('Intertek', 'ISO 9001:2015'), ('Intertek', 'ISO 14001:2015'), ('Intertek', 'ISO 45001:2018'),
         ('CIDB', 'Grade G7'), ('PKK', 'Grade G7'), ('Highwire Safety', 'Gold Award'),
         ('MCIEA 2024', 'Builder of the Year')]
cert_html = ''.join(f'<span class="cert">{esc(a)} <strong>{esc(b)}</strong></span>' for a, b in certs)
ph_glance = ph('Corporate facility exterior, IAQ delivered project')
slide(f'''
    <div class="glance">
      <div class="side-media is-ph">{ph_glance}</div>
      <div class="stats iconic">{stat_html}</div>
    </div>
    <div class="sub">
      <div class="label">Certification &amp; Recognition</div>
      <div class="certs">{cert_html}</div>
    </div>''',
      part_idx=0, num='01.2', title='IAQ at a Glance',
      note='The company in six numbers, and the certifications that stand behind them.', fill=True)

# ---------------------------------------------------------------- 01.3 MILESTONES
slide('<div class="colcards c5 eras-v"><article class="colcard"><img src="img/st-johor.jpg" alt=""><div class="cc-body"><div class="cc-num">1994<span class="to">&ndash;</span>2000</div><h3 class="cc-name">Foundation</h3><ul class="mile"><li><span class="yr">1994</span><span class="ev">Established as a cleanroom specialist</span></li><li><span class="yr">2000</span><span class="ev">First decade of cleanroom delivery in Malaysia</span></li></ul></div></article><article class="colcard"><img src="img/memc-ipoh.jpg" alt=""><div class="cc-body"><div class="cc-num">2006<span class="to">&ndash;</span>2009</div><h3 class="cc-name">Regional Expansion</h3><ul class="mile"><li><span class="yr">2006</span><span class="ev">(EPCC) ST Microelectronics, Class 10K cleanroom</span></li><li><span class="yr">2008</span><span class="ev">(PCC) Western Digital PJ, Class 10 cleanroom</span></li><li><span class="yr">2009</span><span class="ev">(GC / D&amp;B) MEMC Ipoh, Class 1 cleanroom</span></li></ul></div></article><article class="colcard"><img src="img/klcc-dcp.jpg" alt=""><div class="cc-body"><div class="cc-num">2013<span class="to">&ndash;</span>2017</div><h3 class="cc-name">Landmark Plants</h3><ul class="mile"><li><span class="yr">2013</span><span class="ev">(GC) KLCC DCC Plant, largest in Malaysia</span></li><li><span class="yr">2016</span><span class="ev">(EPCC) SilTerra FAB · (EPC) Infineon MKZ Class 1K</span></li><li><span class="yr">2017</span><span class="ev">(GC) Ain Medicare</span></li></ul></div></article><article class="colcard"><img src="img/bosch-testing.jpg" alt=""><div class="cc-body"><div class="cc-num">2020<span class="to">&ndash;</span>2022</div><h3 class="cc-name">Global Scale</h3><ul class="mile"><li><span class="yr">2020</span><span class="ev">(GC) Vital Healthcare</span></li><li><span class="yr">2021</span><span class="ev">(GC / PCC) Robert Bosch · P Project</span></li><li><span class="yr">2022</span><span class="ev">(PCC) Microsoft Data Center · (EPCM / D&amp;B) Soitec PR1A</span></li></ul></div></article><article class="colcard"><img src="img/xfab-kuching.jpg" alt=""><div class="cc-body"><div class="cc-num">2023<span class="to">&ndash;</span>2026</div><h3 class="cc-name">Advanced Technology</h3><ul class="mile"><li><span class="yr">2023</span><span class="ev">(GC / D&amp;B) XFAB 40K Expansion</span></li><li><span class="yr">2025</span><span class="ev">(PCC) 160MW hyperscale data centre · (EPCC) ESCM Germany</span></li><li><span class="yr">2026</span><span class="ev">(D&amp;B) Tata Dholera DF1 · (EPCM / HU) Micron MSH</span></li></ul></div></article></div>',
      part_idx=0, num='01.3', title='Milestones',
      note='Landmark projects from 1994 to 2026, grouped into five eras of growth. The full project list is in 02.11.', fill=True)

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
    <div class="foot-grid">
      <div class="side-media"><img src="img/map-world.jpg" alt="IAQ offices worldwide"></div>
      <div class="mkts"><div class="mkt"><svg class="flg" viewBox="0 0 48 24" preserveAspectRatio="xMidYMid meet"><rect width="48" height="24" fill="#fff"/><rect y="0.00" width="48" height="1.71" fill="#CC0001"/><rect y="3.43" width="48" height="1.71" fill="#CC0001"/><rect y="6.86" width="48" height="1.71" fill="#CC0001"/><rect y="10.28" width="48" height="1.71" fill="#CC0001"/><rect y="13.71" width="48" height="1.71" fill="#CC0001"/><rect y="17.14" width="48" height="1.71" fill="#CC0001"/><rect y="20.57" width="48" height="1.71" fill="#CC0001"/><rect width="24" height="13.71" fill="#010066"/><circle cx="9.4" cy="6.9" r="4.2" fill="#FC0"/><circle cx="11.3" cy="6.9" r="3.7" fill="#010066"/><path d="M16.8 3.1l.83 2.55h2.68l-2.17 1.58.83 2.55-2.17-1.58-2.17 1.58.83-2.55-2.17-1.58h2.68z" fill="#FC0"/></svg><div class="mk-yr">1994</div><div class="mk-tx"><h3 class="mk-name">Malaysia</h3><p class="mk-note">Turnkey design, procurement, construction and commissioning for hi-tech clients. Selangor (HQ), Penang, Johor and Kuching.</p></div></div><div class="mkt"><svg class="flg" viewBox="0 0 48 30" preserveAspectRatio="xMidYMid meet"><rect width="48" height="30" fill="#006AA7"/><rect y="12" width="48" height="6" fill="#FECC00"/><rect x="13" width="6" height="30" fill="#FECC00"/></svg><div class="mk-yr">2020</div><div class="mk-tx"><h3 class="mk-name">Sweden</h3><p class="mk-note">Gigafactory construction for EV battery manufacture, part of Europe&rsquo;s clean and digital transition.</p></div></div><div class="mkt"><svg class="flg" viewBox="0 0 48 32" preserveAspectRatio="xMidYMid meet"><rect width="48" height="32" fill="#fff"/><rect width="48" height="16" fill="#ED2939"/><circle cx="10.5" cy="8" r="5.6" fill="#fff"/><circle cx="13.2" cy="8" r="4.8" fill="#ED2939"/><g fill="#fff"><circle cx="18" cy="4.6" r="1"/><circle cx="21.4" cy="7" r="1"/><circle cx="20.1" cy="11" r="1"/><circle cx="15.9" cy="11" r="1"/><circle cx="14.6" cy="7" r="1"/></g></svg><div class="mk-yr">2023</div><div class="mk-tx"><h3 class="mk-name">Singapore</h3><p class="mk-note">Design &amp; build EPCM services to global semiconductor clients.</p></div></div><div class="mkt"><svg class="flg" viewBox="0 0 48 30" preserveAspectRatio="xMidYMid meet"><rect width="48" height="10" fill="#000"/><rect y="10" width="48" height="10" fill="#D00"/><rect y="20" width="48" height="10" fill="#FFCE00"/></svg><div class="mk-yr">2025</div><div class="mk-tx"><h3 class="mk-name">Germany</h3><p class="mk-note">EPCC services following semiconductor expansion in Europe.</p></div></div><div class="mkt"><svg class="flg" viewBox="0 0 48 32" preserveAspectRatio="xMidYMid meet"><rect width="48" height="10.7" fill="#F93"/><rect y="10.7" width="48" height="10.6" fill="#fff"/><rect y="21.3" width="48" height="10.7" fill="#138808"/><circle cx="24" cy="16" r="4" fill="none" stroke="#008" stroke-width="1"/><circle cx="24" cy="16" r="1.1" fill="#008"/></svg><div class="mk-yr">2026</div><div class="mk-tx"><h3 class="mk-name">India · United States</h3><p class="mk-note">D&amp;B turnkey for India&rsquo;s first wafer fab, and US entry following localisation of advanced tech facilities.</p></div></div><div class="mk-more"><span class="label">Additional Offices</span><span class="offs"><span class="off"><svg class="flg" viewBox="0 0 48 35" preserveAspectRatio="xMidYMid meet"><rect width="48" height="35" fill="#BA0C2F"/><rect y="13" width="48" height="9" fill="#fff"/><rect x="11" width="9" height="35" fill="#fff"/><rect y="15.5" width="48" height="4" fill="#00205B"/><rect x="13.5" width="4" height="35" fill="#00205B"/></svg>Norway</span><span class="off"><svg class="flg" viewBox="0 0 48 32" preserveAspectRatio="xMidYMid meet"><rect width="48" height="32" fill="#DE2910"/><path d="M9 4l1.4 4.3H15l-3.7 2.7 1.4 4.3L9 12.6l-3.7 2.7 1.4-4.3L3 8.3h4.6z" fill="#FFDE00"/><g fill="#FFDE00"><circle cx="18" cy="4" r="1.3"/><circle cx="21.5" cy="7.5" r="1.3"/><circle cx="21.5" cy="12.5" r="1.3"/><circle cx="18" cy="16" r="1.3"/></g></svg>China</span><span class="off"><svg class="flg" viewBox="0 0 48 32" preserveAspectRatio="xMidYMid meet"><rect width="16" height="32" fill="#002395"/><rect x="16" width="16" height="32" fill="#fff"/><rect x="32" width="16" height="32" fill="#ED2939"/></svg>France</span><span class="off"><svg class="flg" viewBox="0 0 48 30" preserveAspectRatio="xMidYMid meet"><rect width="48" height="15" fill="#fff"/><rect y="15" width="48" height="15" fill="#DC143C"/></svg>Poland</span></span></div></div>
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
ph_bu1 = ph('EPCC delivery on an active construction site')
ph_bu2 = ph('Process critical utilities and tool installation inside a fab')
ph_bu3 = ph('Energy plant and facility management operations')
slide(f'<div class="colcards c3"><article class="colcard">{ph_bu1}<div class="cc-body"><div class="cc-num">01</div><h3 class="cc-name">IAQ Solutions Sdn Bhd</h3><p class="cc-spec">Engineering, Procurement, Construction &amp; Commissioning</p><p class="cc-note">EPCC from conception to operation, completion and maintenance. Every stage managed, from initial design through commissioning, so clients in hi-tech industries can bring their visions to life.</p></div></article><article class="colcard">{ph_bu2}<div class="cc-body"><div class="cc-num">02</div><h3 class="cc-name">IAQ Utility Solutions Sdn Bhd</h3><p class="cc-spec">Process Critical Utilities &amp; Total Tool Install</p><p class="cc-note">EPCM partner for semiconductor manufacturing: process-critical utility infrastructure and total tool installation, bridging facility readiness and manufacturing start-up to accelerate fab ramp-up.</p></div></article><article class="colcard">{ph_bu3}<div class="cc-body"><div class="cc-num">03</div><h3 class="cc-name">IAQ Energy Facility Management Sdn Bhd</h3><p class="cc-spec">Energy Management</p><p class="cc-note">Energy management solutions that optimise operations and reduce carbon footprint, keeping facilities running at the highest levels of efficiency and sustainability.</p></div></article></div>',
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
    f'<div class="chip">{SERVICE_ICONS[k-1]}<span class="c-num">{k:02d}</span>'
    f'<span class="c-name">{n}</span><span class="c-note">{d}</span></div>'
    for k, (n, d) in enumerate(scope, start=1))
slide(f'<div class="chips four">{s_html}</div>',
      part_idx=0, num='01.7', title='Scope of Services',
      note='Twelve packages, self-performed and integrated under one contract.')

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
    f'<div class="chip">{INDUSTRY_ICONS[k-1]}<span class="c-num">{k:02d}</span>'
    f'<span class="c-name">{n}</span><span class="c-note">{d}</span></div>'
    for k, (n, d) in enumerate(inds, start=1))
i_html += ('<div class="chip solid">' + INDUSTRY_ICONS[7] + '<span class="c-num">+</span>'
           '<span class="c-name">Your facility next</span>'
           '<span class="c-note">Total facility solutions, end to end</span></div>')
slide(f'<div class="chips four">{i_html}</div>',
      part_idx=0, num='01.8', title='Industry Focus',
      note='Seven sectors, one discipline: contamination control under code and class.')

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

# ---------------------------------------------------------------- 02.2 to 02.10
# One slide per category, two projects on each, a single card format throughout.
slide('<div class="grid two">' + pcard('infineon-kulim', 'Kulim, Kedah · greenfield wafer fab', 'Infineon Kulim Wafer Fab 3', [('Cleanroom', 'ISO 4 · 5 · 6 · 7 (Class 10 · 100 · 1K · 10K)', True), ('Scope', 'PCC for cleanroom and mechanical works', False), ('Description', 'General contractor for WP06, KLM3 Expansion, 35,000 m² cleanroom area', False)]) + pcard('p-project', 'Advanced packaging · 75,000 m²', 'P Project', [('Cleanroom', 'ISO 4 to 7 (Class 10 to 10K)', True), ('Scope', 'Design & build GC: CSA, MEP, process utilities, chemical & gases system, waste treatment', False), ('Description', "Progressive-built EPCM contract model for the client's advanced packaging facility", False)]) + '\n    </div>',
      part_idx=1, num='02.2', title='Semiconductor · Malaysia',
      note='Wafer fab, advanced packaging, test and assembly. Further Malaysian projects are listed in 02.11.',
      foot='Semiconductor · Malaysia')

slide('<div class="grid two">' + pcard('teksend', 'Photomask facility', 'Teksend Photomask', [('Cleanroom', 'Class 1 to Class 10K', True), ('Scope', 'EPCC for cleanroom, ACMV, electrical, process utility, BMS, PA, WWT, UPW, tool hookup', False), ('Description', 'Addition and alteration to an existing two-storey building with cleanroom facilities and ancillary office', False)]) + pcard('micron-msh', 'Progressive tool hookup', 'Micron MSH Tool HU', [('Scope', 'Progressive tool hook up', False), ('Description', '2,000 progressive tool hookup services for MSH', False)]) + '\n    </div>',
      part_idx=1, num='02.3', title='Semiconductor · Singapore',
      note='Design & build EPCM in Singapore since 2023.',
      foot='Semiconductor · Singapore')

slide('<div class="grid two">' + pcard('hyperscale-dc', 'Client confidential · 160 MW', 'Hyperscale Data Centre', [('Scope', 'Construction, completion, testing & commissioning for mechanical packages 1 & 2', False), ('Description', 'Office, data halls and mechanical utility building', False)]) + pcard('microsoft-kul03', 'KUL03 Phase 1 · 9.6 MW', 'Microsoft DTC-KUL 03', [('Scope', 'PCC for CHW and CW piping works', False), ('Description', '9.6 MW data centre', False)]) + '\n    </div>',
      part_idx=1, num='02.4', title='Data Centre',
      note='Hyperscale and colocation, 9.6 MW to 160 MW.',
      foot='Data Centre')

slide('<div class="grid two">' + pcard('northvolt', 'Skellefteå, Sweden · 62,000 m²', 'Northvolt AB Gigafactory', [('Environment', 'Dry Room', True), ('Scope', 'Cleanroom and dry room architecture works', False), ('Description', 'Europe gigafactory for lithium-ion battery manufacture', False)]) + pcard('morrow', 'Norway · Battery Coast · 8,600 m²', 'Morrow Batteries', [('Environment', 'Dry Room', True), ('Scope', 'Cleanroom and dry room architectural system, ACMV', False), ('Description', "Norway's Battery Coast project", False)]) + '\n    </div>',
      part_idx=1, num='02.5', title='EV Battery · Europe',
      note='Dry rooms for the gigafactories: moisture control and contamination control at scale.',
      foot='EV Battery · Europe')

slide('<div class="grid two">' + pcard('confidential-cmos', 'Client confidential · wafer fab', '28/22nm CMOS · 16/12nm FinFET Plant', [('Cleanroom', 'Class 1 to Class 10K', True), ('Scope', 'Cleanroom & mechanical general contractor', False), ('Description', 'Design, supply, installation & commissioning of cleanroom facilities', False)]) + pcard('st-casablanca', 'Casablanca, Morocco · 60,000 m²', 'STMicroelectronics', [('Cleanroom', 'ISO 5 (Class 100)', True), ('Scope', 'Cleanroom, mechanical, electrical, process utilities and hookup works', False)]) + '\n    </div>',
      part_idx=1, num='02.6', title='Semiconductor · Europe & Morocco',
      note='Following the fabs into Europe: advanced-node cleanrooms and progressive hookup.',
      foot='Semiconductor · Europe')

slide('<div class="grid two">' + pcard('ferrotec-hangzhou', 'Hangzhou · 23,400 m²', 'Ferrotec Semiconductor', [('Cleanroom', 'ISO 4 · 5 (Class 10 & 100)', True), ('Scope', 'EPCC for cleanroom, mechanical, electrical and plumbing works and hookup', False)]) + pcard('infineon-wuxi', 'Wuxi · 8,000 m²', 'Infineon Technologies', [('Cleanroom', 'ISO 5 (Class 100)', True), ('Scope', 'EPCC for cleanroom, mechanical, electrical and plumbing works and hookup', False)]) + '\n    </div>',
      part_idx=1, num='02.7', title='Semiconductor & Display · China',
      note='EPCC across semiconductor, display and precision manufacturing.',
      foot='China')

slide('<div class="grid two">' + pcard('first-solar', 'Kulim, Malaysia', 'First Solar Malaysia', [('Scope', 'PCC for mechanical & electrical, KMW building; CSA and M&E for forming gas plant; M&E for SCO1', False)]) + pcard('chint-solar', 'China · 57,000 m²', 'Chint Solar Technology', [('Cleanroom', 'ISO 8 (Class 100K)', True), ('Scope', 'Cleanroom system, ACMV, process utilities and tools hookup', False)]) + '\n    </div>',
      part_idx=1, num='02.8', title='Photovoltaics',
      note='Solar cell and module manufacturing, including toxic material and waste handling.',
      foot='Photovoltaics')

slide('<div class="grid two">' + pcard('insulet', 'Greenfield · medical device', 'Insulet', [('Cleanroom', 'ISO 8 (Class 100K)', True), ('Scope', 'Design and build mechanical, cleanroom & electrical package', False)]) + pcard('pharmaniaga', 'Puchong, Selangor', 'Pharmaniaga', [('Cleanroom', 'ISO 5 · 7 · 8 (Class 100 · 10K · 100K)', True), ('Scope', 'Cleanroom system and ACMV for a small volume parenteral facility', False)]) + '\n    </div>',
      part_idx=1, num='02.9', title='Pharmaceutical & Medical',
      note='GMP grades and regulated environments, from parenteral facilities to medical device plants.',
      foot='Pharmaceutical & Medical')

slide('<div class="grid two">' + pcard('klcc-dcp', 'Gas District Cooling (M) Sdn Bhd', 'KLCC District Cooling Plant', [('Description', 'Largest district cooling centre in Malaysia', True), ('Scope', 'ACMV, electrical & instrumentation, fire protection, process utility, plumbing & sanitary, water treatment, CSA', False)]) + pcard('gdc-putrajaya', 'PICC Plant, Putrajaya', 'GDC Putrajaya', [('Scope', 'EPCC of plant electrification, chiller replacement and associated works at Gas District Cooling Putrajaya', False)]) + '\n    </div>',
      part_idx=1, num='02.10', title='District Cooling & Energy',
      note='Plant, chillers and co-generation for urban and industrial energy.',
      foot='District Cooling & Energy')

# ---------------------------------------------------------------- 02.11 INDEX
index_cols = [('Malaysia · Semiconductor', ['XFAB Kuching 40K Expansion, 40,000 m²', 'SOITEC PR1A Expansion, 45,000 m²', 'Robert Bosch Testing Manufacturing Plant', 'Wafer Fab Facility &amp; Expansion, FAB1E A/B', 'Texas Instruments, Melaka, 32,000 m²', 'Infineon Technologies, Melaka, Block 8', 'MEMC Ipoh, Class 1 cleanroom', 'STMicroelectronics, Johor', 'Western Digital (M), Petaling Jaya', 'WD Media (M), Penang, MA 28 &amp; MA 29', 'Flextronics Shah Alam']), ('Malaysia · Other Sectors &amp; Singapore', ['AUO Sunpower, Melaka, Fab 3A', 'Vital Healthcare, medical device plant', 'Ain Medicare, pharmaceutical building', 'M Project, food flavouring plant, 40,000 m²', 'P Project, MEP works, mega lab retrofit', 'Rapid Petronas Pengerang Co-gen', 'Pagoh Education Hub DCS', 'Rapid MCD chemical plant', 'Matrix (M) Sdn Bhd', 'T Hasegawa, spray dryer &amp; microwave tunnel', 'Elegant Aura (M) Sdn Bhd', 'Caterpillar Asia, 7T office renovation', 'Micron F10A &amp; F10NX, Singapore', 'National University of Singapore, tissue culture lab']), ('Europe &amp; Morocco', ['ACC Phase 1, France, 35,000 m²', 'Envision, France', 'Soitec Semiconductor, Paris, 11,000 m²', 'Xfab Semiconductor, Paris', 'Nemotek, Rabat, Morocco', 'Kimoto, Poland', 'Sumika, Poland']), ('China', ['SMIC, Ningbo, 22,000 m²', 'Maxtor Technology, Suzhou, 95,000 m²', 'All-Cent RF Technology, Wuxi, 25,600 m²', 'Kunshan Visionox Display, 27,000 m²', 'GS Magicdrive Inc., 68,000 m²', 'Shantou Goworld Display', 'M-Flex (Suzhou), 25,000 m²', 'MMI Industries (Wuxi)', 'Huawei Technologies Co., Ltd', 'Shanghai Roche Pharmaceuticals', 'Suzhou Ascentage Pharma, 25,800 m²', 'Jiangsu GenScript Biotech', 'Mindray Group Co., Ltd', 'Unilever · GE · Dow · Rohm and Haas R&amp;D centres'])]
w_html = ''.join(
    f'<div class="wcol"><h3>{name}</h3><ul>' + ''.join(f'<li>{x}</li>' for x in items) + '</ul></div>'
    for name, items in index_cols)
slide(f'<div class="wall w4">{w_html}</div>',
      part_idx=1, num='02.11', title='Reference Index',
      note='A selection from 200+ completed projects. The full reference list is available on request.',
      foot='Project References', fill=True, rows=True)

# ================================================================ PART 03
divider(2, '03', 'Safety, Quality & ESG', 'Sections 03.1 to 03.4', None,
        ['Highwire Gold safety award',
         'ISO 45001:2018 occupational health & safety',
         '20 tons per annum carbon footprint reduction'],
        ph_note='Site safety in practice: crew in full PPE, toolbox briefing or EHS walkdown on an IAQ site')

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
slide('<div class="colcards c3"><article class="colcard"><img src="img/value-2.jpg" alt=""><div class="cc-body"><div class="cc-num">E</div><h3 class="cc-name">Environmental Responsibility</h3><p class="cc-note">Minimising environmental footprint through sustainable design and construction. Energy-efficient solutions and eco-friendly technologies, prioritised at design stage.</p></div></article><article class="colcard"><img src="img/value-3.jpg" alt=""><div class="cc-body"><div class="cc-num">S</div><h3 class="cc-name">Social Accountability</h3><p class="cc-note">The well-being and safety of employees and communities first. A diverse, inclusive work environment and ethical labour practices.</p></div></article><article class="colcard"><img src="img/value-4.jpg" alt=""><div class="cc-body"><div class="cc-num">G</div><h3 class="cc-name">Corporate Governance</h3><p class="cc-note">Transparency, accountability and ethical decision-making, with the highest standards of compliance, building trust with clients, partners and stakeholders.</p></div></article></div>',
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
    <div class="split media">
      <div class="lede">
        <h3 class="statement">Judged on the things<br>that actually matter.</h3>
        <p class="body">MCIEA award recipients are evaluated across company performance, project
        management, technical expertise, innovation, quality, safety and sustainability. The same
        criteria our clients audit us against.</p>
        <div class="awards">{a_html}</div>
      </div>
      <div class="side-media"><img src="img/p-project.jpg" alt="IAQ project site"></div>
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
people = [
    ('Nelson Tan Wee Keong', 'Business Development Director',
     'nelsontan@iaqtechnology.com.my', '+6012-372 7329'),
    ('Sunny Lim Qin Xiang', 'Senior Engineer, Business Development',
     'qinxiang.lim@iaqtechnology.com.my', '+6016-442 4578'),
]
cards = ''.join(person(*p) for p in people)
rows = [('General', 'info@iaqtechnology.com.my'),
        ('Head Office', '9, Jalan Sungai Jeluh 32/192, Kawasan Perindustrian Kemuning, '
                        'Seksyen 32, 40460 Shah Alam, Selangor, Malaysia')]
row_html = ''.join('<div class="er"><dt>%s</dt><dd>%s</dd></div>' % (esc(a), esc(b)) for a, b in rows)
slide(f"""
    <div class="endgrid">
      <div class="endmark">
        <img class="signoff" src="img/iaq-logo.png" alt="IAQ">
        <div class="end-tag">Your Total Facility Solutions Provider</div>
        <p class="end-line">Engineering, procurement, construction and energy management
        for the industries where contamination, uptime and safety decide the outcome.
        Established 1994.</p>
      </div>
      <div class="ccards">{cards}</div>
      <dl class="endrows">{row_html}</dl>
    </div>""",
      part_idx=2, num='03.4', title='Contacts', dark=True,
      note='For inquiry and business opportunity.', fill=True)

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

<div class="progress" aria-hidden="true"><span id="bar"></span></div>

<nav class="nav" aria-label="Presentation controls">
  <button type="button" id="btn-grid" aria-label="Slide overview (O)">Overview</button>
  <span class="counter" id="counter" aria-live="polite">01 / {TOTAL}</span>
  <button type="button" id="prev" aria-label="Previous slide">Prev</button>
  <button type="button" id="next" aria-label="Next slide">Next</button>
  <span class="timer" id="timer" role="timer">00:00</span>
  <button type="button" id="btn-full" aria-label="Present full screen (F)">Present</button>
  <button type="button" id="btn-help" class="sq" aria-label="Keyboard shortcuts">?</button>
</nav>

<div class="overview" id="overview" hidden>
  <div class="ov-head">
    <span class="ov-title">IAQ Company Deck</span>
    <span class="ov-hint">Click a slide to jump &middot; type a number and press Enter</span>
    <button type="button" id="ov-close" aria-label="Close overview">Close</button>
  </div>
  <div class="ov-grid" id="ovGrid"></div>
</div>

<div class="helpbox" id="help" hidden>
  <div class="hb-title">Presenter shortcuts</div>
  <dl class="hb-list">
    <div><dt>&rarr; &nbsp;Space</dt><dd>Next slide</dd></div>
    <div><dt>&larr;</dt><dd>Previous slide</dd></div>
    <div><dt>F</dt><dd>Present full screen</dd></div>
    <div><dt>O</dt><dd>Slide overview</dd></div>
    <div><dt>B</dt><dd>Blank the screen</dd></div>
    <div><dt>T</dt><dd>Pause or resume the timer</dd></div>
    <div><dt>0&ndash;9 then Enter</dt><dd>Jump to a slide</dd></div>
    <div><dt>Home &nbsp;End</dt><dd>First or last slide</dd></div>
    <div><dt>Esc</dt><dd>Close, or leave full screen</dd></div>
  </dl>
</div>

<div class="blackout" id="blackout" hidden></div>

<script>
{JS}
</script>
</body>
</html>
'''
open(OUT, 'w').write(doc)
print(f'wrote {OUT} — {TOTAL} slides, {len(doc)//1024} KB')
