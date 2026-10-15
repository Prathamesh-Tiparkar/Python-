# ========================================================
# Program 19-3
# Write a program which contains filter(), map()
# and reduce().
#
# Filter : Numbers >=70 and <=90
# Map    : Increase each number by 10
# Reduce : Product of all numbers
# ========================================================

from functools import reduce

Filter = lambda no : no >= 70 and no <= 90
Map = lambda no : no + 10
Reduce = lambda x, y : x * y

def main():

    Data = [4,34,36,76,68,24,89,23,86,90,45,70]

    FData = list(filter(Filter, Data))
    print("List after filter :", FData)

    MData = list(map(Map, FData))
    print("List after map :", MData)

    RData = reduce(Reduce, MData)
    print("Output :", RData)

if __name__ == "__main__":
    main()