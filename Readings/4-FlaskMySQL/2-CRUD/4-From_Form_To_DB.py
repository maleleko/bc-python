#                   From Form To DB


# Now that we can retrieve friends, let's add the functionality that allows us to create a friend.  We first need to create a @classmethod to create a row in the data base.

    # first_flask_mysql/friend.py

# # import the function that will return an instance of a connection
# from mysqlconnection import connectToMySQL
# # model the class after the friend table from our database
# class Friend:
#     # ... other class methods
#     # class method to save our friend to the database
#     @classmethod
#     def save(cls, data ):
#         query = "INSERT INTO friends ( first_name , last_name , occupation , created_at, updated_at ) VALUES ( %(fname)s , %(lname)s , %(occ)s , NOW() , NOW() );"
#         # data is a dictionary that will be passed into the save method from server.py
#         return connectToMySQL('first_flask').query_db( query, data )



# ** Remember that because this query includes variables, we should use a prepared statement.  **

# To Python, the query variable is just a string, and the data dictionary just another variable. But when passed to our MySQL server through our PyMySQL connection, our MySQL database understands the string as a query it can execute!

# Next let's add a form to our template:
    # first_flask_mysql/templates/index.html
        # <h1>Add a Friend</h1>
        # <form action="/create_friend" method="POST">
        #     <label for="fname">First Name:</label>
        #     <input type="text" name="fname">
        #     <label for="lname">Last Name:</label>
        #     <input type="text" name="lname">
        #     <label for="occ" >Occupation:</label>
        #     <input type="text" name="occ">
        #     <input type="submit" value="Add Friend">
        # </form> 

# Now we need a method to handle the submission of our form. Let's update our server.py file and pass the request.form into the save method from the Friend class.

# first_flask_mysql/server.py
    # # relevant code snippet from server.py
    # from friend import Friend
    # @app.route('/create_friend', methods=["POST"])
    # def create_friend():
    #     # First we make a data dictionary from our request.form coming from our template.
    #     # The keys in data need to line up exactly with the variables in our query string.
    #     data = {
    #         "fname": request.form["fname"],
    #         "lname" : request.form["lname"],
    #         "occ" : request.form["occ"]
    #     }
    #     # We pass the data dictionary into the save method from the Friend class.
    #     Friend.save(data)
    #     # Don't forget to redirect after saving to the database.
    #     return redirect('/')


# Once the data has been processed, remember to redirect, because we don't want to render on a post!

# Note: We have set up the query_db method so that each attempted query will be printed to the terminal. Whenever the query you put together does not seem to work or gives an error message, investigate the actual query being run in the terminal. You may try copying and pasting the query into MySQL Workbench to see if you have the right syntax.