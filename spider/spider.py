# !/usr/bin/python
# -*- coding: utf-8 -*-
from celery_config import app
import re
import requests
import urllib

@app.task
#获取页面URL
def getPageUrl():
    urllist = []
    for i in range(1,140):
        url = "http://www.umei.cc/p/gaoqing/rihan/"+str(i)+".htm"
        urllist.append(url)
    return urllist
@app.task
#获取图片集URL
def getUrl(html):
    reg = r'/p/gaoqing/rihan/2016.*?\.htm'
    urlre = re.compile(reg)  
    urllist = urlre.findall(html)  
    urllist = set(urllist)                                  #去重
    return urllist
@app.task
#从HTML匹配获取图片
def getImg(html):  
    reg = r'http://i1.umei.cc.*?\.jpg'  
    imgre = re.compile(reg)  
    imglist = imgre.findall(html)  
    imglist = set(imglist)#去重
    return imglist
