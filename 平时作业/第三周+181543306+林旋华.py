#第三周+181543306+林旋华.py
import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def fillUnivList(ulist,strs,html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            print(tds)
            if(tds[2].string.strip()==strs):
                ulist.append([tds[0].string.strip(), tds[1].a.string.strip(), tds[2].string.strip()])
    print(ulist[:])
    
def printUnivList(ulist,num):
    print("{0:^12}\t{1:^12}\t{2:^20}".format("排名","学校名称","省份",chr(12288)))
    for i in range(num):
        u=ulist[i]
        print("{0:^12}\t{1:{3}^10}\t{2:^12}".format(u[0],u[1],u[2],chr(12288)))
    
def main():
    uinfo = []
    url = 'http://www.shanghairanking.cn/rankings/bcur/202011'
    html = getHTMLText(url)
    strs = input("输入: ")
    fillUnivList(uinfo,strs,html)
    printUnivList(uinfo,20) # 20 univs
main()
