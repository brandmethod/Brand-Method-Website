# ==================================================== 09 DIVIDER 02
divider("02","Verbal Identity",
  "What Vit&rsquo;s says, in what order, and the tone it says it in. Four pillars and one voice, "
  "used the same way by everyone.",
  [("2.1","Messaging Pillars"),("2.2","Voice and Character")],
  "02 &middot; Verbal Identity", "02 Verbal")

# ============================================== 10 MESSAGING PILLARS
_pillars = [("01","Fifty years of it",
  "Vit&rsquo;s has made noodles since 1975. Not a heritage story bolted on afterwards &mdash; the "
  "same business, still making the same category.",
  ["Founded 1975, Selayang","One of Malaysia&rsquo;s pioneer noodle manufacturers","50+ years in the category"]),
 ("02","Halal since 1980",
  "Certification was taken early and deliberately, so that a bowl of Vit&rsquo;s could be shared "
  "by any Malaysian household.",
  ["HALAL Malaysia certified","Certificate serial 1 001-01/2005","Pure, hygienic, permissible"]),
 ("03","Made to global standard",
  "Food safety management anchored on ISO 22000 and FSSC 22000, with critical-control monitoring "
  "at every production stage.",
  ["FSSC 22000 &amp; ISO 22000","HACCP and GMP","SMETA audited"]),
 ("04","From Rawang, outward",
  "A 105,000 sq ft plant supplying Malaysia nationwide and more than thirty export markets, "
  "under our brands and our partners&rsquo;.",
  ["30+ export countries","105,000 sq ft facility","OEM and private label"])]
sheet("2.1 Messaging Pillars", "02 Verbal", "02 &middot; Verbal Identity", "2.1 &middot; Messaging Pillars",
  "Messaging Pillars",
  "Four claims Vit&rsquo;s is entitled to make. Every one carries proof underneath it &mdash; if the "
  "proof is missing, the claim does not go out.",
  f'''<div class="grid" style="grid-template-columns:repeat(4,1fr);height:100%;align-items:stretch">
  {"".join(f'''<div class="card rv" style="--d:{200+i*60}ms;display:flex;flex-direction:column;padding:30px 30px 26px">
    <div class="num" style="font-size:26px">{n}</div>
    <h3 style="margin-top:12px;font-size:24px">{t}</h3>
    <p style="font-size:16px;line-height:25px">{b}</p>
    <div style="flex:1"></div>
    <div style="margin-top:24px;border-top:1px solid var(--ink14);padding-top:16px">
      <div class="mono s acc" style="margin-bottom:11px">Proof</div>
      {"".join(f"""<div style="display:flex;gap:9px;align-items:baseline;padding:4px 0">
        <span style="color:{RED};font-size:13px;flex:none">&#9679;</span>
        <span style="font-size:14.5px;line-height:21px;color:var(--ink72)">{p}</span></div>""" for p in ps)}
    </div></div>''' for i, (n, t, b, ps) in enumerate(_pillars))}</div>''')

# ============================================ 11 VOICE AND CHARACTER
_voice = [("Plain","Say the thing. A noodle brand that talks like a consultancy has lost the room."),
  ("Warm, not sentimental","This is food for ordinary evenings. Affection is fine; nostalgia-bait is not."),
  ("Specific","&lsquo;FSSC 22000&rsquo; beats &lsquo;world class&rsquo;. Numbers and names, every time."),
  ("Unhurried","Fifty years does not need to shout. Confidence reads as calm.")]
_rewrites = [("Vit&rsquo;s is a leading provider of premium noodle solutions.",
    "Vit&rsquo;s makes noodles. We have since 1975."),
  ("Our world-class facility upholds the highest standards of excellence.",
    "Our Rawang plant runs to FSSC 22000, HACCP and GMP."),
  ("Halal-certified for your peace of mind!",
    "Halal certified since 1980, so it can go on any Malaysian table."),
  ("An explosion of authentic Malaysian flavour in every bite!!",
    "Penang white curry mee, the way it is actually eaten in Penang.")]
sheet("2.2 Voice and Character", "02 Verbal", "02 &middot; Verbal Identity", "2.2 &middot; Voice and Character",
  "Voice and Character",
  "Four attributes, and the rewrites that show what each one means in practice.",
  f'''<div style="display:grid;grid-template-columns:.86fr 1.25fr;gap:64px;height:100%">
  <div style="display:flex;flex-direction:column">
    <div class="rv" style="--d:190ms" class="mono s acc"><span class="mono s acc">Attributes</span></div>
    <div style="display:flex;flex-direction:column;margin-top:18px">
    {"".join(f'''<div class="rv" style="--d:{230+i*55}ms;padding:20px 0;
      border-top:1px solid var(--ink14)">
      <div style="font-family:var(--fd);font-weight:800;font-size:24px;letter-spacing:-.014em">{t}</div>
      <div style="font-size:16px;line-height:25px;color:var(--ink72);margin-top:8px">{b}</div></div>'''
      for i, (t, b) in enumerate(_voice))}</div>
    <div style="flex:1"></div>
    <div class="rv" style="--d:470ms;display:flex;flex-wrap:wrap;gap:8px;padding-top:18px">
      {"".join(f'<span class="chip on">{w}</span>' for w in ["We are","Direct","Warm","Exact","Steady"])}
      {"".join(f'<span class="chip">{w}</span>' for w in ["Not","Salesy","Cute","Vague","Loud"])}
    </div>
  </div>
  <div class="rv" style="--d:300ms;display:flex;flex-direction:column">
    <span class="mono s acc">Say it this way</span>
    <div style="display:flex;flex-direction:column;gap:0;margin-top:18px;flex:1">
    {"".join(f'''<div style="display:grid;grid-template-columns:1fr 1fr;gap:22px;padding:18px 0;
      border-top:1px solid var(--ink14);align-items:start">
      <div style="display:flex;gap:11px;align-items:flex-start">
        <span style="flex:none;width:18px;height:18px;border-radius:50%;background:{BROTH};color:#fff;
          display:flex;align-items:center;justify-content:center;font-size:12px;margin-top:2px">&times;</span>
        <span style="font-size:16px;line-height:25px;color:var(--ink54);text-decoration:line-through;
          text-decoration-color:rgba(25,20,16,.28)">{a}</span></div>
      <div style="display:flex;gap:11px;align-items:flex-start">
        <span style="flex:none;width:18px;height:18px;border-radius:50%;background:{RED};color:#fff;
          display:flex;align-items:center;justify-content:center;font-size:11px;margin-top:2px">&#10003;</span>
        <span style="font-size:16.5px;line-height:25px;color:var(--ink)">{b}</span></div></div>'''
      for a, b in _rewrites)}</div>
  </div></div>''', ground="steam")

# ==================================================== 12 DIVIDER 03
divider("03","Visual Identity",
  "The working section. Mark, clearspace, palette and type, specified with values you can copy "
  "straight into artwork.",
  [("3.1","Logo Overview"),("3.2","Logo Concept"),("3.3","Logo Formats"),("3.4","Clearspace and Size"),
   ("3.5","Backgrounds"),("3.6","Logo Don&rsquo;ts"),("3.7","Colour Palette"),("3.8","Colour in Use"),
   ("3.9","Typography"),("3.10","Type Scale"),("3.11","Language Variants")],
  "03 &middot; Visual Identity", "03 Visual")
