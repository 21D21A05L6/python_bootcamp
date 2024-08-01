# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 13:54:04 2024

@author: gsrav
"""
def check(s):
    s=s.split()
    s=list(reversed(s))
    for i in s:
        rev=i[::-1]
        print(rev,end=' ')
s='sridevi womens engineering college'
check(s)


#without using functions
#s=input()
#for i in range(len(s)-1,-1,-1):
 #   print(s[i],end='') 