# -*- coding: utf-8 -*-
"""
P145
"""
import numpy as np
from decimal import Decimal
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

colors = [(31,119,180),(174,199,232),(255,128,0),(255,15,14),(44,160,44),
          (152,232,138),(214,39,40),(255,173,61),(148,103,189),(197,176,213),
          (140,86,75),(196,156,148),(227,119,194),(247,182,210),(127,127,127),
          (199,199,199),(188,189,34),(219,219,141),(23,190,207),(158,218,229)]

for i in range(len(colors)):
    r,g,b = colors[i]
    colors[i] = (r/255.,g/255.,b/255.)
    
def printHeaders(term, extra):
    print("\nExtra-Payment: $"+str(extra)+" Term: "+str(term)+" years")
    print("--------------------------------------------------------")
    print('Pmt no'.rjust(6),' ','Beg. bal.'.ljust(13),' ')
    print('Payment'.ljust(9),' ','Principal'.ljust(9),' ')
    print('Interest'.ljust(9),' ','End. bal.'.ljust(13))
    print(''.rjust(6,'-'),' ',''.ljust(13,'-'),' ')
    print(''.rjust(9,'-'),' ',''.ljust(9,'-'),' ')
    print(''.rjust(9,'-'),' ',''.ljust(13,'-'),' ')
    
def amortization_table(principal,rate,term,extrapayment,printData=False):
    xarr=[]
    begarr=[]
    
    original_loan=principal
    money_saved=0
    total_payment=0
    payment=pmt(principal,rate,term)
    begBal=principal
    
    num=1
    endBal=1
    if printData==True:
        printHeaders(term,extrapayment)
        
    while (num<term+1) and (endBal>0) :
        interest=round(begBal*(rate/(12*100.0)),2)
        applied=extrapayment+round(float(payment)-float(interest),2)
        endBal=round(begBal-applied,2)
        if (((num-1)%12==0) or (endBal<applied+extrapayment)) and endBal>0 :
            begarr.append(begBal)
            xarr.append(num/12)
            if printData==True :
                print('{0:3d}'.format(num).center(6),' ')
                print('{0:,.2f}'.format(begBal).rjust(13),' ')
                print('{0:,.2f}'.format(payment).rjust(9),' ')
                print('{0:,.2f}'.format(applied).rjust(9),' ')
                print('{0:,.2f}'.format(interest).rjust(9),' ')
                print('{0:,.2f}'.format(endBal).rjust(13))
        total_payment+=applied+extrapayment
        num+=1
        if endBal>0:
            begBal=endBal
    if extrapayment>0 :
        money_saved=abs(original_loan-total_payment)
        print('\nTotal Payment:','{0:,.2f}'.format(total_payment).rjust(13))
        print(' Money Saved:','{0:.2f}'.format(money_saved).rjust(13))
    return xarr,begarr,'{0:.2f}'.format(money_saved)
    
def pmt(principal,rate,term):
    ratePerTwelve=rate/(12*100.0)
    result=principal*(ratePerTwelve/(1-(1+ratePerTwelve)**(-term)))
    
    result=Decimal(result)
    result=round(result,2)
    return result
    
plt.figure(figsize=(18,14))

i=0
markers=['o','s','D','^','v','*','p','s','D','o','s','D','^','v','*','p','s','D']
markersize=[8,8,8,12,8,8,8,12,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8]

'''figure = plt.figure(figsize=(20,16))
gs = GridSpec(3,1)
ax1 = plt.subplot(gs[:2,:])
ax2 = plt.subplot(gs[2,:])'''
for extra in range(100,1700,100):
    xv1,bv1,saved1=amortization_table(250000,5,360,extra,False)
    xv2,bv2,saved2=amortization_table(350000,5,360,extra,False)
    xv3,bv3,saved3=amortization_table(450000,5,360,extra,False)
    s1=[]
    s2=[]
    s3=[]
    s1.append(saved1)
    s2.append(saved2)
    s3.append(saved3)
    position = np.arange(1,4)
    w = 0.3   
    if extra==0:
        plt.plot(xv1,bv1,color=colors[i],lw=2.2,label='Principal only',marker=markers[i],markersize=markersize[i])
        #ax1.legend('Principal only')
    else:
        plt.plot(xv1,bv1,color=colors[i],lw=2.2,label='Principal plus\$'+str(extra)+str("/month,Saved:\$")+saved1,marker=markers[i],markersize=markersize[i])
        #ax1.legend('Principal plus\$'+str(extra)+str("/month,Saved:\$")+saved1)
        '''ax2.bar(position-w,height=s1,width=w)
        ax2.bar(position,height=s2,width=w)
        ax2.bar(position+w,height=s3,width=w)
   '''   
   i+=1

    
plt.grid(True)
plt.xlabel('Years',fontsize=18)
plt.ylabel('Mortgage Balance',fontsize=18)
plt.title("Mortgage Loan For $350,000 With Additional Payment Chart",fontsize=20)
plt.legend()
plt.show()

"""
P149
"""

'''import matplotlib.pyplot as plt

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
plt.show()'''
