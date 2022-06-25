import logging
from pyppeteer import launch
from pyppeteer.errors import TimeoutError
import asyncio

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

INDEX_URL = 'https://spa2.scrape.center/page/{page}'
TIMEOUT = 10
TOTAL_PAGE = 10
WINDOW_WIDTH, WINDOW_HEIGHT = 1366, 768

HEADLESS = False
browser, page = None, None


async def init():
    global browser, page
    browser = await launch(headless=HEADLESS, args=['--disable-infobars',
                                                    f'--window-size={WINDOW_WIDTH}, {WINDOW_HEIGHT}'])
    page = await browser.newPage()
    await page.evaluateOnNewDocument('Object.defineProperty(navigator, "webdriver", {get:()=>undefined})')
    await page.setViewport({'width': WINDOW_WIDTH, 'height': WINDOW_HEIGHT})


async def scrape_page(url, selector):
    logging.info('scraping %s', url)
    try:
        await page.goto(url)
        # selector为CSS筛选器
        await page.waitForSelector(selector, options={
            'timeout': TIMEOUT * 1000
        })
    except TimeoutError:
        logging.error('error occurred while scraping %s', url, exc_info=True)


async def scrape_index(page):
    url = INDEX_URL.format(page=page)
    await scrape_page(url, '.item .name')


async def parse_index():
    # 根据筛选器找到符合条件的节点，并执行js方法，返回结果
    return await page.querySelectorAllEval('.item .name', 'nodes => nodes.map(node => node.href)')


async def scrape_detail(url):
    await scrape_page(url, 'h2')


async def parse_detail():
    url = page.url
    name = await page.querySelectorEval('h2', 'node => node.innerText')
    categories = await page.querySelectorAllEval('.categories button span', 'nodes => nodes.map(node =>'
                                                                            'node.innerText)')
    cover = await page.querySelectorEval('.cover', 'node => node.src')
    score = await page.querySelectorEval('.score', 'node => node.innerText')
    drama = await page.querySelectorEval('.drama p', 'node => node.innerText')
    return {
        'url': url,
        'name': name,
        'categories': categories,
        'cover': cover,
        'score': score,
        'drama': drama
    }


async def main():
    await init()
    try:
        for page in range(1, TOTAL_PAGE + 1):
            await scrape_index(page)
            detail_urls = await parse_index()
            # logging.info('detail urls %s', detail_urls)
            for detail_url in detail_urls:
                await scrape_detail(detail_url)
                detail_data = await parse_detail()
                logging.info('detail data %s', detail_data)
    finally:
        await browser.close()


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
