# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 10:58:59 2020

@author: Lenovo
"""
import csv
import matplotlib.pyplot as plt
import datetime as dt

fig = plt.figure(figsize=(15,13))
plt.ylim(740,1128)
plt.xlim(1965,2011)
with open('mortality1.csv') as csvfile:
    mortdata = [row for row in csv.DictReader(csvfile)]
    
x=[]
males_y=[]
females_y=[]
every_y=[]
yrval=1968
for row in mortdata:
    x+=[yrval]
    males_y+=[row['Males']]
    females_y+=[row['Females']]
    every_y+=[row['Everyone']]
    yrval=yrval+1
    
m_y=[row[2] for row in males_y]
m_y=[float[i] for i in m_y]
f_y=[row[2] for row in females_y]
f_y=[float[i] for i in f_y]
e_y=[row[2] for row in every_y]
e_y=[float[i] for i in e_y]

 

plt.plot(x,m_y,color='#1a61c3',label='Males',linewidth=1.8)
plt.plot(x,f_y,color='#bc108d',label='Females',linewidth=1.8)
plt.plot(x,e_y,color='#747e8a',label='Everyone',linewidth=1.8)
plt.legend(loc=0,prop={'size':10})
plt.show()


