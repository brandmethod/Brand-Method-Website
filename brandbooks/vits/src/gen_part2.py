CSS = r"""
*,*::before,*::after{box-sizing:border-box}
html,body{margin:0;padding:0}
:root{
  --red:#EC1F28; --redD:#C4141C; --gold:#F0A81E; --goldD:#B87C08;
  --ink:#191410; --broth:#8A7360; --steam:#FAF4E9; --paper:#fff;
  --ink72:rgba(25,20,16,.82); --ink54:rgba(25,20,16,.66); --ink14:rgba(25,20,16,.18);
  --ink08:rgba(25,20,16,.09);
  --w72:rgba(255,255,255,.84); --w52:rgba(255,255,255,.68); --w18:rgba(255,255,255,.24);
  --w10:rgba(255,255,255,.11);
  --fd:'Archivo',Helvetica Neue,Arial,sans-serif;      /* display and wordmark */
  --ft:'Figtree',Helvetica Neue,Arial,sans-serif;      /* text */
  --fm:'JetBrains Mono',ui-monospace,Menlo,monospace;  /* data and labels */
  --fa:Arial,Helvetica,sans-serif;                     /* documents and email */
  --fsc:'Noto Sans SC','Figtree',sans-serif;
  --far:'Noto Naskh Arabic',serif;
  --pw:1920px; --ph:1080px; --ps:1; --navh:104px;
  --ease:cubic-bezier(.22,1,.36,1);
}
body{background:#16110D;font-family:var(--ft);font-weight:400;-webkit-font-smoothing:antialiased;overflow:hidden}

#stage{position:fixed;left:0;right:0;top:0;bottom:var(--navh);overflow:hidden}
#scaler{position:absolute;left:50%;top:50%;width:1920px;height:1080px;
  transform-origin:center center;transform:translate(-50%,-50%) scale(1)}
.slide{position:absolute;inset:0;width:1920px;height:1080px;opacity:0;visibility:hidden;
  pointer-events:none;transition:opacity .4s var(--ease),transform .5s var(--ease)}
.slide.on{opacity:1;visibility:visible;pointer-events:auto;transform:none;z-index:2}
.slide.pre{transform:translateX(-30px)}
.slide.post{transform:translateX(30px)}

/* ------------------------------------------------------------------ page */
.pg{position:relative;width:1920px;height:1080px;overflow:hidden;background:var(--paper);color:var(--ink)}
.pg.steam{background:var(--steam)}
.pg.ink{background:var(--ink);color:#fff}
.pg.red{background:var(--red);color:#fff}

.cv{position:absolute;left:0;right:0;top:0;bottom:0;padding:64px 120px 96px;z-index:2;
  display:flex;flex-direction:column}
.top{display:flex;align-items:baseline;justify-content:space-between;font-family:var(--fm);
  font-size:14.5px;font-weight:600;letter-spacing:.18em;text-transform:uppercase;color:var(--ink54)}
.top b{color:var(--redD);font-weight:700}
.pg.ink .top{color:var(--w52)} .pg.ink .top b{color:var(--gold)}
.pg.red .top{color:rgba(255,255,255,.66)} .pg.red .top b{color:#fff}
.hair{height:1px;background:var(--ink14);margin-top:16px}
.pg.ink .hair{background:var(--w18)} .pg.red .hair{background:rgba(255,255,255,.28)}

/* Title sits tight under the topbar rule. Description aligns to its cap height,
   not its baseline, so the 12px pad optically levels the two. */
.head{padding-top:30px}
h1.t{font-family:var(--fd);font-weight:800;font-stretch:112%;font-size:60px;line-height:1.02;
  letter-spacing:-.018em;text-wrap:balance;margin:0}
h1.t.sm{font-size:49px}
.lead{font-size:23px;line-height:36px;color:var(--ink72);max-width:760px;text-wrap:balance;margin-top:22px}
.pg.ink .lead{color:var(--w72)} .pg.red .lead{color:rgba(255,255,255,.84)}
.head.split{display:flex;align-items:flex-start;justify-content:space-between;gap:70px}
.head.split .lead{margin-top:0;padding-top:12px;max-width:620px;text-align:right;font-size:20px;
  line-height:31px;text-wrap:balance}

.body{flex:1;min-height:0;padding-top:44px;display:flex;flex-direction:column}
.body>*{min-height:0}
.body>*:only-child{flex:1 1 auto}

.ftr{position:absolute;left:120px;right:120px;bottom:40px;display:flex;align-items:center;
  justify-content:space-between;z-index:4;font-family:var(--fm);font-size:12.5px;font-weight:600;
  letter-spacing:.14em;text-transform:uppercase;color:var(--ink54)}
.pg.ink .ftr{color:var(--w52)} .pg.red .ftr{color:rgba(255,255,255,.66)}
.fl{display:flex;align-items:center;gap:12px}
.fname{font-family:var(--fd);font-weight:800;font-stretch:115%;font-size:15px;letter-spacing:.01em;color:var(--ink)}
.pg.ink .fname{color:#fff} .pg.red .fname{color:#fff}
.fc{font-size:12.5px;letter-spacing:.05em;text-transform:none;font-family:var(--ft);opacity:.78}
.fr{display:flex;align-items:center;gap:14px}
.fpg{font-family:var(--fd);font-weight:800;font-size:16.5px;letter-spacing:0;color:var(--ink)}
.pg.ink .fpg{color:var(--gold)} .pg.red .fpg{color:#fff}

/* ------------------------------------------------------------ primitives */
.mono{font-family:var(--fm);font-size:14.5px;font-weight:600;letter-spacing:.15em;text-transform:uppercase}
.mono.s{font-size:13px;letter-spacing:.15em}
.dim{color:var(--ink54)} .pg.ink .dim{color:var(--w52)} .pg.red .dim{color:rgba(255,255,255,.68)}
.acc{color:var(--redD)} .pg.ink .acc{color:var(--gold)} .pg.red .acc{color:#fff}
.grid{display:grid;gap:24px}
.card{border:1px solid var(--ink14);padding:26px 28px;background:var(--paper);position:relative}
.pg.ink .card{border-color:var(--w18);background:rgba(255,255,255,.05)}
.pg.steam .card{background:var(--paper)}
.pg.red .card{border-color:rgba(255,255,255,.3);background:rgba(255,255,255,.10)}
.card h3{font-family:var(--fd);font-weight:800;font-stretch:105%;font-size:22.5px;line-height:1.24;
  letter-spacing:-.012em;text-wrap:balance;margin:0}
.card p{font-size:18px;line-height:30px;color:var(--ink72);text-wrap:balance;margin:11px 0 0}
.pg.ink .card p{color:var(--w72)} .pg.red .card p{color:rgba(255,255,255,.84)}
.chip{display:inline-flex;align-items:center;gap:7px;font-family:var(--fm);font-size:12.5px;font-weight:600;
  letter-spacing:.14em;text-transform:uppercase;border:1px solid var(--ink14);padding:6px 12px;color:var(--ink54)}
.pg.ink .chip{border-color:var(--w18);color:var(--w72)}
.chip.on{border-color:var(--red);color:var(--redD);background:rgba(236,31,40,.10)}
.pg.ink .chip.on{color:var(--gold);border-color:var(--gold);background:rgba(240,168,30,.14)}
.p{font-size:19.5px;line-height:31px;color:var(--ink72);text-wrap:balance}
.pg.ink .p{color:var(--w72)} .pg.red .p{color:rgba(255,255,255,.86)}
.p+.p{margin-top:14px}
.num{font-family:var(--fd);font-weight:800;font-size:16.5px;letter-spacing:.02em;color:var(--redD)}
.pg.ink .num{color:var(--gold)}

table.tb{width:100%;border-collapse:collapse}
table.tb th{font-family:var(--fm);font-size:13px;font-weight:600;letter-spacing:.16em;text-transform:uppercase;
  color:var(--redD);text-align:left;padding:0 14px 12px 0;border-bottom:1px solid var(--ink14);white-space:nowrap}
table.tb td{padding:16px 14px 16px 0;border-bottom:1px solid var(--ink08);font-size:18px;
  line-height:28px;color:var(--ink72);vertical-align:middle}
table.tb td.k{color:var(--ink);font-weight:800;font-family:var(--fd);font-stretch:104%;white-space:nowrap}
.pg.ink table.tb th{color:var(--gold);border-bottom-color:var(--w18)}
.pg.ink table.tb td{color:var(--w72);border-bottom-color:var(--w10)}
.pg.ink table.tb td.k{color:#fff}
.spec{width:100%;border-collapse:collapse}
.spec tr{border-bottom:1px solid var(--ink08)}
.pg.ink .spec tr{border-bottom-color:var(--w10)}
.spec td{padding:12px 0;font-family:var(--fm);font-size:13.5px;font-weight:600;letter-spacing:.11em;
  text-transform:uppercase;color:var(--ink54);vertical-align:top}
.pg.ink .spec td{color:var(--w52)}
.spec td+td{text-align:right;color:var(--ink);font-weight:700;letter-spacing:.01em;
  text-transform:none;font-family:var(--ft);font-size:18.5px;line-height:26px}
.pg.ink .spec td+td{color:#fff}

/* Placeholder zone. This edition is a wireframe: every box marked this way is
   art direction pending, not a final asset. */
.slot{position:relative;border:1px dashed rgba(236,31,40,.55);background:rgba(236,31,40,.06);
  display:flex;flex-direction:column;align-items:center;justify-content:center;gap:6px;text-align:center}
.slot .st{font-family:var(--fd);font-weight:800;font-size:17.5px;color:var(--redD)}
.slot .sm{font-family:var(--fm);font-size:12.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--ink54)}
.pg.ink .slot{border-color:rgba(240,168,30,.5);background:rgba(240,168,30,.07)}
.pg.ink .slot .st{color:var(--gold)} .pg.ink .slot .sm{color:var(--w52)}

/* ------------------------------------------------------------- divider */
.dv-mark{position:absolute;right:-130px;top:50%;transform:translateY(-50%);opacity:.10;z-index:1}
.dv-wrap{position:absolute;left:120px;top:50%;transform:translateY(-50%);max-width:820px;z-index:3}
.dv-n{font-family:var(--fd);font-weight:800;font-stretch:120%;font-size:164px;line-height:.86;
  letter-spacing:-.035em;color:var(--gold)}
.dv-t{font-family:var(--fd);font-weight:800;font-stretch:112%;font-size:76px;line-height:1;
  letter-spacing:-.024em;color:#fff;text-wrap:balance;margin-top:8px}
.dv-b{font-size:21.5px;line-height:34px;color:var(--w72);text-wrap:balance;margin-top:20px;max-width:600px}
.dv-idx{position:absolute;right:120px;top:50%;transform:translateY(-50%);width:470px;z-index:3}
.dv-row{display:flex;align-items:baseline;gap:22px;padding:12px 0;border-top:1px solid var(--w10)}
.dv-row .n{font-family:var(--fm);font-size:13.5px;letter-spacing:.14em;color:var(--gold);width:44px;flex:none}
.dv-row .s{font-size:19px;color:rgba(255,255,255,.92)}

.rv{opacity:0;transform:translateY(14px)}
.slide.on .rv{animation:rvin .58s var(--ease) forwards;animation-delay:var(--d,0ms)}
@keyframes rvin{to{opacity:1;transform:none}}
html.static .rv{opacity:1;transform:none;animation:none}
"""
