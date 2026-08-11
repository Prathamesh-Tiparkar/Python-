# ========================================================
# Write a lambda function which accepts one number and 
# returns cube of that number.
# ========================================================

square = lambda num : num * num *num

def main():
        
    num = int(input("Enter a number : "))

    Ret = square(num)

    print("Square of number is : ",Ret)

if __name__ == "__main__":
    main()
