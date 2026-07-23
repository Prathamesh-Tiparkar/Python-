def DisplayEven(iNo):
    
    for i in range(2,iNo + 1, 2):
        print(i) 

def main():
    iValue = int(input("Enter number :"))
    DisplayEven(iValue)

if __name__ == "__main__":
    main()