import asyncio
import aiohttp
import time

start = time.time()

'''
    asyncio & aiohttp的使用
    async/loop/gather
'''
async def request():
    url = 'https://www.httpbin.org/delay/5'
    print('waiting for', url)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            await response.text()
            print('Get response from url: ', url, ', response: ', response)


async def main():
    tasks = [asyncio.ensure_future(request()) for _ in range(10)]
    await asyncio.gather(*tasks)
    end = time.time()
    print('Cost time:', end - start)

if __name__ == '__main__':
    # asyncio.run(main())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())