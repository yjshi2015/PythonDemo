# coding:utf-8
import socket
# 创建socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 9999))
print 'bind udp on 9999'
while True:
    # 直接发送、接收数据
    data, addr = s.recvfrom(1024)
    print 'receive from %s:%s .' % addr
    s.sendto('loop_msg : %s !' % data, addr)