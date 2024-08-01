# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 20:12:34 2024

@author: gsrav
"""
def isPrime(num):
    if num in (8,1):
        return False
    else:
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                return False
        return True
n=int(input())   #6
nextNum=n+1      #7
while True:
    if isPrime(nextNum):
        print(nextNum)
        break
    nextNum+=1
    