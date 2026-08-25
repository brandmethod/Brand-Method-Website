# ================================================= 19 COLOUR PALETTE
_pal = [("Vit&rsquo;s Red", RED, "#fff", "216, 35, 42", "0, 84, 81, 15",
   "The signature. Packaging field, the mark, and one call to action per surface."),
  ("Golden Wheat", GOLD, INK, "240, 168, 30", "0, 30, 88, 6",
   "Wheat, heat and the crest. Flavour banding and the single warm accent."),
  ("Soy Ink", INK, "#fff", "25, 20, 16", "0, 20, 36, 90",
   "Headlines, body copy and dark grounds. A warm black, never a neutral one."),
  ("Steam", STEAM, INK, "250, 244, 233", "0, 2, 7, 2",
   "The default light ground. An off white carrying a trace of the gold."),
  ("Broth", BROTH, "#fff", "138, 115, 96", "0, 17, 30, 46",
   "Quiet panels and photographic grounds. Large type only &mdash; see 3.8.")]
sheet("3.7 Colour Palette", "03 Visual", "03 &middot; Visual Identity", "3.7 &middot; Colour Palette",
  "Colour Palette",
  "Five values carry the system. Red is the field, gold is the accent, and gold is rationed.",
  f'''<div style="display:flex;flex-direction:column;height:100%">
  <div class="grid" style="grid-template-columns:repeat(5,1fr);flex:1;min-height:0;gap:22px">
  {"".join(f'''<div class="rv" style="--d:{200+i*55}ms;display:flex;flex-direction:column;
    border:1px solid var(--ink14)">
    <div style="flex:1;min-height:0;background:{hexv};position:relative">
      <div style="position:absolute;left:20px;bottom:16px;font-family:var(--fd);font-weight:800;
        font-size:20px;letter-spacing:-.014em;color:{fg}">{name}</div></div>
    <div style="padding:15px 18px 17px;background:var(--paper)">
      <div class="mono" style="font-weight:700;font-size:14px;letter-spacing:.04em">{hexv.upper()}</div>
      <div class="mono s dim" style="margin-top:8px;line-height:1.85;letter-spacing:.05em">
        RGB {rgb}<br>CMYK {cmyk}<br>PANTONE To be matched</div>
      <div style="font-size:14.5px;line-height:22px;color:var(--ink72);margin-top:10px">{note}</div>
    </div></div>''' for i, (name, hexv, fg, rgb, cmyk, note) in enumerate(_pal))}
  </div>
  <div class="rv" style="--d:480ms;flex:none;margin-top:22px;padding-top:16px;
    border-top:1px solid var(--ink14);display:flex;gap:20px">
    <span class="mono s acc" style="flex:none">Spot colour</span>
    <span style="font-size:15.5px;line-height:24px;color:var(--ink72)">CMYK breakdowns above are
    process conversions. Pantone references are to be matched against a printed pack under D50 before
    this edition is signed off &mdash; food packaging red shifts badly across substrates, and the
    flexo result on film will not match the litho result on carton without a spot.</span></div>
  </div>''', ground="steam")

# ================================================== 20 COLOUR IN USE
_prop = [(42,"Steam and Paper",STEAM,INK),(26,"Vit&rsquo;s Red",RED,"#fff"),
         (20,"Soy Ink",INK,"#fff"),(8,"Golden Wheat",GOLD,INK),(4,"Broth",BROTH,"#fff")]
_pairs = [("Ink on Paper", PAPER, INK, "18.3 : 1", "AAA", True),
  ("Ink on Steam", STEAM, INK, "16.7 : 1", "AAA", True),
  ("Steam on Ink", INK, STEAM, "16.7 : 1", "AAA", True),
  ("Ink on Gold", GOLD, INK, "9.0 : 1", "AAA", True),
  ("Paper on Red", RED, PAPER, "5.0 : 1", "AA", True),
  ("Red on Steam", STEAM, RED, "4.6 : 1", "AA", True),
  ("Broth on Steam", STEAM, BROTH, "4.1 : 1", "24px+ only", False),
  ("Gold on Steam", STEAM, GOLD, "1.8 : 1", "Refused", False)]
sheet("3.8 Colour in Use", "03 Visual", "03 &middot; Visual Identity", "3.8 &middot; Colour in Use",
  "Colour in Use",
  "Proportion first, then the pairings that are cleared to carry type.",
  f'''<div style="display:flex;flex-direction:column;height:100%">
  <div class="rv" style="--d:200ms;display:flex;height:106px;border:1px solid var(--ink14)">
    {"".join(f'<div style="flex:{p};background:{bg}"></div>' for p, _, bg, _fg in _prop)}</div>
  <div class="rv" style="--d:240ms;display:flex;margin-top:12px">
    {"".join(f'''<div style="flex:{p}"><div style="font-family:var(--fd);font-weight:800;
      font-size:17px">{p}%</div><div class="mono s dim" style="margin-top:4px">{n}</div></div>'''
      for p, n, _bg, _fg in _prop)}</div>
  <div class="rv" style="--d:300ms;margin-top:30px"><span class="mono s acc">Cleared pairings
    &nbsp;&mdash;&nbsp; WCAG 2.1 contrast, measured</span></div>
  <div class="rv" style="--d:340ms;margin-top:14px;flex:1;min-height:0">
    <div style="display:grid;grid-template-columns:repeat(4,1fr);grid-template-rows:1fr 1fr;
      gap:16px;height:100%">
    {"".join(f'''<div style="display:flex;flex-direction:column;gap:9px;min-height:0">
      <div style="flex:1;min-height:0;background:{bg};{'border:1px solid var(--ink14);' if bg in (PAPER, STEAM) else ''}
        display:flex;align-items:center;justify-content:center">
        <span style="font-family:var(--fd);font-weight:800;font-stretch:112%;font-size:26px;
          letter-spacing:-.014em;color:{fg}">VIT&rsquo;S</span></div>
      <div style="display:flex;justify-content:space-between;gap:8px;align-items:baseline">
        <span class="mono s dim" style="font-size:10.5px">{label}</span>
        <span class="mono s" style="color:{REDD if ok else BROTH};font-size:10.5px;white-space:nowrap">{ratio}
          &nbsp;{grade}</span></div></div>'''
      for label, bg, fg, ratio, grade, ok in _pairs)}</div></div>
  <div class="rv" style="--d:520ms;flex:none;margin-top:20px;padding-top:15px;
    border-top:1px solid var(--ink14);display:flex;gap:20px">
    <span class="mono s acc" style="flex:none">Gold is not a text colour</span>
    <span style="font-size:15.5px;line-height:24px;color:var(--ink72)">Golden Wheat reaches 1.8 : 1 on
    Steam. It carries shapes, rules and bands &mdash; never body copy on a light ground. On Ink it is
    cleared at 9.0 : 1 and may set type freely.</span></div></div>''')

# ==================================================== 21 TYPOGRAPHY
_faces = [("Archivo","Display","800 Expanded, 700",
   "Headlines, the wordmark, pack front-of-face and any type over 30px. Set expanded at 112&ndash;118% "
   "width; it is what gives the brand its shelf voice.", "var(--fd)", "800", "112%"),
  ("Figtree","Text","400, 500, 600",
   "Body copy, decks, pack back-of-face, long-form. Warm humanist proportions that stay legible at "
   "6pt on film.", "var(--ft)", "500", "100%"),
  ("JetBrains Mono","Data","500, 700",
   "Labels, batch codes, weights, nutritional panels, specifications. Anything that must line up in "
   "a column.", "var(--fm)", "500", "100%"),
  ("Arial","Fallback","Regular, Bold",
   "Email, Office documents and any system without the brand faces licensed. Never used in artwork.",
   "var(--fa)", "700", "100%")]
sheet("3.9 Typography", "03 Visual", "03 &middot; Visual Identity", "3.9 &middot; Typography",
  "Typography",
  "Three brand faces and one fallback. Archivo carries the personality; Figtree carries the reading.",
  f'''<div style="display:flex;flex-direction:column;height:100%;gap:0">
  {"".join(f'''<div class="rv" style="--d:{200+i*70}ms;display:grid;grid-template-columns:250px 1fr 330px;
    gap:44px;padding:26px 0;border-top:1px solid var(--ink14);align-items:center;flex:1;min-height:0">
    <div><div style="font-family:var(--fd);font-weight:800;font-size:26px;letter-spacing:-.015em">{fam}</div>
      <div class="mono s dim" style="margin-top:7px">{role} &nbsp;&middot;&nbsp; {wts}</div></div>
    <div style="font-family:{ff};font-weight:{w};font-stretch:{st};font-size:52px;line-height:1;
      letter-spacing:-.02em;white-space:nowrap;overflow:hidden">Aa Bb &nbsp;Mi Segera &nbsp;1975</div>
    <div style="font-size:15px;line-height:23px;color:var(--ink72)">{note}</div></div>'''
    for i, (fam, role, wts, note, ff, w, st) in enumerate(_faces))}
  <div class="rv" style="--d:520ms;flex:none;margin-top:14px;padding-top:15px;
    border-top:1px solid var(--ink14);display:flex;gap:20px">
    <span class="mono s acc" style="flex:none">Licensing</span>
    <span style="font-size:15.5px;line-height:24px;color:var(--ink72)">Archivo, Figtree and JetBrains
    Mono are all offered under the SIL Open Font Licence, so packaging artwork, web embedding and
    partner co-branding carry no per-seat cost. Confirm the licence text ships with any file handed
    to a co-packer.</span></div></div>''', ground="steam")

# ==================================================== 22 TYPE SCALE
_scale = [("Display","Archivo 800 Exp","132 / 124","-3.2%","Cover and back cover only",56),
  ("Page title","Archivo 800 Exp","60 / 61","-1.8%","One per page, top left",34),
  ("Statement","Archivo 800","40 / 50","-1.8%","Positioning, vision, pull quotes",26),
  ("Section head","Archivo 800","24 / 30","-1.4%","Card titles and sub heads",20),
  ("Lead","Figtree 400","21 / 34","0","Page description, right of title",18),
  ("Body","Figtree 400","16.5 / 26","0","Running copy inside cards and columns",16),
  ("Caption","Figtree 400","14.5 / 21","0","Under specimens and diagrams",14),
  ("Label","JetBrains Mono 500","10.5 / 18","+17%","Topbars, footers, all uppercase",11)]
sheet("3.10 Type Scale", "03 Visual", "03 &middot; Visual Identity", "3.10 &middot; Type Scale",
  "Type Scale",
  "Eight steps. Everything in this book is set from them &mdash; nothing is sized by eye.",
  f'''<div style="display:grid;grid-template-columns:1.02fr 1fr;gap:64px;height:100%">
  <div class="rv" style="--d:200ms">
    <table class="tb"><thead><tr><th>Step</th><th>Face</th><th>Size / Leading</th>
      <th>Tracking</th></tr></thead><tbody>
      {"".join(f'''<tr><td class="k">{n}</td><td class="mono" style="font-size:12.5px;
        letter-spacing:.03em;text-transform:none">{f}</td>
        <td class="mono" style="font-size:12.5px;letter-spacing:.03em">{s}</td>
        <td class="mono" style="font-size:12.5px;letter-spacing:.03em">{t}</td></tr>'''
        for n, f, s, t, _u, _px in _scale)}</tbody></table></div>
  <div class="rv" style="--d:280ms;display:flex;flex-direction:column;justify-content:space-between">
    {"".join(f'''<div style="display:flex;align-items:baseline;gap:20px;padding:9px 0;
      border-bottom:1px solid var(--ink08)">
      <span class="mono s dim" style="width:96px;flex:none">{n}</span>
      <span style="font-family:{'var(--fd)' if 'Archivo' in f else ('var(--fm)' if 'Mono' in f else 'var(--ft)')};
        font-weight:{800 if 'Archivo' in f else (500 if 'Mono' in f else 400)};
        font-stretch:{'112%' if 'Exp' in f else '100%'};
        font-size:{px}px;line-height:1.15;letter-spacing:{'-.02em' if 'Archivo' in f else ('.17em' if 'Mono' in f else '0')};
        {'text-transform:uppercase;' if 'Mono' in f else ''}
        white-space:nowrap;overflow:hidden;flex:1">{u}</span></div>'''
      for n, f, _s, _t, u, px in _scale)}</div></div>''')

# =============================================== 23 LANGUAGE VARIANTS
_langs = [("English","Primary","Halal instant noodles, made in Malaysia since 1975.",
   "var(--ft)","ltr","Front of pack, export, corporate and digital."),
  ("Bahasa Malaysia","Primary","Mi segera halal, dibuat di Malaysia sejak 1975.",
   "var(--ft)","ltr","Statutory on Malaysian retail packs, equal weight with English."),
  ("&#20013;&#25991; Chinese","Secondary","&#28165;&#30495;&#26041;&#20415;&#38754; &middot; &#21807;&#19968;",
   "var(--fsc)","ltr","Malaysian retail, Singapore, Greater China export."),
  ("&#1575;&#1604;&#1593;&#1585;&#1576;&#1610;&#1577; Arabic","Secondary",
   "&#1606;&#1608;&#1583;&#1604;&#1586; &#1587;&#1585;&#1610;&#1593;&#1577; &#1575;&#1604;&#1578;&#1581;&#1590;&#1610;&#1585; &middot; &#1581;&#1604;&#1575;&#1604;",
   "var(--far)","rtl","Gulf and Middle East export markets.")]
sheet("3.11 Language Variants", "03 Visual", "03 &middot; Visual Identity", "3.11 &middot; Language Variants",
  "Language Variants",
  "Vit&rsquo;s sells into a multiracial home market and thirty export markets. The mark never "
  "translates; the copy around it always does.",
  f'''<div style="display:flex;flex-direction:column;height:100%;gap:0">
  {"".join(f'''<div class="rv" style="--d:{200+i*65}ms;display:grid;grid-template-columns:300px 1fr 300px;
    gap:44px;padding:24px 0;border-top:1px solid var(--ink14);align-items:center;flex:1;min-height:0">
    <div><div style="font-family:var(--fd);font-weight:800;font-size:23px;letter-spacing:-.014em">{name}</div>
      <div class="mono s dim" style="margin-top:7px">{role}</div></div>
    <div dir="{d}" style="font-family:{ff};font-size:34px;line-height:1.45;color:var(--ink);
      {'text-align:right;' if d == 'rtl' else ''}">{txt}</div>
    <div style="font-size:15px;line-height:23px;color:var(--ink72)">{use}</div></div>'''
    for i, (name, role, txt, ff, d, use) in enumerate(_langs))}
  <div class="rv" style="--d:500ms;flex:none;margin-top:16px;padding-top:15px;
    border-top:1px solid var(--ink14);display:grid;grid-template-columns:1fr 1fr;gap:44px">
    <div style="display:flex;gap:18px"><span class="mono s acc" style="flex:none">Typefaces</span>
      <span style="font-size:15px;line-height:23px;color:var(--ink72)">Chinese sets in Noto Sans SC,
      Arabic in Noto Naskh Arabic. Both are matched to Figtree at optical size, not at nominal
      point size.</span></div>
    <div style="display:flex;gap:18px"><span class="mono s acc" style="flex:none">Regulatory</span>
      <span style="font-size:15px;line-height:23px;color:var(--ink72)">Label language, halal marking
      and ingredient declaration follow the destination market&rsquo;s own rules. This page governs
      typography only, never legal compliance.</span></div></div></div>''', ground="steam")
