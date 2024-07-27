# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 10:15:06 2024

@author: gsrav
"""

# n=2397
# m=3 
#output=592721      if even add   if odd multiply





n=input()
m=3
n=str(n)
for i in n:
        if int(i)%2==0:
            print(int(i)+m,end=' ')
        else:
            print(int(i)*m,end=' ')  
            
            
            
            
            
            
            
            