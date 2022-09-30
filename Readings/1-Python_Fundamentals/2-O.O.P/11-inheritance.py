# inheritance,is defining a new class based on another class
# it allows one class to take on the attributes and methods from another class with little additional code

class BankAccount:
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else: 
            self.balance -= amount
        return self

    def display_acc_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

#no point in creating 2 separate classes when they share multiple attr's/methods. 
#REMEMBER D.R.Y
#instead we can create 2 separate classes that belong to the main class

class CheckingAccount(BankAccount):
    pass

class RetirementAccount(BankAccount):
    def __init__(self, int_rate, is_roth, balance=0): #we've added IS_ROTH, a separate parameter only available to RetirementAccount class
        self.int_rate = int_rate
        self.is_roth = is_roth
        self.balance = balance
#but since our BankAccount class already does 2 of the 3 lines of code for RetirementAccount class, we don't need them in our __init__ method.

class RetirementAccount(BankAccount):
    def __init__(self, int_rate, is_roth, balance=0):
        super().__init__(int_rate, balance) #here we call on BankAccount class parameter, with super().__init__ and specified which parameters we wanted to grab from BankAccount
        self.is_roth = is_roth #<--- this is the only new line we to add tbh.

#say we wanted to add some extra logic to our withdraw() method inside RetirementAccount
    def withdraw(self, amount, is_early): #<-- add a new parameter we want to utilize
        if is_early: #<-- add our new logic before we want to call on the method below.
            amount = amount *1.10
        super().withdraw(amount) #<-- literally just add super().METHODNAME(parameterhere)
        return self

