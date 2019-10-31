# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from zhihuCrawl.item import UserInfoItem

class ZhihucrawlPipeline(object):

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db


    '''
        @classmethod修饰的方法类似于Java的静态方法,而没有此注解的方法为实例方法
        第一个参数cls代表当前类
        该方法返回了一个实例化之后的ZhihucrawlPipline对象
    '''
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO__DATABASE', 'zhihu')
        )

    def open_spider(self, spider):
        self.client= pymongo.MongoClient(self.mongo_uri)
        self.db=self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close

    def process_item(self, item, spider):
        if isinstance(item, UserInfoItem):
            self._process_user_item(item)
        else:
            self._process_relation_item(item)
        return item

    def _process_user_item(self, item):
        self.db.UserInfo.insert(dict(item))

    def _process_relation_item(self, item):
        self.db.Relation.insert(dict(item))