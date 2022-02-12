# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 11:40:47 2020

@author: Administrator
"""

from mpl_toolkits.mplot3d import Axes3d
from matplotlib import cm
from matplotlib.ticker import LinearLocator,FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figur(figsize = (12,9))
ax = fig.gca(projecyion ='3d')
X = np.arange(-4,4,0.25)
Y = np.arange(-4,4,0.25)
X,Y = np.sqrt(X,Y)
R = np.meshgrid(X.Y)
Z = np.sin(R)

surf = ax.plot_surface(X,Y,Z,rstride = 1,cstride = 1,camp = cm.coolwarm,linewidth = 0,antialiased = False)

ax.set_zlim(-1.01,1.01)
ax.zaxis.set_major_locator(LinearLoctator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

fig.colorbar(surf,ahrink = 0.6,aspect = 6)

plt.show()