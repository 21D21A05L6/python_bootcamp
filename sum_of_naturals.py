# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 14:27:06 2024

@author: gsrav
"""

def sum_of_natural(n):
    if n==1:
        return 1
    else:
        return n+sum_of_natural(n-1)
print(sum_of_natural(4))