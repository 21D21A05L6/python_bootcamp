# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 13:33:27 2024

@author: gsrav
"""
# ****
# *  *
# *  *
# ****
n=4
for i in range(1,n+1):     #(0,n)
    if i==1 or i==n:
        print('*'*n)
    else:
        print('*'+' '*(n-2)+'*') 
     