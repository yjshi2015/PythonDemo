# coding=utf-8

import pymongo

# 创建数据库链接
client = pymongo.MongoClient('localhost',27017)
# 连接到指定数据库spider_mongodb
db = client.spider_mongodb
# 获取表page_table这个集合
collection = db.page_table
print '--------->获取表集合成功'
# 插入文档,注意此时要先启mongol服务,否则会报拒绝链接
books = [{"author": "Mike",
          "text": "My first book!",
          "tags": ["爬虫", "python", "网络"],
          "date": "2019-07-13"
          },
         {"author": "qiye",
          "text": "My sec book!",
          "tags": ["hack", "python", "渗透"],
          "date": "2019-07-14"
         }]
collection.insert(books)
print '-------->写入数据成功'
for book in collection.find():
    print book