import re

import scrapy
from scrapy import Request
from seleniumDemo.items import BookItem

times = 0

class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['spa5.scrape.center']
    base_url = 'https://spa5.scrape.center'

    def start_requests(self):
        start_url = f'{self.base_url}/page/1'
        yield Request(start_url, callback=self.parse_index)

    def parse_index(self, response):
        global times
        items = response.css('#index .item')
        for item in items:
            times = times + 1
            if times > 1: return None
            detail_url = item.css('a::attr(href)').extract_first()
            detail_url = response.urljoin(detail_url)
            yield Request(detail_url, callback=self.parse_detail, priority=2)

        # 暂且不访问下一页数据
        # match = re.search(r'page/(\d+)', response.url)
        # if not match: return
        # page = int(match.group(1)) + 1
        # next_url = f'{self.base_url}/page/{page}'
        # yield Request(next_url, callback=self.parse_index)

    def parse_detail(self, response):
        item = BookItem()
        item['name'] = response.xpath(
            '//div[contains(@class, "item")]//h2[contains(@class, "name")]/text()').extract_first()
        item['score'] = response.xpath(
            '//div[contains(@class, "item")]//span[contains(@class, "score")]/text()').re_first('[\d\.]+')
        item['tags'] = response.css('.tags button span::text').extract()
        item['cover'] = response.css('.cover::attr(src)').extract_first()
        item['price'] = response.css('.info .price span::text').extract_first().strip()
        yield item
