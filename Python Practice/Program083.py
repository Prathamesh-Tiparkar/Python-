# ========================================================
# Program 20-3
# Design a Python application that creates two threads
# named EvenList and OddList.
#
# Both threads accept a list of integers.
#
# EvenList displays sum of all even elements.
# OddList displays sum of all odd elements.
# ========================================================

import threading

def EvenList(arr):

    sum = 0

    for i in arr:
        if i % 2 == 0:
            sum = sum + i

    print("Sum of Even elements :", sum)

def OddList(arr):

    sum = 0

    for i in arr:
        if i % 2 != 0:
            sum = sum + i

    print("Sum of Odd elements :", sum)

def main():

    size = int(input("Enter number of elements : "))

    Data = []

    print("Enter the elements :")

    for i in range(size):
        value = int(input())
        Data.append(value)

    T1 = threading.Thread(target = EvenList, args = (Data,), name = "EvenList")
    T2 = threading.Thread(target = OddList, args = (Data,), name = "OddList")

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()