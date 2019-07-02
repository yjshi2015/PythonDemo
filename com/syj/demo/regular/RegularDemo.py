# coding=utf-8
'''
    .  匹配除换行符以外的任意字符
    \b 匹配单词的开始或结束
    \d 匹配数字
    \w 匹配字母/数字/下划线或汉子
    \s 匹配任意空白符.包括空格/制表符Tab/换行符/中文全角空格
    ^  匹配字符串的开始
    $  匹配字符串的结束

反义
    \W  匹配任意不是字符/数字/下划线/汉字的字符
    \S  匹配任意不是空白符的字符
    \D  匹配任意非数字的字符
    \B  匹配不是单词开头或者结束的位置
    [^a]  匹配除了a以外的任意字符
    [^abcd]  匹配除了a/b/c/d以外的任意字符

重复
    *   重复0次或更多次
    +   重复1次或更多次
    ?   重复0次或1次
    {n} 重复n次
    {n,} 重复n次或更多次
    {n,m} 重复n到m次

贪婪与懒惰
    *?  重复任意次,但尽可能少
    +?  重复1到更多次,但尽可能少
    ??  重复0或者1次,但尽可能少
    {n,m}? 重复n到m次,但尽可能少重复
    {n,}?  重复n次以上,但尽可能少重复


字符集合
    [abcd] 匹配abcd中的任意一个字符
    [a-z0-9A-Z] 等同于\w,只考虑英文情况

条件分支
    |   使用该符号将不同规则分隔开,从左到右的测试每个条件,如果满足了某个分支,就不会再管其他条件了

分组
    匹配IP ((25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d){3}((25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d))


实例
1. 匹配we are still studying and so busy中所有以s开头的单词,假设还存在s100这样的情况
\bs\w*\b 并且 ^s\d*$

2. hello\d+ 匹配hello后面跟1个或更多数字,例如匹配hello1,hello10等情况

3. ^\d{5,12}$ 匹配5到12个数字的字符串,例如QQ号

4. we\b? 匹配we后面跟0或者1个数字,例如we,we0等情况

5. a\w+b 匹配a12b34b后,会尽可能匹配更多的个数,最后会匹配整个a12b34b
   a\w+?b 匹配的结果则是a12b(启用懒惰模式)
'''

import re
# 将正则表达式编译成pattern对象
pattern = re.compile(r'\d+')

# 使用re.match匹配文本,活动匹配结果,无法匹配时返回None
result1 = re.match(pattern, '182abc')
if result1:
    print result1.group()
else:
    print '匹配失败1'

result2 = re.match(pattern, 'abc182')
if result2:
    print result2.group()
else:
    print '匹配失败2'

# 使用re.search匹配文本,与match方法及其类似,区别在于match函数只从string的开始位置匹配
# search会扫描整个string查找匹配

result3 = re.search(pattern, 'abc182')
if result3:
    print result3.group()
else:
    print '匹配失败3'

# 按照能够匹配的字符串将string分割后返回列表
print re.split(pattern, 'a1b2c3d4')

# 搜索整个string,以列表形式返回能匹配的全部子串
print re.findall(pattern, 'a1b2c3d4')

# 搜索整个string,以迭代器形式返回能匹配的全部match对象
matchiter = re.finditer(pattern, 'a1b2c3d4')
for match in matchiter:
    print match.group()