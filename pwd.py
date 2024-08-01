# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 15:37:49 2024

@author: gsrav
"""

#------------------------------------
#PASSWORD:-----------------
# string
# for loop:
#     if condition:
#         elif
#         else:
#             lcount--------lower case
#             ucount-----------upper case
#             dcount-------------digit count
#             scount-----------special character count

s=input()
ucount,lcount,dcount,scount=0,0,0,0
for c in s:
    if c.isupper():
        ucount+=1
    elif c.islower():
        lcount+=1
    elif c.isdigit():
        dcount+=1
    else:
        scount+=1
if len(s)>8 and ucount>0 and lcount>0 and dcount>0 and scount>0:
    print('valid')
else:
    print('invalid')
    