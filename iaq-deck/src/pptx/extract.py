import asyncio, json, io
from playwright.async_api import async_playwright

async def main():
    fn = io.open('extract.js', encoding='utf-8').read()
    async with async_playwright() as p:
        b = await p.chromium.launch(
            executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome',
            args=['--no-sandbox', '--force-device-scale-factor=1'])
        pg = await b.new_page(viewport={'width': 1920, 'height': 1080})
        await pg.goto('file:///home/user/Brand-Method-Website/iaq-deck/index.html')
        await pg.add_style_tag(content="""
          .progress,.nav,.overview,.helpbox,.blackout{display:none!important}
          .deck{overflow:visible;height:auto;scroll-snap-type:none}
          .stage{padding:0;height:auto;display:block}
          .slide{width:1920px!important;height:1080px!important;aspect-ratio:auto!important}
        """)
        await pg.wait_for_timeout(3000)
        data = await pg.evaluate(fn)
        io.open('slides.json', 'w', encoding='utf-8').write(json.dumps(data))
        print('slides:', len(data), '| items:', sum(len(s['items']) for s in data))
        from collections import Counter
        c = Counter(i['k'] for s in data for i in s['items'])
        print(dict(c))
        await b.close()

asyncio.run(main())
