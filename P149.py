# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 15:10:13 2020

@author: Administrator
"""

import matplotlib.pyplot as plt

yvals1=[101000,111000,121000,131000,138000,143000,148000,153000,158000]
yvals2=[130000,142000,155000,160000,170000,180000,190000,194000,200000]
yvals3=[125000,139000,157000,171000,183000,194000,205000,212000,220000]
xvals=['500','600','700','800','900','1000','1100','1200','1300']

bubble1=[]
bubble2=[]
bubble3=[]

for i in range(0,9):
    bubble1.append(yvals1[i]/20)
    bubble2.append(yvals2[i]/20)
    bubble3.append(yvals3[i]/20)

fig,ax=plt.subplots(figsize=(10,12))
plt1=ax.scatter(xvals,yvals1,c='#d82730',s=bubble1,alpha=0.5)
plt2=ax.scatter(xvals,yvals2,c='#2077b4',s=bubble2,alpha=0.5)
plt3=ax.scatter(xvals,yvals3,c='#ff8010',s=bubble3,alpha=0.5)

ax.set_xlabel('Extra Dollar Amount',fontsize=16)
ax.set_ylabel('Savings',fontsize=16)
ax.set_title('Mortgage Savings (Paying Extra Every Month)',fontsize=20)

#ax.set_xlim(400,1450)
#ax.set_ylim(90000,230000)

ax.grid(True)
ax.legend((plt1,plt2,plt3),('$250,000 Loan','$350,000 Loan','$450,000 Loan'),scatterpoints=1,loc='upper left',markerscale=0.17,fontsize=10,ncol=1)

fig.tight_layout()
plt.show()