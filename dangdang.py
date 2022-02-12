import requests
import re
import pandas as pd
def getHTMLText(url):
    try:
        headers = {'user-agent':'Mozilla/5.0(Windows NT 6.1;rv:40.0) Gecko/20100101 Firefox/40.0'}
        r = requests.get(url,headers=headers,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.text)
        return r.text
    except:
        return "获取失败"

def parsePage(ilt,html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
        print(plt)
        #clt = re.finfall(r'q">(.*?)条评论',html)
        #print(clt)
        slt = re.findall(r'\"raw_title\"\:\".*?\"',html)
        print(slt)
        alt = re.findall(r'\"item_loc\"\:\".*?\"',html)
        print(alt)
        33333333
        for j in range(len(plt)):
            price = plt[j]
            #comments = clt[j]
            shop = slt[j]
            address = alt[j]
            ilt.append([price,shop,address])
    except:
        print("出现错误")

def printGoodsList(ilt,newilt):
    head = ["序号","价格（元）","店名","地理位置"]
    count = 0
    #ilt.sort(key = (lambda x:x[1],reverse = True)
    #ilt.sort(key = (lambda x:x[0],reverse = False)
    print(ilt)
    for g in ilt:
        count = count +1
        newilt.append([count,g[0],g[1],g[2]])
        print(newilt)
    df = pd.DataFrame(columns = head,data =newilt)
    df.to_excel(r'D:/taobao.xlsx',encoding ='utf-8',index=False)


def main():
    goods = '书包'
    depth = 3
    start_url = 'https://s.taobao.com/search?q=' + goods
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