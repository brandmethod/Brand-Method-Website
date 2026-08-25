# -*- coding: utf-8 -*-
"""Vit's Noodles Brand Book - page generator.
Structure mirrors the Agensia Brand Book page system: 1920x1080 sheets,
mono topbar, hairline, title/lead head, body, footer.

The mark is a redrawing of the asset the client supplied (Vits-Logo.png): a red
badge with a domed top and a scalloped base, an inner keyline, and the Vit's
wordmark reversed out of it. The badge silhouette is traced; the wordmark is set
in Archivo 900 as the closest available match and is NOT the real drawing."""

RED="#EC1F28"; GOLD="#F0A81E"; INK="#191410"; STEAM="#FAF4E9"; BROTH="#8A7360"; PAPER="#FFFFFF"
REDD="#C4141C"   # deeper red for small type on light grounds

# The badge silhouette, on a 1000 x 655 artboard.
BADGE_D = ("M10 300 C10 130 210 10 500 10 C790 10 990 130 990 300 "
           "C990 450 915 570 800 640 C690 600 600 578 500 578 "
           "C400 578 310 600 200 640 C85 570 10 450 10 300 Z")
_uid = [0]

def badge(w=200, fill=RED, opacity=None):
    """Badge silhouette only. Watermarks and decoration, never as a logo."""
    h = round(w * 0.655)
    op = f' opacity="{opacity}"' if opacity is not None else ""
    return (f'<svg viewBox="0 0 1000 655" width="{w}" height="{h}" xmlns="http://www.w3.org/2000/svg" '
            f'aria-hidden="true" style="display:block;flex:none"{op}>'
            f'<path d="{BADGE_D}" fill="{fill}"/></svg>')

def mark(w=200, fill=RED, fg="#fff", tm=False, keyline=None):
    """The Vit's mark. w is the badge width; height follows at 0.655 of it.

    Below 46px the keyline closes up and is dropped automatically, which is the
    same rule stated on page 3.4."""
    _uid[0] += 1; i = _uid[0]
    if keyline is None: keyline = w >= 46
    vb   = "0 0 1075 690" if tm else "0 0 1000 655"
    ratio = 0.642 if tm else 0.655
    h    = round(w * ratio)
    shift = ' transform="translate(0,45)"' if tm else ''
    kl = (f'<g transform="translate(500,327) scale(.947) translate(-500,-327)">'
          f'<use href="#vb{i}" fill="none" stroke="{fg}" stroke-width="11"/></g>') if keyline else ''
    tmk = (f'<text x="1068" y="74" text-anchor="end" fill="{fill}" font-family="Archivo" '
           f'style="font-weight:600;font-size:70px">TM</text>') if tm else ''
    return (f'<svg viewBox="{vb}" width="{w}" height="{h}" xmlns="http://www.w3.org/2000/svg" '
            f'style="display:block;flex:none" role="img" aria-label="Vit&rsquo;s">'
            f'<g{shift}><path id="vb{i}" d="{BADGE_D}" fill="{fill}"/>{kl}'
            f'<text x="502" y="472" text-anchor="middle" fill="{fg}" font-family="Archivo" '
            f'style="font-weight:900;font-size:350px;font-stretch:102%;letter-spacing:-5px"'
            f'>Vit&#8217;s</text></g>{tmk}</svg>')

def wordmark(size=40, color=INK):
    """The wordmark lifted out of the badge. Only where the badge already
    appears elsewhere on the surface."""
    return (f'<span style="font-family:var(--fd);font-weight:900;font-stretch:102%;'
            f'font-size:{size}px;letter-spacing:-.022em;line-height:1;color:{color};'
            f'white-space:nowrap">Vit&rsquo;s</span>')

def lockup(w=200, fill=RED, fg="#fff", tm=False):
    """Alias kept so page code reads the way the book talks about it."""
    return mark(w, fill, fg, tm)

def rv(d, extra=""):
    return f'class="rv" style="--d:{d}ms;{extra}"'
