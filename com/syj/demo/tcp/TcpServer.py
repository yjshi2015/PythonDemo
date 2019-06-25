# coding=utf-8
import socket
import threading
import time


def dealClient(sock, addr):
    # 4.接收传来的数据,并发送给对方数据
    print ('accept new connection from %s:%s...' % addr)
    sock.send(b'Hello , i am server')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        print 'receive --->%s' % data.decode('utf-8')
        sock.send(('loop_msg: %s!' % data.decode('utf-8')).encode('utf-8'))

    # 5.关闭socket
    sock.close()
    print ('connect from %s:%s closed.' % addr)


if __name__=="__main__":
    # 1.创建基于IPv4和TCP协议的socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 9999))
    # 2.监听链接,参数为指定在拒绝连接前,操作系统可以挂起的最大连接数量.至少为1,大部分应用设为5就可以了
    s.listen(5)
    print 'wating for connection...'
    while True:
        # 3.建立新连接
        sock, addr = s.accept()
        # 创建新线程来处理TCP链接
        t = threading.Thread(target=dealClient, args=(sock, addr))
        t.start()