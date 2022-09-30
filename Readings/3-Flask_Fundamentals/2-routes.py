#                       ROUTES

# A route is much like a variable name we assign to a request.
    #The job of a route is to communicate to the server what kind of information the client needs.


# Every route has two parts:
    #1).  HTTP method (GET, POST, PUT, PATCH, DELETE)
    #2). URL

# Setting Up your Routes
    # Let's add a route to our server.
    # # import statements, maybe some other routes
    
        # @app.route('/success')
            # def success():
            #return "success"
        # app.run(debug=True) should be the very last statement! 

# Now we have 2 routes--if the client requests localhost:5000/, the hello_world function will run. But if the client requests localhost:5000/success, the success function will run.

# if we wanted to add a "Hello, Michael" or "Hello, Amy" we could make 3 routes, but that's repetitive. Here is a great opportunity to add VARIABLE RULES to our routes. 
# for the example above, we could make the name a variable like so.

        # @app.route('/hello/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
        #     def hello(name):
        #     print(name)
        #     return "Hello, " + name


# We can add as many of these as we need, giving each var a diff name.

# @app.route('/users/<username>/<id>') # for a route '/users/____/____', two parameters in the url get passed as username and id
# def show_user_profile(username, id):
#     print(username)
#     print(id)
#     return "username: " + username + ", id: " + id

# The localhost:8000 part of the route determines which server to call upon. The rest of the route, including the "/", tells the server which function should be invoked.

