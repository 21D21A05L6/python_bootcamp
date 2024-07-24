# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 11:56:49 2024

@author: gsrav
"""

cong={
      7:5,
      18:22,
      32:4,
      71:5,
      66:6
      }
bjp={
     7:58,
     18:20,
     32:4,
     71:9,
     66:2
     }
cong_sum=0
bjp_sum=0
for age,votes in cong.items():
    if age>=18:
        cong_sum+=votes
print(cong_sum)


      
      