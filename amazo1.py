# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 18:11:23 2020

@author: Lenovo
"""
import requests
import re
import pandas as pd
def getHTMLText(url):
    try:
        headers = {'user-agent':'Mozilla/5.0(Windows NT 6.1;rv:40.0) Gecko/20100101 Firefox/40.0'}
        r = requests.get(url,headers=headers,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "获取失败"

def parsePage(ilt,html):
    try:
        plt = re.findall(r'<span class="a-offscreen">￥(.*?)</span>',html)
        #print(plt)
        tlt = re.findall(r'<span class="a-size-base-plus a-color-base a-text-normal" dir="auto">(.*?)</span>',html)
        #print(tlt)
        slt = re.findall(r'<span dir="auto">(.*?)</span>',html)
        for j in range(len(plt)):
            price = plt[j]
            #comments = clt[j]
            shop = slt[j]
            title = tlt[j]
            ilt.append([price,shop,title])
    except:
        print("出现错误")

def printGoodsList(ilt,newilt):
    head = ["序号","价格（元）","满减活动","商品描述"]
    count = 0
    #ilt.sort(key = (lambda x:x[1],reverse = True)
    #ilt.sort(key = (lambda x:x[0],reverse = False)
    print(ilt)
    for g in ilt:
        count = count +1
        newilt.append([count,g[0],g[1],g[2]])
        print(newilt)
    df = pd.DataFrame(columns = head,data =newilt)
    df.to_excel(r'D:/amazon.xlsx',encoding ='utf-8',index=False)

def main():
    goods = input("你想查什么:")
    depth = 3
    start_url = 'http://www.amazon.cn/s?k=' + goods + '&act=input'
    infoList = []
    newinfoList=[]
    for i in range(1,depth+1):
        try:
            print('正在爬取第{}页，请稍等'.format(i))
            url = start_url + '&page_index=' + str(i)
            html = getHTMLText(url)
            parsePage(infoList, html)
        except:
            print(2)
            continue
    printGoodsList(infoList,newinfoList)
main()
