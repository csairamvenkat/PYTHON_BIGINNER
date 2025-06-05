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



# Different Poly morphisms in python.
# Duck Typeing : Same method names but different class. All methods should be present in all classes. When we call methods then call the method from outside class.It gives that respective o/p.
# Operator Overloading
# Method Overloading
# Method over Riding
