# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 09:29:09 2024

@author: gsrav
"""

# s='hello world hello world good morning good afternoon'
# remove duplicate words
# output:
#     hello world good morning afternoon

s='hello world hello world good morning good afternoon'
s=s.split()
# s1=''                     #without using built in functions
# for i in s:
#     if i not in s1:
#         s1=s1+i+' '
# print(s1)


#by using dictionaries

d={}               
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
s1=''
for k,v in d.items():
    if v>=1:
        s1+=k+' '
print(s1)        