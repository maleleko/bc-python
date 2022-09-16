

class BankAccount:
    accounts = [] #class attr
    
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        #if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
        if self.balance < amount:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        #decreases the account balance by the given amount if there are sufficient funds
        else: 
            self.balance -= amount
        return self

    def displayaccinfo(self):
        print(f"Balance: ${self.balance}")
        return self

    def yieldint(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self
        #increases the account balance by the current balance * the interest rate (as long as the balance is positive)
    
    @classmethod #new class method to 
    def printall(cls):
        for account in cls.accounts:
            account.displayaccinfo()

acc_one = BankAccount(0.2, 666.33)
acc_two = BankAccount(0.2, 420.69)

print("savings:")
acc_one.deposit(111.30).deposit(69.42).deposit(420.24).withdraw(777.28).yieldint().displayaccinfo()

print(" ")
print("checkings:")
acc_two.deposit(125).deposit(124).withdraw(60.42).withdraw(222.22).withdraw(202.20).withdraw(69.69).yieldint().displayaccinfo()

print(" ")

BankAccount.printall()
#Create a BankAccount class with the attributes interest rate and balance

# Add a deposit method to the BankAccount class

# Add a withdraw method to the BankAccount class

# Add a display_account_info method to the BankAccount class

# Add a yield_interest method to the BankAccount class

# Create 2 accounts

# To the first account, make 3 deposits and 1 withdrawal, then yield interest and display the account's info all in one line of code (i.e. chaining)

# To the second account, make 2 deposits and 4 withdrawals, then yield interest and display the account's info all in one line of code (i.e. chaining)

# NINJA BONUS: use a classmethod to print all instances of a Bank Account's info
