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

    def load_cargo(self, cargo_weight):
        if not self.is_engine_started:
            if self.load + cargo_weight <= self.max_cargo_weight:
                self.load += cargo_weight
            else:
                print(f"Cannot load cargo more than max limit: {self.max_cargo_weight}")
        else:
            print("Cannot load cargo during motion")

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
