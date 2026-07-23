def CheckPalindrome(iNo):
    iTemp = iNo
    iRev = 0

    while iNo != 0:
        iDigit = iNo % 10
        iRev = (iRev * 10) + iDigit
        iNo = iNo // 10

    if iTemp == iRev:
        return True
    else:
        return False

def main():
    iValue = int(input("Enter number : "))

    Ret = CheckPalindrome(iValue)

    if Ret == True:
        print("Palindrome")
    else:
        print("Not Palindrome")

if __name__ == "__main__":
    main()