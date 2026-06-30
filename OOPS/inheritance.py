# INHERITANCE = Child class GETS properties from Parent class
# Just like children inherit features from parents!
# Example: Animal is parent, Dog & Cat are children

# 🔵 PARENT CLASS (Base Class)
class Animal:
    
    def __init__(self, name, color):
        self.name  = name
        self.color = color
    
    def eat(self):
        print(f"{self.name} is eating 🍖")
    
    def sleep(self):
        print(f"{self.name} is sleeping 😴")
    
    def show_info(self):
        print(f"Name  : {self.name}")
        print(f"Color : {self.color}")


# 🟢 CHILD CLASS 1 - Dog inherits from Animal
class Dog(Animal):   # Animal is written in brackets = inheritance
    
    def __init__(self, name, color, breed):
        super().__init__(name, color)   # calling parent constructor
        self.breed = breed              # extra property of Dog
    
    def bark(self):                     # extra method of Dog
        print(f"{self.name} is barking: Woof! 🐶")
    
    def show_info(self):
        super().show_info()             # calling parent method
        print(f"Breed : {self.breed}")  # adding extra info


# 🟡 CHILD CLASS 2 - Cat inherits from Animal
class Cat(Animal):
    
    def __init__(self, name, color, indoor):
        super().__init__(name, color)
        self.indoor = indoor
    
    def meow(self):
        print(f"{self.name} is meowing: Meow! 🐱")
    
    def show_info(self):
        super().show_info()
        print(f"Indoor Cat : {self.indoor}")


# 🔴 CHILD CLASS 3 - Bird inherits from Animal
class Bird(Animal):
    
    def __init__(self, name, color, can_fly):
        super().__init__(name, color)
        self.can_fly = can_fly
    
    def fly(self):
        if self.can_fly:
            print(f"{self.name} is flying high! 🐦")
        else:
            print(f"{self.name} cannot fly!")
    
    def show_info(self):
        super().show_info()
        print(f"Can Fly : {self.can_fly}")


# ✅ Creating objects
print("========== Dog ==========")
dog = Dog("Tommy", "Brown", "Labrador")
dog.show_info()
dog.eat()      # inherited from Animal
dog.sleep()    # inherited from Animal
dog.bark()     # own method

print("\n========== Cat ==========")
cat = Cat("Kitty", "White", True)
cat.show_info()
cat.eat()      # inherited from Animal
cat.meow()     # own method

print("\n========== Bird ==========")
bird = Bird("Tweety", "Yellow", True)
bird.show_info()
bird.eat()     # inherited from Animal
bird.fly()     # own method