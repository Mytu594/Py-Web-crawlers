import openpyxl
from wordcloud import WordCloud
# 读取数据
wb = openpyxl.load_workbook('data.xlsx')
# 获取工作表
ws = wb['国内义擎']
frequency_in = {}
for row in ws.values:
    if row[0] == '省份':
        pass
    else:
        frequency_in[row[0]] = float(row[1])

frequency_out = {}
sheet_name = wb.sheetnames
for each in sheet_name:
    if "洲" in each:
        ws = wb[each]
        for row in ws.values:
            if row[0] == '国家':
                pass
            else:
                frequency_out[row[0]] = float(row[1])

def generate_pic(frequency,name):
    wordcloud = WordCloud(font_path="C:/Windows/Fonts/SIMLI.TTF",
                          background_color="white",
                          width=1920, height=1080)
    # 根据确诊病例的数目生成词云
    wordcloud.generate_from_frequencies(frequency)
    # 保存词云
    wordcloud.to_file('%s.png'%(name))

generate_pic(frequency_in,'国内义擎情况词云图')
generate_pic(frequency_out,'世界义擎词云图')