# ========================================================
# Write a lambda function using reduce() which accepts a list of numbers and
# returns the count of even numbers.
# ========================================================

from functools import reduce

Count = lambda Count, No: Count + 1 if No % 2 == 0 else Count

def main():

    Arr = list(map(int, input("Enter Numbers : ").split()))

    Ret = reduce(Count, Arr, 0)

    print("Count of even numbers is :", Ret)

if __name__ == "__main__":
    main()