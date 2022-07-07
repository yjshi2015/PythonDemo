# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HttpbinDemoItem(scrapy.Item):
    args = scrapy.Field()
    headers = scrapy.Field()
    origin = scrapy.Field()
    url = scrapy.Field()
