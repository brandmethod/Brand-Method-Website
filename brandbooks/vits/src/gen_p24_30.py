# ==================================================== 24 DIVIDER 04
divider("04","Application",
  "How the system lands on the things Vit&rsquo;s actually makes and sends out. Every page in this "
  "section is a wireframe &mdash; structure fixed, art direction still open.",
  [("4.1","Packaging System"),("4.2","Stationery"),("4.3","Retail and Shelf"),("4.4","Digital and Social")],
  "04 &middot; Application", "04 Application")

def zone(label, h, bg="rgba(25,20,16,.05)", fg=INK, border="1px solid rgba(25,20,16,.16)",
         extra="", inner=None):
    return (f'<div style="height:{h};background:{bg};border:{border};display:flex;align-items:center;'
            f'justify-content:center;color:{fg};font-family:var(--fm);font-size:9.5px;'
            f'letter-spacing:.14em;text-transform:uppercase;text-align:center;flex:none;{extra}">'
            f'{inner if inner is not None else label}</div>')

# ================================================ 25 PACKAGING SYSTEM
_zones = [("1","Brand block","Stacked lockup, centred, never smaller than 28 mm wide."),
  ("2","Flavour band","Full-bleed colour band. One flavour, one colour, held in the flavour register."),
  ("3","Descriptor","Figtree 600. Product name in English and Bahasa Malaysia, equal weight."),
  ("4","Serving image","Photography window. Bowl three-quarter, steam visible, no props competing."),
  ("5","Net weight","JetBrains Mono 700. Bottom left, always in grams."),
  ("6","Halal and certification","HALAL Malaysia lockup plus plant code. Never resized, never recoloured.")]
_flavours = [("Chicken", "#C8961E"), ("Curry", "#D8232A"), ("Tom Yam", "#E2571F"),
             ("Asam Laksa", "#8E2A4E"), ("Vegetarian", "#3F7A3A"), ("Aglio Olio", "#1F5B7A")]
sheet("4.1 Packaging System", "04 Application", "04 &middot; Application", "4.1 &middot; Packaging System",
  "Packaging System",
  "The front of pack is a fixed six-zone grid. Flavour changes the band colour and nothing else.",
  f'''<div style="display:grid;grid-template-columns:400px 1fr 1fr;gap:56px;height:100%">
  <div class="rv" style="--d:200ms;display:flex;flex-direction:column">
    <span class="mono s acc" style="margin-bottom:14px">Front of pack &mdash; wireframe</span>
    <div style="flex:1;min-height:0;background:var(--paper);border:1px solid var(--ink14);
      padding:16px;display:flex;flex-direction:column;gap:9px;position:relative">
      <div style="height:78px;background:{STEAM};border:1px dashed rgba(25,20,16,.22);display:flex;
        align-items:center;justify-content:center;flex:none;position:relative">
        <span style="position:absolute;left:8px;top:6px;font-family:var(--fm);font-size:9px;
          color:var(--ink54)">1</span>
        <span style="display:flex;flex-direction:column;align-items:center;gap:6px">{mark(36)}{wordmark(19)}</span>
      </div>
      <div style="height:38px;background:{RED};flex:none;display:flex;align-items:center;
        padding:0 12px;position:relative">
        <span style="position:absolute;left:8px;top:4px;font-family:var(--fm);font-size:9px;
          color:rgba(255,255,255,.7)">2</span>
        <span style="font-family:var(--fd);font-weight:800;font-stretch:112%;font-size:19px;
          color:#fff;margin:0 auto">CURRY</span></div>
      <div style="flex:none;position:relative;padding-left:0">
        <span style="position:absolute;left:0;top:-2px;font-family:var(--fm);font-size:9px;
          color:var(--ink54)">3</span>
        <div style="text-align:center;font-family:var(--ft);font-weight:600;font-size:13px;
          line-height:1.5;color:var(--ink);padding-top:8px">Instant Noodles<br>
          <span style="color:var(--ink54);font-weight:400">Mi Segera</span></div></div>
      <div class="slot" style="flex:1;min-height:0;position:relative">
        <span style="position:absolute;left:8px;top:6px;font-family:var(--fm);font-size:9px;
          color:var(--ink54)">4</span>
        <span class="st" style="font-size:14px">Serving image</span>
        <span class="sm" style="font-size:9px">Photography to be shot</span></div>
      <div style="display:flex;gap:9px;flex:none;align-items:stretch">
        <div style="flex:1;border:1px dashed rgba(25,20,16,.22);padding:8px 10px;position:relative">
          <span style="position:absolute;left:6px;top:4px;font-family:var(--fm);font-size:9px;
            color:var(--ink54)">5</span>
          <div style="font-family:var(--fm);font-weight:700;font-size:16px;color:var(--ink);
            text-align:center;padding-top:6px">75 g</div></div>
        <div style="flex:1.25;border:1px dashed rgba(25,20,16,.22);display:flex;align-items:center;
          justify-content:center;gap:7px;position:relative;padding:8px">
          <span style="position:absolute;left:6px;top:4px;font-family:var(--fm);font-size:9px;
            color:var(--ink54)">6</span>
          <span style="font-family:var(--fm);font-size:8.5px;letter-spacing:.1em;color:var(--ink54);
            text-align:center;line-height:1.6">HALAL MALAYSIA<br>FSSC 22000</span></div></div>
    </div>
  </div>
  <div class="rv" style="--d:280ms;display:flex;flex-direction:column">
    <span class="mono s acc" style="margin-bottom:14px">Zones</span>
    {"".join(f'''<div style="display:grid;grid-template-columns:30px 1fr;gap:14px;padding:14px 0;
      border-top:1px solid var(--ink14);align-items:start">
      <span style="width:24px;height:24px;border-radius:50%;background:{INK};color:#fff;display:flex;
        align-items:center;justify-content:center;font-family:var(--fm);font-size:11px;font-weight:700">{n}</span>
      <div><div style="font-family:var(--fd);font-weight:800;font-size:17px;letter-spacing:-.01em">{t}</div>
      <div style="font-size:14.5px;line-height:22px;color:var(--ink72);margin-top:5px">{b}</div></div></div>'''
      for n, t, b in _zones)}
  </div>
  <div class="rv" style="--d:360ms;display:flex;flex-direction:column">
    <span class="mono s acc" style="margin-bottom:14px">Flavour register &mdash; draft</span>
    <div style="display:flex;flex-direction:column;gap:10px">
    {"".join(f'''<div style="display:flex;align-items:center;gap:14px">
      <div style="width:76px;height:44px;background:{c};flex:none"></div>
      <div style="flex:1"><div style="font-family:var(--fd);font-weight:800;font-size:16px">{n}</div>
      <div class="mono s dim" style="margin-top:3px;font-size:9.5px">{c.upper()}</div></div></div>'''
      for n, c in _flavours)}</div>
    <div style="flex:1"></div>
    <div style="background:{INK};color:#fff;padding:18px 20px;display:flex;gap:16px;margin-top:20px">
      <span class="mono s" style="color:{GOLD};flex:none">Draft</span>
      <span style="font-size:14.5px;line-height:22px;color:var(--w72)">Flavour colours are proposed.
      Each must be matched to the current pack before it enters the register, and no two flavours may
      sit within &Delta;E 5 of each other on shelf.</span></div>
  </div></div>''', ground="steam")

# ==================================================== 26 STATIONERY
sheet("4.2 Stationery", "04 Application", "04 &middot; Application", "4.2 &middot; Stationery",
  "Stationery",
  "Letterhead, card and compliment slip. The mark sits top left on everything; the red rule is the "
  "only ornament.",
  f'''<div style="display:grid;grid-template-columns:1fr 1.5fr;gap:56px;height:100%">
  <div class="rv" style="--d:200ms;display:flex;flex-direction:column">
    <span class="mono s acc" style="margin-bottom:14px">Letterhead &mdash; A4 portrait</span>
    <div style="flex:1;min-height:0;background:var(--paper);border:1px solid var(--ink14);
      padding:30px 34px;display:flex;flex-direction:column">
      <div style="display:flex;align-items:flex-start;justify-content:space-between">
        {lockup(40, 28)}
        <span style="font-family:var(--fm);font-size:8px;letter-spacing:.12em;color:var(--ink54);
          text-align:right;line-height:1.9">VIT MAKANAN (KL) SDN BHD<br>25143-H</span></div>
      <div style="height:3px;background:{RED};margin-top:16px;flex:none"></div>
      <div style="margin-top:22px;display:flex;flex-direction:column;gap:7px">
        {"".join(f'<div style="height:6px;background:rgba(25,20,16,.10);width:{w}%"></div>' for w in
          [46,100,100,94,100,88,100,72,100,100,66])}
      </div>
      <div style="flex:1"></div>
      <div style="border-top:1px solid var(--ink14);padding-top:11px;font-family:var(--fm);
        font-size:7.5px;letter-spacing:.1em;color:var(--ink54);line-height:1.9">
        LOT 126, JALAN TAMAN INDUSTRI, INTEGRASI RAWANG 1/2, 48000 RAWANG, SELANGOR<br>
        +603 6093 3999 &nbsp;&middot;&nbsp; VIT@VIT.COM.MY &nbsp;&middot;&nbsp; VITSNOODLES.COM</div>
    </div>
  </div>
  <div style="display:flex;flex-direction:column;gap:26px">
    <div class="rv" style="--d:280ms;flex:1;min-height:0;display:grid;grid-template-columns:1fr 1fr;gap:26px">
      <div style="display:flex;flex-direction:column">
        <span class="mono s acc" style="margin-bottom:12px">Business card &mdash; face</span>
        <div style="flex:1;min-height:0;background:var(--paper);border:1px solid var(--ink14);
          padding:26px 28px;display:flex;flex-direction:column;justify-content:space-between">
          <div>{lockup(34, 24)}</div>
          <div><div style="font-family:var(--fd);font-weight:800;font-size:19px;letter-spacing:-.012em">
            Name Surname</div>
            <div style="font-family:var(--ft);font-size:13px;color:var(--ink72);margin-top:3px">Role, Department</div>
            <div style="height:2px;background:{RED};width:34px;margin:13px 0"></div>
            <div style="font-family:var(--fm);font-size:9px;letter-spacing:.09em;color:var(--ink54);
              line-height:2">+603 6093 3999<br>NAME@VIT.COM.MY</div></div></div>
      </div>
      <div style="display:flex;flex-direction:column">
        <span class="mono s acc" style="margin-bottom:12px">Business card &mdash; reverse</span>
        <div style="flex:1;min-height:0;background:{RED};display:flex;align-items:center;
          justify-content:center;position:relative;overflow:hidden">
          <div style="position:absolute;right:-70px;bottom:-60px;opacity:.20">{symbol(280, STEAM, "rgba(250,244,233,.6)")}</div>
          <span style="position:relative;display:flex;flex-direction:column;align-items:center;gap:14px">
            {mark(52, "#fff", "#fff", "#fff")}
            <span style="font-family:var(--fd);font-weight:800;font-stretch:110%;font-size:15px;
              color:#fff;text-align:center;line-height:1.5">The only one.<br>Since 1975.</span></span></div>
      </div>
    </div>
    <div class="rv" style="--d:360ms;flex:none;height:210px;display:flex;flex-direction:column">
      <span class="mono s acc" style="margin-bottom:12px">Compliment slip &mdash; DL</span>
      <div style="flex:1;min-height:0;background:var(--paper);border:1px solid var(--ink14);
        padding:24px 30px;display:flex;align-items:center;justify-content:space-between">
        {lockup(38, 26)}
        <span style="font-family:var(--fd);font-weight:800;font-size:24px;letter-spacing:-.014em;
          color:var(--ink54)">With compliments</span>
        <span style="font-family:var(--fm);font-size:9px;letter-spacing:.1em;color:var(--ink54);
          text-align:right;line-height:2">RAWANG, SELANGOR<br>VITSNOODLES.COM</span></div>
    </div>
  </div></div>''')

# ============================================== 27 RETAIL AND SHELF
sheet("4.3 Retail and Shelf", "04 Application", "04 &middot; Application", "4.3 &middot; Retail and Shelf",
  "Retail and Shelf",
  "Vit&rsquo;s is bought in a second, in a crowded aisle. The block has to read as one brand before "
  "any single pack reads as a flavour.",
  f'''<div style="display:flex;flex-direction:column;height:100%;gap:26px">
  <div class="rv" style="--d:200ms;flex:1;min-height:0;display:flex;flex-direction:column">
    <span class="mono s acc" style="margin-bottom:12px">Shelf block &mdash; six facings, one brand</span>
    <div style="flex:1;min-height:0;background:var(--paper);border:1px solid var(--ink14);
      padding:20px;display:flex;gap:12px;align-items:stretch">
      {"".join(f'''<div style="flex:1;display:flex;flex-direction:column;gap:6px;background:{STEAM};
        border:1px solid rgba(25,20,16,.12);padding:12px 10px">
        <div style="display:flex;flex-direction:column;align-items:center;gap:4px;flex:none">
          {mark(24)}<span style="font-family:var(--fd);font-weight:800;font-stretch:115%;font-size:11px;
          color:{INK}">VIT&rsquo;S</span></div>
        <div style="height:22px;background:{c};display:flex;align-items:center;justify-content:center;
          flex:none;margin-top:2px"><span style="font-family:var(--fd);font-weight:800;font-size:9.5px;
          color:#fff;letter-spacing:.02em">{n.upper()}</span></div>
        <div class="slot" style="flex:1;min-height:0;border-style:dashed">
          <span class="sm" style="font-size:8px">Image</span></div>
        <div style="font-family:var(--fm);font-size:8px;color:var(--ink54);text-align:center;
          flex:none">75 G</div></div>''' for n, c in _flavours)}
    </div>
  </div>
  <div style="flex:none;height:250px;display:grid;grid-template-columns:1.1fr 1fr 1fr;gap:26px">
    <div class="rv" style="--d:280ms;display:flex;flex-direction:column">
      <span class="mono s acc" style="margin-bottom:12px">Shipping carton</span>
      <div style="flex:1;min-height:0;background:#D9C9A8;border:1px solid var(--ink14);
        padding:18px 22px;display:flex;flex-direction:column;justify-content:space-between">
        <div style="display:flex;align-items:center;justify-content:space-between">
          {lockup(30, 21, INK, INK, INK, INK)}
          <span style="font-family:var(--fm);font-size:8.5px;letter-spacing:.1em;color:rgba(25,20,16,.62)">
            1&nbsp;PLATE&nbsp;/&nbsp;INK</span></div>
        <div style="font-family:var(--fm);font-size:10px;letter-spacing:.11em;color:rgba(25,20,16,.72);
          line-height:2.1">INSTANT NOODLES &middot; CURRY<br>40 &times; 75 G &nbsp;&middot;&nbsp; NET 3.0 KG<br>
          BATCH &nbsp;&middot;&nbsp; BEST BEFORE</div></div>
    </div>
    <div class="rv" style="--d:340ms;display:flex;flex-direction:column">
      <span class="mono s acc" style="margin-bottom:12px">Shelf wobbler</span>
      <div style="flex:1;min-height:0;background:{RED};display:flex;flex-direction:column;
        align-items:center;justify-content:center;gap:10px;text-align:center;padding:16px">
        {mark(38, "#fff", "#fff", "#fff")}
        <span style="font-family:var(--fd);font-weight:800;font-stretch:112%;font-size:21px;
          color:#fff;line-height:1.2">Halal since 1980</span>
        <span style="font-family:var(--ft);font-size:12.5px;color:rgba(255,255,255,.84)">Made in Rawang</span></div>
    </div>
    <div class="rv" style="--d:400ms;display:flex;flex-direction:column">
      <span class="mono s acc" style="margin-bottom:12px">Gondola end &mdash; header</span>
      <div class="slot" style="flex:1;min-height:0">
        <span class="st">Retail photography</span>
        <span class="sm">Art direction pending</span></div>
    </div>
  </div></div>''', ground="steam")

# ============================================= 28 DIGITAL AND SOCIAL
sheet("4.4 Digital and Social", "04 Application", "04 &middot; Application", "4.4 &middot; Digital and Social",
  "Digital and Social",
  "The mark shrinks a long way online. Below 28 px the symbol replaces the lockup, without exception.",
  f'''<div style="display:grid;grid-template-columns:1.45fr 1fr;gap:50px;height:100%">
  <div style="display:flex;flex-direction:column;gap:24px">
    <div class="rv" style="--d:200ms;flex:none;display:flex;flex-direction:column">
      <span class="mono s acc" style="margin-bottom:12px">Website header</span>
      <div style="background:var(--paper);border:1px solid var(--ink14)">
        <div style="display:flex;align-items:center;justify-content:space-between;padding:16px 24px;
          border-bottom:1px solid var(--ink14)">
          {lockup(30, 21)}
          <div style="display:flex;align-items:center;gap:22px">
            {"".join(f'<span style="font-family:var(--ft);font-weight:500;font-size:12.5px;color:var(--ink72)">{x}</span>' for x in ["Products","About","OEM","Private Label","Blog"])}
            <span style="font-family:var(--ft);font-weight:600;font-size:12px;color:#fff;
              background:{RED};padding:8px 16px">Contact us</span></div></div>
        <div class="slot" style="height:132px;border-left:none;border-right:none;border-bottom:none">
          <span class="st">Hero &mdash; bowl photography</span>
          <span class="sm">Art direction pending</span></div></div>
    </div>
    <div class="rv" style="--d:280ms;flex:1;min-height:0;display:grid;grid-template-columns:repeat(3,1fr);
      gap:20px;align-content:start">
      {"".join(f'''<div style="display:flex;flex-direction:column;gap:9px;min-height:0">
        <div style="aspect-ratio:1;background:{bg};display:flex;flex-direction:column;
          justify-content:{jc};padding:20px;gap:10px;{'border:1px solid var(--ink14);' if bg == PAPER else ''}">
          {inner}</div>
        <span class="mono s dim" style="font-size:9.5px">{cap}</span></div>'''
        for bg, jc, inner, cap in [
          (RED, "space-between",
           f'{mark(30, "#fff", "#fff", "#fff")}<span style="font-family:var(--fd);font-weight:800;'
           f'font-stretch:110%;font-size:23px;color:#fff;line-height:1.16">Fifty years of the everyday bowl.</span>',
           "1:1 &mdash; statement post"),
          (INK, "space-between",
           f'<span class="mono s" style="color:{GOLD};font-size:9px">NEW FLAVOUR</span>'
           f'<div class="slot" style="flex:1;min-height:0;margin:8px 0"><span class="sm" style="font-size:8.5px">Product shot</span></div>'
           f'<span style="font-family:var(--fd);font-weight:800;font-size:16px;color:#fff">Italian Mi Goreng</span>',
           "1:1 &mdash; product post"),
          (PAPER, "space-between",
           f'<span style="font-family:var(--fd);font-weight:800;font-size:19px;letter-spacing:-.012em;'
           f'line-height:1.25;color:{INK}">Halal since 1980. Not because anyone asked.</span>'
           f'<div style="display:flex;align-items:center;gap:9px">{mark(22)}'
           f'<span style="font-family:var(--fm);font-size:9px;letter-spacing:.1em;color:var(--ink54)">@VITSNOODLES</span></div>',
           "1:1 &mdash; editorial post")])}
    </div>
  </div>
  <div style="display:flex;flex-direction:column;gap:24px">
    <div class="rv" style="--d:340ms;flex:none">
      <span class="mono s acc">Avatars and icons</span>
      <div style="display:flex;align-items:flex-end;gap:22px;margin-top:14px;background:var(--paper);
        border:1px solid var(--ink14);padding:22px 24px">
        {"".join(f'''<div style="display:flex;flex-direction:column;align-items:center;gap:9px">
          <div style="width:{s}px;height:{s}px;border-radius:50%;background:{RED};display:flex;
            align-items:center;justify-content:center">{symbol(int(s*0.6), "#fff", "#fff")}</div>
          <span class="mono s dim" style="font-size:9px">{s}</span></div>''' for s in [76, 52, 36, 28])}
        <div style="display:flex;flex-direction:column;align-items:center;gap:9px">
          <div style="width:32px;height:32px;background:{RED};display:flex;align-items:center;
            justify-content:center">{symbol(20, "#fff", "#fff")}</div>
          <span class="mono s dim" style="font-size:9px">Favicon</span></div></div>
    </div>
    <div class="rv" style="--d:400ms;flex:1;min-height:0;display:flex;flex-direction:column">
      <span class="mono s acc">Email signature &mdash; Arial, no images</span>
      <div style="flex:1;min-height:0;background:var(--paper);border:1px solid var(--ink14);
        padding:24px 26px;margin-top:14px;font-family:var(--fa);display:flex;flex-direction:column;
        justify-content:flex-start">
        <div style="font-size:15px;font-weight:700;color:{INK}">Name Surname</div>
        <div style="font-size:13px;color:var(--ink72);margin-top:2px">Role, Department</div>
        <div style="height:2px;background:{RED};width:38px;margin:12px 0"></div>
        <div style="font-size:12.5px;line-height:1.85;color:var(--ink72)">
          <b style="color:{INK}">Vit Makanan (KL) Sdn Bhd</b><br>
          Rawang, Selangor, Malaysia<br>
          +603 6093 3999 &nbsp;&middot;&nbsp; vitsnoodles.com</div>
        <div style="font-size:11px;color:var(--ink54);margin-top:12px">Halal certified since 1980</div>
        <div style="flex:1"></div>
        <div style="border-top:1px solid var(--ink14);padding-top:14px;margin-top:18px;
          font-family:var(--ft);font-size:13.5px;line-height:21px;color:var(--ink72)">
          <b style="color:{INK}">No image files.</b> Signatures are live text so they survive
          forwarding, corporate filters and dark mode. Never paste the lockup as a picture.</div></div>
    </div>
  </div></div>''')

# ============================================== 29 CONTACTS AND LEGAL
_contact = [("Brand governance","Brand Method &mdash; appointed agency of record"),
  ("Artwork approval","All packaging artwork routes through Marketing before separation"),
  ("Legal entity","Vit Makanan (Kuala Lumpur) Sdn Bhd &nbsp;(25143-H)"),
  ("Registered address","Lot 126, Jalan Taman Industri, Integrasi Rawang 1/2,<br>Taman Industri "
   "Integrasi Rawang, 48000 Rawang, Selangor, Malaysia"),
  ("Telephone","+603 6093 3999"),("Facsimile","+603 6093 3888"),
  ("Email","vit@vit.com.my"),("Web","vitsnoodles.com")]
sheet("5.1 Contacts and Legal", "05 Close", "05 &middot; Close", "5.1 &middot; Contacts and Legal",
  "Contacts and Legal",
  "Anything this book does not answer comes here before it goes to artwork.",
  f'''<div style="display:grid;grid-template-columns:1.15fr 1fr;gap:70px;height:100%">
  <div class="rv" style="--d:200ms;display:flex;flex-direction:column"><table class="spec">
    {"".join(f"<tr><td>{k}</td><td>{v}</td></tr>" for k, v in _contact)}</table>
    <div style="flex:1"></div>
    <div style="border:1px solid var(--ink14);background:var(--paper);padding:36px 40px;
      display:flex;align-items:center;justify-content:space-between;gap:34px;margin-top:34px">
      {lockup(78, 54)}
      <span style="text-align:right"><span class="mono s acc">Master files</span>
        <span style="display:block;font-size:15.5px;line-height:24px;color:var(--ink72);
          margin-top:9px;max-width:260px">Vector artwork, colour profiles and the licensed font
          files are released by Brand Governance on request.</span></span>
    </div></div>
  <div style="display:flex;flex-direction:column;gap:24px">
    <div class="rv" style="--d:280ms;background:{INK};color:#fff;padding:28px 32px">
      <span class="mono s" style="color:{GOLD}">Status of this edition</span>
      <div style="font-size:16.5px;line-height:26px;color:var(--w72);margin-top:14px">
        V1.0 is a <b style="color:#fff">wireframe draft</b>. Structure, hierarchy and copy are
        proposed for review. The mark, the palette and the typeface selection are a design proposal
        &mdash; they have not yet been reconciled against the artwork Vit&rsquo;s currently holds,
        and no file in this edition is a production master.</div>
    </div>
    <div class="rv" style="--d:340ms;display:flex;flex-direction:column;gap:16px">
      <span class="mono s acc">Before V2.0 is signed off</span>
      {"".join(f'''<div style="display:flex;gap:13px;align-items:baseline;padding-bottom:13px;
        border-bottom:1px solid var(--ink08)">
        <span class="mono s" style="color:{REDD};flex:none">{i+1:02d}</span>
        <span style="font-size:15.5px;line-height:24px;color:var(--ink72)">{t}</span></div>'''
        for i, t in enumerate([
          "Reconcile the mark against the held vector masters and pack artwork.",
          "Match Pantone references on a printed pack under D50.",
          "Confirm the wordmark typeface, or commission the drawing.",
          "Lock the flavour register against current retail range.",
          "Commission the photography the wireframes leave open."]))}
    </div>
    <div style="flex:1"></div>
    <div class="rv" style="--d:420ms;padding-top:16px;border-top:1px solid var(--ink14);
      font-size:14px;line-height:22px;color:var(--ink54)">
      Vit&rsquo;s, the phoenix symbol and the Vit&rsquo;s wordmark are trade marks of Vit Makanan
      (Kuala Lumpur) Sdn Bhd. This document is confidential and issued for internal and authorised
      partner use only. Do not redistribute.</div>
  </div></div>''', ground="steam")

# ================================================== 30 BACK COVER
n = len(PAGES) + 1
raw("Back Cover", "Back", ground="ink", inner=f'''
<div style="position:absolute;right:-160px;top:50%;transform:translateY(-50%);opacity:.09;z-index:1">
  {symbol(760, "#fff", GOLD)}</div>
<div class="cv" style="justify-content:center;z-index:3">
  <div class="rv" style="--d:60ms">{lockup(96, 66, "#fff", RED, GOLD, "#fff")}</div>
  <div class="rv" style="--d:130ms;font-family:var(--fd);font-weight:800;font-stretch:114%;
    font-size:80px;line-height:1.05;letter-spacing:-.028em;color:#fff;margin-top:40px;max-width:1100px">
    The only one.<br>Since 1975.</div>
  <div class="rv" style="--d:200ms;font-size:20px;line-height:32px;color:var(--w72);
    max-width:560px;margin-top:26px">
    Vit Makanan (Kuala Lumpur) Sdn Bhd &mdash; Rawang, Selangor, Malaysia.
    Halal certified since 1980. Exporting to more than thirty countries.</div>
</div>
<div style="position:absolute;left:120px;bottom:40px;right:120px;z-index:4;display:flex;
  align-items:center;justify-content:space-between;font-family:var(--fm);font-size:10.5px;
  letter-spacing:.16em;text-transform:uppercase;color:var(--w52)">
  <span>{COPY}</span><span style="color:{GOLD};font-weight:700">{n:02d}</span></div>''')
