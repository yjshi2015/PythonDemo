import logging
from pyppeteer import launch
import asyncio
from pyquery import PyQuery as pq

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

TIMEOUT = 10

'''
如下demo爬取出来的name是乱序的
'''
async def main():
    browser = await launch()
    page = await browser.newPage()

    await page.goto('https://antispider3.scrape.center/')
    # 等待的条件最好和筛选节点的条件一致，保证需要筛选的节点一定存在！！！
    await page.waitForSelector('#index .bottom h3', options={'timeout': 5000})
    doc = pq(await page.content())
    book_infos = doc('#index .bottom h3')
    for book_info in book_infos.items():
        book_name = []
        if 'whole' in book_info.attr('class'):
            book_name.append(book_info.text())
            logging.info('book name :%s', ''.join(book_name))
            continue
        for span_item in book_info.items():
            book_name.append(span_item.text())
        logging.info('book name :%s', ''.join(book_name))
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())
