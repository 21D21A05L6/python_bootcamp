# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 13:50:09 2024

@author: gsrav
"""

# s='1c0c1c1A0B1'
# A  &
# B  |
# C  ^
# OUTPUT:
# 1
s='1A1B1C0C1B0A1'
res=int(s[0])
for i in range(1,len(s),2):
    if s[i]=='A':
        res=res&int(s[i+1])
    elif s[i]=='B':
        res=res|int(s[i+1])
    elif s[i]=='C':
        res=res^int(s[i+1])
print(res) 

