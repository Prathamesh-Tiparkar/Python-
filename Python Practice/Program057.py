
# ========================================================
# Program 16-7
# Write a program which contains one function that accepts
# one number from user and returns True if number is
# divisible by 5 otherwise returns False.
#
# IP: 8
# OP: False
#
# IP: 25
# OP: True
# ========================================================

def Check(no):
    if no % 5 == 0:
        return True
    else:
        return False

def main():
    value = int(input("Enter a number : "))

    ret = Check(value)

    print(ret)

if __name__ == "__main__":
    main()