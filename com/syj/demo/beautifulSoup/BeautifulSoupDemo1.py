# coding=utf-8
from bs4 import BeautifulSoup
import re

soup = BeautifulSoup(open('/home/syj/桌面/parseDemo.html'))

# 搜索文档树,find_all(name, attrs, recursive, text, **kwargs)
# name 参数,在搜索方法中传入一个字符串参数,BeautifulSoup会查找与该字符串 完整匹配 的内容
for tag in soup.find_all('li'):
    print '-------------name 参数,查找指定的标签'
    print tag

# 传入正则表达式作为参数,BeautifulSoup 会通过正则表达式的match()来匹配内容
for tag in soup.find_all(re.compile("^b")):
    print '-------------查找所有以b开头的标签'
    print tag

# 传入列表参数,BeautifulSoup会将与列表中任一元素匹配的内容返回
for tag in soup.find_all(["head", "title"]):
    print '-------------查找文档中所有的header标签,和title标签'
    print tag

# 传入的参数是true,则可以匹配任何标签,但是不会匹配字符串节点
for tag in soup.find_all(True):
    print 'true-------------查找所有的节点'
    print tag

# kwargs参数.如果一个指定名字的参数不是搜索内置的参数名,搜索时会把该参数当做指定名字Tag的属性来搜索
# 搜索包含id参数,且值为link2的标签
for tag in soup.find_all(id='J_service'):
    print '=================kwargs 搜索指定tag的属性'
    print tag

# 如果传入href参数,BeaSoup会搜索每个Tag的href属性
for tag in soup.find_all(href=re.compile("jipiao")):
    print '=====================查找href属性中含有jipiao的标签'
    print tag

# 查找所有包含id属性的Tag标签
for tag in soup.find_all(id=True):
    print '=====================查找所有包含id属性的标签'
    print tag

# 使用class来过滤
for tag in soup.find_all("li", class_="service_item"):
    print '====================查找包含属性service_item的li标签'
    print tag

# 使用多个指定名字的参数可用同时过滤Tag的多个属性
for tag in soup.find_all(href=re.compile("jd\.com"), class_="service_lk"):
    print '====================查找href包含jd.com,且class属性包含service_lk的Tag标签'
    print tag