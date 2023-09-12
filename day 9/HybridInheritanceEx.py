# Base class
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} is starting")

# Derived class inheriting from Vehicle
class Car(Vehicle):
    def drive(self):
        print(f"{self.brand} is driving")

# Another derived class inheriting from Vehicle
class Boat(Vehicle):
    def sail(self):
        print(f"{self.brand} is sailing")

# Class inheriting from both Car and Boat
class AmphibiousVehicle(Car, Boat):
    def operate(self):
        print(f"{self.brand} is operating as an amphibious vehicle")

# Create instances of the classes
car = Car("Toyota")
boat = Boat("Yamaha")
amphibious = AmphibiousVehicle("AmphiCraft")

# Demonstrate hybrid inheritance
car.start()
car.drive()

boat.start()
boat.sail()

amphibious.start()
amphibious.drive()
amphibious.sail()
amphibious.operate()
