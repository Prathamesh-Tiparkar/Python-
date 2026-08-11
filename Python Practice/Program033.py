# ========================================================
# Write a lambda function which accepts two number and 
# returns maximum number.
# ========================================================

Max = lambda No1, No2 : No1 if No1 > No2 else No2

def main():
        
    No1 = int(input("Enter first number : "))
    No2 = int(input("Enter second number : "))

    Ret = Max(No1, No2)


    print("Maximum number is : ",Ret)

if __name__ == "__main__":
    main()
