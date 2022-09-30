#                           PATTERN VALIDATION

# Another common validation that needs to be performed is checking whether an input matches a certain pattern. For example, email addresses have a particular pattern; passwords are often required to have a certain number of different types of characters. We can achieve this by using something known as a **regular expression** or **regex**. 

# A regex is a sequence of characters that defines a search pattern. It can be used to match a string that follows a pattern. For example, every email has a series of alphanumeric characters followed by an @ symbol followed by another series of alphanumeric characters followed by a "." and finally another series of alphanumeric characters. You don't need to know how to create regex at this point, but understanding what they are and what they are used for is definitely important. The Python regex for matching an email address based on the above criteria looks something like this (the preceding r indicates the string is a raw string, i.e. all characters should be taken literally):
        # r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$'

# The snippets below show the important additions to our models/user file:
# models/user.py

# import re	# the regex module
# # create a regular expression object that we'll use later
# EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# class User:
#     @staticmethod
#     def validate_user(user):
#         is_valid = True
#         # test whether a field matches the pattern
#         if not EMAIL_REGEX.match(user['email']):
#             flash("Invalid email address!")
#             is_valid = False
#         return is_valid

# The EMAIL_REGEX object has a method called .match() that will return None if no match can be found. If the argument matches the regular expression, a match object instance is returned.

# controllers/users.py

# from flask_app.models.user import User
# @app.route('/register', methods=['POST'])
# def register():
#     if not User.validate_user(request.form):
#         # we redirect to the template with the form.
#         return redirect('/')
#     # ... do other things
#     return redirect('/dashboard')


#           FLASH MESSAGES WITH CATEGORIES

# Say we want to categorize flash messages into different labels or buckets. We can utilize categories by passing a second argument in the flash function:
    # flash("Email cannot be blank!", 'email')

# Here's the documentation on flash messages with categories, where you can learn more about them, including how to display them on templates.
    # http://flask.pocoo.org/docs/1.0/patterns/flashing/#flashing-with-categories


#           OTHER USEFUL VALIDATION TOOLS:
    # str.isalpha() -- returns a boolean that shows whether a string contains only alphabetic characters
        # https://docs.python.org/3.6/library/stdtypes.html#str.isalpha

    # other string methods
        # https://docs.python.org/3.6/library/stdtypes.html#string-methods

    # time.strptime(string, format) -- changes a string to a time using the given format
        # https://docs.python.org/3.6/library/time.html#time.strptime