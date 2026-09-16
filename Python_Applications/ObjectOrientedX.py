
class Arithematic:
  
    def Addition(self, No1, No2):
        Ans = No1 + No2
        return Ans

# Ret = Addition(aobj, Value1, Value2)

    def Substarction(self, No1, No2):
        Ans = No1 - No2
        return Ans
    
aobj = Arithematic()

print("Enter 1st number: ")
Value1 = int(input())

print("Enter 2nd number: ")
Value2 = int(input())

# Ret = Addition(aobj, Value1, Value2)

Ret = aobj.Addition(Value1, Value2)         
print("Additon is : ",Ret)

Ret = aobj.Substarction(Value1, Value2)     
print("Substraction is : ",Ret)
