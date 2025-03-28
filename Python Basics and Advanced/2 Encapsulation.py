
# Encapsulation is the bundling of data (attributes) and methods within a class. It also involves restricting direct access to some attributes using access modifiers.

# Public: Accessible everywhere.
# Private: Accessible only within the class (prefix with __).
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder  # Public
        self.__balance = balance  # Private

    def deposit(self, amount):
        self.__balance += amount

    def __display_balance(self):  # Private method
        print(f"Balance: {self.__balance}")

    def get_balance(self):  # Public method to access private attribute
        return self.__balance

account = BankAccount("Bob", 1000)
print(account.get_balance())  # Output: 1000
