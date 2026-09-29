"""Every word the deck shows must survive into the extracted primitives."""
import asyncio, json, io, re
from playwright.async_api import async_playwright
SRC='file:///tmp/claude-0/-home-user-Brand-Method-Website/471a0940-bfd5-599e-8262-8b46047adbb9/scratchpad/iaq-deck-standalone.html'
norm=lambda s: re.sub(r'\s+',' ', s).strip().lower()
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args=['--no-sandbox'])
        pg=await b.new_page(); await pg.goto(SRC, timeout=120000); await pg.wait_for_timeout(4000)
        html=await pg.evaluate("()=>[...document.querySelectorAll('.slide')].map(s=>s.innerText)")
        await b.close()
    data=json.load(io.open('slides.json',encoding='utf-8'))
    bad=0
    for i,(h,s) in enumerate(zip(html,data),1):
        got=norm(' '.join(r['t'] for it in s['items'] if it['k']=='text' for r in it['runs']))
        miss=[w for w in set(re.findall(r"[a-z0-9][a-z0-9&/.,'-]{2,}", norm(h))) if w not in got]
        if miss:
            bad+=1; print(i, sorted(miss)[:12])
    print('slides with missing words:', bad)
asyncio.run(main())
