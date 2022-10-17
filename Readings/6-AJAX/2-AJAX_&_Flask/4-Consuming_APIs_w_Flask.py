# Once you have obtained an API Key we can now use it to retrieve information for other servers in our flask app. And it will be secure!  In order to make those http requests from flask, we need a helpful module.


                # Requests Module

# The requests module allows us to consume APIs from a python file.  In order for us to use it, we must first install it in our virtual environment.
    # pipenv install requests

# Once we have it installed, we need to import in whatever file we will use it. In our case, we will use it in one of our controller files.

# Somewhere in a controller file . . .
    # import requests
    # from flask_app import app
    # import os
    # from flask import jsonify
    # @app.route('/searching'):
    #     r = requests.get(f"https:api.information.com/{os.environ.get('FLASK_API_KEY')}")
    #     # we must keep in line with JSON format.
    #     # requests has a method to convert the data coming back into JSON.
    #     return jsonify( r.json() )

# Notice in the code snippet above that we are making our api request in python and injecting the API key into the string

# NOTE: Not all API keys are use in the same manner, so it is important to read the API documentation.




                    # From Front-end to Back-end

# Now the only missing piece to create a way for the front end to invoke the search method in our controller.  And we might also what to send some search parameters in our query as well.  To do this we must first create a form on the front-end.

# index.html
    # <form id="searchForm" onsubmit="search(event)" >
    #     <h2>Search</h2>
    #     <input type="text" name="query">
    #     <input type="submit" value="Search" >
    # </form>

# Now we want to create a function in our JavaScript file that prevents default behavior and send the query to the server to make the call.

# script.js
    # function search(e){
    #     e.preventDefault();
    #     var searchForm = document.getElementById('searchForm')
    #     var form = new FormData(searchForm);
    #     fetch('http://localhost:5000/search',{method:'POST',body:form})
    #         .then(res => res.json() )
    #         .then( data => console.log(data) )
    # }

# We need to reconfigure the controller code above to accept our form data.

# Somewhere in a controller file...
    # import requests
    # from flask_app import app
    # import os
    # from flask import jsonify, requests
    # @app.route('/searching',methods=['POST']):
    #     print(request.form['query'])
    #     # now we inject the query into our string
    #     r = requests.get(f"https:api.information.com/{os.environ.get('FLASK_API_KEY')}/search?={request.form['query']}")
    #     # we must keep in line with JSON format.
    #     # requests has a method to convert the data coming back into JSON.
    #     return jsonify( r.json() )


# We now have all the tools to securely call our APIs and make our applications more interactive!!!

# For more documentation on the requests module.
    # https://docs.python-requests.org/en/latest/user/quickstart/