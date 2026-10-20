#!/usr/bin/env python3
"""Build the IAQ master template: every layout a client starts a new slide from.

Each layout is written twice over — once filled with real IAQ content so the
client can see what good looks like, once empty with a line in every box
saying what belongs there. The pair is what gets handed over; the empty one
is also what the PowerPoint template's layout is cut from.
"""
import html, io, os, sys

DECK = '/home/user/Brand-Method-Website/iaq-deck/'
# the template itself is the empty set: a client opens it, copies the page they
# need and types into it. The paired build keeps a worked example beside each
# one, for reference rather than for use.
EMPTY_ONLY = 'paired' not in sys.argv
OUT = DECK + ('template.html' if not EMPTY_ONLY else 'template-empty.html')
LEGAL = 'IAQ Technology International Sdn Bhd'

esc = lambda t: html.escape(t, quote=False)
slides = []
index = []          # (number, name, purpose) for the contents page


def page(body, *, name, title, note, foot, twin=False, dark=False, cls='',
         bare=False, fill=False, raw=False):
    n = len(slides) + 1
    head = '' if bare else f'''
    <header class="shead">
      <h2 class="s-title">{esc(title)}</h2>
      <p class="s-note">{esc(note)}</p>
    </header>'''
    slides.append(f'''<div class="stage"><section class="slide{' dark' if dark else ''}\
{' twin' if twin else ''} {cls}">
  <div class="topline">
    <div class="tl-l"><span class="tab">{len(index):02d}</span>\
<span class="tl-part">{esc(foot)}</span></div>
    <div class="tl-r"><span class="mark{' on-dark' if dark else ''}" role="img"
      aria-label="IAQ: your total facility solutions provider"></span></div>
  </div>{head}
  {body if raw else f'<div class="canvas{" fill" if fill else ""}">{body}</div>'}
  <footer class="botline">
    <div class="bl-l"><span class="folio">{n:02d}</span></div>
    <div class="bl-c"></div>
    <div class="bl-r">{esc(name)}</div>
  </footer>
</section></div>''')


def layout(key, name, purpose, filled, empty):
    """One layout, shown filled and then empty."""
    index.append((len(index) + 1, name, purpose))
    opts = dict(name=name)
    if EMPTY_ONLY:
        page(empty['body'], twin=True, title=empty['title'], note=empty['note'],
             foot=empty['foot'], dark=empty.get('dark', False),
             cls=empty.get('cls', ''), bare=empty.get('bare', False),
             fill=empty.get('fill', False), raw=empty.get('raw', False), **opts)
        return
    page(filled['body'], twin=False, title=filled['title'], note=filled['note'],
         foot=filled['foot'], dark=filled.get('dark', False),
         cls=filled.get('cls', ''), bare=filled.get('bare', False),
         fill=filled.get('fill', False), raw=filled.get('raw', False), **opts)
    page(empty['body'], twin=True, title=empty['title'], note=empty['note'],
         foot=empty['foot'], dark=empty.get('dark', False),
         cls=empty.get('cls', ''), bare=empty.get('bare', False),
         fill=empty.get('fill', False), raw=empty.get('raw', False), **opts)


# ------------------------------------------------------------------ marks
ICON = {
 'person': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="4"/><path d="M4.5 20.5c0-4 3.4-6.5 7.5-6.5s7.5 2.5 7.5 6.5"/></svg>',
 'gear': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3.1"/><path d="M12 2.6v2.8M12 18.6v2.8M21.4 12h-2.8M5.4 12H2.6M18.6 5.4l-2 2M7.4 16.6l-2 2M18.6 18.6l-2-2M7.4 7.4l-2-2"/></svg>',
 'check': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M8 12.4l2.7 2.7L16 9.4"/></svg>',
 'bolt': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2.6L5.4 14h6l-1 7.4L18 10h-6z"/></svg>',
 'leaf': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M20.2 3.8c0 9.1-4.9 13.7-11.1 13.7H5.4C5.4 9.4 11 3.8 20.2 3.8z"/><path d="M3.8 21c1.5-4.6 4.1-7.5 7.7-9.6"/></svg>',
 'shield': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2.8l7.6 2.9v6c0 4.3-3 8-7.6 9.5-4.6-1.5-7.6-5.2-7.6-9.5v-6z"/><path d="M8.7 11.9l2.4 2.4 4.2-4.6"/></svg>',
 'clock': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M12 6.6v5.7l3.6 2.1"/></svg>',
 'globe': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M3.2 12h17.6"/><path d="M12 3c2.6 2.7 3.9 5.7 3.9 9s-1.3 6.3-3.9 9c-2.6-2.7-3.9-5.7-3.9-9S9.4 5.7 12 3z"/></svg>',
}
G = '·'

# ============================================================ 01 title page
layout('title', 'Title', 'Open a deck or a chapter of one.',
  dict(title='', note='', foot=LEGAL, dark=True, bare=True, fill=True,
       body=f'''
      <div class="tp">
        <span class="tp-k">Capability statement {G} 2026</span>
        <h1 class="tp-h">Engineering the facilities advanced industry runs on.</h1>
        <p class="tp-n">Cleanroom critical delivery for semiconductor, data centre,
        EV battery, pharmaceutical and energy.</p>
        <span class="tp-m">Prepared for {G} Client name {G} October 2026</span>
      </div>'''),
  dict(title='', note='', foot=LEGAL, dark=True, bare=True, fill=True,
       body=f'''
      <div class="tp">
        <span class="tp-k">Kicker {G} two or three words</span>
        <h1 class="tp-h">The one line this deck is about, eight words or fewer.</h1>
        <p class="tp-n">A sentence under it saying who it is for and what it covers.</p>
        <span class="tp-m">Prepared for {G} client {G} date</span>
      </div>'''))

# ============================================================ 02 divider
layout('divider', 'Section divider', 'Open a new part of the deck.',
  dict(title='', note='', foot='Part 02 ' + G + ' Project References', dark=True,
       bare=True, raw=True, cls='divider',
       body='''
  <div class="div-grid">
    <div class="div-copy">
      <span class="div-kicker">Part 02 of 03</span>
      <div class="div-num">02</div>
      <h2 class="div-title">Project References</h2>
      <p class="div-note">Sections 02.1 to 02.47</p>
      <ul class="div-list"><li>235+ projects completed across three regions</li>
      <li>Over 1.5 million m&sup2; of cleanroom built</li></ul>
    </div>
    <div class="div-media"><img src="img/refs-crew.jpg" alt=""></div>
  </div>'''),
  dict(title='', note='', foot='Section name', dark=True,
       bare=True, raw=True, cls='divider',
       body='''
  <div class="div-grid">
    <div class="div-copy">
      <span class="div-kicker">Part 00 of 00</span>
      <div class="div-num">00</div>
      <h2 class="div-title">Section name</h2>
      <p class="div-note">What this part covers</p>
      <ul class="div-list"><li>A fact worth leading with</li>
      <li>A second fact, the same length</li></ul>
    </div>
    <div class="div-media"><img src="img/refs-crew.jpg" alt=""></div>
  </div>'''))

# ============================================================ 03 statement
layout('statement', 'Statement', 'One argument, said plainly, with a photograph.',
  dict(title='Why IAQ', note='The case in one line, and what stands behind it.',
       foot='Part 01 ' + G + ' The Company', fill=True,
       body='''
      <div class="split media">
        <div class="lede">
          <h3 class="statement">Thirty-one years of building the rooms that cannot fail.</h3>
          <p class="body">Cleanrooms, process utilities and tool hookup for the
          industries where contamination control, precision and compliance are
          absolute. Self-performed, under one contract.</p>
        </div>
        <div class="side-media"><img src="img/glance-cleanroom.jpg" alt=""></div>
      </div>'''),
  dict(title='Page title', note='One line under it saying what the page is for.',
       foot='Section name', fill=True,
       body='''
      <div class="split media">
        <div class="lede">
          <h3 class="statement">The statement, two lines at most, said plainly.</h3>
          <p class="body">Two or three sentences carrying the argument. Say what
          is true, what it is worth, and leave the rest to the next page.</p>
        </div>
        <div class="side-media"><img src="img/glance-cleanroom.jpg" alt=""></div>
      </div>'''))

# ============================================================ 04 highlights
def hl(k, fig, unit, note, on=False):
    u = f'<span class="hl-u">{unit}</span>' if unit else ''
    return (f'<div class="hl-c{" on" if on else ""}"><span class="hl-k">{k}</span>'
            f'<div class="hl-f">{fig}{u}</div><p class="hl-n">{note}</p></div>')

layout('highlights', 'Highlights', 'Three or four figures that carry the page.',
  dict(title='The year in four numbers', note='Where the work went in 2026.',
       foot='Part 01 ' + G + ' The Company', fill=True,
       body='<div class="hl">'
            + hl('Delivered', '235', '+', 'Projects completed since 1995', on=True)
            + hl('Built', '1.5', 'mil m&sup2;', 'Cleanroom built-up area')
            + hl('People', '530', '+', 'Engineers, supervisors and crew')
            + hl('Reach', '7', '', 'Offices across three continents')
            + '</div>'),
  dict(title='Page title', note='One line under it saying what the page is for.',
       foot='Section name', fill=True,
       body='<div class="hl">'
            + hl('Label', '00', '+', 'What the figure counts, one line', on=True)
            + hl('Label', '00', 'unit', 'What the figure counts, one line')
            + hl('Label', '00', '%', 'What the figure counts, one line')
            + hl('Label', '00', '', 'What the figure counts, one line')
            + '</div>'))

# ============================================================ 05 icon cards
def card(icon, name, note, num):
    return (f'<div class="chip"><span class="c-ico">{ICON[icon]}</span>'
            f'<div class="c-body"><span class="c-name">{name}</span>'
            f'<span class="c-note">{note}</span></div>'
            f'<span class="c-num">{num:02d}</span></div>')

layout('cards', 'Icon cards', 'A set of capabilities, services or principles.',
  dict(title='What we self-perform', note='Six packages under one contract.',
       foot='Part 01 ' + G + ' The Company', fill=True,
       body='<div class="scope2 solo"><div class="chips four sv cols3">'
            + card('gear', 'Engineering design', 'CSA and MEP, to specification', 1)
            + card('bolt', 'Electrical systems', 'Up to 33kV substations', 2)
            + card('shield', 'Cleanroom systems', 'ISO 3 to ISO 8', 3)
            + card('check', 'Commissioning', 'Testing and handover', 4)
            + card('clock', 'Maintenance', 'Operate, service, optimise', 5)
            + card('leaf', 'Energy management', 'Carbon and cost reduction', 6)
            + '</div></div>'),
  dict(title='Page title', note='One line under it saying what the page is for.',
       foot='Section name', fill=True,
       body='<div class="scope2 solo"><div class="chips four sv cols3">'
            + ''.join(card('gear', 'Item name', 'What it covers, four or five words', i)
                      for i in range(1, 7))
            + '</div></div>'))

# ============================================================ 06 comparison
def col(k, h, summary, items, on=False):
    return (f'<div class="cmp-col{" on" if on else ""}"><span class="cmp-k">{k}</span>'
            f'<h3 class="cmp-h">{h}</h3><p class="cmp-sum">{summary}</p>'
            '<ul class="cmp-l">' + ''.join(f'<li>{x}</li>' for x in items) + '</ul></div>')

layout('compare', 'Comparison', 'Two or three options read side by side.',
  dict(title='Three ways to contract the work',
       note='The same crews, scoped three ways.',
       foot='Part 01 ' + G + ' The Company', fill=True,
       body='<div class="cmp">'
            + col('Model 01', 'EPCM', 'Management of engineering, procurement and construction.',
                  ['Client holds the trade contracts', 'IAQ manages delivery',
                   'Fastest route to a fab ramp', 'Best where scope is still moving'])
            + col('Model 02', 'EPCC', 'Full turnkey from conception to operation.',
                  ['IAQ holds every contract', 'One programme, one accountability',
                   'Fixed scope, fixed completion', 'Best where the brief is settled'], on=True)
            + col('Model 03', 'EFM', 'Energy and facility management after handover.',
                  ['Planned and reactive maintenance', 'Energy and carbon reduction',
                   'Operates the asset for its life', 'Best where uptime decides value'])
            + '</div>'),
  dict(title='Page title', note='One line under it saying what the page is for.',
       foot='Section name', fill=True,
       body='<div class="cmp">'
            + col('Option 01', 'First option', 'One sentence saying what it is.',
                  ['A point of difference', 'A second point', 'A third point',
                   'When to choose it'])
            + col('Option 02', 'Second option', 'One sentence saying what it is.',
                  ['A point of difference', 'A second point', 'A third point',
                   'When to choose it'], on=True)
            + col('Option 03', 'Third option', 'One sentence saying what it is.',
                  ['A point of difference', 'A second point', 'A third point',
                   'When to choose it'])
            + '</div>'))

# ============================================================ 07 org chart, tree
def node(role, name, under='', on=False):
    u = f'<span class="node-u">{under}</span>' if under else ''
    return (f'<div class="node{" on" if on else ""}"><span class="node-r">{role}</span>'
            f'<span class="node-n">{name}</span>{u}</div>')

def tree(top, mids):
    # the bus bar runs between the first and last drop, not past them
    ticks = ''.join('<i></i>' for _ in mids)
    span = 100 - 100 / len(mids)
    return (f'<div class="org">{top}<div class="org-drop"></div>'
            f'<div class="org-span" style="width:{span:.2f}%"></div>'
            f'<div class="org-ticks">{ticks}</div>'
            f'<div class="org-row">{"".join(mids)}</div></div>')

layout('org-tree', 'Org chart ' + G + ' reporting tree',
       'Who reports to whom, three levels at most.',
  dict(title='How the company is run', note='Board, executive and the four lines.',
       foot='Part 01 ' + G + ' The Company', fill=True,
       body=tree(node('Chairman', 'Board of Directors', 'Governance and strategy', on=True),
                 [node('Managing Director', 'Group MD', 'Operations and delivery'),
                  node('Director', 'Engineering', 'Design and method'),
                  node('Director', 'Commercial', 'Cost, contracts and risk'),
                  node('Director', 'HSE and Quality', 'Standards and audit')])),
  dict(title='Page title', note='One line under it saying what the page is for.',
       foot='Section name', fill=True,
       body=tree(node('Role', 'Name or function', 'What they are accountable for', on=True),
                 [node('Role', 'Name or function', 'One line'),
                  node('Role', 'Name or function', 'One line'),
                  node('Role', 'Name or function', 'One line'),
                  node('Role', 'Name or function', 'One line')])))

# ============================================================ 08 org chart, band
def person(role, name, under):
    return (f'<div class="node"><span class="band-ava">{ICON["person"]}</span>'
            f'<span class="node-r">{role}</span><span class="node-n">{name}</span>'
            f'<span class="node-u">{under}</span></div>')

layout('org-band', 'Org chart ' + G + ' flat team band',
       'A team of peers, no hierarchy implied.',
  dict(title='The project team', note='Who the client deals with, day to day.',
       foot='Part 01 ' + G + ' The Company', fill=True,
       body='<div class="band">'
            + person('Project Director', 'Name here', 'Single point of contact')
            + person('Construction Manager', 'Name here', 'Site and programme')
            + person('Lead Engineer', 'Name here', 'Design and method')
            + person('QA / QC Manager', 'Name here', 'Inspection and records')
            + person('HSE Manager', 'Name here', 'Safety on every shift')
            + '</div>'),
  dict(title='Page title', note='One line under it saying what the page is for.',
       foot='Section name', fill=True,
       body='<div class="band">'
            + ''.join(person('Role', 'Name', 'What they own') for _ in range(5))
            + '</div>'))

# ============================================================ 09 org chart, group
def gcard(role, name, items):
    return (f'<div class="grp-c"><span class="node-r">{role}</span>'
            f'<span class="node-n">{name}</span>'
            '<ul class="grp-l">' + ''.join(f'<li>{x}</li>' for x in items) + '</ul></div>')

def group(top, cards):
    ticks = ''.join('<i></i>' for _ in cards)
    span = 100 - 100 / len(cards)
    return (f'<div class="grp">{top}<div class="org-drop"></div>'
            f'<div class="org-span" style="width:{span:.2f}%"></div>'
            f'<div class="org-ticks">{ticks}</div>'
            f'<div class="grp-row">{"".join(cards)}</div></div>')

layout('org-group', 'Org chart ' + G + ' group structure',
       'A holding company and the businesses under it.',
  dict(title='The group', note='One holding company, four operating businesses.',
       foot='Part 01 ' + G + ' The Company', fill=True,
       body=group(node('Holding', LEGAL, 'Incorporated 1995 ' + G + ' 200001031412', on=True),
                  [gcard('Company 01', 'IAQ Solutions', ['Cleanroom systems', 'CSA and MEP', 'Malaysia and Singapore']),
                   gcard('Company 02', 'IAQ Utility Solutions', ['Process utilities', 'Tool hookup', 'EPCM packages']),
                   gcard('Company 03', 'IAQ Energy Facility Management', ['District cooling', 'Chiller plants', 'Operate and maintain']),
                   gcard('Company 04', 'IAQ Europe', ['Gigafactories', 'Wafer fabs', 'Sweden, Germany, France'])])),
  dict(title='Page title', note='One line under it saying what the page is for.',
       foot='Section name', fill=True,
       body=group(node('Holding', 'Parent company name', 'Incorporated 0000', on=True),
                  [gcard('Company 00', 'Business name',
                         ['What it does', 'What it does', 'Where it works'])
                   for _ in range(4)])))

# ============================================================ 10 process
def step(icon, k, name, note):
    return (f'<div class="cy-step"><span class="cy-mark">{ICON[icon]}<b>{k:02d}</b></span>'
            f'<div class="cy-name">{name}</div><div class="cy-note">{note}</div></div>')

def cycle(label, lead, steps):
    return (f'<section class="cycle"><div class="cy-head"><span class="label">{label}</span>'
            f'<p class="cy-lead">{lead}</p></div>'
            f'<div class="cy-track">{"".join(steps)}</div></section>')

layout('process', 'Process', 'Stages that run in order, start to finish.',
  dict(title='How a package is delivered', note='Five stages, one accountability.',
       foot='Part 01 ' + G + ' The Company', fill=True, cls='tpl-proc',
       body=cycle('The delivery cycle',
                  'Every package runs the same five stages, whoever holds the contract.',
                  [step('gear', 1, 'Engineering', 'Design and consultation'),
                   step('check', 2, 'Procurement', 'Sourcing and supply chain'),
                   step('bolt', 3, 'Construction', 'Self-performed packages'),
                   step('shield', 4, 'Testing', 'Commissioning and handover'),
                   step('clock', 5, 'Maintenance', 'Operate, service, optimise')])),
  dict(title='Page title', note='One line under it saying what the page is for.',
       foot='Section name', fill=True, cls='tpl-proc',
       body=cycle('Process name',
                  'One sentence saying what the process is and where it starts.',
                  [step('gear', i, 'Stage name', 'Three or four words')
                   for i in range(1, 6)])))

# ============================================================ 11 timeline
def tml(years, ups, dns):
    up = ''.join(f'<div class="tml-i"><span class="tml-h">{h}</span>'
                 f'<p class="tml-n">{n}</p></div>' if h else '<div class="tml-i"></div>'
                 for h, n in ups)
    dn = ''.join(f'<div class="tml-i"><span class="tml-h">{h}</span>'
                 f'<p class="tml-n">{n}</p></div>' if h else '<div class="tml-i"></div>'
                 for h, n in dns)
    dots = ''.join(f'<div class="tml-node"><span class="tml-dot">{y}</span></div>'
                   for y in years)
    return (f'<div class="tml"><div class="tml-row up">{up}</div>'
            f'<div class="tml-rail">{dots}</div>'
            f'<div class="tml-row dn">{dn}</div></div>')

layout('timeline', 'Timeline', 'Dates in order, with what happened at each.',
  dict(title='Thirty-one years', note='The turns that made the company.',
       foot='Part 01 ' + G + ' The Company', fill=True,
       body=tml(['1995', '2008', '2016', '2021', '2026'],
                [('Founded', 'Incorporated as a cleanroom specialist'), ('', ''),
                 ('Largest DCC plant', 'KLCC district cooling, a national first'), ('', ''),
                 ('Three continents', 'India, the United States and Ireland open')],
                [('', ''), ('Class 10 cleanroom', 'Western Digital PJ, a first in the region'),
                 ('', ''), ('Four fab expansions', 'SilTerra, Soitec, Infineon, Microsoft'),
                 ('', '')])),
  dict(title='Page title', note='One line under it saying what the page is for.',
       foot='Section name', fill=True,
       body=tml(['0000', '0000', '0000', '0000', '0000'],
                [('Event', 'One line on what happened'), ('', ''),
                 ('Event', 'One line on what happened'), ('', ''),
                 ('Event', 'One line on what happened')],
                [('', ''), ('Event', 'One line on what happened'),
                 ('', ''), ('Event', 'One line on what happened'), ('', '')])))

# ============================================================ 12 infographic
def fxi(icon, k, name, note):
    return (f'<article class="fx"><span class="fx-vis"><span class="fx-ico">{ICON[icon]}</span></span>'
            f'<div class="fx-body"><span class="fx-k">{k:02d}</span>'
            f'<h3 class="fx-name">{name}</h3><p class="fx-note">{note}</p></div></article>')

def info(left, right, img, cap, lead):
    return (f'<div class="fabx"><div class="fx-col">{"".join(left)}</div>'
            f'<div class="fx-core"><span class="fx-cap">{cap}</span>'
            f'<img src="{img}" alt=""><p class="fx-lead">{lead}</p></div>'
            f'<div class="fx-col">{"".join(right)}</div></div>')

layout('infographic', 'Infographic', 'One visual in the middle, the parts around it.',
  dict(title='What goes into the building',
       note='Six systems, one model, one contract.',
       foot='Part 01 ' + G + ' The Company', fill=True,
       body=info([fxi('gear', 1, 'Structure', 'Greenfield and brownfield CSA'),
                  fxi('bolt', 2, 'Electrical', 'Up to 33kV substations'),
                  fxi('shield', 3, 'Cleanroom', 'ISO 3 to ISO 8')],
                 [fxi('check', 4, 'Process utilities', 'Water, chemical, gas, exhaust'),
                  fxi('clock', 5, 'Monitoring', 'FMCS, BMS, PA'),
                  fxi('globe', 6, 'Tool hookup', 'Progressive install')],
                 'img/fab-section.png', 'One model, six systems',
                 'Every system on this page is installed in the same building, '
                 'by IAQ&rsquo;s own crews, under one programme.')),
  dict(title='Page title', note='One line under it saying what the page is for.',
       foot='Section name', fill=True,
       body=info([fxi('gear', i, 'Part name', 'What it covers, four words')
                  for i in (1, 2, 3)],
                 [fxi('gear', i, 'Part name', 'What it covers, four words')
                  for i in (4, 5, 6)],
                 'img/fab-section.png', 'Caption over the visual',
                 'One sentence under the visual saying what the whole thing adds up to.')))

# ============================================================ 13 image + specs
def specs(img, k, h, tags, rows):
    t = ''.join(f'<li>{x}</li>' for x in tags)
    r = ''.join(f'<div class="spec-r"><span class="spec-l">{a}</span>'
                f'<span class="spec-v">{b}</span></div>' for a, b in rows)
    return (f'<div class="pspec"><div class="spec-media"><img src="{img}" alt=""></div>'
            f'<div class="spec-tx"><span class="spec-k">{k}</span><h3 class="spec-h">{h}</h3>'
            f'<ul class="spec-tags">{t}</ul><div class="spec-rows">{r}</div></div></div>')

layout('imagespecs', 'Image and specs', 'One project or product, pictured and specified.',
  dict(title='Project reference', note='One project, what it was and what it took.',
       foot='Part 02 ' + G + ' Project References', fill=True,
       body=specs('img/infineon-kulim.jpg', 'Kulim, Kedah ' + G + ' greenfield wafer fab',
                  'Infineon Kulim Wafer Fab 3',
                  ['EPCC &amp; design build', 'Cleanroom systems', 'ACMV &amp; mechanical'],
                  [('Description', 'General contractor for WP06, KLM3 Expansion, 36,000 m&sup2; cleanroom area'),
                   ('Scope', 'PCC for cleanroom and mechanical works'),
                   ('Cleanroom', 'ISO 4 to 7 ' + G + ' Class 10 to 100 to 10K'),
                   ('Completed', '2024')])),
  dict(title='Page title', note='One line under it saying what the page is for.',
       foot='Section name', fill=True,
       body=specs('img/infineon-kulim.jpg', 'Location ' + G + ' what kind of facility',
                  'Project or product name',
                  ['Service line', 'Service line', 'Service line'],
                  [('Description', 'One sentence on what the job was'),
                   ('Scope', 'What was in the contract'),
                   ('Cleanroom', 'Class or grade, if it applies'),
                   ('Completed', 'Year')])))

# ============================================================ 14 programme
def gantt(scale, rows):
    head = ''.join(f'<span>{s}</span>' for s in scale)
    body = ''
    for name, sub, start, span, tag, soft in rows:
        left = start / len(scale) * 100
        width = span / len(scale) * 100
        b = (f'<span class="gt-bar{" soft" if soft else ""}" '
             f'style="left:{left:.2f}%;width:{width:.2f}%">'
             f'{f"<b>{tag}</b>" if tag else ""}</span>')
        body += (f'<div class="gt-row"><div><div class="gt-name">{name}</div>'
                 f'<div class="gt-sub">{sub}</div></div>'
                 f'<div class="gt-track">{b}</div></div>')
    return (f'<div class="gantt"><div class="gt-head"><div></div>'
            f'<div class="gt-scale">{head}</div></div>'
            f'<div class="gt-body">{body}</div></div>')

Q = ['Q1 26', 'Q2 26', 'Q3 26', 'Q4 26', 'Q1 27', 'Q2 27']
layout('gantt', 'Programme', 'Work packages against a calendar.',
  dict(title='Indicative programme', note='Six quarters, from award to handover.',
       foot='Part 01 ' + G + ' The Company', fill=True,
       body=gantt(Q, [
           ('Engineering design', 'CSA and MEP to IFC', 0, 2, '8 weeks', False),
           ('Long lead procurement', 'AHUs, switchgear, chillers', 0.6, 2.4, '', True),
           ('Civil and structural', 'Foundations to envelope', 1.4, 2.2, '', False),
           ('Cleanroom build', 'Walls, ceilings, flooring', 2.6, 1.8, '', False),
           ('Process utilities', 'Water, gas, chemical, exhaust', 3.2, 1.8, '', False),
           ('Testing and handover', 'Classification and C&amp;Q', 4.6, 1.4, 'Handover', False)])),
  dict(title='Page title', note='One line under it saying what the page is for.',
       foot='Section name', fill=True,
       body=gantt(['Period', 'Period', 'Period', 'Period', 'Period', 'Period'], [
           ('Work package', 'What is in it', 0, 2, 'Milestone', False),
           ('Work package', 'What is in it', 1, 2, '', True),
           ('Work package', 'What is in it', 2, 2, '', False),
           ('Work package', 'What is in it', 3, 2, '', False),
           ('Work package', 'What is in it', 3.8, 1.6, '', False),
           ('Work package', 'What is in it', 4.4, 1.6, 'Milestone', False)])))

# ============================================================ 15 table
def table(cols, rows):
    head = ''.join(f'<th>{c}</th>' for c in cols)
    body = ''
    for r in rows:
        body += '<tr>' + ''.join(
            f'<td class="hot">{c[1:]}</td>' if str(c).startswith('*') else f'<td>{c}</td>'
            for c in r) + '</tr>'
    return (f'<table class="tbl"><thead><tr>{head}</tr></thead>'
            f'<tbody>{body}</tbody></table>')

layout('table', 'Table', 'Rows and columns, where the detail has to be exact.',
  dict(title='Cleanroom classes we build to',
       note='What each grade means and where it is used.',
       foot='Part 01 ' + G + ' The Company', fill=True,
       body=table(['Class', 'ISO grade', 'Particles per m&sup3;', 'Typical use', 'Delivered'],
                  [['Class 1', 'ISO 3', '&le; 1,000 at 0.1 &micro;m', 'Advanced-node lithography', '*Yes'],
                   ['Class 10', 'ISO 4', '&le; 10,000 at 0.1 &micro;m', 'Wafer fabrication', '*Yes'],
                   ['Class 100', 'ISO 5', '&le; 3,520 at 0.5 &micro;m', 'Photomask, test and assembly', '*Yes'],
                   ['Class 1K', 'ISO 6', '&le; 35,200 at 0.5 &micro;m', 'Medical device, parenteral', '*Yes'],
                   ['Class 10K', 'ISO 7', '&le; 352,000 at 0.5 &micro;m', 'Pharmaceutical, GMP', '*Yes'],
                   ['Class 100K', 'ISO 8', '&le; 3.5 m at 0.5 &micro;m', 'Packaging and support areas', '*Yes']])),
  dict(title='Page title', note='One line under it saying what the page is for.',
       foot='Section name', fill=True,
       body=table(['Column', 'Column', 'Column', 'Column', 'Column'],
                  [['Row label', 'Value', 'Value', 'Value', '*Called out']
                   for _ in range(6)])))

# ============================================================ 16 full bleed
def bleed(img, line, note):
    return (f'<div class="bl-img"><img src="{img}" alt=""></div>'
            f'<div class="bl-plate"></div>'
            f'<div class="bl-tx"><p class="bl-line">{line}</p>'
            f'<p class="bl-note">{note}</p></div>')

layout('bleed', 'Full-bleed image', 'Let one photograph carry the page.',
  dict(title='', note='', foot=LEGAL, dark=True, bare=True, raw=True,
       cls='bleed',
       body=bleed('img/cover-site.jpg',
                  'The rooms that cannot fail.',
                  'Thirty-one years of cleanroom critical delivery, on three continents.')),
  dict(title='', note='', foot=LEGAL, dark=True, bare=True, raw=True,
       cls='bleed',
       body=bleed('img/cover-site.jpg',
                  'One line over the photograph.',
                  'A sentence under it, if the line needs support. Otherwise leave it out.')))

# ============================================================ 17 closing
def closing(line, note, rows):
    r = ''.join(f'<div class="spec-r"><span class="spec-l">{a}</span>'
                f'<span class="spec-v">{b}</span></div>' for a, b in rows)
    return (f'<div class="tp"><h1 class="tp-h">{line}</h1>'
            f'<p class="tp-n">{note}</p>'
            f'<div class="spec-rows" style="max-width:calc(900 * var(--u))">{r}</div></div>')

layout('closing', 'Closing', 'End the deck: the ask, and how to reach you.',
  dict(title='', note='', foot=LEGAL, dark=True, bare=True, fill=True,
       body=closing('Let us look at your facility.',
                    'Tell us the class, the programme and the constraint. '
                    'We will tell you what it takes.',
                    [('Enquiries', 'business@iaqtechnology.com.my'),
                     ('Telephone', '+603 5131 9999'),
                     ('Head office', '12, Jalan Sungai Jeluh 32/192, Shah Alam, Selangor'),
                     ('Online', 'iaqtechnology.com.my')])),
  dict(title='', note='', foot=LEGAL, dark=True, bare=True, fill=True,
       body=closing('The closing line, six words or fewer.',
                    'A sentence saying what you want to happen next.',
                    [('Label', 'The detail'), ('Label', 'The detail'),
                     ('Label', 'The detail'), ('Label', 'The detail')])))

# ============================================================ contents, front
rows = ''.join(
    f'<div class="ix-r"><span class="ix-n">{n:02d}</span>'
    f'<span class="ix-h">{esc(name)}</span>'
    f'<span class="ix-p">{esc(purpose)}</span></div>'
    for n, name, purpose in index)
slides.insert(0, f'''<div class="stage"><section class="slide">
  <div class="topline">
    <div class="tl-l"><span class="tl-part">{esc(LEGAL)}</span></div>
    <div class="tl-r"><span class="mark" role="img"
      aria-label="IAQ: your total facility solutions provider"></span></div>
  </div>
  <header class="shead">
    <h2 class="s-title">Master template</h2>
    <p class="s-note">{'Seventeen layouts to build a new slide from. Copy the page you need and type into it.' if EMPTY_ONLY else 'Seventeen layouts to build a new slide from. Each one is shown filled, then empty with a line in every box.'}</p>
  </header>
  <div class="canvas fill">
    <div class="ix">{rows}</div>
  </div>
  <footer class="botline">
    <div class="bl-l"><span class="folio">00</span></div>
    <div class="bl-c"></div>
    <div class="bl-r">Contents</div>
  </footer>
</section></div>''')

CSS = (io.open(DECK + 'deck.css', encoding='utf-8').read() + '\n'
       + io.open(DECK + 'src/tpl.css', encoding='utf-8').read())
JS = io.open(DECK + 'deck.js', encoding='utf-8').read()

doc = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>IAQ Master Template</title>
<meta name="description" content="Layouts a client starts a new IAQ slide from.">
<link rel="stylesheet" href="fonts.css">
<style>
{CSS}
</style>
</head>
<body>
<div class="deck">
{chr(10).join(slides)}
</div>
<script>
{JS}
</script>
</body>
</html>'''

io.open(OUT, 'w', encoding='utf-8').write(doc)
# the layout names travel with the pages, so the PowerPoint template cannot
# drift from what the examples show
import json
if not EMPTY_ONLY:
    json.dump([{'n': n, 'name': name, 'purpose': purpose} for n, name, purpose in index],
              io.open(DECK + 'template/layouts.json', 'w', encoding='utf-8'), indent=1)
print('wrote %s - %d slides, %d layouts, %d KB'
      % (OUT, len(slides), len(index), len(doc.encode()) // 1024))
