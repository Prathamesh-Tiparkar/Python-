# ========================================================
# Program 10
# Write a program which accepts number from user and
# returns addition of digits in that number.
#
# IP: 5187934
# OP: 37
# ========================================================

def SumDigits(no):

    sum = 0

    while no > 0:
        digit = no % 10
        sum = sum + digit
        no = no // 10

    return sum

def main():

    value = int(input("Enter a number : "))

    ret = SumDigits(value)

    print("Addition of digits :", ret)

if __name__ == "__main__":
    main()