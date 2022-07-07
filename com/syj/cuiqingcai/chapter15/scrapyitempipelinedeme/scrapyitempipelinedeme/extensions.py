import requests
from scrapy import signals

NOTIFYCATION_URI = 'http://localhost:5000/notify'


class NotificationExtension(object):

    @classmethod
    def from_crawler(cls, crawler):
        print('------->from_crawl')
        ext = cls()
        crawler.signals.connect(ext.spider_open, signal=signals.spider_opened)
        crawler.signals.connect(ext.spider_close, signal=signals.spider_closed)
        crawler.signals.connect(ext.item_scraped, signal=signals.item_scraped)
        return ext


    def spider_open(self, spider):
        print('------->spider_open')
        requests.post(NOTIFYCATION_URI, json={
            'event': 'SPIDER_OPEN',
            'data': {'spider_name': spider.name}
        })


    def spider_close(self, spider):
        print('------->spider_close')
        requests.post(NOTIFYCATION_URI, json={
            'event': 'SPIDER_CLOSE',
            'data': {'spider_name': spider.name}
        })

    def item_scraped(self, item, spider):
        print('------->item_scraped')
        requests.post(NOTIFYCATION_URI, json={
            'event': 'ITEM_SCRAPED',
            'data': {'spider_name': spider.name, 'item': dict(item)}
        })
