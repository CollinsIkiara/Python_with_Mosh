# Classes are blueprints for creating objects. They define a set of attributes and methods that the created objects will have.

class Point:
    def move(self):
        print("move")
        
    def draw(self):
        print("draw")
        
        
point1 = Point() # creating an instance (object) of the Point class
point1.x = 10 # adding an attribute 'x' to the point1 object
print(point1.x)
point1.draw()

point2 = Point()
point2.x = 1 
print(point2.x)  