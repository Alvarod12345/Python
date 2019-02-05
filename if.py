# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 18:28:16 2019

@author: New
"""

"""
Python is easy:Homework assignment 3
"if" statement
"""
#creating a function for comparision
def func (x,y,z):
    #if-else statement is used
    if x == y or y == z:
        return True
    elif x == z:
        return True
    else:
        return False
    
#three different parameters are passed and print the result for three different scenarios    
print(func (1,3,3))
print(func (3,3,3))
print(func (1,2,3))

#for extra credit
def func (x,y,z):
# string type values is converted into int type values
    x = int(x)
    y = int(y)
    z = int(z)
    if x == y or y == z:
        return True
    elif x == z:
        return True
    else:
        return False
    
print(func(6,5,"5"))
    
    
    