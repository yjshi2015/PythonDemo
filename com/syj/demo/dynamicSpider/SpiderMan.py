# coding=utf-8
import time
from HtmlDownloader import HtmlDownloader
from HtmlParse import HtmlParse
from DataOutput import DataOutput


class SpiderMan(object):

    def __init__(self):
        self.downloader = HtmlDownloader()
        self.parser = HtmlParse()
        self.output = DataOutput()

    def crawl(self, root_url):
        content = self.downloader.downloader(root_url)
        urls = self.parser.parser_url(root_url, content)
        # 构造一个获取票房连接的URL
        for url in urls:
            print '---------->URL', url, url[0], url[1]
            try:
                t = time.strftime("%Y%m%d%H%M%S3282", time.localtime())
                rank_url = 'http://service.library.mtime.com/Movie.api' \
                    '?Ajax_CallBack=true' \
                    '&Ajax_CallBackType=Mtime.Library.Services' \
                    '&Ajax_CallBackMethod=GetMovieOverviewRating' \
                    '&Ajax_CrossDomain=1' \
                    '&Ajax_RequestUrl=%s' \
                    '&t=%s' \
                    '&Ajax_CallBackArgument0=%s' % (url[0], t, url[1])
                rank_content = self.downloader.downloader(rank_url)
                print 'ajax接口返回内容-------->', rank_content
                data = self.parser.parser_json(rank_url, rank_content)
                self.output.store_data(data)
            except Exception, e:
                print '获取ajax动态数据失败', e
        self.output.output_end()
        print '=======end========='


if __name__ == '__main__':
    spider = SpiderMan()
    spider.crawl('http://theater.mtime.com/China_Beijing/')