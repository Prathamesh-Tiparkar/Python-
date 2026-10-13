
# ========================================================
# Program 17-4
# Write a program which accepts one number from user
# and returns addition of its factors.
#
# IP: 12
# OP: 16
# ========================================================

def SumFactors(no):

    sum = 0

    for i in range(1, no):
        if no % i == 0:
            sum = sum + i

    return sum

def main():

    value = int(input("Enter a number : "))

    ret = SumFactors(value)

    print("Addition of factors :", ret)

if __name__ == "__main__":
    main()