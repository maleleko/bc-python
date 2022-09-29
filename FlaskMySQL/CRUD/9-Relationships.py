#                   Relationships One to Many

# When dealing with either one-to-many or many-to-many relationships, we know SQL only saves the id or foreign key in the table on the many side of the relationship. The foreign key is a primary key of a different table. Because of this, we can display the data that is already saved in the database, that is needed in the relationship.

# Let's say we wanted to relate restaurants to certain burgers. A restaurant can have many burgers but a burger can only belong to one restaurant. We need to create a class for the restaurant and a table in our database and then associate the Burger class in the Restaurant class.

        # https://s3.us-east-1.amazonaws.com/General_V88/boomyeah2015/codingdojo/curriculum/content/chapter/1631560504__Screen%20Shot%202021-09-10%20at%202.42.16%20PM.png

# models/restaurant.py
    # class Restaurant:
    #     def __init__(self , db_data ):
    #         self.id = db_data['id']
    #         self.name = db_data['name']
    #         self.created_at = db_data['created_at']
    #         self.updated_at = db_data['updated_at']
    #         # We create a list so that later we can add in all the burgers that are associated with a restaurant.
    #         self.burgers = []
    #     @classmethod
    #     def save( cls , data ):
    #         query = "INSERT INTO restaurants ( name , created_at , updated_at ) VALUES (%(name)s,NOW(),NOW());"
    #         return connectToMySQL('burgers').query_db( query, data)

# Now when we create a burger we will need the id of the restaurant in order to create the burger. For this we must set it up in the form, and when we render the form for the burger we need to pass in a list of all the restaurants into a select tag.

    # <form action="/create/burger" method="post">
    # ...
    #     <select name="restaurant_id">
    #     <!-- Need to create an option list for the user to select a restaurant. -->
    #     <!-- Note that we are passing the restaurant id into the value -->
    #     {% for restaurant in all_restaurants %}
    #     <option value={{restaurant.id}}>{{restaurant.name}}</option>
    #     {% endfor %}
    #     </select>
    # </form>

# models/burger.py
    # @classmethod
    # def save( cls , data ):
    #     query = "INSERT INTO burgers ( name , bun, meat, calories, restaurant_id, created_at , updated_at ) VALUES (%(name)s, %(bun)s, %(meat)s, %(calories)s, %(restaurant_id)s,NOW(),NOW());"
    #     return connectToMySQL('burgers').query_db(query,data)


                    # Parsing Data into Associated Classes

# Now we can create a class method in our Restaurant class that will associate all the burgers with the restaurant.

# models/restaurant.py
        # # We need to import the burger class from our models
        # from flask_app.models import burger
        # class Restaurant:
        #     ...
        #     @classmethod
        #     def get_restaurant_with_burgers( cls , data ):
        #         query = "SELECT * FROM restaurants LEFT JOIN burgers ON burgers.restaurant_id = restaurants.id WHERE restaurants.id = %(id)s;"
        #         results = connectToMySQL('burgers').query_db( query , data )
        #         # results will be a list of topping objects with the burger attached to each row. 
        #         restaurant = cls( results[0] )
        #         for row_from_db in results:
        #             # Now we parse the burger data to make instances of burgers and add them into our list.
        #             burger_data = {
        #                 "id" : row_from_db["burgers.id"],
        #                 "name" : row_from_db["burgers.name"],
        #                 "bun" : row_from_db["bun"],
        #                 "meat" : row_from_db["meat"],
        #                 "calories" : row_from_db["calories"],
        #                 "created_at" : row_from_db["burgers.created_at"],
        #                 "updated_at" : row_from_db["burgers.updated_at"]
        #             }
        #             restaurant.burgers.append( burger.Burger( burger_data ) )
        #         return restaurant

# NOTE: Common columns that exists on the table will come back from in our results with the table name attached.