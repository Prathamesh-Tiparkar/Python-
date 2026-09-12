def main():

    Ans = 0
    try:

        print("Enter 1st number: ")
        No1 = int(input())

        print("Enter 2nd number: ")
        No2 = int(input())   

        Ans = No1/No2

        print("Division is Sucessful")

    except Exception as eobj:
        print("Exception Occured",eobj)

    print("Result is : ",Ans)

if __name__ == "__main__":
    main()