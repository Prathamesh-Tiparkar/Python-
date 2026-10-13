# ========================================================
# Program 17-1
# Create one module named Arithmetic which contains
# 4 functions:
# Add() for addition
# Sub() for subtraction
# Mult() for multiplication
# Div() for division
#
# All functions accept two parameters and perform the
# respective operation. Write a Python program which
# calls all the functions from Arithmetic module.
#
# IP: 10 5
# OP:
# Addition       : 15
# Subtraction    : 5
# Multiplication : 50
# Division       : 2.0
# ========================================================

import Arithmetic

def main():

    No1 = int(input("Enter first number: "))
    No2 = int(input("Enter second number: "))

    Arithmetic.Add(No1, No2)
    Arithmetic.Sub(No1, No2)
    Arithmetic.Mult(No1, No2)
    Arithmetic.Div(No1, No2)

if __name__ == "__main__":
    main()