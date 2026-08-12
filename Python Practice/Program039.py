# ========================================================
# Write a lambda function which accepts two numbers and 
# returns Multiplication.
# ========================================================

Mult = lambda No1, No2: No1 * No2

def main():
        
    No1 = int(input("Enter first number : "))
    No2 = int(input("Enter second number : "))

    Ret = Mult(No1, No2)

    print(Ret)

if __name__ == "__main__":
    main()
