#                       Connecting to a Database



#1) We'll of course need a database to connect to.

# 2) In addition to the server.py file we make in each project, we'll now also need the following file

# first_flask_mysql/mysqlconnection.py

# # a cursor is the object we use to interact with the database
# import pymysql.cursors
# # this class will give us an instance of a connection to our database
# class MySQLConnection:
#     def __init__(self, db):
#         # change the user and password as needed
#         connection = pymysql.connect(host = 'localhost',
#                                     user = 'root', 
#                                     password = 'root', 
#                                     db = db,
#                                     charset = 'utf8mb4',
#                                     cursorclass = pymysql.cursors.DictCursor,
#                                     autocommit = True)
#         # establish the connection to the database
#         self.connection = connection
#     # the method to query the database
#     def query_db(self, query, data=None):
#         with self.connection.cursor() as cursor:
#             try:
#                 query = cursor.mogrify(query, data)
#                 print("Running Query:", query)

#                 cursor.execute(query, data)
#                 if query.lower().find("insert") >= 0:
#                     # INSERT queries will return the ID NUMBER of the row inserted
#                     self.connection.commit()
#                     return cursor.lastrowid
#                 elif query.lower().find("select") >= 0:
#                     # SELECT queries will return the data from the database as a LIST OF DICTIONARIES
#                     result = cursor.fetchall()
#                     return result
#                 else:
#                     # UPDATE and DELETE queries will return nothing
#                     self.connection.commit()
#             except Exception as e:
#                 # if the query fails the method will return FALSE
#                 print("Something went wrong", e)
#                 return False
#             finally:
#                 # close the connection
#                 self.connection.close() 
# # connectToMySQL receives the database we're using and uses it to create an instance of MySQLConnection
# def connectToMySQL(db):
#     return MySQLConnection(db)

    # At this time, you do not need to know how to create one of these files. By the end of the bootcamp, you will be experienced enough to create your own connection files!

    # While you don't have to understand everything 100%, you should know how to use the file and recognize the principles of OOP at work.
#         SELECT queries will return a list of dictionaries
        # INSERT queries will return the auto-generated id of the inserted row
        # UPDATE and DELETE queries will return nothing
        # If the query goes wrong, it will return False

# 3) Now we are gonna use OOP, and create a class that is modeled after our table in a file called friend.py.

# # import the function that will return an instance of a connection
# from mysqlconnection import connectToMySQL
# # model the class after the friend table from our database
# class Friend:
#     def __init__( self , data ):
#         self.id = data['id']
#         self.first_name = data['first_name']
#         self.last_name = data['last_name']
#         self.occupation = data['occupation']
#         self.created_at = data['created_at']
#         self.updated_at = data['updated_at']
#     # Now we use class methods to query our database
#     @classmethod
#     def get_all(cls):
#         query = "SELECT * FROM friends;"
#         # make sure to call the connectToMySQL function with the schema you are targeting.
#         results = connectToMySQL('first_flask').query_db(query)
#         # Create an empty list to append our instances of friends
#         friends = []
#         # Iterate over the db results and create instances of friends with cls.
#         for friend in results:
#             friends.append( cls(friend) )
#         return friends

    # Note: We will need to call on the connectToMySQL function every time we want to execute a query because our connection closes as soon as the query finishes executing.

    # 4) Now let's update our server.py file to import the class and call on the class method to query our database.
        # first_flask_mysql/server.py

    # from flask import Flask, render_template
    # # import the class from friend.py
    # from friend import Friend
    # app = Flask(__name__)
    # @app.route("/")
    # def index():
    #     # call the get all classmethod to get all friends
    #     friends = Friend.get_all()
    #     print(friends)
    #     return render_template("index.html")
                
    # if __name__ == "__main__":
    #     app.run(debug=True)

# 5) Run the server and see what gets printed in the terminal when you go to localhost:5000!