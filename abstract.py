# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 11:17:55 2024

@author: gsrav
"""
from abc import ABC       #abc is a module
class RBIBank(ABC):
    def interest():       #if we are writing a body it is abstract,if we are not writing any body then it is non abstract
        pass
    def loan():
        print('provides home loan')
class HDFC(RBIBank):
    def interest():
         print('7.5% interest')
class SBI(RBIBank):
    def interest():
        print('11% interest')
class AXIS(RBIBank):
    def interest():
        print('10% interest')
aobj=AXIS
aobj.loan()
aobj.interest()

