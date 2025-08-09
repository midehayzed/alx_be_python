# polymorphism_demo.py
import math

# Base class
class Shape:
    def area(self):
        """This method should be overridden by subclasses."""
        raise NotImplementedError("Subclasses must override the area() method")

# Rectangle subclass
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Circle subclass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)
