# python Automation.py --h
# python Automation.py --u
# python Automation.py Marvellous

import sys

def main():
    DirectoryName = sys.argv[1]

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("Help")
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Usage")
        else:
            DirectoryName = sys.argv[1]
            print("Directory name is : ",DirectoryName)
    else:
        print("Invalid no of arguments")
        print("Please use --h or --u for more information")

if __name__ == "__main__":
    main()

# --h -> help
# --u -> usage

'''
D:\PYTHON GEN AI\Automations>python3 AutomationScript3.py --u
Usage

D:\PYTHON GEN AI\Automations>python3 AutomationScript3.py --h
Help

D:\PYTHON GEN AI\Automations>python3 AutomationScript3.py Marvellous
Directory name is :  Marvellous

D:\PYTHON GEN AI\Automations>python3 AutomationScript3.py Marvellous Demo
Invalid no of arguments
Please use --h or --u for more information

'''