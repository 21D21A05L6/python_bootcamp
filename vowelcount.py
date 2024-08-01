# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 10:59:56 2024

@author: gsrav
"""

s='umer'
vowels=['a','e','i','o','u']
count=0
for c in s:
    if c in vowels:
        count+=1
print(count)