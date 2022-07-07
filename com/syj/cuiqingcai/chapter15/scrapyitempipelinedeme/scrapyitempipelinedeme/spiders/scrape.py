import scrapy
from scrapy.http import Request
from scrapyitempipelinedeme.items import MovieItem


class ScrapeSpider(scrapy.Spider):
    name = 'scrape'
    allowed_domains = ['ssr1.scrape.center']
    base_url = 'https://ssr1.scrape.center'
    max_page = 1

    def start_requests(self):
        for i in range(1, self.max_page + 1):
            url = f'{self.base_url}/page/{i}'
            yield Request(url=url, callback=self.parse_index)

    def parse_index(self, response):
        items = response.css('#index .item')
        for item in items:
            href = item.css('.name::attr(href)').extract_first()
            url = response.urljoin(href)
            yield Request(url=url, callback=self.parse_detail)

    def parse_detail(self, response):
        item = MovieItem()
        # css写法
        # item['name'] = response.css('.item a h2::text').extract_first()
        item['name'] = response.xpath('//div[contains(@class,"item")]//h2/text()').extract_first()
        # css写法
        # item['categories'] = response.css('.categories button span::text').extract()
        item['categories'] = response.xpath('//button[contains(@class, "category")]/span/text()').extract()
        # 正则匹配
        item['score'] = response.css('.score::text').re_first('[\d\.]+')
        # class属性+tag共同筛选
        item['drama'] = response.css('.drama p::text').extract_first().strip()
        # 属性包含
        directors = response.xpath('//div[contains(@class, "directors")]//div[contains(@class, "director")]')
        item['directors'] = []
        for director in directors:
            # 属性等于  && 获取属性
            director_image = director.xpath('.//img[@class="image"]/@src').extract_first()
            director_name = director.xpath('.//p[contains(@class, "name")]/text()').extract_first()
            item['directors'].append({
                'name': director_name,
                'image': director_image
            })
        item['actors'] = []
        actor_nodes = response.css('.actors .actor')
        for actor in actor_nodes:
            actor_image = actor.css('.actor .image::attr(src)').extract_first()
            actor_name= actor.xpath('.//p[contains(@class, "name")]/text()').extract_first().strip()
            item['actors'].append({
                'name': actor_name,
                'image': actor_image
            })
        yield item