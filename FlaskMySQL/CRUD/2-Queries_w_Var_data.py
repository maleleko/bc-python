#               Queries with Variable Data


# With our SELECT * FROM friends statement, we are just asking for everything from the database. However, we will often want to provide variable data in the query that would be terrible to hard-code into the query.

    # SELECT * FROM friends WHERE id=1 (where the actual id number will vary)
    # UPDATE friends SET first_name="Bryanna" WHERE id=9 (where the actual first name and id will vary)

# **Whenever we run a query that includes variables, we should use a prepared statement rather than string interpolation**
# In other words, use the following pattern instead of f-strings or string concatenation
# Practically what this means is that we'll need a string variable for the query and then a dictionary for the values to be used in the string
# When we call on the database connection to execute the query, we will pass both the query and the dictionary, like so:

    #query = "UPDATE friends SET first_name=%(fn)s WHERE id=%(id_num)s;"
    # data = {
    # "fn": #possibly a value from a form
    # "id_num": #possibly a value from the url,
    # }
    # mysql.query_db(query, data)

        # connection to the db - mysql - the instance of the MySQLConnection class
        # query string - "INSERT INTO ..." - the string that will eventually be executed on our MySQL server
        # data dictionary - the values that will be interpolated into the query string
        # data dictionary keys - fn, id_num - the keys of the data dictionary used in the query string with %-interpolation
            # (i.e. %(key_name)s)