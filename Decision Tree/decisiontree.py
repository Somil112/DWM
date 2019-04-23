# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 16:13:22 2019

@author: Somil
"""

import pandas as pd
import math
from collections import Counter

dataset=pd.read_csv('dec.csv')

age=dataset["AGE"].tolist()
income=dataset["INCOME"].tolist()
student=dataset["STUDENT"].tolist()
credit=dataset["CREDIT"].tolist()

y=dataset["CLASS"].tolist()
f=["Age","Income","Stud","Credit"]
features=[age,income,student,credit]

ycount = dict(Counter(y))

yc = ycount['Yes']
nc = ycount['No']

        
tot_entropy=0
tot_entrop=-yc/len(y)*math.log(yc/len(y),2)-nc/len(y)*math.log(nc/len(y),2)

print("Total Entropy",tot_entropy)
index=0
d1={}
for i in features:
    
    temp=list(set(i))
    ent=0
   
    for uni in temp:
        yes=0
        count=0
        no=0
        for k in range(len(y)):
            if i[k]==uni and y[k]=="Yes":
                yes+=1
                count+=1
            elif i[k]==uni and y[k]=="No":
                no+=1
                count+=1
        if not no == 0 or yes == 0:
            ent+=(count/len(y))*((-yes/count)*math.log(yes/count,2)-(no/count)*math.log(no/count,2))
    print("Entropy:",ent)
    print("Index",index)
    d1[index]=ent
    index+=1
n=99
res=0
for key,value in d1.items():
    if value<n:
        n=value
        res=key

print(f[res],n)       
    
    