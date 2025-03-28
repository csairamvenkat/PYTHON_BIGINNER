#Polymorphism allows different classes to be treated the same way. It is implemented via method overriding or method overloading.
class Shape:
    def area(self):
        print("Calculating area.")

class Circle(Shape):
    def area(self):
        print("Area = π * r^2")

shape = Shape()
shape.area()  # Output: Calculating area.

circle = Circle()
circle.area()  # Output: Area = π * r^2
