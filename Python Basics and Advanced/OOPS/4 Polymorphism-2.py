#Method Overloading (via Default Arguments):
class Calculator:
    def add(self, a, b, c=0):
        return a + b + c

calc = Calculator()
print(calc.add(1, 2))       # Output: 3
print(calc.add(1, 2, 3))    # Output: 6
