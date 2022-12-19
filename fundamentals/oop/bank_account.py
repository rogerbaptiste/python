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

#value = class(arguments for def values in parameters)
money_market_account = BankAccount(.06,7000)
checking_account = BankAccount(.03,500)

#chainingmethod below
money_market_account.deposit(3250).deposit(600).deposit(1850).withdraw(475).yield_interest().display_account_info()

checking_account.deposit(2521.21).deposit(6700.81).withdraw(2500).withdraw(347.67).withdraw(52).withdraw(212).yield_interest().display_account_info()

#Calling/Using class method to print
BankAccount.all_accounts()


#Examples below
# checking_account.withdraw(550)

# checking_account.yield_interest()

# checking_account.display_account_info()

