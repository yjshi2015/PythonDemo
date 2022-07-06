# Scrapy
[英文文档](https://docs.scrapy.org/en/latest/)、
[中文文档](https://scrapy-chs.readthedocs.io/zh_CN/0.24/)、
[git地址](https://github.com/scrapy/scrapy/tree/2.6.1)

- 轻量级保存：用文件保存爬虫结果
```python
# json格式保存
scrapy crawl quotes -o quotes.json
# json行格式保存
scrapy crawl quotes -o quotes.jsonlines
# CSV格式保存
scrapy crawl quotes -o quotes.csv
# xml格式保存
scrapy crawl quotes -o quotes.xml
# pickle格式保存
scrapy crawl quotes -o quotes.pickle
# marshal格式
scrapy crawl quotes -o quotes.marshal
# ftp远程输出
scrapy crawl quotes -o ftp://user:pass@ftp.example.com/path/to/quotes.csv
```