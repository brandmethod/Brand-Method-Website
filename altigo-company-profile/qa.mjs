import { chromium } from 'playwright-core';
import path from 'path'; import { fileURLToPath } from 'url';
const dir = path.dirname(fileURLToPath(import.meta.url));
const b = await chromium.launch({ executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome', args:['--no-sandbox'] });
const pg = await b.newPage({ viewport:{width:1440,height:810} });
await pg.goto('file://'+path.join(dir,'index.html'), { waitUntil:'load' });
await pg.evaluate(()=>document.fonts.ready); await pg.waitForTimeout(500);
const bad = await pg.evaluate(() => {
  const out=[];
  document.querySelectorAll('section.page').forEach((s,i)=>{
    const pr=s.getBoundingClientRect();
    // overflow beyond the page box
    s.querySelectorAll('*').forEach(el=>{
      const r=el.getBoundingClientRect();
      if(r.width===0||r.height===0) return;
      // full-bleed art is meant to run past the trim; everything else is a bug
      if(el.closest('[data-bleed]')) return;
      const over=[];
      if(r.bottom > pr.bottom+0.5) over.push('bottom+'+Math.round(r.bottom-pr.bottom));
      if(r.top    < pr.top-0.5)    over.push('top-'+Math.round(pr.top-r.top));
      if(r.right  > pr.right+0.5)  over.push('right+'+Math.round(r.right-pr.right));
      if(r.left   < pr.left-0.5)   over.push('left-'+Math.round(pr.left-r.left));
      if(over.length) out.push({page:i+1, tag:el.tagName.toLowerCase(),
        cls:(el.className&&el.className.toString().slice(0,34))||'',
        txt:(el.textContent||'').trim().slice(0,42), over:over.join(',')});
    });
    // scroll overflow inside clipped containers
    s.querySelectorAll('.wrap,.band,.card,.tl-card,.quote,.callout').forEach(el=>{
      if(el.scrollHeight > el.clientHeight+1)
        out.push({page:i+1,tag:'CLIP',cls:(el.className||'').toString().slice(0,34),
          txt:(el.textContent||'').trim().slice(0,42), over:'scrollH '+el.scrollHeight+'>'+el.clientHeight});
    });
  });
  return out;
});
const seen=new Set(); const uniq=bad.filter(x=>{const k=x.page+x.cls+x.over+x.txt; if(seen.has(k))return false; seen.add(k); return true;});
console.log('issues:', uniq.length);
uniq.slice(0,60).forEach(x=>console.log(`p${String(x.page).padStart(2,'0')} ${x.over.padEnd(18)} ${x.tag.padEnd(6)} ${x.cls.padEnd(30)} "${x.txt}"`));
await b.close();
