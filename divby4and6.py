# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 13:22:38 2024

@author: gsrav
"""

#arr=[1,36,24,9,12,4,2]
#count how many numbers are divisible by 4 and 6
#count=0
#for i in arr:
 #   if i%4==0 and i%6==0:
  #      count+=1
#print(count)

#passing arr as function parameter
def check(arr1):
    count=0
    for i in arr1:
        if i%4==0 and i%6==0:
            print(i,end=' ')
            count+=1
    return count
arr=[1,36,2,4,12,24,9]
arr1=list(map(int,input().split()))
#taking input from user
print("the count is:",check(arr1))
