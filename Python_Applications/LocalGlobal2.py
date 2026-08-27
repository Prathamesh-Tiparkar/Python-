
no = 11             # Global variable

def Display():
    A = 21
    print("From Display : ",no)
    print("From Display value of A is: ",A)        # Local Variable
    pass

def Demo():
    print("From Demo : ",no)
    print("From Demo value of A : ",A)      # Logical Error
    pass

Display()
Demo()