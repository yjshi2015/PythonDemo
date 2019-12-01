# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request, FormRequest
import encSecParams
import re
import json

class WangyispiderSpider(CrawlSpider):
    name = 'wangyiSpider'
    allowed_domains = ['163.com']
    web_domain = 'https://music.163.com'
    comments_domain = 'https://music.163.com/weapi/v1/resource/comments/'
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
        # print '----------准备进入discover页面'
        return [Request(
            self.start_urls[0],
            meta={'cookiejar': response.meta['cookiejar']},
            callback=self.parse_home_page)
        ]

    def parse_home_page(self, response):
        # print '----------开始解析discover页面'
        tops = response.xpath("//dt[@class='top']")
        for top in tops:
            # print '----------一下为top内容'
            title = top.xpath(".//*[@class='tit']/a/@title").extract()[0]
            href = self.web_domain + top.xpath(".//*[@class='tit']/a/@href").extract()[0]
            # print title + " : " + href
            # 构造request并提交给Scrapy引擎
            yield Request(url=href, callback=self.parse_top_list)

    def parse_top_list(self, response):
        # print '----------开始解析top list页面'
        songs = response.xpath("//*[@id='song-list-pre-cache']/ul/li")
        for song_item in songs:
            meta = {}
            song_name = song_item.xpath(".//a/text()").extract()[0]
            song_link = self.web_domain + song_item.xpath(".//a/@href").extract()[0]
            pattern = re.compile(r'=\d+')
            result = re.search(pattern, song_link)
            if result:
                song_id = result.group()[1:]
                meta['song_id'] = song_id
            meta['song_name'] = song_name
            meta['song_link'] = song_link
            yield Request(url=song_link, meta=meta, callback=self.parse_song_detail)

    def parse_song_detail(self, response):
        # print '-------------获取到了歌曲详情页'
        rid = 'R_SO_4_' + response.meta['song_id']
        text = {"offset": "0", "total": "true", "limit": "20", "csrf_token": "",
                'rid': rid}
        # 加密
        formdata = encSecParams.encRequest(text)
        yield FormRequest(url=self.comments_domain + rid + '?csrf_token=',
                          formdata=formdata,
                          meta=response.meta,
                          callback=self.parse_song_comment)

    def parse_song_comment(self, response):
        comment_item = {'song_id': response.meta['song_id'],
                        'song_name': response.meta['song_name'],
                        'song_link': response.meta['song_link']}

        comments_result = response.text
        if comments_result:
            all_comments = json.loads(comments_result)
            hot_comments = all_comments.get('hotComments')
            for hot in hot_comments:
                user_id = hot.get('user').get('userId')
                nick_name = hot.get('user').get('nickname')
                comment_id = hot.get('commentId')
                content = hot.get('content')
                dian_zan = hot.get('likedCount')
                time = hot.get('time')
                comment_item['user_id'] = user_id
                comment_item['nick_name'] = nick_name
                comment_item['comment_id'] = comment_id
                comment_item['content'] = content
                comment_item['dian_zan'] = dian_zan
                comment_item['time'] = time
                print comment_item
        # with open('my_girl.txt', 'wb') as f:
        #     import pickle
        #     html = response.text.encode('utf-8').decode('unicode_escape')
        #     pickle.dump(html, f)
