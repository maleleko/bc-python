class User:
    def __init__(self, name, int_rate=0.02, balance=0):
        self.name = name
        self.account = {'checkings': BankAccount(int_rate, balance=0), 'savings': BankAccount(int_rate, balance=0)}

    def make_deposit(self, amount, user_acc):
        self.account[user_acc].deposit(amount)
        return self
    
    def make_withdraw(self, amount, user_acc):
        self.account[user_acc].withdraw(amount)
        return self

    def display_acc(self):
        print(f"Checkings: ${self.account['checkings'].balance}")
        print(f"Savings: ${self.account['savings'].balance}")
        return self
    
    def yield_int(self):
        self.account.yield_interest()
        return self

    @staticmethod
    def transfer_dollas(self, amount, other_acc):
        if other_acc in BankAccount is self.account["savings"]:
            self.account -= amount in self.balance["savings"]
            self.account += amount in self.balance["checkings"]
        else: 
            other_acc in BankAccount is self.balance["checkings"]
            self.account -= amount in self.balance["checkings"]
            self.account += amount in self.balance["savings"]
    
    # @staticmethod
    # def transfer_money(amount, user_acc, other_acc):
    #     if user_acc in BankAccount["checkings"].withdraw(amount):
    #         other_acc in BankAccount["savings"].deposit(amount)
    #     else:
    #         user_acc in BankAccount["savings"].withdraw(amount)
    #         other_acc in BankAccount["checkings"].deposit(amount)
    #     return amount

    # @staticmethod
    # def transfer_dollas(self, amount, other_acc):
    #     if self.account in BankAccount["checkings"].withdraw(amount):
    #         other_acc in BankAccount["savings"].deposit(amount)
    #     else:
    #         self.account in BankAccount["savings"].withdraw(amount)
    #         other_acc in BankAccount["checkings"].deposit(amount)
    #     return amount

class BankAccount:
    def __init__(self, int_rate=0.02, balance=0):
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
        # print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

    # @staticmethod
    # def transfer_dollas(self, amount, other_acc):
    #     if other_acc in User is self.account["savings"]:
    #         self.balance -= amount in self.account["savings"]
    #         self.balance += amount in self.account["checkings"]
    #     else: 
    #         other_acc in User is self.account["checkings"]
    #         self.balance -= amount in self.account["checkings"]
    #         self.balance += amount in self.account["savings"]
    
    # @staticmethod
    # def transfer_dollas(amount, user_acc, other_acc):
    #     if user_acc in BankAccount["checkings"].withdraw(amount):
    #         other_acc in BankAccount["savings"].deposit(amount)
    #     else:
    #         user_acc in BankAccount["savings"].withdraw(amount)
    #         other_acc in BankAccount["checkings"].deposit(amount)
    #     return amount

user1 = User("koh")
# savings = User("koh")

user1.display_acc().make_deposit(100,"checkings").make_deposit(1500, "savings").display_acc().make_withdraw(50, "checkings").display_acc()

user1.transfer_dollas(50, "savings", "checkings")
user1.display_acc()
# checkings.withdraw(50).displaybalance()
# checkings.yieldint().displaybalance()
# Update the User class __init__ method

#i will practice with the bonuses later

# SENSEI BONUS: Allow a user to have multiple accounts; update methods so the user has to specify which account they are withdrawing or depositing to


#SENPAI BONUS: Add a transfer_money(self, amount, other_user) method to the user class that takes an amount and a different User instance, and transfers money from the user's account into another user's account.

#TIM HINT
#used static method - for withdraw, we will be able to reuse the withdraw method in our transfer method