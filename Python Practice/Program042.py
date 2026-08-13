# ========================================================
# Write a lambda function using filter() which accepts a list of numbers and  
# returns a list of Even of each number.
# ========================================================

Even = lambda No: No % 2 == 0

def main():
        
    Arr = list(map(int, input("Enter Numbers : ").split()))

    Ret = list(filter(Even, Arr))

    print("Even of numbers are : ",Ret)

if __name__ == "__main__":
    main()
