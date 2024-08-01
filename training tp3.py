# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 20:44:03 2024

@author: gsrav
"""

def gcd(a,b):
    while b:
        
        a,b=b,a%b
    return a
def lcm(a,b):
    return a*b//gcd(a,b)
a,b=list(map(int,input().split(' ')))
print(gcd(a,b))
print(lcm(a,b))