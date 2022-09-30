#                       Basic Form Validation


# Form validation is a key component of any back-end developer's arsenal. Validation is more of a logical challenge than a whole bunch of new code to learn. Common validation rules include:
    # Checking that the data is present
    # Making sure the data is in the correct format

# The most important validation tool is the if/else statement. Every validation is conditional! IF the data is not valid, we should let the user know, ELSE we should process it and update our database. Form validation centers around using if statements combined with functions that return TRUE or FALSE depending on whether the data given is valid.

# ______________________________________________________________________________________

                        # Step 1: Validation Method on Model

# Let's put some validations on our burger.  We are going to use @staticmethod to validate our form data:

# models/burger.py
# from flask import flash
# class Burger:
#     # Other Burger methods up yonder.
#     # Static methods don't have self or cls passed into the parameters.
#     # We do need to take in a parameter to represent our burger

#     @staticmethod
#     def validate_burger(burger):
#         is_valid = True #we assume this is true
#         if len(burger['name']) < 3:
#             flash("Name must be at least 3 characters.")
#             is_valid = False
#         if len(burger['name']) < 3:
#             flash("Bun must be at least 3 characters.")
#             is_valid = False
#         if int(burger['calories']) < 200:
#             flash("Calories must be 200 or greater.")
#             is_valid = False
#         if len(burger['meat']) < 3:
#             flash("Bun must be at least 3 characters.")
#             is_valid = False
#         return is_valid

        # Flash
# Flash uses session so that we can "flash" our error messages on the form page.  Luckily, ** flash messages are strings that exist for just one redirect cycle!**  The difference between flash and session is that flash messages only last for one redirect while session stays until it is manually popped. **This makes flash messages perfect for validations where we only need to display the error or message temporarily!**

# In order to use flash, we must import it into our models. Under the hood, flash messages utilize session, so we need to make sure that session is setup in our __init__.py.

# Now using flash is as easy as invoking the flash function and passing in a string message! Let's first see how this would look in the if statement. Next we'll see how to display the messages on the client-side.

# ______________________________________________________________________________________

                                # Step 2: Passing Form Data

# In our controller file, we accept a POST method and send validate the from using the Model:
    # controllers/burgers.py

# from flask_app.models.burger import Burger
# @app.route('/create', methods=['POST'])
# def create_buger():
#     # if there are errors:
#     # we call the staticmethod on Burger model to validate
#     if not Burger.validate_burger(request.form):
#         reutrn redirect('/')
#     # else no errors:
#     Burger.save(request.form)
#     return redirect("/burgers")

# ______________________________________________________________________________________

# Step 3: Displaying Flash Messages on the Template

# The last step is to get those flash messages onto the template! The http://flask.pocoo.org/docs/1.0/patterns/flashing/ (DOCUMENTATION) shows us how:

# {% with messages = get_flashed_messages() %}     <!-- declare a variable called messages -->
#     {% if messages %}                            <!-- check if there are any messages -->
#         {% for message in messages %}            <!-- loop through the messages -->
#             <p>{{message}}</p>                   <!-- display each message in a paragraph tag -->
#         {% endfor %}
#     {% endif %}
# {% endwith %}

# Congratulations! We have learned how to do basic validations.