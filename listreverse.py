# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 09:59:10 2024

@author: gsrav
"""

arr=[1,2,3,4,5]
k=3
'''first=arr[k-1:]
second=arr[:k-1]
print(first+second)         op= [4, 5, 6, [1, 2, 3]]'''
   
first=arr[k+1:k-(k-1):-1]    #to print [5, 4, 3, [1, 2]]
second=arr[:k-1]
print(first+second)

