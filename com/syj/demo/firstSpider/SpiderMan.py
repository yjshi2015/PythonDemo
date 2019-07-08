# coding=utf-8

from DataOutput import DataOutput
from HtmlDownloader import HtmlDownloader
from HtmlParser import HtmlParser
from UrlManager import UrlManager

class SpiderMan(object):

    def __init__(self):
        self.manager = UrlManager()
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        self.output = DataOutput()

    def crawl(self, root_url):
        # 添加入口URL
        self.manager.add_new_url(root_url)
        # 判断是否有新的URL及已抓取数量
        while (self.manager.has_new_url() and self.manager.old_url_size() < 100):
            try:
                # 从URL管理器获取新的链接
                new_url = self.manager.get_new_url()
                print '1-------->new_url', new_url
                # 下载网页
                html = self.downloader.download(new_url)
                print '2-------->html'
                # 解析抽取网页
                new_urls, data = self.parser.parser(new_url, html)
                print '3-------->new_urls, data', new_urls, data
                # 将抽取的URL添加到管理器中
                self.manager.add_new_urls(new_urls)
                print '4-------->new_urls', new_urls
                # 数据存储器存储文件
                self.output.store_data(data)
                print '已经抓取%d个链接' % self.manager.old_url_size()
            except Exception, e:
                print 'crawl failed %s' % e
        # 将数据存储为指定格式
        self.output.output_html()


if __name__ =="__main__":
    spider_man = SpiderMan()
    spider_man.crawl("https://baike.baidu.com/item/%E9%95%BF%E5%AE%89%E5%8D%81%E4%BA%8C%E6%97%B6%E8%BE%B0/20110435")