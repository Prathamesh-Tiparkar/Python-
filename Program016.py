def PrimeNumber(iNo):
    if iNo <= 1:
        return False
    
    for i in range(2,iNo):
        if iNo % i == 0:
            return False
        
    return True

def main():
    iValue = int(input("Enter a Number : "))

    Ret = PrimeNumber(iValue)

    if Ret == True:
        print("Prime Number")
    else:
        print("Not a Prime Number")

if __name__ == "__main__":
    main()