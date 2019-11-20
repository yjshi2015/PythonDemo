# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request, FormRequest


class WangyispiderSpider(CrawlSpider):
    name = 'wangyiSpider'
    allowed_domains = ['163.com']
    web_domain = 'https://music.163.com'
    start_urls = ['https://music.163.com/discover']

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def start_requests(self):
        # 首先进入主页面
        return [Request('https://music.163.com',
                        callback=self.start_home_page,
                        meta={'cookiejar': 1})
                ]

    def start_home_page(self, response):
        print '----------准备进入discover页面'
        return [Request(
                self.start_urls[0],
                meta={'cookiejar': response.meta['cookiejar']},
                callback=self.parse_home_page)
                ]

    def parse_home_page(self, response):
        print '----------开始解析discover页面'
        tops = response.xpath("//dt[@class='top']")
        # tops = response.xpath(".//*[@id='top-flag']")
        for top in tops:
            print '----------一下为top内容'
            title = top.xpath(".//*[@class='tit']/a/@title").extract()[0]
            href = self.web_domain + top.xpath(".//*[@class='tit']/a/@href").extract()[0]
            print title + " : " + href
            # 构造request并提交给Scrapy引擎
            yield Request(url=href, callback=self.parse_top_list)

    def parse_top_list(self, response):
        print '----------开始解析top list页面'
        html = response.text
        print html
        # songs = response.xpath("//tbody")
        # print '----------size:' + str(len(songs))
        # for song in songs:
        #     song_item = song.xpath(".//*[@class='ttc']/span/a")
        #     song_link = song_item.xpath(".//@href").extract()
        #     song_name = song_item.xpath(".//b/@title").extract()
        #     print song_link
        #     print song_name