# coding=utf-8

import pymongo

# 创建数据库链接
client = pymongo.MongoClient('localhost',27017)
# 连接到指定数据库spider_mongodb
db = client.spider_mongodb
# 获取表page_table数据
collection = db.page_table