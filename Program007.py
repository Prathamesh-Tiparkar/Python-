''' Write a program which contains one function ChkGreater()
    that accepts two numbers and prints the greater number.'''

def ChkGreater(iValue1, iValue2):
    if(iValue1 > iValue2):
        return iValue1
    else:
        return iValue2

def main():
    No1 = int(input("Enter first number: "))
    No2 = int(input("Enter second number: "))

    Ret = ChkGreater(No1, No2)

    print("Greater number is : ",Ret)

if __name__ == "__main__":
    main()