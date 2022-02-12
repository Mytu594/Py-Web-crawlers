# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 23:31:10 2020

@author: Lenovo
"""
'''import pandas as pd
def isBigGrowth(L,rate):
    for index,val in enumerate(L):
        if ((val-L[index-1])/L[index-1])>0.3:
            return "快速"
            continue
        else:
            return "否"
            break
rate=0.3
df = pd.read_csv("smartPhone.txt",encoding="gbk",sep="\s+",index_col=0)
df.astype("float")
df['是否快速增长'] = df.apply(lambda x:isBigGrowth(x,rate),axis=1) 
print(df)'''

'''import pandas as pd
import numpy as np
df = pd.read_csv("smartPhone.txt",encoding="gbk",sep="\s+",index_col=0)
array = np.array(df)
rate = 0.3
rates = []
def isBigGrowth(L,rate):
    for i in range(1,len(L)):
        r = (L[i]-L[i-1])/L[i-1]
        if r > rate:
            rates.append(True)
        else:
            rates.append(False)
        
for L in array:
    L = list(L)
    isBigGrowth(L,rate)
    
rates = [rates[x:x+3] for x in range(len(rates)) if x%3==0]
li=[]
for a in rates:
    a = np.array(a)
    if (a==1).all():
        li.append("快速")
    else:
        li.append("否")
        
ff = pd.DataFrame(columns=["是否快速增长？"],index=df.index,data=li)
ff.index.name="手机公司"
print(ff)'''

import pandas as pd

def isBigGrowth(L,rate):
    li = []
    for i,val in enumerate(L):
        r = (val-L[i-1])/L[i-1]
        if r > rate:
            li.append(True)
            continue
        else:
            li.append(False)
            break
        
def main():
    rate = 0.3
    df = pd.read_csv("smartPhone.txt",encoding="gbk",sep="\s+",index_col=0)
    df.astype("float")
    isBigGrowth(L,rate)
    ff = pd.DataFrame(columns=["是否快速增长？"],index=df.index,data=li)
    print(ff)
    
if __name__ == '__main__':
	main()