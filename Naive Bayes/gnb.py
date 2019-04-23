# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 14:27:08 2019

@author: Somil
"""

"""
This code is only for continuous values.
Check NB.py for discrete ka code.
"""

import pandas as pd
import numpy as np
from collections import Counter


# Converts a n,1 array into a list
def getlist(array):
    return list(array.flatten())

# Calculate the mean
# If you have numpy use np.mean(X)
def calcmean(inplist):
    return sum(inplist)/float(len(inplist))


# Calculate the standard deviation
# If you have numpy, use np.std(X)
def calcsd(mean,inplist):
    sd = 0.0
    tempsum = 0.0
    for i in range(len(inplist)):
        tempsum += np.square(inplist[i] - mean)
    sd = np.sqrt(tempsum/len(inplist))
    return sd

# Formula for gaussian distribution
def gaussian_pred(val,mean,sd):
    temp = (1/(np.sqrt(2*3.14)*sd))*np.exp(-np.square(val-mean)/(2*np.square(sd)))
    return temp
    
    

dataset = pd.read_csv('datasetexp3.csv')

# Sort values as per output
dataset = dataset.sort_values(by=['Output'])
gender = dataset.iloc[:,[1]].values
height = dataset.iloc[:,[2]].values
Y = dataset.iloc[:,[3]].values

# Check function above
gender = getlist(gender)
height = getlist(height)
Y = getlist(Y)

# Counter will give you how many values are there for a particular class
# For example there are 3 rows with 'Medium' height
# Calculate ranges
counteroutput = dict(Counter(Y))
range1 = counteroutput['Medium']
range2 = range1+counteroutput['Short']
range3 = range2+counteroutput['Tall']

medmean = 0.0
shortmean = 0.0
tallmean = 0.0
medsd = 0.0
shortsd = 0.0
tallsd = 0.0

medheight = []
shortheight = []
tallheight = []

medgender = []
shortgender = []
tallgender = []

for i in range(len(dataset)):
    if(i in range(0,range1)):
        medheight.append(height[i])
        medgender.append(gender[i])    
    elif(i in range(range1,range2)):
        shortheight.append(height[i])
        shortgender.append(gender[i])     
    elif(i in range(range2,range3)):
        tallheight.append(height[i])
        tallgender.append(gender[i])
        
medmean = calcmean(medheight)
medsd = calcsd(medmean,medheight)

shortmean = calcmean(shortheight)
shortsd = calcsd(shortmean,shortheight)

tallmean = calcmean(tallheight)
tallsd = calcsd(tallmean,tallheight)

med = dict(Counter(medgender))
tall = dict(Counter(tallgender))
short = dict(Counter(shortgender))


shortpred = gaussian_pred(1.95,shortmean,shortsd)
medpred = gaussian_pred(1.95,medmean,medsd)
tallpred = gaussian_pred(1.95,tallmean,tallsd)





        
    
        
