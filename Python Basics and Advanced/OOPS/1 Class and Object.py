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

'''

| Method Type         | What it operates on        | First Parameter | Accesses                |
| ------------------- | -------------------------- | --------------- | ----------------------- |
| **Instance Method** | The instance (`object`)    | `self`          | Instance and class data |
| **Class Method**    | The class itself (`class`) | `cls`           | Only class-level data   |

'''
# Instance Method
class MyClass:
    def __init__(self, value):
        self.value = value

    def show(self):  # instance method
        print(f"Value is {self.value}")

obj = MyClass(42)
obj.show()  # Output: Value is 42

# Class Method 

class MyClass:
    count = 0

    def __init__(self):
        MyClass.count += 1

    @classmethod
    def show_count(cls):  # class method
        print(f"Number of instances: {cls.count}")

obj1 = MyClass()
obj2 = MyClass()
MyClass.show_count()  # Output: Number of instances: 2

