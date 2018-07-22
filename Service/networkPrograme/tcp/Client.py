# coding:utf-8
import socket

# 1.初始化socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2.连接目标地址
s.connect(('127.0.0.1', 9999))
# 3.接收消息
print '1---->' + s.recv(1024).decode('utf-8')
# 4.发送消息
# s.send('Hello, i am client')
# print '2---->' + s.recv(1024).decode('utf-8')
# s.send(b'exit')
# 5.关闭socket
s.close()
