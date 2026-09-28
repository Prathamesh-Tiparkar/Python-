# seek (kuth jaychay? , Kuthun)
# kuthun : 0/1/2

# 0 Starting
# 1 Current
# 2 End

def main():
    try : 
        fobj = open("Demo.txt","r")
        print("File gets opened")

        fobj.seek(10,0)

        data = fobj.read()

        print(data)        

    except FileNotFoundError as fobj:
        print("File is not presented in current directory")

if __name__ == "__main__":
    main()