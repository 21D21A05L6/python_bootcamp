# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 13:26:02 2024

@author: gsrav
"""

# Encapsulation:
#     binding data and methods into the single component is called encapsulation.
#     example:
#         class is the best example of encapsulate:
            # why?
            # adv:
            #     security
            #     code integration
                
            #     access modifiers:
            #         public,private,protected
class Employee:
    def __init__(self,name,role,salary):
        self.name=name
        self.role=role
        self.__salary=salary     #private data
    def get_salary(self):        #public method
        return self.__salary
    def Empdisplay(self):
        print(self.name,self.role)   #public method
class Company(Employee):
    def __init__(self,cname,loc):
        self.cname=cname
        self.loc=loc
    def  Comdisplay(self):
        print(self.cname,self.loc)
    def _hiring(self):
        print('hiring for the manager role')
cobj=Company('wipro','gachibowli')
eobj=Employee('sravani', 'sham',85000)
eobj.Empdisplay()
print(cobj._hiring ())
    
        
        

                   
                