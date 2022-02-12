# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 14:02:05 2020

@author: zxl
"""

import requests
from bs4 import BeautifulSoup
import re
 
def getHTMLText(url, code="utf-8"):
    kv={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
    try:
        r = requests.get(url,headers=kv)
        r.raise_for_status()
        r.encoding = code
        return r.text
    except:
        return ""
 
def getStockl, 'html.parser') 
    li=soup.find('sectioList(lst, stockURL):
    html = getHTMLText(stockURL, "GBK")
    soup = BeautifulSoup(htmn',attrs={'class':'stockTable'})    
    a = li.find_all('a')
    for i in a[:3]:
        try:
            href = i.attrs['href']
            lst.append(re.findall(r"[S][ZH]\d{6}", href)[0])
        except:
            continue
           
def getStockInfo(lst, stockURL, fpath):
    count = 0
    for stock in lst:
        url = stockURL + stock   
        html = getHTMLText(url)
        #print(url)
        try:
            if html=="":
                continue
            infoDict = {}
            soup = BeautifulSoup(html, 'html.parser')
            mc = soup.find('header',attrs={'class':'stock_title'})
            name = mc.find('h1')
            infoDict.update({'股票名称': name.text})

            stockInfo = soup.find('section',attrs={'class':'stock_price clearfix'})             
            keyList = stockInfo.find_all('dt')
            valueList = stockInfo.find_all('dd')
            for i in range(len(keyList)):
                key = keyList[i].text
                val = valueList[i].text
                infoDict[key] = val
            
            if count==0:
                r='w'
            else:
                r='a'
            with open(fpath, r, encoding='utf-8_sig') as f:
                f.write(str(infoDict) + '\n')
                count = count + 1
                print("\r当前进度: {:.2f}%".format(count*100/len(lst)),end="")
        except:
            count = count + 1
            print("\r当前进度: {:.2f}%".format(count*100/len(lst)),end="")
            continue
 
def main():
    stock_list_url = 'https://hq.gucheng.com/gpdmylb.html'
    stock_info_url = 'https://hq.gucheng.com/'
    output_file = 'StockInfo.csv'
    slist=[]
    getStockList(slist, stock_list_url)
    getStockInfo(slist, stock_info_url, output_file)
 
main()

