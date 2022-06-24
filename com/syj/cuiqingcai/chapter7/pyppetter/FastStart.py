import asyncio
from pyppeteer import launch
from pyquery import PyQuery as pq

width, height = 1368, 768

async def main():
    # 关闭无头模式
    # 禁用提示条
    browser = await launch(headless=False, args=['--disable-infobars'])
    page = await browser.newPage()
    # 设置浏览器界面大小
    await page.setViewport({'width': width, 'height': height})
    # 突破反爬
    await page.evaluateOnNewDocument('Object.defineProperty(navigator, "webdriver", {get:()=>undefined}')
    await page.goto('https://spa2.scrape.center')
    await page.waitForSelector('.item .name')
    doc = pq(await page.content())
    names = [item.text() for item in doc('.item .name').items()]
    print('Names:', names)
    await asyncio.sleep(10)
    # 截屏
    await page.screenshot(path='example.png')
    # 执行js脚本
    dimensions = await page.evaluate('''() => {
        return {
            width: document.documentElement.clientWidth,
            height:document.documentElement.clientHeight,
            deviceScaleFactor: window.devicePixelRatio,
        }
    }
    ''')
    print(dimensions)
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())
