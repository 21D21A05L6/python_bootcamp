# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 20:46:22 2024

@author: gsrav
"""
# n=136
# op=1936     1=1^2 ,9=3^2,36=6^2
n=input()
res=''
for i in n:
    cur_num=int(i)
    res+=str(cur_num**2)
print(res)
