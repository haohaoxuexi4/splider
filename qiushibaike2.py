# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
import thread
import time

class QSBK:
    def __init__(self):
        self.pageIndex=1
        self.user_agent='Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers={'User-Agent':self.user_agent}
        self.stories=[]
        self.enable=False
    
    #得到某一个网页源码
    def getPage(self,pageIndex):
        try:
            url='http://www.qiushibaike.com/hot/page/'+str(pageIndex)+'?s=4987362'
            request=urllib2.Request(url,headers=self.headers)
            response=urllib2.urlopen(request)
            pagecode=response.read().decode('utf-8')
            return pagecode
        except urllib2.URLError,e:
            if hasattr(e,"reason"):
                print u"连接错误",e.reason
                return None
    #得到不带图片的段子
    def getPageItem(self,pageIndex):
        pagecode=self.getPage(pageIndex)
        if not pagecode:
            print "页面加载失败"
            return None
        pattern=re.compile('<div.*?class="author.*?>.*?<a.*?</a>.*?<a.*?>(.*?)</a>.*?<div.*?class'+
                         '="content".*?title="(.*?)">(.*?)</div>(.*?)<div class="stats.*?class="number">(.*?)</i>',re.S)
        items=re.findall(pattern,pagecode)
        pageStories=[]
        for item in items:
            haveImg=re.search("img",item[3])
            #if not haveImg:
            pageStories.append([item[0].strip(),item[1].strip(),item[2].strip(),item[4].strip()])
            return pageStories
    
    #加载并提取内容，加入列表中
    def loadPage(self):
        if self.enable==True:
            if len(self.stories)<2:
                pageStories=self.getPageItem(self.pageIndex)

                if pageStories:
                    self.stories.append(pageStories)
                    self.pageIndex+=1
    #调用该方法，每次敲回车打印输出一个段子
    def getOneStory(self,pageStories,page):
        for story in pageStories:
            #等待用户输入
            input=raw_input()
            self.loadPage()
            if input=="q":
                self.enable=False
                return
            print u"第%d页\t发布人:%s\t发布时间:%s\n%s\n赞:%s\n" %(page,story[0],story[1],story[2],story[3])

    #开始方法
    def start(self):
        print u"正在读取"
        self.enable=True
        self.loadPage()
        newpage=0
        print len(self.stories)
        while self.enable:
            if len(self.stories)>0:
                pageStories=self.stories[0]
                newpage += 1
                del self.stories[0]
                self.getOneStory(pageStories,newpage)
spider=QSBK()
spider.start()
