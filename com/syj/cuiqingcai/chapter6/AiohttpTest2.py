import asyncio
import aiohttp
import time

'''
    异步线程的循环
'''
async def get():
    url = 'https://www.baid.com'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            await response.text()
            # 此处不可以打印response.text()函数，因为该函数为携程
            # print("=======", response)


async def request(number):
    start = time.time()
    tasks = [asyncio.ensure_future(get()) for _ in range(number)]
    await asyncio.gather(*tasks)
    end = time.time()
    print('Number:', number, ',Cost time:', end - start)

if __name__ == '__main__':
    for number in [1, 3, 5, 10, 15, 30, 50, 100, 200, 500]:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(request(number))
