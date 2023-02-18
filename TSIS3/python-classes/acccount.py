class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, deposit_):
        self.balance += deposit_

    def withdraw(self, withdraw):

        if(withdraw > self.balance):
            print(f"Current balance - {self.balance}, and it's doesn't have this count of money")
        else:
            self.balance -= withdraw
            print(f"You took {withdraw}")
            print(f"Current balance - {self.balance}")
