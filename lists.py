# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 19:51:29 2019

@author: New
"""

"""
Python is easy:Homework assignment 4
Lists
"""

#creating an empty lists: global variable
myUniqueList = []   #inputs should get added to this list
myLeftovers = []    #rejected inputs to get added to this list: FOR EXTRA CREDIT

#creating a function to add new inputs to lists
def addToGlbl(input):
    #using if-else statement to add new inputs to both the lists and returning true or false
    if input in myUniqueList:   
        myLeftovers.append(input)
        return False
    else:
        myUniqueList.append(input)
        return True

#calling a function and passing a input to it    
ank = addToGlbl(15)
print(myUniqueList)
print(myLeftovers)
print(ank)

print("----------new input----------")

#passing new input
ank = addToGlbl(10)
print(myUniqueList)
print(myLeftovers)
print(ank)

print("----------new input----------")

#passing the same input to get rejected and get added to myLeftover
ank = addToGlbl(15)
print(myUniqueList)
print(myLeftovers)
print(ank)    


print("----------new input----------")
    
#passing new input
ank = addToGlbl(12)
print(myUniqueList)
print(myLeftovers)
print(ank)

print("----------new input----------")

#passing the same input to get rejected and get added to myLeftover
ank = addToGlbl(10)
print(myUniqueList)
print(myLeftovers)
print(ank)