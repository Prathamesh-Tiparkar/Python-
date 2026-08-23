def Calculations(No1, No2):
    Mult = No1 * No2
    Div = No1 / No2
    return Mult, Div

def main():
    Value1 = int(input("Enter first number: "))
    Value2 = int(input("Enter Second number: "))

    Ret1, Ret2 = Calculations(Value1, Value2)
    
    print("multplication is: ",Ret1)
    print("division is: ",Ret2)

if __name__ == "__main__":
    main()
