# POLYMORPHISM = "Many Forms"
# Same method name but DIFFERENT behavior for different classes
# Example: Every animal makes sound, but sound is DIFFERENT

class Cat:
    def speak(self):
        print("Cat says    : Meow Meow 🐱")

class Dog:
    def speak(self):
        print("Dog says    : Woof Woof 🐶")

class Cow:
    def speak(self):
        print("Cow says    : Moo Moo 🐄")

class Duck:
    def speak(self):
        print("Duck says   : Quack Quack 🦆")


# ✅ Same function call, but DIFFERENT output for different objects
# This is POLYMORPHISM!

def make_animal_speak(animal):
    animal.speak()   # same method name "speak()"


print("====== Polymorphism Example ======")

# Creating objects
cat  = Cat()
dog  = Dog()
cow  = Cow()
duck = Duck()

# Storing all objects in a list
animals = [cat, dog, cow, duck]

# Calling same method on different objects
for animal in animals:
    make_animal_speak(animal)   # same call, different result!


# ✅ Another Example: Area calculation (same method, different shapes)
print("\n====== Shape Area Example ======")

class Circle:
    def area(self, radius):
        result = 3.14 * radius * radius
        print(f"Circle Area  = {result}")

class Rectangle:
    def area(self, length, width):
        result = length * width
        print(f"Rectangle Area = {result}")

class Triangle:
    def area(self, base, height):
        result = 0.5 * base * height
        print(f"Triangle Area  = {result}")


c = Circle()
r = Rectangle()
t = Triangle()

c.area(5)
r.area(4, 6)
t.area(3, 8)