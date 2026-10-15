# ========================================================
# Program 19-1
# Write a program which contains one lambda function
# which accepts one parameter and returns power of two.
#
# IP: 4
# OP: 16
# ========================================================

Power = lambda no : no ** 2

def main():

    value = int(input("Enter number : "))

    ret = Power(value)

    print(ret)

if __name__ == "__main__":
    main()