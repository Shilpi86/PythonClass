# Truck class should have the following attributes & methods #
# Old Attributes:
# color, max_speed, acceleration, tyre_friction, is_engine_started, current_speed
# New Attributes:
# max_cargo_weight, load
# Old Methods:
# start_engine, stop_engine, accelerate, apply_brakes, sound_horn
# Override Methods: sound_horn:
# - Print "Honk Honk" if truck engine is on
# - Print "Car has not started yet" if truck engine is off

class Car:
    def __init__(self, color, max_speed, acceleration, tyre_friction):
        self.color = color
        self.max_speed = max_speed
        self.acceleration = acceleration
        self.tyre_friction = tyre_friction
        self.is_engine_started = False
        self.current_speed = 0

    def start_engine(self):
        if not self.is_engine_started:
            self.is_engine_started = True

    def stop_engine(self):
        if self.is_engine_started:
            self.is_engine_started = False

    def accelerate(self):
        if self.is_engine_started:
            if self.current_speed + self.acceleration <= self.max_speed:
                self.current_speed += self.acceleration
            else:
                self.current_speed = self.max_speed

    def apply_brakes(self):
        if self.is_engine_started:
            if self.current_speed - self.tyre_friction >= 0:
                self.current_speed -= self.tyre_friction
            else:
                self.current_speed = 0

    def sound_horn(self):
        if self.is_engine_started:
            print("Honk Honk")
        else:
            print("Car has not started yet")

class Truck(Car):
    def __init__(self, color, max_speed, acceleration, tyre_friction, max_cargo_weight):
        super().__init__(color, max_speed, acceleration, tyre_friction)
        self.max_cargo_weight = max_cargo_weight
        self.load = 0

# load_cargo:
# - This method will have an argument cargo_weight, denoting the weight to be loaded in the truck.
# - Truck can load some cargo within max_cargo_weight
# - When this method is called when the car engine is off, the current_load of the truck
# should increase according to the cargo_weight passed as an argument to this method.
# - When this method is called when the car engine is on, print the message "Cannot load cargo during motion"
# - When the cargo_weight is more than max_cargo_weight,
# print the message "Cannot load cargo more than max limit: {max_cargo_weight}"

    def load_cargo(self, cargo_weight):
        if not self.is_engine_started:
            if self.load + cargo_weight <= self.max_cargo_weight:
                self.load += cargo_weight
            else:
                print(f"Cannot load cargo more than max limit: {self.max_cargo_weight}")
        else:
            print("Cannot load cargo during motion")

# unload_cargo:
# - This method will have an argument cargo_weight, denoting the weight to be unloaded from the truck.
# - Truck can unload amount of cargo_weight passed as an argument, only when the truck engine is off.
# - If the truck engine is on, print the message "Cannot unload cargo during motion"
# - Truck load can never go behind 0
# When a new Truck is created, the engine should be off by default and current_speed, load should be 0
#Truck can unload amount of cargo_weight passed as an argument,
                                        # only when the truck engine is off.
    def unload_cargo(self, cargo_weight):
        if not self.is_engine_started:
            if self.load - cargo_weight >= 0:
                self.load -= cargo_weight
            else:
                self.load = 0
        else:
            print("Cannot unload cargo during motion")


def sound_horn(self):
    if self.is_engine_started:
        print("Honk Honk")
    else:
        print("Car has not started yet")


# Example usage:
truck = Truck("Red", 80, 10, 5, 1000)
truck.start_engine()
truck.accelerate()
truck.load_cargo(500)
truck.sound_horn()
truck.stop_engine()
truck.unload_cargo(300)