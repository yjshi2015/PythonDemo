# coding=utf-8

from HtmlDownloader import HtmlDownloader
from HtmlParser import HtmlParser

from multiprocessing.managers import BaseManager


class SpiderWork(object):

    def __init__(self):
        # 爬虫调度器需要先连接上控制节点,然后从url_q队列中获取URL,下载并解析网页,接着将获取的数据提交给
        # result_q队列并返回给控制节点
        BaseManager.register('get_task_queue')
        BaseManager.register('get_result_queue')
        # 链接到服务器
        server_addr = '127.0.0.1'
        print ('connect to server %s....' % server_addr)
        self.m = BaseManager(address=(server_addr, 8001), authkey='baike')
        self.m.connect()
        # 获取Queue对象
        self.task = self.m.get_task_queue()
        self.result = self.m.get_result_queue()
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()

    def crawl(self):
        while (True):
            try:
                if not self.task.empty():
                    url = self.task.get()
                    if url == 'end':
                        print '爬虫节点接到停止通知'
                        # 接着通知其他节点停止工作
                        self.result.put({'new_urls': 'end', 'data': 'end'})
                        return
                    print '爬虫节点正在解析%s ' % url.encode('utf-8')

                    # 下载网页
                    html = self.downloader.download(url)
                    # 解析抽取网页
                    new_urls, data = self.parser.parser(url, html)
                    self.result.put({'new_urls': new_urls, 'data': data})
            except EOFError, e:
                print '链接节点工作失效'
            except Exception, e:
                print e,url
                print 'craw fail..'


if __name__ =="__main__":
    spider_man = SpiderWork()
    spider_man.crawl()
