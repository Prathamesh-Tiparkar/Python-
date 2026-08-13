# ========================================================
# Write a lambda function using reduce() which accepts a list of numbers and  
# returns the addition of all elements.
# ========================================================

from functools import reduce

Addition = lambda No1, No2: No1 + No2

def main():
        
    Arr = list(map(int, input("Enter Numbers : ").split()))

    Ret = reduce(Addition, Arr)

    print("Addition of all numbers are : ",Ret)

if __name__ == "__main__":
    main()
