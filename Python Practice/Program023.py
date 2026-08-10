# ========================================================
# Write a program which accepts two numbers and prints
# addition, subtraction, multiplication and division.
#
# IP: 10 5
# OP:
# Addition : 15
# Subtraction : 5
# Multiplication : 50
# Division : 2.0
# ========================================================

no1 = int(input("Enter first number : "))
no2 = int(input("Enter second number : "))

print("Addition :", no1 + no2)
print("Subtraction :", no1 - no2)
print("Multiplication :", no1 * no2)

if no2 != 0:
    print("Division :", no1 / no2)
else:
    print("Division not possible")
