# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 10:19:03 2024

@author: gsrav
"""
#    BINARY TO DECIMAL 
# n=101011

# 1*2**0      1
# 1*2**1      2
# 0*2**2      0
# 1*2**3      8
# 0*2**4      0
# 1*2**5      32
            # -----
            #   43
            # -----     
n=int(input())
s=0
i=0
while n>0:
    d=n%10            #to find the remainder
    # s=s+d*i
    # i=i*2
    pro=d*pow(2,i)
    s+=pro
    i+=1
    n=n//10              #not to get float value
print(s)

    
