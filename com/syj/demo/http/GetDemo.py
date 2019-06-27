import urllib2

response = urllib2.urlopen("https://www.jd.com")
html = response.read()
print html