import scrapy
from scrapytutorial.items import QuoteItem
from loguru import logger


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['https://quotes.toscrape.com/']

    def parse(self, response):
        quotes = response.css('.quote')
        for quote in quotes:
            item = QuoteItem()
            item['text'] = quote.css('.text::text').extract_first()
            item['author'] = quote.css('.author::text').extract_first()
            item['tags'] = quote.css('.tags .tag::text').extract()
            yield item

        next = response.css('.paper .next a::attr(href)').extract_first()
        logger.info('next url {}', next)
        url = response.urljoin(next)
        yield scrapy.Request(url=url, callback=self.parse)
