# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 13:49:11 2024

@author: gsrav
"""

# convert time in 12hr format
# time=20:34:55
# 00:00:00
#output=8:34:55
time='24:79:80'  
time=time.split(':')
hrs=time[0]
min=time[1]
sec=time[2]
if int(hrs)>12:
    hrs=int(hrs)-12
if int(min)>59:
    hrs+=1
    min=int(min)-60     #for min greater than 60
if int(sec)>59:
    min+=1
    sec=int(sec)-60     #for sec greater than 60
print(str(hrs)+':'+str(min)+':'+str(sec)) 



