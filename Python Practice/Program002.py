''' Write a function that does not return anything but prints 
 a msg. Explain the default return value of such a function. '''

def Display():
    print("Welcome to Marvellous")

def main():
    Ret = Display()
    print("Return Value is: ",Ret)

if __name__ == "__main__":
    main()