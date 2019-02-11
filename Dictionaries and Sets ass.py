# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 20:21:32 2019

@author: New
"""

"""
Python is easy : Homework assignment #7
Dictionaries and Sets
"""

# Creating a dictionary in which keys and values are assigned 

Songdict = {
                "SongName":"There For You" ,
                "Artist":"Martin Garrix, Troye Sivan" ,
                "Genre ":"EDM",
                "Duration": 3.41 ,
                "Lyricist":"Troye Sivan, Jessie Thomas",
                "Released":2017
                } 

# using a loop to print a dictionary with keys and values

for key in Songdict:
    print(key,  ":", Songdict[key])
    


# defining the function that allows someone to guess the value
    
def guessVl(key, value):
    userInpur = str(input("Guess the song's " + key + ":"))
    if userInpur ==str(value):
        return True
    else:
        return False
    
guessKey = "SongName"     #using a key that exist in a dictionary which is created
#guessKey = "Artist"      # can't i use these keys in a seperate "sets" variable?????????????please answer this question??
#guessKey = "Genre "
#guessKey = "Cast"        #using a key that doesn't exist
    

# calling the function to guess any value

if guessKey in Songdict:
    result = guessVl(guessKey , Songdict[guessKey])
else:
    print("wrong input")
    

# checking the input given by the user is correct or not    
    
if result == True:
    print("true : you are right ")
else:
    print("false : it is not in the dictionary")
    
    
    