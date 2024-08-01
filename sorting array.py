# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 10:25:01 2024

@author: gsrav
"""

# arr=[1,1,0,1,1,0,0]
# op=0,0,0,1,1,1,1

arr=[1,1,0,1,1,0,0]
ones=[]
zeros=[]
for i in arr:
    if i==0:
        zeros.append(i)
    else:
        ones.append(i)
print(zeros+ones) 

#by using built in function sorted()
# arr=sorted(arr)
# print(arr)
        
