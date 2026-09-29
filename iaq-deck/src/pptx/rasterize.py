"""Every inline SVG in the deck becomes a PNG at four times its drawn size, so
the icons and flags stay sharp when PowerPoint scales the slide up."""
import asyncio, json, hashlib, io, os, re
from playwright.async_api import async_playwright

SCALE = 4
OUT = 'svg'

async def main():
    data = json.load(io.open('slides.json', encoding='utf-8'))
    os.makedirs(OUT, exist_ok=True)
    jobs = {}
    for s in data:
        for it in s['items']:
            if it['k'] != 'svg':
                continue
            key = hashlib.md5((it['html'] + it['color'] +
                               f"{it['w']:.1f}x{it['h']:.1f}").encode()).hexdigest()[:16]
            it['png'] = f'{OUT}/{key}.png'
            jobs[key] = it
    async with async_playwright() as p:
        b = await p.chromium.launch(
            executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome',
            args=['--no-sandbox'])
        pg = await b.new_page(viewport={'width': 600, 'height': 600},
                              device_scale_factor=SCALE)
        for key, it in jobs.items():
            w, h = max(it['w'], 1), max(it['h'], 1)
            # size the svg with CSS, the way the deck's own stylesheet does: editing
            # the markup would hit the first rect's width, not the svg's
            await pg.set_content(
                f'<body style="margin:0;background:transparent">'
                f'<style>#w>svg{{width:100%;height:100%;display:block}}</style>'
                f'<div id="w" style="width:{w}px;height:{h}px;color:{it["color"]}">'
                f'{it["html"]}</div></body>')
            await pg.wait_for_timeout(30)
            await pg.locator('#w').screenshot(path=it['png'], omit_background=True)
        await b.close()
    json.dump(data, io.open('slides.json', 'w', encoding='utf-8'))
    print('rasterised', len(jobs), 'unique SVGs')

asyncio.run(main())
