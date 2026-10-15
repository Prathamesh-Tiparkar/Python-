# ========================================================
# Program 20-4
# Design a Python application that creates three threads
# named Small, Capital and Digits.
#
# Accept a string from user.
#
# Small   : Count lowercase letters.
# Capital : Count uppercase letters.
# Digits  : Count numeric digits.
#
# Display Thread ID and Thread Name.
# ========================================================

import threading

def Small(str):

    count = 0

    for ch in str:
        if ch.islower():
            count = count + 1

    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    print("Small letters :", count)

def Capital(str):

    count = 0

    for ch in str:
        if ch.isupper():
            count = count + 1

    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    print("Capital letters :", count)

def Digits(str):

    count = 0

    for ch in str:
        if ch.isdigit():
            count = count + 1

    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    print("Digits :", count)

def main():

    value = input("Enter string : ")

    T1 = threading.Thread(target = Small, args = (value,), name = "Small")
    T2 = threading.Thread(target = Capital, args = (value,), name = "Capital")
    T3 = threading.Thread(target = Digits, args = (value,), name = "Digits")

    T1.start()
    T2.start()
    T3.start()

    T1.join()
    T2.join()
    T3.join()

    print("Exit from main")

if __name__ == "__main__":
    main()