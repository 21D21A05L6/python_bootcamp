# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 19:35:24 2024

@author: gsrav
"""

n=int(input())
arr=list(map(int,input().split()))
arr.sort()
a,b=arr[-1],arr[-2]
avg=(a+b)/2
for i in range(n):
     if avg[i]<avg:
         arr[i]==0
print(sum(arr))