# coding=utf-8
import requests

loginUrl = 'https://passport.jd.com/new/login.aspx?ReturnUrl=https://www.jd.com/'
s = requests.Session()
# 首先访问登录页面,作为游客,服务器会先分配一个cookie
r = s.get(loginUrl, allow_redirects=True)
# 设置header
user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0'
referer='https://www.jd.com'
headers={'User-Agent': user_agent, 'Referer': referer}
# post请求
postdata= {'username': '18618224639',
           'password': 'syjjd2015'}
# 向登录链接发送post请求,验证成功,游客权限转为会员权限
r = s.post(loginUrl, headers=headers, data=postdata, allow_redirects=True)
print r.text