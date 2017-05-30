
import urllib
import urllib2

url='https://www.ricequant.com/login'
user_ageent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
values={'username':'cqc','password':'xxx'}
headers={'User-Agent':user_ageent}
data=urllib.urlencode(values)

request=urllib2.Request(url,data,headers)
response=urllib2.urlopen(request)
page=response.read()
print page