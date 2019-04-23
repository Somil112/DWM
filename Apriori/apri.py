# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 17:53:25 2019

@author: Somil
"""
import pandas as pd
from collections import Counter
import itertools

# Import Dataset
dataset = pd.read_csv('apr.csv')

# Enter the support required
support = int(input("Input Support: "))

#Seperate trainsactions and itemsets
transaction = dataset.iloc[:,[0]].values.flatten().tolist()
itemsets = dataset.iloc[:,[1]].values

#List to count the count of each item
countcheck = []
temp = []

for i in range(len(itemsets)):
    templist = itemsets[i][0].split(',')
    for item in templist:
        print(item)
        countcheck.append(item)        
    temp.append(templist)

#Actual itemsets
itemsets = temp

Cn = dict(Counter(countcheck))
Ln = dict()
temptransac = []

for key,value in Cn.items():
    if(value>=support):
        Ln[key] = value
        temptransac.append(key)
        
temptransac = list(set(list(np.asarray(temptransac).flatten())))      
newlist = list(itertools.combinations(temptransac,2))


combcount = 3
flag = 0
while flag!=1:
    Lntemp = Ln
    Cn = dict()
    Ln = dict()
    for i in range(len(newlist)):
        count = 0
        for j in range(len(itemsets)):
            if(all(x in itemsets[j] for x in newlist[i])):
                count += 1
                
        Cn[newlist[i]] = count
    temptransac = []
    for key,value in Cn.items():
        if(value>=support):
            Ln[key] = value
            temptransac.append(key)
    print(Ln)
    if bool(Ln) == False:
        flag = 1
    print(temptransac)
    temptransac = list(set(list(np.asarray(temptransac).flatten())))    
    newlist = list(itertools.combinations(temptransac,combcount))
    combcount += 1
    


        

        


