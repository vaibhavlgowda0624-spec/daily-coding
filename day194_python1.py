class BankAccount:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal successful.")
        else:
            print("Insufficient balance.")

    def display(self):
        print("Owner:", self.owner)
        print("Balance:", self.balance)


account = BankAccount("Rahul", 5000)

account.deposit(2000)
account.withdraw(1500)

account.display()
