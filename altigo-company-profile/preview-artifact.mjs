// Mimics the Artifact host: wraps the body-level HTML in a doctype/head/body
// skeleton with a minimal reset, then screenshots light + dark.
import { chromium } from 'playwright-core';
import fs from 'fs'; import path from 'path'; import { fileURLToPath } from 'url';
const dir = path.dirname(fileURLToPath(import.meta.url));
const inner = fs.readFileSync(path.join(dir,'altigo-profile-viewer.html'),'utf8');
const wrapped = `<!doctype html><html><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<style>*,*::before,*::after{box-sizing:border-box}body{margin:0}img,svg{max-width:100%}</style>
</head><body>${inner}</body></html>`;
const tmp = path.join(dir,'.preview.html');
fs.writeFileSync(tmp, wrapped);

const b = await chromium.launch({ executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome', args:['--no-sandbox'] });
for (const [scheme, w, h, tag] of [['light',1280,900,'light'],['dark',1280,900,'dark'],['light',420,860,'mobile']]) {
  const pg = await b.newPage({ viewport:{width:w,height:h}, colorScheme:scheme, deviceScaleFactor:1.5 });
  await pg.goto('file://'+tmp, { waitUntil:'load' });
  await pg.evaluate(()=>document.fonts.ready); await pg.waitForTimeout(700);
  await pg.screenshot({ path: path.join(dir,`prev-${tag}-top.png`) });
  // jump to an interior slide
  await pg.evaluate(()=>document.getElementById('p14').scrollIntoView({block:'start',behavior:'instant'}));
  await pg.waitForTimeout(400);
  await pg.screenshot({ path: path.join(dir,`prev-${tag}-mid.png`) });
  // report any horizontal overflow
  const ov = await pg.evaluate(()=>({docW:document.documentElement.scrollWidth, winW:innerWidth,
     scale:getComputedStyle(document.documentElement).getPropertyValue('--s').trim(),
     count:document.querySelectorAll('.v-slide').length}));
  console.log(tag, JSON.stringify(ov));
  await pg.close();
}
await b.close();
