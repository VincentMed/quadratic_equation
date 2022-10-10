# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 09:21:43 2022

@author: Vincent Medrano with help from Geeks for Geeks and CUEMATH
"""

# =============================================================================
# Write a function roots that computes the roots of a quadratic equation.
# Check for complex roots and print an
# error message saying that the roots are complex.
# Hint 1: Your function should take three parameters- what are they?
# Hint 2: We know the roots are complex when what condition about the discriminant is met?
# Be sure to use a variety of test cases, that include complex roots, real roots, and double roots.
# Optional: For an extra challenge, compute and print out the complex roots
#(Python can natively handle complex numbers)
# =============================================================================

import math
# quadratic equation is ax**2 + bx + c = 0

# create a function to find roots

def roots_finder(a,b,c):
    # formula for calculating discriminant
    discriminant = b * b - 4 * a * c 
    square_value = math.sqrt(abs(discriminant)) # abs for positive integer
    
    if discriminant > 0:
        print("Real and different roots")
        print((-b + square_value)/(2 * a)) 
        print((-b - square_value)/(2 * a)) 
        
    elif discriminant == 0:
        print(" real and same roots") 
        print(-b / (2 * a))
        
    else:
        print("Complex Roots") 
        print(- b / (2 * a), " + i", square_value) 
        print(- b / (2 * a), " - i", square_value) 




# ask user to input values for a, b and c
a = int(input("Please enter a value for a"))
b = int(input("Please enter a value for b"))
c = int(input("Please enter a value for c"))

roots_finder(a,b,c)

