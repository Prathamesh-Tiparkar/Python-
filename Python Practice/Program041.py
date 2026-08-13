# ========================================================
# Write a lambda function using map() which accepts a list of numbers and  
# returns a list of squares of each number.
# ========================================================

Square = lambda No: No * No

def main():
        
    Arr = list(map(int, input("Enter Numbers : ").split()))

    Ret = list(map(Square, Arr))

    print("Squares of numbers are : ",Ret)

if __name__ == "__main__":
    main()
