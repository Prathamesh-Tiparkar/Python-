# ========================================================
# Write a lambda function using reduce() which accepts a list of numbers and  
# returns minimum elements.
# ========================================================

from functools import reduce

Min = lambda No1, No2: No1 if No1 < No2 else No2

def main():
        
    Arr = list(map(int, input("Enter Numbers : ").split()))

    Ret = reduce(Min, Arr)

    print("Minimum element is : ",Ret)

if __name__ == "__main__":
    main()
