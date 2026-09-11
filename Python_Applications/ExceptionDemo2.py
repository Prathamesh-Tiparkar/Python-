def main():

    Ans = 0
    try:

        print("Enter 1st number: ")
        No1 = int(input())

        print("Enter 2nd number: ")
        No2 = int(input())   

        Ans = No1/No2

        print("Division is Sucessful")

    except ZeroDivisionError as zobj:
        print("Exception Occured due to second operand is zero",zobj)

    print("Result is : ",Ans)

if __name__ == "__main__":
    main()