import json, os
R = os.path.dirname(os.path.abspath(__file__))
P = json.load(open(os.path.join(R, ".artifact-parts.json")))

CHROME = """
/* ============================================================
   VIEWER SHELL
   The deck already carries a finished visual identity, so the
   chrome stays deferential: ALTIGO's own blues, the document's
   own typeface, and nothing that competes with a slide.
   Slides render identically in both themes by design — only the
   surrounding shell responds to the viewer's setting.
   ============================================================ */
:root{
  --v-bg:#E9EDF7;
  --v-bg-2:#DDE3F2;
  --v-surface:#FFFFFF;
  --v-ink:#1B1F45;
  --v-muted:#5A628C;
  --v-accent:#0743C9;
  --v-red:#EA1701;
  --v-line:rgba(42,42,112,.15);
  --v-line-soft:rgba(42,42,112,.08);
  --v-shadow:0 1px 2px rgba(16,22,60,.06),0 18px 44px rgba(16,22,60,.14);
  --v-bar:rgba(233,237,247,.86);
  --v-logo-colour:1; --v-logo-white:0;
  --v-pad:clamp(12px,3vw,44px);
}
@media (prefers-color-scheme:dark){
  :root:not([data-theme="light"]){
    --v-bg:#070A1E;
    --v-bg-2:#0C1130;
    --v-surface:#101534;
    --v-ink:#E9EDFA;
    --v-muted:#98A0C4;
    --v-accent:#7FA8FF;
    --v-red:#FF5A47;
    --v-line:rgba(255,255,255,.14);
    --v-line-soft:rgba(255,255,255,.07);
    --v-shadow:0 1px 2px rgba(0,0,0,.4),0 20px 50px rgba(0,0,0,.55);
    --v-bar:rgba(7,10,30,.84);
    --v-logo-colour:0; --v-logo-white:1;
  }
}
:root[data-theme="dark"]{
  --v-bg:#070A1E;
  --v-bg-2:#0C1130;
  --v-surface:#101534;
  --v-ink:#E9EDFA;
  --v-muted:#98A0C4;
  --v-accent:#7FA8FF;
  --v-red:#FF5A47;
  --v-line:rgba(255,255,255,.14);
  --v-line-soft:rgba(255,255,255,.07);
  --v-shadow:0 1px 2px rgba(0,0,0,.4),0 20px 50px rgba(0,0,0,.55);
  --v-bar:rgba(7,10,30,.84);
  --v-logo-colour:0; --v-logo-white:1;
}

body{
  margin:0;
  background:var(--v-bg);
  color:var(--v-ink);
  font-family:'ALTIGO Sans','Plus Jakarta Sans',system-ui,-apple-system,'Segoe UI',sans-serif;
  font-weight:500;
  -webkit-font-smoothing:antialiased;
}

/* ---------- sticky bar ---------- */
.v-bar{
  position:sticky;top:0;z-index:50;
  display:flex;align-items:center;gap:18px;
  padding:11px var(--v-pad);
  background:var(--v-bar);
  -webkit-backdrop-filter:saturate(1.6) blur(14px);
  backdrop-filter:saturate(1.6) blur(14px);
  border-bottom:1px solid var(--v-line);
}
.v-logo{position:relative;height:20px;width:94px;flex:none}
.v-logo img{position:absolute;inset:0;height:100%;width:auto;display:block}
.v-logo .lc{opacity:var(--v-logo-colour)}
.v-logo .lw{opacity:var(--v-logo-white)}

.v-bar-title{
  font-size:11px;font-weight:700;letter-spacing:.17em;text-transform:uppercase;
  color:var(--v-muted);white-space:nowrap;flex:none;
  padding-left:18px;border-left:1px solid var(--v-line);
}
.v-bar-title b{color:var(--v-ink);font-weight:700}
.v-spacer{flex:1}

.v-jump{
  font:inherit;font-size:12.5px;font-weight:600;
  color:var(--v-ink);background:var(--v-surface);
  border:1px solid var(--v-line);border-radius:7px;
  padding:7px 10px;
  flex:0 1 280px;min-width:0;   /* a select's intrinsic width is its longest
                                   option — without min-width:0 it refuses to
                                   shrink and pushes the page sideways */
  cursor:pointer;
}
.v-count{
  font-size:12.5px;font-weight:700;color:var(--v-muted);
  font-variant-numeric:tabular-nums;white-space:nowrap;
  min-width:62px;text-align:right;
}
.v-count b{color:var(--v-ink)}
.v-nav{display:flex;gap:6px}
.v-btn{
  width:32px;height:32px;display:grid;place-items:center;
  background:var(--v-surface);color:var(--v-ink);
  border:1px solid var(--v-line);border-radius:7px;
  cursor:pointer;padding:0;
}
.v-btn:hover{border-color:var(--v-accent);color:var(--v-accent)}
.v-btn:disabled{opacity:.36;cursor:default}
.v-btn:disabled:hover{border-color:var(--v-line);color:var(--v-ink)}
.v-btn svg{width:15px;height:15px;stroke:currentColor;fill:none;stroke-width:2;
  stroke-linecap:round;stroke-linejoin:round}
.v-btn:focus-visible,.v-jump:focus-visible{outline:2px solid var(--v-accent);outline-offset:2px}

/* ---------- document ---------- */
.v-doc{
  padding:0 var(--v-pad) 64px;
  display:flex;flex-direction:column;gap:clamp(26px,4vw,52px);
  scroll-behavior:smooth;
}
@media (prefers-reduced-motion:reduce){ .v-doc{scroll-behavior:auto} html{scroll-behavior:auto} }

.v-slide{scroll-margin-top:72px}
.v-slide-bar{
  display:flex;align-items:baseline;gap:12px;
  padding:22px 2px 9px;
}
.v-folio{
  font-size:10.5px;font-weight:800;letter-spacing:.14em;
  color:var(--v-red);font-variant-numeric:tabular-nums;
}
.v-slide-name{
  font-size:10.5px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;
  color:var(--v-muted);
}
.v-stage{
  position:relative;width:100%;aspect-ratio:1440/810;
  overflow:hidden;background:var(--v-surface);
  border-radius:4px;box-shadow:var(--v-shadow);
}
.v-fit{
  position:absolute;top:0;left:0;
  width:1440px;height:810px;
  transform-origin:0 0;transform:scale(var(--s,.5));
}
.v-fit .page{box-shadow:none;border-radius:0}

/* ---------- foot ---------- */
.v-foot{
  padding:26px var(--v-pad) 46px;
  border-top:1px solid var(--v-line-soft);
  display:flex;flex-wrap:wrap;gap:8px 22px;align-items:baseline;
  font-size:11px;font-weight:600;letter-spacing:.03em;color:var(--v-muted);
}
.v-foot b{color:var(--v-ink);font-weight:700;letter-spacing:.14em;text-transform:uppercase;font-size:10px}

/* ---------- narrow ---------- */
@media (max-width:860px){
  .v-bar{gap:12px}
  .v-bar-title{display:none}
}
@media (max-width:560px){
  .v-jump{display:none}
  .v-slide-name{
    overflow:hidden;text-overflow:ellipsis;white-space:nowrap;
  }
  .v-slide-bar{gap:9px;padding-top:16px}
}
"""

BAR = """
<header class="v-bar">
  <span class="v-logo">
    <img class="lc" src="{lc}" alt="ALTIGO">
    <img class="lw" src="{lw}" alt="" aria-hidden="true">
  </span>
  <span class="v-bar-title"><b>Company Profile</b> &middot; Edition 2026</span>
  <span class="v-spacer"></span>
  <select class="v-jump" id="vJump" aria-label="Jump to page"></select>
  <span class="v-count" id="vCount"><b>01</b> / 41</span>
  <span class="v-nav">
    <button class="v-btn" id="vPrev" aria-label="Previous page">
      <svg viewBox="0 0 24 24"><path d="M15 5l-7 7 7 7"/></svg></button>
    <button class="v-btn" id="vNext" aria-label="Next page">
      <svg viewBox="0 0 24 24"><path d="M9 5l7 7-7 7"/></svg></button>
  </span>
</header>
""".format(lc=P["logo_colour"], lw=P["logo_white"])

SCRIPT = """
<script>
(function(){
  var slides = Array.prototype.slice.call(document.querySelectorAll('.v-slide'));
  var stage  = document.querySelector('.v-stage');
  var root   = document.documentElement;

  function fit(){
    var w = stage ? stage.clientWidth : 0;
    if(w > 0) root.style.setProperty('--s', w / 1440);
  }
  fit();
  addEventListener('resize', fit);
  if(window.ResizeObserver && stage) new ResizeObserver(fit).observe(stage);
  if(document.fonts && document.fonts.ready) document.fonts.ready.then(fit);

  var jump  = document.getElementById('vJump');
  var count = document.getElementById('vCount');
  var prev  = document.getElementById('vPrev');
  var next  = document.getElementById('vNext');
  var cur   = 0;

  slides.forEach(function(s, i){
    var name = (s.getAttribute('aria-label') || '').replace(/^Page \\d+: /, '');
    var o = document.createElement('option');
    o.value = i;
    o.textContent = ('0' + (i + 1)).slice(-2) + '  \\u00b7  ' + name;
    jump.appendChild(o);
  });

  function mark(i){
    if(i === cur) return;
    cur = i;
    count.innerHTML = '<b>' + ('0' + (i + 1)).slice(-2) + '</b> / 41';
    jump.value = i;
    prev.disabled = i === 0;
    next.disabled = i === slides.length - 1;
  }
  mark(0); prev.disabled = true;

  function go(i){
    i = Math.max(0, Math.min(slides.length - 1, i));
    slides[i].scrollIntoView({block:'start'});
  }
  prev.addEventListener('click', function(){ go(cur - 1); });
  next.addEventListener('click', function(){ go(cur + 1); });
  jump.addEventListener('change', function(){ go(+jump.value); });

  addEventListener('keydown', function(e){
    if(e.target && /^(INPUT|SELECT|TEXTAREA)$/.test(e.target.tagName)) return;
    if(e.key === 'ArrowRight' || e.key === 'PageDown'){ e.preventDefault(); go(cur + 1); }
    else if(e.key === 'ArrowLeft' || e.key === 'PageUp'){ e.preventDefault(); go(cur - 1); }
    else if(e.key === 'Home'){ e.preventDefault(); go(0); }
    else if(e.key === 'End'){ e.preventDefault(); go(slides.length - 1); }
  });

  if(window.IntersectionObserver){
    var io = new IntersectionObserver(function(entries){
      entries.forEach(function(en){
        if(en.isIntersecting) mark(slides.indexOf(en.target));
      });
    }, {rootMargin:'-45% 0px -45% 0px', threshold:0});
    slides.forEach(function(s){ io.observe(s); });
  }
})();
</script>
"""

FOOT = """
<footer class="v-foot">
  <b>ALTIGO Elevator Sdn Bhd</b>
  <span>562238-H &middot; DOSH Certified &middot; Penang, Kuala Lumpur, Negeri Sembilan</span>
  <span>&copy; 2026 ALTIGO Elevator Sdn Bhd &middot; All rights reserved &middot; Confidential document prepared for authorised client and partner use.</span>
</footer>
"""

out = []
out.append("<title>ALTIGO Company Profile 2026</title>")
out.append("<style>\n" + P["face"] + P["style"] + CHROME + "\n</style>")
out.append(P["sprite"])
out.append(BAR)
out.append('<main class="v-doc">')
out.append(P["shell"])
out.append("</main>")
out.append(FOOT)
out.append(SCRIPT)

path = os.path.join(R, "altigo-profile-viewer.html")
open(path, "w", encoding="utf-8").write("\n".join(out))
print("wrote", path, os.path.getsize(path)//1024, "KB")
