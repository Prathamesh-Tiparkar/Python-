
# ========================================================
# Program 16-10
# Write a program which accepts name from user and
# displays length of its name.
#
# IP: Marvellous
# OP: 10
# ========================================================

def NameLength(name):
    return len(name)

def main():
    str = input("Enter your name : ")

    ret = NameLength(str)

    print("Length of name is :", ret)

if __name__ == "__main__":
    main()