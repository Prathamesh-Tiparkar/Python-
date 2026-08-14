# ========================================================
# Write a lambda function using reduce() which accepts a list of numbers and  
# returns the product of all elements.
# ========================================================

from functools import reduce

Product = lambda No1, No2: No1 * No2 

def main():
        
    Arr = list(map(int, input("Enter Numbers : ").split()))

    Ret = reduce(Product, Arr)

    print("Product of all numbers are : ",Ret)

if __name__ == "__main__":
    main()
