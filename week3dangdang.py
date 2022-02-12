# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#CrowdangdangPrice.py
import requests
import re
import pandas as pd
     
def getHTMLText(url):
    try:
        
        headers={'user-agent':'Mozilla/5.0 (Windows NT 6.1;rv:40.0) Gecko/20100101 Firefox/40.0'}
        r = requests.get(url, headers=headers,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "获取失败"
         
def parsePage(ilt, html):
    try:
        plt = re.findall(r'<span class="a-price-whole">(.*?)</span>',html)
        #print(plt)
        tlt = re.findall(r'<span class="a-size-base-plus a-color-base a-text-normal" dir="auto">(.*?)</span>',html)
        #print(tlt)
        slt = re.findall(r'<span dir="auto">(.*?)</span>',html)
        
        for i in range(len(plt)):
            price = plt[i]
            title = tlt[i]
            shop=slt[i]
            ilt.append([price , shop,title])
    except:
        print("出现错误")
     
def printGoodsList(ilt,newilt):
    head=["序号","价格","店名","商品名称"]
    count = 0
    for g in ilt:
        count = count + 1
        newilt.append([count,g[0],g[1],g[2]])
    df=pd.DataFrame(columns=head,data=newilt)
    df.to_excel(r'f:/dangdang.xlsx',encoding='utf-8',index=False)
             
def main():
    goods = '书包'
    depth = 2
    start_url = 'http://search.dangdang.com/?key=' + goods+'&act=input'
    infoList = []
    newinfoList=[]
    for i in range(1,depth+1):
        try:
            url = start_url + '&page_index=' + str(i)
            html = getHTMLText(url)
            parsePage(infoList, html)
        except:
            continue
    printGoodsList(infoList,newinfoList)
         
main()
