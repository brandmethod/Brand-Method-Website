import asyncio, os, re, json
from playwright.async_api import async_playwright
CHROME='/opt/pw-browsers/chromium-1194/chrome-linux/chrome'
URL='file:///home/user/Brand-Method-Website/iaq-deck/index.html'
OUT='/home/user/Brand-Method-Website/iaq-deck/slides-png'
os.makedirs(OUT, exist_ok=True)

def slug(t):
    t = re.sub(r'[^A-Za-z0-9]+', '-', t).strip('-')
    return (t[:44] or 'slide').lower()

async def main():
    async with async_playwright() as pw:
        b = await pw.chromium.launch(executable_path=CHROME, args=['--no-sandbox'])
        # 1920 CSS px wide slide => exact 1920x1080 output at scale 1
        pg = await b.new_page(viewport={'width': 2000, 'height': 1180}, device_scale_factor=1)
        await pg.goto(URL)
        await pg.wait_for_timeout(4000)
        # present mode geometry: slide = min(100vw, 100vh*16/9) -> force an exact 1920 box
        await pg.add_style_tag(content="""
          .progress,.nav,.overview,.helpbox,.blackout{display:none!important}
          .stage{padding:0}
          .slide{width:1920px!important;height:1080px!important;aspect-ratio:auto!important}
        """)
        await pg.wait_for_timeout(1200)
        titles = await pg.evaluate("""()=>[...document.querySelectorAll('.stage')].map(st=>{
          if(st.querySelector('.cover-title')) return 'Cover';
          const e=st.querySelector('.s-title, .div-title, .hero-title');
          if(!e) return 'Slide';
          const d=document.createElement('div');
          d.innerHTML=e.innerHTML.replace(/<br\\s*\\/?>/gi,' ');
          return d.textContent.replace(/\\s+/g,' ').trim();})""")
        slides = await pg.query_selector_all('.slide')
        names = []
        for i, el in enumerate(slides):
            await pg.evaluate("i=>document.querySelectorAll('.stage')[i].scrollIntoView({block:'center'})", i)
            await pg.wait_for_timeout(260)
            name = 'IAQ-%02d-%s.png' % (i + 1, slug(titles[i]))
            await el.screenshot(path=os.path.join(OUT, name))
            names.append(name)
        await b.close()
        print(json.dumps(names, indent=0)[:400])
asyncio.run(main())
