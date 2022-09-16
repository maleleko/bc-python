                            #Class vs Instance
#we can also declare and set attributes that don't belong to a single instance but to the class itself.
#normally when we create a method on a class we pass in SELF to refer to the **instance** of the object. these are referred to as **instance methods**

                            #Class Attributes
#Class Attributes are defined outside of any instance methods, and is shared among all instances of the class. 

class BankAccount:
    #declaring a class attr
    #shared among all bank accs
    bank_name = "First National Dojo"

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
#Class attr's are more flexible bc we can change them on an instance or the entire class.

#changing them on an instance:
adriensAccount = BankAccount()
sadiesAccount = BankAccount()
adriensAccount.bank_name = "Dojo Credit Union"

print(adriensAccount.bank_name)
#output "dojo credit union"

print(sadiesAccount.bank_name)
#output 'first national dojo

#changing them on the entire class:
BankAccount.bank_name = 'Bank of Dojo'

print(adriensAccount.bank_name)
#output 'bank of dojo'

print(sadiesAccount.bank_name)
#output 'bank of dojo'


                            #@classmethod
#class methods are defined with a decorator @classmethod. they belong to the class itself instead of the instance. instead of implicitly passing SELF into the method, we pass CLS. this is reference to the class.

#this is how we write @classmethods

class BankAccount:
    
    bank_name = 'first national dojo'
    #new class attr, a list of all the docs
    all_accounts = []

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
        #class method to change the name of the bank

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name
        
        #class method to get balance of all accs
    @classmethod
    def all_balances(cls):
        sum = 0 
        #we use cls to refer to the class
        for account in cls.all_accounts:
            sum += account.balance
        return sum

#its important to know that class methods have no access to the instance attr or any attr that starts with SELF.



                            #@staticmethod
#static methods are functions define with the class with a decorator @staticmethod
#they have no access on instance or class attr's so if we need any existing values, they need to be passed in as argu's.

#if we wanted our BankAccount class to have a utility function to add or subtract, we could implement @staticmethod

class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def with_draw(self, amount):
        #we can use static method here to eval
        #if we can with draw the funds without going neg
        if BankAccount.can_withdraw(self.balance, amount):
            self.balance -= amount
        else:
            print("Insufficient Funds")
        return self
    #static methods have no access to any attr
    #only to what is passed into it
    @staticmethod
    def can_withdraw(balance, amount):
        if (balance - amount) < 0:
            return False
        else:
            return True

#static methods offer us the opportunity to organize our code in a better way. 
#we could do a simple check to see if the account can be withdrawn from, but what if we want to scale up our application with more logic around this idea? well then we would have to update everywhere we are making that eval, but if put it in a @staticmethod, then we can update all the checks from one place. and our code becomes a bit more D.R.Y
