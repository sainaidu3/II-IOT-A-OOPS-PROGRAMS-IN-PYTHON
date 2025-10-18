class shape:
    def no_of_sides(self):
        print("This shape has many sides")
class Square(shape):
    def no_of_sides(self):
        print("A square has 4 sides")
#Creating objects
s1 = shape()
s2 = Square()
#calling the method
s1.no_of_sides() #Parent class method
s2.no_of_sides() #Child class overrides the method
        
