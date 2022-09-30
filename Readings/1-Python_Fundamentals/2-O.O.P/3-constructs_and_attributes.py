                            #THE CONSTRUCTOR

#A constructor is a function that contains instructions for making a new instance of a class.
#this is a special function called the __init__ method. 
#When called, this method will designate some space in memory to store the user, and then assign the first name, last name and age by executing the lines below:

class User:
    def __init__(self):
        self.first_name = "Maleko"
        self.last_name = "Osby"
        self.age = 26

                            #MAKING INSTANCES
#by defining the User class, we've defined a new DATA TYPE - User.
#__init__ method creates a user, but when/how does it get called to create new users? User().

#You can use the syntax Your_Class_Name() to create and then store a new instance of a class, in this case,  User() to make and save a new user in memory, but remember, you'll need a variable to store it! For the most part, you'll create your object instances outside the class definition, in the outer or global scope. 

class User:
    def __init__(self):
        self.first_name = "Maleko"
        self.last_name = "Osby"
        self.age = 26
user_maleko = User()
print(user_maleko.first_name, user_maleko.last_name, user_maleko.age)
#prints the above

                            #INTRO TO SELF
#self is a placeholder for future instances, future users, like a blank form.
#when user_maleko = User() is executed, __init__ method is called. the self variable is referring to user_maleko. 
#if you create another variable like, user_2 = User(), the constructor is called again but this time the SELF variable inside the construct will refer to user_2. 

user_2 = User()
print(user_2.first_name)





                            #4) SETTING ATTRIBUTES


                        #INSTANCE ATTRIBUTES
#Instance attributes are defined in the constructor, that special __init__ method, which is called when a new object is instantiated, in this case, when a new type of shoes is added to inventory.
class Shoe:
    def __init__(self):
        self.brand = "Nike"
        self.type = "SB Blazers"
        self.price = 89.99
        self.in_stock = True
#The first parameter of an instance method within a class will be SELF, and the instance attributes are also indicated by self.

#SELF is a reference to the **instance**, not the class, in this case this particular pair of shoes, not the generic SHOE class


#now we create INSTANCES of SHOE outside the scope
skater_shoe = Shoe()
dress_shoe = Shoe()
print(skater_shoe.type) #SB BLAZERS
print(dress_shoe.type) #SB BLAZERS
#We can also set the values for our instance's attributes:
skater_shoe.type = "Grant Taylor Lows"
print(skater_shoe.type)
dress_shoe.type = "Dr. Martins"
print(dress_shoe.type)

                            #PASSING IN ARGUMENTS
#now we're gonna pass in arguments into the __init__ method to specify a shoe's instance attributes.

#When a particular Shoe instance is created, we should expect to receive specific values for the brand, type and price. 
# We'll assume, however, that every shoe starts with in_stock set to true. Let's adjust our code to allow arguments to be passed in upon instantiation, so we can customize all the attributes as soon as it is created:

class Shoe:
    def __init__(self, brand, shoe_type, price):
        #assign accordingly
        self.brand = brand
        self.type = shoe_type
        self.price = price
        self.in_stock = True
skater_shoe = Shoe("Nike", "SB Blazers", 89.99)
dress_shoe = Shoe("Dr Martins", "Leather Platform", 180.00)
print(skater_shoe.type, skater_shoe.price)
print(dress_shoe.type, dress_shoe.price)