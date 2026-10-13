
# ========================================================
# Program 2
# Write a program which accepts one number and displays
# the following pattern.
#
# IP: 5
#
# OP:
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# ========================================================

def Display(no):
    for i in range(no):
        for j in range(no):
            print("*", end="\t")
        print()

def main():

    value = int(input("Enter a number : "))

    Display(value)

if __name__ == "__main__":
    main()
