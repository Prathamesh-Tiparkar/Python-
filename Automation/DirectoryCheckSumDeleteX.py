import sys
import os
import hashlib          # for calculting checksum and md5

def CalculateCheckSum(FileName):
    fobj = open(FileName,"rb")      # rb is binary file

    hobj = hashlib.md5()

    Buffer = fobj.read(1024)

    while(len(Buffer) > 0 ):
        hobj.update(Buffer)
        Buffer = fobj.read(1024)       

    fobj.close()

    return hobj.hexdigest()

def FindDuplicate(DirectoryName):
    Ret = False

    Ret = os.path.exists(DirectoryName)

    if(Ret == False):
        print("Path is Invalid")
        return

    Ret = os.path.isdir(DirectoryName)

    if(Ret == False):
        print("It is not a Directory")
        return

    Duplicate = {}

    for FolderName, SubFolder, FileName in os.walk(DirectoryName):
        for fname in FileName:
            fname = os.path.join(FolderName,fname)

            Checksum = CalculateCheckSum(fname)

            if Checksum in Duplicate :
                Duplicate[Checksum].append(fname)
            else:
                Duplicate[Checksum] = [fname]

    return Duplicate

def DeleteDuplicate(DirectoryName):
    MyDict = FindDuplicate(DirectoryName)

    Result = list(filter(lambda x : len(x) > 1, MyDict.values()))

    Count = 0
    TotalDeleted = 0

    for value in Result:
        
        for subvalue in value:
            Count = Count + 1
            if(Count > 1):
                print("Duplicate Found : ",subvalue)  
                TotalDeleted = TotalDeleted + 1
        Count = 0          
        
    print("Total Deleted files : ",TotalDeleted)
    
def main():
    Data = DeleteDuplicate("Test")


if __name__ == "__main__":
    main()
