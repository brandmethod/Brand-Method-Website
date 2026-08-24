// Renders index.html -> ALTIGO_Company_Profile_2026.pdf  (1440 x 810 slides)
import { chromium } from 'playwright-core';
import { fileURLToPath } from 'url';
import path from 'path';

const dir  = path.dirname(fileURLToPath(import.meta.url));
const url  = 'file://' + path.join(dir, 'index.html');
const out  = path.join(dir, 'ALTIGO_Company_Profile_2026.pdf');
const png  = process.argv.includes('--png');

const browser = await chromium.launch({
  executablePath: process.env.CHROME_PATH || '/opt/pw-browsers/chromium-1194/chrome-linux/chrome',
  args: ['--no-sandbox', '--font-render-hinting=none', '--disable-lcd-text']
});
const page = await browser.newPage({ viewport: { width: 1440, height: 810 }, deviceScaleFactor: 2 });
await page.goto(url, { waitUntil: 'load' });
await page.evaluate(() => document.fonts.ready);
await page.waitForTimeout(600);

const n = await page.locator('section.page').count();
console.log(`slides: ${n}`);

if (png) {
  const only = process.argv.find(a => a.startsWith('--only='));
  const list = only ? only.split('=')[1].split(',').map(Number) : [...Array(n)].map((_, i) => i + 1);
  for (const i of list) {
    await page.locator('section.page').nth(i - 1)
      .screenshot({ path: path.join(dir, `out/p${String(i).padStart(2, '0')}.png`) });
  }
  console.log('png written:', list.length);
} else {
  await page.pdf({ path: out, width: '1440px', height: '810px',
                   printBackground: true, pageRanges: `1-${n}` });
  // normalise page boxes to 1440 x 810 pt (same trim size as the prior edition)
  const { execFileSync } = await import('child_process');
  execFileSync('python3', [path.join(dir, 'rescale.py'), out], { stdio: 'inherit' });
  console.log('pdf ->', out);
}
await browser.close();
