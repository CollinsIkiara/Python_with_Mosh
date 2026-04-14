# The following code illustrates the use of constructors in Classes. A constructor is a special method that is called when an object is instantiated. In Python, the constructor method is defined using the `__init__` method.

class Person:
    def __init__(self, name): # Constructor method.
        self.name = name
        
    def talk(self):
        print(f"Hello, my name is {self.name}")
        
person1 = Person("Collins") # When we create an object of the Person class, we pass the name to the constructor, which initializes the name attribute of the person1 object.
person1.talk() 
person1.name = "John" # We can also change the name attribute of the person1 object after it has been created. This demonstrates that the attributes of an object can be modified after instantiation.
person1.talk()

# Each object is a different instance of the Person class.