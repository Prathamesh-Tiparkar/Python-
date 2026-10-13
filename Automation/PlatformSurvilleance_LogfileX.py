import psutil
import sys
import os
import time

def PlatformSurvillance(FolderName):
    Border = "-"*50

    Ret = False

    Ret = os.path.exists(FolderName)

    if(Ret == True):
        Ret = os.path.isidr(FolderName)
        if(Ret == False):
            print("Unable to proceed as folder name is existing but its not a directory")
            return
    else:
        os.mkdir(FolderName)
        print("Directory for the log file gets created successfully")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")

    FileName = os.path.join(FolderName,"Marvellous_%s.log" %timestamp)

    fobj = open(FileName,"w")

    print(f"Log File gets Successfully created with name {FileName}")

def main():
    Border = "-"*50
    print(Border)
    print(" --- Marvellous Platform Survilleance System --- ")
    print(Border)

    # --h & --u 
    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This Automation script is used to perform ")
            print("1: It fetch the information of the running processor")
            print("2: It fetch the information about the Primary storage as RAM")
            print("3: It fetch the information about the secondary storage as HDD")
            print("4: It fetch the information about the microprocessor")
            print("5: It gets auto scheduled peroidically")
            print("6: It maintains all the records into log file")
            print("7: It sends the log files through mail periodically")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the automation script as : ")
            print(f"python {sys.argv[0]} Time_Interval Folder_Name")
            print("Time_Interval : Time in minutes for periodic execution")
            print("Folder_Name : Name of Folder for the log file creation")
        else:
            print("Unable to proceed as aruguments are not matching")
            print("Please Use --h or --u flag for getting more details")           

    # actual project code
    elif(len(sys.argv) == 3):
        PlatformSurvillance(sys.argv[2])
    else:
        print("Invalid number of arguements")
        print("Unable to proceed as aruguments are not matching")
        print("Please Use --h or --u flag for getting more details")

    print(Border)
    print(" --- Thank You for using our Automation System --- ")
    print(Border)

if __name__ == "__main__":
    main()