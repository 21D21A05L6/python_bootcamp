# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 10:35:25 2024

@author: gsrav
"""

#TUPLES:
    #tuple_name=(,,,,)

student=(101,'sravani','cse','hyderabad')
student=list(student)    #as we cannot perform any operations on tuple, we are converting tuple into list 
student.append('sridevi')
student[2]='it'
student.insert(3,'d')
print(student)
