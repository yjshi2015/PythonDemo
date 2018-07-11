# coding=utf-8
import Queue
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support


# 任务个数
task_number = 10
# 定义收发队列
task_queue = Queue.Queue(task_number)
result_queue = Queue.Queue(task_number)


# 1.创建任务和结果队列
def get_task():
    return task_queue


def get_result():
    return result_queue


# 创建类似的QueueManager
class QueueManager(BaseManager):
    pass


def win_run():
    # 2.利用register方法，把创建的2个队列注册在网络上
    QueueManager.register('get_task_queue', callable=get_task)
    QueueManager.register('get_result_queue', callable=get_result)
    # 3.绑定端口，并设置验证口令
    manager = QueueManager(address=('127.0.0.1', 8001), authkey='syj')
    # 4.启动管理，监听信息通道
    manager.start()
    try:
        # 5.通过网络获取任务队列和结果队列
        task = manager.get_task_queue()
        result = manager.get_result_queue()
        # 6.添加任务
        for url in ["ImageUrl_" + str(i) for i in range(10)]:
            print 'put task %s ……' % url
            task.put(url)
        print 'try get result……'
        for i in range(10):
            print 'result is %s ' % result.get(timeout=10)
    except:
        print 'manager error'
    finally:
        # 关闭管理
        manager.shutdown

if __name__ == '__main__':
    # window下多进程可能会有问题，添加这句可以缓解
    freeze_support()
    win_run()
