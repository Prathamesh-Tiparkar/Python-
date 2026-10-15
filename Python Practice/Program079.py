# ========================================================
# Program 19-4
# Write a program which contains filter(), map()
# and reduce().
#
# Filter : Even numbers
# Map    : Square
# Reduce : Addition
# ========================================================

from functools import reduce

Filter = lambda no : no % 2 == 0
Map = lambda no : no * no
Reduce = lambda x, y : x + y

def main():

    Data = [5,2,3,4,3,4,1,2,8,10]

    FData = list(filter(Filter, Data))
    print("List after filter :", FData)

    MData = list(map(Map, FData))
    print("List after map :", MData)

    RData = reduce(Reduce, MData)
    print("Output :", RData)

if __name__ == "__main__":
    main()