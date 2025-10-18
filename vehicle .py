class vehicle:
    def describe(self):
        print("This is a generic vehicle.")

class car(vehicle):

      print("This is a sporty car.")

class Motorcycle(vehicle):
    def describe(self):
        print("This is a fast motorcycle.")

#Make objects from each class
vehicle = vehicle()
car = car()
Motorcycle = Motorcycle()
