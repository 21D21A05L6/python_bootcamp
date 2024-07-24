# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 10:44:49 2024

@author: gsrav
"""

# datatypes,operators,variables
# conditional stmts
# loops
# patterns
# nested loops
# string
# functions
# arrays

# anagram-->all characters of s2 is there in s1

s1='bat'
s2='tab'
#print(sorted(s1))
#print(sorted(s2))
if len(s1)==len(s2)  and sorted(s1)==sorted(s2):
    print('anagram')
else:
    print('not')
        
    