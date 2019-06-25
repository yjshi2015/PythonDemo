# coding=utf-8
# 服务端进程,用来产生任务队列,并接收处理结果

import random,time,Queue
from multiprocessing.managers import BaseManager

# 1.建立task_queue和result_queue,用来存储任务和结果
task_queue = Queue.Queue()
result_queue = Queue.Queue()


class Queuemanager(BaseManager):
    pass


# 2.创建的任务注册到网络中
Queuemanager.register('get_task_queue', callable=lambda:task_queue)
Queuemanager.register('get_result_queue', callable=lambda : result_queue)

# 3.绑定端口,相当于对象的初始化
manage = Queuemanager(address=('', 8001), authkey='syj')

# 4.启动管理,坚挺信息通道
manage.start()

# 5.通过管理实例的方法获得通过网络访问的Queue对象
task = manage.get_task_queue()
result = manage.get_result_queue()

# 6.添加任务
for url in ["Imageurl_" + str(i) for i in range(10)]:
    print 'put task %s ...' % url
    task.put(url)

# 获得返回结果
print 'try get result ....'
for i in range(10):
    print 'result is %s' % result.get(timeout=10)

# 关闭管理
manage.shutdown