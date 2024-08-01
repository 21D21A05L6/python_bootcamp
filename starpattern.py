# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 11:48:12 2024

@author: gsrav
"""

# *
# **
# ***
# ****
# *****

# n=5
# for i in range(1,n+1):
#     print('*'*i)
    
# *      *
#     *
# *      *   


n=3
for i in range(1,n+1):     #(0,n)
    for j in range(1,n+1):
        if i==j or i+j==n+1:    #i+j==n-1
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()      

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
    



        