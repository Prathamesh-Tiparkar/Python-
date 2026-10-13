#===================================================================
# Python Assignment 16-3
#===================================================================
# Write a program which contains one function named as Add() 
# which accept 2 numbers from user and return Additon of that 2 number.
# 
# ip: 11  5         op: 16
#===================================================================

def Add(No1, No2):
    Ans = No1 + No2
    return Ans

def main():
    Num1 = int(input("Enter First number : "))
    Num2 = int(input("Enter second number : "))

    Ret = Add(Num1, Num2)

    print(Ret)
    
if __name__ == "__main__":
    main()