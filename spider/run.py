# !/usr/bin/python
# -*- coding: utf-8 -*-
from spider import getPageUrl
from spider import getUrl
from spider import getImg
import requests
import threading
import urllib
x = 0
def Run(url):
    html = requests.get(url[0]).text
    urllist = getUrl.delay(html).get()
    for url in urllist:
        url = 'http://umei.cc'+url
        print url
        ImgHtml = requests.get(url).text
        imglist = getImg.delay(ImgHtml).get()
        for imgurl in imglist: 
            print imgurl
            urllib.urlretrieve(imgurl,'/test/%s.jpg' % x)  
            global x
            x += 1
#加入多线程
def main():
    pageurls = getPageUrl.delay().get()
    urlgroup = []
    j = 0
    for i in range(0,len(pageurls)):
        if (j + 1) % 2 == 0:
            urlgroup.append(pageurls[i])
            t = threading.Thread(target=Run,args=(urlgroup,))
            t.start()
            t.join(1)
            urlgroup = []
        else:
            urlgroup.append(pageurls[i])
        j = j + 1

if __name__ == '__main__':
    main()
