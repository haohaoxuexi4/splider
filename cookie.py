import urllib
import urllib2
import cookielib

filename='cookie.txt'

cookie=cookielib.MozillaCookieJar(filename)
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
postdata=urllib.urlencode({
    'stdid':'5454',
    'pwd':'35445'
})

loginurl='http://www.baidu.com'
#模拟登陆
result=opener.open(loginurl,postdata)
#保存cookie到本地
cookie.save(ignore_discard=True,ignore_expires=True)

#目标url
finalurl='http://www.baidu.com'

result=opener.open(finalurl)
print result.read()
