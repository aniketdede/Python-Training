# ABSTRACTION = HIDING complex details, showing only IMPORTANT things
# Like a TV Remote - you press button, TV changes channel
# You don't know HOW it works internally, you just USE it!

# To use Abstraction in Python, we use ABC (Abstract Base Class)
from abc import ABC, abstractmethod

# 🔵 ABSTRACT CLASS - acts as a TEMPLATE
# Cannot create object of abstract class directly
class Vehicle(ABC):
    
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year  = year
    
    # @abstractmethod = MUST be implemented by child classes
    # These methods have NO body here (abstract)
    @abstractmethod
    def start_engine(self):
        pass
    
    @abstractmethod
    def stop_engine(self):
        pass
    
    @abstractmethod
    def fuel_type(self):
        pass
    
    # Normal method (not abstract) - common for all vehicles
    def show_info(self):
        print(f"Brand : {self.brand}")
        print(f"Model : {self.model}")
        print(f"Year  : {self.year}")


# 🟢 CONCRETE CLASS 1 - Car
class Car(Vehicle):
    
    # MUST implement all abstract methods
    def start_engine(self):
        print(f"🚗 {self.brand} Car engine started: Vroom Vroom!")
    
    def stop_engine(self):
        print(f"🚗 {self.brand} Car engine stopped!")
    
    def fuel_type(self):
        print(f"⛽ Fuel Type: Petrol/Diesel")


# 🟡 CONCRETE CLASS 2 - Electric Car
class ElectricCar(Vehicle):
    
    def __init__(self, brand, model, year, battery_capacity):
        super().__init__(brand, model, year)
        self.battery_capacity = battery_capacity
    
    def start_engine(self):
        print(f"⚡ {self.brand} Electric Car started silently!")
    
    def stop_engine(self):
        print(f"⚡ {self.brand} Electric Car stopped!")
    
    def fuel_type(self):
        print(f"🔋 Fuel Type: Electric Battery ({self.battery_capacity} kWh)")


# 🔴 CONCRETE CLASS 3 - Bike
class Bike(Vehicle):
    
    def start_engine(self):
        print(f"🏍️ {self.brand} Bike engine started: Prrr!")
    
    def stop_engine(self):
        print(f"🏍️ {self.brand} Bike engine stopped!")
    
    def fuel_type(self):
        print(f"⛽ Fuel Type: Petrol")


# ✅ Creating objects of concrete classes
print("======== Car ========")
car = Car("Toyota", "Innova", 2022)
car.show_info()
car.start_engine()
car.fuel_type()
car.stop_engine()

print("\n======== Electric Car ========")
ecar = ElectricCar("Tesla", "Model 3", 2023, 75)
ecar.show_info()
ecar.start_engine()
ecar.fuel_type()
ecar.stop_engine()

print("\n======== Bike ========")
bike = Bike("Honda", "Shine", 2021)
bike.show_info()
bike.start_engine()
bike.fuel_type()
bike.stop_engine()

# ❌ Cannot create object of Abstract class
print("\n--- Trying to create object of Abstract class ---")
try:
    v = Vehicle("Some", "Vehicle", 2020)
except TypeError:
    print("❌ Cannot create object of Abstract class Vehicle!")