
# ========================================================
# Program 4
# Write a program which accepts N numbers from user and
# stores them into a List. Accept one another number
# from user and return frequency of that number.
#
# IP:
# Number of elements : 11
# Input Elements : 13 5 45 7 4 56 5 34 2 5 65
# Element to search : 5
#
# OP: 3
# ========================================================

def Frequency(arr, no):

    count = 0

    for i in arr:
        if i == no:
            count = count + 1

    return count

def main():

    size = int(input("Enter number of elements : "))

    data = []

    print("Enter the elements :")

    for i in range(size):
        value = int(input())
        data.append(value)

    search = int(input("Enter element to search : "))

    ret = Frequency(data, search)

    print("Frequency :", ret)

if __name__ == "__main__":
    main()
