# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 14:59:45 2024

@author: gsrav
"""

arr=[5,9,12,6,17,3]
def check(ele):
    return ele%2==0              #for odd return ele%2!=0
def increment(arr):
    count=0
    for i in arr:
        if check(i):
            print(i)
            count+=1
    return count
print(increment(arr))   
        
 #for palindrome
'''def check(ele):
    ele=str(ele)
    return ele==ele[::-1]              #for odd return ele%2!=0
def increment(arr):
    count=0
    for ele in arr:
         if check(ele):
             print(ele)
             count+=1
    return count
arr=[21,121,98,1001,76,41]
print(increment(arr))      