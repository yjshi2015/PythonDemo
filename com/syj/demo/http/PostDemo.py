import urllib
import urllib2

url = 'https://passport.jd.com/new/login.aspx?ReturnUrl=https://www.jd.com/'
user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0'
referer='https://www.jd.com'
postdata= {'username': '18618224639',
           'password': 'syjjd2015'}
headers={'User-Agent': user_agent, 'Referer': referer}
data = urllib.urlencode(postdata)
req = urllib2.Request(url, data, headers)
response = urllib2.urlopen(req)
html = response.read()
print html