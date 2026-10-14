

# ========================================================
# Program 5
# Write a program which accepts N numbers from user and
# stores them into a List. Return addition of all
# prime numbers from that List.
#
# Main python file accepts N numbers from user and
# passes each number to ChkPrime() function which is
# present in user-defined module MarvellousNum.
#
# IP:
# Number of elements : 11
# Input Elements : 13 5 45 7 4 56 10 34 2 5 8
#
# OP: 32
# (13 + 5 + 7 + 2 + 5)
# ========================================================


import MarvellousNum

def ListPrime(arr):

    sum = 0

    for i in arr:
        if MarvellousNum.ChkPrime(i):
            sum = sum + i

    return sum

def main():

    size = int(input("Enter number of elements : "))

    data = []

    print("Enter the elements :")

    for i in range(size):
        value = int(input())
        data.append(value)

    ret = ListPrime(data)

    print("Addition of prime numbers :", ret)

if __name__ == "__main__":
    main()