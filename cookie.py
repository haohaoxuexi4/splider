
import urllib2
import cookielib

cookie=cookielib.CookieJar()
hander=urllib2.HTTPCookieProcessor(cookie)

opener=urllib2.build_opener(hander)
response=opener.open('http://www.baidu.com')
for item in cookie:
    print 'name'+item.name
    print 'value'+item.value
