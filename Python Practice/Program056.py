
# ========================================================
# Program 16-6
# Write a program which accepts a number from user and
# checks whether that number is positive, negative or zero.
#
# IP: 11
# OP: Positive Number
#
# IP: -8
# OP: Negative Number
#
# IP: 0
# OP: Zero
# ========================================================

def CheckNumber(no):
    if no > 0:
        print("Positive Number")
    elif no < 0:
        print("Negative Number")
    else:
        print("Zero")

def main():
    value = int(input("Enter a number : "))
    CheckNumber(value)

if __name__ == "__main__":
    main()
