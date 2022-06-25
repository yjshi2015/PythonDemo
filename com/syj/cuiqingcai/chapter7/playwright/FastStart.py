from playwright.sync_api import sync_playwright
from playwright.async_api import async_playwright
import asyncio
from time import sleep
import re


def main_sync():
    '''
    同步操作demo
    :return:
    '''
    with sync_playwright() as p:
        for browser_type in [p.chromium, p.firefox, p.webkit]:
            browser = browser_type.launch(headless=False)
            page = browser.new_page()
            page.goto('https://www.baidu.com')
            sleep(3)
            page.screenshot(path=f'screenshot-{browser_type.name}.png')
            print(page.title())
            browser.close()


async def main_async():
    '''
    异步操作demo
    :return:
    '''
    async with async_playwright() as p:
        for browser_type in [p.chromium, p.firefox, p.webkit]:
            browser = await browser_type.launch(headless=False)
            page = await browser.new_page()
            await page.goto('https://www.baidu.com')
            sleep(3)
            await page.screenshot(path=f'async-screenshot-{browser_type.name}.png')
            print(await page.title())
            await browser.close()


def on_response(response):
    print(f'statue {response.status}:{response.url}')


def event_listening():
    '''
    事件监听demo
    :return:
    '''
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        # 注册监听事件
        page.on('response', on_response)
        page.goto('https://spa6.scrape.center')
        # 等待页面加载，所有网络请求加载完成
        page.wait_for_load_state('networkidle')
        # page.wait_for_selector('css筛选器')

        # 获取网页源代码
        html = page.content()
        print(html)
        browser.close()


def hack():
    '''
    网络劫持 demo，拦截所有图片下载请求，只获取图片src即可，提升页面爬取速度
    :return:
    '''
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # 网络劫持入口，拦截所有图片下载
        page.route(re.compile(r"(\.png)|(\.jpg)"), cancle_request)

        page.goto('https://spa6.scrape.center')
        page.wait_for_load_state('networkidle')

        page.screenshot(path='no_picture.png')
        browser.close()


def cancle_request(route, request):
    route.abort()


if __name__ == '__main__':
    # asyncio.get_event_loop().run_until_complete(main_async())
    # main_sync()
    # event_listening()
    hack()
