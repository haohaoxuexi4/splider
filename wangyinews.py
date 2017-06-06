# _*_ coding: utf-8 _*_
#抓取网易新闻排行榜，每个新闻和对应的连接
#连接：http://news.163.com/rank/



import os
import sys
import urllib2
#import requests
import re

#from lxml import etree

def StringListSave(save_path,filename,slist):
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        path=save_path+"/"+filename+".txt"
        with open(path,"w+")as fp:
            for s in slist:
                fp.write("%s\t\t%s\n" % (s[0].encode('utf-8'),s[1].encode('utf-8')))
class splider:
    def __init__(self,url):
        self.url=url
    
    def start(self):
        print ('start')
        i=0
        mypage=urllib2.urlopen(self.url).read().decode('gbk')
        
        mypage_info=re.findall(r'<div class="titleBar" id=".*?"><h2>(.*?)</h2><div class="more"><a href="(.*?)">.*?</a></div></div>', mypage, re.S)
        
        print mypage_info[2];
        save_path=u"网易新闻抓取"
        filename=str(i)+"_"+u"新闻排行榜"
        StringListSave(save_path,filename,mypage_info)

sp=splider('http://news.163.com/rank/')
sp.start();