class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance


    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount

    def print_balance(self):
        print(self.balance)


test = BankAccount("Alex", 100)
test.print_balance()

test.deposit(100)
test.print_balance()

test.withdraw(100)
test.print_balance()

test.withdraw(1000)