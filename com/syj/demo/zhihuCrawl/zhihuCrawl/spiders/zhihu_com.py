# -*- coding: utf-8 -*-
import json
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request,FormRequest
from scrapy.selector import Selector
import os

from com.syj.demo.zhihuCrawl.zhihuCrawl.items import UserInfoItem,RelationItem


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
        name = response.xpath("//*[@class='title-section']/span/text()").extract_first()
        location = response.xpath("//*[@class='location item']/@title").extract_first()
        business = response.xpath("//*[@class='business item']/@title").extract_first()
        gender = response.xpath("//*[@class='item gender']/i/@class").extract_first()
        if gender and u"female" in gender:
            gender = u"female"
        else:
            gender = u"male"
        employment = response.xpath("//*[@class='employment item']/@title").extract_first()
        position = response.xpath("//*[@class='position item'/@title").extract_first()
        education = response.xpath("//*[@class='education item']/@title").extract_first()

        try:
            followees_num, followers_num = tuple(response.xpath("//div[@class='zm-profile-side-following"
                                                                "zg-clear']/a[@class='item']/strong/text()").extract())
            relation_url = response.xpath("//*[@class='zm-profile-side-followingzg-clear']/a/@href").extract()
        except Exception, e:
            followees_num, followers_num = tuple(response.xpath("//div[@class='Profile-followStatusValue']/text()").extract())
            relation_url = response.xpath("//a[@class='Profile-followStatus']/@href").extract()

        # 构造用户信息返回
        user_info_item = UserInfoItem(user_id=user_id, user_image_url=user_image_url, name=name, location=location,
                                      business=business, gender=gender, employment=employment, position=position,
                                      education=education, followers_num=int(followers_num),
                                      followees_num=int(followees_num))
        yield user_info_item

        # 开始分析用户关系
        for url in relation_url:
            if u"followees" in url:
                relation_type = u"followees"
            else:
                relation_type = u"followers"
            yield Request(response.urljoin(url=url),
                          meta={
                              'user_id': user_id,
                              'relation_type': relation_type,
                              'cookiejar': response.meta['cookiejar'],
                              'dont_merge_cookies': True
                          },
                          errback=self.parse_err,
                          callback=self.parse_relation
                          )

    def parse_relation(self, response):
        '''
        解析和我有关系的用户,只能处理前20个
        :param response:
        :return:
        '''
        user_id = response.meta['user_id']
        # 参数通过meta来传递
        relation_type = response.meta['relation_type']
        relations_url = response.xpath("//*[@class='zh-general-list clearfix']/div/a/@href").extract()
        # 每个关注者/被关注者的id
        relations_id = [os.path.split(url)[-1] for url in relations_url]
        yield RelationItem(user_id=user_id, relation_type=relation_type, relations_id=relations_id)