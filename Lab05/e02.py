class BankAccount:
    def __init__(self,owner):
        self.owner = owner
        self.balance = 0
        self.transactions = []

    def deposit(self,amount):
        self.balance += amount
        self.transactions.append(f'Added {amount}')

    def withdraw(self,amount):
        self.balance -= amount
        self.transactions.append(f'Withdrew {amount}')

    def transfer(self, amount, account):
        self.balance -= amount
        account.balance += amount
        self.transactions.append(f'Sent {amount} to {account.owner}')
        account.transactions.append(f'Received {amount} from {self.owner}')

    def history(self):
        print(self.transactions)

class SavingsAccount(BankAccount):
    def __init__(self, owner, interest_rate):
        super().__init__(owner)
        self.interest_rate = interest_rate

    def apply_interest(self):
        self.balance += self.balance * self.interest_rate
        self.transactions.append(f'Added to your account the amount of {self.balance * self.interest_rate} from a {self.interest_rate}% interest rate')

MyAccount = BankAccount('Me')
MySavingsAccount = SavingsAccount('SavingsAccount', 0.05)

MyAccount.deposit(1000)
MyAccount.transfer(100, MySavingsAccount)
MySavingsAccount.apply_interest()

MyAccount.history()
MySavingsAccount.history()
