
# ========================================================
# Program 17-5
# Write a program which accepts one number from user
# and checks whether the number is prime or not.
#
# IP: 5
# OP: Prime Number
# ========================================================

def CheckPrime(no):

    count = 0

    for i in range(1, no + 1):
        if no % i == 0:
            count = count + 1

    if count == 2:
        return True
    else:
        return False

def main():

    value = int(input("Enter a number : "))

    ret = CheckPrime(value)

    if ret == True:
        print("Prime Number")
    else:
        print("Not a Prime Number")

if __name__ == "__main__":
    main()