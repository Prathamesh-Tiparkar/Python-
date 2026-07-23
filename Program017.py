def CountDigits(iNo):
    iCount = 0

    while iNo != 0:
        iCount = iCount + 1
        iNo = iNo // 10

    return iCount

def main():
    iValue = int(input("Enter number : "))

    Ret = CountDigits(iValue)

    print("Number of digits :", Ret)

if __name__ == "__main__":
    main()