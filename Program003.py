''' WAP to dsiplay Data type, memory address, size in bytes 
  of the variable entered by the user. '''

import sys

def main():
    No = int(input("Enter a Number: "))
    
    print("Value : ",No)
    print("Data Type : ",type(No))
    print("Memory Address : ",id(No))
    print("Size in Bytes : ",sys.getsizeof(No))

if __name__ == "__main__":
    main()