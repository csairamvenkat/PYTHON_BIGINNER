# If inherited and sub class donot have construuctor it calls parent class constructor.If Sub class has constructor it doesnot call the parent class constructor.
#Super is keyword to call the parent class constructor.


# 🔍 MRO in Python (Method Resolution Order)
# MRO stands for Method Resolution Order, and it defines the order in which Python looks for a method or attribute in a hierarchy of classes — especially important when using inheritance (particularly multiple or multilevel inheritance).

# ✅ Why is MRO important?
# When you call a method on an object, Python searches for it in a specific order. If it’s not in the current class, it checks the parent(s), and then their parents — based on MRO.

# In multiple ingeritane mro is executed from left to right
# Eg : Class A, Class B, Class C (A,B)-->when executed calls class A but not B

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
