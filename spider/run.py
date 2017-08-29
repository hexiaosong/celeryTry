# !/usr/bin/python
# -*- coding: utf-8 -*-
from spider import getPageUrl
from spider import getUrl
from spider import getImg
import requests
import threading
import urllib
x = 0
#run函数
def Run():
    pageurls = getPageUrl.delay().get()
    for i in range(1,len(pageurls)):
        html = requests.get(pageurls[i]).text
        urllist = getUrl.delay(html).get()
        for url in urllist:
            url = 'http://umei.cc'+url
            print url
            ImgHtml = requests.get(url).text
            imglist = getImg.delay(ImgHtml).get()
            for imgurl in imglist: 
                print imgurl
                urllib.urlretrieve(imgurl,'/Users/hexiaosong/github/celeryTry/spider/test/%s.jpg' % x)  
                global x
                x += 1
if __name__ == '__main__':
    Run()
