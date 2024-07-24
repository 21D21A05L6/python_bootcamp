# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 11:47:25 2024

@author: gsrav
"""

from abc import ABC
class Vehicle(ABC):
    def speed():
        pass
    def milage():
        pass
    def model():
        pass
    def breaks():
        print('stop the vehicle')
class RangeRover(Vehicle):
    def speed():
        print('450 max speed')
    def milage():
        print('120kmph')
    def model():
        print('new model')
fobj=RangeRover
fobj.speed()
fobj.milage()
fobj.model()
fobj.breaks()

