# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 12:01:14 2024

@author: gsrav
"""

n=int(input())
def check(n):
    if n%2==0:  #without using modulus if 1&n==0:
        return "even"
    else:
        return "odd"
print(check(n))
