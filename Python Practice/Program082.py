# ========================================================
# Program 20-2
# Design a Python application that creates two threads
# named EvenFactor and OddFactor.
#
# Both threads accept one integer number.
#
# EvenFactor displays sum of even factors.
# OddFactor displays sum of odd factors.
#
# After completion display:
# Exit from main
# ========================================================

import threading

def EvenFactor(no):

    sum = 0

    for i in range(1, no + 1):
        if (no % i == 0) and (i % 2 == 0):
            sum = sum + i

    print("Sum of Even Factors :", sum)

def OddFactor(no):

    sum = 0

    for i in range(1, no + 1):
        if (no % i == 0) and (i % 2 != 0):
            sum = sum + i

    print("Sum of Odd Factors :", sum)

def main():

    value = int(input("Enter number : "))

    T1 = threading.Thread(target = EvenFactor, args = (value,), name = "EvenFactor")
    T2 = threading.Thread(target = OddFactor, args = (value,), name = "OddFactor")

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()