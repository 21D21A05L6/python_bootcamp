# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 13:29:59 2024

@author: gsrav
"""
#    11
# n1=288
# n2=594 +
# ---------------
#    882
# ---------------
# count the no.of carry?

#output---->2

n1=288
n2=594
carry=0
count=0
while n1>0 and n2>0:
    rem1=n1%10      #8
    rem2=n2%10      #4
    sum=rem1+rem2+carry
    if(sum>9):
        carry=1
        count+=1
    else:
        carry=0
    n1=n1//10
    n2=n2//10
print(count)       
    