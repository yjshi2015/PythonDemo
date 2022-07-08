from scrapy.cmdline import execute
import os
import sys


if __name__ == '__main__':
    '''
    1、 os.path.abspath(path) 返回绝对路径
    2、os.path.dirname(path) 返回文件夹路径
    3、sys.path 返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值， sys.path.append当前文件执行的目录的路劲就加入到python
    路劲里面
    4、file 本文件的地址
    文件解析具体些地址参考https://blog.csdn.net/huangwencai123/article/details/89879951
    这行代码获取当前py文件的父目录，省去我们直接复制路径的精力和时间，同时也方便我们将该项目放到其他的平台上去运行，不会报路径的错误。
    5、execute（execute函数是内嵌在scrapy中的，调用这个函数可以直接调用该Scrapy工程项目的爬虫脚本，这个函数的执行需要在爬虫项目的父目录下进行。execute函数里边的参数其实就是将Scrapy爬虫执行命令拆分，然后分别以一个字符的方式放到了一个数组中。
    '''
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    execute(['scrapy', 'crawl', 'book'])