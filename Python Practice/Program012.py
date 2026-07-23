def Sum(iNo):
    iSum = 0
    for i  in range(1, iNo+1):
        iSum = iSum + i
    print("Summation is : ",iSum) 

def main():
    iValue = int(input("Enter number :"))
    Sum(iValue)

if __name__ == "__main__":
    main()