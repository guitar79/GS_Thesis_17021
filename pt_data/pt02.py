'''
# Learn about API authentication here: https://plot.ly/python/getting-started
# Find your api_key here: https://plot.ly/settings/api

ModuleNotFoundError: No module named 'plotly'
'''

import plotly.plotly as py
import plotly.graph_objs as go

# MatPlotlib
import matplotlib.pyplot as plt
from matplotlib import pylab

# Scientific libraries
import numpy as np
from scipy.optimize import curve_fit

f_names = ['pt1.txt', 'pt2.txt', 'pt3.txt', 'pt4.txt', 'pt5.txt', 'pt6.txt', 'pt7.txt', 'pt8.txt']

f_name = f_names[0]

with open(f_name) as f:
  lineList = f.readlines()

x, y=[], []
for i in range(len(lineList)) :
#for i in range(5) :
    if i > 2 : 
        xy = lineList[i].split(';')
        x.append(float(xy[0]))
        y.append(float(xy[1][1:-1]))
        
print("x value")
print(x)
print("y value")
print(y)

max_iy = y.index(max(y))

print('maximun value of y:', max(y))
print('maximun index of y:', max_iy)
print(y[max_iy:])

def exponenial_func(x, a, b, c, d, e, f):
    return a+b*np.exp(-(x-f)/c)+d*np.exp(-(x-f)/e)

popt, pcov = curve_fit(exponenial_func, x[max_iy:], y[max_iy:], p0=(5.18487289e+01, 1.98739841e+04, 8.87326337e-01, 1.94470209e+04, 2.32283572e-01, 2.86684750e+01))

xx = np.linspace(0, 50, 1000)
yy = exponenial_func(xx, *popt)

print("result1")
print('popt :', popt)
print("result2")
print('pcov :', pcov)

plt.figure(1, figsize = (15,10))
plt.plot(x, y, 'o', xx, yy, marker='o', linestyle='dashed', linewidth=1, markersize=2)
plt.ylim(0, 2000)
#plt.ylim(0, max(y)+1000)
pylab.title('Exponential Fit')

#ax = plt.gca()
#ax.set_axis_bgcolor((0.898, 0.898, 0.898))
#fig = plt.gcf()
#py.plot_mpl(fig, filename='Exponential-Fit-with-matplotlib')