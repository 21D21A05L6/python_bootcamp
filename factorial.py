# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 14:11:01 2024

@author: gsrav
"""

#recursion
#factorial
# n=5
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(fact)

def fact(n):
    if n==0 or n==1:     #for example n=7
        return 1          #if condition is not matching
    else:                
        return n*fact(n-1)   #7*f(6)  if stmt is false
n=int(input())   #in next step 7*6 will be n and (7*6)*f(5) and so on.... until if condition becomes true
print(fact(n))
    