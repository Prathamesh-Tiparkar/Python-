def Reverse(iNo):
    iRev = 0

    while iNo != 0:
        iDigit = iNo % 10
        iRev = (iRev * 10) + iDigit
        iNo = iNo // 10

    return iRev

def main():
    iValue = int(input("Enter number : "))

    Ret = Reverse(iValue)

    print("Reverse of number :", Ret)

if __name__ == "__main__":
    main()