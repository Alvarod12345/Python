# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 23:29:05 2019

@author: New
"""

"""
Python is easy:Homework assignment #5
fizzbuzz and prime
"""
#creating a function for prime numbers
def isprime(N):
    for n in range(2, N):     #we need numbers from 2 to N-1
        if N % n == 0 and N % 1 == 0:     #to check whether the number is prime or not
            return False               #if not a prime number
        
    return True

#loop through all the numbers between 1 to 100
for n in range(1, 101):
             
    if n % 3 == 0 and n % 5 == 0:    #to check if number is divisible by 3 or 5
        print("FizzBuzz")
    
    elif n % 3 == 0:         #to check if number is divisible by 3
        print("Fizz")
        
    elif n % 5 == 0:        #to check if number is divisible by 5
        print("Buzz")
        
    elif n % 3 == 0 and n % 5 == 0:    #to check if number is divisible by 3 or 5
        print("FizzBuzz")
    
    elif (isprime(n)):        #to check a number is prime or not
        print("Prime")
    else:
        print(n)    #print the numbers between 1 to 100
  
   