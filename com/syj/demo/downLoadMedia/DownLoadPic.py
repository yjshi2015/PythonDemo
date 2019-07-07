# coding=utf-8
import urllib
from bs4 import BeautifulSoup
import requests

def Schedule(blocknum, blocksize, totalsize):
    '''
    :param blocknum: 已下载的数据块
    :param blocksize: 数据块大小
    :param totalsize: 远程文件的大小
    :return:
    '''
    per = 100.0 * blocknum * blocksize / totalsize
    if per > 100:
        per = 100
    print '当前下载进度%d' %per


user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0'
headers = {'User-Agent': user_agent}
response = requests.get('https://www.ivsky.com/tupian/ziranfengguang/', headers=headers)

soup = BeautifulSoup(response.text, 'html.parser', from_encoding='utf-8')
i=0
# 根据标签获取页面内容
for img in soup.find_all('img'):
    # 根据标签中的属性获取属性值
    src = img.get('src')
    # 核心:下载媒体资源
    urllib.urlretrieve('https:'+src, '/home/syj/下载/syj_img'+str(i)+'.jpg', Schedule)
    i += 1