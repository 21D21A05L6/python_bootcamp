# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 20:27:07 2024

@author: gsrav
"""

s=input()
d={}
for i in s:
    if i in d.keys():
        d[i]+=1
    else:
        d[i]=1
#print(*d.items())
ans=len(s)-max(d.values())
print(ans)