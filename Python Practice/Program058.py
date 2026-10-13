
# ========================================================
# Program 15-8
# Write a program which accepts a number from user and
# prints that number of "*" on screen.
#
# IP: 5
# OP: * * * * *
# ========================================================

def Display(no):
    for i in range(no):
        print("*", end=" ")

def main():
    value = int(input("Enter a number : "))
    Display(value)

if __name__ == "__main__":
    main()
