# coding:utf-8
import socket
import threading
import time


def dealClient(sock, addr):
    # 4.接收传来的数据，并发送给对方
    print 'Accept new connect from %s:%s……' % addr
    sock.send('hello ! i am service')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        print '---->>%s!' % data.decode('utf-8')
        sock.send(('loop_msg: %s!' % data.decode('utf-8')).encode('utf-8'))
    # 5.关闭socket
    sock.close()
    print 'connect from %s:%s closed.' % addr

if __name__ == '__main__':
    # 1.创建一个机遇ipv4和TCP协议的socket,绑定的ip和端口
    # socket.AF_INET服务器之间基于IPV4网络通信；socket.AF_INET6 IPV6
    # socket.SOCK_STREAM 流式socket，用于TCP；socket.SOCK_DGRAM 数据报式socket，用于UDP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 9999))
    # 2.服务端开始监听TCP传入的客户端连接,最大5个连接数
    s.listen(5)
    print 'waiting for connect……'
    while True:
        # 3.服务端接收客户端一个TCP连接并返回socket对象和客户端的地址
        sock, addr = s.accept()
        # 创建新线程来处理TCP连接
        t = threading.Thread(target=dealClient, args=(sock, addr))
        t.start()
