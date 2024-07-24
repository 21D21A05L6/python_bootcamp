# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 10:39:33 2024

@author: gsrav
"""

from collections import deque
numbers=[1,2,3,4]
numbers=deque(numbers)
numbers.popleft()    #pop from start
print(numbers)
numbers.pop()        #pop from end
print(numbers)