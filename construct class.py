class Student:
    def __init__(self,name):
        self.name = name
        
    def show(self):
        print('Hello,my name is',self.name)
s1 = Student('Sai')
s1.show()
