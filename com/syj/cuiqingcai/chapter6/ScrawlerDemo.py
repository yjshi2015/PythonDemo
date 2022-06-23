import asyncio
import logging
import json
import aiohttp

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s:%(message)s')

INDEX_URL = 'https://spa5.scrape.center/api/book/?limit=18&offset={offset}'
DETAIL_URL = 'https://spa5.scrape.center/api/book/{id}'
PAGE_SIZE = 18
PAGE_NUMBER = 1000
CONCURRENCY = 5

semaphore = asyncio.Semaphore(CONCURRENCY)


async def scrape_api(url):
    async with semaphore:
        try:
            logging.info('scraping %s', url)
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    return await response.json()
        except aiohttp.ClientError:
            logging.error('error occurred while scaping %s', url, exc_info=True)


async def scrape_index(page):
    url = INDEX_URL.format(offset=PAGE_SIZE * (page - 1))
    return await scrape_api(url)


async def save_data(data):
    logging.info('sava data : ', data)


async def scrape_detail(id):
    url = DETAIL_URL.format(id=id)
    data = await scrape_api(url)
    await save_data(data)


async def main():
    # 爬取列表页数据
    scrape_index_tasks = [asyncio.ensure_future(scrape_index(page)) for page in range(1, PAGE_NUMBER + 1)]
    results = await asyncio.gather(*scrape_index_tasks)
    # logging.info('results %s', json.dumps(results, ensure_ascii=False, indent=2))
    ids = []
    for index_data in results:
        if not index_data: continue
        for item in index_data.get('results'):
            ids.append(item.get('id'))
    # 爬取详情页数据
    scrape_detail_tasks = [asyncio.ensure_future(scrape_detail(id)) for id in ids]
    await asyncio.gather(*scrape_detail_tasks)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())