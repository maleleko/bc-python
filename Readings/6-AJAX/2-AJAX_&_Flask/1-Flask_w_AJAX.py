# Now that we understand how to use fetch to get data from another server, the next step is to be able to communicate with our own servers.  In our flask app we will start responding with JSON instead of rendering templates.

    # Somewhere in a controller file . . . 
        # from flask import jsonify
        # from flask_app import app
        # @app.route('/get_data')
        # def get_data():
        #     # jsonify will serialize data into JSON format.
        #     return jsonify(message="Hello World")

    # Somewhere in your static javascript file . . .
        # function getData(){
        #     fetch('http://localhost:5000/get_data')
        #         .then( response => response.json() )
        #         .then( data => console.log(data) )
        # }
        # // Prints out { message : "Hello World" }
        # getData();

# And now we can fetch data from our own server!!!

# To understand this process a bit further let's create an example together.

    # 1.) Go ahead and create a new ERD in MySQL workbench that looks like this with the schema called user_names:
        # https://s3.us-east-1.amazonaws.com/General_V88/boomyeah2015/codingdojo/curriculum/content/chapter/1624297221__Screen%20Shot%202021-06-21%20at%2012.40.08%20PM.png
            # https://s3.us-east-1.amazonaws.com/General_V88/boomyeah2015/codingdojo/curriculum/content/chapter/1624297391__user_names.mwb

    # 2.) Once you created the ERD, or dowloaded the file and opened in MySQL Workbench, go ahead and forward engineer it to your local database.

    # 3.) Create a couple of rows in your users table using a SQL query.

    # 4.) Download this basic MVC Flask App.  Make sure to change the mysql password for your config file to your own password!!!
        # https://s3.us-east-1.amazonaws.com/General_V88/boomyeah2015/codingdojo/curriculum/content/chapter/1624305079__form_data.zip

    # 5.) Once opened in VSCode, run pipenv install flask PyMySQL in the terminal.

    # 6.) Then run the server.


# We are now rendering a template for our index route and using our javascript file to get the data and insert it into the table.

# https://s3.us-east-1.amazonaws.com/General_V88/boomyeah2015/codingdojo/curriculum/content/chapter/1624303409__user_names.gif