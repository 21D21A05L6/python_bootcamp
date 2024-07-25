# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 11:25:52 2024

@author: gsrav
"""

arr=[1,3,6,2,5,3,7,5,1]
count=0
#count the frequency of each number
res={}
for i in arr:
    if i in res:
        res[i]+=1
    else:
        res[i]=1
for num,count in res.items():
    if count==1: #to print unique numbers
    #if count>1:   to print repeated values
        print(num)