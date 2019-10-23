# -*- coding: utf-8 -*-
import json
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request,FormRequest
from scrapy.selector import Selector


class ZhihuComSpider(CrawlSpider):
    name = 'zhihu.com'
    allowed_domains = ['zhihu.com']
    start_urls = ['https://www.zhihu.com/people/faraway-43-18/activities']

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def __init__(self, *args, **kwargs):
        super(ZhihuComSpider, self).__init__(*args, **kwargs)
        self.xsrf = ''
        self.cookies = ''

    def start_requests(self):
        # 首先进入登录页面
        return [Request('https://www.zhihu.com/#signin',
                        callback=self.start_login,
                        meta={'cookiejar': 1})
                ]

    def start_login(self, response):
        # 开始登录
        self.xsrf = Selector(response).xpath(
            '//input[@name="_xsrf"]/@value'
        ).extract_first()
        return [FormRequest(
            'https://www.zhihu.com/login/phone_num',
            method='POST',
            meta={'cookiejar': response.meta['cookiejar']},
            formdata={
                '_xsrf': self.xsrf,
                'phone_num': 'xxxxx',
                'password': 'xxxxx',
                'captcha_type': 'cn'
            },
            callback=self.after_login
        )]

    def after_login(self, response):
        # 验证是否登录成功
        if json.loads(response.body)['msg'].encode('utf8') == "登录成功":
            self.logger.info(str(response.meta['cookiejar']))
            return [Request(
                # 此处为跳转到用户主页面
                self.start_urls[0],
                meta={'cookiejar': response.meta['cookiejar']},
                callback=self.parse_user_info,
                errback=self.parse_err
            )]
        else:
            self.logger.error('登录失败')
            return

    def parse_user_info(self, response):
        # 解析用户信息
        user_id = os.path.split(response.url)[-1]
        user_image_url = response.xpath("//img[@class='AvatarAvatar--1']/@src").extract_first()
