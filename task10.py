class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Yangi balans: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Yechib olindi. Yangi balans: {self.balance}")
        else:
            print("Xatolik: balansda yetarli mablag' mavjud emas.")

account1 = BankAccount("Nilufar", 500)
account1.deposit(250)
account1.withdraw(100)
account1.withdraw(800)
