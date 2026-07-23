''' Write a program which accepts one number and checks
    whether it is divisible by 3 and 5.'''

def ChkDivision(iValue):
    return iValue % 3 == 0 and iValue % 5 == 0

def main():
    No1 = int(input("Enter number: "))

    Ret = ChkDivision(No1)
    print("Divisble by 3 and 5 ",Ret)

if __name__ == "__main__":
    main()