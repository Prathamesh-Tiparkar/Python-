
# ========================================================
# Program 18-2
# Write a program which accepts N numbers from user and
# stores them into a List. Return maximum number
# from that List.
#
# IP:
# Number of elements : 7
# Input Elements : 13 5 45 7 4 56 34
#
# OP: 56
# ========================================================


def Maximum(arr):

    max = arr[0]

    for i in arr:
        if i > max:
            max = i

    return max

def main():

    size = int(input("Enter number of elements : "))

    data = []

    print("Enter the elements :")

    for i in range(size):
        value = int(input())
        data.append(value)

    ret = Maximum(data)

    print("Maximum element :", ret)

if __name__ == "__main__":
    main()
