# ========================================================
# Program 20-1
# Design a Python application that creates two separate
# threads named Even and Odd.
#
# Even thread displays first 10 even numbers.
# Odd thread displays first 10 odd numbers.
# ========================================================

import threading

def Even():

    print("Even Thread")

    for i in range(2, 21, 2):
        print(i)

def Odd():

    print("Odd Thread")

    for i in range(1, 20, 2):
        print(i)

def main():

    T1 = threading.Thread(target = Even, name = "Even")
    T2 = threading.Thread(target = Odd, name = "Odd")

    T1.start()
    T1.join()

    T2.start()
    T2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()