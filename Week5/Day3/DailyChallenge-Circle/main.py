# Instructions :
# The goal is to create a class that represents a simple circle.
# A Circle can be defined by either specifying the radius or the diameter. 
# The user can query the circle for either its radius or diameter.
# Other abilities of a Circle instance:
# Compute the circle’s area
# Print the circle and get something nice
# Be able to add two circles together
# Be able to compare two circles to see which is bigger
# Be able to compare two circles and see if there are equal
# Be able to put them in a list and sort them
from cmath import pi


class Circle:
    def __init__(self, radius) -> None:
        self.radius = radius
        self.diameter = radius * 2
        print (f'New circle:  {self}')
    @classmethod
    def from_diameter(cls, diameter):
        new_circle = Circle(diameter/2)
        return new_circle

    def area(self):
        return self.radius ** 2 * pi

    def __str__(self):
        return f'radius: {self.radius} and diameter: {self.diameter}'

    def __add__(self,other):
        new_radius = self.radius + other.radius
        return Circle(new_radius)

    def __gt__(self, other):
        return self.radius > other.radius
    
    def __lt__(self, other):
        return self.radius < other.radius
    
    def __eq__(self, other):
        return self.radius == other.radius

    def __repr__(self):
        return str(self.radius)
    




a = Circle(4)
b = Circle.from_diameter(4)
print(f'r-{a.radius} d-{a.diameter}')
print(f'r-{b.radius} d-{b.diameter}')

print(a)
print(a.area())
c = a+b
print(b > a)
list = [b, a]
c = sorted(list)
print(c)

