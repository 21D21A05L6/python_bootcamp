# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 10:39:26 2024

@author: gsrav
"""
#double pointer

arr=[1,2,3,4,5]


# arr=sorted(arr)
# print(arr)

k=6
count=0
first=0
last=len(arr)-1
while first<last:
    if arr[first]+arr[last]==k:
#  sum of two numbers is 6---->1,5  4,2  5,1  4,2
# for i in range(0,len(arr)):                    }
#     for j in range(1,len(arr)):                }------>
time complexity
#         if arr[i]+arr[j]==k:                   }
#             count+=1                           }
        count+=1
        first+=1
        last-=1
    elif arr[first]+arr[last]<k:
        first+=1
    else:
        last-=1    
print(count) 





