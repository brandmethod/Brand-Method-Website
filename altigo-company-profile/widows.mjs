// Reports body-copy blocks whose final line holds 3 words or fewer — the
// stranded-word case that makes a paragraph look broken.
import { chromium } from 'playwright-core';
import path from 'path'; import { fileURLToPath } from 'url';
const dir = path.dirname(fileURLToPath(import.meta.url));
const b = await chromium.launch({ executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome', args:['--no-sandbox'] });
const pg = await b.newPage({ viewport:{width:1440,height:810} });
await pg.goto('file://'+path.join(dir,'index.html'), { waitUntil:'load' });
await pg.evaluate(()=>document.fonts.ready); await pg.waitForTimeout(500);

const bad = await pg.evaluate(() => {
  const SEL = '.deck, .p, .p-sm, .ch-deck, .quote .q, .toc-s';
  const out = [];
  document.querySelectorAll('section.page').forEach((s, pi) => {
    s.querySelectorAll(SEL).forEach(el => {
      const tn = [...el.childNodes].filter(n => n.nodeType === 3 && n.textContent.trim());
      if (!tn.length) return;
      const r = document.createRange();
      r.selectNodeContents(el);
      const lines = [...r.getClientRects()].filter(x => x.width > 1);
      if (lines.length < 2) return;                       // single line: not a widow
      const last = lines[lines.length - 1];
      // count words whose box sits on that final line
      let words = 0;
      tn.forEach(node => {
        const t = node.textContent;
        let i = 0;
        t.split(/(\s+)/).forEach(tok => {
          if (tok.trim()) {
            const wr = document.createRange();
            wr.setStart(node, i); wr.setEnd(node, i + tok.length);
            const br = wr.getBoundingClientRect();
            if (br.width && Math.abs(br.top - last.top) < 3) words++;
          }
          i += tok.length;
        });
      });
      if (words > 0 && words <= 3)
        out.push({ page: pi + 1, words, text: el.textContent.trim().slice(-52) });
    });
  });
  return out;
});
console.log('stranded last lines (<=3 words):', bad.length);
bad.forEach(x => console.log(`  p${String(x.page).padStart(2,'0')}  ${x.words}w  …${x.text}`));
await b.close();
