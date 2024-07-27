# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 14:32:51 2024

@author: gsrav
"""
# finding n fibonoci series
# n=8
# 0 1 1 2 3 5 8 13
def fib(n):
    if n==0 or n==1:
        return n
    else:
        return fib(n-1)+fib(n-2)
n=4            #n=int(input()) taking value from user
print(fib(n))