CHROME_CSS = r"""
/* ------------------------------------------------- universal deck nav */
.nav{position:fixed;left:50%;bottom:20px;transform:translateX(-50%);z-index:900;display:flex;
  align-items:center;height:64px;padding:0 10px;border-radius:99px;background:var(--ink);
  border:1px solid rgba(255,255,255,.16);box-shadow:0 16px 44px rgba(0,0,0,.45);
  font-family:var(--fm);max-width:calc(100vw - 32px)}
.nav.hide{opacity:0;pointer-events:none}
.nav button{border:none;background:transparent;color:rgba(255,255,255,.74);cursor:pointer;
  font-family:var(--fm);font-size:11px;letter-spacing:.08em;display:flex;align-items:center;
  justify-content:center;border-radius:99px;transition:background .14s,color .14s}
.nav button:hover{background:rgba(255,255,255,.13);color:#fff}
.nav button:focus-visible{outline:2px solid var(--gold);outline-offset:2px}
.nav button:disabled{opacity:.3;cursor:default;background:transparent}
.nav .arr{width:34px;height:34px;font-size:15px;flex:none}
.nsep{width:1px;height:26px;background:rgba(255,255,255,.16);margin:0 10px;flex:none}

.dots{display:flex;align-items:center;gap:7px;overflow-x:auto;scrollbar-width:none;
  max-width:250px;padding:6px 2px;flex:none}
.dots::-webkit-scrollbar{display:none}
.nav .dot-i{width:6px;height:6px;border-radius:99px;background:rgba(255,255,255,.34);flex:none;
  cursor:pointer;transition:transform .14s,background .14s;border:none;padding:0}
.nav .dot-i:hover{transform:scale(1.5);background:rgba(255,255,255,.72)}
.nav .dot-i.on{width:24px;height:15px;border-radius:99px;background:var(--gold);color:var(--ink);
  font-family:var(--fm);font-size:9px;font-weight:700;display:flex;align-items:center;
  justify-content:center;transform:none}
.nav .dot-i.on:hover{transform:none;background:var(--gold)}

.nname{font-size:11.5px;letter-spacing:.04em;color:#fff;white-space:nowrap;overflow:hidden;
  text-overflow:ellipsis;max-width:210px;flex:none;text-transform:none}
.ncount{font-size:11.5px;letter-spacing:.06em;color:rgba(255,255,255,.64);white-space:nowrap;flex:none}
.ncount b{color:#fff;font-weight:700}

.zm{display:flex;align-items:center;gap:2px;flex:none}
.zm button{width:28px;height:28px;font-size:15px}
.zm #zpct{min-width:52px;height:28px;font-size:10.5px;letter-spacing:.04em;color:#fff}
.zm #zfit{width:auto;padding:0 12px;height:28px;font-size:10px;letter-spacing:.1em;
  border:1px solid rgba(255,255,255,.22)}
.nav.zoomed .zm #zpct{color:var(--gold)}

.nico{width:38px;height:38px;flex:none}
.nico svg{width:18px;height:18px;display:block}

.hint{position:fixed;left:22px;bottom:38px;z-index:880;font-family:var(--fm);font-size:9.5px;
  letter-spacing:.12em;text-transform:uppercase;color:rgba(255,255,255,.36);pointer-events:none;
  transition:opacity .4s;max-width:270px;line-height:1.7}
.hint.hide{opacity:0}
html.thumbonly .nav,html.thumbonly .hint{display:none!important}
html.thumbonly #stage{bottom:0}

.sheetlist{position:fixed;inset:0;z-index:940;background:rgba(22,17,13,.985);opacity:0;pointer-events:none;
  transition:opacity .26s;display:flex;flex-direction:column}
.sheetlist.open{opacity:1;pointer-events:auto}
.slbar{display:flex;align-items:center;gap:16px;padding:20px 34px;border-bottom:1px solid rgba(255,255,255,.13)}
.slbar h4{font-family:var(--fd);font-weight:800;font-stretch:112%;font-size:19px;color:#fff;margin:0}
.slbar .sub{font-family:var(--fm);font-size:11px;letter-spacing:.14em;color:rgba(255,255,255,.46);flex:1;text-transform:uppercase}
.slbar .x{font-family:var(--fm);font-size:11px;color:var(--ink);background:var(--gold);padding:8px 16px;
  border-radius:99px;border:none;cursor:pointer;font-weight:700}
.slscroll{flex:1;overflow-y:auto;padding:24px 34px 44px}
.slgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:22px;align-content:start}
.slgroup{grid-column:1/-1;font-family:var(--fm);font-size:10px;letter-spacing:.2em;text-transform:uppercase;
  color:var(--gold);padding:14px 0 2px;border-top:1px solid rgba(255,255,255,.13)}
.slgroup:first-child{border-top:none;padding-top:0}
.slth{cursor:pointer}
.slfr{position:relative;width:100%;height:0;padding-top:56.25%;overflow:hidden;
  border:1.5px solid rgba(255,255,255,.15);background:#fff;transition:border-color .16s}
.slth:hover .slfr{border-color:var(--gold)}
.slfr>.mini{position:absolute;left:0;top:0;width:1920px;height:1080px;transform-origin:0 0}
.slcap{margin-top:9px;font-family:var(--fm);font-size:9.5px;letter-spacing:.1em;color:rgba(255,255,255,.52);text-transform:uppercase}
.slcap b{color:var(--gold);font-weight:700}

.pm{position:fixed;inset:0;z-index:960;background:rgba(22,17,13,.88);backdrop-filter:blur(6px);
  display:flex;align-items:center;justify-content:center;opacity:0;pointer-events:none;transition:opacity .24s}
.pm.open{opacity:1;pointer-events:auto}
.pmbox{width:560px;background:#231C16;border:1px solid rgba(255,255,255,.15);padding:32px}
.pmbox h4{font-family:var(--fd);font-weight:800;font-stretch:112%;font-size:24px;color:#fff;margin:0 0 8px}
.pmbox p{font-size:14px;line-height:22px;color:rgba(255,255,255,.66);margin:0 0 22px}
.pmbox p b{color:#fff}
.pmlab{font-family:var(--fm);font-size:9.5px;letter-spacing:.2em;text-transform:uppercase;color:var(--gold);margin:0 0 10px}
.opts{display:grid;gap:8px;margin-bottom:20px}
.opt{display:flex;align-items:baseline;gap:12px;padding:11px 14px;cursor:pointer;
  border:1px solid rgba(255,255,255,.15);color:rgba(255,255,255,.84);font-size:13.5px}
.opt:hover{background:rgba(255,255,255,.08)}
.opt.sel{border-color:var(--gold);background:rgba(240,168,30,.18);color:#fff}
.opt span{font-family:var(--fm);font-size:10px;color:rgba(255,255,255,.48);margin-left:auto}
.pmact{display:flex;gap:10px;justify-content:flex-end}
.pmact button{font-family:var(--fm);font-size:11px;letter-spacing:.12em;text-transform:uppercase;
  padding:11px 20px;border:1px solid rgba(255,255,255,.2);background:transparent;color:rgba(255,255,255,.8);cursor:pointer}
.pmact button.go{background:var(--gold);border-color:var(--gold);color:var(--ink);font-weight:700}

@media (prefers-reduced-motion:reduce){.rv{animation:none!important;opacity:1!important;transform:none!important}
  .slide{transition:none!important}}

@media print{
  html,body{background:#fff!important;overflow:visible!important;height:auto!important}
  .nav,.sheetlist,.pm,.hint,#stage{display:none!important}
  #printroot{display:block!important}
  .sheet{width:var(--pw);height:var(--ph);page-break-after:always;break-after:page;overflow:hidden;
    display:flex;align-items:center;justify-content:center;position:relative}
  .sheet:last-child{page-break-after:auto;break-after:auto}
  .sheet>.pg{transform:scale(var(--ps));transform-origin:center center;flex:none}
  .rv{opacity:1!important;transform:none!important;animation:none!important}
  *{-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important}
}
#printroot{display:none}
"""
