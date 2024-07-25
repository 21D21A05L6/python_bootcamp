# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 10:50:53 2024

@author: gsrav
"""

menu={
      'chicken_biryani':555,
      'butter_chicken':400,
      'tandoori_chicken':555,
      'juicy_mandi':700,
      'juicy_mandi':850
      }
print(menu['juicy_mandi'])
for i in menu.values():#cost
    print(i)
for i in menu.keys(): #dish names
    print(i)
for i in menu.items(): #dishes along with costs
    print(i)
    
