#                       Circular Imports


# Since we are building our application in a modularized structure, we need to import files into others.  If we reference how we handled Many to Many relationships, the two classes are dependent on each other in order to make those connections.  One major issue that we might run into is a Circular Imports.


            # topping.py

# from flask_app.models.burger import Burger
# class Topping:
#     ...
#     @classmethod
#     def get_topping_with_burgers(cls, data):
#         ...
#         for row_from_db in results:
#             ...
#             # this is where the topping class
#             # is dependant on the Burger class
#             topping.on_burgers.append(Burger(burger_data))


            # burger.py
# from flask_app.models.topping import Topping
# class Burger:
#     ...
#     @classmethod
#     def get_burger_with_toppings(cls, data):
#         ...
#         for row_from_db in results:
#             ...
#             # this is where the Burger class
#             # is dependent on the Topping class
#             burger.toppings.append(Topping(topping_data))


# We will end up with an error that looks like this:
    # https://s3.us-east-1.amazonaws.com/General_V88/boomyeah2015/codingdojo/curriculum/content/chapter/1631547701__Screen%20Shot%202021-09-13%20at%2010.40.30%20AM.png

# The reason for this error is because we are importing each class into the other and trying to invoke the instances when relating them together. Creating a circular import, which is bad and breaks our code.

# ** To fix this issue we need to adjust our code and import the file instead of the classes. **

# Refactored Code in topping.py
    # from flask_app.models import burger
    # topping.on_burgers.append(burger.Burger(burger_data))

# Refactored Code in burger.py
    # from flask_app.models import topping
    # burger.toppings.append(topping.Topping(topping_data))