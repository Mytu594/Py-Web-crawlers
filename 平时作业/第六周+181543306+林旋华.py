# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 00:09:30 2020

@author: Lenovo
"""
#1.在同一幅图上绘制 [-2π， 2π] 范围内的正弦和余弦曲线。

'''import numpy as np

import matplotlib.pyplot as plt

x=np.linspace(-2*np.pi, 2*np.pi,100)

plt.plot(x,np.sin(x), label='sin(x)')

plt.plot(x,np.cos(x), label='cos(x)')

xlabels = (r'-2$\pi$',  r'$-\pi$', '0', r'$+\pi$',  r'+2$\pi$')     # LaTeX语法

plt.xticks((-2*np.pi, -np.pi,0, np.pi, 2*np.pi), xlabels )  # 修改x轴刻度显示

plt.legend()'''


#2.自行下载一个股票数据文件，用pandas读入数据，绘制某段时间内的收盘价折线图。

'''import pandas as pd

df=pd.read_csv('000002.txt',encoding='utf-8',sep='\s+',parse_dates=['时间'],index_col='时间')

df['收盘'].plot()'''


#3.一张图上分4个子图，分别绘制圆形、正方形、三角形和直线。

'''fig = plt.figure()              # 创建一个Figure对象

ax1 = fig.add_subplot(221)      # 2行x 2列图形的第一个子图

x = np.linspace(-2, 2, 50)      # [-2, 2]之间生成50个x值

y = np.sqrt(4 - x**2)           # 计算半径为2的圆上的点的 y 坐标

ax1.axis('equal')

ax1.plot(x, y,x,-y)

ax2 = fig.add_subplot(222)      # 2行x 2列图形的第二个子图

x=[0,0,2,2,0]               # 正方形，定义5个点，注意首尾点坐标相同

y=[0,2,2,0,0]

ax2.axis('equal')

ax2.plot(x, y)

ax3 = fig.add_subplot(223)      # 第三个子图

x=[0,2,4,0]                     # 三角形，定义4个点，注意首尾点坐标相同

y=[1,2,1,1]

ax3.plot(x, y)

ax4 = fig.add_subplot(224)      # 第四个子图

x=np.arange(5)

ax4.plot(x, 2*x)'''


#4.随机产生一组具有线性关系y= 3*x + 2+a的点坐标，a为-2与2之间的一个随机数，绘制散点图。

'''import numpy as np

import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 20)

y=  3*x + 2 + np.random.rand(len(x))*2   # 计算y值并加入随机干扰值

plt.scatter(x, y)
'''

#5.用数据集 [2,5,8,6] 绘制饼图，要加上百分比，并突显数据项8。

'''lst = [2,5,8,6]

explode = (0, 0, 0.2, 0)  

labels = [str(x) for x in lst]

plt.pie(lst, explode=explode, autopct='%.1f%%', labels=labels)

plt.axis('equal')'''


#6.分别绘制x=[1,2,3]和y=[3,5,8]对应的柱形图，水平条形图，堆积柱形图。x=[1,2,3]
import matplotlib.pyplot as plt

x=[1,2,3]

y=[3,5,8]

plt.bar(x, y)   					# 柱形图

plt.figure()

plt.barh(x, y)  					# 水平条形图

plt.figure()

plt.bar(list('ABC'),x)

plt.bar(list('ABC'), y,  bottom=x)  	# 堆积柱形图, 注意 bottom参数