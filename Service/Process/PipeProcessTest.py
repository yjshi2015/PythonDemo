# coding=utf-8
# 进程间通信方式：Queue和Pipe,区别在于Queue用来在多个进程间通信，Pipe是在2个进程间通信
import multiprocessing
import os
import random
import time


def proc_send(p, urls):
    for url in urls:
        print "process %s send : %s" % (os.getpid(), url)
        p.send(url)
        time.sleep(random.random())


def proc_recv(p):
    while True:
        print "process %s recv: %s" % (os.getpid(), p.recv())
        time.sleep(random.random())


if __name__ == "__main__":
    pipe = multiprocessing.Pipe()
    p1 = multiprocessing.Process(target=proc_send, args=(pipe[0], ['url_' + str(i) for i in range(10)]))
    p2 = multiprocessing.Process(target=proc_recv, args=(pipe[1],))
    p1.start()
    p2.start()
    p1.join()
    p2.terminate()
