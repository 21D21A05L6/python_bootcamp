# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 14:10:37 2024

@author: gsrav
"""

# POLYMORPHISM:many forms
#     ------------------
#     human being:
#         in college student
#         in theater audience
#         in market customer
#         in sports players
#         in home child
        
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f'{self.name},{self.age}'
class Student(Person):
    def __init__(self,name,age,roll,branch):
        super().__init__(self)
        self.roll=roll
        self.branch=branch
    def __str__(self):
        perdetails=super().__str__(self)
        return f'{self.perdetails},{self.roll},{self.branch}'
class AnnualDay(Student):
    def __init__(self,name,age,roll,branch,program):
        super().__init__(name,age,roll,branch)
        self.program=program
    def __str__(self):
        studetails=super().__str__()
        return f'{studetails},{self.program}'
aobj=AnnualDay('prasana',20,'h0','cse','solo')
print(aobj)
    
        
        

        