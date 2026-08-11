# ========================================================
# Write a lambda function which accepts one number and 
# returns True if number is even otherwise False
# ========================================================

Even = lambda No1: True if No1 % 2 == 0 else False

def main():
        
    No1 = int(input("Enter first number : "))

    Ret = Even(No1)

    print(Ret)

if __name__ == "__main__":
    main()
