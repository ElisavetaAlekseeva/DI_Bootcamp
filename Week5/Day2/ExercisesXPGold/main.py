# Exercise 1: Bank Account
# Instructions
# Part I:
# Create a class called BankAccount that contains the following attributes and methods:
# balance - (an attribute)
# __init__ : initialize the attribute
# deposit : - (a method) accepts a positive int and adds to the balance, raise an Exception if the int is not positive.
# withdraw : - (a method) accepts a positive int and deducts from the balance, raise an Exception if not positive
# Part II : Minimum balance account
# Create a MinimumBalanceAccount that inherits from BankAccount.
# Extend the __init__ method and accept a parameter called minimum_balance with a default value of 0.
# Override the withdraw method so it only allows the user to withdraw money if the balance remains higher than the minimum_balance, raise an Exception if not.
# Part III: Expand the bank account class
# Add the following attributes to the BankAccount class:
# username
# password
# authenticated (False by default)
# Create a method called authenticate. This method should accept 2 strings : a username and a password. If the username and password match the attibutes username and password the method should set the authenticated boolean to True.
# Edit withdraw and deposit to only work if authenticated is set to True, if someone tries an action without being authenticated raise an Exception
# Part IV: BONUS Create an ATM class
# __init__:
# Accepts the following parameters: account_list and try_limit.
# Validates that account_list contains a list of BankAccount or MinimumBalanceAccount instances.
# Hint: isinstance()
# Validates that try_limit is a positive number, if you get an invalid input raise an Exception, then move along and set try_limit to 2. 
# Hint: Check out this tutorial
# Sets attribute current_tries = 0
# Call the method show_main_menu (see below)
# Methods:
# show_main_menu:
# This method will start a while loop to display a menu letting a user select:
# Log in : Will ask for the users username and password and call the log_in method with the username and password (see below).
# Exit.
# log_in:
# Accepts a username and a password.
# Checks the username and the password against all accounts in account_list.
# If there is a match (ie. use the authenticate method), call the method show_account_menu.
# If there is no match with any existing accounts, increment the current tries by 1. Continue asking the user for a username and a password, until the limit is reached (ie. try_limit attribute). Once reached display a message saying they reached max tries and shutdown the program.
# show_account_menu:
# Accepts an instance of BankAccount or MinimumBalanceAccount.
# The method will start a loop giving the user the option to deposit, withdraw or exit.

# Part 1:
# class BankAccount:
#     def __init__(self, balance) -> None:
#         self.balance = balance
#     def deposit(self, deposit):
#         if deposit > 0:
#             try:
#                 self.balance += deposit
#             except ValueError:
#                 print(ValueError)
#         print(self.balance)
                
#     def withdraw(self, deducts):
#         if deducts > 0:
#             try:
#                 self.balance -= deducts
#             except ValueError:
#                 print(ValueError)
#         print(self.balance)

# my_account = BankAccount(1000)
# my_account.deposit(400)
# my_account.withdraw(-200)



# # part 2:
# class MinimumBalanceAccount(BankAccount):
#     def __init__(self, balance, minimum_balance = 0) -> None:
#         super().__init__(balance)
#         self.minimum_balance =minimum_balance
#     def withdraw(self, deducts):
#         if self.balance > self.minimum_balance:
#                 self.balance -= deducts
#         else:
#                 print(ValueError)
#         print(self.balance)

# new_account = MinimumBalanceAccount(200, 300)
# new_account.withdraw(200)


# part 3:
class BankAccount:
    def __init__(self, balance, username, password, authenticated = False) -> None:
        self.balance = balance
        self.username = username
        self.password = password
        self.authenticated = authenticated

    def deposit(self, deposit):
        if self.authenticated == True:
            try:
                self.balance += deposit
            except ValueError:
                print(ValueError)
        print(self.balance)
                
    def withdraw(self, deducts):
        if self.authenticated == True:
            try:
                self.balance -= deducts
            except ValueError:
                print(ValueError)
        print(self.balance)

    def authenticate(self, username, password):
        if username == self.username and password == self.password:
            self.authenticated = True
            return self.authenticated

my_account1 = BankAccount(1000, 'Lisa', '123Lisa')
my_account2 = BankAccount(200, 'Misha', '123isa')
my_account3 = BankAccount(4000, 'Katya', '123sa')

my_account1.authenticate('Lisa', '123Lisa')

# my_account.deposit(400)
# my_account.withdraw(-200)


# part 4:
class ATM:
    def __init__(self,account_list,try_limit) -> None:
        self.account_list = account_list
        self.current_tries = 0

        for account in self.account_list:
            if not isinstance(account, BankAccount):
                self.account_list.remove(account)
        print(self.account_list)
        try:
            if try_limit <= 0:
                raise ValueError
            else:
                self.try_limit = try_limit
        except ValueError:
            self.try_limit = 2
        print(self.try_limit)



    def show_main_menu(self):
        while True:
            print('ok')
            user_name = input('Username or "exit": ')
            if user_name == 'exit':
                break
            user_password = input('Userpassword: ')
            self.log_in(user_name, user_password)

    def log_in(self, username, password):
        for account in self.account_list:
            if isinstance(account, BankAccount):
                if account.authenticate(username,password):
                    self.show_account_menu()
                    print('ok')
                else:
                    self.current_tries += 1
                    self.show_main_menu()
    def show_account_menu(self, account):
        while True:
            user = input('exit, deposit withdraw: ')
            if user == 'exit':
                break
            elif user == 'deposit':
                user_deposit = int(input('deposit: '))
                account.deposit(user_deposit)
            elif user == 'withdraw':
                user_withdraw = int(input('withdraw: '))
                account.withdraw(user_withdraw)


a = ATM([my_account1,my_account2, my_account3], 3)
a.show_account_menu(my_account1)