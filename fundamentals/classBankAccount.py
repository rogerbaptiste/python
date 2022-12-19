class BankAccount:
    accounts = []
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        # your code here! (remember, instance attributes go here)
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance-=amount
            print(f'Amount withdrawn: {amount}')
        else:
            print(f'Insufficient funds: {self.balance}')
            self.balance -= 5
        return self

    def display_account_info(self):
        print(self.balance)
        return self

    def yield_interest(self):
        if self.balance >= 1:
            self.balance += self.balance * self.int_rate
        return self

    @classmethod
    def all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

money_market_account = BankAccount(.06,7000)
checking_account = BankAccount(.03,500)

money_market_account.deposit(250).deposit(75).deposit(600).yield_interest().display_account_info()