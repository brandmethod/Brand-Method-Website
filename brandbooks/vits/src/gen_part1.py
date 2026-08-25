# -*- coding: utf-8 -*-
"""Vit's Noodles Brand Book - page generator.
Structure mirrors the Agensia Brand Book page system: 1920x1080 sheets,
mono topbar, hairline, title/lead head, body, footer. Palette, typography
and marks are Vit's own."""

RED="#D8232A"; GOLD="#F0A81E"; INK="#191410"; STEAM="#FAF4E9"; BROTH="#8A7360"; PAPER="#FFFFFF"
REDD="#B01B22"   # deeper red for small type on light grounds

def mark(w=60, red=RED, gold=GOLD, bowl=INK, crest=None):
    """The Vit's phoenix rising from the bowl. Square 120x120 artboard."""
    crest = crest or gold
    return (f'<svg viewBox="0 0 120 120" width="{w}" height="{w}" xmlns="http://www.w3.org/2000/svg" '
      f'aria-hidden="true" style="display:block;flex:none">'
      f'<path d="M15 78 L105 78 C105 99 87 112 60 112 C33 112 15 99 15 78 Z" fill="{bowl}"/>'
      f'<path d="M63 49 C80 46 96 34 108 12 C89 19 73 29 62 42 Z" fill="{red}"/>'
      f'<path d="M57 49 C40 46 24 34 12 12 C31 19 47 29 58 42 Z" fill="{red}"/>'
      f'<path d="M63 63 C76 61 87 52 94 38 C81 43 70 50 62 58 Z" fill="{gold}"/>'
      f'<path d="M57 63 C44 61 33 52 26 38 C39 43 50 50 58 58 Z" fill="{gold}"/>'
      f'<path d="M60 84 C54 70 53 52 57 36 L63 36 C67 52 66 70 60 84 Z" fill="{red}"/>'
      f'<circle cx="60" cy="29" r="7" fill="{red}"/>'
      f'<path d="M62 24 C68 15 77 10 87 9" fill="none" stroke="{crest}" stroke-width="5.4" '
      f'stroke-linecap="round"/></svg>')

def symbol(w=60, red=RED, gold=GOLD, crest=None):
    """Phoenix alone, no bowl - for avatars, favicons and embossing."""
    crest = crest or gold
    return (f'<svg viewBox="0 0 120 120" width="{w}" height="{w}" xmlns="http://www.w3.org/2000/svg" '
      f'aria-hidden="true" style="display:block;flex:none">'
      f'<path d="M63 56 C80 53 96 41 108 19 C89 26 73 36 62 49 Z" fill="{red}"/>'
      f'<path d="M57 56 C40 53 24 41 12 19 C31 26 47 36 58 49 Z" fill="{red}"/>'
      f'<path d="M63 70 C76 68 87 59 94 45 C81 50 70 57 62 65 Z" fill="{gold}"/>'
      f'<path d="M57 70 C44 68 33 59 26 45 C39 50 50 57 58 65 Z" fill="{gold}"/>'
      f'<path d="M60 104 C53 86 52 60 57 40 L63 40 C68 60 67 86 60 104 Z" fill="{red}"/>'
      f'<circle cx="60" cy="33" r="7.2" fill="{red}"/>'
      f'<path d="M62 28 C68 18 78 12 89 11" fill="none" stroke="{crest}" stroke-width="5.6" '
      f'stroke-linecap="round"/></svg>')

def wordmark(size=40, color=INK):
    return (f'<span style="font-family:var(--fd);font-weight:800;font-stretch:118%;font-size:{size}px;'
            f'letter-spacing:.005em;line-height:1;color:{color};white-space:nowrap">VIT&rsquo;S</span>')

def lockup(m=60, t=40, color=INK, red=RED, gold=GOLD, bowl=INK, gap=None):
    gap = gap if gap is not None else round(m*0.30)
    return (f'<span style="display:inline-flex;align-items:center;gap:{gap}px">'
            f'{mark(m, red, gold, bowl)}{wordmark(t, color)}</span>')

def rv(d, extra=""):
    return f'class="rv" style="--d:{d}ms;{extra}"'
