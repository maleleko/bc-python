

class User:
    def __init__(self, name, int_rate=0.02, balance=0):
        self.name = name
        self.account = {'Checkings': BankAccount(int_rate, balance=0), 'Savings': BankAccount(int_rate, balance=0)}

    def make_deposit(self, amount, user_acc):
        self.account[user_acc].deposit(amount)
        return self
    
    def make_withdraw(self, amount, user_acc):
        self.account[user_acc].withdraw(amount)
        return self

    def display_acc(self):
        print(f"Checkings: ${self.account['Checkings'].balance}")
        print(f"Savings: ${self.account['Savings'].balance}")
        
        return self
    
    def yield_int(self):
        self.account.yield_interest()
        return self
        
        #transferring between individual accounts
    def transfer_dollas(self, amount, acc_type, other_acc_type):
        self.display_acc() #just some fun stuff
        print(f"Withdrawing from: {acc_type}") #just some fun stuff

        self.account[acc_type].withdraw(amount) #ACTUAL FUNCTION OPERATION

        self.display_acc() #just some fun stuff
        print(f"Depositing into: {other_acc_type}") #just some fun stuff

        self.account[other_acc_type].deposit(amount) #ACTUAL FUNCTION OPERATION

        self.display_acc() #just some fun stuff
        print("Transfer Complete") #just some fun stuff
        return self
            
            
            #tranfferring from one user to another
    def tranfer_toandfrom(self, user_acc, amount, acc_type, another_useracc, other_usersacc_type):
        print("INITIALIZING TRANSFER..") #just some fun stuff
        print(f"{user_acc.name}'s Account") # just some fun stuff
        self.display_acc() #just some fun stuff
        print(f"{another_useracc.name}'s Account") #just some fun stuff
        another_useracc.display_acc() #just some fun stuff
        print(f"TRANSFERRING FROM: {user_acc.name}'s {acc_type}...") #just some fun stuff
        print(f"TO: {another_useracc.name}'s {other_usersacc_type}...") #just some fun stuff
        print(f"{user_acc.name}'s Account New Balance") #just some fun stuff

        user_acc.account[acc_type].withdraw(amount) #ACTUAL FUNCTION OPERATION
        another_useracc.account[other_usersacc_type].deposit(amount) #ACTUAL FUNCTION OPERATION

        self.display_acc() #just some fun stuff
        print(f"{another_useracc.name}'s Account New Balance") #just some fun stuff
        another_useracc.display_acc() #just some fun stuff
        print("TRANSFER SUCCESSFUL.") #just some fun stuff
        return self

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


user1 = User("Maleko")
user2 = User("Svet")
#_____________________

print("______________")
print("Maleko's Account")
user1.make_deposit(200, "Checkings").make_deposit(500, "Savings").display_acc()
print("______________")

print(" ")

print("______________")
print("Svet's Account")
user2.make_deposit(1000, "Checkings").make_deposit(5000, "Savings").display_acc()
print("______________")

print(" ")

print("______________")
user1.transfer_dollas(50, "Checkings", "Savings")
print("______________")

print(" ")

print("______________")
user1.tranfer_toandfrom(user1, 50, "Checkings", user2, "Savings")
print("______________")


# Update the User class __init__ method

#i will practice with the bonuses later

# SENSEI BONUS: Allow a user to have multiple accounts; update methods so the user has to specify which account they are withdrawing or depositing to


#SENPAI BONUS: Add a transfer_money(self, amount, other_user) method to the user class that takes an amount and a different User instance, and transfers money from the user's account into another user's account.

#TIM HINT
#used static method - for withdraw, we will be able to reuse the withdraw method in our transfer method
#didnt end up using this


#things that didnt work but tired my best
    # @staticmethod
    # def transfer_dollas(self, amount, other_acc):
    #     if other_acc in BankAccount is self.account["savings"]:
    #         self.account -= amount in self.balance["savings"].withdraw()
    #         self.account += amount in self.balance["checkings"].deposit()
    #     else: 
    #         other_acc in BankAccount is self.balance["checkings"]
    #         self.account -= amount in self.balance["checkings"]
    #         self.account += amount in self.balance["savings"]
    
    # @staticmethod
    # def transfer_dollas(amount, user_acc, other_acc):
    #     if user_acc in BankAccount["checkings"].withdraw(amount):
    #         other_acc in BankAccount["savings"].deposit(amount)
    #     else:
    #         user_acc in BankAccount["savings"].withdraw(amount)
    #         other_acc in BankAccount["checkings"].deposit(amount)
    #     return amount

    

    #      "name": "Variables",
    #   "scope": "variable",
    #   "settings": {
        # "foreground": "#e06c75"

    #        "name": "js variable readwrite",
    #   "scope": "variable.other.readwrite,meta.object-literal.key,support.variable.property,support.variable.object.process,support.variable.object.node",
    #   "settings": {
    #     "foreground": "#e06c75"