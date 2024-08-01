# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 19:40:22 2024

@author: gsrav
"""

a=input()
s=input()
total_cost=0
for i in a:
    if i not in s:
        distance=125
        for j in s:
            temp_dist=abs(ord(i)-ord(j))
            if temp_dist<distance:
                distance=temp_dist
        total_cost+=distance
print(total_cost)
        
        