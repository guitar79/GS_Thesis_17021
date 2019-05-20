'''
# Learn about API authentication here: https://plot.ly/python/getting-started
# Find your api_key here: https://plot.ly/settings/api

'''

# MatPlotlib
import matplotlib.pyplot as plt

# Scientific libraries
import numpy as np
from scipy.optimize import curve_fit

import os
from datetime import datetime

#set varivables for options
debug = False
save_chart = True 
chart_dir_name = 'chart/'

#set for adding log
log_file = 'python_log.txt'
def write_log(log_file, log_str):
    with open(log_file, 'a') as log_f:
        log_f.write(log_str+'\n')
    return print (log_str)

#for checking time
cht_start_time = datetime.now()
def print_working_time():
    working_time = (datetime.now() - cht_start_time) #total days for downloading
    return print('working time ::: %s' % (working_time))
print_working_time()

if save_chart == True :
    if not os.path.exists(chart_dir_name):
        os.makedirs(chart_dir_name)
        write_log(log_file, '{0} ::: {1} is created'.format(datetime.now(), \
                   chart_dir_name))
    else : 
        write_log(log_file, '{0} ::: {1} is already exist'.format(datetime.now(), \
                   chart_dir_name))

def exponenial_func(x, a, b, c, d, e, f):
        return a+b*np.exp(-(x-f)/c)+d*np.exp(-(x-f)/e)
    
#list for drawing chart
f_names = ['pt1.txt', 'pt2.txt', 'pt3.txt', 'pt4.txt', 'pt5.txt', 'pt6.txt', 'pt7.txt', 'pt8.txt']

#processing each files
for f_name in f_names :
    
    #making empty list for plotting
    x, y=[], []
    #open data file
    with open(f_name) as f:
        lineList = f.readlines()    
    for i in range(len(lineList)) :
    #for i in range(5) :
        if i > 2 : 
            xy = lineList[i].split(';')
            x.append(float(xy[0]))
            y.append(float(xy[1][1:-1]))
            
    if debug == True :
        print("x value")
        print(x)
        print("y value")
        print(y)
    #getting index of maximin of y value
    max_iy = y.index(max(y))
    
    #getting index of last y value
    for j in range(len(y)) :
        if y[j] != 0 and y[j+1] == 0 and y[j+2] == 0 and y[j+3] == 0 and j > max_iy:
            last_iy = j
            break
    
    if debug == True :
        print('maximun index of y:', max_iy)
        print('maximun value of y:', max(y))
        
        print('last index of y value:', max_iy)
        print('last value of y:', y[last_iy])
        print(y[max_iy:last_iy])
        
    p00 = (5.18487289e+01, 1.98739841e+04, 8.87326337e-01, 1.94470209e+04, 2.32283572e-01, 2.86684750e+01)
    popt, pcov = curve_fit(exponenial_func, x[max_iy:], y[max_iy:], p0=p00)
    
    xx = np.linspace(0, 50, 1000)
    yy = exponenial_func(xx, *popt)
    
    print('popt :', popt)
    print('pcov :', pcov)
    
    plt.figure(1, figsize = (15,10))
    plt.plot(x, y, 'o', xx, yy, marker='o', linestyle='dashed', linewidth=1, markersize=2)
    #plt.ylim(0, 2000)
    plt.xlim(28, 52)
    plt.ylim(-100, 70000)
    #plt.ylim(0, max(y)+1000)
    plt.title('Exponential Fit', fontsize=16)
    plt.text(45, 2000, 'max_iy : {0}'.format(max_iy), horizontalalignment='left', verticalalignment='center')
    plt.text(30, -5000, 'p00 : {0}'.format(p00), horizontalalignment='left', verticalalignment='center')
    plt.text(30, -8000, 'popt : {0}'.format(popt), horizontalalignment='left', verticalalignment='center')
    if  save_chart == True :
        #plt.savefig('{0}{1}_{2}.pdf'.format(chart_dir_name, f_name[:-4], start_time.strftime("%Y%m%d%H%M%S")))
        plt.savefig('{0}{1}_{2}.png'.format(chart_dir_name, f_name[:-4], cht_start_time.strftime("%Y%m%d%H%M%S")))
        write_log(log_file, '{0} ::: {1}{2}_{3}.png is created'.format(datetime.now(), chart_dir_name, f_name[:-4], cht_start_time.strftime("%Y%m%d%H%M%S")))
    with open('{0}{1}_{2}.txt'.format(chart_dir_name, f_name[:-4], cht_start_time.strftime("%Y%m%d%H%M%S")), 'w') as result_f:
        result = 'maximun index of y: {0}\n'.format(max_iy)
        result += 'maximun value of y: {0}\n'.format(max(y))
        result += 'last index of y value: {0}\n'.format(last_iy)
        result += 'last value of y: {0}\n'.format(y[last_iy])
        result += 'p00 : {0}\n'.format(p00)
        result += 'popt : {0}\n'.format(popt)
        result += 'pcov : {0}\n'.format(pcov)
        result_f.write(result)
    plt.show()