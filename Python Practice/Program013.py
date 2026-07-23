def Factorial(iNo):
    iFact = 1
    for i in range(1,iNo + 1):
        iFact = iFact * i
    print("Summation is : ",iFact) 

def main():
    iValue = int(input("Enter number :"))
    Factorial(iValue)

if __name__ == "__main__":
    main()