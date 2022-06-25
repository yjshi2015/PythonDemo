import logging
import re

from pyppeteer import launch
import asyncio
from pyquery import PyQuery as pq

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')


async def parse_name(book_h3_html):
    items = []
    if 'whole' in book_h3_html.attr('class'):
        items.append(book_h3_html.text())
        logging.info('book name :%s', ''.join(items))
        return ''.join(items)
    spans = book_h3_html('.char')
    for span in spans.items():
        items.append({
            # 获取span标签对应的文本
            'text': span.text().strip(),
            # 获取span标签对应的位置，
            # <span …… style="left: 16px;">白</span>
            # <span …… style="left: 0px;">清</span>
            # <span …… style="left: 48px;">家</span>
            # <span …… style="left: 32px;">之</span>
            'left': int(re.search('(\d+)px', span.attr('style')).group(1))
        })
    # 按照绝对位置排序
    items = sorted(items, key=lambda x: x['left'], reverse=False)
    return ''.join(item.get('text') for item in items)


async def main():
    # 设置无头/禁用提示条/窗口大小/突破反爬
    browser = await launch()
    page = await browser.newPage()
    # 突破反爬
    await page.evaluateOnNewDocument('Object.defineProperty(navigator, "webdriver", {get:()=>undefined})')

    await page.goto('https://antispider3.scrape.center/')
    # 设置等待
    await page.waitForSelector('#index .bottom h3', options={'timeout': 10000})
    doc = pq(await page.content())
    book_infos = doc('#index .bottom h3')
    for book_info in book_infos.items():
        book_name = await parse_name(book_info)
        logging.info('book name %s:', book_name)
    await browser.close()


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())