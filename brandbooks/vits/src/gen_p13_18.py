# ================================================= 13 LOGO OVERVIEW
sheet("3.1 Logo Overview", "03 Visual", "03 &middot; Visual Identity", "3.1 &middot; Logo Overview",
  "Logo Overview",
  "One primary lockup. Two supporting forms. Everything else in this section governs how these three "
  "are used.",
  f'''<div style="display:flex;flex-direction:column;height:100%;gap:26px">
  <div class="rv" style="--d:200ms;flex:1;min-height:0;background:var(--paper);
    border:1px solid var(--ink14);display:flex;align-items:center;justify-content:center;position:relative">
    <span class="mono s dim" style="position:absolute;left:26px;top:22px">Primary lockup</span>
    {lockup(150, 104)}
  </div>
  <div style="display:grid;grid-template-columns:1fr 1fr 1.25fr;gap:26px;flex:none;height:268px">
    <div class="rv" style="--d:270ms;background:var(--paper);border:1px solid var(--ink14);
      display:flex;flex-direction:column;align-items:center;justify-content:center;gap:22px;position:relative">
      <span class="mono s dim" style="position:absolute;left:22px;top:18px">Symbol</span>
      {symbol(104)}
      <span style="font-size:15px;line-height:22px;color:var(--ink72);text-align:center;max-width:270px">
        The phoenix alone. Avatars, favicons, embossing and any space too tight for the wordmark.</span>
    </div>
    <div class="rv" style="--d:330ms;background:var(--paper);border:1px solid var(--ink14);
      display:flex;flex-direction:column;align-items:center;justify-content:center;gap:22px;position:relative">
      <span class="mono s dim" style="position:absolute;left:22px;top:18px">Wordmark</span>
      {wordmark(58)}
      <span style="font-size:15px;line-height:22px;color:var(--ink72);text-align:center;max-width:270px">
        Set in Archivo Expanded 800. Used where the symbol already appears elsewhere on the surface.</span>
    </div>
    <div class="rv" style="--d:390ms;background:{INK};display:flex;align-items:center;
      justify-content:center;position:relative">
      <span class="mono s" style="position:absolute;left:22px;top:18px;color:rgba(255,255,255,.54)">Reversed</span>
      {lockup(92, 64, "#fff", RED, GOLD, "#fff")}
    </div>
  </div>
  <div class="rv" style="--d:450ms;flex:none;display:flex;gap:20px;border-top:1px solid var(--ink14);
    padding-top:16px">
    <span class="mono s acc" style="flex:none">Master files</span>
    <span style="font-size:15.5px;line-height:24px;color:var(--ink72)">Vector masters are held by Brand
    Governance. Never redraw the mark, never trace it from a pack shot, and never recreate the wordmark
    by typing it in a different weight.</span></div></div>''', ground="steam")

# ================================================== 14 LOGO CONCEPT
_anat = [("A","The phoenix","Wei Yi &mdash; the only one. Power, renewal and longevity, and a "
    "business that has had to rebuild more than once in fifty years."),
  ("B","Wings as strands","The primaries read as noodle strands lifting. The category is in the "
    "mark, not just the name."),
  ("C","The gold crest","The single warm accent. It is the only stroke allowed to break the "
    "silhouette upward."),
  ("D","The bowl","An everyday bowl, not a trophy. It anchors the phoenix and sets the "
    "clearspace unit.")]
sheet("3.2 Logo Concept", "03 Visual", "03 &middot; Visual Identity", "3.2 &middot; Logo Concept",
  "Logo Concept",
  "A phoenix rising as steam from a bowl. Two halves of the same idea &mdash; where Vit&rsquo;s comes "
  "from, and what it makes.",
  f'''<div style="display:grid;grid-template-columns:1.15fr 1fr;gap:70px;height:100%">
  <div class="rv" style="--d:200ms;background:var(--paper);border:1px solid var(--ink14);
    position:relative;display:flex;align-items:center;justify-content:center">
    <div style="position:relative;width:430px;height:430px">
      <div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center">
        {mark(430)}</div>
      {"".join(f'''<span style="position:absolute;{line};background:{INK};opacity:.42"></span>
        <span style="position:absolute;{pos};width:29px;height:29px;border-radius:50%;
        background:{bgc};color:{fgc};display:flex;align-items:center;justify-content:center;
        font-family:var(--fm);font-size:11.5px;font-weight:700">{lab}</span>'''
        for lab, pos, line, bgc, fgc in [
          ("A","left:200px;top:32px","left:214px;top:46px;width:1px;height:30px",INK,"#fff"),
          ("B","left:30px;top:94px","left:59px;top:108px;width:66px;height:1px",INK,"#fff"),
          ("C","left:362px;top:24px","left:322px;top:38px;width:42px;height:1px",INK,"#fff"),
          ("D","left:200px;top:320px","left:214px;top:0;width:0;height:0","#fff",INK)])}
    </div>
  </div>
  <div style="display:flex;flex-direction:column">
    <div class="rv" style="--d:260ms;font-family:var(--fd);font-weight:800;font-stretch:106%;
      font-size:34px;line-height:1.26;letter-spacing:-.018em;text-wrap:balance">
      The steam that rises off a bowl of Vit&rsquo;s takes the shape of the bird the name has always
      carried.</div>
    <div style="display:flex;flex-direction:column;margin-top:30px">
    {"".join(f'''<div class="rv" style="--d:{320+i*55}ms;display:grid;grid-template-columns:38px 1fr;
      gap:18px;padding:17px 0;border-top:1px solid var(--ink14);align-items:start">
      <span style="width:28px;height:28px;border-radius:50%;background:{RED};color:#fff;
        display:flex;align-items:center;justify-content:center;font-family:var(--fm);
        font-size:11.5px;font-weight:700">{lab}</span>
      <div><div style="font-family:var(--fd);font-weight:800;font-size:19px;letter-spacing:-.01em">{t}</div>
      <div style="font-size:15.5px;line-height:24px;color:var(--ink72);margin-top:6px">{b}</div></div></div>'''
      for i, (lab, t, b) in enumerate(_anat))}</div>
    <div style="flex:1"></div>
    <div class="rv" style="--d:560ms;display:flex;align-items:center;gap:30px;background:{INK};
      color:#fff;padding:26px 32px;margin-top:26px">
      <span style="font-family:var(--fsc);font-weight:700;font-size:62px;line-height:1;
        color:{GOLD};flex:none">&#21807;&#19968;</span>
      <span><span class="mono s" style="color:{GOLD}">Wei Yi</span>
        <span style="display:block;font-size:16.5px;line-height:26px;color:var(--w72);margin-top:9px">
        The only one. The mark exists to make a fifty-year-old Mandarin pun visible on a shelf
        in thirty countries.</span></span>
    </div>
  </div></div>''')

# ================================================== 15 LOGO FORMATS
def _fmt(label, note, inner, ground_bg, d, h=200):
    return f'''<div class="rv" style="--d:{d}ms;display:flex;flex-direction:column;gap:11px">
      <div style="flex:1;min-height:0;background:{ground_bg};border:1px solid var(--ink14);
        display:flex;align-items:center;justify-content:center;padding:18px">{inner}</div>
      <div><div class="mono s" style="color:{REDD}">{label}</div>
      <div style="font-size:14.5px;line-height:21px;color:var(--ink72);margin-top:5px">{note}</div></div></div>'''
sheet("3.3 Logo Formats", "03 Visual", "03 &middot; Visual Identity", "3.3 &middot; Logo Formats",
  "Logo Formats",
  "Six approved constructions. Pick by the space you have, not by preference.",
  f'''<div class="grid" style="grid-template-columns:repeat(3,1fr);grid-template-rows:1fr 1fr;
    height:100%;gap:26px">
  {_fmt("01 &nbsp;Horizontal &mdash; primary","The default. Use wherever width allows.",
        lockup(76, 52), PAPER, 200)}
  {_fmt("02 &nbsp;Stacked","Narrow columns, square formats, packaging end panels.",
        f'<span style="display:flex;flex-direction:column;align-items:center;gap:14px">{mark(78)}{wordmark(40)}</span>',
        PAPER, 250)}
  {_fmt("03 &nbsp;Symbol only","Avatars, app icons, favicons, embossing, cap seals.",
        symbol(84), PAPER, 300)}
  {_fmt("04 &nbsp;Reversed","On Ink or on a dark photographic ground.",
        lockup(72, 50, "#fff", RED, GOLD, "#fff"), INK, 350)}
  {_fmt("05 &nbsp;One colour, Ink","Faxable, single-plate print, stamps, engraving.",
        lockup(72, 50, INK, INK, INK, INK), PAPER, 400)}
  {_fmt("06 &nbsp;One colour, knockout","On Vit&rsquo;s Red and on flavour bands.",
        lockup(72, 50, "#fff", "#fff", "#fff", "#fff"), RED, 450)}
  </div>''', ground="steam")

# ============================================ 16 CLEARSPACE AND SIZE
_sizes = [("Print &mdash; horizontal lockup","28 mm wide"),("Print &mdash; symbol only","9 mm wide"),
  ("Digital &mdash; horizontal lockup","132 px wide"),("Digital &mdash; symbol only","28 px wide"),
  ("Embossing and debossing","14 mm wide, symbol only"),("Favicon","32 &times; 32 px, symbol only")]
sheet("3.4 Clearspace and Size", "03 Visual", "03 &middot; Visual Identity", "3.4 &middot; Clearspace and Size",
  "Clearspace and Size",
  "Clearspace is measured in <b>X</b>, the height of the bowl. Nothing enters the field &mdash; not "
  "type, not a rule, not the edge of the sheet.",
  f'''<div style="display:grid;grid-template-columns:1.35fr 1fr;gap:64px;height:100%">
  <div class="rv" style="--d:200ms;background:var(--paper);border:1px solid var(--ink14);
    display:flex;align-items:center;justify-content:center;position:relative">
    <span class="mono s dim" style="position:absolute;left:24px;top:20px">Clearspace &nbsp;=&nbsp; 1X on every side</span>
    <div style="position:relative;padding:88px">
      <div style="position:absolute;inset:0;border:1px dashed rgba(216,35,42,.6);
        background:rgba(216,35,42,.05)"></div>
      <div style="position:relative;background:var(--paper);padding:3px">{lockup(128, 88)}</div>
      {"".join(f'''<span style="position:absolute;{ln};background:{RED}"></span>
        <span style="position:absolute;{lb};font-family:var(--fm);font-size:13px;font-weight:700;
        color:{REDD}">X</span>'''
        for ln, lb in [
          ("left:50%;top:0;width:1px;height:88px","left:calc(50% + 10px);top:32px"),
          ("left:50%;bottom:0;width:1px;height:88px","left:calc(50% + 10px);bottom:32px"),
          ("left:0;top:50%;height:1px;width:88px","left:34px;top:calc(50% - 26px)"),
          ("right:0;top:50%;height:1px;width:88px","right:34px;top:calc(50% - 26px)")])}
    </div>
  </div>
  <div style="display:flex;flex-direction:column">
    <div class="rv" style="--d:260ms;display:flex;align-items:flex-end;gap:22px;
      padding-bottom:24px;border-bottom:1px solid var(--ink14)">
      <div style="position:relative">{mark(96)}
        <span style="position:absolute;left:-16px;top:64px;height:34px;width:1px;background:{RED}"></span>
      </div>
      <div><div class="mono s acc">The X unit</div>
      <div style="font-size:16.5px;line-height:26px;color:var(--ink72);margin-top:8px;max-width:340px">
        X is the height of the bowl, measured from rim to base. At every scale the clearspace
        recalculates from it.</div></div>
    </div>
    <div class="rv" style="--d:330ms;margin-top:26px"><span class="mono s acc">Minimum sizes</span></div>
    <table class="spec rv" style="--d:380ms;margin-top:12px">
      {"".join(f"<tr><td>{k}</td><td>{v}</td></tr>" for k, v in _sizes)}</table>
    <div style="flex:1"></div>
    <div class="rv" style="--d:430ms;padding:22px 0;border-top:1px solid var(--ink14)">
      <span class="mono s acc">At minimum size</span>
      <div style="display:flex;align-items:flex-end;gap:34px;margin-top:18px">
        <div style="display:flex;flex-direction:column;gap:9px">{lockup(26, 18)}
          <span class="mono s dim" style="font-size:9px">132 px lockup</span></div>
        <div style="display:flex;flex-direction:column;gap:9px;align-items:center">{symbol(28)}
          <span class="mono s dim" style="font-size:9px">28 px symbol</span></div>
        <div style="display:flex;flex-direction:column;gap:9px;align-items:center">{symbol(20)}
          <span class="mono s dim" style="font-size:9px">Favicon</span></div>
      </div>
    </div>
    <div class="rv" style="--d:470ms;background:{INK};color:#fff;padding:20px 24px;display:flex;gap:18px">
      <span class="mono s" style="color:{GOLD};flex:none">Below minimum</span>
      <span style="font-size:15.5px;line-height:24px;color:var(--w72)">Drop to the symbol before you
      drop below the minimum. A lockup too small to read the wordmark is worse than no wordmark.</span>
    </div>
  </div></div>''')

# =================================================== 17 BACKGROUNDS
_bgs = [("Steam", STEAM, INK, "Default light ground for documents and decks.", True),
  ("Paper", PAPER, INK, "Packaging faces, stationery, anywhere print white is available.", True),
  ("Ink", INK, "#fff", "Covers, dividers and dark photographic grounds.", True),
  ("Vit&rsquo;s Red", RED, "#fff", "Knockout lockup only. Never the full-colour mark.", True),
  ("Golden Wheat", GOLD, INK, "Ink lockup only, and only on flavour bands.", False),
  ("Broth", BROTH, "#fff", "Not approved. Contrast fails at lockup scale.", False)]
sheet("3.5 Backgrounds", "03 Visual", "03 &middot; Visual Identity", "3.5 &middot; Backgrounds",
  "Backgrounds",
  "Four approved grounds, one conditional, one refused. When in doubt put the mark on Steam.",
  f'''<div class="grid" style="grid-template-columns:repeat(3,1fr);grid-template-rows:1fr 1fr;
    height:100%;gap:26px">
  {"".join(f'''<div class="rv" style="--d:{200+i*55}ms;display:flex;flex-direction:column;gap:11px">
    <div style="flex:1;min-height:0;background:{bg};border:1px solid var(--ink14);display:flex;
      align-items:center;justify-content:center;position:relative">
      {lockup(66, 46, fg, RED if name in ("Steam","Paper") else fg,
              GOLD if name in ("Steam","Paper") else fg, INK if name in ("Steam","Paper") else fg)}
      <span style="position:absolute;right:14px;top:14px;width:22px;height:22px;border-radius:50%;
        background:{RED if not ok else INK};color:#fff;display:flex;align-items:center;
        justify-content:center;font-size:{'13' if not ok else '12'}px;font-weight:700">{'&times;' if not ok else '&#10003;'}</span>
    </div>
    <div><div class="mono s" style="color:{REDD if ok else BROTH}">{name}</div>
    <div style="font-size:14.5px;line-height:21px;color:var(--ink72);margin-top:5px">{note}</div></div></div>'''
    for i, (name, bg, fg, note, ok) in enumerate(_bgs))}</div>''', ground="steam")

# =================================================== 18 LOGO DON'TS
_donts = [("Do not recolour the mark", 'style=""', lockup(60, 42, "#2E7D32", "#2E7D32", "#7CB342", "#2E7D32")),
  ("Do not stretch or distort", 'style="transform:scaleX(1.55)"', lockup(60, 42)),
  ("Do not rotate", 'style="transform:rotate(-14deg)"', lockup(60, 42)),
  ("Do not add effects", 'style="filter:drop-shadow(0 8px 12px rgba(216,35,42,.85))"', lockup(60, 42)),
  ("Do not reset the wordmark",
   'style=""', f'<span style="display:inline-flex;align-items:center;gap:18px">{mark(60)}'
   f'<span style="font-family:Georgia,serif;font-style:italic;font-size:40px;color:{INK}">Vit&rsquo;s</span></span>'),
  ("Do not crowd the clearspace",
   'style=""', f'<span style="display:inline-flex;align-items:center;gap:4px">{lockup(60, 42)}'
   f'<span style="font-family:var(--fm);font-size:13px;color:{INK};border-left:1px solid {INK};'
   f'padding-left:5px;line-height:1.4">SINCE<br>1975</span></span>'),
  ("Do not change the lockup order",
   'style=""', f'<span style="display:inline-flex;align-items:center;gap:18px">{wordmark(42)}{mark(60)}</span>'),
  ("Do not place on a busy ground",
   'style=""', f'<span style="display:inline-flex;padding:14px;background:repeating-linear-gradient('
   f'45deg,{GOLD},{GOLD} 11px,{RED} 11px,{RED} 22px)">{lockup(60, 42)}</span>')]
sheet("3.6 Logo Don&rsquo;ts", "03 Visual", "03 &middot; Visual Identity", "3.6 &middot; Logo Don&rsquo;ts",
  "Logo Don&rsquo;ts",
  "Eight things that break the mark. If your artwork appears on this page, change it before it ships.",
  f'''<div class="grid" style="grid-template-columns:repeat(4,1fr);grid-template-rows:1fr 1fr;
    height:100%;gap:22px">
  {"".join(f'''<div class="rv" style="--d:{200+i*40}ms;display:flex;flex-direction:column;gap:12px">
    <div style="flex:1;min-height:0;position:relative;display:flex;align-items:center;
      justify-content:center;border:1px solid rgba(216,35,42,.32);background:var(--paper);overflow:hidden">
      <span style="position:absolute;right:10px;top:10px;width:19px;height:19px;border-radius:50%;
        background:{RED};color:#fff;display:flex;align-items:center;justify-content:center;
        font-size:12.5px;font-weight:700">&times;</span>
      <div {tf}>{art}</div></div>
    <div style="display:flex;gap:9px;align-items:baseline">
      <span class="mono s" style="color:{RED};flex:none">{i+1:02d}</span>
      <span style="font-size:15.5px;line-height:22px;color:var(--ink72)">{label}</span></div></div>'''
    for i, (label, tf, art) in enumerate(_donts))}</div>''', ground="steam")
