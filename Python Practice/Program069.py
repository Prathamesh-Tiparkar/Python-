# ========================================================
# Program 9
# Write a program which accepts number from user and
# returns number of digits in that number.
#
# IP: 5187934
# OP: 7
# ========================================================

def CountDigits(no):

    count = 0

    while no > 0:
        count = count + 1
        no = no // 10

    return count

def main():

    value = int(input("Enter a number : "))

    ret = CountDigits(value)

    print("Number of digits :", ret)

if __name__ == "__main__":
    main()