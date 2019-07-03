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

# 遍历文档树:子节点  .contents和children属性仅仅包含Tag的直接子节点,不会包含跟它并列的兄弟节点
print '遍历文档树:子节点--->contents'
print len(soup.div.contents)
print soup.div.contents
for child in soup.div.contents:
    print '注意:开头和结尾的元素都为空元素--------------------'
    print child

print '遍历文档树:子节点--->children,它返回的是个迭代器'
for child in soup.div.children:
    print child

print '遍历文档树:子孙节点,这个迭代器不断循环迭代,一层层的解析,直到最后一个子孙元素,厉害!!!'
for child in soup.div.descendants:
    print '--------------------开始遍历子孙节点'
    print child

print '遍历文档树:获取节点内容'
print soup.head.string
print soup.title.string
print soup.div.string
for string in soup.div.stripped_strings:
    print '瞅瞅是啥--------'
    print string

print '遍历文档树:获取兄弟节点'
for sibling in soup.div.next_siblings:
    print '看看你的兄弟是啥'
    print sibling