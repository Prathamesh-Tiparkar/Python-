
class Arithematic:
  
    def Addition(No1, No2):
        Ans = No1 + No2
        return Ans

# Ret = Addition(aobj, Value1, Value2)

    def Substarction(No1, No2):
        Ans = No1 - No2
        return Ans
    
aobj = Arithematic()

print("Enter 1st number: ")
Value1 = int(input())

print("Enter 2nd number: ")
Value2 = int(input())

Ret = aobj.Addition(Value1, Value2)         # Error
print("Additon is : ",Ret)

Ret = aobj.Substarction(Value1, Value2)     # Error
print("Substraction is : ",Ret)
