
CheckEven = lambda No: (No % 2 == 0)
Increment = lambda No: No + 1
Addition = lambda No1, No2: No1 + No2

def filterX(Task, Elements):
    Result = []

    for No in Elements:
        Ret = Task(No)          # CheckEven(no)

        if(Ret == True):
            Result.append(No)

    return Result

def mapX(Task, Elements):
    Result = []

    for No in Elements:
        Ret = Task(No)          # Increment(No)
        Result.append(Ret)

    return Result

def reduceX(Task, Elements):
    Sum = 0

    for No in Elements:
        Sum = Task(Sum,No)
    
    return Sum

def main():
    Data = [13,12,8,10,11,20]

    print("Input Data is : ",Data)

    FData = list(filterX(CheckEven, Data))
    print("Data after filter : ",FData)

    MData = list(mapX(Increment,FData))
    print("Data after Map : ",MData)

    RData = reduceX(Addition, MData)
    print("Data after Reduce : ",RData)

if __name__ == "__main__":
    main()