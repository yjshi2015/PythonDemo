import json

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ChromeOptions
import logging
from time import sleep
from urllib.parse import urljoin
from os import makedirs
from os.path import exists

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

RESULTS_DIR = 'results'
exists(RESULTS_DIR) or makedirs(RESULTS_DIR)

INDEX_URL = 'https://spa2.scrape.center/page/{page}'
TIME_OUT = 10
TOTAL_PAGE = 10

options = ChromeOptions()
# 隐藏webdriver提示条
options.add_experimental_option('excludeSwitches', ['enable-automation'])
# 隐藏自动化扩展信息
options.add_experimental_option('useAutomationExtension', False)
# 无头模式，提升爬取性能
options.add_argument('--headless')
browser = webdriver.Chrome(options=options)
# cdp即chrome devtools protocol,chrome开发工具协议，
# 利用它可以实现在每个页面钢架在的时候就执行JavaScript语句，进而反屏蔽。
# 这里执行的CDP方法叫做Page.addScriptToEvaluateOnNewDocument
browser.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
    'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined}'
})
wait = WebDriverWait(browser, TIME_OUT)


def scrape_page(url, condition, locator):
    logging.info('scraping %s', url)
    try:
        browser.get(url)
        wait.until(condition(locator))
    except TimeoutException:
        logging.error('error occurred while scraping %s', url, exc_info=True)


def scrape_index(page):
    url = INDEX_URL.format(page=page)
    scrape_page(url, condition=EC.visibility_of_all_elements_located,
                locator=(By.CSS_SELECTOR, '#index .item'))


def parse_index():
    elements = browser.find_elements(By.CSS_SELECTOR, '#index .item .name')
    for element in elements:
        href = element.get_attribute('href')
        yield urljoin(INDEX_URL, href)


def scrape_detail(url):
    scrape_page(url, condition=EC.visibility_of_element_located,
                locator=(By.TAG_NAME, 'h2'))


def parse_detail():
    url = browser.current_url
    name = browser.find_element(By.CSS_SELECTOR, '.item h2').text
    categories = [element.text for element in browser.find_elements(By.CSS_SELECTOR, '.categories span')]
    cover = browser.find_element(By.CSS_SELECTOR, '.cover').get_attribute('src')
    score = browser.find_element(By.CSS_SELECTOR, '.score').text
    drama = browser.find_element(By.CSS_SELECTOR, '.drama p').text
    return {
        'url': url,
        'name': name,
        'categories': categories,
        'cover': cover,
        'score': score,
        'drama': drama
    }


def save_data(data):
    name = data.get('name')
    data_path = f'{RESULTS_DIR}/{name}.json'
    json.dump(data, open(data_path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)


def main():
    try:
        for page in range(1, TOTAL_PAGE + 1):
            scrape_index(page)
            detail_urls = parse_index()
            # logging.info('details urls %s', list(detail_urls))
            for detail_url in list(detail_urls):
                scrape_detail(detail_url)
                detail_data = parse_detail()
                save_data(detail_data)
                # logging.info('detail url %s, data data %s', detail_url, detail_data)
    finally:
        browser.close()


if __name__ == '__main__':
    main()