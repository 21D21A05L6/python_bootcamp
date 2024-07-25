# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 15:32:34 2024

@author: gsrav
"""

try:
    arr=[1,7,8,12,36]
    print(arr[4])
except IndexError:
    print('cannot access index value')
else:
    print('no exception occured')
finally:
    print('finally wednesday is a last day of task')