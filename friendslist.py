# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 09:24:28 2024

@author: gsrav
"""

#list: it is a mutable datastructure
#syntax:
   # list_name=[obj1,ob2,obj3....,objn]
'''   
mobiles=['iphone','samsung','oppo']
mobiles.insert(2,'vivo') adding object
mobiles.pop(0)   deleting an object
mobiles.remove('samsung')
print(mobiles)
'''

friends=['swanthana','satya','yamini','loki','vedha','deepthi','ramya']
friends.insert(3,'archana')
print(friends)
friends.pop(5)
print(friends)
friends.remove('swanthana')
print(friends)
friends.append('mamatha')
print(friends)
print(friends[::-1])
print(friends[True])  #print 1 index name
print(friends[not True])
friends.clear()   #empty list
print(friends)
