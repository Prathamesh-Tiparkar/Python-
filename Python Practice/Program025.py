# ========================================================
# Write a program which accepts one number and prints
# that many numbers in reverse order.
#
# IP: 5
# OP: 5 4 3 2 1
# ========================================================

no = int(input("Enter a number : "))

for i in range(no, 0, -1):
    print(i, end=" ")