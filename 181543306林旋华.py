import time
import requests
# 爬取网页时直接出现403，意思是没有访问权限
from bs4 import BeautifulSoup
import json
# 入口网页
import xlwt

url = 'http://chs.meituan.com/'

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Proxy-Connection': 'keep-alive',
    'Host': 'chs.meituan.com',
    'Referer': 'http://chs.meituan.com/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    'Content-Type': 'text/html;charset=utf-8',
    'Cookie': '_lxsdk_cuid=164c9bed44ac8-0bf488e0cbc5d9-5b193413-1fa400-164c9bed44bc8; __mta=248363576.1532393090021.1532393090021.1532393090021.1; rvct=70%2C1; ci=70; iuuid=30CB504DBAC7CCDD72645E3809496C48229D8143D427C01A5532A4DDB0D42388; cityname=%E9%95%BF%E6%B2%99; _lxsdk=30CB504DBAC7CCDD72645E3809496C48229D8143D427C01A5532A4DDB0D42388; _ga=GA1.2.1889738019.1532505689; uuid=2b2adb1787947dbe0888.1534733150.0.0.0; oc=d4TCN9aIiRPd6Py96Y94AGxfsjATZHPGsCDua9-Z_NQHsXDcp6WlG2x7iJpYzpSLttNvEucwm_D_SuJ7VRJkLcjqV6Nk8s_q3VyOJw5IsVJ6RJPL3qCgybGW3vxTkMHr9A4yChReTafbZ7f93F1PkCyUeFBQV4D-YXoVoFV5h3o; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; client-id=97664882-24cd-4743-b21c-d25de878708e; lat=28.189822; lng=112.97422; _lxsdk_s=165553df04a-bc8-311-ba7%7C%7C6',
}


# with open(r'美团西安美食.csv',"w", newline='',encoding='UTF-8') as csvfile
# 获取主页源码(获取分类-美食、电影)
# def get_start_links(url):
# html=requests.get(url).text#发送请求获取主页文本
# print html
# soup=BeautifulSoup(html,'lxml')#解析网页
# <span ckass="nav-text-wrapper">==$
# <span>
# <a href="http://chs.meituan.com/meishi/"
# links='http://chs.meituan.com/meishi/
# links=[link.find('span').find('a')['href'] for link in soup.find_all('span',class_='nav-text-wrapper')]
# print links
# return links
# 获取分类链接中间的店铺id
# find:取第一个（返回一个具体的元素，没有为null）find_all:匹配所有（返回列表，没有返回[]）
def get_detail_id(category_url):
    html = requests.get(category_url, headers=headers).text
    # print html
    soup = BeautifulSoup(html, 'lxml')  # 解析网页
    # print soup
    texts = soup.find_all('script')
    # print texts
    text = texts[14].get_text().strip()
    # print text
    text = text[19:-1]

    result1 = json.loads(text, encoding='utf-8')
    # print result1
    result2 = result1['poiLists']
    result3 = result2['poiInfos']
    # print result3
    Info_list = []
    for it in result3:
        # print it
        Info_list.append(it['poiId'])
        # Info_list.append(it['address'])
        # Info_list.append(it['avgScore'])
        # Info_list.append(it['avgPrice'])
    # print  Info_list
    return Info_list


# 获取店铺详情数据
def get_item_info(url):
    # print url
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Proxy-Connection': 'keep-alive',
        'Host': 'chs.meituan.com',
        'Referer': 'http://chs.meituan.com/',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        'Content-Type': 'text/html;charset=utf-8',
        'Cookie': '_lxsdk_cuid=164c9bed44ac8-0bf488e0cbc5d9-5b193413-1fa400-164c9bed44bc8; __mta=248363576.1532393090021.1532393090021.1532393090021.1; rvct=70%2C1; ci=70; iuuid=30CB504DBAC7CCDD72645E3809496C48229D8143D427C01A5532A4DDB0D42388; cityname=%E9%95%BF%E6%B2%99; _lxsdk=30CB504DBAC7CCDD72645E3809496C48229D8143D427C01A5532A4DDB0D42388; _ga=GA1.2.1889738019.1532505689; uuid=2b2adb1787947dbe0888.1534733150.0.0.0; oc=d4TCN9aIiRPd6Py96Y94AGxfsjATZHPGsCDua9-Z_NQHsXDcp6WlG2x7iJpYzpSLttNvEucwm_D_SuJ7VRJkLcjqV6Nk8s_q3VyOJw5IsVJ6RJPL3qCgybGW3vxTkMHr9A4yChReTafbZ7f93F1PkCyUeFBQV4D-YXoVoFV5h3o; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; client-id=97664882-24cd-4743-b21c-d25de878708e; lat=28.189822; lng=112.97422; _lxsdk_s=165553df04a-bc8-311-ba7%7C%7C6',
    }

    html = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html, 'lxml')
    texts = soup.find_all('script')
    # print texts
    text2 = texts[15].get_text().strip()
    # print text2
    text = text2[19:-1]
    result4 = json.loads(text, encoding='utf-8')
    # print result4
    result5 = result4['detailInfo']
    it = result5
    # print result5
    Info_list = []
    Info_list.append(it['name'])
    Info_list.append(it['address'])
    Info_list.append(it['phone'])
    Info_list.append(it['longitude'])
    Info_list.append(it['latitude'])
    print(Info_list)
    return Info_list


# 多页获取商品id
if __name__ == '__main__':
    items_list = []
    new_list = []
    items = []
    # start_url_list=get_start_links(url)
    start_url_list = ['http://chs.meituan.com/meishi/']
    start_url = 'http://chs.meituan.com/meishi/'
    for j in start_url_list:
        for i in range(1, 2):  # 遍历1-11页
            category_url = j + 'pn{}/'.format(i)
            shop_url_list = get_detail_id(category_url)
            # print category_url
            # print shop_id_list
            for shop_id in shop_url_list:
                # total_url=url+'shop/{}'.format(shop_id,headers)
                # print total_url

                # print soup
                items = get_item_info(start_url + '{}/'.format(shop_id))
                items_list = items_list + items
    new_list = [items_list[p:p + 5] for p in range(0, len(items_list), 5)]
    print(new_list)
    new_table = r'D:lin6.csv'
    book = xlwt.Workbook()
    sheet1 = book.add_sheet('sheet1', cell_overwrite_ok=True)
    heads = [u'商家名称', u'商家地址', u'电话', u'经度', u'纬度']
    print(u'\n准备将数据存入表格...')
    ii = 0
    for head in heads:
        sheet1.write(0, ii, head)
        ii += 1
    i = 1
    for list in new_list:
        j = 0
        for data in list:
            sheet1.write(i, j, data)
            j += 1
        i += 1
    book.save(new_table)