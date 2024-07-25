# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 09:16:03 2024

@author: gsrav
"""


# n1=7823
# n2=5489
# n3=1384
# sum of all min digits
# sum of all max digits
# and find the difference


#            'without using built in functions'
# n1=7823
# n2=5489
# n3=1384
#n1=str(n1)
# n2=str(n2)
# n3=str(n3)
# print(min(n1),min(n2),min(n3))
# sum1=int(min(n1))+int(min(n2))+int(min(n3))
# print(sum1)
# print(max(n1),max(n2),max(n3))
# sum2=int(max(n1))+int(max(n2))+int(max(n3))
# print(sum2)
# res=sum2-sum1
# print(res)


n1=6521
n2=9078
n3=2486
max_sum=0
min_sum=0
def  min_check(n):
    s=str(n)
    min=int(s[0])
    for i in s:
        if int(i)<min:
            min=int(i) 
    return min
            
def  max_check(n):
    s=str(n)
    max=int(s[0])
    for i in s:
        if int(i)>max:
            max=int(i)
    return max
min_sum=min_check(n1)+min_check(n2)+min_check(n3)
max_sum=max_check(n1)+max_check(n2)+max_check(n3)   
diff=abs(min_sum-max_sum)         #abs is used to print the result positive
print(diff)   
        
            
        



   
        
    
