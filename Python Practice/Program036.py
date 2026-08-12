# ========================================================
# Write a lambda function which accepts one number and 
# returns True if number is Odd otherwise False
# ========================================================

Odd = lambda No1: True if No1 % 1 == 0 else False

def main():
        
    No1 = int(input("Enter first number : "))

    Ret = Odd(No1)

    print(Ret)

if __name__ == "__main__":
    main()
