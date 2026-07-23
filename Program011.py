
def Multiply(iNo):
    Mult = 1
    for i in range(1,11):
        print(iNo * i)

def main():
    iValue = int(input("Enter number "))

    Multiply(iValue)


if __name__ == "__main__":
    main()