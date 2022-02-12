# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
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
