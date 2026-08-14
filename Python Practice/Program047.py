# ========================================================
# Write a lambda function using filter() which accepts a list of strings and  
# returns a list of strings having length greater than 5.
# ========================================================

Greater = lambda Str: len(Str) > 5

def main():
        
    Arr = input("Enter Numbers : ").split()

    Ret = list(filter(Greater, Arr))

    print("Strings having length Greater than 5 are : ",Ret)

if __name__ == "__main__":
    main()
