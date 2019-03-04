# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 23:54:50 2019

@author: Ankur Singh
"""
"""
Python is easy 
Project #1 : Connect4 # A simple game
"""

"""This is the connect 4 game.
The player choosing the column on the playing board.
The player's piece is dropped from the top into grid.
The pieces fall straight down.
The piece occupying the lowest available space within the column
After that turn is passed to the next player.
The first player formed vertical, horizontal or diagonal line of pieces wins.
"""


PLAYING = "PLAYING"
WAITING = "WAITING"
WINNERX = "XXXX"
WINNERO = "OOOO"

# User Class
class User:
    state = ""
    name = ""
    def __init__(self,name, stateParam):               #declaring class attributes
        self.name = name
        self.state = stateParam

    def userInfo(self):
        return self.name

    def getState(self):
        return self.state
    def setState(self, stateParam):
        self.state = stateParam

#defining function for making the playing board
def printBoard(matrix):
    for num in range(1, 7):
        print(" "+ str(num) +" ", end = " ")
    print()

    for row in range(0, 6):
        for col in range(0, 6):
            print(" "+ str(matrix[row][col]) +" ", end = " ")
        print("")


#defining function for creating the board
def createMatrix(row, column) :
    mat = ["*"] * row
    for i in range(row):
        mat[i] = ["*"] * column
    return mat


#defining function for checking the winnng move
def findMatrixMatched(matrix) :
    winFlg = False                        #if the four matches in row,column or in diagonal it will be changed to true
    rowStrArr = []                        #an empty list is made  
    # get rows check
    for row in range(0, 6):
        str = ""
        for col in range(0, 6):
            str = str + matrix[row][col]
        rowStrArr.append(str)

    for rowStr in rowStrArr:
        if WINNERX in rowStr or WINNERO in rowStr:
            winFlg = True
            break


    # get columns check
    colStrArr = []
    for col in range(0, 6):
        str = ""
        for row in range(0, 6):
            str = str + matrix[row][col]
        colStrArr.append(str)

    for colStr in colStrArr:
        if WINNERX in colStr or WINNERO in colStr :
            winFlg = True
            break

    # get diagonal check
    diagStrArr = [""] * 25
    for col in range(0, 6):
        diagNum = col

        for row in range(0, 6):
            if row + col > 5 :
                break
            if col == 0:
                diagStrArr[diagNum] = diagStrArr[diagNum] + matrix[row][row]  # middle
            else :
                diagStrArr[diagNum] = diagStrArr[diagNum] + matrix[row][row + col]  # upper
                diagStrArr[diagNum + 5] = diagStrArr[diagNum + 5] + matrix[row + col][row]  # lower

    # get diagonal check
    for col in range(0, 6):
        diagNum = col + 12

        for row in range(0,6):
            rowId = 5-row
            if rowId - col < 0 :
                break

            if col == 0:
                diagStrArr[diagNum] = diagStrArr[diagNum] + matrix[row][rowId]  # middle
            else :
                diagStrArr[diagNum] = diagStrArr[diagNum] + matrix[row][rowId - col]  # upper
                diagStrArr[diagNum + 5] = diagStrArr[diagNum + 5] + matrix[row + col][rowId]  # lower


    for diagStr in diagStrArr:
        if WINNERX in diagStr or WINNERO in diagStr:
            winFlg = True
            break

    return winFlg                


#defining function for playing the game
def appConnect():
    userA = User("A" , PLAYING)
    userB = User("B" , WAITING)

    matBoard = createMatrix(6,6)
    printBoard(matBoard)

    turn = 0
    while True:
        user = userA
        if turn % 2 == 0 :
            user = userA
            userA.setState(PLAYING)
            userB.setState(WAITING)
        else :
            user = userB
            userB.setState(PLAYING)
            userA.setState(WAITING)

        print(".................................................. ")
        print("Preference : ", user.userInfo() , " SEQ : ", str(turn + 1))
        print(".................................................. ")

        try:
            print( user.userInfo() , " turn >>>>>......................... ")
            color = str(input("Please select X or O > "))
            if color != 'X' and color != 'O' :
                print("Wrong Entry", color)
                continue

            colNum = int(input("Please Enter column Number >"))
            if colNum > 6 and colNum < 0:
                print("Wrong Entry -> Please Enter 1 - 5 :", colNum)
                continue

            colNum = colNum - 1;                    # column starting from 0
            for row in range(5, -1, -1):
                if matBoard[row][colNum] == "*" :
                    matBoard[row][colNum] = color
                    break;

            turn += 1
        except ValueError:
            print("Invalid Number !! Please try again")

        printBoard(matBoard)
        if findMatrixMatched(matBoard) :
            print(".................................................. ")
            print("User : ", user.userInfo() , " Win the Match by ", str(turn / 2) , " Steps")
            print(".................................................. ")
            break

        if turn >= 20:
            print("You have crossed maximum limits. Please start again.")
            break

if __name__ == "__main__":
   appConnect()