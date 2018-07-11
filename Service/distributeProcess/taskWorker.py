# coding=utf-8
import time
from multiprocessing.managers import BaseManager


# 创建类似的QueueManager
class QueueManager(BaseManager):
    pass

# 1.使用queuemanager注册用于获取queue的方法名称
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')
# 2.连接到服务器
server_add = '127.0.0.1'
print 'connet to server %s ……' % server_add
# 通过端口和验证口令获取队列
m = QueueManager(address=(server_add, 8001), authkey='syj')
# 建立连接
m.connect()
# 3.获取queue的对象
task = m.get_task_queue()
result = m.get_result_queue()
# 4.从task中获取任务，并把结果写入result队列
while not task.empty():
    image_url = task.get(True, timeout=5)
    print 'run task download %s ……' % image_url
    time.sleep(1)
    result.put('%s------> success' % image_url)

# 处理结束
print 'worker exit.'
