# Define a class
#Ctrl+Shift+D to enable debug window
class MyClass:
    # Constructor method to initialize the object
    def __init__(self, value):
        self.value = value  # Attribute
    
    # Method
    def display(self):
        print(f"The value is {self.value}")

# Create an object (instance) of the class
obj = MyClass(10)

# Access attributes and call methods
print(obj.value)  # Output: 10
#obj.display()     # Output: The value is 10
