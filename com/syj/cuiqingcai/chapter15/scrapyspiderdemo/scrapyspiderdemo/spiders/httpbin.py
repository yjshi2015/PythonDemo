import scrapy
from scrapy.http import Request
from scrapy.http import JsonRequest, FormRequest


class HttpbinSpider(scrapy.Spider):
    name = 'httpbin'
    allowed_domains = ['www.httpbin.org']
    start_url = 'https://www.httpbin.org/post'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    cookies = {'name': 'syj', 'age': 18}

    #get请求
    # def start_requests(self):
    #     for offset in range(5):
    #         url = self.start_url + f'?offset={offset}'
    #         yield Request(url, headers=self.headers, cookies=self.cookies, callback=self.parse_response,
    #                       meta={'offset': offset})


    # post请求
    data = {'name': 'syj', 'age': '18'}
    def start_requests(self):
        # form表单形式
        yield FormRequest(self.start_url, callback=self.parse_response, formdata=self.data)

        # json形式
        yield JsonRequest(self.start_url, callback=self.parse_response, data=self.data)


    def parse_response(self, response):
        print('url', response.url)
        print('request', response.request)
        print('status', response.status)
        print('header', response.headers)
        print('text', response.text)
        print('meta', response.meta)
