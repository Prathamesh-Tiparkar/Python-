# ========================================================
# Write a lambda function which accepts two number and 
# returns minimum number.
# ========================================================

Min = lambda No1, No2 : No2 if No1 > No2 else No1

def main():
        
    No1 = int(input("Enter first number : "))
    No2 = int(input("Enter second number : "))

    Ret = Min(No1, No2)


    print("Minimum number is : ",Ret)

if __name__ == "__main__":
    main()
