# coding=utf-8
import scrapy


class BlogSpider(scrapy.Spider):
    name = "blog_spider" # 爬虫的名称
    allowed_domains = ["cnblogs.com"] # 允许的域名
    start_urls = ["http://www.cnblogs.com/qiyeboy/default.html?page=1"]

    def parse(self, response):
        # 实现网页的解析
        # 首先抽取所有的文章
        papers = response.xpath(".//*[@class='day']")
        # 从每篇文章中抽取数据
        for paper in papers:
            print "---------------"
            print paper
            url = paper.xpath(".//*[@class='postTitle']/a/@href").extract()[0]
            title = paper.xpath(".//*[@class='postTitle']/a/text()").extract()[0]
            time = paper.xpath(".//*[@class='dayTitle']/a/text()").extract()[0]
            content = paper.xpath(".//*[@class='postCon']/div/text()").extract()[0]
            print "url: " + url, " title: " + title, " time: " + time, " content: " + content