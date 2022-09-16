# To establish this relationship, we can update our User's __init__ method to something like this, removing the account_balance attribute and adding an account attribute:

class User: 
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0) #we added this line

# The BankAccount class should be in the same file as the User class, so the reference to it is recognized. Take a look into MODULARIZATION if you feel the need to have the 2 classes in separate files.

# We interact with this new attribute just as we do with previous attributes--the only difference is that we have personally defined the functionality of this class! We know the attributes and methods available to the account attribute by looking at our BankAccount class.

class User:
    def  example(self):
        #we can cal the BankAccount instance's methods
        self.account.deposit(100)
        #or acccess its attrs
        print(self.account.balance)
