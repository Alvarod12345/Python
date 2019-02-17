# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 19:26:56 2019

@author: Ankur Singh
"""
"""
Python is easy : Homework assignment #8
Input and Output
"""

filename = input("Please enter the file name: ")                #Ask a user for a filename

if filename == "aks.txt":                                       #check if filename matches or not
     action = input("For reading:r  For writing:w  For append:a ")       #input for action what user want to do
    
     if action == "r":                                              #for reading
         wanttofile = open("filename",action)
         TheWholeFile = wanttofile.read()
         print(TheWholeFile)
         wanttofile.close()
       
     elif action == "w":                                            #for writing
         wanttofile = open("filename",action)
         text = input("Enter the text to write in a file: ")
         wanttofile.write(text)
         wanttofile.close()
      
     elif action == "a":                                           #for appending
         wanttofile = open("filename",action)
         text = input("Enter the text to append in a file: ")
         wanttofile.write(text)
         wanttofile.close()
         
        
else:                                                             #If filename doesn't exist
     text = input("Add a text to a file: ")                       
     wanttofile = open("filename", "w")
     wanttofile.write(text)
     wanttofile = open("filename", "r")
     print(wanttofile.read())
     wanttofile.close()
    








