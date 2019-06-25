# coding=utf-8
'''
 TCP通信需要建立一个可靠地链接,且通信的双方以流的形式发送数据
 DCP则是面向无链接的协议,只需要知道对方的IP地址和端口号即可,直接发送数据包,但是并不关心是否能够到达目的端.
 虽然用UDP协议不可靠,但是由于没有建立连接的过程.

 速度比TCP快得多,对于不要求可靠到达的数据,就可以使用UDP协议,比如电话通信的音频数据
'''

import socket
# 穿件socket,绑定指定IP,SOCK_DGRAM指定了这个socket的类型是UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 9999))
print 'bind UDP on 9999...'
while True:
    # 直接发送和接收数据
    data, addr = s.recvfrom(1024)
    print ('received from %s:%s' % addr)
    s.sendto(b'hello, %s...' % data, addr)
