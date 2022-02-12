# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 12:43:40 2020

@author: Lenovo
"""
'''import pandas as pd
import numpy as np
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
'''

def isBigGrowth(L,rate):
    result = True
    for i in range(1,len(L)):
        r = (L[i]-L[i-1])/L[i-1]
        if r < rate:
            result = False
            break
    return result
print("手机公司\t是否快速增长？")
