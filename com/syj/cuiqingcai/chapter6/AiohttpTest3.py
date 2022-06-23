import asyncio
import aiohttp
import time

'''
    异步aiohttp线程的api
    session.post('http://www.httpbin.org/post', data=b'data')
    session.put('http://www.httpbin.org/put', data=b'data')
    session.delete('http://www.httpbin.org/delete')
    session.head('http://www.httpbin.org/get')
    session.options('http://www.httpbin.org/get')
    session.patch('http://www.httpbin.org/patch', data=b'data')
'''

# 最大协程数量为5，即并发量为5
semaphore = asyncio.Semaphore(5)

async def get_params():
    params = {
        'name': 'zhangsan',
        'age': 20
    }
    url = 'https://www.httpbin.org/get'
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            print(await response.text())


async def post_data():
    '''
    针对请求头中的content-type为application/x-www-form-rulencoded
    :return:
    '''
    data = {
        'name': 'zhangsan',
        'age': 20
    }
    url = 'https://www.httpbin.org/post'
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=data) as response:
            print(await response.text())


async def post_data_2():
    '''
    针对请求头的content-type为application/json格式
    :return:
    '''
    data = {
        'name': 'zhangsan',
        'age': 20
    }
    url = 'https://www.httpbin.org/post'
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=data) as response:
            print(await response.text())


async def post_data_3():
    '''
    熟悉response中的各个部分，status/header/body/响应体二进制内容/响应体json结果
    超时时间设置
    :return:
    '''
    data = {
        'name': 'zhangsan',
        'age': 20
    }
    url = 'https://www.httpbin.org/post'
    async with aiohttp.ClientSession(timeout= aiohttp.ClientTimeout(total=5)) as session:
        async with session.post(url, json=data) as response:
            print('status :', response.status)
            print('header :', response.headers)
            print('body :', await response.text())
            print('bytes :', await response.read())
            print('json :', await response.json())


async def post_data_semaphore():
    '''
    aiohttp支持非常高的并发，出于对目标网站的保护，以及防止容器的资源耗尽，需要设置最大并发数
    类型于Java线程池的最大线程数
    :return:
    '''
    data = {
        'name': 'zhangsan',
        'age': 20
    }
    url = 'https://www.httpbin.org/post'
    start = time.time()
    async with semaphore:
        async with aiohttp.ClientSession(timeout= aiohttp.ClientTimeout(total=5)) as session:
            async with session.post(url, json=data) as response:
                print('Cost time :', time.time() - start)


async def main():
    tasks = [asyncio.ensure_future(post_data_semaphore()) for _ in range(10000)]
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    # loop.run_until_complete(get_params())
    # loop.run_until_complete(post_data())
    # loop.run_until_complete(post_data_2())
    # loop.run_until_complete(post_data_3())
    loop.run_until_complete(main())
