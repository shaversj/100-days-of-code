class Account(object):
    def __init__(self, name):
        self.name = name


class CheckingAccount(Account):
    def __init__(self, name, balance=0):
        Account.__init__(self, name)
        self.balance = balance

    def balance(self):

        return self.balance

    def deposit(self, amount: int):
        self.balance += amount

    def withdrawl(self, amount: int):
        self.balance -= amount


class SavingsAccount(Account):
    def __init__(self, name, balance=0):
        Account.__init__(self, name)
        self.balance = balance

    def balance(self):

        return self.balance

    def deposit(self, amount: int):
        self.balance += amount

    def withdrawl(self, amount: int):
        self.balance -= amount


class BusinessAccount(Account):
    def __init__(self, name, balance=0):
        Account.__init__(self, name)
        self.balance = balance

    def balance(self):
        return self.balance

    def deposit(self, amount: int):
        self.balance += amount

    def withdrawl(self, amount: int):
        self.balance -= amount


josh_checking = CheckingAccount(name='Josh')
josh_checking.deposit(500)
josh_checking.withdrawl(260)

bob_savings = SavingsAccount(name='Bob', balance=1000)
bob_savings.withdrawl(100)

terry_business = BusinessAccount(name='Terry', balance=10000)
terry_business.deposit(500)


print(josh_checking.balance)
print(bob_savings.balance)
print(terry_business.balance)
