# ============================================================ 01 COVER
raw("Cover", "Front", ground="steam", inner=f'''
<div style="position:absolute;right:0;top:0;bottom:0;width:612px;background:{RED};z-index:1;
  display:flex;align-items:center;justify-content:center;overflow:hidden">
  <div style="opacity:.22;transform:translateX(30px)">{badge(700, STEAM)}</div>
</div>
<div class="cv" style="padding:64px 120px 96px;width:1308px">
  <div class="rv mono s acc" style="--d:60ms;letter-spacing:.18em">Client level &middot; Brand identity</div>
  <div class="rv" style="--d:110ms;margin-top:26px">{mark(300, tm=True)}</div>
  <h1 class="rv" style="--d:170ms;font-family:var(--fd);font-weight:800;font-stretch:118%;
    font-size:132px;line-height:.94;letter-spacing:-.032em;margin:44px 0 0">Brand Book</h1>
  <div class="rv" style="--d:230ms;font-size:23px;line-height:36px;color:var(--ink72);
    max-width:640px;margin-top:26px;text-wrap:balance">
    The controlled reference for the Vit&rsquo;s identity: who we are, how we speak,
    and how the mark, palette and typography are applied.</div>
  <div style="flex:1"></div>
  <div class="rv" style="--d:300ms;display:flex;gap:0;border-top:1px solid var(--ink14);padding-top:22px">
    {"".join(f"""<div style="flex:1"><div class="mono s dim">{k}</div>
      <div style="font-family:var(--fd);font-weight:800;font-size:18.5px;margin-top:7px">{v}</div></div>"""
      for k, v in [("Brand owner","Vit Makanan (KL) Sdn Bhd"),("Prepared by","Brand Method"),
                   ("Edition","V1.0 &nbsp;Wireframe draft"),("Issued","August 2026")])}
  </div>
</div>
<div style="position:absolute;left:120px;bottom:40px;z-index:4;font-family:var(--fm);font-size:12px;
  letter-spacing:.16em;text-transform:uppercase;color:var(--ink54)">{COPY}</div>''')

# ================================================== 02 INTRODUCTION
_notes = [("01","Read Section 01 first",
  "Every visual rule that follows carries the story in Brand. A layout that looks right but says "
  "the wrong thing has still failed."),
 ("02","Work from Section 03",
  "Visual Identity is the working reference. Mark, colour and type rules are specified with values "
  "you can copy straight into a file."),
 ("03","Check 3.6 before you ship",
  "The Logo Don&rsquo;ts page is short on purpose. If your artwork appears there, change it."),
 ("04","This edition is a draft",
  "Pages marked with a dashed frame are placeholders. Colour and type are proposed, pending match "
  "against the held brand assets.")]
sheet("0.1 Introduction", "00 Essentials", "00 &middot; Essentials", "0.1 &middot; Introduction",
  "Introduction",
  "This is the Vit&rsquo;s Brand Book. It defines who we are, how we speak and how the identity is "
  "applied, in the shortest form that still governs the work.",
  f'''<div style="display:flex;flex-direction:column;height:100%">
  <div class="grid" style="grid-template-columns:repeat(4,1fr);flex:none">
  {"".join(f"""<div class="rv" style="--d:{220+i*55}ms;border-top:1px solid var(--ink14);padding-top:18px">
    <div class="mono s dim">{n}</div>
    <h3 style="font-family:var(--fd);font-weight:800;font-size:19px;letter-spacing:-.012em;margin:9px 0 0">{t}</h3>
    <p style="font-size:18px;line-height:28px;color:var(--ink72);margin-top:9px">{b}</p></div>"""
    for i, (n, t, b) in enumerate(_notes))}
  </div>
  <div class="rv" style="--d:420ms;flex:1;min-height:0;display:grid;
    grid-template-columns:auto 1fr 1.05fr;gap:60px;align-items:center;padding:40px 0;
    margin-top:44px;border-top:1px solid var(--ink14);
    border-bottom:1px solid var(--ink14);margin-bottom:40px">
    <div style="display:flex;flex-direction:column;gap:14px">
      <span class="mono s dim">The mark</span>{mark(200)}</div>
    <div style="display:flex;flex-direction:column;gap:14px">
      <span class="mono s dim">Five colours</span>
      <div style="display:flex;gap:10px">
      {"".join(f"""<div style="flex:1"><div style="height:62px;background:{c};
        {'border:1px solid var(--ink14);' if c == STEAM else ''}"></div>
        <div class="mono s dim" style="margin-top:7px;font-size:10.5px">{n}</div></div>"""
        for n, c in [("Red",RED),("Gold",GOLD),("Ink",INK),("Steam",STEAM),("Broth",BROTH)])}</div></div>
    <div style="display:flex;flex-direction:column;gap:14px">
      <span class="mono s dim">Three faces</span>
      <div style="display:flex;gap:26px;align-items:baseline">
      {"".join(f"""<div><div style="font-family:{ff};font-weight:{w};font-stretch:{st};
        font-size:40px;line-height:1;letter-spacing:-.01em">Aa</div>
        <div class="mono s dim" style="margin-top:9px;font-size:10.5px">{n}</div></div>"""
        for n, ff, w, st in [("Archivo","var(--fd)","800","112%"),("Figtree","var(--ft)","500","100%"),
                             ("JB Mono","var(--fm)","500","100%")])}</div></div>
  </div>
  <div class="rv" style="--d:480ms"><div style="display:flex;align-items:center;gap:26px;
    padding:26px 32px;background:{INK};color:#fff">
    <span class="mono s" style="color:{GOLD};flex:none">Brand promise</span>
    <span style="font-family:var(--fd);font-weight:800;font-stretch:110%;font-size:30px;
      letter-spacing:-.018em">The only one. Since 1975.</span></div></div></div>''')

# ============================================== 03 TABLE OF CONTENTS
_toc = [("01","Brand",[("1.1","Company Introduction","05"),("1.2","Positioning and Script","06"),
                       ("1.3","Vision and Mission","07"),("1.4","Values and Culture","08")]),
        ("02","Verbal Identity",[("2.1","Messaging Pillars","10"),("2.2","Voice and Character","11")]),
        ("03","Visual Identity",[("3.1","Logo Overview","13"),("3.2","Logo Concept","14"),
                       ("3.3","Logo Formats","15"),("3.4","Clearspace and Size","16"),
                       ("3.5","Backgrounds","17"),("3.6","Logo Don&rsquo;ts","18"),
                       ("3.7","Colour Palette","19"),("3.8","Colour in Use","20"),
                       ("3.9","Typography","21"),("3.10","Type Scale","22"),
                       ("3.11","Language Variants","23")]),
        ("04","Application",[("4.1","Packaging System","25"),("4.2","Stationery","26"),
                       ("4.3","Retail and Shelf","27"),("4.4","Digital and Social","28")]),
        ("05","Close",[("5.1","Contacts and Legal","29")])]
def _col(num, title, rows, d):
    r = "".join(f'''<div style="display:flex;align-items:baseline;gap:12px;padding:9px 0;
      border-top:1px solid var(--ink08)"><span class="mono s dim" style="width:34px;flex:none">{a}</span>
      <span style="flex:1;font-size:17.5px;line-height:25px">{b}</span>
      <span class="mono s dim" style="flex:none">{c}</span></div>''' for a, b, c in rows)
    return f'''<div class="rv" style="--d:{d}ms">
      <div style="display:flex;align-items:baseline;gap:12px;padding-bottom:13px">
        <span class="num" style="font-size:30px;font-stretch:115%">{num}</span>
        <span style="font-family:var(--fd);font-weight:800;font-size:22px;letter-spacing:-.012em">{title}</span></div>
      {r}</div>'''
sheet("0.2 Table of Contents", "00 Essentials", "00 &middot; Essentials", "0.2 &middot; Table of Contents",
  "Table of Contents",
  "Thirty pages in five sections. Section 03 is the one most people will use daily.",
  f'''<div style="display:grid;grid-template-columns:1fr 1fr 1.15fr;gap:60px;height:100%;align-content:start">
  <div style="display:flex;flex-direction:column;gap:36px">{_col("01","Brand",_toc[0][2],200)}{_col("02","Verbal Identity",_toc[1][2],260)}</div>
  <div style="display:flex;flex-direction:column;gap:36px">{_col("04","Application",_toc[3][2],380)}{_col("05","Close",_toc[4][2],430)}</div>
  <div>{_col("03","Visual Identity",_toc[2][2],320)}</div></div>''', ground="steam")

# ==================================================== 04 DIVIDER 01
divider("01","Brand",
  "Where Vit&rsquo;s came from, what it stands for and the promise every pack has to keep. "
  "Read this before touching anything visual.",
  [("1.1","Company Introduction"),("1.2","Positioning and Script"),
   ("1.3","Vision and Mission"),("1.4","Values and Culture")],
  "01 &middot; Brand", "01 Brand")
