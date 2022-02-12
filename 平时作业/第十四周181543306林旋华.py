import matplotlib.pyplot as plt
import numpy as np
import numpy.random as npr
import pandas as pd
'''
#军工A

import tushare as ts
ts.get_hist_data('502004',start='2019-12-12',end='2020-12-11').to_csv('E:jungongA.csv',index=False)
'''
data = pd.read_csv('E:jungongA.csv')
print(data['close'].head())
ret = np.log(data['close']/data['close'].shift(1))
ret = ret.dropna()
ret.head
#mu
print(ret.mean())
#sigma
print(ret.std())


days = n = 252#工作日
dt = 1/252


start_price=0.994
mu = 7.831037405838157e-19
sigma = 0.02590912874781305

def Geometic_Brownian_Motion(start_price,n,mu,sigma):
    result=np.zeros(n)
    result[0] = start_price
    for t in range(1,n):
    	e=npr.standard_normal(1)#生成服从正态分布的ε
    	result[t]=result[t-1]*np.exp((mu-0.5*sigma**2)*dt+sigma*e*np.sqrt(dt))
    return result

for run in range(50):
    plt.plot(Geometic_Brownian_Motion(start_price,n,mu,sigma))   
#plt.plot(result)
plt.ylabel("Price")
plt.title('Geometic Brownian Motion(Simulation)')
plt.show()

# Set a large numebr of runs
runs = 10000

# Create an empty matrix to hold the end price data
simulations = np.zeros(runs)

# Set the print options of numpy to only display 0-5 points from an 
# array to suppress output
np.set_printoptions(threshold=5)

for run in range(runs):
    # Set the simulation data point as the last stock price for that run
    simulations[run] = Geometic_Brownian_Motion(start_price,days,mu,sigma)[days-1]

#define q as the 1% empirical qunatile, this basically means that 
# 99% of the values should fall between here
q = np.percentile(simulations, 1)

# plot the distribution of the end prices
plt.hist(simulations,bins=200)

# Using plt.figtext to fill in some additional information onto the plot

# Starting Price
plt.figtext(0.6, 0.8, s="Start price: $%.2f" %start_price)
# Mean ending price
plt.figtext(0.6, 0.7, "Mean final price: $%.2f" % simulations.mean())

# Variance of the price (within 99% confidence interval)
plt.figtext(0.6, 0.6, "VaR(0.99): $%.2f" % (start_price - q,))

# Display 1% quantile
plt.figtext(0.15, 0.6, "q(0.99): $%.2f" % q)

# Plot a line at the 1% quantile result
plt.axvline(x=q, linewidth=4, color='r')

# Title
plt.title(u"Final price distribution for GZMT Stock after %s days" % days,
weight='bold');
plt.show()