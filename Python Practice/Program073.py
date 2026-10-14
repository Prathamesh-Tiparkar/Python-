
# ========================================================
# Program 3
# Write a program which accepts N numbers from user and
# stores them into a List. Return minimum number
# from that List.
#
# IP:
# Number of elements : 4
# Input Elements : 13 5 45 7
#
# OP: 5
# ========================================================

def Minimum(arr):

    min = arr[0]

    for i in arr:
        if i < min:
            min = i

    return min

def main():

    size = int(input("Enter number of elements : "))

    data = []

    print("Enter the elements :")

    for i in range(size):
        value = int(input())
        data.append(value)

    ret = Minimum(data)

    print("Minimum element :", ret)

if __name__ == "__main__":
    main()

