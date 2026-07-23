def DisplayOdd(iNo):
    
    for i in range(1,iNo + 1, 2):
        print(i) 

def main():
    iValue = int(input("Enter number :"))
    DisplayOdd(iValue)

if __name__ == "__main__":
    main()