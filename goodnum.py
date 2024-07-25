# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 14:11:30 2024

@author: gsrav
"""

#Good Numbers:
#------------------------------- 
   
import math
arr=[35,9,1,126]
count=0
for ele in arr:
    low=1
    high=math.ceil(ele**0.3)    
    while low<high:
        res=low**3 + high**3 
        print(ele)
        if res==ele:
            count+=1
        low+=1
print('the count is: ',count)


        
            
    