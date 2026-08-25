# ============================================ 05 COMPANY INTRODUCTION
_spec = [("Legal entity","Vit Makanan (Kuala Lumpur) Sdn Bhd &nbsp;(25143-H)"),
         ("Founded","1975, noodle making begins in Selayang"),
         ("Head office and plant","Rawang, Selangor, Malaysia"),
         ("Facility","105,000 sq ft, Taman Industri Integrasi Rawang"),
         ("Markets","Malaysia nationwide, plus 30+ export countries"),
         ("Certification","HALAL Malaysia, FSSC 22000, ISO 22000, HACCP, GMP, SMETA"),
         ("Categories","Instant noodles, fresh and air dried noodles, OEM and private label")]
_chapters = [("1975","A kitchen in Selayang","A passion for making noodles becomes a business."),
  ("1980","Halal by choice","Certification sought and obtained, so every Malaysian could eat it."),
  ("Growth","Rawang, 105,000 sq ft","The plant moves to meet rising international demand."),
  ("Standard","HACCP, GMP, FSSC 22000","Food safety anchored to global benchmarks at every stage."),
  ("Today","30+ countries","Asia, the Middle East, Europe and beyond.")]
sheet("1.1 Company Introduction", "01 Brand", "01 &middot; Brand", "1.1 &middot; Company Introduction",
  "Company Introduction",
  "One of Malaysia&rsquo;s pioneer noodle manufacturers. Fifty years of making the everyday bowl, "
  "and exporting it.",
  f'''<div style="display:flex;flex-direction:column;height:100%;gap:34px">
  <div style="display:grid;grid-template-columns:1.05fr 1fr;gap:70px">
    <div class="rv" style="--d:200ms">
      <p class="p">Vit&rsquo;s began in 1975 as a passion for making noodles. From a small kitchen in
      Selayang it has grown into a leading Malaysian halal certified noodle brand, exporting to more
      than thirty countries.</p>
      <p class="p">The name comes from the Mandarin <b style="color:var(--ink)">Wei Yi</b>,
      meaning <i>the only one</i>. The phoenix that carries it stands for power, renewal and longevity.
      Vit&rsquo;s intends to be Malaysia&rsquo;s one and only noodle expert of choice.</p>
      <div style="display:flex;margin-top:38px;border-top:1px solid var(--ink14);padding-top:26px">
      {"".join(f'''<div style="flex:1;{'border-left:1px solid var(--ink14);padding-left:26px;' if i else 'padding-right:26px;'}">
        <div style="font-family:var(--fd);font-weight:800;font-stretch:114%;font-size:46px;
          line-height:1;letter-spacing:-.03em;color:{REDD}">{big}</div>
        <div class="mono s dim" style="margin-top:12px;line-height:1.85">{lab}</div></div>'''
        for i, (big, lab) in enumerate([("50+","Years in the<br>category"),
          ("30+","Export<br>markets"),("105k","Sq ft plant<br>in Rawang")]))}</div>
    </div>
    <div class="rv" style="--d:260ms"><table class="spec">
      {"".join(f"<tr><td>{k}</td><td>{v}</td></tr>" for k, v in _spec)}</table></div>
  </div>
  <div style="flex:1"></div>
  <div class="rv" style="--d:360ms">
    <div class="mono s acc" style="margin-bottom:16px">Five chapters</div>
    <div style="display:grid;grid-template-columns:repeat(5,1fr);gap:0;border-top:2px solid {RED}">
    {"".join(f'''<div style="padding:18px 26px 0 0;position:relative">
      <span style="position:absolute;left:0;top:-6px;width:9px;height:9px;background:{RED};
        border-radius:50%"></span>
      <div class="mono s" style="color:{REDD};padding-left:0">{y}</div>
      <div style="font-family:var(--fd);font-weight:800;font-size:18px;letter-spacing:-.01em;
        margin-top:8px;line-height:1.25">{t}</div>
      <div style="font-size:16.5px;line-height:25px;color:var(--ink72);margin-top:7px">{b}</div></div>'''
      for y, t, b in _chapters)}</div></div></div>''')

# =========================================== 06 POSITIONING AND SCRIPT
sheet("1.2 Positioning and Script", "01 Brand", "01 &middot; Brand", "1.2 &middot; Positioning and Script",
  "Positioning and Script",
  "One statement everyone agrees on, and the thirty seconds you say out loud when someone asks "
  "what Vit&rsquo;s is.",
  f'''<div style="display:flex;flex-direction:column;height:100%;gap:30px">
  <div class="rv" style="--d:200ms;background:{INK};color:#fff;padding:44px 52px">
    <div class="mono s" style="color:{GOLD}">Positioning statement</div>
    <div style="font-family:var(--fd);font-weight:800;font-stretch:107%;font-size:40px;line-height:1.24;
      letter-spacing:-.018em;margin-top:18px;max-width:1480px;text-wrap:balance">
      For every household that wants a good bowl without a second thought, Vit&rsquo;s is
      Malaysia&rsquo;s noodle expert: halal since 1980, made in Rawang to global food safety
      standard, and trusted in more than thirty countries.</div>
  </div>
  <div style="display:grid;grid-template-columns:1.3fr 1fr;gap:60px;flex:1;min-height:0">
    <div class="rv" style="--d:280ms">
      <div class="mono s acc">The thirty second script</div>
      <p class="p" style="margin-top:16px">&ldquo;Vit&rsquo;s has been making noodles in Malaysia
      since 1975. We started in a small kitchen in Selayang. Today we run a 105,000 square foot plant
      in Rawang and ship to more than thirty countries.</p>
      <p class="p">We took halal certification in 1980, before anyone asked us to, because a bowl of
      noodles should be something every Malaysian can share. Everything we make is built to FSSC 22000,
      HACCP and GMP standard.</p>
      <p class="p">We make our own brands, and we make other people&rsquo;s too: OEM and private
      label, from air dried to fresh noodle. If it is a noodle, we know how to make it well.&rdquo;</p>
    </div>
    <div class="rv" style="--d:340ms;display:flex;flex-direction:column;gap:20px">
    {"".join(f'''<div class="card" style="padding:22px 26px">
      <div class="mono s acc">{k}</div>
      <p style="margin-top:9px;font-size:18px;line-height:28px">{v}</p></div>'''
      for k, v in [("Who it is for",
        "Malaysian households first. Then distributors, retailers and OEM partners who need a "
        "manufacturer that will not embarrass them."),
        ("What we make",
        "Instant, fresh and air dried noodles under Vit&rsquo;s, and under partner brands through "
        "OEM and private label."),
        ("Why it matters",
        "Halal, safe and consistent is not a claim here. It is audited: FSSC 22000, HACCP, "
        "GMP and SMETA.")])}</div>
  </div></div>''', ground="steam")

# ============================================== 07 VISION AND MISSION
_mission = [("01","Make it halal, always",
   "Certification since 1980 is not a market tactic. It is the condition of being on every "
   "Malaysian table, whatever the faith of the household."),
  ("02","Hold the standard",
   "FSSC 22000 and ISO 22000 food safety management, critical control monitoring at every "
   "production stage, facilities aligned to Ministry of Health requirements."),
  ("03","Carry Malaysia outward",
   "Export the authentic taste of Malaysia, from Penang white curry to asam laksa "
   "and Hokkien mee, out to Asia, the Middle East, Europe and beyond."),
  ("04","Make it for others too",
   "OEM and private label built to the same standard as our own brands, for partners worldwide.")]
sheet("1.3 Vision and Mission", "01 Brand", "01 &middot; Brand", "1.3 &middot; Vision and Mission",
  "Vision and Mission",
  "The vision is old and it has not moved. The mission is how it gets kept.",
  f'''<div style="display:flex;flex-direction:column;height:100%;gap:34px">
  <div class="rv" style="--d:200ms;display:grid;grid-template-columns:170px 1fr;gap:44px;
    align-items:start;border-bottom:1px solid var(--ink14);padding-bottom:32px">
    <div class="mono s acc" style="padding-top:14px">Vision</div>
    <div style="font-family:var(--fd);font-weight:800;font-stretch:106%;font-size:42px;line-height:1.22;
      letter-spacing:-.02em;text-wrap:balance">Shared prosperity through something simple:
      a bowl of noodles welcome in every Malaysian home, regardless of race or religion.</div>
  </div>
  <div class="rv" style="--d:270ms"><div class="mono s acc">Mission</div></div>
  <div class="grid" style="grid-template-columns:repeat(4,1fr);flex:1;min-height:0;align-content:start">
  {"".join(f'''<div class="card rv" style="--d:{320+i*55}ms;display:flex;flex-direction:column">
    <div class="num" style="font-size:26px">{n}</div>
    <h3 style="margin-top:12px">{t}</h3><p>{b}</p></div>''' for i, (n, t, b) in enumerate(_mission))}
  </div></div>''')

# ============================================= 08 VALUES AND CULTURE
_values = [("Wei Yi, the only one",
   "The name is a standard, not a boast. If a competitor can do it the same way, we have not "
   "finished the job."),
  ("Halal by conviction",
   "We sought certification in 1980 because it was right, not because a buyer required it. That "
   "order of events is the value."),
  ("Rise again",
   "The phoenix is not decoration. Fifty years means recipes retired, lines rebuilt and markets "
   "lost and won back."),
  ("Everyone&rsquo;s table",
   "A bowl that works for every household in a multiracial country. No formulation that quietly "
   "excludes someone."),
  ("Made to standard",
   "Audited, not asserted. FSSC 22000, HACCP, GMP and SMETA, with the paperwork to show any "
   "buyer who asks.")]
sheet("1.4 Values and Culture", "01 Brand", "01 &middot; Brand", "1.4 &middot; Values and Culture",
  "Values and Culture",
  "Five values. Each one is a decision the company has actually had to make.",
  f'''<div style="display:grid;grid-template-columns:repeat(5,1fr);gap:0;height:100%;align-items:stretch">
  {"".join(f'''<div class="rv" style="--d:{200+i*60}ms;padding:0 30px 0 0;
    {'border-right:1px solid var(--ink14);' if i < 4 else ''}display:flex;flex-direction:column;
    {'padding-left:30px;' if i > 0 else ''}">
    <div style="height:6px;background:{RED};width:44px;flex:none"></div>
    <div style="font-family:var(--fd);font-weight:800;font-size:25px;line-height:1.22;
      letter-spacing:-.014em;margin-top:24px;text-wrap:balance">{t}</div>
    <div style="font-size:18px;line-height:29px;color:var(--ink72);margin-top:16px">{b}</div>
    <div style="flex:1"></div>
    <div class="mono s dim" style="margin-top:24px">Value {i+1:02d}</div></div>'''
    for i, (t, b) in enumerate(_values))}</div>''', ground="steam")
