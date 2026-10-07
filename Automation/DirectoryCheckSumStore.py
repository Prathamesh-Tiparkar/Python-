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
    Unique = 0
    Same = 0

    for FolderName, SubFolder, FileName in os.walk(DirectoryName):
        for fname in FileName:
            fname = os.path.join(FolderName,fname)

            Checksum = CalculateCheckSum(fname)

            print(f"{fname} : {Checksum}")

            if Checksum in Duplicate :
                Same = Same + 1
                Duplicate[Checksum].append(fname)
            else:
                Unique = Unique + 1
                Duplicate[Checksum] = [fname]

    print("Unique Files found : ",Unique)
    print("Duplicate Files found : ",Same)
    
def main():
    FindDuplicate("Test")

if __name__ == "__main__":
    main()
