def BigBazar():
    print("Inside BigBazar")

    def Amul():                                     # Inner Function / Nested Function
        print("Inside Amul IceCream Parlor")

    Amul()
    Amul()
    
def main():
    BigBazar()          # Allowed

if __name__ == "__main__":
    main()
