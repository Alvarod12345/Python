# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 23:48:15 2019

@author: New
"""

"""
Python is easy: Homework assignment #6
Advanced Loops
"""

# for the maximum width(columns) and maximum height(rows) that my playing board can take 
# This was achieved by trial and error

# Defining the function which takes two inputs - rows and columns

def playingBoard(rows,columns):
    if rows<=15 and columns<=15:     #declaring the number of rows and columns
        for r in range(1,rows):      #loop for the rows
            if r % 2 == 0:           #checking the rows if it is even or not
                for c in range(1,columns):     #loop for the columns
                    if c % 2 == 1:             #checking the columns for odd
                        print(" ",end=" ")     #printing for even row and odd column
                    else:
                        print("$$",end=" ")    #printing for even row and even column
            else:
                for c in range(1,columns):
                    if c % 2 == 1:
                        print("$$",end=" ")    #printing for odd row and odd column
                    else:
                        print(" ",end=" ")     #printing for odd row and even column
            print(" ")
        return True
    else:
        return False

op = playingBoard(6,8)          #calling the function and passing the value

if op == True:
    print("True : playing board is created successfully")
else:
    print("False : number of rows and columns exceeds the limit")
    
print(" ")    
print("check maximum width and height of playing board")
print(" ")
    
op = playingBoard(11,14)      #calling the function and passing the value

if op == True:
    print("True : playing board is created successfully")
else:
    print("False : number of rows and columns exceeds the limit")
    
print(" ")    
print("check maximum width and height of playing board")
print(" ")    
    
op = playingBoard(16,18)       #calling the function and passing the value

if op == True:
    print("True : playing board is created successfully")
else:
    print("False : number of rows and columns exceeds the limit")    
    
    
                    
                        
                            