# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 09:52:40 2024

@author: gsrav
"""

s=7
t=11
a=3
b=15
apples=[6,5,-4]
oranges=[9,8,-4]
acount=0
ocount=0
for i in apples:
#     if a+i in range(s,t+1):   #checks from 7 to 11
#         acount+=1
# for i in oranges:
#     if b+i in range(s,t+1):
#         ocount+=1
# print(acount,ocount)
      if a+i>=7 and a+i<=11:
          acount+=1
for i in oranges:
      if b+i>=7 and b+i<=11:
          ocount+=1
print(acount,ocount) 
        
    
        
