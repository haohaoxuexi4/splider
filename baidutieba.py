# -*- coding:utf-8 -*-
import urllib
import urllib2
import re

class Tool:
    #去除img 标签，7位长空格
    removeImg=re.compile('<img.*?>| {7}|')
    #删除超链接标签 
    removeAddr=re.compile('<a.*?>|</a>')
    #把换行替换成\n
    replaceLine=re.compile('<tr>|<div>|</div>|</p>')
    #将表格制表<td>替换成\t
    replaceTD=re.compile('<td>')
    #把段落开头换为\n加空两格
    replacePara=re.compile('<p.*?>')
    #将换行符或双行符替换成\n
    replaceBR=re.compile('<br><br>|<br>')
    #将其余标签删除
    removeExtraTag=re.compile('<.*?>')
    def replace(self,x):
        x=re.sub(self.removeImg,"",x)
        x=re.sub(self.removeAddr,"",x)
        x=re.sub(self.replaceLine,"\n",x)
        x=re.sub(self.replaceTD,"\t",x)
        x=re.sub(self.replacePara,"\n   ",x)
        x=re.sub(self.replaceBR,"\n",x)
        x=re.sub(self.removeExtraTag,"",x)
        return x.strip()

class BDTB:
    def __init__(self,baseurl,seeLZ):
        self.baseurl=baseurl
        self.seeLZ='?see_lz'+str(seeLZ)
        self.tool=Tool()
    def getPage(self,pageNum):
        try:
            url=self.baseurl+self.seeLZ+'&pn='+str(pageNum)
            request=urllib2.Request(url)
            response=urllib2.urlopen(request)
            pagecode=response.read().decode('utf-8')
            return pagecode
        except urllib2.URLError,e:
            if hasattr(e,"reason"):
                print u"连接百度贴吧失败",e.reason
                return None
            
    def getTitle(self):
        page=self.getPage(1)
        pattern = re.compile('<h3 class="core_title_txt.*?>(.*?)</h3>',re.S)
        result = re.search(pattern,page)
        if result:
            print result.group(1)
            return result.group(1).strip()
        else:
            print "none"
            return None
    def getPageNum(self):
        page=self.getPage(1)
        pattern=re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>',re.S)
        result=re.search(pattern,page)
        if result:
            print 'pagenum'
            print  result.group(1)
            return result.group(1).strip()
        else:
            return None
    def getContent(self):
        page=self.getPage(1)
        pattern=re.compile('<div id="post_content_.*?>(.*?)</div>',re.S)
        items=re.findall(pattern,page)
        floor=1
        for item in items:
            print floor,u"楼-------------"
            print self.tool.replace(item)
            floor+=1
        #for item in items:
        #print items[1]
baseurl='http://tieba.baidu.com/p/3138733512'
bdtb=BDTB(baseurl,1)
bdtb.getTitle()
bdtb.getPageNum()
bdtb.getContent()