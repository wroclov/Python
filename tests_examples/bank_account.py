
class InsufficientFundsError(Exception):
    pass

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Cannot deposite negative amount!")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds to withdraw", amount)
        self.balance -= amount

    def get_balance(self):
        return self.balance

    def get_owner(self):
        return self.owner

    def transfer_to(self, target_account, amount):
        if amount <= 0:
            raise ValueError("Transfer amount must be positive")
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds for transfer")
        self.withdraw(amount)
        target_account.deposit(amount)



