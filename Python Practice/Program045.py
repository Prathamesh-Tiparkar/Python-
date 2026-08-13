# ========================================================
# Write a lambda function using reduce() which accepts a list of numbers and  
# returns maximum elements.
# ========================================================

from functools import reduce

Max = lambda No1, No2: No1 if No1 > No2 else No2

def main():
        
    Arr = list(map(int, input("Enter Numbers : ").split()))

    Ret = reduce(Max, Arr)

    print("Maximum element is : ",Ret)

if __name__ == "__main__":
    main()
