import logging
import re

from playwright.async_api import async_playwright

import asyncio

logging.basicConfig(level=logging.INFO, format=('%(asctime)s - %(levelname)s : %(message)s'))
mapping = None


async def main():
    global mapping
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        await page.goto('https://antispider4.scrape.center/css/app.654ba59e.css')
        await page.wait_for_load_state('networkidle')
        css_content = await page.content()
        mapping = parse_icon_number(css_content)

        await page.goto('https://antispider4.scrape.center')
        await page.wait_for_load_state('networkidle')

        items = await page.query_selector_all('#index .item')
        for item in items:
            film_info = await parse_film_info(item)
            logging.info('film info %s', film_info)
        await browser.close()


def parse_icon_number(css_content):
    '''
    解析css中的icon-xxx跟数字的映射关系
    ①强行使用playwright，熟悉playwright语法。其实可以使用requests更合适，避免跟接下来的核心逻辑使用同一个浏览器驱动
    ②re.search用于匹配1个位置的元素；re.compile结合re.findall用于匹配多个位置的元素
    :param css_content:
    :return: 字典dict
    '''
    pattern = re.compile(r"(icon-\d+):before{content:\"(.*?)\"}")
    result = re.findall(pattern, css_content)
    return {item[0]: item[1] for item in result}


async def parse_film_info(item_html):
    '''
    解析item节点下的電影名字和得分
    ①通过筛选器query_selector获取到节点后，再获取节点属性，还必须加await！！！
    :param item_html:
    :return:
    '''
    file_name = await item_html.query_selector('a h2')
    # 获取属性，还得用await
    file_name = await file_name.text_content()
    icons = await item_html.query_selector_all('.score span i')
    scores = []
    for icon in icons:
        # 获取属性，还得用await
        key = await icon.get_attribute('class')
        scores.append(mapping.get(key.split(' ')[1]))
    return {'file_name': file_name, 'score': ''.join(scores)}



if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())