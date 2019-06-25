# coding=utf-8
# 任务进程,消费task_queue队列,生产result_result队列

import time
from multiprocessing.managers import BaseManager


# 创建队列管理对象
class QueueManager(BaseManager):
    pass


# 1.使用QueueManager注册用于获取Queue的方法名称
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')


# 2.连接到服务器
server_addr = '127.0.0.1'
print ('connect to server %s...' % server_addr)
manager = QueueManager(address=(server_addr, 8001), authkey='syj')
manager.connect()

# 3.获取Queue的对象
task = manager.get_task_queue()
result = manager.get_result_queue()


# 4.从task队列获取任务,把处理结果写入result队列
while(not task.empty()):
    image_url = task.get(True, timeout=5)
    print ('run task download %s...' % image_url)
    time.sleep(1)
    result.put('%s ---> success' % image_url)


# 处理结束
print ('worker exit.')
