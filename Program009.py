''' Write a program which accepts one number and prints 
    CUBE of that number.'''

def NumCube(iValue):
    Sum = iValue * iValue * iValue
    return Sum

def main():
    No1 = int(input("Enter number: "))

    Ret = NumCube(No1)

    print("Cube is : ",Ret)

if __name__ == "__main__":
    main()