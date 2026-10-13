#===================================================================
# Python Assignment 16-2
#===================================================================
# Write a program which contains one function named as ChkNum() 
# which accept one parameter as number. If number is even then it  
# should display "Even number" otherwise display "Odd number" on console.
# 
# ip: 11            op: Odd Number
# ip: 8             op: Even Number
#===================================================================

def ChkNum(No):
    if(No % 2 == 0):
        print("Even Number")
    else:
        print("Odd Number")

def main():
    Num = int(input("Enter a number : "))

    ChkNum(Num)

if __name__ == "__main__":
    main()