# coding=utf-8
'''
    设置代理和超时时间
'''
import urllib2

try:
    proxy = urllib2.ProxyHandler({'http': '127.0.0.1:8087'})
    opener = urllib2.build_opener(proxy,)
    response = opener.open('http://www.google.com', timeout=3)
#    response = urllib2.urlopen('http://www.google.com', timeout=1)
    html = response.read()
    print html
except urllib2.HTTPError as e:
    print e
    if hasattr(e, 'code'):
        print 'Error code:', e.code
except Exception as e1:
    print e1