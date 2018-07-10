# coding=utf-8
from multiprocessing import Process, Queue
import os, time, random


# 添加进程
def proc_write(q, urls):
    print 'Process(%s) is writing……' % os.getpid()
    for url in urls:
        q.put(url)
        print 'Put %s to queue……' % url
        time.sleep(random.random())


# 删除进程
def proc_read(q):
    print 'Process %s is reading' % os.getpid()
    while True:
        url = q.get(True)
        print 'Get %s from queue' % url

if __name__ == '__main__':
    # 父进程创建Queue，并传给各个子进程
    q = Queue()
    proc_write1 = Process(target=proc_write, args=(q, ['url1', 'url2', 'url3']))
    proc_write2 = Process(target=proc_write, args=(q, ['url4', 'url5', 'url6']))
    proc_reader = Process(target=proc_read, args=(q,))
    # 启动子进程写入
    proc_write1.start()
    proc_write2.start()
    # 启动子进程读取
    proc_reader.start()
    # 等待writer结束
    proc_write1.join()
    proc_write2.join()
    # reader进程是死循环，只能强制结束
    proc_reader.terminate()
