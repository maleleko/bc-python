#classes are the blueprints in OOP

#declaring x = [1,2,3], x is an INSTANCE of a list. an instance is simply an object that follows the pattern defined by its class.

# https://s3.us-east-1.amazonaws.com/General_V88/boomyeah2015/codingdojo/curriculum/content/chapter/1620316939__blue_print.png

class User:
    pass #we'll fill this out momentarily

#As almost all applications revolve around users, they should define a User class. Instead of allowing a user to define their own properties, we set a standard for what a user should have on our website.  This ensures consistent creation of User instances.

#heres how we create a new instance of our class:
michael = User()
anna = User()

#Attributes: Characteristics shared by all instances of the class type.
#Methods: Actions that an object can perform. A user in a banking application, for example, may need to be able to calculate age based on the user's birthday or open a new bank account associated with that user.

#shoe class
# https://s3.us-east-1.amazonaws.com/General_V88/boomyeah2015/codingdojo/curriculum/content/chapter/1651097927__shoes_class.png