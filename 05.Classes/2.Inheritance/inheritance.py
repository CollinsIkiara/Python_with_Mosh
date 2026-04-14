# This code demonstrates inheritance in Python. The Mammal class is the parent class, and Dog and Cat are child classes that inherit from Mammal. Each child class has its own unique method (bark for Dog and meow for Cat) while also sharing the walk method from the Mammal class.

class Mammal:
    def __init__(self, name):
        self.name = name
        
    def walk(self):
        print(f"{self.name} walks like a mammal.")
        
        
class Dog(Mammal):
    def bark(self):
        print(f"But {self.name} barks like a dog.")
        
        
class Cat(Mammal):
    def meow(self):
        print(f"But {self.name} meows like a cat.")
        
        
dog = Dog("Buddy") 
dog.walk()
dog.bark()

cat = Cat("Whiskers")
cat.walk()
cat.meow()