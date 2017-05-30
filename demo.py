#! usr/bin/python
#coding=utf-8   //这句是使用utf8编码方式方法， 可以单独加入python头使用。
# -*- coding:cp936 -*-
#解析html,

import urllib2
request=urllib2.Request('http://www.baidu.com')
response=urllib2.urlopen(request)
print response.read()
