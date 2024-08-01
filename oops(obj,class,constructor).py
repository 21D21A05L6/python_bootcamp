# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 09:21:21 2024

@author: gsrav
"""

# OOPS

# ------------------------
# CLASS=BLUPRINT OF AN OBJECT,AND IT IS LOGICAL ENTITY.IT CONTAINS FUNCTIONS,CONSTRUCTORS,DATA.
# OBJ=REAL WORLD ENTITY.OBJ IS INSTANCE OF CLASS(copy).IT IS SUBPART OF CLASS.OBJ CONTAINS PROPERTIES,BEHAVIOUR(fun),IDENTITY.
#CONSTRUCTOR=IT IS A SPECIAL METHOD WHICH IS USED TO INVOKE INSTANCE VARIABLES(obj var).IT DOESN'T RETURN ANY VALUE.WHILE CREATING AN OBJECT CONSTRUCTOR WILL CALL IMPLICITLY.THERE ARE THREE TYPES OF CONSTRUCTORS. THEY ARE default,parameterized,not parameterized.
# ABSTRACTION=HIDING THE IMPLIMENTATION DETAILS
# ENCAPSULATION
# INHERITANCE
# POLYMORPHISM

# STATIC IS USED FOR MEMORY MANAGEMENT

'''
# class Student:
#     branch='CSE'
#     def __init__(self,name,roll,address,email):
#         self.name=name
#         self.roll=roll
#         #self.branch=branch
#         self.address=address
#         self.email=email
#     def display(self):
#         print('Name is:',self.name)
#         print('Roll is:',self.roll)
#         print('Branch is:',self.branch)
#         print('Address is:',self.address)
#         print('Email is:',self.email)
# s1=Student('Sravani',101,'HYD','sravanigoud5@gmail.com')
# s2=Student('Srivani',102,'WGL','srivanigoud5@gmail.com')
# s1.display()
# s2.display()
'''


class Employee:
    company='Tata'
    def __init__(self,name,id,address,email):
        self.name=name
        self.id=id
        #self.branch=branch
        self.address=address
        self.email=email
    def __str__(self):
        return f'{self.name} {self.id} {Employee.company} {self.address} {self.email}'
s1=Employee('Sravani',101,'HYD','sravanigoud5@gmail.com')
s2=Employee('Srivani',102,'WGL','srivanigoud5@gmail.com')
print(s1)
print(s2)





        
    