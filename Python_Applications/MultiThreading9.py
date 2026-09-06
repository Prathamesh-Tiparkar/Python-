import time
import threading

def SumEven(No):
    print("TID os sumeven thread is : ",threading.get_ident())

def SumOdd(No):
    print("TID os sumodd thread is : ",threading.get_ident())

def main():
    print("TID os sumeven thread is : ",threading.get_ident())

    start_time = time.perf_counter()

    t1 = threading.Thread(target = SumEven, args = (100000000,))
    t2 = threading.Thread(target = SumOdd, args = (100000000,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    end_time = time.perf_counter()

    print(f"Time required is : {end_time - start_time:.5f}")

if __name__ == "__main__":
    main()

''' Summation of Odd :  2500000000000000
    Summation of Even :  2499999950000000
    Time required is : 9.02457 '''