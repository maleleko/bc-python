                    # Default Form Submission

# Forms typically come with submit buttons. Submit buttons, however, cause the browser to make a request to the url in the action attribute. In other words, the browser redirects to that url, which we don't want if we are using AJAX to submit the form. For example, consider the code below:

    # <form action='/new_destination' id='myForm' method='post'>
        # <label for="name">Name: </label>
        # <input type='text' name='name'>
        # <input type='submit' id='submit_btn' value='Submit'>
    # </form>

    # <script>
    #     var myForm = document.getElementById('myForm');
    #     myForm.onsubmit = function(e){
    #         // "e" is the event happening when we submit the form.
    #         // do something here ...
    #     }
    # </script>

# When the submit button is clicked, it will send an invoke the function and submit the form normally. This means the browser will redirect to "/new_destination".  To prevent the browser from going to that page directly, you need to add e.preventDefault() so that it does not submit the form normally.

# In other words, your code would now look like this

    # <form  id="myForm" method="post">
        # <label for="name">Name: </label>
        # <input type="text" name="name">
        # <input type="submit" id="submit_btn" value="Submit">
    # </form>
    
    # <script>
    #     var myForm = document.getElementById('myForm');
    #     myForm.onsubmit = function(e){
    #         // "e" is the js event happening when we submit the form.
    #         // e.preventDefault() is a method that stops the default nature of javascript.
    #         e.preventDefault();
    #         // do something here ...
    #     }
    # </script>




                    # POST Requests w/ Fetch


# Now that we can disable Javascript's default behavior on a form, we need to send the form data to our Flask server via fetch().

    # <form id="myForm" method="post">
    #     <label for="name">Name: </label>
    #     <input type="text" name="name">
    #     <input type="submit" id="submit_btn" value="Submit">
    # </form>
    
    # <script>
    #     var myForm = document.getElementById('myForm');
    #     myForm.onsubmit = function(e){
    #         // "e" is the js event happening when we submit the form.
    #         // e.preventDefault() is a method that stops the default nature of javascript.
    #         e.preventDefault();
    #         // create FormData object from javascript and send it through a fetch post request.
    #         var form = new FormData(myForm);
    #         // this how we set up a post request and send the form data.
    #         fetch("http://localhost:5000/create/user", { method :'POST', body : form})
    #             .then( response => response.json() )
    #             .then( data => console.log(data) )
    #     }
    # </script>

# We need to make sure that our server will be able interpret the form data in the request, so we need to create an instance of Javascript's FormData object.

# var form = new FormData( formData)



# For more on the FormData Object.
    # https://developer.mozilla.org/en-US/docs/Web/API/FormData/Using_FormData_Objects



        # Meanwhile somewhere in our a controller file . . .

    # from flask_app.models.user import User
    # from flask_app import app
    # from flask import render_template, jsonify, request, redirect
    # @app.route('/create/user',methods=['POST'])
    # def create_user():
    #     print(request.form)
    #     # write code to save it to our database . . .
    #     return jsonify(message="Add a user!!!")