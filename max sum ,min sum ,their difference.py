# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 14:53:44 2024

@author: gsrav
"""

# num=[1,2,3,4,5]

# hide 1 and do sum 14
# hide 2 and do sum 13
# hide 3 and do sum 12
# hide 4 and do sum 11
# hide 5 and do sum 10

# maximum sum=14
# minimum sum=10
# difference =4

num=[1,2,3,4,5]
res=sum(num)
list=[]
for i in num:
    res1=res-i
    list.append(res1)
l1=sorted(list)
print('min_sum',l1[0])
print('max_sum',l1[len(l1)-1])
print(l1[4]-l1[0]) 

    
    
    
    
    
    