# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 19:40:13 2019

@author: New
"""
"""
Python is easy:Homework assignment 2
Functions
"""

#creating functions

def SongName():
    name = "There For You"
    return name

def Artist():
    name = "Martin Garrix, Troye Sivan"
    return name

def Genre():
    name = "EDM"
    return name

def Lyricist():
    name = "Troye Sivan,Jessie Thomas"
    return name

def Duration():
    name = 3.41
    return name

#creating boolean function that will return a boolean value: for extra credit
def Boolean(name2):
    name1 = "Martin Garrix"
    Bool = (name1 == name2)
    return Bool

#calling each function
SongName1 = SongName()
ArtistName = Artist()
GenreName = Genre()
LyricistName = Lyricist()
DurationM = Duration()
BooleanV = Boolean("Troye Sivan")

#Printing the data wich we get using "return" in function
print(SongName1)
print(ArtistName)
print(GenreName)
print(LyricistName)
print(DurationM)
print(BooleanV)