def SumDigits(iNo):
    iSum = 0

    while iNo != 0:
        iDigit = iNo % 10
        iSum = iSum + iDigit
        iNo = iNo // 10

    return iSum

def main():
    iValue = int(input("Enter number : "))

    Ret = SumDigits(iValue)

    print("Summation of digits :", Ret)

if __name__ == "__main__":
    main()