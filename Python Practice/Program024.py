# ========================================================
# Write a program which accepts one number and prints
# that many numbers starting from 1.
#
# IP: 5
# OP: 1 2 3 4 5
# ========================================================

no = int(input("Enter a number : "))

for i in range(1, no + 1):
    print(i, end=" ")
