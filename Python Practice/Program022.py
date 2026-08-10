# ========================================================
# Write a program which accepts one number and prints
# its factors.
#
# IP: 12
# OP: 1 2 3 4 6 12
# ========================================================

no = int(input("Enter a number : "))

print("Factors are :")

for i in range(1, no + 1):
    if no % i == 0:
        print(i, end=" ")
