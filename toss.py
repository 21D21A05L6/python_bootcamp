# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 20:57:58 2024

@author: gsrav
"""

s=input()
c=0
for i in range(len(s)):
    if i+2<=len(s)-1:
       if s[i]=="H" and s[i+1]=="H" and s[i+2]=="H":
           c+=6
           print(c)
           exit()
    if s[i]=="H":
          c+=2
    else:
          c-=1
print(c)

