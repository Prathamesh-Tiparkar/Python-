# ========================================================
# Write a program which accepts marks and displays grade.
#
# Conditions:
# Marks >= 75 : Distinction
# Marks >= 60 : First Class
# Marks >= 50 : Second Class
# Marks < 50  : Fail
#
# IP: 68
# OP: First Class
# ========================================================

marks = int(input("Enter marks : "))

if marks >= 75:
    print("Distinction")
elif marks >= 60:
    print("First Class")
elif marks >= 50:
    print("Second Class")
else:
    print("Fail")