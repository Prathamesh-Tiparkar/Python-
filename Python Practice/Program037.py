# ========================================================
# Write a lambda function which accepts one number and 
# returns True if divisible by 5.
# ========================================================

Div = lambda No1: True if No1 % 5 == 0 else False

def main():
        
    No1 = int(input("Enter first number : "))

    Ret = Div(No1)

    print(Ret)

if __name__ == "__main__":
    main()
