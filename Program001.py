# Write a function to accept 2 numbers and return their multiplication

def Multiplication(No1, No2):
    Ans = No1 * No2
    return Ans

def main():
    
    No1 = int(input("Enter First number: "))
    No2 = int(input("Enter Second number: "))
  
    Ret = Multiplication(No1, No2)
    print("Multiplication is: ",Ret)
    
if __name__ == "__main__":
    main()