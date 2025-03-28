# A class is a blueprint for creating objects. It defines the structure and behavior of the objects.
# An object is an instance of a class.
# Define a class
class Person:
    def __init__(self, name, age):
        self.name = name  # Attribute
        self.age = age    # Attribute

    def greet(self):  # Method
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Create an object
person1 = Person("Alice", 25)
person1.greet()  # Output: Hello, my name is Alice and I am 25 years old.
