                            #METHODS

#methods are just functions that belong to a class. meaning we can't call them independently as we have called functions previous. methods must be called fom an instance of a class.

#we want to get custom greetings for users, like "Hello my name is Adrien!" we want to be able to call the method FROM THE USER INSTANCE using dot notation, bc each user has a different name. making such a call would look something like this:

# adrien.greeting()

#to be able to call on this method, it needs to exist.
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        #add greeting method
    def greeting(self):
        print(f"Hello,my name is {self.name}.", f"My email is {self.email} if you'd like to get in contact with me!")
#the FIRST PARAMETER of EVERY METHOD within a class should be SELF.
#notice that, whatever arguments are passed in as a trad funct, METHODS ALSO HAVE ACCESS TO THE CLASS'S ATTRIBUTES

adrien = User("Adrien", "adion@codingdojo.com")
cool_person = User("Sadie", "sflick@codingdojo.com")
adrien.greeting()
cool_person.greeting()


                            #SELF
#The self parameter includes all the information about the individual object that has called the method.
#But how does it get passed in? Based on the signature for the __init__ method, it requires 3 arguments. However, when we call on it, we only pass in two.
#Likewise the greeting method requires one argument, but we call it with no arguments. What's happening here? Because we are calling on the method from the instance, this is known as "IMPLICIT PASSAGE OF SELF".
#When we call on a method from an instance, the memory address of that instance, along with all of its information (name, email, balance), is passed in as SELF.




                            #METHODS AND UPDATING ATTRIBUTES
#changing shoes without methods
#lets take the 'on sale' functionality we want to implement, what would it look like without writing an methods?

class Shoe:
    def __init__(self, brand, shoe_type, price):
        #assign accordingly
        self.brand = brand
        self.type = shoe_type
        self.price = price
        self.in_stock = True
skater_shoe = Shoe("Nike", "SB Blazers", 89.99)
dress_shoe = Shoe("Dr Martins", "Leather Platform", 180.00)

#skater shoe goes on sale by 20%:
skater_shoe.price = skater_shoe.price * (1 - 0.2)
#dress shoe goes on sale by 10%:
dress_shoe.price = dress_shoe.price * (1 - 0.1)
#skater shoe on sale again with an additional 10%:
skater_shoe.price = skater_shoe.price * (1 - 0.1)

#we want to follow the D.R.Y mantra, Dont Repeat Yourself.

                            #methods and using self
#we're gonna move the above code into a method. 

class Shoe:
    def __init__(self, brand, shoe_type, price):
        #assign accordingly
        self.brand = brand
        self.type = shoe_type
        self.price = price
        self.in_stock = True

        #heres our new percentage method
    def sale_by_perc(self, percent):
        self.price = self.price * (1 - percent)
skater_shoe = Shoe("Nike", "SB Blazers", 89.99)
dress_shoe = Shoe("Dr Martins", "Leather Platform", 180.00)
skater_shoe.sale_by_perc(0.2)
print(skater_shoe.price)

#if we want to put in some sort of tax rate
class Shoe:
    def __init__(self, brand, shoe_type, price):
        #assign accordingly
        self.brand = brand
        self.type = shoe_type
        self.price = price
        self.in_stock = True

        #heres our new method
    def sale_by_perc(self, percent):
        self.price = self.price * (1 - percent)

        #tax rate method here
    def totalwtax(self, tax_rate):
        tax = self.price * tax_rate
        total = self.price  + tax
        return total

        #heres an example with a cut price method
    def cutpriceby(self, amount):
        if amount < self.price:
            self.price -= amount
        else:
            print("nah we not makin money.")
skater_shoe = Shoe("Nike", "SB Blazers", 89.99)
dress_shoe = Shoe("Dr Martins", "Leather Platform", 180.00)
# skater_shoe.sale_by_perc(0.2)
# print(skater_shoe.totalwtax(0.095))
skater_shoe.cutpriceby(10)
print(skater_shoe.price)
dress_shoe.cutpriceby(80)
print(dress_shoe.price)