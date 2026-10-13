# ========================================================
# Program 17-7
# Write a program which accepts one number and displays
# the following pattern.
#
# IP: 5
#
# OP:
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# ========================================================

def Display(no):

    for i in range(no):
        for j in range(1, no + 1):
            print(j, end="\t")
        print()

def main():

    value = int(input("Enter a number : "))

    Display(value)

if __name__ == "__main__":
    main()