class User:

    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate = 0.02, balance = 0)

    def make_deposit(self,amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self,amount):
        self.account.withdraw(amount)
        return self

    def display_balance(self):
        self.account.display_account_info()
        return self

class BankAccount:
    def __init__(self, int_rate, balance): 
        # your code here! (remember, instance attributes go here)
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance-=amount
            print(f'Amount withdrawn: {amount}')
        else:
            print(f'Insufficient funds: $5 fee will be charged to account {self.balance}')
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

user_one = User('Roger Baptiste', 'rogerbap@outlook.com')

user_one.make_deposit(325).make_withdrawal(100).display_balance()



    # def transfer_money(self, amount, other_user):



# class User:
#     def example_method(self):
# # we can call the BankAccount instance's methods
#         self.account.deposit(100)
# # or access its attributes
#         print(self.account.balance)





































# class BankAccount:
#     def __init__(self,int_rate, balance):
#         self.int_rate = int_rate
#         self.balance = balance
    
#     def deposit(self,amount):
#         self.balance+=amount
#         return self

# class User:
#     def __init__(self,name,email):
#         self.name = name
#         self.email = email
#         self.account - BankAccount(int_rate=0.02, balance =0)

#     def make_deposit(self,amount):
#         self.account.deposit(amount)
#         print(f'you now have ${self.account.balance}')
#         return self


# henry= User("Henry", "h@noemail.com")

# henry.make_deposit(150)
