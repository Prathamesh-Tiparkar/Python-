
class Arithematic:
    def __init__(self,A,B):     # Parameterized Constructor 
        self.No1 = A
        self.No2 = B
  
    def Addition(self):
        Ans = self.No1 + self.No2
        return Ans

    def Substarction(self):
        Ans = self.No1 - self.No2
        return Ans

print("Enter 1st number: ")
Value1 = int(input())

print("Enter 2nd number: ")
Value2 = int(input())

aobj = Arithematic(Value1, Value2)

# Ret = Addition(aobj, Value1, Value2)

Ret = aobj.Addition()         
print("Additon is : ",Ret)

Ret = aobj.Substarction()     
print("Substraction is : ",Ret)
