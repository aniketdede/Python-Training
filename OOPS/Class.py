# Class is like a BLUEPRINT
# Object is like a REAL THING made from that blueprint

# Example: Dog is a class, "Tommy" is an object

class Dog:
    
    # __init__ is called CONSTRUCTOR (runs automatically when object is created)
    def __init__(self, name, age, breed):
        self.name = name      # attributes (properties)
        self.age = age
        self.breed = breed
    
    # Methods (functions inside a class)
    def bark(self):
        print(f"{self.name} says: Woof! Woof! 🐶")
    
    def show_info(self):
        print(f"Name  : {self.name}")
        print(f"Age   : {self.age} years")
        print(f"Breed : {self.breed}")
        print("-" * 25)


# ✅ Creating OBJECTS from the class
dog1 = Dog("Tommy", 3, "Labrador")
dog2 = Dog("Bruno", 5, "German Shepherd")
dog3 = Dog("Coco",  2, "Poodle")

# Calling methods on objects
print("====== Dog Information ======")
dog1.show_info()
dog2.show_info()
dog3.show_info()

dog1.bark()
dog2.bark()
