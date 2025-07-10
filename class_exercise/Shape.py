import math

#CLASS SHAPE
class Shape:
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return math.pow(self.side,2)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * math.pow(self.radius,2)
    
square = Square(4)
print(f'Square area: {square.area()}')

circle = Circle(5)
print(f'Circle area: {circle.area()}')