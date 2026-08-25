# ================================================= 13 LOGO OVERVIEW
sheet("3.1 Logo Overview", "03 Visual", "03 &middot; Visual Identity", "3.1 &middot; Logo Overview",
  "Logo Overview",
  "One mark, used whole. The badge carries the name inside it, so there is no separate symbol and "
  "no separate wordmark to place.",
  f'''<div style="display:flex;flex-direction:column;height:100%;gap:26px">
  <div class="rv" style="--d:200ms;flex:1;min-height:0;background:var(--paper);
    border:1px solid var(--ink14);display:flex;align-items:center;justify-content:center;position:relative">
    <span class="mono s dim" style="position:absolute;left:26px;top:22px">Primary mark</span>
    {mark(470, tm=True)}
  </div>
  <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:26px;flex:none;height:250px">
    {"".join(f'''<div class="rv" style="--d:{270+i*60}ms;background:{bg};
      {'border:1px solid var(--ink14);' if bg in (PAPER, STEAM) else ''}display:flex;
      align-items:center;justify-content:center;position:relative">
      <span class="mono s" style="position:absolute;left:22px;top:18px;color:{lab}">{name}</span>
      {art}</div>'''
      for i, (name, bg, lab, art) in enumerate([
        ("On Steam", STEAM, "rgba(25,20,16,.62)", mark(210)),
        ("On Ink", INK, "rgba(255,255,255,.6)", mark(210)),
        ("On Vit&rsquo;s Red", RED, "rgba(255,255,255,.78)", mark(210, "#fff", RED))]))}
  </div>
  <div class="rv" style="--d:460ms;flex:none;display:flex;gap:20px;border-top:1px solid var(--ink14);
    padding-top:16px">
    <span class="mono s acc" style="flex:none">Master files</span>
    <span style="font-size:17px;line-height:26px;color:var(--ink72)">The badge here is redrawn from
    the file Vit&rsquo;s supplied. Treat it as a working stand in: request the vector master from
    Brand Governance before any artwork goes to separation. Never trace the mark from a pack shot
    and never rebuild it by setting the name inside a drawn shape.</span></div></div>''', ground="steam")

# ================================================== 14 LOGO CONCEPT
_anat = [("A","The dome","A broad, even arch. It reads as the near side of a full bowl and it gives "
    "the mark its stability on shelf."),
  ("B","The scalloped base","Two dropped points with a rise between them. This is the line that "
    "makes the badge recognisable at a glance, and the part most often lost when the mark is redrawn."),
  ("C","The keyline","A rule inset inside the edge, holding the badge off whatever sits behind it. "
    "It closes up below 46px and is dropped there, never thinned."),
  ("D","The wordmark","Reversed out, optically centred, sitting slightly above the middle so the "
    "scalloped base does not crowd it.")]
sheet("3.2 Logo Concept", "03 Visual", "03 &middot; Visual Identity", "3.2 &middot; Logo Concept",
  "Logo Concept",
  "Four parts, and one open question about what the mark is meant to say.",
  f'''<div style="display:grid;grid-template-columns:1.1fr 1fr;gap:64px;height:100%">
  <div class="rv" style="--d:200ms;background:var(--paper);border:1px solid var(--ink14);
    position:relative;display:flex;align-items:center;justify-content:center">
    <div style="position:relative;width:520px;height:341px">
      <div style="position:absolute;inset:0">{mark(520)}</div>
      {"".join(f'''<span style="position:absolute;{ln};background:{INK};opacity:.45"></span>
        <span style="position:absolute;{pos};width:30px;height:30px;border-radius:50%;
        background:{bgc};color:{fgc};display:flex;align-items:center;justify-content:center;
        font-family:var(--fm);font-size:12px;font-weight:700">{lab}</span>'''
        for lab, pos, ln, bgc, fgc in [
          ("A","left:245px;top:-46px","left:259px;top:-16px;width:1px;height:24px",INK,"#fff"),
          ("B","left:245px;bottom:-46px","left:259px;bottom:-16px;width:1px;height:26px",INK,"#fff"),
          ("C","left:-52px;top:150px","left:-22px;top:165px;width:40px;height:1px",INK,"#fff"),
          ("D","right:-52px;top:150px","right:-22px;top:165px;width:40px;height:1px",INK,"#fff")])}
    </div>
  </div>
  <div style="display:flex;flex-direction:column">
    <div style="display:flex;flex-direction:column">
    {"".join(f'''<div class="rv" style="--d:{260+i*55}ms;display:grid;grid-template-columns:40px 1fr;
      gap:18px;padding:16px 0;border-top:1px solid var(--ink14);align-items:start">
      <span style="width:30px;height:30px;border-radius:50%;background:{RED};color:#fff;
        display:flex;align-items:center;justify-content:center;font-family:var(--fm);
        font-size:12.5px;font-weight:700">{lab}</span>
      <div><div style="font-family:var(--fd);font-weight:800;font-size:20px;letter-spacing:-.01em">{t}</div>
      <div style="font-size:16.5px;line-height:25px;color:var(--ink72);margin-top:6px">{b}</div></div></div>'''
      for i, (lab, t, b) in enumerate(_anat))}</div>
    <div style="flex:1"></div>
    <div class="rv" style="--d:520ms;background:{INK};color:#fff;padding:24px 30px;margin-top:24px">
      <span class="mono s" style="color:{GOLD}">Open question</span>
      <div style="font-size:16.5px;line-height:26px;color:var(--w72);margin-top:10px">
        Vit&rsquo;s own storytelling rests on the phoenix, from <b style="color:#fff">Wei Yi</b>,
        the only one. The mark does not depict it. Either the story reaches the mark or the mark
        stays a pure name badge and the phoenix stays a story. That is the client&rsquo;s call, and
        it is the one decision in this book that changes Section 03 wholesale.</div>
    </div>
  </div></div>''')

# ================================================== 15 LOGO FORMATS
def _fmt(label, note, inner, ground_bg, d):
    return f'''<div class="rv" style="--d:{d}ms;display:flex;flex-direction:column;gap:11px">
      <div style="flex:1;min-height:0;background:{ground_bg};border:1px solid var(--ink14);
        display:flex;align-items:center;justify-content:center;padding:18px">{inner}</div>
      <div><div class="mono s" style="color:{REDD}">{label}</div>
      <div style="font-size:16px;line-height:23px;color:var(--ink72);margin-top:5px">{note}</div></div></div>'''
sheet("3.3 Logo Formats", "03 Visual", "03 &middot; Visual Identity", "3.3 &middot; Logo Formats",
  "Logo Formats",
  "Six approved constructions. Pick by the ground you are on and the size you have, never by taste.",
  f'''<div class="grid" style="grid-template-columns:repeat(3,1fr);grid-template-rows:1fr 1fr;
    height:100%;gap:26px">
  {_fmt("01 &nbsp;Primary, with TM","The default on any first or standalone appearance.",
        mark(200, tm=True), PAPER, 200)}
  {_fmt("02 &nbsp;Primary, no TM","Where the mark repeats on one surface, and at small sizes.",
        mark(200), PAPER, 250)}
  {_fmt("03 &nbsp;Knockout","White badge, red wordmark. On the red, and over photography.",
        mark(200, "#fff", RED), RED, 300)}
  {_fmt("04 &nbsp;One colour, ink","Single plate print, stamps, engraving, faxable documents.",
        mark(200, INK), PAPER, 350)}
  {_fmt("05 &nbsp;One colour, white","Embossing, debossing and dark photographic grounds.",
        mark(200, "#fff", INK), INK, 400)}
  {_fmt("06 &nbsp;Silhouette","Watermarks and pattern only. This is not a logo and never stands in for one.",
        badge(200, "rgba(236,31,40,.22)"), PAPER, 450)}
  </div>''', ground="steam")

# ============================================ 16 CLEARSPACE AND SIZE
_sizes = [("Print, full mark","22 mm wide"),("Print, minimum","14 mm wide, keyline dropped"),
  ("Digital, full mark","110 px wide"),("Digital, minimum","46 px wide, keyline dropped"),
  ("Embossing and debossing","18 mm wide"),("App icon and favicon","Not this mark. See below.")]
sheet("3.4 Clearspace and Size", "03 Visual", "03 &middot; Visual Identity", "3.4 &middot; Clearspace and Size",
  "Clearspace and Size",
  "Clearspace is measured in <b>X</b>, one quarter of the badge height. Nothing enters the field: "
  "not type, not a rule, not the edge of the sheet.",
  f'''<div style="display:grid;grid-template-columns:1.3fr 1fr;gap:60px;height:100%">
  <div class="rv" style="--d:200ms;background:var(--paper);border:1px solid var(--ink14);
    display:flex;align-items:center;justify-content:center;position:relative">
    <span class="mono s dim" style="position:absolute;left:24px;top:20px">Clearspace &nbsp;=&nbsp; 1X on every side</span>
    <div style="position:relative;padding:76px">
      <div style="position:absolute;inset:0;border:1px dashed rgba(236,31,40,.6);
        background:rgba(236,31,40,.05)"></div>
      <div style="position:relative">{mark(300)}</div>
      {"".join(f'''<span style="position:absolute;{ln};background:{RED}"></span>
        <span style="position:absolute;{lb};font-family:var(--fm);font-size:13px;font-weight:700;
        color:{REDD}">X</span>'''
        for ln, lb in [
          ("left:50%;top:0;width:1px;height:76px","left:calc(50% + 10px);top:26px"),
          ("left:50%;bottom:0;width:1px;height:76px","left:calc(50% + 10px);bottom:26px"),
          ("left:0;top:50%;height:1px;width:76px","left:28px;top:calc(50% - 26px)"),
          ("right:0;top:50%;height:1px;width:76px","right:28px;top:calc(50% - 26px)")])}
    </div>
  </div>
  <div style="display:flex;flex-direction:column">
    <div class="rv" style="--d:260ms"><span class="mono s acc">Minimum sizes</span></div>
    <table class="spec rv" style="--d:310ms;margin-top:12px">
      {"".join(f"<tr><td>{k}</td><td>{v}</td></tr>" for k, v in _sizes)}</table>
    <div class="rv" style="--d:380ms;margin-top:26px;padding-top:20px;border-top:1px solid var(--ink14)">
      <span class="mono s acc">Where the keyline gives out</span>
      <div style="display:flex;align-items:flex-end;gap:30px;margin-top:18px">
      {"".join(f'''<div style="display:flex;flex-direction:column;align-items:center;gap:10px">
        {mark(w)}<span class="mono s dim" style="font-size:10.5px">{w} px</span></div>'''
        for w in [110, 74, 46, 30])}
      </div>
      <div style="font-size:16px;line-height:24px;color:var(--ink72);margin-top:16px">
        At 110px the keyline is clean. At 46px it has closed to a hairline and is dropped. At 30px
        the wordmark fills in and the mark stops working at all.</div>
    </div>
    <div style="flex:1"></div>
    <div class="rv" style="--d:470ms;background:{INK};color:#fff;padding:20px 24px;display:flex;gap:18px">
      <span class="mono s" style="color:{GOLD};flex:none">Open item</span>
      <span style="font-size:17px;line-height:26px;color:var(--w72)">A wide badge cannot carry a
      square app icon or a 32px favicon. A dedicated icon has to be drawn, and it is on the list on
      page 5.1. Until it exists, use the red tile shown on 4.4.</span>
    </div>
  </div></div>''')

# =================================================== 17 BACKGROUNDS
_bgs = [("Steam", STEAM, "primary", "Default light ground for documents and decks.", True),
  ("Paper", PAPER, "primary", "Packaging faces, stationery, anywhere print white is available.", True),
  ("Soy Ink", INK, "primary", "Covers, dividers and dark grounds. The red holds against the black.", True),
  ("Vit&rsquo;s Red", RED, "knockout", "Knockout only. The red badge on red is not a mark.", True),
  ("Golden Wheat", GOLD, "primary", "Conditional. Flavour bands only, and never with the ink variant.", False),
  ("Broth", BROTH, "knockout", "Not approved. The badge loses its edge against the mid tone.", False)]
sheet("3.5 Backgrounds", "03 Visual", "03 &middot; Visual Identity", "3.5 &middot; Backgrounds",
  "Backgrounds",
  "Four approved grounds, one conditional, one refused. When in doubt put the mark on Steam.",
  f'''<div class="grid" style="grid-template-columns:repeat(3,1fr);grid-template-rows:1fr 1fr;
    height:100%;gap:26px">
  {"".join(f'''<div class="rv" style="--d:{200+i*55}ms;display:flex;flex-direction:column;gap:11px">
    <div style="flex:1;min-height:0;background:{bg};border:1px solid var(--ink14);display:flex;
      align-items:center;justify-content:center;position:relative">
      {mark(180) if variant == "primary" else mark(180, "#fff", RED)}
      <span style="position:absolute;right:14px;top:14px;width:24px;height:24px;border-radius:50%;
        background:{RED if not ok else INK};color:#fff;display:flex;align-items:center;
        justify-content:center;font-size:{'14' if not ok else '13'}px;font-weight:700">{'&times;' if not ok else '&#10003;'}</span>
    </div>
    <div><div class="mono s" style="color:{REDD if ok else BROTH}">{name}</div>
    <div style="font-size:16px;line-height:23px;color:var(--ink72);margin-top:5px">{note}</div></div></div>'''
    for i, (name, bg, variant, note, ok) in enumerate(_bgs))}</div>''', ground="steam")

# =================================================== 18 LOGO DON'TS
_donts = [
  ("Do not recolour the badge", 'style=""', mark(150, "#2E7D32")),
  ("Do not stretch or distort", 'style="transform:scaleX(1.5)"', mark(150)),
  ("Do not rotate", 'style="transform:rotate(-13deg)"', mark(150)),
  ("Do not add effects", 'style="filter:drop-shadow(0 8px 12px rgba(236,31,40,.9))"', mark(150)),
  ("Do not reset the wordmark", 'style=""',
   f'<span style="position:relative;display:inline-flex">{badge(150)}'
   f'<span style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;'
   f'font-family:Georgia,serif;font-style:italic;font-size:44px;color:#fff;padding-bottom:6px">Vit&rsquo;s</span></span>'),
  ("Do not thin or drop the keyline above 46px", 'style=""', mark(150, RED, "#fff", False, False)),
  ("Do not use the silhouette as the logo", 'style=""', badge(150)),
  ("Do not place on a busy ground", 'style=""',
   f'<span style="display:inline-flex;padding:14px;background:repeating-linear-gradient('
   f'45deg,{GOLD},{GOLD} 11px,{RED} 11px,{RED} 22px)">{mark(130)}</span>')]
sheet("3.6 Logo Don&rsquo;ts", "03 Visual", "03 &middot; Visual Identity", "3.6 &middot; Logo Don&rsquo;ts",
  "Logo Don&rsquo;ts",
  "Eight things that break the mark. If your artwork appears on this page, change it before it ships.",
  f'''<div class="grid" style="grid-template-columns:repeat(4,1fr);grid-template-rows:1fr 1fr;
    height:100%;gap:22px">
  {"".join(f'''<div class="rv" style="--d:{200+i*40}ms;display:flex;flex-direction:column;gap:12px">
    <div style="flex:1;min-height:0;position:relative;display:flex;align-items:center;
      justify-content:center;border:1px solid rgba(236,31,40,.32);background:var(--paper);overflow:hidden">
      <span style="position:absolute;right:10px;top:10px;width:21px;height:21px;border-radius:50%;
        background:{RED};color:#fff;display:flex;align-items:center;justify-content:center;
        font-size:13.5px;font-weight:700">&times;</span>
      <div {tf}>{art}</div></div>
    <div style="display:flex;gap:9px;align-items:baseline">
      <span class="mono s" style="color:{RED};flex:none">{i+1:02d}</span>
      <span style="font-size:16px;line-height:23px;color:var(--ink72)">{label}</span></div></div>'''
    for i, (label, tf, art) in enumerate(_donts))}</div>''', ground="steam")
