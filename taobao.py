import requests
import re
import pandas as pd
def getHTMLText(url):
    kv = {'cookie': 'cookie:t=b2452a83b29c8cf1915ce6ee9bd422ca; _m_h5_tk=5845db53e2a00c787f23fdfdc910f7f8_1608625201527; _m_h5_tk_enc=368420e8eb78d694a5af033a027231e0; cna=Syq4Fl/Qgk4CAbcEOwCcbMJk; isg=BPb2H4qXtaAu4ECeNu2v6kD1RCz4FzpRnTwBFmDdmFlSo5Q9yaZkYXwRu__PEDJp; tfstk=cebhBFYaSM-CVAqwkyTCiyVvaKqACjreda7N7NZyHwFheA09Th5c4coq72PMp54iV; l=eBEiSearQIfQLdfoBO5BPurza77TXQA4zkPzaNbMiInca1-FtK5eHNQ2crjySdtfgtfXYeKzvffAydHX8Qzdg2HvCbKrCyCoQYvw-; xlly_s=1; mt=ci=4_1; sgcookie=E100bTCXOdArLDBh5MxKGbfKxhQ3xT1KTideWojmQ%2FVHTh%2FbLVfex4g8ZUr8…CuAMtD9jWd%2BkbTgA%3D&id2=UNk%2FSy%2FBM1g6TQ%3D%3D; lgc=my%5Cu5F92594; uc4=id4=0%40Ug41Su69%2Bx1coZeHy2zh1asLTKu%2F&nk4=0%40DCx7hXSu%2FQp35qjqNqkkmoW5; tracknick=my%5Cu5F92594; _cc_=V32FPkk%2Fhw%3D%3D; enc=VW3%2B%2Bu6y4kmJdk8hT5l07aLWFBZEt7aiULMQZDbQ0ebOdkO9jzyJcY1RZJwzHGb%2BX2Z5ah476O9XSbNhO%2B2Oxw%3D%3D; thw=cn; hng=CN%7Czh-CN%7CCNY%7C156; v=0; _tb_token_=e1f483bbe785e; uc1=cookie14=Uoe0ZeTjfuG2VA%3D%3D; JSESSIONID=0E67AA571418AD1C67B006BA59DA4296; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com',
        'user-agent': 'Mozilla/5.0'}
    try:
        r = requests.get(url, headers=kv, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def parsePage(ilt,html):
    try:
        plt=re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
        slt=re.findall(r'\"view_sales\"\:\".*?\"', html)	#识别销量
        tlt=re.findall(r'\"raw_title\"\:\".*?\"',html)
        blt=re.findall(r'\"item_loc\"\:\".*?\"',html)
        for i in range(len(plt)):
            price=eval(plt[i].split(':')[1])
            sales=eval(slt[i].split(':')[1])
            title=eval(tlt[i].split(':')[1])
            address = eval(tlt[i].split(':')[1])
            ilt.append([price,sales,title,address])
    except:
        print("")

def printGoodList(ilt,newilt):
    head = ["序号", "价格（元）", "店名", "地理位置"]
    count = 0
    tplt="{:4}\t{:8}\t{:9}\t{:16}\t{:20}"
    print(tplt.format("序号","价格","销量","商品名称","地理位置"))
    count=0
    for g in ilt:
        count=count+1
        newilt.append([count, g[0], g[1], g[2],g[3]])
        print(tplt.format(count,g[0],g[1],g[2],g[3]))
    df = pd.DataFrame(columns=head, data=newilt)
    df.to_excel(r'D:/taobao4.xlsx', encoding='utf-8', index=False)

def main():
    goods="圣诞节"
    depth=2
    start_url="https://s.taobao.com/search?q="+goods
    infoList=[]
    newinfoList=[]
    for i in range(depth+1):
        try:
            url=start_url+"&s="+str(44*i)
            html=getHTMLText(url)
            parsePage(infoList,html)
        except:
            continue
    printGoodList(infoList,newinfoList)
main()
