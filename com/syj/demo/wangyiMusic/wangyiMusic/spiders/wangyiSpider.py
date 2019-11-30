# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request, FormRequest
import string


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
            print title + " : " + href
            # 构造request并提交给Scrapy引擎
            yield Request(url=href, callback=self.parse_top_list)

    def parse_top_list(self, response):
        # print '----------开始解析top list页面'
        songs = response.xpath("//*[@id='song-list-pre-cache']/ul/li")
        for song_item in songs:
            song_link = self.web_domain + song_item.xpath(".//a/@href").extract()[0]
            song_name = song_item.xpath(".//a/text()").extract()[0]
            if song_link.find('1405319676') > -1:
                print '----------以下为歌曲基础信息'
                print song_name + ' : ' + song_link
                yield Request(url=song_link, callback=self.parse_song_detail)

    def parse_song_detail(self, response):
        print '-------------获取到了歌曲详情页'
        yield FormRequest(url='https://music.163.com/weapi/v1/resource/comments/R_SO_4_1405319676?csrf_token=',
                      cookies={'JSESSIONID-WYYY': 'Ts9secQyEF8vvK7IRyEgHEpEJsIN22zEriFa7bJs%2Bs1lJMu34n%2B%2Fhpn1opXXHO6D4FtZ8KEy0KlBy8gY%5Crsk72vm7r2u4pOA7obH0Hfe0F%5CvZ1xMO8gebEwEZEenabVR00XlnIkXel7ZYK0%2BDwsNmDehGjMnTRAYBhVud88OMOZTxSzT%3A1575122816996',
                                '_iuqxldmzr_': '32',
                                '_ntes_nnid': '7830b2e4dcb89f4879ef80aa0d69fdce,1573600963954',
                                '_ntes_nuid': '7830b2e4dcb89f4879ef80aa0d69fdce',
                                'WM_NI': 'cNxbDqb6XAcSPskR7EA8bFcZeSHyG0INM9%2Fd1QyxEfukQFLHQFOidITPBMNMJ%2FsjxlWqdU71yC5A0v2hlLQXwmV5Vza7SeRzpufJnuqxT7A90K704iRfzxjfYS9vSc5IOHc%3D',
                                'WM_NIKE': '9ca17ae2e6ffcda170e2e6eeb0ca79a9ef8eb4ee428a9a8aa3d44e828f9e84b87b8fea87a5ae45f6e7bbbad42af0fea7c3b92aa192b883c77ba2ea98a2e25994ada5b3b64f83e8aea7e252a78d889ac63c8b9283daae70f38fb799c86eb7b59fa7cf44939a818ae74398908eaecd478af1bd8bfb6895afacb6b63bbb9dfba2b37ef2b8a4add454b5b39ad6d572a3e99d86d172b4abaaabed7fb3a89cd8c433f495f9d1b76392bab699e96e9b8df797d269f79781a9e237e2a3',
                                'WM_TID': 'Cz9oYWEWcbVAEVVRFBJt%2BXlSqbIbwUMo'},
                      formdata={'params': 'J4mA81M0gdSMYccqBWLDohZPox0U03zM1Mb6RwMdxje73KQXW1u9+WcILAlu69A7YaiTWnPpKf+9dCdYxpPLD10hBPMuWm+32otwE8LpPU64jI5LHPgb8YJv2i8WRlAYySizPx+ROipOyatjF+fCErN63/NEyXkPSPzkLN9ueHrGzDu483N+i/gUBRCdnDap',
                            'encSecKey': '5c8ba02d28bef410560590c76535530c50f4afb4898142be0a594b0467889ee10afb98755b9411968d2eaba50a69666d31705179f255f5841890620e3677eb453612a13dbfd8c7b1af4404a2d1ffba412611dd81502aecabfb0275f47ad085482201e6858962619ac22becff6aac2d4a95e44dc1e2f3c2990eb5df0c764a0510'},
                      callback=self.parse_song_comment)

    def parse_song_comment(self, response):
        print '-------------获取到了歌曲评论页'
        print response.text
        print '-------------歌曲评论页结束'
        # with open('my_girl.txt', 'wb') as f:
        #     import pickle
        #     html = response.text.encode('utf-8').decode('unicode_escape')
        #     pickle.dump(html, f)

