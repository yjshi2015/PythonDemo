# coding=utf-8
import socket

# 初始化socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 链接目标IP
s.connect(('127.0.0.1', 9999))
# 接收消息
print('--->' + s.recv(1024).decode('utf-8'))
# 发送消息
s.send(b'hello, i am a client')
print ('-->' + s.recv(1024).decode('utf-8'))
s.send(b'exit')
# 关闭
s.close()