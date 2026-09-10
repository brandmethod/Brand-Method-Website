import asyncio
from playwright.async_api import async_playwright
CHROME='/opt/pw-browsers/chromium-1194/chrome-linux/chrome'
OUT='/home/user/Brand-Method-Website/iaq-deck/IAQ-Company-Deck-2026.pdf'
async def main():
    async with async_playwright() as pw:
        b=await pw.chromium.launch(executable_path=CHROME,args=['--no-sandbox'])
        pg=await b.new_page(viewport={'width':1600,'height':900})
        await pg.goto('file:///home/user/Brand-Method-Website/iaq-deck/index.html')
        await pg.wait_for_timeout(3500)
        await pg.emulate_media(media='print')
        await pg.pdf(path=OUT, prefer_css_page_size=True, print_background=True)
        await b.close()
asyncio.run(main())
