from abc import ABC, abstractmethod

# Abstract Base Class (ABC) or Interface-like Class
class Vehicle(ABC):
    
    def __init__(self, wc) -> None:
        self.wheelsCount = wc
    
    @abstractmethod
    def start(self):
        pass
    
    # Concrete method
    def display(self):
        print("This message is from vehicle class")

# Concrete Subclass 1: Bike
class Bike(Vehicle):
    def __init__(self, vc):
        super().__init__(vc)
        self.vehicleCount = vc
    
    def start(self):
        print("Start by Kick and having", self.vehicleCount, "tyres.")

# Concrete Subclass 2: Scooty
class Scooty(Vehicle):
    def __init__(self, color):
        super().__init__(4)
        self.color = color
    
    def start(self):
        print("Start by Self-start button and have", self.wheelsCount, "tyres and is of", self.color, "color.")

# Concrete Subclass 3: Car
class Car(Vehicle):
    def __init__(self, vc, gears):
        super().__init__(vc)
        self.gears = gears
    
    def start(self):
        print("Start by Key having", self.wheelsCount, "tyres and having", self.gears, "gears")

# Testing Polymorphism
if __name__ == "__main__":
    bike = Bike(2)
    bike.start()

    sc = Scooty("Red")
    sc.start()

    cr = Car(4, 6)
    cr.start()
