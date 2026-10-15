# ========================================================
# Program 19-5
# Write a program which contains filter(), map()
# and reduce().
#
# Filter : Prime numbers
# Map    : Multiply by 2
# Reduce : Maximum number
# ========================================================

from functools import reduce

def ChkPrime(no):

    count = 0

    for i in range(1, no + 1):
        if no % i == 0:
            count = count + 1

    if count == 2:
        return True
    else:
        return False

Map = lambda no : no * 2
Reduce = lambda x, y : x if x > y else y

def main():

    Data = [2,70,11,10,17,23,31,77]

    FData = list(filter(ChkPrime, Data))
    print("List after filter :", FData)

    MData = list(map(Map, FData))
    print("List after map :", MData)

    RData = reduce(Reduce, MData)
    print("Output :", RData)

if __name__ == "__main__":
    main()