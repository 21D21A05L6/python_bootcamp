# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

n=int(input())
result=n
sum=0
while n>0:
    d=n%10
    sum=sum+d
    n=n//10
print(sum)
d=sum
temp=0
while d>0:
    rem=d%10
    temp=temp*10+rem
    d=d//10
print(temp)

pro=sum*temp
print(pro)
if pro==result:
    print("magical")
else:
    print("not magical")
    
