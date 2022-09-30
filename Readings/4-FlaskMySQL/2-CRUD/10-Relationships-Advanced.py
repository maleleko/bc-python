#                   Relationships Advanced



#               Many to Many Relationships
# Let's say we wanted to start adding toppings onto our burgers.  Let's look at the ERD of how we can add Toppings to our application.
        # https://s3.us-east-1.amazonaws.com/General_V88/boomyeah2015/codingdojo/curriculum/content/chapter/1631304952__Screen%20Shot%202021-09-10%20at%203.15.26%20PM.png

# As you can see, we need a middle table to relate the topping to the burger.  A burger can have many toppings and a topping can be on many burgers. 

# Now we need to create our Topping class to line up with our Toppings Table in our database. Along with the class methods to associate our classes together.

# We will use this query to get the data we need to associate our Burgers to Topping class.
    # "SELECT * FROM toppings 

    # LEFT JOIN add_ons ON add_ons.topping_id = toppings.id 

    # LEFT JOIN burgers ON add_ons.burger_id = burgers.id 

    # WHERE toppings.id = %(id)s;"


# models/topping.py

    # # We will need to import burger.py to access the class
    # from flask_app.models import burger
    # class Topping:
    #     def __init__( self , db_data ):
    #         self.id = db_data['id']
    #         self.topping_name = db_data['topping_name']
    #         # we need have a list in case we want to show which burgers are related to the topping.
    #         self.on_burgers = []
    #         self.created_at = db_data['created_at']
    #         self.updated_at = db_data['updated_at']

    #     @classmethod
    #     def save( cls , data ):
    #         query = "INSERT INTO toppings ( topping_name, created_at , updated_at ) VALUES (%(topping_name)s,NOW(),NOW());"
    #         return connectToMySQL('burgers').query_db(query, data)
    #     # This method will retrieve the specific topping along with all the burgers associated with it.
    #     @classmethod
    #     def get_topping_with_burgers( cls , data ):
    #         query = "SELECT * FROM toppings LEFT JOIN add_ons ON add_ons.topping_id = toppings.id LEFT JOIN burgers ON add_ons.burger_id = burgers.id WHERE toppings.id = %(id)s;"
    #         results = connectToMySQL('burgers').query_db( query , data )
    #         # results will be a list of topping objects with the burger attached to each row. 
    #         topping = cls( results[0] )
    #         for row_from_db in results:
    #             # Now we parse the topping data to make instances of toppings and add them into our list.
    #             burger_data = {
    #                 "id" : row_from_db["burgers.id"],
    #                 "name" : row_from_db["name"],
    #                 "bun" : row_from_db["bun"],
    #                 "calories" : row_from_db["calories"],
    #                 "created_at" : row_from_db["toppings.created_at"],
    #                 "updated_at" : row_from_db["toppings.updated_at"]
    #             }
    #             topping.on_burgers.append( burger.Burger( burger_data ) )
    #         return topping


# Now we add in a class method into our burger class to associate the classes together.

# We will use this query to get the data we need to associate our Toppings to the Burger class.

        # "SELECT * FROM burgers 

        # LEFT JOIN add_ons ON add_ons.burger_id = burgers.id 

        # LEFT JOIN toppings ON add_ons.topping_id = toppings.id 

        # WHERE burgers.id = %(id)s;"

# models/burger.py

# we need to import the topping class from our models
# from burgers.flask_app.config.mysqlconnection import connectToMySQL
# from flask_app.models import topping
# class Burger:
#     def __init__( self, data):
#         self.id = data['id']
#         self.id = data['name']
#         self.bun = data['bun']
#         self.meat = data['meat']
#         self.calories = data['calories']
#         self.created_at = data['created_at']
#         self.updated_at = data['updated_at']
#         # we now create a list so that later we can add in all the topping objects that relate to a burger.
#         self.toppings = []
#         # this method will retrieve the burger with all the toppings that are associated with the burger.

#     @classmethod
#     def get_burger_with_toppings(cls, data):
#         query = "SELECT * FROM burgers LEFT JOIN add_ons ON add_ons.burger_id = burgers.id LEFT JOIN toppings ON add_ons.topping_id = toppings.id WHERE burgers.id = %(id)s;"
#         results = connectToMySQL('burgers').query_db(query, data)
#         # results will be a list of topping objects with the burger attached to each row.         
#         burger = cls(results[0])
#         for row_from_db in results:
#             # Now we parse the topping data to make instances of toppings and add them into our list.
#             topping_data = {
#                 "id": row_from_db["toppings.id"],
#                 "topping_name": row_from_db["topping_name"],
#                 "created_at": row_from_db["toppings.created_at"],
#                 "updated_at": row_from_db["toppings.updated_at"]
#             }
#             burger.toppings.append( topping.Topping(topping_data) )
#             return burger

# NOTE: Common columns that exists on the table will come back from in our results with the table name attached.