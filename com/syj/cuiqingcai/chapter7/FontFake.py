import logging
from playwright.async_api import async_playwright

import asyncio

logging.basicConfig(level=logging.INFO, format={'%(asctime)s - %(levelname)s : %(message)s'})


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        await page.goto('https://antispider4.scrape.center')
        await page.wait_for_load_state('networkidle')

        elements = await page.query_selector_all('#index .item p')
        for element in elements:
            print('-----')
        browser.close()


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())