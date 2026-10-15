# ========================================================
# Program 19-2
# Write a program which contains one lambda function
# which accepts two parameters and returns multiplication.
#
# IP: 4 3
# OP: 12
# ========================================================

Mult = lambda no1, no2 : no1 * no2

def main():

    value1 = int(input("Enter first number : "))
    value2 = int(input("Enter second number : "))

    ret = Mult(value1, value2)

    print(ret)

if __name__ == "__main__":
    main()