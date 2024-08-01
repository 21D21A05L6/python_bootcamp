# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 11:48:30 2024

@author: gsrav
"""

import random
ran=random.randint(1,10)
print(ran)
chances=1
while  chances<=3:
    guess=int(input('enter the number:'))
    if guess==ran:
        print('congrats')
        break
    else:
        chances+=1
        continue
if chances<=3:
    print('failed try next time')    