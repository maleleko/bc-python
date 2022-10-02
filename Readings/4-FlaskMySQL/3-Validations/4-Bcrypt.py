#                                   Flask-Bcrypt


# With your pipenv environment activated (pipenv shell), run the following command:
    # pipenv install flask-bcrypt


# In your model file, add the following:
    # from flask_bcrypt import Bcrypt        
    # bcrypt = Bcrypt(app)    # we are creating an object called bcrypt, which is made by invoking the function Bcrypt with our app as an argument

# After making the object bcrypt, we have access to two methods that we will use to generate our password hashes and to compare passwords.
    # 1.) To generate a hash, provide the password to be hashed as an argument
        # bcrypt.generate_password_hash(password_string)

    # 2.) To compare passwords, provide the hash as the first argument and the password to be checked as the second argument
        # bcrypt.check_password_hash(hashed_password, password_string)


# Let's explore the generate_password_hash() method. If we pass it a string and print the result, we may see something like this:
    # $2b$12$sqjyok5RQccl9S6eFLhEPuaRaJCcH3Esl2RWLm/cimMIEnhnLb7iC

# We will store this string in our database, and there is a lot of information contained in it! Within the first set of $ signs, we have the Bcrypt ID (in this case, 2b). Between the next set of $ signs, the number 12 tells us how many rounds of hashing we did - this is what slows Bcrypt down. If you want it to take even longer, you may pass a larger value as a second argument - just for fun, try asking it to run 17 rounds! The next 22 characters is the salt (128 bits), and the rest is our 184-bit hash.

# Next, when we want to verify a user's password, we'll compare it with the hash we have associated with that user in the database. We pass both the hash and the provided password to check_password_hash(). Bcrypt extracts the salt from the hash and applies it to the provided password, hashes it, and compares the result to the saved hash. If they match, it returns True. If not, it returns False.


                    # Hashing Upon Registration
# Let's see how some of our code may look when we are creating a user. In the example below, we did not include validations, but of course you would validate the user input before adding it to the database.


# controllers/users.py
    # from flask_app import app
    # from flask_bcrypt import Bcrypt
    # bcrypt = Bcrypt(app)
    # @app.route('/register/user', methods=['POST'])
    # def register():
    #     # validate the form here ...
    #     # create the hash
    #     pw_hash = bcrypt.generate_password_hash(request.form['password'])
    #     print(pw_hash)
    #     # put the pw_hash into the data dictionary
    #     data = {
    #         "username": request.form['username'],
    #         "password" : pw_hash
    #     }
    #     # Call the save @classmethod on User
    #     user_id = User.save(data)
    #     # store user id into session
    #     session['user_id'] = user_id
    #     return redirect("/dashboard")

# models/user.py
    # class User:
    # @classmethod
    # def save(cls,data):
    #     query = "INSERT INTO users (username, password) VALUES (%(username)s, %(password)s);"
    #     return connectToMySQL("mydb").mysql.query_db(query, data)



                    # Comparing Upon Login

# Here's how our code may look when a user logs in. We'll need to check the provided password with the hash in the database:

# controllers/users.py
    # from flask_app import app
    # from flask_bcrypt import Bcrypt
    # bcrypt = Bcrypt(app)
    # @app.route('/login', methods=['POST'])
    # def login():
    #     # see if the username provided exists in the database
    #     data = { "email" : request.form["email"] }
    #     user_in_db = User.get_by_email(data)
    #     # user is not registered in the db
    #     if not user_in_db:
    #         flash("Invalid Email/Password")
    #         return redirect("/")
    #     if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
    #         # if we get False after checking the password
    #         flash("Invalid Email/Password")
    #         return redirect('/')
    #     # if the passwords matched, we set the user_id into session
    #     session['user_id'] = user_in_db.id
    #     # never render on a post!!!
    #     return redirect("/dashboard")


# models/user.py
# class User:
#     @classmethod
#     def get_by_email(cls,data):
#         query = "SELECT * FROM users WHERE email = %(email)s;"
#         result = connectToMySQL("mydb").query_db(query,data)
#         # Didn't find a matching user
#         if len(result) < 1:
#             return False
#         return cls(result[0])