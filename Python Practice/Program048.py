# ========================================================
# Write a lambda function using filter() which accepts a list of numbers and  
# returns a list of numbers divisible by 3 and 5.
# ========================================================

Greater = lambda No: No % 3 == 0 and No % 5 == 0

def main():
        
    Arr = list(map(int, input("Enter Numbers : ").split()))

    Ret = list(filter(Greater, Arr))

    print("numbers divisible by 3 and 5 are : ",Ret)

if __name__ == "__main__":
    main()
