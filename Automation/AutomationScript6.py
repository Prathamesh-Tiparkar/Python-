# python Automation.py --h
# python Automation.py --u
# python Automation.py Marvellous

import sys

def main():
    Border = "-"*40
    print(Border)
    print(" Marvellous Automation Script ")
    print(Border)

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This automation script is ude to travel the directory")
            print("for better usage please check --u flag")
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Please execute the script as ")
            print("python FileName.py DirectoryName")
            print("DirectoryName should be Absolute path")
        else:
            DirectoryName = sys.argv[1]
            print("Directory name is : ",DirectoryName)
    else:
        print("Invalid no of arguments")
        print("Please use --h or --u for more information")
    
    print(Border)
    print(" Thank You for using Marvellous Automation Script ")
    print(Border)

if __name__ == "__main__":
    main()

# --h -> help
# --u -> usage
