# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 14:31:17 2024

@author: gsrav
"""

s='{[()]}'


class StackExample:
    def __init__(self):
        self.stack=[]
    def push(self,data):
        self.stack.append(data)
    def is_empty(self):
        return self.stack==()
    def pop(self):
        if not self.is_empty():
            self.stack.pop()
        else:
            print('stack underflow')
    def display(self):
        if not self.is_empty():
            for top in range(len(self.stack)-1,-1,-1):
                print(self.stack[top])
        else:
            print('stack is empty')
    def peek(self):
        if not self.is_empty():
            print('the peek ele:',self.stack[-1])
        else:
            print('stack is empty')
obj=StackExample()
obj.push(10)
obj.push(20)
obj.push(30)
obj.peek()
obj.pop()
obj.pop()
obj.push(44)
obj.display()
    
        
        
        
    