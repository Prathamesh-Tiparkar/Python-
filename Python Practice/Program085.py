# ========================================================
# Program 20-5
# Design a Python application that creates two threads
# named Thread1 and Thread2.
#
# Thread1 displays numbers from 1 to 50.
# Thread2 displays numbers from 50 to 1.
#
# Thread2 starts only after Thread1 completes.
# ========================================================

import threading

def Display():

    for i in range(1, 51):
        print(i)

def Reverse():

    for i in range(50, 0, -1):
        print(i)

def main():

    T1 = threading.Thread(target = Display, name = "Thread1")
    T2 = threading.Thread(target = Reverse, name = "Thread2")

    T1.start()
    T1.join()

    T2.start()
    T2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()