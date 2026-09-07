import time
import multiprocessing
import os

def SumEven(No):
    print(f"PID of SumEven : {os.getpid()} PPID of SumEven : {os.getppid()}")
    Sum = 0
    
    for i in range(2,No,2):
        Sum = Sum + i

    print("Summation of Even : ",Sum)

def SumOdd(No):
    print(f"PID of SumOdd : {os.getpid()} PPID of SumOdd : {os.getppid()}")
    Sum = 0
    
    for i in range(1,No,2):
        Sum = Sum + i

    print("Summation of Odd : ",Sum)

def main():
    print(f"PID of Main : {os.getpid()} PPID of Main : {os.getppid()}")

    start_time = time.perf_counter()

    t1 = multiprocessing.Process(target = SumEven, args = (100000000,))
    t2 = multiprocessing.Process(target = SumOdd, args = (100000000,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    end_time = time.perf_counter()

    print(f"Time required is : {end_time - start_time:.5f}")

if __name__ == "__main__":
    main()

''' PID of Main : 13264 PPID of Main : 12216
    PID of SumEven : 10704 PPID of SumEven : 13264
    PID of SumOdd : 5192 PPID of SumOdd : 13264
    Summation of Even :  2499999950000000
    Summation of Odd :  2500000000000000
    Time required is : 4.78907  '''