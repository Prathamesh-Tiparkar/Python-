import sys

def main():
    DirectoryName = sys.argv[1]

    print(len(sys.argv))
    print("Directory name is : ",DirectoryName)

if __name__ == "__main__":
    main()


'''
D:\PYTHON GEN AI\Automations>python3 AutomationScript.py Marvellous
Directory name is :  Marvellous

D:\PYTHON GEN AI\Automations>python3 AutomationScript.py Demo
Directory name is :  Demo

D:\PYTHON GEN AI\Automations>   '''