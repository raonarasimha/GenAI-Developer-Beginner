class BankAccount:
    def __init__(self, owner, balance, account_type, pin):
        self.owner = owner              # public attribute
        self._balance = balance         # protected attribute by convention
        self._account_type = account_type  # protected attribute by convention
        self.__pin = pin                # private attribute (name mangling)

    def get_balance(self):
        return self._balance

    def set_balance(self, amount):
        if amount >= 0:
            self._balance = amount
        else:
            print("Balance cannot be negative!")

    def get_account_type(self):
        return self._account_type

    def get_pin(self):
        # Accessor for private variable
        return self.__pin

if __name__ == "__main__":
    account = BankAccount("Alice", 1000, "Savings", 1234)
    print(f"Owner: {account.owner}")
    print(f"Balance: {account.get_balance()}")
    print(f"Account Type (protected): {account.get_account_type()}")
    # Accessing protected variable directly (not recommended, but possible)
    print(f"Protected _account_type: {account._account_type}")
    # Accessing private variable via method
    print(f"PIN (private, via method): {account.get_pin()}")
    # Attempting to access private variable directly (will fail)
    try:
        print(account.__pin)
    except AttributeError:
        print("Cannot access __pin directly: AttributeError")
    # Accessing private variable using name mangling (not recommended)
    print(f"Private __pin (name mangling): {account._BankAccount__pin}")

    account.set_balance(1200)
    print(f"Updated Balance: {account.get_balance()}")
    account.set_balance(-500)  # Should print a warning