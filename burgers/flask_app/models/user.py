from flask_app.config.mysqlconnection import connectToMySQL
# from pattern validation reading
import re	# the regex module
from flask import flash
# create a regular expression object that we'll use later
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    @staticmethod
    def validate_user(user):
        is_valid = True
        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email address!")
            # flash messages with categories
            flash("Email cannot be blank!", 'email')
            is_valid = False
        return is_valid

# from bcrypt reading
@classmethod
def save(cls,data):
    query = "INSERT INTO users (username, password) VALUES (%(username)s, %(password)s);"
    return connectToMySQL("mydb").mysql.query_db(query, data)


# from bcrypt reading
class User:
    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL("mydb").query_db(query,data)
        # Didn't find a matching user
        if len(result) < 1:
            return False
        return cls(result[0])