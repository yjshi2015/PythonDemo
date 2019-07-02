# coding=utf-8
import bs4
from bs4 import BeautifulSoup

soup = BeautifulSoup(open('/home/syj/桌面/parseDemo.html'))

# 格式化输出
#print soup.prettify()

# 对象种类,Tag标签,如下:
# 利用这种方式,查找的是所有内容中第一个符合要求的标记
print soup.title
print soup.a
print soup.li
# 获取标签的名字
print soup.a.name
# 修改标签的名字
soup.a.name = 'my_a_tag'
print soup.my_a_tag
# 获取标签的属性
print soup.div.attrs

# 对象种类,NavigableString,即Tag中的字符串
print soup.title.string
print type(soup.title.string)

# 对象种类,Comment,即注释
print soup.span.string
print type(soup.span.string)