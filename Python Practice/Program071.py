# ========================================================
# Program 18-1
# Write a program which accepts N numbers from user and
# stores them into a List. Return addition of all
# elements from that List.
#
# IP:
# Number of elements : 6
# Input Elements : 13 5 45 7 4 56
#
# OP: 130
# ========================================================


def SumList(arr):

    sum = 0

    for i in arr:
        sum = sum + i

    return sum

def main():

    size = int(input("Enter number of elements : "))

    data = []

    print("Enter the elements :")

    for i in range(size):
        value = int(input())
        data.append(value)

    ret = SumList(data)

    print("Addition of elements :", ret)

if __name__ == "__main__":
    main()