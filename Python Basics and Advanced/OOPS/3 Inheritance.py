# Parent class
class Animal:
    def speak(self):
        print("Animal makes a sound.")

# Child class
class Dog(Animal):
    def speak(self):
        print("Dog barks.")

# Create objects
animal = Animal()
animal.speak()  # Output: Animal makes a sound.

dog = Dog()
dog.speak()     # Output: Dog barks.
