# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 10:00:27 2024

@author: gsrav
"""

# s='abcdz'
# output:
#     bcdea
s='abcdz'
s1=''
for i in s:    
   # print(chr(ord(i)+1))
   if ord(i)>=97 and ord(i)<122:
       s1+=chr(ord(i)+1)
   else:
       s1+=chr(ord(i)-25)
print(s1)

    
 