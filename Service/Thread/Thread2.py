# coding=utf-8
import random
import threading
import time


class MyThread(threading.Thread):
    def __init__(self, name, urls):
        threading.Thread.__init__(self, name=name)
        self.urls = urls

    def run(self):
        print "current %s is running……" % threading.current_thread().name
        for url in self.urls:
            print "%s -------> %s" % (threading.current_thread().name, url)
            time.sleep(random.random())
        print "%s end." % threading.current_thread().name


print "main %s is running……" % threading.current_thread().name
t1 = MyThread(name='thread_1', urls=['url1', 'url2', 'url3'])
t2 = MyThread(name='thread_2', urls=['url4', 'url5', 'url6'])
t1.start()
t2.start()
t1.join()
t2.join()
print "main %s ended" % threading.current_thread().name
