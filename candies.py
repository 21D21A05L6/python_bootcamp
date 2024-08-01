# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 20:20:21 2024

@author: gsrav
"""

N,K,A=list(map(int,input().split(' ')))
ans=(A+K-1)%N
if ans==0:
    print(N)
else:
    print(ans)