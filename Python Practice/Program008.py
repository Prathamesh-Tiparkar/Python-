''' Write a program which accepts one number and prints 
    square of that number.'''

def NumSquare(iValue):
    Sum = iValue * iValue
    return Sum

def main():
    No1 = int(input("Enter number: "))

    Ret = NumSquare(No1)

    print("Square is : ",Ret)

if __name__ == "__main__":
    main()