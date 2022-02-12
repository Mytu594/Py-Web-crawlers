# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 10:58:59 2020

@author: lxh
"""
'''
import csv
import matplotlib.pyplot as plt

fig = plt.figure(figsize = (15,13))
plt.ylim(740,1128)
plt.xlim(1965,2011)

with open('mortality1.csv') as csvfile:
    mordata = [row for row in csv.DictReader(csvfile)]

x = []
males_y = []
females_y = []
every_y = []
yrval = 1968
for row in mordata:
    x += [yrval]
    males_y += [float(row['Males'])]   #将其转换为浮点数
    females_y += [float(row['Females'])]
    every_y += [float(row['Everyone'])]
    yrval = yrval + 1


plt.plot(x, males_y, color = '#1a61c3', label = 'Males', linewidth = 1.8)
plt.plot(x, females_y, color ='#bc108d', label = 'Females', linewidth = 1.8)
plt.plot(x, every_y, color = '#747e8a', label = 'Everyone', linewidth = 1.8)
plt.legend(loc = 0, prop = {'size' : 10})
plt.show()
'''

import csv
import matplotlib.pyplot as plt

fig = plt.figure(figsize = (15,13))
plt.ylim(35,102)
plt.xlim(1965,2015)

colorsdata = ['#168cf8', '#ff0000', '#009f00', '#1d437c', '#eb912b', '#8663ec', '#38762b']
labeldata = ['Below 25', '25-44', '45-54', '55-64', '65-74', '75-84', 'Over 85']
with open('mortality2.csv') as csvfile:
    mortdata = [row for row in csv.reader(csvfile)]

x = []
for row in mortdata:
    yrval = int(row[0])
    if (yrval == 1969):
        y = [[row[1]], [row[2]], [row[3]], [row[4]], [row[5]], [row[6]], [row[7]]]
    else:
        for col in range(0,7):
            y[col] += [row[col + 1]]
    x += [yrval]

for col in range(0,7):
    if (col == 1):
        plt.plot(x, y[col], color = colorsdata[col], label = labeldata[col], linewidth = 3.8)
    else:
        plt.plot(x, y[col], color = colorsdata[col], label = labeldata[col], linewidth = 2)

plt.legend(loc = 0, prop = {'size' : 10})
plt.show()