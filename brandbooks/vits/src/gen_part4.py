PAGES = []   # each: dict(name, group, html)

COPY = ("&copy; 2026 Vit Makanan (Kuala Lumpur) Sdn Bhd. All rights reserved. "
        "Confidential and proprietary. Internal and authorised partner use only.")

def footer(ref, n, ground=""):
    fm = mark(44, "#fff" if ground == "red" else RED, RED if ground == "red" else "#fff")
    return (f'<div class="ftr"><div class="fl">{fm}'
            f'<span>Brand Book &nbsp;V1.0 Draft</span></div>'
            f'<div class="fc">{COPY}</div>'
            f'<div class="fr"><span>{ref}</span><span class="fpg">{n:02d}</span></div></div>')

def sheet(name, group, sec, sub, title, lead, body, ground="", split=True, sm=False):
    """Standard content page: topbar, hairline, head, body, footer."""
    n = len(PAGES) + 1
    ref = sub.split(" &middot; ")[0] if " &middot; " in sub else sub
    cls = f"pg {ground}".strip()
    tcls = "t sm" if sm else "t"
    if split:
        head = (f'<div class="head split"><div><h1 class="{tcls} rv" style="--d:60ms">{title}</h1></div>'
                f'<div class="lead rv" style="--d:150ms">{lead}</div></div>')
    else:
        head = (f'<div class="head"><h1 class="{tcls} rv" style="--d:60ms">{title}</h1>'
                + (f'<div class="lead rv" style="--d:150ms">{lead}</div>' if lead else '') + '</div>')
    html = (f'<div class="slide" id="s{n}"><div class="{cls}"><div class="cv">'
            f'<div class="top"><span><b>{sec}</b></span><span>{sub}</span></div>'
            f'<div class="hair"></div>{head}'
            f'<div class="body">{body}</div></div>{footer(ref, n, ground)}</div></div>')
    PAGES.append(dict(name=name, group=group, html=html))

def raw(name, group, inner, ground=""):
    """Full bleed page: cover, dividers, back cover."""
    n = len(PAGES) + 1
    cls = f"pg {ground}".strip()
    PAGES.append(dict(name=name, group=group,
        html=f'<div class="slide" id="s{n}"><div class="{cls}">{inner}</div></div>'))

def divider(num, title, blurb, rows, name, group):
    n = len(PAGES) + 1
    idx = "".join(f'<div class="dv-row"><span class="n">{a}</span><span class="s">{b}</span></div>'
                  for a, b in rows)
    inner = (f'<div class="cv" style="padding-bottom:64px">'
             f'<div class="top"><span><b>{num} &middot; {title.upper()}</b></span>'
             f'<span>Section {num}</span></div><div class="hair"></div></div>'
             f'<div class="dv-mark">{badge(880, "#fff")}</div>'
             f'<div class="dv-wrap"><div class="dv-n rv" style="--d:60ms">{num}</div>'
             f'<div class="dv-t rv" style="--d:130ms">{title}</div>'
             f'<div class="dv-b rv" style="--d:200ms">{blurb}</div></div>'
             f'<div class="dv-idx rv" style="--d:280ms">{idx}</div>'
             f'{footer(num, n, "ink")}')
    PAGES.append(dict(name=name, group=group,
        html=f'<div class="slide" id="s{n}"><div class="pg ink">{inner}</div></div>'))
