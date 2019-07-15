# coding=utf-8

import requests

# 网页下载器
class HtmlDownloader(object):

    def downloader(self, url):
        if url is None:
            return None
        user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0'
        headers = {'User-Agent': user_agent}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            response.encoding = 'utf-8'
            return response.text
        return None