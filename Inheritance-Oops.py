#single Inheritance
class A:
    
    def displayA(self):
        print("Inheritance A Class")
        
class B(A):

    def displayB(self):
        print("Inheritance B Class")

Obj=B()
Obj.displayA()
Obj.displayB()

print()
#Multi Label Inheritance
class A:

    def displayA(self):
        print("Inheritance C Class")

class B(A):

    def displayB(self):
        print("Inheritance B Class")


class C(B):

    def displayC(self):
        print("Inheritance C Class")

Obj=C()
Obj.displayA()
Obj.displayB()
Obj.displayC()
    
