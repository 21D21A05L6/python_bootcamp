# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 15:14:15 2024

@author: gsrav
"""

# errors -> during compile time
try:
    a=10
    b=0
    c=a/b
    print(c)
except Exception:
    print("divide by zero is not possible")
    n1=100
    n2=200
    print(n1+n2)
    a1=1000
    a2=2000
    print(a1+a2)