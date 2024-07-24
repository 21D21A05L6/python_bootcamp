# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 11:31:06 2024

@author: gsrav
"""

candles=[3,7,1,5,4,7]
# print(candles.count(max(candles)))     #count the highest value from candles
max=candles[0]
count=0
for i in candles:
    if i>max:
        max=i
for i in candles:
    if max==i:
        count+=1
print(count) 

