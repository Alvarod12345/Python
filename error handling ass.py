# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 23:42:34 2019

@author: Ankur Singh
"""

"""
Python is easy : Homework assignment #11
error handling
"""

#using try,except and finally to handle the errors in a fizzbuzz assignment



#function for checking if number is prime or not prime
def isprime(N):
    try:
        for n in range(100):
            if N % n == 0 and N % 1 == 0:
                return False 
        return True
    
    except Exception as e:
        print(e)
    
    finally:
        for n in range(2,N):
            if N % n == 0 and N % 1 == 0:
                return False
        return True    
   
#loop through all the numbers between 1 to 100
for n in range(1, 101):
    print(n)      #print all the numbers between 1 to 100
   
    if n % 3 == 0:         #to check if number is divisible by 3
        print("Fizz")
       
    if n % 5 == 0:        #to check if number is divisible by 5
        print("Buzz")
        
    if n % 3 == 0 and n % 5 == 0:    #to check if number is divisible by 3 or 5
        print("FizzBuzz")
        
    if (isprime(n)):        #to check a number is prime or not
        print("Prime")    
            
    
isprime(n)     
isprime(10)   