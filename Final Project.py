# -*- coding: utf-8 -*-
"""
Created on Sat July 6 21:49:58 2019

@author: Ankur Singh
"""
import math

ch='y'
while(ch=='y'or ch=='Y'):
    
    #Taking inputs for the type of calculations you need to do
    a=int(input("""Enter your choice:\n                        
    1-General\n
    2-Trigonometric\n
    3-Powers and Logarithms\n"""))
    
    #for general calculations
    if(a==1):                                         
            start = input("""
            Please enter the choice:
            1 - addition
            2 - subtraction
            3 - multiplication
            4 - division
            5 -  square
            6 - square root
            7 - factorial\n""")
                
            #Using loop to take the choices
            if start== "1" or start== "2" or start== "3" or start== "4":
                #Taking inputs
                number1 = int(input("Please enter first number: "))
                number2 =int(input("Please enter second number: "))
                
                if(start=="1"):
                    print("The result is:", number1 + number2)
                elif(start=="2"):
                    print("The result is:", number1 -number2)
                elif(start=="3"):
                    print("The result is:", number1 * number2)
                elif(start=="4"):
                    print("The result is:", number1 / number2)
                    
            elif start== "5" or start== "6":
                number1 = int(input("Please enter number: "))
                if(start== "5"):
                    print("The result is:", number1 * number1)
                elif(start== "6"):
                    print("The result is:", math.sqrt(number1))
                    
            elif(start=="7"):
                number1 = int(input("Please enter number: "))
                try:                                            #Using try and except for error handling
                    print(f"{number1}!=",math.factorial(number1))
                except:
                    print("Wrong input")
                
            else:
                start=input("Wrong choice,enter again:")
            
  #For Trignometric calculations          
    elif(a==2):            
        start = input("""
            Please enter the choice:
            1 - sine
            2 - cosine
            3 - tangent
            4 - arcsin
            5 - arccos
            6 - arctan\n""")
            
        if(start=="1"):
            x=float(input("Enter the angle in degrees:"))
            print(f"sin({x})=",math.sin(math.radians(x)))
            
        elif(start=="2"):
            x=float(input("Enter the angle in degrees:"))
            print(f"cos({x})=",math.cos(math.radians(x)))
            
        elif(start=="3"):
            x=float(input("Enter the angle in degrees:"))
            print(f"tan({x})=",math.tan(math.radians(x)))
            
        elif(start=="4"):
            x=float(input("Enter the no.:"))
            print(f"sin^-1({x})=",math.degrees(math.asin(x)))
            
        elif(start=="5"):
            x=float(input("Enter the no.:"))
            print(f"cos^-1({x})=",math.degrees(math.acos(x)))
            
        elif(start=="6"):
            x=float(input("Enter the no.:"))
            print(f"tan^-1({x})=",math.degrees(math.atan(x)))
        else:
            print("wrong choice")
            
  #For Logarithmic calc.    
    elif(a==3):
        #Choices what to do
        start = input("""
            Please enter the choice:
            1 - log10(x)
            2 - ln(x)
            3 - e^x
            4 - x^y
            5 - 'n'th root of x\n""")
            
        if(start=="1"):
            x=float(input("Enter the no.:"))
            try:
                print(f"log10({x})=",math.log10(x))
            except ValueError as e:
                e=print("the no. must be greater than zero:")
                print(e)
                
        elif(start=="2"):
            x=float(input("Enter the no.:"))
            try:
                print(f"ln({x})=",math.log1p(x-1))
            except ValueError as e:
                e=print("the no. must be greater than zero:")
                print(e)
                
        elif(start=="3"):
            x=float(input("Enter the power:"))
            print(f"e^{x}=",math.exp(x))
            
        elif(start=="4"):
            x=float(input("Enter the base(x):"))
            y=float(input("Enter the exponent(y):"))
            print(f"{x}^{y}=",math.pow(x,y))
            
        elif(start=="5"):
            x=float(input("Enter the base(x):"))
            y=float(input("Enter the root(y):"))
            print(f"{x}^{y}=",math.pow(x,1/y))
        else:
            print("Wrong choice")
            
    ch=str(input("Want to use again?(y/n):"))