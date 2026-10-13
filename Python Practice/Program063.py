
# ========================================================
# Program 17-3
# Write a program which accepts one number from user
# and returns its factorial.
#
# IP: 5
# OP: 120
# ========================================================

def Factorial(no):

    fact = 1

    for i in range(1, no + 1):
        fact = fact * i

    return fact

def main():

    value = int(input("Enter a number : "))

    ret = Factorial(value)

    print("Factorial :", ret)

if __name__ == "__main__":
    main()