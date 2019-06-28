# coding=utf-8
import urllib
import urllib2

url = 'https://passport.jd.com/new/login.aspx?ReturnUrl=https://www.jd.com/'
# 设置header
user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0'
referer='https://www.jd.com'
# post请求
postdata= {'username': '18618224639',
           'password': 'syjjd2015'}
headers={'User-Agent': user_agent, 'Referer': referer}
data = urllib.urlencode(postdata)
req = urllib2.Request(url, data, headers)
# 设置超时时间
response = urllib2.urlopen(req, timeout=2)
html = response.read()
print html