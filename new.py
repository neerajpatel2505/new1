# # protected variable------------
# class BankAccount:
#     def __init__(self, account_number, balance):
#         self.account_number = account_number  # Public attribute
#         self._balance = balance               # Protected attribute

#     def deposit(self, amount):
#         if amount > 0:
#             self._balance += amount
#             print(f"Deposited ${amount}. New balance: ${self._balance}")
#         else:
#             print("Invalid deposit amount!")

#     def withdraw(self, amount):
#         if 0 < amount <= self._balance:
#             self._balance -= amount
#             print(f" Withdrew ${amount}. New balance: ${self._balance}")
#         else:
#             print("Invalid or insufficient funds!")

#     def get_balance(self):  # Getter for _balance
#         return self._balance

# account = BankAccount("12345", 1000)
# print(f"Account Number: {account.account_number}")
# print(f"Balance (via getter): {account.get_balance()}")
# print(f"Directly accessing balance: {account._balance}")
# account.deposit(500)
# account.withdraw(300)


# private variable------------
class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # Private attribute
        self.__balance = balance                # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid or insufficient funds!")

    def get_balance(self):  # Getter for __balance
        return self.__balance

account = BankAccount("12345", 1000)
print(account._BankAccount__balance)
print("Hello for testing..........")